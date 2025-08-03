ftp client resumable-transfer enable
====================================

ftp client resumable-transfer enable

Function
--------



The **ftp client resumable-transfer enable** command enables the resumable transfer function on the FTP client.

The **undo ftp client resumable-transfer enable** command disables the resumable transfer function on the FTP client.



By default, the resumable transfer service of FTP client is disabled.


Format
------

**ftp client resumable-transfer enable**

**undo ftp client resumable-transfer enable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to enable the resumable file transfer service on the FTP client to implement resumable file transfer.


Example
-------

# Enable the resumable transfer service of FTP client.
```
<HUAWEI> system-view
[~HUAWEI] ftp client resumable-transfer enable

```