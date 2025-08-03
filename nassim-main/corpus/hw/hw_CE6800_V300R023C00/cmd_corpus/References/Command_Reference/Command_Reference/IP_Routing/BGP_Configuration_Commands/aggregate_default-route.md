aggregate default-route
=======================

aggregate default-route

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

BGP-IPv4 unicast address family view,BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To enable a BGP device to summarize the routes that match a specified IPv4 prefix list into a summary default route, run the aggregate default-route command. For details about the usage scenario, see "IP Routing" > "BGP Configuration" > "Configuring BGP to Generate a Summary Default Route" in the related configuration guide.

**Prerequisites**

An IPv4 prefix list has been configured using the **ip ip-prefix** command.

**Precautions**

The number of entries in the IPv4 prefix list specified in the aggregate default-route command cannot exceed 200.


Example
-------

# Enable a BGP device to summarize the routes that match an IPv4 prefix list into a summary default route.
```
<HUAWEI> system-view
[~HUAWEI] ip ip-prefix p1 index 10 permit 192.168.1.1 29
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family unicast
[*HUAWEI-bgp-af-ipv4] aggregate default-route origin-ip-prefix p1

```

# Enable a BGP device to summarize the routes that match an IPv4 prefix list into a summary default route and specify an attribute route-policy for the summary default route.
```
<HUAWEI> system-view
[~HUAWEI] ip ip-prefix prefix-a index 10 permit 192.168.1.0 24
[*HUAWEI] route-policy policy1 permit node 10
[*HUAWEI-route-policy] if-match ip-prefix prefix-a
[*HUAWEI-route-policy] apply cost 100
[*HUAWEI-route-policy] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family unicast
[*HUAWEI-bgp-af-ipv4] aggregate default-route origin-ip-prefix prefix-a attribute-policy policy1

```