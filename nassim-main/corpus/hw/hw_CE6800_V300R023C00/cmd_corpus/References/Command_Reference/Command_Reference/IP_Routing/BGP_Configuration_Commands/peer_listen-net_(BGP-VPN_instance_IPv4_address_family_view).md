peer listen-net (BGP-VPN instance IPv4 address family view)
===========================================================

peer listen-net (BGP-VPN instance IPv4 address family view)

Function
--------



The **peer listen-net** command specifies a network segment from which a dynamic BGP peer group listens for BGP connection requests.

The **undo peer listen-net** command deletes the specified network segment from which a dynamic BGP peer group listens for BGP connection requests.



By default, no network segment from which a dynamic BGP peer group listens for BGP connection requests is specified.


Format
------

**peer** *group-name* **listen-net** *ipv4-address* [ *mask-length* | *mask* ]

**undo peer** *group-name* **listen-net** *ipv4-address* [ *mask-length* | *mask* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The value is a string of 1 to 47 case-sensitive characters, spaces not supported. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| *ipv4-address* | Specifies a network segment from which the dynamic BGP peer group listens for BGP connection requests. | It is in dotted decimal notation. |
| *mask-length* | Specifies the mask length. A 32-bit mask is represented by consecutive 1s, and the mask in dotted decimal notation can be replaced by the mask length. | The value is an integer in the range from 0 to 32. |
| *mask* | Specifies a subnet mask of an IP address. | It is in dotted decimal notation. |



Views
-----

BGP-VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



On a BGP network, if multiple peers frequently change, the establishment of peer relationships changes accordingly. If you use the common peer configuration mode, you need to frequently add or delete peer configurations on the local end, which increases the maintenance workload. In this case, you can configure the dynamic BGP peer function and specify a network segment from which a dynamic peer group listens for connection requests. After receiving connection requests, BGP dynamically establishes BGP peer relationships and adds these peers to the same dynamic peer group. In this manner, when one of the peers changes, you do not need to add or delete BGP peer configurations on the local end, which reduces the workload of network maintenance. The **peer listen-net** command specifies a network segment from which a dynamic BGP peer group listens for BGP connection requests.



**Prerequisites**



A dynamic BGP peer group has been configured using the group listen [ internal | external ] command. In the case of a dynamic EBGP peer group, a peer AS from which the peer group listens for BGP connection requests must also have been specified using the peer listen-as command.



**Precautions**

* It is recommended that the hold time be set based on the total number of BGP peers in each address family. As the number of peers increases, increase the minimum hold time accordingly. Adjust the hold time according to "Mapping Between the Total Number of BGP Peers in Each Address Family and the Recommended Minimum Hold Time" in the usage guide of the **peer timer** command.
* The same listening network segment cannot be configured in the same VPN instance.


Example
-------

# Specify a network segment from which the dynamic EBGP peer group named ex listens for BGP connection requests.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] group ex listen external
[*HUAWEI-bgp] peer ex listen-as 200
[*HUAWEI-bgp] peer ex listen-net 10.10.10.0 24

```

# Specify a network segment from which the dynamic IBGP peer group named in listens for BGP connection requests.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] group in listen internal
[*HUAWEI-bgp] peer in listen-net 10.10.10.0 24

```