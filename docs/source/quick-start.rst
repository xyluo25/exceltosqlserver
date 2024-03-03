===========
Quick Start
===========

In this section, some examples are provided to quickly show how to use exceltosqlserver.


Simple Example
==============

.. code-block:: python

    from exceltosqlserver import ExcelToDB, hostname, local_ip

    # Step 1, prepare your input parameters

    yourFile  = "test01.xls"  # available for xlsx, xls,csv
    yourUsrID = ""
    yourPWD   = ""
    yourDBname= ""
    rename_table = ""  # Use your filename as table name to MySQL Server or user define their preferred table name. e.g. : "test"

    # get your local host name
    # this will return your local computer name for your MySQL server database
    host_name = hostname

    # get your local ip address
    # this will return your local ip address (if your sql server can be accessed by DNS)
    IP = local_ip
    yourHostOrIP  = "localhost"   # you need to change your host if needed, dns: local ip address

    # Step 2, save your data onto MySQL
    ex = ExcelToDB(yourFile, yourHoseOrIP, yourUsrID, yourPWD, yourDBname, rename_table)
    ex.save2db()


    # output:
    # Successfully load excel data...
    # Secessfully connected to SQL Server...
    # Secessfully saved 'yourtable' to SQL Server...


