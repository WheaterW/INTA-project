dhcp snooping alarm enable
==========================

dhcp snooping alarm enable

Function
--------



The **dhcp snooping alarm enable** command enables the alarm function for DHCP snooping.

The **undo dhcp snooping alarm enable** command disables the alarm function for DHCP snooping.



By default, the alarm function is disabled for DHCP snooping.


Format
------

**dhcp snooping alarm** { **dhcp-request** | **dhcp-chaddr** | **dhcp-reply** } **enable**

**undo dhcp snooping alarm** { **dhcp-request** | **dhcp-chaddr** | **dhcp-reply** } **enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **dhcp-request** | Indicates that an alarm is generated when the number of DHCPv4 Request messages discarded because they do not match the binding entries reaches the threshold. | - |
| **dhcp-chaddr** | Indicates that an alarm is generated when the number of DHCPv4 Request messages discarded because the CHADDR field in the messages does not match the MAC address in the frame header reaches the alarm threshold. | - |
| **dhcp-reply** | Indicates that an alarm is generated when the number of DHCPv4 or DHCPv6 Reply messages discarded by untrusted interfaces from the server reaches the threshold. | - |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,VLAN view,Bridge domain view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After the alarm function is enabled, alarm messages are displayed if DHCP attacks occur and the number of discarded attack messages reaches the threshold. The minimum interval for sending alarm messages is 1 minute. The alarm threshold is set using the **dhcp snooping alarm threshold** command.

**Prerequisites**

DHCP snooping has been enabled on the device using the **dhcp snooping enable** command.By default, the device does not check the packets received from the client side. Therefore:· Before running the **dhcp snooping alarm dhcp-request enable** command, run the **dhcp snooping check dhcp-request enable** command to enable the device to check DHCP messages against the DHCP snooping binding table.· Before running the **dhcp snooping alarm dhcp-chaddr enable** command, run the **dhcp snooping check dhcp-chaddr enable** command to enable the device to check whether the CHADDR field value is the same as the source MAC address in the header of a DHCPv4 Request message.To ensure that alarms can be reported, run the **snmp-agent trap enable feature-name dhcp** command to enable the DHCP module to report alarms. You can run the **display snmp-agent trap feature-name dhcp all** command to check whether the alarm reporting function of the DHCP module is enabled.


Example
-------

# On 100GE1/0/1, enable DHCP snooping, dhcp-chaddr check, and alarm function for DHCP messages discarded by dhcp-chaddr check.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] dhcp snooping enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] dhcp snooping enable
[*HUAWEI-100GE1/0/1] dhcp snooping check dhcp-chaddr enable
[*HUAWEI-100GE1/0/1] dhcp snooping alarm dhcp-chaddr enable

```