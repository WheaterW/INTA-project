dhcp snooping check dhcp-giaddr enable
======================================

dhcp snooping check dhcp-giaddr enable

Function
--------



The **dhcp snooping check dhcp-giaddr enable** command enables the device to check whether the GIADDR field in a DHCP Request message is 0.

The **undo dhcp snooping check dhcp-giaddr enable** command disables the device from checking whether the GIADDR field in a DHCP Request message is 0.



By default, the device does not check whether the GIADDR field in a DHCP Request message is 0.


Format
------

**dhcp snooping check dhcp-giaddr enable**

**undo dhcp snooping check dhcp-giaddr enable**


Parameters
----------

None

Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,VLAN view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To ensure that the device can obtain user parameters such as MAC addresses when generating DHCP snooping binding entries, DHCP snooping needs to be applied to the access device or the first DHCP relay agent on the Layer 2 network. Therefore, the GIADDR field in the DHCP messages received by the DHCP snooping-enabled device must be 0. If the GIADDR field is not 0, the DHCP messages are invalid and need to be discarded. This function is recommended when DHCP snooping is enabled on the DHCP relay agent. Generally, the GIADDR field in DHCP messages sent by a PC is 0. In some cases, the GIADDR field in DHCP messages sent by a PC is not 0, which may cause the DHCP server to allocate an incorrect IP address. To prevent PC users from forging DHCP messages with non-0 GIADDR field to apply for IP addresses, you are advised to configure this function.

**Prerequisites**

DHCP snooping has been enabled on the device using the **dhcp snooping enable** command.

**Precautions**

If you run this command in the VLAN view, the command takes effect only for the DHCP messages in the VLAN. If you run this command in the interface view, the command takes effect for all DHCP messages on the interface.


Example
-------

# Enable the device to check whether the GIADDR field in DHCP messages received on 100GE1/0/1 is 0.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] dhcp snooping enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] dhcp snooping enable
[*HUAWEI-100GE1/0/1] dhcp snooping check dhcp-giaddr enable

```