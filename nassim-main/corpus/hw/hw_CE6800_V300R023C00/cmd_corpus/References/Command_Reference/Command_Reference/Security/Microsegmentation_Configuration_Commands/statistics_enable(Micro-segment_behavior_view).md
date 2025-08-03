statistics enable(Micro-segment behavior view)
==============================================

statistics enable(Micro-segment behavior view)

Function
--------



The **statistics enable** command enables traffic statistics collection for a microsegmentation grouping policy.

The **undo statistics enable** command disables traffic statistics collection for a microsegmentation grouping policy.



By default, traffic statistics collection is disabled for a microsegmentation grouping policy.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**statistics enable**

**undo statistics enable**


Parameters
----------

None

Views
-----

Micro-segment behavior view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To display packet statistics after a microsegmentation grouping policy is applied, run the **statistics enable** command to enable the traffic statistics collection function.


Example
-------

# Enable the traffic statistics collection function for a microsegmentation grouping policy.
```
<HUAWEI> system-view
[~HUAWEI] traffic-segment enable
[*HUAWEI] segment behavior test
[*HUAWEI-segmentbehavior-test] statistics enable

```