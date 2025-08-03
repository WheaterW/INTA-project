peer ebgp-max-hop (BGP-VPN instance IPv4 address family view) (IPv4)
====================================================================

peer ebgp-max-hop (BGP-VPN instance IPv4 address family view) (IPv4)

Function
--------



The **peer ebgp-max-hop** command configures a BGP device to establish an EBGP peer relationship with a peer on an indirectly-connected network and set the maximum number of hops between the two devices.

The **undo peer ebgp-max-hop** command cancels the existing configuration.



By default, an EBGP connection can be set up only on a directly-connected physical link.


Format
------

**peer** *ipv4-address* **ebgp-max-hop** [ *hop-count* ]

**undo peer** *ipv4-address* **ebgp-max-hop**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| *hop-count* | Specifies the maximum number of hops. | The value is an integer ranging from 1 to 255. By default, the maximum number of hops in an EBGP connection is 1. If the specified maximum number of hops is 1, EBGP connection cannot be established between non-directly connected devices. If hop-count is not specified in the peer ebgp-max-hop command, 255 is used as the maximum number of hops in EBGP connections. |



Views
-----

BGP-VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Generally, a directly connected physical link must be available between EBGP peers. If a directly connected physical link is unavailable, the **peer ebgp-max-hop** command must be used to allow EBGP peers to establish a multi-hop connection.If loopback interfaces are used to establish an EBGP peer relationship, the **peer ebgp-max-hop** command (hop-count â¥ 2) must be run. Otherwise, the EBGP peer relationship cannot be established.

**Precautions**

If the **peer ebgp-max-hop** command is used on one end of an EBGP connection, it must also be used on the other end.The configurations of GTSM and EBGP-MAX-HOP affect the TTL values of sent BGP packets, and the configurations of the two functions are mutually exclusive.


Example
-------

# Allow indirectly connected EBGP peer to establish a connection with the local device.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpn1
[*HUAWEI-bgp-vpn1] peer 10.1.1.1 as-number 200
[*HUAWEI-bgp-vpn1] peer 10.1.1.1 ebgp-max-hop

```