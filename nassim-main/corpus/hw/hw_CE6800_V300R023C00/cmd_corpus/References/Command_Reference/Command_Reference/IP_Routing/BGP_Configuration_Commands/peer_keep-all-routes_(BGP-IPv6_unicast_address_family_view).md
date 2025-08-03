peer keep-all-routes (BGP-IPv6 unicast address family view)
===========================================================

peer keep-all-routes (BGP-IPv6 unicast address family view)

Function
--------



The **peer keep-all-routes** command saves all the BGP routing updates from the specified peer or the peer group after the BGP connection is set up, even though those routes do not pass the configured ingress policy.

The **undo peer keep-all-routes** command disables this function.



By default, only the BGP routing updates received from the peers and passing the configured ingress policy are saved.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *ipv4-address* **keep-all-routes**

**undo peer** *ipv4-address* **keep-all-routes**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |



Views
-----

BGP-IPv6 unicast address family view


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

# Configure a device to save all BGP routing updates received from its peers.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 1.1.1.1 as-number 100
[*HUAWEI-bgp] ipv6-family unicast
[*HUAWEI-bgp-af-ipv6] peer 1.1.1.1 enable
[*HUAWEI-bgp-af-ipv6] peer 1.1.1.1 keep-all-routes

```