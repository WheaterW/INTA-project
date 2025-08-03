arp delete trigger link-down enable
===================================

arp delete trigger link-down enable

Function
--------



The **arp delete trigger link-down enable** command enables the device to delete ARP entries learned by an interface immediately after the interface link goes Down.

The **undo arp delete trigger link-down enable** command restores the default setting.



By default, the device is disabled from deleting ARP entries learned by an interface immediately after the interface link goes Down.


Format
------

**arp delete trigger link-down enable**

**undo arp delete trigger link-down enable**


Parameters
----------

None

Views
-----

VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



By default, when a member interface of a VLAN goes Down, the device deletes the ARP entries learned by the member interface only after detecting that they are aged in an ARP probe. The device then updates routing entries. This processing mechanism may delay link switchover in an ECMP scenario.Run the arp delete trigger link-down enable command to enable the device to delete ARP entries learned by a member interface of a VLAN immediately after the interface link goes Down without waiting for the ARP aging probe result.




Example
-------

# Enable the device to delete ARP entries learned by an interface immediately after the interface link goes Down.
```
<HUAWEI> system-view
[~HUAWEI] interface Vlanif 10
[*HUAWEI-Vlanif10] arp delete trigger link-down enable

```