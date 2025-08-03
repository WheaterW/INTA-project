reset segment-policy statistics
===============================

reset segment-policy statistics

Function
--------



The **reset segment-policy statistics** command clears packet statistics of a microsegmentation policy.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**reset segment-policy statistics** *policy-name* [ **class** *class-name* ] **slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *policy-name* | Specifies the name of a microsegmentation grouping policy. | The value is a string of 1 to 31 characters. |
| **class** *class-name* | Specifies the name of a microsegmentation classifier. | The value is a string of 1 to 31 characters. |
| **slot** *slot-id* | Displays statistics about microsegmentation policies on a specified card. | The value is a string of characters. The value is a slot ID. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

Before recollecting packet statistics, run the **reset segment-policy statistics** command to clear existing microsegmentation policy packet statistics and then run the **display segment-policy statistics** command to view existing packet statistics.


Example
-------

# Clear statistics about packets matching the microsegmentation policy named pp in slot 1.
```
<HUAWEI> reset segment-policy statistics pp slot 1

```