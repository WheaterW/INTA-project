peer ssl-policy role
====================

peer ssl-policy role

Function
--------



The **peer ssl-policy role client** command configures a peer as an SSL client.

The **undo peer ssl-policy role client** command cancels the SSL client configuration.

The **peer ssl-policy role server** command configures a peer as an SSL server.

The **undo peer ssl-policy role server** command cancels the SSL server configuration.

The **peer ssl-policy role disable** command disables SSL role setting for a peer.

The **undo peer ssl-policy role disable** command restores the default configuration and takes effect only when the peer ssl-policy role disable command is run.



By default, no peer is configured as an SSL client or server.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**peer** { *ipv4-address* | *ipv6-address* } **ssl-policy** **role** **server**

**peer** { *ipv4-address* | *ipv6-address* } **ssl-policy** **role** **client**

**peer** { *ipv4-address* | *ipv6-address* } **ssl-policy** **role** **disable**

**undo peer** { *ipv4-address* | *ipv6-address* } **ssl-policy** **role** **server**

**undo peer** { *ipv4-address* | *ipv6-address* } **ssl-policy** **role** **client**

**undo peer** { *ipv4-address* | *ipv6-address* } **ssl-policy** **role** **disable**

For CE6885-LL (low latency mode):

**peer** *ipv4-address* **ssl-policy** **role** **server**

**peer** *ipv4-address* **ssl-policy** **role** **client**

**peer** *ipv4-address* **ssl-policy** **role** **disable**

**undo peer** *ipv4-address* **ssl-policy** **role** **server**

**undo peer** *ipv4-address* **ssl-policy** **role** **client**

**undo peer** *ipv4-address* **ssl-policy** **role** **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| *ipv6-address* | Specifies the IPv6 address of a peer.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **disable** | Disables SSL role setting for a peer. | - |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The Secure Sockets Layer (SSL) protocol protects data privacy on the Internet by preventing attackers from eavesdropping on data exchanged between a client and a server. Specifically, to ensure data transmission security on a network, a peer needs to be configured as an SSL client using the peer ssl-policy role client command or as a server using the peer ssl-policy role server command, and the SSL data encryption, identity authentication, and message integrity verification mechanisms need to be used.


Example
-------

# Configure a peer as an SSL client.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.2 as-number 100
[*HUAWEI-bgp] peer 10.1.1.2 ssl-policy role client

```