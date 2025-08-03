display isis purge-source-trace analysis-report
===============================================

display isis purge-source-trace analysis-report

Function
--------



The **display isis purge-source-trace analysis-report** command displays information about definitely and possibly faulty nodes identified by IS-IS purge LSP source tracing.




Format
------

**display isis** [ *process-id* ] **purge-source-trace** **analysis-report** [ **level-1** | **level-2** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the ID of an IS-IS process. | The value is an integer ranging from 1 to 4294967295. |
| **level-1** | Displays information about definitely and possibly faulty Level-1 nodes identified by IS-IS purge LSP source tracing. | - |
| **level-2** | Displays information about definitely and possibly faulty Level-2 nodes identified by IS-IS purge LSP source tracing. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



To check information about definitely and possibly faulty nodes identified by IS-IS purge LSP source tracing, run the display isis purge-source-trace analysis-report command. The identified definitely and possibly faulty nodes are displayed in descending order in the command output, which helps maintenance personnel locate the faulty nodes and isolate them in time.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about definitely and possibly faulty nodes identified by IS-IS purge LSP source tracing.
```
<HUAWEI> display isis purge-source-trace analysis-report
Purge Source Analysis Report for ISIS(1)

                      Level-1 Analysis Report

Almost Purge Source  :1        Possible Purge Source  :0
Maybe Purge Source   :0        Not Purge Source       :3
Total                :4                            
 System Id           Host Name        PurgeSoure     IP(v6) Address
--------------------------------------------------------------------------------
0000.0000.0001                        almost         1.1.1.1
0000.0000.0002                        no             1.1.1.2
0000.0000.0003                        no             2.2.2.3
ffff.ad1c.eec4                        no             2.2.2.3

                      Level-2 Analysis Report

Almost Purge Source  :1        Possible Purge Source  :0  
Maybe Purge Source   :0        Not Purge Source       :3
Total                :4                            
 System Id           Host Name        PurgeSoure     IP(v6) Address
--------------------------------------------------------------------------------
0000.0000.0001                        almost         1.1.1.1
0000.0000.0002                        no             1.1.1.2
0000.0000.0003                        no             2.2.2.3
ffff.ad1c.eec4                        no             2.2.2.3

```

**Table 1** Description of the **display isis purge-source-trace analysis-report** command output
| Item | Description |
| --- | --- |
| Almost Purge Source | Number of definitely faulty nodes identified by IS-IS purge LSP source tracing. |
| Possible Purge Source | Number of possibly faulty nodes identified by IS-IS purge LSP source tracing. |
| Maybe Purge Source | Number of less possibly faulty nodes identified by IS-IS purge LSP source tracing. |
| Not Purge Source | Number of nodes that have been identified as faultless nodes by IS-IS purge LSP source tracing. |
| Total | Total number of faulty nodes identified by IS-IS purge LSP source tracing. |
| System Id | System ID. |
| Host Name | Dynamic hostname. |
| PurgeSoure | Analysis result by IS-IS purge LSP source tracing:   * almost: The node supports IS-IS purge LSP source tracing and has purged IS-IS LSPs advertised by other devices. In addition, the hwIsisDeleteRouteByPurge alarm is generated on the node. * possible: The node does not support IS-IS purge LSP source tracing, and its IS-IS LSPs have not been purged by other devices. * maybe: The node does not support IS-IS purge LSP source tracing, and some of its IS-IS LSPs have been purged by other devices. * no: The node supports IS-IS purge LSP source tracing, but the hwIsisDeleteRouteByPurge alarm is not generated on the node. |
| IP(v6) Address | IPv4 or IPv6 address. |