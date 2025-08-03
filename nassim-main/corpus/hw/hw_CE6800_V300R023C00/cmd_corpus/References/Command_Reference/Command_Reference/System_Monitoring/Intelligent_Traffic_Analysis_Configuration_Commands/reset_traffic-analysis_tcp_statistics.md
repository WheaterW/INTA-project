reset traffic-analysis tcp statistics
=====================================

reset traffic-analysis tcp statistics

Function
--------



The **reset traffic-analysis tcp statistics** command clears statistics about TCP flows involved in the intelligent traffic analysis function.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**reset traffic-analysis tcp statistics** [ **slot** *slot-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | ID of an available slot. | The value is a string of 1 to 15 case-sensitive characters, spaces not supported. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

Statistics about TCP/UDP flows within a specified period may be required for troubleshooting. Before collecting statistics about TCP/UDP flows, you can run this command to clear historical TCP/UDP flow statistics.

**Precautions**

The **reset traffic-analysis tcp statistics** command clears all TCP flow statistics involved in the intelligent traffic analysis function. The statistics cannot be restored after being cleared. Therefore, exercise caution when running this command.The **reset traffic-analysis tcp statistics** command can be run multiple times at any interval.When this command is executed, the data of current will not be clear.


Example
-------

# Clear statistics about TCP flows involved in the intelligent traffic analysis function on the device.
```
<HUAWEI> reset traffic-analysis tcp statistics

```