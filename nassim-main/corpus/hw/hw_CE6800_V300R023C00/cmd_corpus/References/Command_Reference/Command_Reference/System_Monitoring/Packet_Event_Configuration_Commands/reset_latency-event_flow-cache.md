reset latency-event flow-cache
==============================

reset latency-event flow-cache

Function
--------



The **reset latency-event flow-cache** command clears the latency visualization flow table.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset latency-event flow-cache** [ **slot** *slot-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Specifies the slot ID of a card. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

You can use the reset latency-event flow-cache command to clear the latency visualization flow table.


Example
-------

# Clear the latency visualization flow table.
```
<HUAWEI> reset latency-event flow-cache

```