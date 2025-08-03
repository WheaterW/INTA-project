segment classifier
==================

segment classifier

Function
--------



The **segment classifier** command creates a segment classifier and displays the segment classifier view, or displays the view of an existing segment classifier.

The **undo segment classifier** command deletes a segment classifier.



By default, no segment classifier is created.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**segment classifier** *classifier-name*

**undo segment classifier** *classifier-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *classifier-name* | Specifies the name of a segment classifier. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. It must start with a letter or digit. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

On a data center network, servers are grouped into EPGs based on certain rules. If you do not want to use the default microsegmentation policy for packets matching EPGs but specify GBPs for the packets, configure and apply GBPs as follows:

1. Create a segment classifier and configure rules for matching EPG packets in the segment classifier view.
2. Create a segment behavior and configure a traffic control behavior for the EPG in the segment behavior view.
3. Create a segment policy and bind the segment classifier and segment behavior to the segment policy in the segment policy view.
4. Apply the segment policy.

Example
-------

# Create a segment classifier c1 and enter the segment classifier view.
```
<HUAWEI> system-view
[~HUAWEI] traffic-segment enable
[*HUAWEI] segment classifier c1

```