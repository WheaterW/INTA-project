peer enable (BGP-VPN-Target address family view)
================================================

peer enable (BGP-VPN-Target address family view)

Function
--------



The **peer enable** command enables a BGP device to exchange routes with a specified peer in the address family view.

The **undo peer enable** command disables a BGP device from exchanging routes with a specified peer.



By default, a device is disabled from exchanging routing information with a specified peer.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**peer** { *ipv4-address* | *ipv6-address* } **enable**

**undo peer** { *ipv4-address* | *ipv6-address* } **enable**

For CE6885-LL (low latency mode):

**peer** *ipv4-address* **enable**

**undo peer** *ipv4-address* **enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies the IPv4 address of a peer. | It is in dotted decimal notation. |
| *ipv6-address* | Specifies an IPv6 peer address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |



Views
-----

BGP-VPN-target address family view


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

If the device has established peer relationships with a peer in other address families, running the **peer enable** command may disconnect and re-establish all peer relationships with the peer, causing route flapping. Therefore, exercise caution when running this command.A large number of VPN ORF peer relationships may compromise the performance.


Example
-------

# Enable the device to exchange routing information with a specified peer in the address family view.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.2.2.2 as-number 100
[*HUAWEI-bgp] ipv4-family vpn-target
[*HUAWEI-bgp-af-vpn-target] peer 10.2.2.2 enable

```