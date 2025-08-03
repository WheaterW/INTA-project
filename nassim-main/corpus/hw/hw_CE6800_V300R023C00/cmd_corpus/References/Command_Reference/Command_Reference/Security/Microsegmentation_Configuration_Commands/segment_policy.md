segment policy
==============

segment policy

Function
--------



The **segment policy** command creates a microsegmentation grouping policy and displays the microsegmentation grouping policy view, or displays the view of an existing microsegmentation grouping policy.

The **undo segment policy** command deletes a specified microsegmentation grouping policy.



By default, no microsegmentation grouping policy is created.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**segment policy** *policy-name*

**undo segment policy** *policy-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *policy-name* | Specifies the name of a segment policy. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

On a data center network, servers are grouped into EPGs based on certain rules. If you do not want packets matching EPGs to use the default microsegmentation policy but specify GBPs for the packets, configure and apply GBPs as follows:

1. Create a segment classifier and configure rules for matching EPG packets in the segment classifier view.
2. Create a segment behavior and configure a traffic control behavior for the EPG in the segment behavior view.
3. Create a segment policy and bind the segment classifier and segment behavior to the segment policy in the segment policy view.
4. Apply the segment policy.

Example
-------

# Create a segment policy p1 and associate the segment classifier c1 and segment behavior b1 with the segment policy.
```
<HUAWEI> system-view
[~HUAWEI] traffic-segment enable
[*HUAWEI] segment classifier c1
[*HUAWEI-segmentclassifier-c1] rule permit source-segment 32768
[*HUAWEI-segmentclassifier-c1] quit
[*HUAWEI] segment behavior b1
[*HUAWEI-segmentbehavior-b1] statistics enable
[*HUAWEI-segmentbehavior-b1] quit
[*HUAWEI] segment policy p1
[*HUAWEI-segmentpolicy-p1] classifier c1 behavior b1

```