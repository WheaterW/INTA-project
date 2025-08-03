peer listen-net(BGP multi-instance VPN instance view)
=====================================================

peer listen-net(BGP multi-instance VPN instance view)

Function
--------



The **peer listen-net** command specifies a network segment from which a dynamic BGP peer group listens for BGP connection requests.

The **undo peer listen-net** command deletes the specified network segment from which a dynamic BGP peer group listens for BGP connection requests.



By default, no network segment from which a dynamic BGP peer group listens for BGP connection requests is specified.


Format
------

**peer** *peerGroupName* **listen-net** *ipv4-address* [ *mask-length* | *mask* ]

**undo peer** *peerGroupName* **listen-net** *ipv4-address* [ *mask-length* | *mask* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerGroupName* | Specifies the name of a dynamic BGP peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| *ipv4-address* | Specifies the network segment from which the dynamic peer group listens for connection requests. | It is in dotted decimal notation. |
| *mask-length* | Indicates the length of an address mask. | The value is an integer ranging from 0 to 32. |
| *mask* | Specifies the mask of an IP address. | It is in dotted decimal notation. |



Views
-----

BGP multi-instance VPN instance session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a BGP network, if multiple peers frequently change, the establishment of peer relationships changes accordingly. If you use the common peer configuration mode, you need to frequently add or delete peer configurations on the local end, which increases the maintenance workload. In this case, you can configure the dynamic BGP peer function and specify a network segment from which a dynamic peer group listens for connection requests. After receiving connection requests, BGP dynamically establishes BGP peer relationships and adds these peers to the same dynamic peer group. In this manner, when one of the peers changes, you do not need to add or delete BGP peer configurations on the local end, which reduces the workload of network maintenance. The **peer listen-net** command specifies a network segment from which a dynamic BGP peer group listens for BGP connection requests.

**Prerequisites**

A dynamic BGP peer group has been created using the group listen [ internal | external ] command. If EBGP peers are created, the peer listen-as command must also be run to specify a peer AS from which the dynamic BGP peer group listens for BGP connection requests.

**Precautions**

* If you run the **undo peer listen-net** command to delete the network segment from which a dynamic peer group listens for BGP connection requests, the corresponding dynamic peers are not deleted. However, if the dynamic peers are disconnected, they cannot be reconnected.
* If both dynamic and static peers are configured on the local end, when the peer end attempts to establish a connection with the local end, the static peer relationship is preferentially established.
* If you run the **peer listen-net** command more than once, all configurations take effect.
* It is recommended that the hold time be set based on the total number of BGP peers in each address family. As the number of peers increases, increase the minimum hold time accordingly. Adjust the hold time according to "Mapping Between the Total Number of BGP Peers in Each Address Family and the Recommended Minimum Hold Time" in the usage guide of the **peer timer** command.
* The same listening network segment cannot be configured in the same VPN instance.

Example
-------

# Specify a network segment from which the dynamic IBGP peer group named in listens for BGP connection requests.
```
<HUAWEI> system
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] route-distinguisher 1:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] bgp 100 instance a
[*HUAWEI-bgp-instance-a] vpn-instance vpna
[*HUAWEI-bgp-instance-a-instance-vpna] group in listen internal
[*HUAWEI-bgp-instance-a-instance-vpna] peer in listen-net 10.10.10.0 24

```