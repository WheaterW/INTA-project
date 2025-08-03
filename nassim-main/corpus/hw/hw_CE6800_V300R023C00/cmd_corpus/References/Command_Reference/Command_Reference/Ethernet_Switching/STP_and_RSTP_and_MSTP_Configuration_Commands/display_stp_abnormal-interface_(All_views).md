display stp abnormal-interface (All views)
==========================================

display stp abnormal-interface (All views)

Function
--------



The **display stp abnormal-interface** command displays information about abnormal interfaces running the Spanning Tree Protocol (STP).




Format
------

**display stp** [ **instance** *instance-id* ] **abnormal-interface**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **instance** *instance-id* | Displays the status of and statistics about a spanning tree instance.  If instance <instance-id> is not specified, the status of and statistics about all spanning tree instances will be displayed in the sequence of the interface numbers. | The value is an integer ranging from 0 to 4094, Value 0 indicates CIST. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



If a device has many interfaces, querying information about abnormal STP interfaces by running the **display stp** command takes a long time.To shorten the time, run the display stp abnormal-interface command.



**Precautions**



If you run this command in the MSTP process view without specifying an MSTP process, information about the MSTP process in this view is displayed by default. If you run this command in other views without specifying the ID of an MSTP process, information about MSTP process 0 is displayed by default. If you specify the ID of an MSTP process, information about the MSTP process with the specified ID is displayed.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about abnormal STP interfaces in instance 0.
```
<HUAWEI> display stp instance 0 abnormal-interface
MSTID    Interface                     Status          Reason                   
    0    100GE1/0/1                    discarding      loop-protected           
    0    100GE1/0/2                    down            bpdu-protected           
    0    100GE1/0/3                    discarding      root-protected           
    0    100GE1/0/4                    discarding      loop-detected

```

**Table 1** Description of the **display stp abnormal-interface (All views)** command output
| Item | Description |
| --- | --- |
| MSTID | MSTP instance ID. |
| Interface | Interface type. |
| Status | Status of an interface after the STP protection takes effect:   * down: The physical status of the interface is Down (including error-down). * discarding: The interface is blocked after the topology of the spanning tree becomes stable. |
| Reason | An STP interface becomes abnormal due to one of the following:   * root-protected: The root protection takes effect. * loop-protected: The loop protection takes effect. * bpdu-protected: The bridge protocol data unit (BPDU) protection takes effect. * loop-detected: The ring detection takes effect. |