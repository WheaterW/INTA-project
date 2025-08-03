dhcp snooping check dhcp-rate enable
====================================

dhcp snooping check dhcp-rate enable

Function
--------



The **dhcp snooping check dhcp-rate enable** command enables the device to check the rate of sending DHCP messages to the processing unit.

The **undo dhcp snooping check dhcp-rate enable** command disables the device from checking the rate of sending DHCP messages to the processing unit.



By default, the function of checking the rate at which DHCP packets are sent to the processing unit is disabled.


Format
------

**dhcp snooping check dhcp-rate enable**

**undo dhcp snooping check dhcp-rate enable**


Parameters
----------

None

Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,VLAN view,Interface group view,System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After DHCP snooping is enabled, the device sends all the received DHCP Request messages and Reply messages to the processing unit. If the rate of sending DHCP messages is high, processing efficiency of the processing unit is affected. After the device is enabled to check the rate of sending DHCP messages to the processing unit, DHCP messages that exceed the specified rate are discarded. After the device is enabled to check the rate of sending DHCP messages to the processing unit, the maximum rate of sending DHCP messages is 5000 pps by default. To change the maximum rate, run the **dhcp snooping check dhcp-rate** command.The configuration in the system view is used to check all packets on the device, the configuration in the interface view is used only for the interface, and the configuration in the VLAN view is used only for the VLAN. The configurations in the system view, interface view, and VLAN view are independent of each other.

**Prerequisites**

DHCP snooping has been enabled on the device using the **dhcp snooping enable** command.


Example
-------

# In VLAN 10, enable the device to check the rate of sending DHCP packets to the processing unit.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] dhcp snooping enable
[*HUAWEI] vlan 10
[*HUAWEI-vlan10] dhcp snooping enable
[*HUAWEI-vlan10] dhcp snooping check dhcp-rate enable

```