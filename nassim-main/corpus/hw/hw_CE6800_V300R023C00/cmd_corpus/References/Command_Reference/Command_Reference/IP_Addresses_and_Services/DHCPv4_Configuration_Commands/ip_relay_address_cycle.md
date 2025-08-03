ip relay address cycle
======================

ip relay address cycle

Function
--------



The **ip relay address cycle** command enables the DHCP server polling function on a DHCP relay agent.

The **undo ip relay address cycle** command disables the DHCP server polling function on a DHCP relay agent.



By default, DHCP server polling is disabled on a DHCP relay agent.


Format
------

**ip relay address cycle**

**undo ip relay address cycle**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

This command applies to DHCP relay agents. When multiple DHCP server addresses are configured on a DHCP relay agent, the DHCP relay agent forwards DHCP Discover messages to all servers by default. As a result, DHCP servers need to process a large number of messages, leading to heavy loads of servers. To solve this problem, configure the **ip relay address cycle** command. After this command is configured, the DHCP relay agent forwards a received DHCP Discover message to one DHCP server at a time, and forwards the DHCP Discover message to a different DHCP server each time it receives the message. Multiple DHCP servers then can allocate the same number of IP addresses, implementing load balancing among DHCP servers.

**Prerequisites**

DHCP has been enabled globally using the dhcp enable command.


Example
-------

# Enable DHCP server polling on the switch in the system view.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] ip relay address cycle

```