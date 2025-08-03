display adaptive-routing notification statistics
================================================

display adaptive-routing notification statistics

Function
--------



The **display adaptive-routing notification statistics** command displays the statistics on ARN messages for congestion and congestion relief notification sent and received on an interface where adaptive routing is enabled.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**display adaptive-routing notification statistics** [ **interface** { *interface-name* | *interface-type* *interface-number* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-name* | Specifies the name of an interface. | - |
| **interface** *interface-type* *interface-number* | Specifies the interface type and interface number. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After the adaptive routing function is enabled on a device, you can run this command to view statistics on ARN messages about congestion and congestion relief sent and received on a specified interface.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics on ARN messages about congestion and congestion relief sent and received on a specified interface.
```
<HUAWEI> display adaptive-routing notification statistics interface 100GE1/0/2
CN-Count: Congestion Notification Count 
CRN-Count: Congestion Release Notification Count 
----------------------------------------------- 
Interface    CN-Count(tx/rx)  CRN-Count(tx/rx)  
-----------------------------------------------  
100GE1/0/2    100/0            2/0 
-----------------------------------------------

```

**Table 1** Description of the **display adaptive-routing notification statistics**  command output
| Item | Description |
| --- | --- |
| Interface | Name of an interface. |
| CN-Count(tx/rx) | Number of sent and received ARN messages about congestion. (Number of sent messages/Number of received messages). |
| CRN-Count(tx/rx) | Number of sent and received ARN messages about congestion relief (Number of sent messages/Number of received messages). |