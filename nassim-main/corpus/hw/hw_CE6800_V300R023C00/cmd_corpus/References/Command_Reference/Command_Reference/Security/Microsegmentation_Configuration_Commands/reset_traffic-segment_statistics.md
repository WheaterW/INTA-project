reset traffic-segment statistics
================================

reset traffic-segment statistics

Function
--------



The **reset traffic-segment statistics** command clears EPG statistics.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**reset traffic-segment statistics** { **segment-id** *id-value* | **segment-name** *name* } **slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **segment-id** *id-value* | Microsegmentation ID. | The value is an integer ranging from 1 to 65535. |
| **segment-name** *name* | Specifies a microsegmentation name. | The value is a string of 1 to 31 case-sensitive characters, starting with a letter. |
| **slot** *slot-id* | Specifies the slot ID. | The value is a string of characters. The value is a slot ID. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

Before recollecting EPG statistics, run the **reset traffic-segment statistics** command to clear existing EPG statistics and then run the **display traffic-segment statistics** command to view existing EPG statistics.


Example
-------

# Clear statistics about EPG 112 in slot 1.
```
<HUAWEI> reset traffic-segment statistics segment-id 112 slot 1

```