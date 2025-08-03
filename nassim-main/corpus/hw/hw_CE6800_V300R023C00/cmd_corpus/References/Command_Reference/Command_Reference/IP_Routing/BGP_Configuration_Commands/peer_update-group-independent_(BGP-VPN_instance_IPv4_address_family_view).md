peer update-group-independent (BGP-VPN instance IPv4 address family view)
=========================================================================

peer update-group-independent (BGP-VPN instance IPv4 address family view)

Function
--------



The **peer update-group-independent** command sets each peer in a peer group as an independent update peer-group.

The **peer update-group-independent enable** command sets a specified peer as an independent update peer-group.

The **peer update-group-independent disable** command disables a peer from being set as an independent update peer-group.

The **undo peer update-group-independent** command disables each peer in a peer group from being set as an independent update peer-group.

The **undo peer update-group-independent enable** command disables a peer from being set as an independent update peer-group.

The **undo peer update-group-independent disable** command sets a specified peer as an independent update peer-group.



By default, no peer is set as an independent update peer-group.


Format
------

**peer** *ipv4-address* **update-group-independent** **enable**

**peer** *ipv4-address* **update-group-independent** **disable**

**undo peer** *ipv4-address* **update-group-independent** **enable**

**undo peer** *ipv4-address* **update-group-independent** **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |



Views
-----

BGP-VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To improve the efficiency of route advertisement, BGP uses the dynamic update peer-group mechanism. The BGP peers with the same configurations are placed in an update peer-group. These routes are grouped once and then sent to all peers in the update peer-group. However, the routes learned from a peer may be sent back to the peer, for example, the preferred route learned from an EBGP peer is sent back to the EBGP peer, or the preferred route that an RR learns from a client is reflected back to the client. In this case, messages are discarded, wasting network resources.To address this problem, you can run the **peer update-group-independent** command to set a specified peer or each peer in a peer group as an independent update peer-group so that the routes learned from the peer are not sent back to the peer. However, if a specified peer or each peer in a peer group is set as an independent update peer-group, the advantages of the dynamic update peer-group mechanism cannot be brought into full play. Therefore, this command is used only when users have such a requirement.




Example
-------

# Set a specified peer as an independent update peer-group.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] vpn-instance vpna
[*HUAWEI-bgp-instance-vpna] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp-instance-vpna] quit
[*HUAWEI-bgp] ipv4-family vpn-instance vpna
[*HUAWEI-bgp-vpna] peer 10.1.1.1 enable
[*HUAWEI-bgp-vpna] peer 10.1.1.1 update-group-independent enable

```