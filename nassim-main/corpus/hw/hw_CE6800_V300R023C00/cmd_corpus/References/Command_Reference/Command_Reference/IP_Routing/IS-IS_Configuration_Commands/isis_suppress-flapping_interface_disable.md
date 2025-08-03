isis suppress-flapping interface disable
========================================

isis suppress-flapping interface disable

Function
--------



The **isis suppress-flapping interface disable** command disables IS-IS interface flapping suppression.

The **undo isis suppress-flapping interface disable** command enables IS-IS interface flapping suppression.



By default, IS-IS interface flapping suppression is enabled.


Format
------

**isis suppress-flapping interface disable**

**undo isis suppress-flapping interface disable**


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

If IS-IS interfaces frequently alternate between up and down, the interfaces will flap, and protocol packets will be frequently exchanged, affecting IS-IS services. To address this issue, run the undo **isis suppress-flapping interface disable** command to enable interface flapping suppression. This function allows a device to delay interface state changes to up.By default, interface flapping suppression is enabled globally for all IS-IS interfaces. If this function is not needed, run the **isis suppress-flapping interface disable** command to disable it.


Example
-------

# Disable IS-IS interface flapping suppression.
```
<HUAWEI> system-view
[~HUAWEI] isis suppress-flapping interface disable

```