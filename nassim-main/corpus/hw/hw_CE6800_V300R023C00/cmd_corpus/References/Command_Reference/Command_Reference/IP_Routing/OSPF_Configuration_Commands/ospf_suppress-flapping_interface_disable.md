ospf suppress-flapping interface disable
========================================

ospf suppress-flapping interface disable

Function
--------



The **ospf suppress-flapping interface disable** command disables OSPF interface flapping suppression.

The **undo ospf suppress-flapping interface disable** command enables OSPF interface flapping suppression.



By default, OSPF interface flapping suppression is enabled.


Format
------

**ospf suppress-flapping interface disable**

**undo ospf suppress-flapping interface disable**


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

If OSPF interfaces frequently alternate between up and down, the interfaces will flap, and protocol packets will be frequently exchanged, affecting OSPF services. To address this issue, run the undo **ospf suppress-flapping interface disable** command to enable interface flapping suppression. This function allows a device to delay interface state changes to up.By default, interface flapping suppression is enabled globally for all OSPF interfaces. If this function is not needed, run the **ospf suppress-flapping interface disable** command to disable it.


Example
-------

# Disable OSPF interface flapping suppression.
```
<HUAWEI> system-view
[~HUAWEI] ospf suppress-flapping interface disable

```