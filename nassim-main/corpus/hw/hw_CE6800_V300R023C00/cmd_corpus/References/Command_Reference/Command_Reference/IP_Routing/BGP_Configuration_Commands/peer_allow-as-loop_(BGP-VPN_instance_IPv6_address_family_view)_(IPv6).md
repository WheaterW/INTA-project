peer allow-as-loop (BGP-VPN instance IPv6 address family view) (IPv6)
=====================================================================

peer allow-as-loop (BGP-VPN instance IPv6 address family view) (IPv6)

Function
--------



The **peer allow-as-loop** command sets the number of local AS number repetitions.

The **undo peer allow-as-loop** command cancels the configuration.



By default, the local AS number cannot be repeated.

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
| *number* | Specifies the maximum number of times the local AS number can be repeated in the AS\_Path of each received route. | The value is an integer in the range from 1 to 10. The default value is 1. |



Views
-----

BGP-VPN instance IPv6 address family view,BGP multi-instance VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Generally, BGP uses AS numbers to detect routing loops. The AS numbers in the AS\_Path of each received route are matched against the local AS number configured using the bgp command and the fake AS number configured using the peer fake-as command. The largest number of times any of the configured AS numbers is repeated is considered as the routing loop count. However, in Hub and Spoke networking, if EBGP runs between a Hub-PE and a Hub-CE, the routes that the Hub-PE sends to the Hub-CE carry the AS number of the Hub-PE; if the Hub-CE sends an Update message to the Hub-PE, the Hub-PE discards the message because the message includes the AS number of the Hub-PE.To ensure proper route transmission in the Hub and Spoke networking, configure all the BGP peers on the path, along which the Hub-CE advertises VPN routes to the Spoke-CE, to accept the routes that contain the local AS number as long as the number of repetitions in each route is within the default limit (1).

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
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv6-family
[*HUAWEI-vpn-instance-vpn1-af-ipv6] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv6] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpna
[*HUAWEI-bgp-6-vpna] peer 2001:DB8:1::1 as-number 100
[*HUAWEI-bgp-6-vpna] peer 2001:DB8:1::1 allow-as-loop 2

```