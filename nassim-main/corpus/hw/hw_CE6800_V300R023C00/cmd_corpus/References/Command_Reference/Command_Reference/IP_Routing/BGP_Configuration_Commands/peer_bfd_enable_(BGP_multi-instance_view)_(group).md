peer bfd enable (BGP multi-instance view) (group)
=================================================

peer bfd enable (BGP multi-instance view) (group)

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
| *group-name* | Specifies the name of a peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **single-hop-prefer** | Preferentially creates a single-hop BFD session for BGP peers. | - |
| **compatible** | Indicates the compatibility mode and sets the TTL value in sent BFD packets to 255. | - |
| **per-link** | Establishes member interface link-based BFD sessions. | - |
| **one-arm-echo** | Indicates a one-arm BFD echo session. | - |



Views
-----

BGP multi-instance view


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



Before enabling BFD on a BGP peer, enable BFD in the system view. If no BFD detection parameter is specified, a BFD session is established using default parameter values.If the command is run more than once, the latest configuration overrides the previous one.NOTE:The **peer bfd block** command and the **peer bfd enable** command are mutually exclusive. After the **peer bfd block** command is run, the BFD session is deleted automatically.




Example
-------

# Configure BFD for peer group.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] quit
[*HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] group test
[*HUAWEI-bgp-instance-a] peer test bfd enable

```