peer ssl-server certificate (BGP view) (group)
==============================================

peer ssl-server certificate (BGP view) (group)

Function
--------



The **peer ssl-server certificate** command enables SSL/TLS authentication on an SSL server.

The **undo peer ssl-server certificate** command cancels SSL/TLS authentication on an SSL server.



By default, SSL/TLS authentication is disabled on an SSL server.


Format
------

**peer** *group-name* **ssl-server** **certificate**

**undo peer** *group-name* **ssl-server** **certificate**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a BGP peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |



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
[*HUAWEI-bgp] group test external
[*HUAWEI-bgp] peer test as-number 200
[*HUAWEI-bgp] peer test ssl-server certificate

```