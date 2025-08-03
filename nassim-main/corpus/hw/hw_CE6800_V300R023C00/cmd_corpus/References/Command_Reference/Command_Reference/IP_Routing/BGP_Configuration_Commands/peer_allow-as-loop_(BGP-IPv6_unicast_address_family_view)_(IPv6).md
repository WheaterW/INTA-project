peer allow-as-loop (BGP-IPv6 unicast address family view) (IPv6)
================================================================

peer allow-as-loop (BGP-IPv6 unicast address family view) (IPv6)

Function
--------



The **peer allow-as-loop** command sets the number of times that the local AS number can be repeated.

The **undo peer allow-as-loop** command disables this function.



By default, local AS number repetition is not allowed.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *ipv6-address* **allow-as-loop** [ *number* ]

**undo peer** *ipv6-address* **allow-as-loop**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies the IPv6 address of a peer. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *number* | Specifies the maximum number of times the local AS number can be repeated in the AS\_Path of each received route. | The value is an integer ranging from 1 to 10. The default value is 1. |



Views
-----

BGP-IPv6 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

BGP uses AS numbers to detect routing loops. The AS numbers in the AS\_Path of each received route are matched against the local AS number configured using the **bgp** command and the fake AS number configured using the **peer local-as** command.After the **peer allow-as-loop** command is executed to configure the number of local AS number repetitions, the BGP speaker can allow routes with repeated AS numbers in AS\_Path to pass to meet the requirements of special scenarios.

**Prerequisites**

Peer relationships have been established using the **peer as-number** command.

**Configuration Impact**

If this command is run for a peer multiple times, the latest configuration overrides the previous one.

**Precautions**

The **peer allow-as-loop** command does not take effect for IBGP peers or BGP peers in a sub-confederation. The device checks whether the routes received from EBGP peers or EBGP peers in the confederation contain the local AS number. The minimum number of repetitions is 2, and the value 1 is not displayed.Running the **peer allow-as-loop** command may cause routing loops. Therefore, exercise caution when running this command and specify the number of AS number repetitions as required.


Example
-------

# Set the number of local AS number repetitions to 2.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 2001:DB8:1::1 as-number 100
[*HUAWEI-bgp] ipv6-family unicast
[*HUAWEI-bgp-af-ipv6] peer 2001:DB8:1::1 enable
[*HUAWEI-bgp-af-ipv6] peer 2001:DB8:1::1 allow-as-loop 2

```