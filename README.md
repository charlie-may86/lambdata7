# lambdata7
A collection of data-science utility functions

## Installation
Visit the website below to get the the install code
and more information
https://test.pypi.org/project/lambdata7/1.3/


The current install code is below
```py
pip install -i https://test.pypi.org/simple/ lambdata7==1.3
```
## Usage

```py
from ds_utilities import enlarge

print(enlarge(5))
```

## To Update
The process whenever you want to release a new version of your package to PyPI is something like:

1. make change and save file
2. revise version value in the setup.py file (for example from 1.0 to 1.1, or from 1.1 to 1.2) and save the file
3. make a commit
4. run the bdist_wheel command to package your code

```py
python setup.py sdist bdist_wheel
```

5. run the twine command to upload the packaged code
```py
twine upload --skip-existing --repository-url https://test.pypi.org/legacy/ dist/*
```
