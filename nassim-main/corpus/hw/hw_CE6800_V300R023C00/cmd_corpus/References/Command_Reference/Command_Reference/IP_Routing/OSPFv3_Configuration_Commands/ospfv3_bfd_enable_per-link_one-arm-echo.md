ospfv3 bfd enable per-link one-arm-echo
=======================================

ospfv3 bfd enable per-link one-arm-echo

Function
--------



The **ospfv3 bfd enable per-link one-arm-echo** command enables link-based loopback detection.

The **undo ospfv3 bfd enable** command disables link-based loopback detection.



By default, link-based loopback detection is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ospfv3 bfd enable per-link one-arm-echo** [ **instance** *instance-id* ]

**undo ospfv3 bfd enable** [ **per-link** **one-arm-echo** ] [ **instance** *instance-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **instance** *instance-id* | Specifies the instance ID of an interface. | The value is an integer in the range from 0 to 255. |



Views
-----

VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

An Eth-Trunk interface in a VLAN can be bound to multiple physical interfaces. After BFD is configured, the BFD session may go Down as long as one physical interface goes Down. As a result, the OSPFv3 neighbor relationship goes Down. After link-based loopback detection is enabled, BFD sessions go Down only when all physical interfaces go Down. This ensures that OSPFv3 neighbor relationships can be established.


Example
-------

# Enable link-based BFD loopback detection on VLANIF100.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] area 0.0.0.0
[*HUAWEI-ospfv3-1-area-0.0.0.0] quit
[*HUAWEI-ospfv3-1] quit
[*HUAWEI] interface Vlanif100
[*HUAWEI-Vlanif100] ipv6 enable
[*HUAWEI-Vlanif100] ospfv3 1 area 0
[*HUAWEI-Vlanif100] ospfv3 bfd enable
[*HUAWEI-Vlanif100] ospfv3 bfd enable per-link one-arm-echo

```