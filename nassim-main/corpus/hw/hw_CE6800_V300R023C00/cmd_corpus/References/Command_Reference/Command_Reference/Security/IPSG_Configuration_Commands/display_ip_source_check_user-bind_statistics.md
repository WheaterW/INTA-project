display ip source check user-bind statistics
============================================

display ip source check user-bind statistics

Function
--------



The **display ip source check user-bind statistics** command displays statistics about packets discarded by IP source guard.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ip source check user-bind statistics** [ **vlan** [ *vlan-id* ] | **interface** [ *interface-name* | *interface-type* *interface-number* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vlan** *vlan-id* | Displays binding entries mapping a specified VLAN ID. | The value is an integer ranging from 1 to 4094. |
| **interface** *interface-name* | Specifies an interface name. | - |
| **interface** *interface-type* *interface-number* | Displays binding entries mapping a specified interface:   * interface-type. * interface-number. | The value is a string of 1 to 64 case-sensitive characters without spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run this command to view statistics on the packets discarded by IPSG, including the total number of discarded packets and the number of discarded packets after the last alarm is generated.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics on discarded IPSG packets.
```
<HUAWEI> display ip source check user-bind statistics
--------------------------------------------------------------------------------------------------                                  
Type            View                 Alarm     Discarded                     Discarded After Alarm                                  
--------------------------------------------------------------------------------------------------                                  
Interface       10GE1/0/1            Enable    60183                         60183                                                  
--------------------------------------------------------------------------------------------------

```

**Table 1** Description of the **display ip source check user-bind statistics** command output
| Item | Description |
| --- | --- |
| Type | Type of the view where IPSG is enabled. |
| View | Name of the view in which IPSG is enabled. |
| Alarm | Whether the alarm function is enabled.   * Enable. * Disable. |
| Discarded | Number of discarded packets on the interface. |
| Discarded After Alarm | Number of packets discarded on the interface after the last alarm is generated. |