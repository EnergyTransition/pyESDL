#!/usr/bin/env bash
set -euo pipefail

cd -- "$(dirname -- "${BASH_SOURCE[0]}")"

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

status=0
results=()
for version in 3.10 3.11 3.12 3.13 3.14; do
  printf '\nTesting Python %s\n' "$version"
  if uv run --isolated --no-project \
    --python "$version" \
    --with-requirements requirements.txt \
    --with setuptools --with wheel --with versioneer \
    --with twine --with future-fstrings \
    python -m pytest tests; then
    results+=("Python $version: PASS")
  else
    exit_code=$?
    results+=("Python $version: FAIL (exit $exit_code)")
    status=1
  fi
done

printf '\n%s\n' 'Test matrix results'
printf '%s\n' "${results[@]}"
exit "$status"
