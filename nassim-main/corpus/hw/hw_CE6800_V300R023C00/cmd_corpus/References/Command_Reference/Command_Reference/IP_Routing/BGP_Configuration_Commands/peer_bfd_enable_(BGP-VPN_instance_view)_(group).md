peer bfd enable (BGP-VPN instance view) (group)
===============================================

peer bfd enable (BGP-VPN instance view) (group)

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

**undo peer** *group-name* **bfd** **enable** [ **single-hop-prefer** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a BGP peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **single-hop-prefer** | Preferentially creates a single-hop BFD session for BGP peers. | - |
| **compatible** | Indicates the compatibility mode. If this keyword is specified, the TTL in packets sent by BFD is set to 255. | - |
| **per-link** | Preferentially creates a single-hop BFD session for BGP peers. | - |
| **one-arm-echo** | Indicates a one-arm BFD echo session. | - |



Views
-----

BGP-VPN instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



BGP uses BFD to quickly detect faults in links between BGP peers. This accelerates network convergence. You can run this command to create a BFD session with default detection parameters for a peer or peer group.If single-hop-prefer is specified, single-hop detection is preferentially used when a BFD session is established between BGP peers. This parameter is used to detect IP connectivity between BGP peers. That is, only one BFD session exists on a specified BGP interface. This parameter is used to ensure that the local and peer ends use the same detection mode when a Huawei device is connected to a non-Huawei device.The per-link one-arm-echo parameter enables one-arm BFD echo for each link. This parameter ensures that the local and peer ends use the same detection mode when a Huawei device is connected to a non-Huawei device.After a peer is added to a peer group, the peer inherits the BFD configuration of the peer group regardless of whether BFD is enabled on the peer. If the peer does not need to inherit the configuration of the peer group, run the **peer bfd block** command on the peer to prevent the peer from inheriting the BFD function of the peer group.If neither single-hop-prefer nor compatible is specified, the multi-hop mode is used by default when a BFD session is established between BGP peers, and the TTL value in BFD packets is 253 by default.



**Configuration Impact**



After this command is run, a BFD session with default parameters can be established between peers or peer groups to rapidly detect link faults.The BFD configuration for a peer takes precedence over that for a peer group. If BFD is not configured on a peer and the peer group to which the peer belongs is enabled with BFD, the peer inherits the BFD configuration from the peer group.



**Precautions**



Before enabling BFD on a BGP peer, enable BFD in the system view. If no BFD detection parameter is specified, a BFD session is established by using default parameter values.If the command is run more than once, the latest configuration overrides the previous one.The **peer bfd block** command and the peer bfd enable command are mutually exclusive. After the **peer bfd block** command is run, related BFD sessions are automatically deleted.per-link one-arm-echo is valid only when a VLANIF interface has only one Eth-Trunk interface.




Example
-------

# Configure BFD for a peer group.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] vpn-instance vpn1
[*HUAWEI-bgp-instance-vpn1] group test external
[*HUAWEI-bgp-instance-vpn1] peer test bfd enable

```