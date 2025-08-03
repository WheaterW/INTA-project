mac-address learning disable (VLAN view)
========================================

mac-address learning disable (VLAN view)

Function
--------



The **mac-address learning disable** command disables MAC address learning.

The **undo mac-address learning disable** command restores MAC address learning.



By default, MAC address learning is enabled.


Format
------

**mac-address learning disable**

**undo mac-address learning disable**


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



If a network is stable, MAC address learning can be disabled on an interface or in a VLAN to save space of the MAC address table.After MAC address learning is disabled on an interface or in a VLAN using the **mac-address learning disable** command, the device will not learn new MAC addresses from this interface, Bridge Domain (BD) or the interfaces in this VLAN.After MAC address learning is enabled, a device can receive Ethernet frames from other devices, parse the source MAC address of each frame, locate the interface that receives each frame, and add new entries to the MAC address table. After that, when receiving an Ethernet frame destined for the MAC address contained in the MAC address table, the device can search the MAC address table to locate the corresponding outbound interface. This reduces broadcast traffic.




Example
-------

# Disable MAC address learning in VLAN 2.
```
<HUAWEI> system-view
[~HUAWEI] vlan 2
[*HUAWEI-vlan2] mac-address learning disable

```