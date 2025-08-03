classifier behavior(Micro-segment policy view)
==============================================

classifier behavior(Micro-segment policy view)

Function
--------



The **classifier behavior** command configures a segment behavior for a specified microsegmentation classifier in a microsegmentation grouping policy, that is, binds a microsegmentation classifier to a microsegmentation behavior.

The **undo classifier** command unbinds a microsegmentation classifier from a microsegmentation behavior in a microsegmentation grouping policy.



By default, no microsegmentation classifier or behavior is bound to a microsegmentation grouping policy.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**classifier** *classifier-name* **behavior** *behavior-name* [ **precedence** *precedence-value* ]

**undo classifier** *classifier-name* [ **behavior** *behavior-name* [ **precedence** *precedence-value* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **behavior** *behavior-name* | Specifies the name of a segment behavior. The value must be a defined segment behavior name. This parameter is configured using the traffic behavior command. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. The first character must be a letter or digit. |
| **precedence** *precedence-value* | Specifies the priority of a CB pair. | The value is an integer that ranges from 0 to 511. |
| **classifier** *classifier-name* | Specifies the name of a segment classifier. The segment classifier must have been defined. This parameter is configured using the traffic classifier command. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. The first character must be a letter or digit. |



Views
-----

Micro-segment policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a data center network, servers are grouped into EPGs based on certain rules. If you do not want to use the default microsegmentation policy for packets matching EPGs but specify GBPs for the packets, configure and apply GBPs as follows:

1. Create a segment classifier and configure rules for matching EPG packets in the segment classifier view.
2. Create a segment behavior and configure a traffic control behavior for the EPG in the segment behavior view.
3. Create a segment policy and bind the segment classifier and segment behavior to the segment policy in the segment policy view.
4. Apply the segment policy.

**Precautions**

If precedence precedence-value is not configured:

* If no microsegmentation classifier or behavior is bound, the default priority of the CB pair is 3.
* If a microsegmentation classifier and a microsegmentation behavior are bound, the priority of the CB pair is a multiple of 3 following the configured maximum value.

Example
-------

# Associate segment classifier c1 with segment behavior b1 in segment policy p1.
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