display mice-elephant-flow flow-cache resource
==============================================

display mice-elephant-flow flow-cache resource

Function
--------



The **display mice-elephant-flow flow-cache resource** command displays hardware flow table resource information for differentiated flow scheduling.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display mice-elephant-flow flow-cache resource** [ **slot** *slot-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Specifies the slot ID. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run this command to view detailed information about hardware flow table resource usage for differentiated flow scheduling in real time.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display hardware flow table resource information for differentiated flow scheduling.
```
<HUAWEI> display mice-elephant-flow flow-cache resource slot 1
Slot: 1
---------------------------------------------
TotalNum          UsedNum       FreeNum      
---------------------------------------------
   16384             4000         12384
---------------------------------------------

```

**Table 1** Description of the **display mice-elephant-flow flow-cache resource** command output
| Item | Description |
| --- | --- |
| TotalNum | Total number of resources. |
| UsedNum | Number of resources in use. |
| FreeNum | Number of idle resources. |
| Slot | Slot ID. |