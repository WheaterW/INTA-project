dhcp snooping alarm threshold
=============================

dhcp snooping alarm threshold

Function
--------



The **dhcp snooping alarm threshold** command sets the alarm threshold for the number of DHCP messages discarded by DHCP snooping.

The **undo dhcp snooping alarm threshold** command restores the default alarm threshold.



By default, the alarm threshold for the number of messages discarded by DHCP snooping is the value configured using the dhcp snooping alarm threshold command in the system view.


Format
------

**dhcp snooping alarm** { **dhcp-request** | **dhcp-chaddr** | **dhcp-reply** } **threshold** *threshold*

**undo dhcp snooping alarm** { **dhcp-request** | **dhcp-chaddr** | **dhcp-reply** } **threshold**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **dhcp-request** | Specifies the alarm threshold for the number of DHCPv4 Request messages discarded because they do not match the binding entries. | - |
| **dhcp-chaddr** | Specifies the alarm threshold for the number of DHCP messages discarded because the CHADDR field in the DHCPv4 Request message does not match the MAC address in the data frame header. | - |
| **dhcp-reply** | Specifies the alarm threshold for the number of DHCPv4 or DHCPv6 Reply messages discarded by untrusted interfaces from the server. | - |
| *threshold* | Specifies the alarm threshold for the number of DHCP messages discarded by DHCP snooping. | The value is an integer ranging from 1 to 1000, in seconds. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,VLAN view,Bridge domain view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After the DHCP snooping alarm function is enabled, you can run the **dhcp snooping alarm threshold** command to set the alarm threshold for the number of discarded DHCPv4 and DHCPv6 messages.

**Prerequisites**

DHCP snooping has been enabled on the device using the **dhcp snooping enable** command. The DHCP snooping alarm function has been enabled using the **dhcp snooping alarm { dhcp-request | dhcp-chaddr | dhcp-reply } enable** command.

**Precautions**

If no alarm threshold is configured in the interface view, VLAN view, or BD view, the global alarm threshold is used.If you run this command in the system view, the command takes effect on all the interfaces of the device.If the alarm threshold for the number of DHCP messages discarded by DHCP snooping is configured in the system view, an alarm is generated when the number of all types of DHCP messages discarded by DHCP snooping reaches the threshold.To ensure that alarms can be reported, run the **snmp-agent trap enable feature-name dhcp** command to enable the DHCP module to report alarms. You can run the **display snmp-agent trap feature-name dhcp all** command to check whether the alarm reporting function of the DHCP module is enabled.


Example
-------

# On 100GE1/0/1, enable DHCP snooping and DHCP CHADDR check, configure the alarm function for DHCP messages discarded because of DHCP CHADDR check failures, and set the alarm threshold to 1000.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] dhcp snooping enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] dhcp snooping enable
[*HUAWEI-100GE1/0/1] dhcp snooping check dhcp-chaddr enable
[*HUAWEI-100GE1/0/1] dhcp snooping alarm dhcp-chaddr enable
[*HUAWEI-100GE1/0/1] dhcp snooping alarm dhcp-chaddr threshold 1000

```