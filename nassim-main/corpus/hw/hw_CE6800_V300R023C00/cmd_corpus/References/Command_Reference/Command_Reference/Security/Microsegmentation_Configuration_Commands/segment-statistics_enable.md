segment-statistics enable
=========================

segment-statistics enable

Function
--------



The **segment-statistics enable** command enables traffic statistics collection for an EPG.

The **undo segment-statistics enable** command disables traffic statistics collection for an EPG.



By default, traffic statistics collection is disabled for an EPG.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**segment-statistics enable**

**undo segment-statistics enable**


Parameters
----------

None

Views
-----

Traffic segment view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To collect traffic statistics based on EPGs, run the **segment-statistics enable** command to enable traffic statistics collection for EPGs.You can run the **display traffic-segment statistics** command in any view to view the statistics.


Example
-------

# Enable statistics collection for EPG 32768.
```
<HUAWEI> system-view
[~HUAWEI] traffic-segment enable
[*HUAWEI] traffic-segment segment-id 32768
[*HUAWEI-traffic-segment-32768] segment-statistics enable

```