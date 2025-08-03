ioam
====

ioam

Function
--------



The **ioam** command creates an IOAM view and displays the view, or displays an existing IOAM view.

The **undo ioam** command deletes a created IOAM view.



By default, no IOAM view is created.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**ioam**

**undo ioam**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To use IOAM to monitor or measure traffic, run this command to enter the IOAM view.

**Precautions**



IOAM and latency-event services cannot be configured at the same time.




Example
-------

# Create an IOAM view and enter the view.
```
<HUAWEI> system-view
[~HUAWEI] ioam
[*HUAWEI-ioam]

```