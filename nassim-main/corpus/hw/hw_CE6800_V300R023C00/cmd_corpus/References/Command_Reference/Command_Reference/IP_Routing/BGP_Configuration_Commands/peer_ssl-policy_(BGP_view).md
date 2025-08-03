peer ssl-policy (BGP view)
==========================

peer ssl-policy (BGP view)

Function
--------



The **peer ssl-policy name** command applies an SSL policy to an SSL client or server.

The **peer ssl-policy disable** command disables an SSL policy applied to an SSL client or server.

The **undo peer ssl-policy name** command cancels the configuration of applying an SSL policy to an SSL client or server.

The **undo peer ssl-policy disable** command restores the default configuration and takes effect only when the peer ssl-policy disable command is run.



By default, no SSL policy is applied to an SSL client or server.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**peer** { *ipv4-address* | *ipv6-address* } **ssl-policy** **name** *ssl-policy-name*

**peer** { *ipv4-address* | *ipv6-address* } **ssl-policy** **disable**

**undo peer** { *ipv4-address* | *ipv6-address* } **ssl-policy** **name** *ssl-policy-name*

**undo peer** { *ipv4-address* | *ipv6-address* } **ssl-policy** **disable**

For CE6885-LL (low latency mode):

**peer** *ipv4-address* **ssl-policy** **name** *ssl-policy-name*

**peer** *ipv4-address* **ssl-policy** **disable**

**undo peer** *ipv4-address* **ssl-policy** **name** *ssl-policy-name*

**undo peer** *ipv4-address* **ssl-policy** **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| *ipv6-address* | Specifies the IPv6 address of a peer.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **name** *ssl-policy-name* | Specifies the name of an SSL policy. | The value is a string of 1 to 23 case-insensitive characters. The value does not contain spaces. |
| **disable** | Disables an SSL policy applied to an SSL client or server. | - |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The Secure Sockets Layer (SSL) protocol protects data privacy on the Internet by preventing attackers from eavesdropping on data exchanged between a client and a server. Specifically, to ensure data transmission security on a network, an SSL policy needs to be applied to an SSL client or server using the peer ssl-policy name command, and SSL data encryption, identity authentication, and message integrity verification mechanisms need to be used.


Example
-------

# Apply the SSL policy named ftps\_der to an SSL client.
```
<HUAWEI> system-view
[~HUAWEI] ssl policy ftps_der
[*HUAWEI-ssl-policy-ftps_der] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp] peer 10.1.1.1 ssl-policy name ftps_der

```

# Apply the SSL default domain policy ftps\_der to the client.
```
<HUAWEI> system-view
[~HUAWEI] ssl policy ftps_der
[*HUAWEI-ssl-policy-ftps_der] pki-domain default
[*HUAWEI-ssl-policy-ftps_der] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp] peer 10.1.1.1 ssl-policy name ftps_der
Warning: The SSL policy is bound to the default PKI domain, Continue? [Y/N]:y

```