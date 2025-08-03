dhcp snooping alarm dhcp-rate enable
====================================

dhcp snooping alarm dhcp-rate enable

Function
--------



The **dhcp snooping alarm dhcp-rate enable** command enables the device to generate an alarm when the number of discarded DHCP messages reaches the threshold.

The **undo dhcp snooping alarm dhcp-rate enable** command disables the device from generating an alarm when the number of discarded DHCP messages reaches the threshold.



By default, the device is disabled from generating an alarm when the number of discarded DHCP messages reaches the threshold.


Format
------

**dhcp snooping alarm dhcp-rate enable**

**undo dhcp snooping alarm dhcp-rate enable**


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

After DHCP snooping is enabled, the device sends all the received DHCP Request messages and Reply messages to the processing unit. If the rate of sending DHCP messages is high, processing efficiency of the processing unit is affected. After you run the **dhcp snooping check dhcp-rate enable** command to enable the device to check the rate of sending DHCP messages to the processing unit, the device checks the rate of sending DHCP messages. Only the DHCP messages whose rate is within the specified rate are sent to the processing unit, and the DHCP messages whose rate exceeds the specified rate are discarded.If the number of discarded DHCP messages reaches the threshold, an alarm is generated. The alarm threshold can be configured using the **dhcp snooping alarm dhcp-rate threshold** command.The configuration in the system view is used to check all packets on the device, the configuration in the interface view is used only for the interface, and the configuration in the VLAN view is used only for the VLAN. The configurations in the system view, interface view, and VLAN view are independent of each other.

**Prerequisites**

DHCP snooping has been enabled on the device using the **dhcp snooping enable** command.

**Precautions**

To ensure that alarms can be reported, run the **snmp-agent trap enable feature-name dhcp** command to enable the DHCP module to report alarms. You can run the **display snmp-agent trap feature-name dhcp all** command to check whether the alarm reporting function of the DHCP module is enabled.


Example
-------

# Enable the device to generate an alarm when the number of discarded DHCP messages reaches the threshold on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] dhcp snooping enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] dhcp snooping check dhcp-rate enable
[*HUAWEI-100GE1/0/1] dhcp snooping alarm dhcp-rate enable

```

# In the system view, enable the device to generate an alarm when the number of discarded DHCP messages reaches the threshold.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] dhcp snooping enable
[*HUAWEI] dhcp snooping check dhcp-rate enable
[*HUAWEI] dhcp snooping alarm dhcp-rate enable

```