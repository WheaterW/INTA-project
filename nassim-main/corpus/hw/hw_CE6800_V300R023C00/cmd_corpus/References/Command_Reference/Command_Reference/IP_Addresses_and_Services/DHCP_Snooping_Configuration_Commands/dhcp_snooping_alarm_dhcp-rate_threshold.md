dhcp snooping alarm dhcp-rate threshold
=======================================

dhcp snooping alarm dhcp-rate threshold

Function
--------



The **dhcp snooping alarm dhcp-rate threshold** command sets the alarm threshold for the number of discarded DHCP messages.

The **undo dhcp snooping alarm dhcp-rate threshold** command restores the default alarm threshold for the number of discarded DHCP messages.



By default, the alarm threshold for the number of discarded DHCP messages is 100.


Format
------

**dhcp snooping alarm dhcp-rate threshold** *threshold*

**undo dhcp snooping alarm dhcp-rate threshold**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **threshold** *threshold* | Specifies the alarm threshold. When the number of discarded DHCP messages reaches the threshold, an alarm is generated. | The value is an integer in the range from 1 to 1000. The default value is 100. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,VLAN view,Interface group view,System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After you run the **dhcp snooping alarm dhcp-rate enable** command to enable the device to generate an alarm when the number of discarded DHCP messages reaches the threshold, you can run the dhcp snooping alarm threshold command to set the alarm threshold. An alarm is generated when the number of discarded DHCP messages reaches the threshold.The configuration in the system view is used to check all packets on the device, the configuration in the interface view is used only for the interface, and the configuration in the VLAN view is used only for the VLAN. The configurations in the system view, interface view, and VLAN view are independent of each other.

**Prerequisites**

DHCP snooping has been enabled on the device using the **dhcp snooping enable** command.


Example
-------

# Set the alarm threshold for the rate of sending DHCP messages to 50 pps on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] dhcp snooping enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] dhcp snooping alarm dhcp-rate threshold 50

```