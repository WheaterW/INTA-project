aggregate default-route (BGP multi-instance VPN instance IPv4 address family view)
==================================================================================

aggregate default-route (BGP multi-instance VPN instance IPv4 address family view)

Function
--------



The **aggregate default-route** command enables a BGP device to summarize the routes that match a specified IPv4 prefix list into a summary default route.

The **undo aggregate default-route** command restores the default configuration.



By default, BGP cannot summarize the routes that match a specified IPv4 prefix list into a summary default route.


Format
------

**aggregate default-route origin-ip-prefix** *ip-prefix-name* [ **attribute-policy** *attribute-policy-name* ]

**undo aggregate default-route**

**undo aggregate default-route origin-ip-prefix** *ip-prefix-name* [ **attribute-policy** *attribute-policy-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **attribute-policy** *attribute-policy-name* | Specifies the name of an attribute route-policy for the summary default route. | The value is a string ranging from 1 to 200. |
| **origin-ip-prefix** *ip-prefix-name* | Specifies the name of an IPv4 prefix list. | The value is a string of 1 to 169 characters and cannot contain spaces. |



Views
-----

BGP multi-instance VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To prevent traffic that does not match the IPv4 prefix filter from being imported to the local device, run this command to configure the local device to advertise default routes to the peer device based on the IPv4 prefix filter. This saves bandwidth resources. For details, see Configuration - IP Routing - BGP Configuration - Configuring BGP to Summarize Default Routes.



**Prerequisites**



An IPv4 prefix list has been configured using the **ip ip-prefix** command.



**Precautions**



The number of entries in the IPv4 prefix list specified in the aggregate default-route command cannot exceed 200.




Example
-------

# Enable a BGP device to summarize the routes that match an IPv4 prefix list into a summary default route and specify an attribute route-policy for the summary default route.
```
<HUAWEI> system-view
[~HUAWEI] ip ip-prefix prefix-a index 10 permit 192.168.1.1 24
[*HUAWEI] route-policy policy1 permit node 10
[*HUAWEI-route-policy] if-match ip-prefix prefix-a
[*HUAWEI-route-policy] apply cost 100
[*HUAWEI-route-policy] quit
[*HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] router-id 10.1.1.9
[*HUAWEI-bgp-instance-a] ipv4-family vpn-instance vpn1
[*HUAWEI-bgp-instance-a-vpn1] aggregate default-route origin-ip-prefix prefix-a attribute-policy policy1

```

# Enable a BGP device to summarize the routes that match an IPv4 prefix list into a summary default route.
```
<HUAWEI> system-view
[~HUAWEI] ip ip-prefix p1 index 10 permit 192.168.1.1 29
[*HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] router-id 10.1.1.9
[*HUAWEI-bgp-instance-a] ipv4-family vpn-instance vpn1
[*HUAWEI-bgp-instance-a-vpn1] aggregate default-route origin-ip-prefix p1

```