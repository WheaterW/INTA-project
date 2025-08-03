display said-node status
========================

display said-node status

Function
--------



The **display said-node status** command displays the status of an SAID node.




Format
------

**display said-node status** [ **slot** *slot-id* [ **cpu** *cpu-id* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Specifies a slot ID. | The value is a string of 1 to 49 case-sensitive characters. It cannot contain spaces. |
| **cpu** *cpu-id* | Specifies a CPU ID. | The value is a string of 1 to 49 case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run this command to view the status of an SAID node. The command output facilitates problem analysis and fault locating.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the status of an SAID node.
```
<HUAWEI> display said-node status
--------------------------------------------------------------------------------                                                    
SLOT  CPU  SAIDID  NAME                             TYPE         CYCLE(s)    STATUS       ENABLEFLAG RECOVERCNT LASTRECOVERTIME     
                                                                                                                                    
-------------------------------------------------------------------------------- 
                                                                                                                                    
1     0    1       said_ping                        common       300         init         enable     0          0000-00-00 00:00:00 
                                                                                                                                    
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display said-node status** command output
| Item | Description |
| --- | --- |
| SLOT | ID of the slot where a SAID node is deployed. |
| CPU | ID of the CPU where the SAID node is deployed. |
| SAIDID | ID of the SAID node. |
| NAME | Name of the SAID node. |
| TYPE | Type of the SAID node.   * common: MPU, which executes the node diagnosis function and can control non-MPU boards. * cooperation: Non-MPU board, which works with the MPU to execute the node diagnosis function. |
| STATUS | Status of the SAID node. |
| ENABLEFLAG | Whether a SAID node is enabled:   * enable: The current SAID node is enabled. * disable: The current SAID node is disabled. |
| RECOVERCNT | Recover times of a SAID node. |
| LASTRECOVERTIME | Time that a SAID node last recovers. |
| CYCLE | Checking cycle of the SAID node. |