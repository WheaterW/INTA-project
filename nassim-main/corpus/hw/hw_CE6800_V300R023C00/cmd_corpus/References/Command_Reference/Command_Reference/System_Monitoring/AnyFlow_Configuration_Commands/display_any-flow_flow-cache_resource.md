display any-flow flow-cache resource
====================================

display any-flow flow-cache resource

Function
--------



The **display any-flow flow-cache resource** command displays resource information in the hardware flow table.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**display any-flow flow-cache resource** [ **slot** *slot-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Specifies the slot ID. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

You can use the display any-flow flow-cache resource command to view resource usage details in the hardware flow table.

**Precautions**

One IPv6 flow entry occupies two hardware resources, and one IPv4 flow entry occupies one hardware resource.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display resource usage details in the hardware flow table.
```
<HUAWEI> display any-flow flow-cache resource slot 1
Slot: 1                                                                                                                             
--------------------------------------------------------------                                                                      
FlowType         TotalNum          UsedNum       FreeNum                                                                            
--------------------------------------------------------------                                                                      
IPv4             15360             12            15348                                                                              
IPv6             7680              0             7680                                                                               
--------------------------------------------------------------

```

**Table 1** Description of the **display any-flow flow-cache resource** command output
| Item | Description |
| --- | --- |
| FlowType | Flow type. |
| TotalNum | Total number of resources. |
| UsedNum | Number of resources in use. |
| FreeNum | Number of idle resources. |
| Slot | slot-id. |