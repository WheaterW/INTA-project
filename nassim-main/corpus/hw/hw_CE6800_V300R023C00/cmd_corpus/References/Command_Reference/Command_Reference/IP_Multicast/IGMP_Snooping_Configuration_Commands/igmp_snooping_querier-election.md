igmp snooping querier-election
==============================

igmp snooping querier-election

Function
--------



The **igmp snooping querier-election** command configures the querier election.

The **undo igmp snooping querier-election** command cancels the querier election.



By default, the querier election function is disabled for all VLANs.


Format
------

**igmp snooping querier-election**

**undo igmp snooping querier-election**


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

If the querier function is enabled on multiple devices in a VLAN, the **igmp snooping querier-election** command can be used to elect the device with the lowest IP address as the querier. Then the device replaces the connected upstream device to send Query messages to user hosts. You can run the **igmp snooping send-query source-address** command to configure a source IP address to be carried by an IGMP Query message. By default, the source IP address carried by an IGMP Query message is 192.168.0.1.

**Prerequisites**

The **igmp snooping querier enable** command has been run to enable the querier function in the VLAN.


Example
-------

# Enable the querier election function for VLAN 10.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable
[*HUAWEI] vlan 10
[*HUAWEI-vlan10] igmp snooping querier-election

```