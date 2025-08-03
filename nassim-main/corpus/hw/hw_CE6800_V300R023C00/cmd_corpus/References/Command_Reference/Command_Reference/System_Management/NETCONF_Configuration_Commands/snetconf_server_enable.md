snetconf server enable
======================

snetconf server enable

Function
--------



The **snetconf server enable** command enables the SNETCONF service on the SSH server.

The **undo snetconf server enable** command disables the SNETCONF service on the SSH server.



By default, the SNETCONF is not enabled.


Format
------

**snetconf server enable**

**undo snetconf server enable**


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

To enable the SNETCONF service on the SSH server, run the **snetconf server enable** command.

* If you run the **snetconf server enable** command, TCP port 22 supports both IPv4 and IPv6 SNETCONF connections and provides the SNETCONF service.
* If you run the **snetconf ipv4 server enable** command, TCP port 22 supports IPv4 SNETCONF connections and provides the IPv4 SNETCONF service.
* If you run the **snetconf ipv6 server enable** command, TCP port 22 supports IPv6 SNETCONF connections and provides the IPv6 SNETCONF service.
* If you run the **undo snetconf server enable** command, TCP port 22 does not support SNETCONF connections or provide the SNETCONF service.Note:After you disable the SNETCONF service on the SSH server, all the clients that connect to the SSH server through TCP port 22 in SNETCONF mode are disconnected.


Example
-------

# Enable the SNETCONF service on the server.
```
<HUAWEI> system-view
[~HUAWEI] snetconf server enable

```