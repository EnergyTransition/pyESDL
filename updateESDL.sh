#!/usr/bin/env bash
set -e

cd "$(dirname "$0")"

curl --fail --location https://raw.githubusercontent.com/EnergyTransition/ESDL/master/esdl/model/esdl.ecore -o esdl/esdl.ecore
pyecoregen -e esdl/esdl.ecore -o . --auto-register-package
