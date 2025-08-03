peer ssl-policy name (BGP view) (group)
=======================================

peer ssl-policy name (BGP view) (group)

Function
--------



The **peer ssl-policy name** command applies an SSL policy to an SSL client or server.

The **undo peer ssl-policy name** command cancels the configuration of applying an SSL policy to an SSL client or server.



By default, no SSL policy is applied to an SSL client or server.


Format
------

**peer** *group-name* **ssl-policy** **name** *ssl-policy-name*

**undo peer** *group-name* **ssl-policy** **name** *ssl-policy-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **name** *ssl-policy-name* | Specifies the name of an SSL policy. | The value is a string of 1 to 23 case-insensitive characters. The value does not contain spaces. |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The Secure Sockets Layer (SSL) protocol protects data privacy on the Internet by preventing attackers from eavesdropping on data exchanged between a client and a server. Specifically, to ensure data transmission security on a network, an SSL policy needs to be applied to an SSL client or server using the peer ssl-policy name command, and SSL data encryption, identity authentication, and message integrity verification mechanisms need to be used.

**Prerequisites**

An SSL policy has been created using the ssl policy command, and a peer relationship has been established using the peer as-number command.

**Precautions**

The same SSL policy cannot be applied to different SSL roles.The SSL policy configuration for a peer takes precedence over that for a peer group to which the peer belongs.SSL/TLS authentication takes effect only when SSL client and server roles are specified, SSL policies are applied to the client and server, and SSL/TLS authentication is enabled on the server (SSL/TLS authentication is not required on the client).


Example
-------

# Apply the default SSL domain policy to the client.
```
<HUAWEI> system-view
[~HUAWEI] ssl policy ftps_der
[*HUAWEI-ssl-policy-ftps_der] pki-domain default
[*HUAWEI-ssl-policy-ftps_der] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] group test external
[*HUAWEI-bgp] peer test as-number 200
[*HUAWEI-bgp] peer test ssl-policy name ftps_der
Warning: The SSL policy is bound to the default PKI domain, Continue? [Y/N]:y

```

# Apply the SSL policy to an SSL client.
```
<HUAWEI> system-view
[~HUAWEI] ssl policy ftps_der
[*HUAWEI-ssl-policy-ftps_der] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] group test external
[*HUAWEI-bgp] peer test as-number 200
[*HUAWEI-bgp] peer test ssl-policy name ftps_der

```