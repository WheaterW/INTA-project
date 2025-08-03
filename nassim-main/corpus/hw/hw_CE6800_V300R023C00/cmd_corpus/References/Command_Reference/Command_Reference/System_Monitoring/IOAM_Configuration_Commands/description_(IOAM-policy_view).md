description (IOAM-policy view)
==============================

description (IOAM-policy view)

Function
--------



The **description** command configures the description for an IOAM policy.

The **undo description** command deletes the description of an IOAM policy.



By default, no description is configured for an IOAM policy.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**description** *text*

**undo description** [ *text* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *text* | IOAM policy description information. | The value is a string of 1 to 80 characters, spaces supported. |



Views
-----

IOAM-policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To facilitate IOAM policy management, identification, and memorization, run the **description** command to configure a description for an IOAM policy.


Example
-------

# Add the description "Huawei" in the IOAM policy view.
```
<HUAWEI> system-view
[~HUAWEI] ioam
[*HUAWEI-ioam] profile default
[*HUAWEI-ioam-profile-default] policy 1
[*HUAWEI-ioam-profile-default-policy-1] description Huawei

```