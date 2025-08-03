display info-center statistics
==============================

display info-center statistics

Function
--------



The **display info-center statistics** command displays all information that information management records.




Format
------

**display info-center statistics**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To view the information that information management records, run the display info-center command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics that information management records.
```
<HUAWEI> display info-center statistics
Information statistics data:
ModuleID    ModuleName          LogRecv   LogDrop  DiagRecv  DiagDrop  EventTrapRecv  EventTrapDrop DebugRecv DebugDrop   HighPrecRecv   HighPrecDrop
0x827       AAA                       0         0         0         0              1              0         0         0              0              0
0x910       BFD                       0         0         6         0              0              0         0         0              0              0
0x939       CACHEM                    0         0         2         0              0              0         0         0              0              0
0x815       CFG                       0         0      2527         0              0              0         0         0              0              0
0x816       CLI                       3         0         3         0              0              0         0         0              0              0
0xC9B       DATAAGTOM                 0         0        39         0              0              0         0         0              0              0
0x9C2       DCN                       0         0        15         0              0              0         0         0              0              0

```

**Table 1** Description of the **display info-center statistics** command output
| Item | Description |
| --- | --- |
| ModuleID | ID of the module in information management. |
| ModuleName | Name of the module that generates logs. |
| LogRecv | Number of received logs. |
| LogDrop | Number of discarded logs. |
| DiagRecv | Number of received diagnosis logs. |
| DiagDrop | Number of discarded diagnosis logs. |
| EventTrapRecv | Number of received event traps. |
| EventTrapDrop | Number of discarded event traps. |
| DebugRecv | Number of received debugging information records. |
| DebugDrop | Number of discarded debugging information records. |
| HighPrecRecv | Number of received high-precision logs. |
| HighPrecDrop | Number of discarded high-precision logs. |