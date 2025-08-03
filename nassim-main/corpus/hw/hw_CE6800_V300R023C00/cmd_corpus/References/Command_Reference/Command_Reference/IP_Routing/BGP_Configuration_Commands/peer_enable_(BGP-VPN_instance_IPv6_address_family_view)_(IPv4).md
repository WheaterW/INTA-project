peer enable (BGP-VPN instance IPv6 address family view) (IPv4)
==============================================================

peer enable (BGP-VPN instance IPv6 address family view) (IPv4)

Function
--------



The **peer enable** command enables a BGP device to exchange routes with a specified peer group in the address family view.

The **undo peer enable** command disables a BGP device from exchanging routes with a specified peer group.



By default, a device is disabled from exchanging routing information with a specified peer.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *ipv4-address* **enable**

**undo peer** *ipv4-address* **enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |



Views
-----

BGP-VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By default, only peer groups in the BGP-IPv4 unicast address family are automatically enabled to exchange routing information. In other words, after the **peer as-number** command is run in the BGP view, the system automatically configures the **peer enable** command. In other address family views, however, this function must be manually enabled.

**Configuration Impact**

Enabling or disabling a BGP peer in this address family causes the BGP connection with the peer in another address family to be disconnected and automatically renegotiated.

**Precautions**

To run the command in the BGP VPN instance IPv4 address family view or BGP VPN instance IPv6 address family view, ensure that the related BGP peers and BGP peer groups have been configured in the BGP VPN instance.If the peer has established a peer relationship in another address family, running the **peer enable** command may disconnect and re-establish all peer relationships with the peer, causing route flapping. Therefore, exercise caution when running this command.


Example
-------

# Enable the device to exchange routing information with a specified peer in the address family view.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv6-family
[*HUAWEI-vpn-instance-vpn1-af-ipv6] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv6] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] vpn-instance vpna
[*HUAWEI-bgp-vpna] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp-vpna] quit
[*HUAWEI-bgp] ipv6-family vpn-instance vpna
[*HUAWEI-bgp-6-vpna] peer 10.1.1.1 enable

```