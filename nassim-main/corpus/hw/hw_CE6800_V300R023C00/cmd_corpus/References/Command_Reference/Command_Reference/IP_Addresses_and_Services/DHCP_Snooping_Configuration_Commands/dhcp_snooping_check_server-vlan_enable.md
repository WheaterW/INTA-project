dhcp snooping check server-vlan enable
======================================

dhcp snooping check server-vlan enable

Function
--------



The **dhcp snooping check server-vlan enable** command enables a DHCP snooping-enabled device to check VLAN information in DHCP reply messages.

The **undo dhcp snooping check server-vlan enable** command disables a DHCP snooping-enabled device from checking VLAN information in DHCP reply messages.



By default, the DHCP snooping-enabled device does not check VLAN information in DHCP reply messages.


Format
------

**dhcp snooping check server-vlan enable**

**undo dhcp snooping check server-vlan enable**


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

By default, a DHCP snooping-enabled device checks DHCP reply messages based only on MAC addresses for server identification. If the device cannot identify servers based only on MAC addresses, run the **dhcp snooping check server-vlan enable** command. After the command is run, the DHCP snooping-enabled device checks DHCPv4 or DHCPv6 reply messages based on both MAC addresses and VLAN information for server identification.

**Prerequisites**

DHCP snooping has been enabled on the device using the **dhcp snooping enable** command.DHCP server detection has been enabled using the **dhcp snooping server record** command.


Example
-------

# Enable the DHCP snooping-enabled device to check VLAN information in DHCP reply messages.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] dhcp snooping enable
[*HUAWEI] dhcp snooping server record
[*HUAWEI] dhcp snooping check server-vlan enable

```