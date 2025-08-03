default-cost (OSPFv3 area view)
===============================

default-cost (OSPFv3 area view)

Function
--------



The **default-cost** command specifies the cost of the default route that is sent to the stub area by OSPFv3.

The **undo default-cost** command restores the cost.



By default, the cost of the default route that is sent to the stub area by OSPFv3 is 1.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**default-cost** *costval*

**undo default-cost**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *costval* | Specifies the cost of the default route that is sent to the stub area by OSPFv3. | The value ranges from 0 to 16777214. |



Views
-----

OSPFv3 area view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If multiple OSPFv3 processes are enabled, the command takes effect only on this process.


Example
-------

# Set the area 1 as the stub area and the cost of the default route that is sent to the stub area to 60.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] area 1
[*HUAWEI-ospfv3-1-area-0.0.0.1] stub
[*HUAWEI-ospfv3-1-area-0.0.0.1] default-cost 60

```