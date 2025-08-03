protocol inbound ssh port 830
=============================

protocol inbound ssh port 830

Function
--------



The **protocol inbound ssh port 830** command configures well-known port 830 to establish an SNETCONF connection.

The **undo protocol inbound ssh port 830** command restores the default setting.



By default, SNETCONF connections are established using well-known port 22.


Format
------

**protocol inbound ssh port 830**

**undo protocol inbound ssh port 830**


Parameters
----------

None

Views
-----

NETCONF user interface view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



The **protocol inbound ssh port 830** command specifies well-known port 830 as the SNETCONF port.When you run the **protocol inbound ssh port 830** command, the SNETCONF server automatically monitors port 830. You do not need to manually change the monitoring port number.




Example
-------

# Configure well-known port 830 to establish SNETCONF connections.
```
<HUAWEI> system-view
[~HUAWEI] netconf
[~HUAWEI-netconf] protocol inbound ssh port 830

```