display stp abnormal-interface
==============================

display stp abnormal-interface

Function
--------



The **display stp abnormal-interface** command displays information about abnormal interfaces running the Spanning Tree Protocol (STP) in a Multiple Spanning Tree Protocol (MSTP) process.




Format
------

**display stp** [ **instance** *instance-id* ] **abnormal-interface**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **instance** *instance-id* | Displays the status of and statistics about a specified spanning tree instance.  If instance <instance-id> is not specified, the status of and statistics about all spanning tree instances will be displayed in the sequence of the interface numbers. | The value is an integer ranging from 0 to 4094, Value 0 indicates CIST. |



Views
-----

MSTP process view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



If a device has many interfaces, querying information about abnormal STP interfaces by running the **display stp** command takes a long time.To shorten the time, run the display stp abnormal-interface command.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about abnormal STP interfaces of MSTP process 1.
```
<HUAWEI> system-view
[~HUAWEI] stp process 1
[*HUAWEI-mst-process-1] display stp instance 0 abnormal-interface
MSTID    Interface                     Status          Reason                   
    0    100GE1/0/1                    discarding      loop-protected           
    0    100GE1/0/2                    down            bpdu-protected           
    0    100GE1/0/3                    discarding      root-protected           
    0    100GE1/0/4                    discarding      loop-detected

```

**Table 1** Description of the **display stp abnormal-interface** command output
| Item | Description |
| --- | --- |
| MSTID | ID of an MSTP instance. |
| Interface | Interface type. |
| Status | Status of an interface after STP protection takes effect:   * DOWN: indicates that the physical status of the interface is Down (including error-down). * DISCARDING: indicates the blocked interface after the topology of the spanning tree becomes stable. |
| Reason | Spanning tree protection type of the abnormal port:   * Root-Protected: Root protection takes effect. * Loop-Protected: Loop protection takes effect. * BPDU-Protected: BPDU protection takes effect. * Loop-Detected: Loop detection takes effect. |