igmp snooping proxy router-protocol-pass (Bridge domain view)
=============================================================

igmp snooping proxy router-protocol-pass (Bridge domain view)

Function
--------



The **igmp snooping proxy router-protocol-pass** command configures transparent transmission of IGMP Report, IGMP Leave, Group-Specific Query, and Group-and-Source-Specific Query messages.

The **undo igmp snooping proxy router-protocol-pass** command disables the device from transparently transmitting IGMP Report, IGMP Leave, Group-Specific Query, and Group-and-Source-Specific Query messages.



By default, a device enabled with IGMP snooping proxy terminates received Report messages, Leave messages, Group-Specific Query messages, and Group-and-Source-Specific Query messages.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**igmp snooping proxy router-protocol-pass**

**undo igmp snooping proxy router-protocol-pass**


Parameters
----------

None

Views
-----

Bridge domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If IGMP snooping proxy is enabled on the upstream and downstream devices, the upstream and downstream devices learn the same multicast forwarding entries. In addition, the upstream and downstream devices continuously send IGMP Query and Report messages to each other, and multicast entries will never be aged out. As a result, multicast protocol messages and data flows are forwarded meaninglessly on the network. After this command is run, the device does not accept IGMP Report messages, IGMP Leave messages, Group-Specific Query messages, or Group-and-Source-Specific Query messages. Instead, the device transparently transmits protocol messages received from a router port to other router ports.You are advised to run this command on a dual-homing network where IGMP snooping proxy is enabled.

**Prerequisites**

The **igmp snooping proxy** command has been run to enable IGMP Snooping Proxy in a BD.

**Configuration Impact**

After this command is run successfully, IGMP snooping proxy changes the behavior of processing IGMP Report messages, IGMP Leave messages, Group-Specific Query messages, and Group-and-Source-Specific Query messages on router ports. The device does not terminate the protocol messages received from the router port but forwards the protocol messages to the upstream device.


Example
-------

# Configure router ports in BD 10 to transparently transmit protocol messages.
```
<HUAWEI> system-view
[~HUAWEI] bridge-domain 10
[*HUAWEI-bd10] undo igmp snooping proxy router-protocol-pass

```