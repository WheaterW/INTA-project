peer bfd (BGP multi-instance VPN instance IPv4 address family view)
===================================================================

peer bfd (BGP multi-instance VPN instance IPv4 address family view)

Function
--------



The **peer bfd** command sets BFD detection parameters for a peer.

The **undo peer bfd** command restores default BFD detection parameter values.



By default, the interval at which BFD packets are sent is 1000 milliseconds, the interval at which BFD packets are received is 1000 milliseconds, the local detection time multiplier is 3.


Format
------

**peer** *ipv4-address* **bfd** { **min-tx-interval** *min-tx-interval* | **min-rx-interval** *min-rx-interval* | **detect-multiplier** *multiplier* } \*

**undo peer** *ipv4-address* **bfd** { **min-tx-interval** | **min-rx-interval** | **detect-multiplier** } \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| **min-tx-interval** *min-tx-interval* | Specifies the interval at which BFD packets are sent. | The value is an integer that ranges from 3 to 1000, in milliseconds. The default value is 1000 milliseconds. |
| **min-rx-interval** *min-rx-interval* | Specifies an interval at which BFD packets are received. | The value is an integer that ranges from 3 to 1000, in milliseconds. The default value is 1000 milliseconds. |
| **detect-multiplier** *multiplier* | Specifies the local detection time multiplier. | The value is an integer ranging from 3 to 50. The default value is 3. |



Views
-----

BGP multi-instance VPN instance IPv4 address family view


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

# Configure BFD and set detection parameters on peer 192.168.1.1.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-instance-vpna] quit
[*HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] ipv4-family vpn-instance vpna
[*HUAWEI-bgp-instance-a-vpna] peer 192.168.1.1 as-number 200
[*HUAWEI-bgp-instance-a-vpna] peer 192.168.1.1 bfd min-tx-interval 100 min-rx-interval 100 detect-multiplier 5

```