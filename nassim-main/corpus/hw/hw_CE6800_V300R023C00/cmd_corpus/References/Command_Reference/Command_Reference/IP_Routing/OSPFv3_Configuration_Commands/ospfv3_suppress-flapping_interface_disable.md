ospfv3 suppress-flapping interface disable
==========================================

ospfv3 suppress-flapping interface disable

Function
--------



The **ospfv3 suppress-flapping interface disable** command disables OSPFv3 interface flapping suppression.

The **undo ospfv3 suppress-flapping interface disable** command enables OSPFv3 interface flapping suppression.



By default, OSPFv3 interface flapping suppression is enabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ospfv3 suppress-flapping interface disable**

**undo ospfv3 suppress-flapping interface disable**


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

If OSPFv3 interfaces frequently alternate between up and down, the interfaces will flap, and protocol packets will be frequently exchanged, affecting OSPFv3 services. To address this issue, run the undo **ospfv3 suppress-flapping interface disable** command to enable interface flapping suppression. This function allows a device to delay interface state changes to up.By default, interface flapping suppression is enabled globally for all OSPFv3 interfaces. If this function is not needed, run the **ospfv3 suppress-flapping interface disable** command to disable it.


Example
-------

# Disable OSPFv3 interface flapping suppression.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 suppress-flapping interface disable

```