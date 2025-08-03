igmp snooping proxy router-protocol-pass
========================================

igmp snooping proxy router-protocol-pass

Function
--------



The **igmp snooping proxy router-protocol-pass** command configures transparent transmission of IGMP Report, IGMP Leave, Group-Specific Query, and Group-and-Source-Specific Query messages.

The **undo igmp snooping proxy router-protocol-pass** command disables the device from transparently transmitting IGMP Report, IGMP Leave, Group-Specific Query, and Group-and-Source-Specific Query messages.



By default, a device enabled with IGMP snooping proxy terminates received Report messages, Leave messages, Group-Specific Query messages, and Group-and-Source-Specific Query messages.


Format
------

**igmp snooping proxy router-protocol-pass**

**undo igmp snooping proxy router-protocol-pass**


Parameters
----------

None

Views
-----

VLAN range view,VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If IGMP snooping proxy is enabled on the upstream and downstream devices, the upstream and downstream devices learn the same multicast forwarding entries. In addition, the upstream and downstream devices continuously send IGMP Query and Report messages to each other, and multicast entries will never be aged out. As a result, multicast protocol messages and data flows are forwarded meaninglessly on the network. After this command is run, the device does not accept IGMP Report messages, IGMP Leave messages, Group-Specific Query messages, or Group-and-Source-Specific Query messages. Instead, the device transparently transmits protocol messages received from a router port to other router ports.You are advised to run this command on a dual-homing network where IGMP snooping proxy is enabled.

**Prerequisites**

The **igmp snooping proxy** command has been run to enable IGMP Snooping Proxy in a VLAN.

**Configuration Impact**

After this command is run successfully, IGMP snooping proxy changes the behavior of processing IGMP Report messages, IGMP Leave messages, Group-Specific Query messages, and Group-and-Source-Specific Query messages on router ports. The device does not terminate the protocol messages received from the router port but forwards the protocol messages to the upstream device.


Example
-------

# Configure router ports in VLAN 10 to transparently transmit protocol messages.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable
[~HUAWEI] vlan 10
[*HUAWEI-vlan10] igmp snooping proxy router-protocol-pass

```