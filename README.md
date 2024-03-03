# Introduction

This package help to convert your excel files (xlsx,xls,csv) to SQL Server database.

# Installation

exceltosqlserver can be installed as:

```python
pip install exceltosqlserver
```

# Dependency

👍   [pandas](https://pandas.pydata.org/)

👍   [pyodbc](https://github.com/mkleehammer/pyodbc)

👍   [sqlalchemy](https://www.sqlalchemy.org/)

# QuickStart

```python
from exceltosqlserver import ExcelToDB, hostname, local_ip

# STEP One, prepare your input pareameters

yourFile  = "test01.xls"  # available for xlsx, xls,csv
yourUsrID = ""
yourPWD   = ""
yourDBname= ""
rename_table = ""  # Use your filename as tablename onto SQL Server or user define the table name, e.g. :"test"

# get your local host name
# this will return your local computer name for your sql server database
host_name = hostname

# get your local ip address
# this will return your local ip address (if your sql server can be accessed by DNS)
ip = local_ip

# you need to change your host if needed, dns: local ip address
#yourHostORip  = "localhost"
# yourHostORip  = host_name
yourHostORip  = ip


# STEP Two add your data to sql server
es = ExcelToDB(yourFile, yourHostORip, yourUsrID, yourPWD, yourDBname, rename_table)
es.save2db()

```

```python
output:
Successfully load excel data...
Sucessfully connected to SQL Server...
Sucessfully saved 'yourtable' to SQL Server...
```

# API Reference

exceltosqlserver.ExcelToDB(`filePath,host_ip=False,usrID =False,pwd=False,db_name=False,rename_table`)

filePath: str

host_ip: str  default: ""

usrID: str  default: ""

pwd: str   default: ""

db_name: str  default: ""

rename_table: str   default: "", will auto save your filename as table name  to sql  server database. If assignmed value, will change table name from your filename to the assigned value.
