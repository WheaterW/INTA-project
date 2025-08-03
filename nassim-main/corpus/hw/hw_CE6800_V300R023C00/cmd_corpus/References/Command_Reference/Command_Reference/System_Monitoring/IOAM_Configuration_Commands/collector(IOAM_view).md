collector(IOAM view)
====================

collector(IOAM view)

Function
--------



The **collector collect** command binds an analyzer with a specified ID.

The **undo collector** command unbinds an analyzer with a specified ID.



By default, no analyzer is bound in the IOAM view.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**collector collect** *collect-id*

**undo collector** [ **collect** [ *collect-id* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **collect** *collect-id* | Specifies the analyzer ID. | The value is an integer that ranges from 1 to 5. |



Views
-----

IOAM view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To use an analyzer to analyze and monitor IOAM network data, you can run this command in the IOAM view to bind the analyzer with a specified ID.

**Prerequisites**

The collector ID has been configured using the **collector** command.


Example
-------

# Configure analyzer 3 and bind it in the IOAM view.
```
<HUAWEI> system-view
[~HUAWEI] collector collect 3
[*HUAWEI-collect-3] source ip 10.10.10.10 export host ip 10.10.10.20 udp-port 1000
[*HUAWEI-collect-3] quit
[*HUAWEI] ioam
[*HUAWEI-ioam] collector collect 3

```