dhcp snooping user-offline remove mac-address
=============================================

dhcp snooping user-offline remove mac-address

Function
--------



The **dhcp snooping user-offline remove mac-address** command enables the device to delete the MAC address entry of a user whose DHCP snooping binding entry is deleted.

The **undo dhcp snooping user-offline remove mac-address** command disables the device from deleting the MAC address entry of a user whose binding entry is deleted.



By default, the device does not delete the MAC address entry of a user whose DHCP snooping entry is deleted.


Format
------

**dhcp snooping user-offline remove mac-address**

**undo dhcp snooping user-offline remove mac-address**


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

If a user goes offline but its MAC address entry is not aged, the device forwards the DHCPv4 and DHCPv6 packets whose destination address is the IP address of the user based on the dynamic MAC address entry. After the **dhcp snooping user-offline remove mac-address** command is run, the user MAC address entry is deleted when the DHCP snooping binding entry is deleted. In addition, the device discards packets destined for offline users when the network-side interface is configured to discard unknown unicast packets.

**Prerequisites**

DHCP snooping has been enabled on the device using the **dhcp snooping enable** command.

**Precautions**

The deleted MAC address entries include the secure dynamic MAC addresses learned after the **port-security enable** command is run.


Example
-------

# Enable the device to delete the MAC address entry of a user whose DHCP snooping binding entry is deleted.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] dhcp snooping enable
[*HUAWEI] dhcp snooping user-offline remove mac-address

```