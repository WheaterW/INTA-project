peer bfd enable (BGP view)
==========================

peer bfd enable (BGP view)

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
| *ipv4-address* | Specifies the IPv4 address of a peer. | It is in dotted decimal notation. |
| **single-hop-prefer** | Configures the BGP peer to preferentially use the single-hop mode when establishing BFD sessions. | - |
| **compatible** | Indicates the compatibility mode and sets the TTL value in sent BFD packets to 255. | - |
| **per-link** | Establishes member interface link-based BFD sessions. | - |
| **one-arm-echo** | Indicates a one-arm BFD echo session. | - |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



BGP uses BFD to quickly detect faults in links between BGP peers. This accelerates network convergence. You can run this command to create a BFD session with default detection parameters for a peer or peer group.If single-hop-prefer is specified, single-hop detection is preferentially used when a BFD session is established between BGP peers. This parameter is used to detect IP connectivity between BGP peers. That is, only one BFD session exists on a specified BGP interface. This parameter is used to ensure that the local and peer ends use the same detection mode when a Huawei device is connected to a non-Huawei device.After a peer is added to a peer group, the peer inherits the BFD configuration of the peer group regardless of whether BFD is enabled on the peer. If the peer does not need to inherit the configuration of the peer group, run the **peer bfd block** command on the peer to prevent the peer from inheriting the BFD function of the peer group.If neither single-hop-prefer nor compatible is specified, the multi-hop mode is used by default when a BFD session is established between BGP peers, and the TTL value in BFD packets is 253 by default.



**Prerequisites**

If a BGP peer is in the Established state, after the **peer bfd enable** command is run to create a BFD session for the peer, the BFD state machine starts about 1 to 20 seconds later. Before the BFD state machine starts, the BFD session cannot be established.

**Configuration Impact**



After this command is run, a BFD session with default parameters can be established between peers or peer groups to rapidly detect link faults.The BFD configuration for a peer takes precedence over that for a peer group. If BFD is not configured on a peer and the peer group to which the peer belongs is enabled with BFD, the peer inherits the BFD configuration from the peer group.



**Precautions**



Before enabling BFD on a BGP peer, enable BFD in the system view. If no BFD detection parameter is specified, a BFD session is established by using default parameter values.If the command is run more than once, the latest configuration overrides the previous one.The **peer bfd block** command and the **peer bfd enable** command are mutually exclusive. After the **peer bfd block** command is run, related BFD sessions are automatically deleted.per-link one-arm-echo is valid only when a VLANIF interface has only one Eth-Trunk interface.




Example
-------

# Configure BFD for peer 192.168.1.1.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 192.168.1.1 as-number 100
[*HUAWEI-bgp] peer 192.168.1.1 bfd enable

```