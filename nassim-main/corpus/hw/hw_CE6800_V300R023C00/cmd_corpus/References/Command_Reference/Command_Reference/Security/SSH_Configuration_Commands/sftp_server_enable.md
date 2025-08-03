sftp server enable
==================

sftp server enable

Function
--------



The **sftp server enable** command enables the SFTP service on the SSH server.

The **undo sftp server enable** command disables the SFTP service on the SSH server.



By default, the SFTP service is not enabled on the SSH server.


Format
------

**sftp server enable**

**undo sftp server enable**


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

To enable TCP port 22 to support the SFTP service, run this command. A client can connect to the SSH server through SFTP only after the SFTP service is enabled on the SSH server.The **sftp server enable** command enables the SFTP service on the SSH server.

**Precautions**

After you disable the SFTP service on the SSH server, all the clients that connect to the SSH server through SFTP are disconnected.This command applies to both IPv4 and IPv6 services.


Example
-------

# Enable the SFTP service on the SFTP server.
```
<HUAWEI> system-view
[~HUAWEI] sftp server enable

```