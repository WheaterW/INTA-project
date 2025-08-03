peer reflect-client (BGP-VPN instance IPv6 address family view) (group)
=======================================================================

peer reflect-client (BGP-VPN instance IPv6 address family view) (group)

Function
--------



The **peer reflect-client** command configures the local device as the route reflector and a peer group as the client of the route reflector.

The **undo peer reflect-client** command cancels the existing configuration.



By default, the route reflector and its client are not configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *group-name* **reflect-client**

**undo peer** *group-name* **reflect-client**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

BGP-VPN instance IPv6 address family view,BGP multi-instance VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Full-meshed connections need to be established between IBGP peers to ensure the connectivity between the IBGP peers. If there are n Devices in an AS, n (n-1)/2 IBGP connections need to be established. A large number of IBGP peers use a lot of network and CPU resources. An RR can be used to solve the problem.In an AS, one Device functions as an RR and other Devices function as clients. The clients establish IBGP connections with the RR. The RR and its clients form a cluster. The RR reflects routes among the clients, and therefore the clients do not need to establish any BGP connection. Assume that an AS has n Devices. If one of the Devices functions as an RR, and other Devices function as clients, the number of IBGP connections to be established is n-1. This means that network and CPU resources are greatly reduced.An RR is easy to configure, because it needs to be configured only on the device that functions as a reflector and clients do not need to know that they are clients.

**Configuration Impact**

If the **peer reflect-client** command is run multiple times in the same view, the latest configuration overwrites the previous one.After the **peer reflect-client** command is run, the local device functions as the RR and the specified peer group functions as the client of the RR.

**Precautions**

The **peer reflect-client** command applies only to IBGP peer groups.The RR information configured in an address family is valid only in this address family and cannot be inherited by other address families. Therefore, you are advised to configure RR information in a specific address family.If this command is run on a specified peer and the **peer advertise best-external** command is run in a specified peer group, the peer cannot inherit the function of the **peer advertise best-external** command when the peer is added to the peer group.


Example
-------

# Configure a peer group as a client of an RR.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv6-family
[*HUAWEI-vpn-instance-vpn1-af-ipv6] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpn1-af-ipv6] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpn1
[*HUAWEI-bgp-6-vpn1] group test internal
[*HUAWEI-bgp-6-vpn1] peer test reflect-client

```