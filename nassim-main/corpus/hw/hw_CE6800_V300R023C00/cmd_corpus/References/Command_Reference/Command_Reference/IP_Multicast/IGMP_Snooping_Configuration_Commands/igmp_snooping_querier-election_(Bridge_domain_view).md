igmp snooping querier-election (Bridge domain view)
===================================================

igmp snooping querier-election (Bridge domain view)

Function
--------



The **igmp snooping querier-election** command configures the querier election.

The **undo igmp snooping querier-election** command cancels the querier election.



By default, the querier election function is disabled for all BDs.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**igmp snooping querier-election**

**undo igmp snooping querier-election**


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

If the querier function is enabled on multiple devices in a BD, the **igmp snooping querier-election** command can be used to elect the device with the lowest IP address as the querier. Then the device replaces the connected upstream device to send Query messages to user hosts. You can run the **igmp snooping send-query source-address** command to configure a source IP address to be carried by an IGMP Query message. By default, the source IP address carried by an IGMP Query message is 192.168.0.1.

**Prerequisites**

The **igmp snooping querier enable** command has been run to enable the querier function in the BD.


Example
-------

# Enable the querier election function for BD 10.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable
[*HUAWEI] bridge-domain 10
[*HUAWEI-bd10] igmp snooping querier-election

```