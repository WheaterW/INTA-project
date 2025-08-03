dhcp snooping check dhcp-request enable
=======================================

dhcp snooping check dhcp-request enable

Function
--------



The **dhcp snooping check dhcp-request enable** command enables the device to check DHCP messages against the DHCP snooping binding table.

The **undo dhcp snooping check dhcp-request enable** command disables the device from checking DHCP messages against the DHCP snooping binding table.



By default, the device does not check DHCP messages against the DHCP snooping binding table.


Format
------

**dhcp snooping check dhcp-request enable**

**undo dhcp snooping check dhcp-request enable**


Parameters
----------

None

Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,VLAN view,Bridge domain view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After a dynamic binding table is generated, the device checks DHCPv4 Request or Release messages against the dynamic binding table. The device forwards only the messages that match the dynamic binding table. Otherwise, the device discards the messages. This effectively prevents unauthorized users from sending bogus DHCP messages to pretend to be authorized users to renew or release IP addresses.The device checks DHCPv4 Request or Release messages against dynamic binding entries based on the following rules:· For DHCPv4 Request messages:

1. The device checks whether the CIADDR field in the DHCPv4 Request message is 0. If the CIADDR field is 0, the DHCPv4 Request message is sent for the first login and is allowed to pass through. If the CIADDR field is not 0, the DHCPv4 Request message is sent for lease renewal and is checked against the dynamic binding table.
2. The device checks whether the CHADDR field in the message matches an entry in the dynamic binding table. If not, the device considers that the user goes online for the first time and allows the message to pass through. If the CHADDR field matches an entry in the dynamic binding table, the device checks whether the VLAN ID, client IP address, and interface information in the message match an entry in the dynamic binding table. If yes, the device forwards the message. If no, the device discards the message.· After receiving a DHCPv4 Release/Inform/Decline message, the device checks whether the CHADDR field in the message matches an entry in the binding table. If not, the device forwards the message. If a binding entry is matched, the device checks whether the VLAN ID, client IP address, and interface information in the message match the binding table. If yes, the device forwards the message. If no, the device discards the message.

**Prerequisites**

DHCP snooping has been enabled on the device using the **dhcp snooping enable** command.

**Precautions**

If you run this command in the VLAN view, the command takes effect for the DHCP messages of the specified VLAN on all device interfaces. If you run this command in the interface view, the command takes effect for all the DHCP messages received on the interface.


Example
-------

# Enable the device to check DHCP messages against the DHCP snooping binding table in VLAN 10.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] dhcp snooping enable
[*HUAWEI] vlan 10
[*HUAWEI-vlan10] dhcp snooping enable
[*HUAWEI-vlan10] dhcp snooping check dhcp-request enable

```