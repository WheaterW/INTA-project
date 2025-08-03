peer keep-all-routes (BGP-VPN instance IPv4 address family view)
================================================================

peer keep-all-routes (BGP-VPN instance IPv4 address family view)

Function
--------



The **peer keep-all-routes** command saves all the BGP routing updates from the specified peer or the peer group after the BGP connection is set up, even though those routes do not pass the configured ingress policy.

The undo peer keep-all-routes command disables this function.



By default, only the BGP routing updates received from the peers and passing the configured ingress policy are saved.


Format
------

**peer** *ipv4-address* **keep-all-routes**

**undo peer** *ipv4-address* **keep-all-routes**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies the IPv4 address of a peer. | It is in dotted decimal notation. |



Views
-----

BGP-VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After changing a BGP import policy, you can reset BGP connections for the new import policy to take effect immediately, interrupting these BGP connections temporarily. If a device's peer does not support route-refresh, the **peer keep-all-routes** command can be used on the device to remain all routing updates received from the peer so that the device can refresh its routing table without closing the connection with the peer.

**Implementation Procedure**

If the **peer keep-all-routes** command is run but no peer exists, a message is displayed, indicating that the peer does not exist.

**Precautions**

If the route does not support the route-refresh capability, the **peer keep-all-routes** command needs to be run on the route and its peer. If the **peer keep-all-routes** command is run on a device for the first time, the sessions between the device and its peers will be re-established.If the route supports the route-refresh capability, running this command does not result in re-establishment of the sessions between the route and its peers. After the **refresh bgp** command is run on the route, however, the route does not refresh its routing table.After the **keep-all-routes** command is run, the **undo peer keep-all-routes** command becomes ineffective. To have the **undo peer keep-all-routes** command become effective, run the **undo keep-all-routes** command and then the **peer keep-all-routes** command.


Example
-------

# Configure a device to store all BGP routing updates received from its peer.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpna
[*HUAWEI-bgp-vpna] peer 1.1.1.1 as-number 100
[*HUAWEI-bgp-vpna] peer 1.1.1.1 keep-all-routes

```