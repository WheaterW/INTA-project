peer allow-as-loop (BGP-EVPN address family view) (IPv6)
========================================================

peer allow-as-loop (BGP-EVPN address family view) (IPv6)

Function
--------



The **peer allow-as-loop** command sets the number of local AS number repetitions.

The **undo peer allow-as-loop** command cancels the configuration.



By default, the local AS number cannot be repeated.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *peerIpv6Addr* **allow-as-loop** [ *num* ]

**undo peer** *peerIpv6Addr* **allow-as-loop**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv6Addr* | Specifies the IPv6 address of a BGP EVPN peer. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| *num* | Maximum number of times the local AS number can be included in the AS\_Path of each received route. | The value is an integer in the range from 1 to 10. The default value is 1. |



Views
-----

BGP-EVPN address family view,bgp-muli-instance-af-evpn view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Generally, BGP uses AS numbers to detect routing loops. The local AS number configured using the bgp command and the fake AS number configured using the peer fake-as command are compared with the AS\_Path carried in the received route. The number of loops is the largest. In Hub and Spoke networking, if EBGP runs between the PE and CE of the Hub, the routing information advertised by the Hub-PE to the Hub-CE carries the AS number of the Hub-CE. When the Hub-PE receives the routing update from the Hub-CE, the routing update carries the AS number of the Hub-PE. In this case, the Hub-PE cannot receive the routing update.To ensure correct route transmission in the Hub and Spoke networking, configure the BGP peers on the path from the Hub-CE to the Spoke-CE to allow the routes with the same AS number in the AS\_Path attribute to pass.

**Prerequisites**

BGP peers have been enabled in the BGP-EVPN address family view.

**Configuration Impact**

If the peer command is run more than once for the same peer, the latest configuration overrides the previous one.

**Precautions**

The **peer allow-as-loop** command does not take effect for IBGP peers or BGP peers in a sub-confederation. The device checks whether the routes received from EBGP peers or EBGP peers in the confederation contain the local AS number. The minimum number of repetitions is 2, and the value 1 is not displayed.Running the **peer allow-as-loop** command may cause routing loops. Therefore, exercise caution when running this command and specify the number of AS number repetitions as required.


Example
-------

# Set the number of local AS number repetitions to 2 in the BGP-EVPN address family view.
```
<HUAWEI> system-view
[~HUAWEI] bgp 200
[*HUAWEI-bgp] peer 2001:db8:1::1 as-number 200
[*HUAWEI-bgp] l2vpn-family evpn
[*HUAWEI-bgp-af-evpn] peer 2001:db8:1::1 enable
[*HUAWEI-bgp-af-evpn] peer 2001:db8:1::1 allow-as-loop 2

```