peer ssl-server certificate
===========================

peer ssl-server certificate

Function
--------



The **peer ssl-server certificate** command enables SSL/TLS authentication on an SSL server.

The **peer ssl-server certificate disable** command disables SSL/TLS authentication on an SSL server.

The **undo peer ssl-server certificate** command cancels SSL/TLS authentication on an SSL server.

The **undo peer ssl-server certificate disable** command cancels the configuration of SSL/TLS authentication on an SSL server.



By default, SSL/TLS authentication is disabled on an SSL server.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**peer** { *ipv4-address* | *ipv6-address* } **ssl-server** **certificate**

**peer** { *ipv4-address* | *ipv6-address* } **ssl-server** **certificate** **disable**

**undo peer** { *ipv4-address* | *ipv6-address* } **ssl-server** **certificate**

**undo peer** { *ipv4-address* | *ipv6-address* } **ssl-server** **certificate** **disable**

For CE6885-LL (low latency mode):

**peer** *ipv4-address* **ssl-server** **certificate**

**peer** *ipv4-address* **ssl-server** **certificate** **disable**

**undo peer** *ipv4-address* **ssl-server** **certificate**

**undo peer** *ipv4-address* **ssl-server** **certificate** **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| *ipv6-address* | Specifies the IPv6 address of a peer.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **disable** | Disables SSL/TLS authentication on an SSL server. | - |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The Secure Sockets Layer (SSL) protocol protects data privacy on the Internet by preventing attackers from eavesdropping on data exchanged between a client and a server. The Transport Layer Security (TLS) protocol is an SSL successor and ensures data integrity and privacy. To enable SSL/TLS authentication on an SSL server, run the peer ssl-server certificate command. BGP messages are then encrypted to ensure data transmission security on the network.


Example
-------

# Enable SSL/TLS authentication on an SSL server.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.2 as-number 100
[*HUAWEI-bgp] peer 10.1.1.2 ssl-server certificate

```