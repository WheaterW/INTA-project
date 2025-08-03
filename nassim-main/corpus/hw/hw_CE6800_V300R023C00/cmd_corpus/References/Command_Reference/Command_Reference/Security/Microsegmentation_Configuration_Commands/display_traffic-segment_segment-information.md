display traffic-segment segment-information
===========================================

display traffic-segment segment-information

Function
--------



The **display traffic-segment segment-information** command displays information about a specified EPG.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**display traffic-segment segment-information** { **segment-id** *id-value* | **segment-name** *name* } **slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **segment-id** *id-value* | Specifies the microsegmentation group ID. | The value is an integer ranging from 1 to 65535. |
| **segment-name** *name* | Specifies a microsegmentation name. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. It must start with a letter. |
| **slot** *slot-id* | Specifies the slot ID. | The value is a string of characters. The value is a slot ID. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To view information about a specified EPG, run the **display traffic-segment segment-information** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about EPG 123.
```
<HUAWEI> display traffic-segment segment-information segment-id 1 slot 1
-------------------------------------------------------------------------------------------                                         
Segment ID: 1,   Segment Name: --                                                                                                   
-------------------------------------------------------------------------------------------                                         
Segment Member                                VPN-Instance                     Status                                               
-------------------------------------------------------------------------------------------                                         
1.1.1.0/24                                    --                               Success                                                 
2001:db8:1::1/64                              --                               Success                                                 
-------------------------------------------------------------------------------------------                                         
Total: 2

```

**Table 1** Description of the **display traffic-segment segment-information** command output
| Item | Description |
| --- | --- |
| Segment ID | ID of an EPG. |
| Segment Name | Name of an EPG. |
| Segment Member | IP address and mask length of an EPG member. |
| VPN-Instance | Name of the VPN instance corresponding to an EPG member. |
| Status | Status of delivering EPG member information to the chip.   * Success: The group member information is successfully delivered. * Fail: The group member information fails to be delivered. |
| Total | Total number of group members. |