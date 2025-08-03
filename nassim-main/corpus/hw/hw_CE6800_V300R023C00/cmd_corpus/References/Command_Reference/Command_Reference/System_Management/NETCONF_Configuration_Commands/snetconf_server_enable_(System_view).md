snetconf server enable (System view)
====================================

snetconf server enable (System view)

Function
--------



The **snetconf server enable** command enables the SNETCONF service on the SSH server.

The **undo snetconf server enable** command disables the SNETCONF service on the SSH server.



By default, the SNETCONF is not enabled.


Format
------

**snetconf ipv4 server enable**

**snetconf ipv6 server enable**

**undo snetconf ipv4 server enable**

**undo snetconf ipv6 server enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ipv6** | Enables the IPv6 SNETCONF service. | - |
| **ipv4** | Enables the IPv4 SNETCONF service. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To control whether TCP port 22 can support the SNETCONF service, run this command.

* If you run the **snetconf server enable** command, TCP port 22 supports both IPv4 and IPv6 SNETCONF connections and provides SNETCONF services.
* If you run the **snetconf ipv4 server enable** command, TCP port 22 supports IPv4 SNETCONF connections and provides IPv4 SNETCONF services.
* If you run the **snetconf ipv6 server enable** command, TCP port 22 supports IPv6 SNETCONF connections and provides IPv6 SNETCONF services.
* If you run the **undo snetconf ipv4 server enable** command, TCP port 22 does not support SNETCONF connections or provide SNETCONF services.Note:After the SNETCONF service is disabled on the SSH server, all clients that log in to the server through TCP port 22 in SNETCONF mode are disconnected.


Example
-------

# Enable the SNETCONF service on the server.
```
<HUAWEI> system-view
[~HUAWEI] snetconf ipv4 server enable

```