# step 1 prepare setpu.py file

After that, run 

`python setup.py sdist bdist_wheel`

under save folder

# step 2 prepare .pypirc file



# step 3 upload your file onto pypi

you will see dist folder under your home_folder,and then 

run

`twine upload --repository testpypi dist/*`

under save folder
