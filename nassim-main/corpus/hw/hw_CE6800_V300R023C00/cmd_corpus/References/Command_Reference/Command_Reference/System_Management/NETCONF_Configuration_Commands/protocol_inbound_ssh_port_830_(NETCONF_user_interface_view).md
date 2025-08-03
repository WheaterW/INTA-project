protocol inbound ssh port 830 (NETCONF user interface view)
===========================================================

protocol inbound ssh port 830 (NETCONF user interface view)

Function
--------



The **protocol inbound ssh port 830** command configures well-known port 830 to establish an SNETCONF connection.

The **undo protocol inbound ssh port 830** command restores the default setting.



By default, SNETCONF connections are established using well-known port 22.


Format
------

**protocol inbound ssh ipv4 port 830**

**protocol inbound ssh ipv6 port 830**

**undo protocol inbound ssh ipv4 port 830**

**undo protocol inbound ssh ipv6 port 830**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ipv6** | Specifies IPv6. | - |
| **ipv4** | Specifies IPv4. | - |



Views
-----

NETCONF user interface view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to set the SNETCONF port number to 830.

* When you run the **protocol inbound ssh ipv4 port 830** command, the SNETCONF server automatically listens to IPv4 port 830.
* When you run the **protocol inbound ssh ipv6 port 830** command, the SNETCONF server automatically listens to IPv6 port 830.


Example
-------

# Configure well-known port 830 to establish SNETCONF connections.
```
<HUAWEI> system-view
[~HUAWEI] netconf
[~HUAWEI-netconf] protocol inbound ssh ipv4 port 830

```