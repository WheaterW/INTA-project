group listen(BGP multi-instance view)
=====================================

group listen(BGP multi-instance view)

Function
--------



The **group listen** command creates a dynamic BGP peer group.

The **undo group listen** command deletes a dynamic BGP peer group.



By default, no dynamic BGP peer groups are created.


Format
------

**group** *peerGroupName* **listen** { **internal** | **external** }

**group** *peerGroupName* **listen**

**undo group** *peerGroupName* **listen** [ **internal** | **external** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerGroupName* | Specifies the name of a dynamic BGP peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **internal** | Creates a dynamic IBGP peer group. | - |
| **external** | Creates a dynamic EBGP peer group. | - |



Views
-----

BGP multi-instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



On a BGP network, multiple peers frequently change, and the establishment of peer relationships changes accordingly. If you configure peers in common mode, you need to frequently add or delete peer configurations on the local device, which increases the maintenance workload. In this case, you can configure the dynamic BGP peer function to enable BGP to listen to BGP connection requests from a specified network segment, dynamically establish BGP peer relationships, and add these peers to the same dynamic peer group. In this manner, when the peer changes, you do not need to add or delete BGP peer configurations on the local end, which reduces the workload of network maintenance. The **group listen** command creates a dynamic BGP peer group.The features of members in a dynamic peer group are the same as those of members in a common peer group. When a peer is added to a dynamic peer group, the peer obtains the same configurations as the peer group.The peers in a peer group can inherit the configurations of the peer group. When the configurations of the peer group are changed, the configurations of the members in the peer group are changed accordingly.After a dynamic BGP peer group is created, if the **peer enable** command is run in an address family view to enable the device to exchange routing information with a specified peer, the **peer enable** command configured in another address family view does not take effect. In this case, you must run the reset bgp command, dynamic neighbor relationships can be established only when they are enabled in other address families.



**Precautions**



If the **group listen** command is run more than once, all configurations take effect.If a dynamic BGP peer group is deleted, connections with all peers in the peer group are deleted.Names of BGP peer groups must be unique, regardless of whether they are of dynamic or static peer groups.If the type (IBGP or EBGP) of a dynamic BGP peer group is not specified, a dynamic IBGP peer group is created by default.Peers in a dynamic BGP peer group share the same attribute. Peer-based attribute configuration is not allowed in a dynamic BGP peer group.The **undo group** command applies to both dynamic and static BGP peer groups. If the command is run, the corresponding peer group and all its configurations are deleted. Therefore, exercise caution when running this command.




Example
-------

# Create a dynamic IBGP peer group named in.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] group in listen internal

```