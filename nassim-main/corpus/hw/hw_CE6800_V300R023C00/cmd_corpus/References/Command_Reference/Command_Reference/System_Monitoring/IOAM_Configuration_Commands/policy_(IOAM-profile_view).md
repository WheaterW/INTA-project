policy (IOAM-profile view)
==========================

policy (IOAM-profile view)

Function
--------



The **policy** command creates an IOAM policy view and displays the view, or displays an existing IOAM policy view.

The **undo policy** command deletes a created IOAM policy.



By default, no IOAM policy is created in the system.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**policy** *policy-id*

**undo policy** *policy-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *policy-id* | Specify the value of the IOAM policy ID. | The value is 1. |



Views
-----

IOAM-profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To configure an IOAM policy to monitor or measure traffic, run this command to create an IOAM policy and enter the IOAM policy view.


Example
-------

# Create an IOAM policy view and enter the view.
```
<HUAWEI> system-view
[~HUAWEI] ioam
[*HUAWEI-ioam] profile default
[*HUAWEI-ioam-profile-default] policy 1
[*HUAWEI-ioam-profile-default-policy-1]

```