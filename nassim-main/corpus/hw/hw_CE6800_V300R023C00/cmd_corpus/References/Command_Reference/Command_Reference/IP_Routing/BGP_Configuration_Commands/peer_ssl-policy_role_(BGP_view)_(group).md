peer ssl-policy role (BGP view) (group)
=======================================

peer ssl-policy role (BGP view) (group)

Function
--------



The **peer ssl-policy role client** command configures a peer group as an SSL client.

The **undo peer ssl-policy role client** command cancels the SSL client configuration.

The **peer ssl-policy role server** command configures a peer group as an SSL server.

The **undo peer ssl-policy role server** command cancels the SSL server configuration.



By default, no peer or peer group is configured as an SSL client or server.


Format
------

**peer** *group-name* **ssl-policy** **role** **server**

**peer** *group-name* **ssl-policy** **role** **client**

**undo peer** *group-name* **ssl-policy** **role** **server**

**undo peer** *group-name* **ssl-policy** **role** **client**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The Secure Sockets Layer (SSL) protocol protects data privacy on the Internet by preventing attackers from eavesdropping on data exchanged between a client and a server. Specifically, to ensure data transmission security on a network, a peer group needs to be configured as an SSL client using the peer ssl-policy role client command or as a server using the peer ssl-policy role server command, and the SSL data encryption, identity authentication, and message integrity verification mechanisms need to be used.

**Prerequisites**

A BGP peer relationship has been established using the peer as-number command.

**Precautions**

A set SSL role (server or client) of a peer group cannot be changed to another role unless you first run the peer ssl-policy role disable or undo peer ssl-policy role command to cancel the role configuration of the peer group.If a peer group is configured as an SSL client, the **peer listen-only** command cannot be run. That is, the **peer listen-only** command is mutually exclusive with the peer ssl-policy role client command. If a peer group is configured as an SSL server, the **peer connect-only** command cannot be run. That is, the **peer connect-only** command is mutually exclusive with the peer ssl-policy role client command.The SSL role configuration for a peer takes precedence over that for a peer group to which the peer belongs.SSL/TLS authentication takes effect only when SSL client and server roles are specified, SSL policies are applied to the client and server, and SSL/TLS authentication is enabled on the server (SSL/TLS authentication is not required on the client).


Example
-------

# Configure the peer group named group1 as an SSL client and configure a peer in the peer group as a server.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] group group1 internal
[*HUAWEI-bgp] peer 10.1.1.1 group group1
[*HUAWEI-bgp] peer 10.1.1.2 group group1
[*HUAWEI-bgp] peer 10.1.1.3 group group1
[*HUAWEI-bgp] peer group1 ssl-policy role client
[*HUAWEI-bgp] peer 10.1.1.1 ssl-policy role server

```