reset fwm smart-link
====================

reset fwm smart-link

Function
--------



The **reset fwm smart-link** command clears statistics.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**reset fwm smart-link interface** { *ifName* | *ifType* *ifNum* } **slot** *slotId*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ifName* | Specifies a port name. | The value is a string case-sensitive characters. It cannot contain spaces. |
| *ifType* | Specifies a port type. | The value is an integer. |
| *ifNum* | Specifies the index of a port. | The value is a string case-sensitive characters. It cannot contain spaces. |
| **slot** *slotId* | Specifies a slot ID. | The value is a string case-sensitive characters. It cannot contain spaces. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

The **reset** command is used to clear statistics on an interface.


Example
-------

# Clear Smart Link statistics on an interface.
```
<HUAWEI> reset fwm smart-link interface 100GE1/0/1 slot 1

```