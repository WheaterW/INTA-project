peer bfd enable (BGP-VPN instance IPv4 address family view)
===========================================================

peer bfd enable (BGP-VPN instance IPv4 address family view)

Function
--------



The **peer bfd enable** command enables a device to establish a BFD session with its peer using default detection parameter values.

The **undo peer bfd enable** command cancels this function.



By default, a BGP device does not establish any BFD session with its peer.


Format
------

**peer** *ipv4-address* **bfd** **enable** [ **single-hop-prefer** ] [ **compatible** ]

**peer** *ipv4-address* **bfd** **enable** **per-link** **one-arm-echo**

**peer** *ipv4-address* **bfd** **enable** **one-arm-echo**

**undo peer** *ipv4-address* **bfd** **enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies the IPv4 address of a peer. | The value is in dotted decimal notation. |
| **single-hop-prefer** | Preferentially creates a single-hop BFD session for BGP peers. | - |
| **compatible** | Indicates the compatibility mode. If this keyword is specified, the TTL in packets sent by BFD is set to 255. | - |
| **per-link** | Preferentially creates a single-hop BFD session for BGP peers. | - |
| **one-arm-echo** | Indicates a one-arm BFD echo session. | - |



Views
-----

BGP-VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



BGP uses BFD to quickly detect faults in links between BGP peers. This accelerates network convergence. You can run this command to create a BFD session with default detection parameters for a peer or peer group.If single-hop-prefer is specified, single-hop detection is preferentially used when a BFD session is established between BGP peers. This parameter is used to detect IP connectivity between BGP peers. That is, only one BFD session exists on a specified BGP interface. This parameter is used to ensure that the local and peer ends use the same detection mode when a Huawei device is connected to a non-Huawei device.The per-link one-arm-echo parameter enables one-arm BFD echo for each link. This parameter ensures that the local and peer ends use the same detection mode when a Huawei device is connected to a non-Huawei device.After a peer is added to a peer group, the peer inherits the BFD configuration of the peer group regardless of whether BFD is enabled on the peer. If the peer does not need to inherit the configuration of the peer group, run the **peer bfd block** command on the peer to prevent the peer from inheriting the BFD function of the peer group.If neither single-hop-prefer nor compatible is specified, the multi-hop mode is used by default when a BFD session is established between BGP peers, and the TTL value in BFD packets is 253 by default.



**Prerequisites**



If a BGP peer is in the Established state, after the **peer bfd enable** command is run to create a BFD session for the peer, the BFD state machine starts about 1 to 20 seconds later. Before the BFD state machine starts, the BFD session cannot be established.



**Configuration Impact**



After the **peer bfd enable** command is enabled, peers or peer groups can establish IPv6 BFD sessions using default parameter values. This allows fast link fault detection.The BFD configuration of a peer takes precedence over that of the peer group to which the peer belongs. If BFD is not configured on a peer and the peer group to which the peer belongs is enabled with BFD, the peer inherits the BFD configurations from the peer group.



**Precautions**



Before enabling BFD on a BGP peer, enable BFD in the system view. If no BFD detection parameter is specified, a BFD session is established using default parameter values.If the command is run more than once, the latest configuration overrides the previous one.The **peer bfd block** command and the **peer bfd enable** command are mutually exclusive. After the **peer bfd block** command is run, the BFD session is deleted automatically.The per-link one-arm-echo parameter only takes effect in the scenario where there is only one Eth-Trunk interface under the VLANIF interface.




Example
-------

# Configure BFD for a peer.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpn1
[*HUAWEI-bgp-vpn1] peer 192.168.1.1 as-number 100
[*HUAWEI-bgp-vpn1] peer 192.168.1.1 bfd enable

```