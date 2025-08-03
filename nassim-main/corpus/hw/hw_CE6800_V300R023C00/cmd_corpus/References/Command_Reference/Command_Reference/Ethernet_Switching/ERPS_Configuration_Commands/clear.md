clear
=====

clear

Function
--------



The **clear** command clears the port blocking mode of an ERPS ring.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**clear**


Parameters
----------

None

Views
-----

ERPS ring view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To clear the FS or MS mode configured by the erps ring protect-switch command or port protect-switch command, run the **clear** command.The **clear** command also provides the following functions:

* Triggers revertive switching before the wait to restore (WTR) or wait to block (WTB) timer expires in the case of revertive operations.
* Triggers revertive switching in the case of non-revertive operations.

Example
-------

# Clear the port blocking mode of ERPS ring 5.
```
<HUAWEI> system-view
[~HUAWEI] erps ring 5
[*HUAWEI-erps-ring5] clear

```