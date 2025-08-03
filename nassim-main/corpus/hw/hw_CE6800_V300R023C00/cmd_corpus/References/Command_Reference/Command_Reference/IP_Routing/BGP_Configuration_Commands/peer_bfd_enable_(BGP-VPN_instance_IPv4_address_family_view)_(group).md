peer bfd enable (BGP-VPN instance IPv4 address family view) (group)
===================================================================

peer bfd enable (BGP-VPN instance IPv4 address family view) (group)

Function
--------



The **peer bfd enable** command enables a device to establish a BFD session with its peer group using default detection parameter values.

The **undo peer bfd enable** command cancels this function.



By default, a BGP device does not establish any BFD session with its peer group.


Format
------

**peer** *group-name* **bfd** **enable** [ **single-hop-prefer** ] [ **compatible** ]

**peer** *group-name* **bfd** **enable** **per-link** **one-arm-echo**

**peer** *group-name* **bfd** **enable** **one-arm-echo**

**undo peer** *group-name* **bfd** **enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a BGP peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |
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



BGP uses BFD to quickly detect faults in links between BGP peers. This accelerates network convergence. You can run this command to create a BFD session with default detection parameters for a peer or peer group.



**Prerequisites**



If a BGP peer is in the Established state, after the **peer bfd enable** command is run to create a BFD session for the peer, the BFD state machine starts about 1 to 20 seconds later. Before the BFD state machine starts, the BFD session cannot be established.



**Configuration Impact**



After the **peer bfd enable** command is enabled, peers or peer groups can establish IPv6 BFD sessions using default parameter values. This allows fast link fault detection.The BFD configuration of a peer takes precedence over that of the peer group to which the peer belongs. If BFD is not configured on a peer and the peer group to which the peer belongs is enabled with BFD, the peer inherits the BFD configurations from the peer group.



**Precautions**



Before enabling BFD on a BGP peer, enable BFD in the system view. If no BFD detection parameter is specified, a BFD session is established by using default parameter values.If the command is run more than once, the latest configuration overrides the previous one.The **peer bfd block** command and the **peer bfd enable** command are mutually exclusive. After the **peer bfd block** command is run, related BFD sessions are automatically deleted.per-link one-arm-echo is valid only when a VLANIF interface has only one Eth-Trunk interface.




Example
-------

# Configure BFD for a peer group.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpn1
[*HUAWEI-bgp-vpn1] group test external
[*HUAWEI-bgp-vpn1] peer test as-number 200
[*HUAWEI-bgp-vpn1] peer test bfd enable

```