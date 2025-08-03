bandwidth-reference (OSPFv3 view)
=================================

bandwidth-reference (OSPFv3 view)

Function
--------



The **bandwidth-reference** command sets the bandwidth reference value for interface cost calculation.

The **undo bandwidth-reference** command restores the default setting.



By default, the reference value of the link cost is 100 Mbit/s.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**bandwidth-reference** *value*

**undo bandwidth-reference**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *value* | Specifies the bandwidth reference value for interface cost calculation. | The value is an integer ranging from 1 to 2147483648, in Mbit/s. |



Views
-----

OSPFv3 view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If no link cost is set, OSPFv3 calculates the link cost based on the link bandwidth (Cost = Reference value/Bandwidth). The bandwidth unit is bit/s. The **ospfv3 cost** command sets the cost for an interface to run OSPFv3. The priority of the cost set using the **ospfv3 cost** command is higher than that of the cost set using the **bandwidth-reference** command.


Example
-------

# Set the bandwidth reference value to 1000.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] bandwidth-reference 1000

```