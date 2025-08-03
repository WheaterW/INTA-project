display traffic-segment statistics
==================================

display traffic-segment statistics

Function
--------



The **display traffic-segment statistics** command displays microsegmentation group statistics.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**display traffic-segment statistics** { **segment-id** *id-value* | **segment-name** *name* } **slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **segment-id** *id-value* | Microsegmentation ID. | The value is an integer ranging from 1 to 65535. |
| **segment-name** *name* | Specifies a microsegmentation name. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |
| **slot** *slot-id* | Specifies the slot ID. | The value is a string of characters. The value is a slot ID. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check EPG statistics, run the **display traffic-segment statistics** command. The command output helps you determine whether EPGs are proper and diagnose faults.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about microsegmentation groups.
```
<HUAWEI> display traffic-segment statistics segment-id 1 slot  1
-----------------------------------------------------------------------------------------------------------------                   
Traffic Segment ID: 1, Name: --                                                                                                     
-----------------------------------------------------------------------------------------------------------------                   
Segment Member                              VPN-Instance                      Source Packets       Destination Packets                   
-----------------------------------------------------------------------------------------------------------------                   
1.1.1.0/24                                  --                                             0                    0                   
1.1.1.0/24                                  _management_vpn_                               0                    0                   
2.2.2.0/24                                  --                                             0                    0                   
2001:db8:1::1/64                            --                                             0                    0                   
2001:db8:1::2/128                             --                                             0                    0                   
-----------------------------------------------------------------------------------------------------------------                   
Total:                                                                                     0                    0                   
-----------------------------------------------------------------------------------------------------------------

```

**Table 1** Description of the **display traffic-segment statistics** command output
| Item | Description |
| --- | --- |
| Traffic Segment ID | ID of an EPG. |
| Segment Member | Microsegmentation group member. |
| VPN-Instance | Name of a VPN instance. |
| Source Packets | Number of packets sent by members in an EPG. |
| Destination Packets | Number of packets received by members in an EPG. |
| Name | Name of an EPG. |
| Total | Total count. |