# HeatMatcher

This python code base is a re-implementation of the Java-based HeatMatcher

## Installing
use the following command to install the HeatMatcher python module from the CI PyPi registry:

`pip install HeatMatcher --extra-index-url https://__token__:<your_personal_token>@ci.tno.nl/gitlab/api/v4/projects/7530/packages/pypi/simple`

## Releasing a new version
1. Do a `git tag` with the new version number
2. Do `python setup.py sdist bdist_wheel` to create the tarball and wheel in the `dist` folder
3. Create a .pypirc with the following content:
    ```
    [distutils]
    index-servers = gitlab
    
    [gitlab]
    repository = https://ci.tno.nl/api/v4/projects/7530/packages/pypi
    username = __token__
    password = <your personal access token>
    ```  
    and replace password with the personal access token in gitlab (See User->Settings). 
`7530` is the project ID for the HeatMatcher project.

4. Issue `python -m twine upload --repository gitlab dist/*` to push it to the PyPi repo in gitlab

##### TODO: make releasing part of CI/CD

