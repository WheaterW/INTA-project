reset icmp fast-reply statistics
================================

reset icmp fast-reply statistics

Function
--------



The **reset icmp fast-reply statistics** command clears ICMP fast reply statistics.




Format
------

**reset icmp fast-reply statistics slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Specifies the ID of a slot in which ICMP fast reply statistics need to be cleared. | The value is a string of 1 to 23 case-sensitive characters, spaces not supported. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

To collect ICMP fast reply statistics in a period of time, run the reset icmp fast-reply statistics command to clear the existing statistics and then perform recollection.


Example
-------

# Clear ICMP fast reply statistics in slot 1.
```
<HUAWEI> reset icmp fast-reply statistics slot 1

```