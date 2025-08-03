cdup
====

cdup

Function
--------



The **cdup** command changes the remote working directory to one level upper directory or parent directory.




Format
------

**cdup**


Parameters
----------

None

Views
-----

FTP client view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The cdup command simplifies the changing of the directory in different operating systems.

**Precautions**

The permission to change the working directory depends on whether the FTP user has the permission to access the directory.


Example
-------

# Change the working directory to one level upper directory.
```
<HUAWEI> ftp 1.1.1.1
[ftp] cdup

```