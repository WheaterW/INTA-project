peer enable(BGP-IPv4 unicast address family view) (IPv6)
========================================================

peer enable(BGP-IPv4 unicast address family view) (IPv6)

Function
--------



The **peer enable** command enables a BGP device to exchange routes with a specified peer group in the address family view.

The **undo peer enable** command disables a BGP device from exchanging routes with a specified peer group.



By default, route exchange with a specified peer is enabled only in the BGP-IPv4 unicast address family.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *peerIpv6Addr* **enable**

**undo peer** *peerIpv6Addr* **enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv6Addr* | Specifies the IPv6 address of a peer. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

BGP-IPv4 unicast address family view


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

If a peer has established a peer relationship in another address family when you run this command, running the **peer enable** command may disconnect and re-establish the peer relationship in all other address families of the peer (using the same address), causing route flapping. Therefore, exercise caution when running this command.


Example
-------

# Enable the device to exchange routing information with a specified peer in the address family view.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 2001:DB8:1::1 as-number 100
[*HUAWEI-bgp] ipv4-family unicast
[*HUAWEI-bgp-af-ipv4] peer 2001:DB8:1::1 enable

```