peer update-group-independent (BGP-VPN instance IPv4 address family view) (group)
=================================================================================

peer update-group-independent (BGP-VPN instance IPv4 address family view) (group)

Function
--------



The **peer update-group-independent** command sets each peer in a peer group as an independent update peer-group.

The **undo peer update-group-independent** command disables each peer in a peer group from being set as an independent update peer-group.



By default, no peer is set as an independent update peer-group.


Format
------

**peer** *group-name* **update-group-independent**

**undo peer** *group-name* **update-group-independent**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a BGP peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

BGP-VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To improve the efficiency of route advertisement, BGP uses the dynamic update peer-group mechanism. The BGP peers with the same configurations are placed in an update peer-group. These routes are grouped once and then sent to all peers in the update peer-group. However, the routes learned from a peer may be sent back to the peer, for example, the preferred route learned from an EBGP peer is sent back to the EBGP peer, or the preferred route that an RR learns from a client is reflected back to the client. In this case, messages are discarded, wasting network resources.To address this problem, you can run the **peer update-group-independent** command to set a specified peer or each peer in a peer group as an independent update peer-group so that the routes learned from the peer are not sent back to the peer. However, if a specified peer or each peer in a peer group is set as an independent update peer-group, the advantages of the dynamic update peer-group mechanism cannot be brought into full play. Therefore, this command is used only when users have such a requirement.



**Prerequisites**



A peer group has been added to an update peer-group using the peer group command.



**Precautions**



The configuration of a peer takes precedence over that of the peer group to which the peer belongs. For example, if the **peer update-group-independent disable** command is run for a peer and the **peer update-group-independent** command is run for the peer group to which the peer belongs, the configuration of the peer prevails. That is, the peer is not set as an independent update peer-group.On a device with a large memory, you are advised to run the **peer update-group-independent** command to prevent network resource waste by route sending back.




Example
-------

# Set a specified peer or each peer in a peer group as an independent update peer-group.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] vpn-instance vpna
[*HUAWEI-bgp-instance-vpna] group test
[*HUAWEI-bgp-instance-vpna] quit
[*HUAWEI-bgp] ipv4-family vpn-instance vpna
[*HUAWEI-bgp-vpna] peer test enable
[*HUAWEI-bgp-vpna] peer test update-group-independent

```