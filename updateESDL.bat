@echo off
cd /d "%~dp0"
if errorlevel 1 exit /b 1

curl --fail --location https://raw.githubusercontent.com/EnergyTransition/ESDL/master/esdl/model/esdl.ecore -o esdl\esdl.ecore
if errorlevel 1 exit /b 1

pyecoregen -e esdl\esdl.ecore -o . --auto-register-package