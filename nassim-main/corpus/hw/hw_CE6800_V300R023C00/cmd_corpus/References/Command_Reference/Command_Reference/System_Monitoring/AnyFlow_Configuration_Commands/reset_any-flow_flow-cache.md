reset any-flow flow-cache
=========================

reset any-flow flow-cache

Function
--------



The **reset any-flow flow-cache** command clears the flow table on the built-in CPU.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**reset any-flow flow-cache** [ **slot** *slot-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Specifies the slot ID. | The value is a string of 1 to 15 case-sensitive characters, spaces not supported. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To clear the flow table on the built-in CPU before the configured aging time expires, run this command.


Example
-------

# Clear the flow table on the built-in CPU.
```
<HUAWEI> reset any-flow flow-cache slot 1

```