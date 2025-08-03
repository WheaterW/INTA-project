peer graceful-restart timer wait-for-rib (BGP-VPN instance IPv6 address family view)(IPv6)
==========================================================================================

peer graceful-restart timer wait-for-rib (BGP-VPN instance IPv6 address family view)(IPv6)

Function
--------



The **peer graceful-restart timer wait-for-rib** command sets the maximum duration for a BGP restarter to wait for the End-of-RIB flag from a specified peer.

The **undo peer graceful-restart timer wait-for-rib** command deletes the configured duration.



By default, a BGP restarter waits for the End-of-RIB flag from a specified peer for a maximum of 600s.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *ipv6-address* **graceful-restart** **timer** **wait-for-rib** *time-value*

**undo peer** *ipv6-address* **graceful-restart** **timer** **wait-for-rib**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies the IPv6 address of a peer. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *time-value* | Specifies the maximum duration for waiting for the End-Of-RIB flag. | The value is an integer ranging from 3 to 3000, in seconds. |



Views
-----

BGP-VPN instance IPv6 address family view,BGP multi-instance VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After the local device reestablishes a BGP session with a specified peer, the local device should receive the End-Of-RIB flag from the specified peer within the period specified by this command. If the local device does not receive the End-Of-RIB flag within the period specified by this command, the local device exits the GR process and selects the optimal route from the existing routes.

**Configuration Impact**

If the peer graceful-restart timer wait-for-rib command is run more than once, the latest configuration overrides the previous one.


Example
-------

# Set the maximum duration during which a BGP restarter waits for the End-of-RIB flag from a specified peer to 100s.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv6-family
[*HUAWEI-vpn-instance-vpna-af-ipv6] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv6] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpna
[*HUAWEI-bgp-6-vpna] peer 2001:DB8:1::1 as-number 100
[*HUAWEI-bgp-6-vpna] peer 2001:DB8:1::1 graceful-restart timer wait-for-rib 100

```