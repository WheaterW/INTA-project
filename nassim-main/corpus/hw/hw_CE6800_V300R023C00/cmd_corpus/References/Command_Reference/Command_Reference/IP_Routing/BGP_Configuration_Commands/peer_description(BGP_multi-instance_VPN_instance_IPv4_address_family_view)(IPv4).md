peer description(BGP multi-instance VPN instance IPv4 address family view)(IPv4)
================================================================================

peer description(BGP multi-instance VPN instance IPv4 address family view)(IPv4)

Function
--------



The **peer description** command configures a description for a peer.

The **undo peer description** command deletes the description of a peer.



By default, no description is configured for a peer.


Format
------

**peer** *ipv4-address* **description** *description-text*

**undo peer** *ipv4-address* **description**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies the IPv4 address of a peer. | The value is in dotted decimal notation. |
| *description-text* | Specifies a description. | The value is a string of 1 to 255 characters. Letters, digits, and spaces are supported. |



Views
-----

BGP multi-instance VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



The peer description can be used to configure a description for a peer, which facilitates management of peers or peer groups. The description records information about the peer, such as the VPN instance to which the peer belongs, and devices that establish peer relationships with the peer.



**Implementation Procedure**



The description configured by using the **peer description** command for a peer is displayed from the first non-space character.



**Configuration Impact**



If the **peer description** command is run multiple times to configure a description for a peer, the latest configuration overwrites the previous one.



**Follow-up Procedure**



You can run display bgp peer verbose command can be used to view the description of a peer.




Example
-------

# Configure a description for a peer.
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
[*HUAWEI-bgp-instance-a-vpna] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp-instance-a-vpna] peer 10.1.1.1 description ISP1

```