peer reflect-client (BGP-VPN-Target address family view) (group)
================================================================

peer reflect-client (BGP-VPN-Target address family view) (group)

Function
--------



The **peer reflect-client** command configures the local device as the route reflector and the peer group as the client of the route reflector.

The **undo peer reflect-client** command cancels the configuration.



By default, the route reflector and its client are not configured.


Format
------

**peer** *group-name* **reflect-client**

**undo peer** *group-name* **reflect-client**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

BGP-VPN-target address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



Full-meshed connections need to be established between IBGP peers to ensure the connectivity between the IBGP peers. If there are n Devices in an AS, n (n-1)/2 IBGP connections need to be established. A large number of IBGP peers use a lot of network and CPU resources. An RR can be used to solve the problem.In an AS, one Device functions as an RR and other Devices function as clients. The clients establish IBGP connections with the RR. The RR and its clients form a cluster. The RR reflects routes among the clients, and therefore the clients do not need to establish any BGP connection. Assume that an AS has n Devices. If one of the Devices functions as an RR, and other Devices function as clients, the number of IBGP connections to be established is n-1. This means that network and CPU resources are greatly reduced.An RR is easy to configure, because it needs to be configured only on the device that functions as a reflector and clients do not need to know that they are clients.



**Configuration Impact**



If the **peer reflect-client** command is run multiple times in the same view, the latest configuration overwrites the previous one.The device where the **peer reflect-client** command is run serves as the RR and a specified peer group serves as the client of the RR.



**Precautions**



The **peer reflect-client** command applies only to IBGP peer groups.The RR information configured in an address family is valid only in this address family and cannot be inherited by other address families. Therefore, you are advised to configure RR information in a specific address family.If this command is run on a specified peer and the **peer advertise best-external** command is run in a specified peer group, the peer cannot inherit the function of the **peer advertise best-external** command when the peer is added to the peer group.




Example
-------

# Configure a peer group as a client of an RR.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp] ipv4-family vpn-target
[*HUAWEI-bgp-af-vpn-target] peer 10.1.1.1 enable
[*HUAWEI-bgp-af-vpn-target] peer 10.1.1.1 reflect-client

```