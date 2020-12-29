import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
try:
    # if have requirements.txt file inside the folder
    with open("requirements.txt", "r", encoding="utf-8") as f:
        modules_needed = [i.strip() for i in fh.readlines()]   
except:
    modules_needed = []

setuptools.setup(
    name="exceltosqlserver", # Replace with your own username
    version="0.1.2",
    author="Xiangyong Luo",
    author_email="rochemay@163.com",
    description="This package help to convert your excel files (xlsx,xls,csv) to SQL Server database.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Xiangyongluo/exceltosqlserver",
    
    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    
    install_requires=modules_needed,
    packages=setuptools.find_packages(),
    include_package_data=True,

    package_data= {'':['*.txt','*.xls','*.xlsx','*.csv'],
                   "test_data":['*.txt']}
)


