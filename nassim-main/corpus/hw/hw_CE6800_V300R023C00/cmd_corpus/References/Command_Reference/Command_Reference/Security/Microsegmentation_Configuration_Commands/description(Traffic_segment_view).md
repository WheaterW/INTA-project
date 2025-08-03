description(Traffic segment view)
=================================

description(Traffic segment view)

Function
--------



The **description** command configures the description of an EPG.

The **undo description** command deletes the description of an EPG.



By default, no description is configured for an EPG.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**description** *desc-string*

**undo description** [ *desc-string* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *desc-string* | Description of a microsegmentation group. | The value is a string of 1 to 256 case-sensitive characters, spaces not supported. It must start with a letter or a digit ranging from 0 to 9. |



Views
-----

Traffic segment view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To facilitate EPG management, identification, and memorization, run the **description** command to configure a description to identify an EPG and record the usage of the EPG.


Example
-------

# Configure the description demo for EPG 32768.
```
<HUAWEI> system-view
[~HUAWEI] traffic-segment enable
[*HUAWEI] traffic-segment segment-id 32768
[*HUAWEI-traffic-segment-32768] description demo

```