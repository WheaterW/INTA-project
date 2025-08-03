rpfr enable
===========

rpfr enable

Function
--------

The **rpfr enable** command enables RPFR.

The **undo rpfr enable** command disables RPFR.

By default, RPFR is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6885-SAN and CE8850-SAN.



Format
------

**rpfr enable**

**undo rpfr enable**


Parameters
----------

None


Views
-----

iNOF view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to enable RPFR.


Example
-------

# Enable RPFR.
```
<HUAWEI> system-view
[~HUAWEI] ai-service
[*HUAWEI-ai-service] inof
[*HUAWEI-ai-service-inof] rpfr enable
```