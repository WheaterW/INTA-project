peer extended-open-message(BGP View)
====================================

peer extended-open-message(BGP View)

Function
--------



The **peer extended-open-message** command enables the capability of extending optional parameters in BGP Open messages.

The **undo peer extended-open-message** command restores the default configuration.



By default, Open messages longer than 255 bytes cannot be packed.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**peer** { *peerIpv4Addr* | *peerIpv6Addr* } **extended-open-message** **disable**

**peer** { *peerIpv4Addr* | *peerIpv6Addr* } **extended-open-message**

**undo peer** { *peerIpv4Addr* | *peerIpv6Addr* } **extended-open-message**

**undo peer** { *peerIpv4Addr* | *peerIpv6Addr* } **extended-open-message** **disable**

For CE6885-LL (low latency mode):

**peer** { *peerIpv4Addr* } **extended-open-message** **disable**

**peer** { *peerIpv4Addr* } **extended-open-message**

**undo peer** { *peerIpv4Addr* } **extended-open-message**

**undo peer** { *peerIpv4Addr* } **extended-open-message** **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv4Addr* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| *peerIpv6Addr* | Specifies the IPv6 address of a peer.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **disable** | Disables the function. | - |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

With the increase of BGP capabilities, when a BGP session negotiates multiple capabilities, the length of an Open message may exceed 255 bytes. You can run the **peer extended-open-message** command to configure the extended format of an Open message so that the Open message longer than 255 bytes can be packed.After the **peer extended-open-message disable** command is run, a peer in a peer group retains the default configuration but does not inherit the configuration of the peer group.

**Precautions**

When the BGP session of the local device negotiates multiple capabilities, the length of the optional parameter in the Open packet exceeds 255. When the local device sends an extended Open packet to the peer device, if the peer device does not support the extended Open packet function, the local device cannot establish a neighbor relationship with the peer device, and the established neighbor relationship may be disconnected. Exercise caution when setting this parameter.


Example
-------

# Disable the extended format of Open messages.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp] peer 10.1.1.1 extended-open-message disable

```

# Enable the extended format of Open messages.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp] peer 10.1.1.1 extended-open-message

```