dhcp anti-attack check udp-checksum
===================================

dhcp anti-attack check udp-checksum

Function
--------



The **dhcp anti-attack check udp-checksum** command enables the function of checking the UDP header checksum in a DHCP packet and discarding a DHCP packet with an incorrect checksum.

The **undo dhcp anti-attack check udp-checksum** command disables the function of checking the UDP header checksum in a DHCP packet.



By default, a device checks the UDP header checksum in a DHCP packet and discards a DHCP packet with an incorrect checksum.


Format
------

**dhcp anti-attack check udp-checksum**

**undo dhcp anti-attack check udp-checksum**


Parameters
----------

None

Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VLAN view,Interface group view,Management interface view,System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Devices from different vendors may use different DHCP implementation mechanisms. After checking the UDP header checksum in a received DHCP packet, a device may not allow the DHCP packet to pass through and discards the packet. As a result, DHCP becomes unavailable. To solve this problem, you can run the undo dhcp anti-attack check udp-checksum command to disable the function of checking the UDP header checksum in a DHCP packet, so that a DHCP packet with an incorrect UDP header checksum can be properly forwarded.The function of checking the UDP header checksum in a DHCP packet is disabled only if the function is disabled globally, on an interface, or in a VLAN.

**Prerequisites**

DHCP has been enabled on the device using the **dhcp enable** command.


Example
-------

# Disable the function of checking the UDP header checksum in a DHCP packet.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] undo dhcp anti-attack check udp-checksum

```