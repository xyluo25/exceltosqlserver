import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="exceltosqlserver", # Replace with your own username
    version="0.0.1",
    author="Xiangyong Luo",
    author_email="rochemay@163.com",
    description="This package help to convert your excel files (xlsx,xls,csv) to SQL Server database.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Xiangyongluo/exceltosqlserver",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)