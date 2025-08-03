enable (IOAM view)
==================

enable (IOAM view)

Function
--------



The **enable** command enables the IOAM function.

The **undo enable** command disables the IOAM function.



By default, the IOAM function is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**enable**

**undo enable**


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

To use IOAM to monitor or measure traffic, run this command to enable IOAM to sample and process service packets.


Example
-------

# Enable the IOAM function in the IOAM view.
```
<HUAWEI> system-view
[~HUAWEI] ioam
[*HUAWEI-ioam] enable

```