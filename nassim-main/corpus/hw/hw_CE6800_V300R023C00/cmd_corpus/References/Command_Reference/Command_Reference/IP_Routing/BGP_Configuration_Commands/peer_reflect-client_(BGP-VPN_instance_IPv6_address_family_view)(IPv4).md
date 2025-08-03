peer reflect-client (BGP-VPN instance IPv6 address family view)(IPv4)
=====================================================================

peer reflect-client (BGP-VPN instance IPv6 address family view)(IPv4)

Function
--------



The **peer reflect-client** command configures the local router as the route reflector and the peer as the client of the route reflector.

The **undo peer reflect-client** command cancels the configuration.



By default, the route reflector and its client are not configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *ipv4-address* **reflect-client**

**undo peer** *ipv4-address* **reflect-client**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies the IPv4 address of a peer. | It is in dotted decimal notation. |



Views
-----

BGP-VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Full-meshed connections need to be established between IBGP peers to ensure the connectivity between the IBGP peers. If there are n Devices in an AS, n (n-1)/2 IBGP connections need to be established. A large number of IBGP peers use a lot of network and CPU resources. An RR can be used to solve the problem.In an AS, one Device functions as an RR and other Devices function as clients. The clients establish IBGP connections with the RR. The RR and its clients form a cluster. The RR reflects routes among the clients, and therefore the clients do not need to establish any BGP connection. Assume that an AS has n Devices. If one of the Devices functions as an RR, and other Devices function as clients, the number of IBGP connections to be established is n-1. This means that network and CPU resources are greatly reduced.An RR is easy to configure, because it needs to be configured only on the device that functions as a reflector and clients do not need to know that they are clients.

**Configuration Impact**

If the **peer reflect-client** command is run multiple times in the same view, the latest configuration overwrites the previous one.The device where the **peer reflect-client** command is run serves as the RR and a specified peer serves as the client of the RR.

**Precautions**

The **peer reflect-client** command applies only to IBGP peers.The RR information configured in an address family is valid only in this address family and cannot be inherited by other address families. Therefore, you are advised to configure RR information in a specific address family.If this command is run on a specified peer and the **peer advertise best-external** command is run in a specified peer group, the peer cannot inherit the function of the **peer advertise best-external** command when the peer is added to the peer group.


Example
-------

# Configure a peer as a client of an RR.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv6-family
[*HUAWEI-vpn-instance-vpn1-af-ipv6] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv6] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] vpn-instance vpna
[*HUAWEI-bgp-vpna] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp-vpna] quit
[*HUAWEI-bgp] ipv6-family vpn-instance vpna
[*HUAWEI-bgp-6-vpna] peer 10.1.1.1 enable
[*HUAWEI-bgp-6-vpna] peer 10.1.1.1 reflect-client

```