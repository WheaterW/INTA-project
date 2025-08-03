dhcp snooping check dhcp-rate
=============================

dhcp snooping check dhcp-rate

Function
--------



The **dhcp snooping check dhcp-rate** command sets the maximum rate of sending DHCP messages to the processing unit.

The **undo dhcp snooping check dhcp-rate** command restores the default maximum rate of sending DHCP messages to the processing unit.



By default, the maximum rate of sending DHCP messages to the processing unit is 5000 pps.


Format
------

**dhcp snooping check dhcp-rate** *rate*

**undo dhcp snooping check dhcp-rate**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **dhcp-rate** *rate* | Specifies the maximum rate of sending DHCP messages to the processing unit. | The value is an integer ranging from 1 to 5000, in pps. The default value is 5000. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,VLAN view,Interface group view,System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After DHCP snooping is enabled, the device sends all the received DHCP Request messages and Reply messages to the processing unit. If the rate of sending DHCP messages is high, processing efficiency of the processing unit is affected. After the device is enabled to check the rate of sending DHCP messages to the processing unit, you can run the dhcp snooping check dhcp-rate command to set the maximum rate of sending DHCP messages to the processing unit. After the rate of sending DHCP messages to the processing unit exceeds the maximum rate, excess DHCP messages are discarded.The configuration in the system view is used to check all packets on the device, the configuration in the interface view is used only for the interface, and the configuration in the VLAN view is used only for the VLAN. The configurations in the system view, interface view, and VLAN view are independent of each other.

**Prerequisites**

Before configuring the maximum rate of sending DHCP messages to the processing unit, ensure that the function of checking the rate of sending DHCP messages to the processing unit has been enabled using the **dhcp snooping check dhcp-rate enable** command. Otherwise, the configuration does not take effect.


Example
-------

# In the VLAN view, set the maximum rate of sending DHCP messages to the processing unit to 50 pps.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] dhcp snooping enable
[*HUAWEI] vlan 10
[*HUAWEI-vlan10] dhcp snooping enable
[*HUAWEI-vlan10] dhcp snooping check dhcp-rate enable
[*HUAWEI-vlan10] dhcp snooping check dhcp-rate 50

```