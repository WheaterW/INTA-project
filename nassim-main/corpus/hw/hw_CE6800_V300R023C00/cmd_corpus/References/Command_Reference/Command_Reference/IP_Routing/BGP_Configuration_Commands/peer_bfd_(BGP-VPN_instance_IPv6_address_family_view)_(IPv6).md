peer bfd (BGP-VPN instance IPv6 address family view) (IPv6)
===========================================================

peer bfd (BGP-VPN instance IPv6 address family view) (IPv6)

Function
--------



The **peer bfd** command sets BFD detection parameters for a peer.

The **undo peer bfd** command restores default BFD detection parameter values.



By default, the interval for sending BFD packets is 1000 ms, the interval for receiving BFD packets is 1000 ms, and the local detection multiplier is 3.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *ipv6-address* **bfd** { **min-tx-interval** *min-tx-interval* | **min-rx-interval** *min-rx-interval* | **detect-multiplier** *multiplier* } \*

**undo peer** *ipv6-address* **bfd** { **min-tx-interval** | **min-rx-interval** | **detect-multiplier** } \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies an IPv6 peer address. | The value is in the format of X:X:X:X:X:X:X:X. |
| **min-tx-interval** *min-tx-interval* | Specifies the interval at which BFD packets are sent. | The value is an integer ranging from 3 to 1000, in milliseconds. The default value is 1000. |
| **min-rx-interval** *min-rx-interval* | Specifies the interval at which BFD packets are received. | The value is an integer ranging from 3 to 1000, in milliseconds. The default value is 1000. |
| **detect-multiplier** *multiplier* | Specifies the local detection multiplier. | The value is an integer ranging from 3 to 50. The default value is 3. |



Views
-----

BGP-VPN instance IPv6 address family view,BGP multi-instance VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

BFD provides millisecond-level fault detection. It helps BGP to detect faults in neighboring devices or links more quickly, and instructs BGP to recalculate routes for correct packet forwarding. The **peer bfd** command can be used to set the values of BFD session parameters on a specified interface.The BFD configuration of a peer takes precedence over that of the peer group to which the peer belongs. If BFD is not configured on a peer and the peer group to which the peer belongs is enabled with BFD, the peer will inherit the BFD configurations of the peer group.

**Prerequisites**



A BFD session can be established only when the corresponding BGP session is in the Established state.



**Configuration Impact**



If the **peer bfd** command is run multiple times, the latest configuration overwrites the previous one. The BFD session uses the latest parameters as the detection parameters.Assume that BFD is configured on a peer. If the peer bfd block command is not run on members of the peer group, the members will establish BFD sessions.



**Precautions**



If BFD parameters are set on a peer, a BFD session will be established by using the BFD parameters on the peer.




Example
-------

# Configure BFD and set detection parameters on the peer.
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
[*HUAWEI-bgp-6-vpna] peer 2001:DB8:1::1 bfd min-tx-interval 100 min-rx-interval 100 detect-multiplier 5

```