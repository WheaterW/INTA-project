mac-address learning disable (NVE interface view)
=================================================

mac-address learning disable (NVE interface view)

Function
--------



The **mac-address learning disable** command disables MAC address learning.

The **undo mac-address learning disable** command restores MAC address learning.



By default, MAC address learning is enabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mac-address learning disable**

**undo mac-address learning disable**


Parameters
----------

None

Views
-----

NVE interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



If a network is stable, MAC address learning can be disabled on an interface or in a VLAN to save space of the MAC address table.After MAC address learning is disabled on an interface or in a VLAN using the **mac-address learning disable** command, the device will not learn new MAC addresses from this interface, Bridge Domain (BD) or the interfaces in this VLAN.After MAC address learning is enabled, a device can receive Ethernet frames from other devices, parse the source MAC address of each frame, locate the interface that receives each frame, and add new entries to the MAC address table. After that, when receiving an Ethernet frame destined for the MAC address contained in the MAC address table, the device can search the MAC address table to locate the corresponding outbound interface. This reduces broadcast traffic.




Example
-------

# Disable MAC address learning in NVE1.
```
<HUAWEI> system-view
[~HUAWEI] interface nve 1
[*HUAWEI-Nve1] mac-address learning disable

```