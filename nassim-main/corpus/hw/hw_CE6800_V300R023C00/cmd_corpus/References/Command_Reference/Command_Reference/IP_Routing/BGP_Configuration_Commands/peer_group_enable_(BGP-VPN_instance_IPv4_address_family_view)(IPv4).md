peer group enable (BGP-VPN instance IPv4 address family view)(IPv4)
===================================================================

peer group enable (BGP-VPN instance IPv4 address family view)(IPv4)

Function
--------



The **peer group enable** command enables a peer to be added to a peer group in the BGP VPN instance address family.

The **undo peer group enable** command disables a peer from being added to a peer group in the BGP VPN instance address family.



By default, a peer is disabled from being added to a peer group in the BGP VPN instance address family.


Format
------

**peer** *ipv4-address* **group** *group-name* **enable**

**undo peer** *ipv4-address* **group** *group-name* **enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| *group-name* | Specifies the name of a BGP peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

BGP-VPN instance IPv4 address family view,BGP multi-instance VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

A large number of BGP peers may exist on a large-scale BGP network. Among these BGP peers, many of them may use the same policies and have the same command configurations. In this situation, you can use peer groups to simplify configurations. Specifically, when configuring multiple peers in the same way, you can create and configure a peer group, and add multiple peers to the peer group. Then, all peers in the peer group will inherit the configurations of the peer group. The **peer group enable** command enables a peer to be added to a peer group in the BGP VPN instance address family. After being added to a peer group, a peer automatically inherits the configurations of the peer group.


Example
-------

# Create an IBGP peer group named test and add a peer to the peer group.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] vpn-instance vpn1
[*HUAWEI-bgp-instance-vpn1] group test internal
[*HUAWEI-bgp-instance-vpn1] peer 10.1.1.1 group test
[*HUAWEI-bgp-instance-vpn1] quit
[*HUAWEI-bgp] ipv4-family vpn-instance vpn1
[*HUAWEI-bgp-vpn1] peer test enable
[*HUAWEI-bgp-vpn1] peer 10.1.1.1 group test enable

```