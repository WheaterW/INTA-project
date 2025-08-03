profile default(IOAM view)
==========================

profile default(IOAM view)

Function
--------



The **profile default** command displays the default IOAM profile view.



By default, a profile named default is created after the IOAM view is created.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**profile default**


Parameters
----------

None

Views
-----

IOAM view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To configure an IOAM policy to monitor or measure traffic, run this command to enter the default IOAM profile view.


Example
-------

# Enter the default IOAM profile view.
```
<HUAWEI> system-view
[~HUAWEI] ioam
[*HUAWEI-ioam] profile default
[*HUAWEI-ioam-profile-default]

```