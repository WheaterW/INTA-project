reset dragonfly abs-pfc statistics
==================================

reset dragonfly abs-pfc statistics

Function
--------



The **reset dragonfly abs-pfc statistics** command clears statistics on dragonfly antilocking PFC on an interface where the adaptive routing function is enabled.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**reset dragonfly abs-pfc statistics** [ **interface** { *interface-name* | *interface-type* *interface-number* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-name* | Specifies the name of an interface. | - |
| **interface** *interface-type* *interface-number* | Specifies the type and number of an interface. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When diagnosing and locating a dragonfly antilocking PFC fault, you need to collect statistics in a specified period.Before recollecting dragonfly antilocking PFC statistics, run the **reset dragonfly abs-pfc statistics** command to clear the existing statistics and then run the **display dragonfly abs-pfc statistics** command to view the statistics.

**Precautions**

After you run this command, dragonfly antilocking PFC statistics are cleared and cannot be restored. Exercise caution when you run this command.


Example
-------

# Clear dragonfly antilocking PFC statistics on a specified interface.
```
<HUAWEI> reset dragonfly abs-pfc statistics interface 100GE 1/0/1

```