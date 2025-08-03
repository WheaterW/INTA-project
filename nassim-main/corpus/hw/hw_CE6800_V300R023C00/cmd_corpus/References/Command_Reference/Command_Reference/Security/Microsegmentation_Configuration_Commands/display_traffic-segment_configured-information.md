display traffic-segment configured-information
==============================================

display traffic-segment configured-information

Function
--------



The **display traffic-segment configured-information** command displays the configuration of an EPG.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**display traffic-segment configured-information**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To view the configuration of an EPG, run the **display traffic-segment configured-information** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the EPG configuration.
```
<HUAWEI> display traffic-segment configured-information
--------------------------------------------------------------------------------
 Segment-Id      Segment-Name                    Member-Type        Member-Num
--------------------------------------------------------------------------------
        112      --                              IPv4                        1  
                                                 IPv6                        1  
        113      example_epg                     IPv4                        0  
                                                 IPv6                        2  
--------------------------------------------------------------------------------
Total: 2 Segment, 4 Member.

```

**Table 1** Description of the **display traffic-segment configured-information** command output
| Item | Description |
| --- | --- |
| Segment-Id | ID of an EPG. |
| Segment-Name | Name of an EPG. |
| Member-Type | Type of an EPG member. |
| Member-Num | Number of EPG members. |
| Total | Total number of existing EPGs and EPG members on the device. |