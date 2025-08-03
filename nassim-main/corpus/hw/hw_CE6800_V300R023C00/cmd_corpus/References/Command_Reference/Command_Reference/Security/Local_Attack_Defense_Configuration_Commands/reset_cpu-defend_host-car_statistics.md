reset cpu-defend host-car statistics
====================================

reset cpu-defend host-car statistics

Function
--------



The **reset cpu-defend host-car statistics** command clears packet statistics in the user-level rate limiting.




Format
------

**reset cpu-defend host-car** [ **mac-address** *mac-address* ] **statistics** [ **slot** *slot-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **mac-address** *mac-address* | Clears statistics on the packets from the specified MAC address. | The value is in the format of H-H-H. |
| **slot** *slot-id* | Clears packet statistics on the specified slot. | The value is a string of 1 to 31 case-sensitive characters without spaces. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

Before viewing the latest packet statistics in the user-level rate limiting, run this command to clear existing packet statistics.


Example
-------

# Clear packet statistics in user-level rate limiting.
```
<HUAWEI> reset cpu-defend host-car statistics

```