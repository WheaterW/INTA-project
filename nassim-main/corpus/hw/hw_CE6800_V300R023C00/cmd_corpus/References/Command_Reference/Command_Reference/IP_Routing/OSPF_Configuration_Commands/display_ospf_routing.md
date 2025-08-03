display ospf routing
====================

display ospf routing

Function
--------



The **display ospf routing** command displays the OSPF routing table.




Format
------

**display ospf** [ *process-id* ] **routing** [ *ip-address* [ *mask* | *mask-length* ] ] [ [ **interface** { *interface-name* | *interfaceType* *interfaceNum* } ] [ **nexthop** *nexthop-ip-address* ] ] \* [ **age** { **min-value** *min-age-value* | **max-value** *max-age-value* } \* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | OSPF process ID. | The value ranges from 1 to 4294967295. |
| *ip-address* | Indicates destination IP addresses. | The value is in dotted decimal notation. |
| *mask* | Specifies a subnet mask. | The value is in dotted decimal notation. |
| *mask-length* | Specifies the length of the prefix. | The value is an integer ranging from 0 to 32. |
| **interface** *interfaceType* *interfaceNum* | Specifies the type or the number of an interface. | - |
| **interface** *interface-name* | Specifies an interface name. | The value is a character string. |
| **nexthop** *nexthop-ip-address* | Specifies the next-hop address. | The value is in dotted decimal notation. |
| **age** | Displays information based on the age time. | - |
| **min-value** *min-age-value* | Displays information about OSPF routes with the age value greater than or equal to the min-age-value value. | The value is an integer ranging from 0 to 4294967295. |
| **max-value** *max-age-value* | Displays information only about LSAs with the age value less than or equal to the max-age-value value. | The value is an integer ranging from 0 to 4294967295. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

By using this command with different parameters, you can view the routes of a specified interface or next hop.The command output can help you troubleshoot OSPF faults.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the OSPF routes to a specified destination address.
```
<HUAWEI> display ospf routing 10.1.1.1

OSPF Process 1 with Router ID 1.1.1.1

 Destination    : 10.1.1.0/24
 AdverRouter    : 10.1.1.1             Tag                 : 1
 Cost           : 1                    Type                : Type2
 NextHop        : 10.1.2.2             Interface           : 100GE1/0/1
 Priority       : High                 Age                 : 00h00m00s
 Backup NextHop : 10.1.3.3             Backup Interface    : 100GE1/0/1
 Backup Type    : LFA LINK

```

# Display the OSPF routing table.
```
<HUAWEI> display ospf routing

OSPF Process 1 with Router ID 4.4.4.4

 Routing for Network
 ------------------------------------------------------------------------------
 Destination        Cost      Type           Next-Hop         AdvRouter       Area
 172.16.1.0/24      1         Inter-area     192.168.2.1     2.2.2.2         0.0.0.2
                    4         Inter-area     192.168.2.3     2.2.2.2         0.0.0.2
 192.168.0.0/24     2         Inter-area     192.168.2.1     2.2.2.2         0.0.0.2
 
 Total Nets: 3
 Intra Area: 1  Inter Area: 2  ASE: 0  NSSA: 0

```

# Display information about OSPF routes with a specified next hop address.
```
<HUAWEI> system-view
[~HUAWEI] display ospf routing nexthop 10.1.1.1

          OSPF Process 1 with Router ID 10.1.1.1

 Destination    : 10.1.1.0/24
 AdverRouter    : 10.1.1.1                 Area                : 0.0.0.0
 Cost           : 1                        Type                : Direct
 NextHop        : 10.1.1.1                 Interface           : Eth1/0/1
 Priority       : Low                      Age                 : 622h07m54s
 CalculateTime  : 2023-04-11 09:43:07.642  DownloadTime        : 2023-04-24 09:56:19.223
 Flags          : A/-

```

# Display the routes to a specified OSPF router.
```
<HUAWEI> display ospf routing router-id 10.1.1.1
OSPF Process 1 with Router ID 10.1.1.1

 Destination    : 10.1.1.2             Route Type          : Intra-area
 Area           : 0.0.0.1              AdvRouter           : 10.1.1.2
 Type           : ASBR                 Age                 : 00:00:33
 URT Cost       : 1
 NextHop        : 10.1.2.2             Interface           : 100GE1/0/1
 Backup NextHop : 10.1.3.3             Backup Interface    : 100GE1/0/1
 Backup Type    : LFA LINK

```

**Table 1** Description of the **display ospf routing** command output
| Item | Description |
| --- | --- |
| Destination | Destination network. |
| AdverRouter | Advertiser. |
| Tag | Route distinguisher. |
| Cost | Cost to the destination address. |
| Type | Type of the destination network:   * Inter-area: inter-area routes. * Stub: routes advertised through router LSAs. The routes correspond to the direct routes of non-broadcast and non-NBMA networks. * Transit: routes advertised through network-LSAs. * Direct: direct route. |
| NextHop | Next-hop address to the destination address. |
| Interface | Outbound interface of a route. |
| Priority | Priority of a route.   * Critical: The convergence priority of OSPF routes is critical. * High: The convergence priority of OSPF routes is high. * Medium: The convergence priority of OSPF routes is medium. * Low: The convergence priority of OSPF routes is low. |
| Age | Time after the route was generated. |
| Backup NextHop | IP address of the next backup hop. |
| Backup Interface | Outbound interface of the next backup route. |
| Backup Type | Backup type:   * LFA LINK: OSPF LFA link protection. * LFA LINK-NODE: OSPF LFA link node protection. * REMOTE LFA LINK: OSPF remote LFA link protection. * REMOTE LFA LINK-NODE: OSPF remote LFA link node protection. * TI-LFA LINK-NODE: OSPF TI-LFA link node protection. |
| AdvRouter | Advertiser. |
| Area | Area ID. |
| Total Nets | Total number of networks in an area, between areas, in ASE areas, and in NSSAs. |
| Intra Area | Total number of internal networks in an area, that is, total number of stub networks and transit networks. |
| Inter Area | Total number of inter-area networks. |
| CalculateTime | Route calculation time. |
| DownloadTime | Time when a route is delivered. |
| Flags | Route information flag:   * A - Added to URT: route is added to the unicast routing table. * S - Secondary route: suboptimal route. |
| Route Type | Route type. |
| URT Cost | Cost value. |
| ASE | Total number of networks in the ASE area. |
| NSSA | Total number of networks in the NSSA. |