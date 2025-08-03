sftp server enable (System view)
================================

sftp server enable (System view)

Function
--------



The **sftp server enable** command enables the SFTP service on the SSH server.

The **undo sftp server enable** command disables the SFTP service on the SSH server.



By default, the SFTP service is not enabled on the SSH server.


Format
------

**sftp ipv4 server enable**

**sftp ipv6 server enable**

**undo sftp ipv4 server enable**

**undo sftp ipv6 server enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ipv6** | Enables the IPv6 SFTP service. | - |
| **ipv4** | Enables the IPv4 SFTP service. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

* To enable TCP port 22 to support the SFTP service, run this command. A client can connect to the SSH server through SFTP only after the SFTP service is enabled on the SSH server.
* The **sftp ipv4 server enable** command enables the IPv4 SFTP service on the SSH server. The **sftp ipv6 server enable** command enables the IPv6 SFTP service on the SSH server.
* After you disable the SFTP service on the SSH server, all the clients that connect to the SSH server through SFTP are disconnected.


Example
-------

# Enable the IPv4 SFTP service on the SFTP server.
```
<HUAWEI> system-view
[~HUAWEI] sftp ipv4 server enable

```