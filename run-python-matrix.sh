#!/usr/bin/env bash
set -euo pipefail

if [[ "${1:-}" == --test ]]; then
  test_args=(tests)
  case "${PYESDL_TEST_EXTRA:-all}" in
    core)
      test_args+=(--ignore=tests/geometry --ignore=tests/profiles)
      ;;
    profiles)
      test_args+=(--ignore=tests/geometry)
      ;;
    geometry)
      test_args+=(--ignore=tests/profiles)
      ;;
    all)
      ;;
    *)
      printf 'Unknown test extra: %s\n' "$PYESDL_TEST_EXTRA" >&2
      exit 2
      ;;
  esac
  exec python -m pytest "${test_args[@]}"
fi

cd -- "$(dirname -- "${BASH_SOURCE[0]}")"
matrix_script="$PWD/run-python-matrix.sh"

docker compose up -d --wait

export PYESDL_POSTGRES_HOST=localhost
export PYESDL_POSTGRES_PORT="${POSTGRES_PORT:-1432}"
export PYESDL_POSTGRES_USER="${POSTGRES_DB_USER:-postgres}"
export PYESDL_POSTGRES_PASSWORD="${POSTGRES_DB_PASSWD:-password}"
export PYESDL_POSTGRES_PROFILE_DB=timeseries_profile
export PYESDL_INFLUXDB_HOST=localhost
export PYESDL_INFLUXDB_PORT="${INFLUXDB_PORT:-1086}"
export PYESDL_INFLUXDB_USER=admin
export PYESDL_INFLUXDB_PASSWORD=admin

test_dir=$(mktemp -d)
trap 'rm -rf -- "$test_dir"' EXIT
uv run --isolated --no-project --python 3.10 --with build==1.2.2.post1 \
  python -m build --outdir "$test_dir/dist"
set -- "$test_dir"/dist/*.whl
wheel=$1
cp -r tests setup.cfg "$test_dir/"
cd -- "$test_dir"
unset PYTHONPATH

status=0
results=()
for version in 3.10 3.11 3.12 3.13 3.14; do
  for extra in core profiles geometry all; do
    printf '\nTesting Python %s (%s)\n' "$version" "$extra"
    requirement=$wheel
    if [[ "$extra" != core ]]; then
      requirement="${wheel}[$extra]"
    fi
    export PYESDL_TEST_EXTRA="$extra"
    if uv run --isolated --no-project \
      --python "$version" \
      --with pytest --with "$requirement" \
      bash "$matrix_script" --test; then
      results+=("Python $version ($extra): PASS")
    else
      exit_code=$?
      results+=("Python $version ($extra): FAIL (exit $exit_code)")
      status=1
    fi
  done
done

printf '\n%s\n' 'Test matrix results'
printf '%s\n' "${results[@]}"
exit "$status"
