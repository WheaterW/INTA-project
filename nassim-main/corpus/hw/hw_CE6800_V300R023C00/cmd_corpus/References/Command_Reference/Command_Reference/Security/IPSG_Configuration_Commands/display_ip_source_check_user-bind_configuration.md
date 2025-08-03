display ip source check user-bind configuration
===============================================

display ip source check user-bind configuration

Function
--------



The **display ip source check user-bind configuration** command displays the configuration of IP packet checking.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ip source check user-bind configuration** [ **vlan** [ *vlan-id* ] | **interface** [ *interface-name* | *interface-type* *interface-number* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vlan** *vlan-id* | Displays the configuration of IP packet checking in a specified VLAN. | The value is an integer ranging from 1 to 4094. |
| **interface** *interface-name* | Specifies an interface name. | - |
| **interface** *interface-type* *interface-number* | Displays the configuration of IP packet checking on a specified interface. The interface is specified by the interface type and number.   * interface-type. * interface-number. | The value is a string of 1 to 64 case-sensitive characters without spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run this command to view the configuration of IP packet checking on an interface, including the check items and alarm function for IP packet checking.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display configurations of IP packet checking.
```
<HUAWEI> display ip source check user-bind configuration
-----------------------------------------------------------------------                                                             
Interface            Vlan   Check-item         Alarm    Alarm-threshold                                                             
-----------------------------------------------------------------------                                                             
Eth-Trunk1           -      IP|MAC|VLAN        Disable  -                                                                          
-----------------------------------------------------------------------

```

**Table 1** Description of the **display ip source check user-bind configuration** command output
| Item | Description |
| --- | --- |
| Interface | Interface on which IP packet checking is enabled. |
| Vlan | VLAN on which IP packet checking is enabled. |
| Check-item | Check items of IP packets.  The options include IP, MAC, VLAN, and Interface. |
| Alarm | Whether the alarm function for checking IP packets is enabled:   * Enable: indicates that the alarm function is enabled. * Disable: indicates that the alarm function is disabled.   To enable the alarm function for checking IP packets, run the ip source check user-bind alarm enable command. |
| Alarm-threshold | Alarm threshold for IP packet check. To configure this parameter, run the ip source check user-bind alarm threshold command. |