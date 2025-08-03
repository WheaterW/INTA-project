peer peer-as-check(BGP-EVPN address family view)
================================================

peer peer-as-check(BGP-EVPN address family view)

Function
--------



The **peer peer-as-check** command prevents the routes received from an EBGP peer from being broadcast to other peers with the same AS number as the EBGP peer.

The **undo peer peer-as-check** command cancels the configuration.



By default, the routes received from an EBGP peer are broadcast to other EBGP peers in the same AS.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *peerIpv4Addr* **peer-as-check**

**peer** *peerIpv4Addr* **peer-as-check** **disable**

**undo peer** *peerIpv4Addr* **peer-as-check**

**undo peer** *peerIpv4Addr* **peer-as-check** **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv4Addr* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| **disable** | Disables the function. | - |



Views
-----

BGP-EVPN address family view,bgp-muli-instance-af-evpn view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By default, after receiving a route from an EBGP peer (for example, in AS 200), the local device (for example, in AS 100) advertises the route to all EBGP peers in AS 200. After the **peer peer-as-check** command is run on a device, the device does not advertise routes received from an EBGP peer to other EBGP peers in the same AS as this EBGP peer. This reduces BGP memory and CPU consumption and speeds up route convergence in case of route flapping.

**Prerequisites**



Run the **evpn-overlay enable** command to enable EVPN as the VXLAN control plane.



**Configuration Impact**

After this command is run, the number of BGP update peer-groups on the device is affected. If the AS numbers of BGP peers configured with this function are different, these BGP peers cannot be added to the same BGP update peer-group.

**Precautions**

This command applies only to EBGP peers.


Example
-------

# Configure a device not to advertise the routes learned from an EBGP peer to a specified peer with the same AS number as this EBGP peer.
```
<HUAWEI> system-view
[~HUAWEI] evpn-overlay enable
[*HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.1 as-number 200
[*HUAWEI-bgp] l2vpn-family evpn
[*HUAWEI-bgp-af-evpn] peer 10.1.1.1 enable
[*HUAWEI-bgp-af-evpn] peer 10.1.1.1 peer-as-check

```

# Configure a device not to advertise the routes learned from an EBGP peer to a specified peer with the same AS number as this EBGP peer.
```
<HUAWEI> system-view
[~HUAWEI] evpn-overlay enable
[*HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] peer 10.1.1.1 enable
[*HUAWEI-bgp-instance-a] l2vpn-family evpn
[*HUAWEI-bgp-instance-a-evpn] peer 10.1.1.1 enable
[*HUAWEI-bgp-instance-a-evpn] peer 10.1.1.1 peer-as-check

```