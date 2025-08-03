ipv6 nd direct-route delay
==========================

ipv6 nd direct-route delay

Function
--------



The **ipv6 nd direct-route delay** command sets a delay in advertising IPv6 NDP Vlink direct routes on an interface.

The **undo ipv6 nd direct-route delay** command deletes the delay in advertising IPv6 NDP Vlink direct routes on an interface.



By default, no delay is set for advertising IPv6 NDP Vlink direct routes.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd direct-route delay** *delay-time*

**undo ipv6 nd direct-route delay** [ *delay-time* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *delay-time* | Specifies a delay in advertising IPv6 NDP Vlink direct routes on an interface. | The value is an integer ranging from 1 to 3600, in seconds. |



Views
-----

VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **ipv6 nd direct-route delay** command sets a delay in advertising IPv6 NDP Vlink direct routes on an interface.

**Prerequisites**

The IPv6 function has been enabled using the **ipv6 enable** command.

**Precautions**

If the **undo ipv6 enable** command is run in the interface view to disable IPv6, the **ipv6 nd direct-route delay** command configuration will be deleted. Therefore, exercise caution when running the former command.


Example
-------

# Set a delay in advertising IPv6 NDP Vlink direct routes on a VLANIF interface.
```
<HUAWEI> system-view
[~HUAWEI] interface vlanif 1
[*HUAWEI-vlanif1] ipv6 enable
[*HUAWEI-vlanif1] ipv6 nd direct-route delay 5

```