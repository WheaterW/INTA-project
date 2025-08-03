display stp tc-bpdu statistics (All views)
==========================================

display stp tc-bpdu statistics (All views)

Function
--------



The **display stp tc-bpdu statistics** command displays statistics about sent and received topology change (TC) and topology change notification (TCN) BPDUs on interfaces.




Format
------

**display stp** [ **instance** *instance-id* ] [ **interface** { *interface-name* | *interface-type* *interface-number* } | **slot** *slot-id* ] **tc-bpdu** **statistics** [ **history** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **instance** *instance-id* | Specifies the ID of an MSTP instance.  If instance <instanceId> is not specified, statistics about TC and TCN BPDUs on all interfaces are displayed in the sequence of the interface numbers. | The value is an integer ranging from 0 to 4094, Value 0 indicates CIST. |
| **interface** *interface-type* *interface-number* | Displays information of a spanning tree on a specified interface.  If interface <ifType> <ifNum> is not specified, the status of and statistics about all interfaces will be displayed in the sequence of the interface numbers. | - |
| **slot** *slot-id* | Specifies the number of a slot of which statistics about TC and TCN BPDUs are displayed. | The value is a string of 1 to 23 case-sensitive characters, spaces not supported. |
| **history** | Displays historical TC/TCN statistics on an interface. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



To determine whether a fault has occurred on interfaces that send and receive TC/TCN BPDUs, run display stp tc-bpdu statistics command to view statistics about sent and received BPDUs. The command output helps you locate the fault.



**Precautions**



If you run this command in the MSTP process view without specifying an MSTP process, information about the MSTP process in this view is displayed by default. If you run this command in other views without specifying the ID of an MSTP process, information about MSTP process 0 is displayed by default. If you specify the ID of an MSTP process, information about the MSTP process with the specified ID is displayed.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about sent and received TC/TCN BPDUs on interfaces of an MSTP instance.
```
<HUAWEI> display stp tc-bpdu statistics
-------------------------- STP TC/TCN information--------------------------
 MSTID Port                        TC(Send/Receive)      TCN(Send/Receive)
 0     100GE1/0/1                  3/2                   0/0 
 0     100GE1/0/2                  1/0                   0/0 
 1     100GE1/0/3                  14/9                  -/-  
 1     100GE1/0/4                  8/10                  -/-  
 2     100GE1/0/5                  3/2                   -/-  
 2     100GE1/0/1                  1/0                   -/-

```

**Table 1** Description of the **display stp tc-bpdu statistics (All views)** command output
| Item | Description |
| --- | --- |
| MSTID | MSTP instance ID. |
| Port | Interface name. |
| TC(Send/Receive) | Statistics of sent and received TC BPDUs. |
| TCN(Send/Receive) | Statistics of sent and received TCN BPDUs. ("-" indicates that MSTP instances except MSTP instance 0 do not have TCN BPDUs sent and received.). |