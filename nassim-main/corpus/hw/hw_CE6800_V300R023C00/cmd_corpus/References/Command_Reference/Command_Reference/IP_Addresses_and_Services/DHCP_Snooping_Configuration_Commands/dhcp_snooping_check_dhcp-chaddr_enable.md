dhcp snooping check dhcp-chaddr enable
======================================

dhcp snooping check dhcp-chaddr enable

Function
--------



The **dhcp snooping check dhcp-chaddr enable** command enables the device to check whether the CHADDR field matches the source MAC address in the header of a DHCP Request message.

The **undo dhcp snooping check dhcp-chaddr enable** command disables the device from checking whether the CHADDR field matches the source MAC address in the header of a DHCP Request message.



By default, the device does not check whether the CHADDR field matches the source MAC address in the header of a DHCP Request message.


Format
------

**dhcp snooping check dhcp-chaddr enable**

**undo dhcp snooping check dhcp-chaddr enable**


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

In normal situations, the CHADDR field in a DHCP Request message is the same as the MAC address of the client that sends the message. The DHCP server identifies the client MAC address based on the CHADDR field. If attackers continuously apply for IP addresses by changing the CHADDR field in the DHCP Request message, addresses in the address pool on the DHCP server will be exhausted. As a result, authorized users cannot obtain IP addresses.

**Prerequisites**

DHCP snooping has been enabled on the device using the **dhcp snooping enable** command.

**Precautions**

If you run this command in the VLAN view, the command takes effect for the DHCP messages of the specified VLAN on all device interfaces. If you run this command in the interface view, the command takes effect for all the DHCP messages received on the interface.


Example
-------

# Enable the device to check whether the CHADDR field matches the source MAC address in the header of a DHCP Request message on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] dhcp snooping enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] dhcp snooping enable
[*HUAWEI-100GE1/0/1] dhcp snooping check dhcp-chaddr enable

```