reset cpu-defend filter statistics
==================================

reset cpu-defend filter statistics

Function
--------



The **reset cpu-defend filter statistics** command clears statistics about packets discarded during packet filtering.




Format
------

**reset cpu-defend filter statistics** [ **slot** *slot-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Specifies the slot ID. | The value is a string of 1 to 31 case-sensitive characters without spaces. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

Run the **reset cpu-defend filter statistics** command to clear existing statistics.


Example
-------

# Clear statistics about packets discarded during packet filtering.
```
<HUAWEI> reset cpu-defend filter statistics

```