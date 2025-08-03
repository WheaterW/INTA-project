peer ebgp-max-hop (BGP multi-instance VPN instance IPv4 address family view) (group)
====================================================================================

peer ebgp-max-hop (BGP multi-instance VPN instance IPv4 address family view) (group)

Function
--------



The **peer ebgp-max-hop** command configures a BGP device to establish an EBGP peer relationship with a peer on an indirectly-connected network and set the maximum number of hops between the two devices.

The **undo peer ebgp-max-hop** command cancels the existing configuration.



By default, an EBGP connection can be set up only on a directly-connected physical link.


Format
------

**peer** *group-name* **ebgp-max-hop** [ *hop-count* ]

**undo peer** *group-name* **ebgp-max-hop**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a BGP peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| *hop-count* | Specifies the maximum number of hops. | The value is an integer ranging from 1 to 255. By default, the maximum number of hops in an EBGP connection is 1. If the specified maximum number of hops is 1, EBGP connection cannot be established between non-directly connected devices. If hop-count is not specified in the peer ebgp-max-hop command, 255 is used as the maximum number of hops in EBGP connections. |



Views
-----

BGP multi-instance VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



Generally, a directly connected physical link must be available between EBGP peers. If a directly connected physical link is unavailable, the **peer ebgp-max-hop** command must be used to allow EBGP peers to establish a multi-hop connection.If loopback interfaces are used to establish an EBGP peer relationship, the **peer ebgp-max-hop** command (hop-count greater than or equal to 2) must be run. Otherwise, the EBGP peer relationship cannot be established.



**Precautions**



If the **peer ebgp-max-hop** command is used on one end of an EBGP connection, it must also be used on the other end.The configurations of GTSM and EBGP-MAX-HOP affect the TTL values of sent BGP packets, and the configurations of the two functions are mutually exclusive.




Example
-------

# Allow indirectly connected EBGP peer group to establish a connection with the local device.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-instance-vpna] quit
[*HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] ipv4-family vpn-instance vpna
[*HUAWEI-bgp-instance-a-vpna] group test external
[*HUAWEI-bgp-instance-a-vpna] peer test ebgp-max-hop

```