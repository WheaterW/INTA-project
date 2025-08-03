peer tcp-mss (BGP-VPN instance IPv6 address family view) (IPv6)
===============================================================

peer tcp-mss (BGP-VPN instance IPv6 address family view) (IPv6)

Function
--------



The **peer tcp-mss** command configures a TCP MSS value used when the local device establishes TCP connections with a peer.

The **undo peer tcp-mss** command deletes the configured TCP MSS value.



By default, no TCP MSS is configured for the local device to establish TCP connections with a peer.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *ipv6-address* **tcp-mss** *tcp-mss-number*

**undo peer** *ipv6-address* **tcp-mss**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies an IPv6 peer address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *tcp-mss-number* | Specifies the maximum TCP MSS value used for TCP connection establishment. | The value is an integer ranging from 176 to 4096, in bytes. |



Views
-----

BGP-VPN instance IPv6 address family view,BGP multi-instance VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **peer tcp-mss** command to configure a TCP MSS value used during TCP connection establishment with the specified peer. The value ranges from 176 to 4096 and is used to fragment TCP packets when the path MTU is unavailable. Such configuration improves network performance.

**Precautions**

If you change the tcp-mss-number value, the TCP connection will be re-established.If both the peer tcp-mss and peer path-mtu auto-discovery commands are run, note the following rules:

* If the local device obtains the path MTU, the smaller value of TCP MSS and path MTU takes effect.
* If the local device fails to obtain the path MTU, TCP MSS takes effect.


Example
-------

# Configure a TCP MSS value for the local device to establish TCP connections with the peer.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv6-family
[*HUAWEI-vpn-instance-vpn1-af-ipv6] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv6] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpna
[*HUAWEI-bgp-6-vpna] peer 2001:DB8:1::1 as-number 100
[*HUAWEI-bgp-6-vpna] peer 2001:DB8:1::1 tcp-mss 200

```