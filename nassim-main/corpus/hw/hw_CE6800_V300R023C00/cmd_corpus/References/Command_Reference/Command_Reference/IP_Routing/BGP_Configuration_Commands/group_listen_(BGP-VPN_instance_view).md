group listen (BGP-VPN instance view)
====================================

group listen (BGP-VPN instance view)

Function
--------



The **group listen** command creates a dynamic BGP peer group.

The **undo group listen** command deletes a dynamic BGP peer group.



By default, no dynamic BGP peer groups are created.


Format
------

**group** *group-name* **listen** { **internal** | **external** }

**group** *group-name* **listen**

**undo group** *group-name* **listen** [ **internal** | **external** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a dynamic BGP peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **internal** | Creates a dynamic IBGP peer group. | - |
| **external** | Creates a dynamic EBGP peer group. | - |



Views
-----

BGP-VPN instance view,BGP multi-instance VPN instance session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If static BGP peers change frequently on a BGP network, you need to add or delete BGP peer configurations in response to each change, which requires a heavy maintenance workload. To address this problem, configure the dynamic BGP peer function to enable BGP to listen for BGP connection requests from a specified network segment, dynamically establish BGP peer relationships, and add these peers to the same dynamic peer group. This spares you from adding or deleting BGP peer configurations in response to each change in dynamic peers. To create a dynamic BGP peer group, run the **group listen** command.After a peer is added to a dynamic peer group, the peer inherits the configurations of this peer group. If the configurations of the peer group change, the configurations of all the peers in the group change accordingly. Such implementation is the same as that of static BGP peer groups.

**Precautions**

If the **group listen** command is run more than once, all configurations take effect.If a dynamic BGP peer group is deleted, connections with all peers in the peer group are deleted.Names of BGP peer groups must be unique, regardless of whether they are of dynamic or static peer groups.If the type (IBGP or EBGP) of a dynamic BGP peer group is not specified, a dynamic IBGP peer group is created by default.Peers in a dynamic BGP peer group share the same attribute. Peer-based attribute configuration is not allowed in a dynamic BGP peer group.The **undo group** command applies to both dynamic and static BGP peer groups. If the command is run, the corresponding peer group and all its configurations are deleted. Therefore, exercise caution when running this command.


Example
-------

# Create a dynamic IBGP peer group named in.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] vpn-instance vpn1
[*HUAWEI-bgp-instance-vpn1] group in listen internal

```