AS\_Path
========

BGP prefers the route with the shortest AS\_Path length (the number of included ASs) during BGP route selection.

Four types of AS\_Path attributes are available: AS\_Sequence, AS\_Set, AS\_Confed\_Sequence, and AS\_Confed\_Set.

* AS\_Sequence: records in reverse order all the ASs through which a route passes from the local device to the destination.
* AS\_Set: records in random order all the ASs through which a route passes from the local device to the destination. The AS\_Set attribute is used in route summarization scenarios.
* AS\_Confed\_Sequence: records in reverse order all the sub-ASs within a BGP confederation through which a route passes from the local device to the destination.
* AS\_Confed\_Set: records in random order all the sub-ASs within a BGP confederation through which a route passes from the local device to the destination.

[Table 1](#EN-US_CONCEPT_0172366326__table_dc_vrp_path_selection_000901) describes the AS\_Path-based route selection rules.

**Table 1** AS\_Path-based route selection rules
| Item | Description |
| --- | --- |
| AS\_Set | Regardless of how many AS numbers are contained in an AS\_Set, BGP considers its length to be 1 during route selection. When the [**aggregate (BGP)**](cmdqueryname=aggregate+%28BGP%29+as-set) command is run to manually generate a summary route, if **as-set** is specified in the command, an AS\_Set will be carried in the summary route. Otherwise, no AS\_Set will be carried. When an AS\_Set is generated:  * If the routes to be summarized have the same AS\_Sequence, the AS\_Sequence of the summary route also contains this AS\_Sequence, and the AS\_Set of the summary route is null. * If the routes to be summarized have different AS\_Sequences, all the AS numbers in the AS\_Sequences are included in the AS\_Set after summarization. |
| AS\_Confed\_Sequence and AS\_Confed\_Set | BGP ignores AS\_Confed\_Sequence and AS\_Confed\_Set when calculating the AS\_Path length. |
| [**bestroute as-path-ignore**](cmdqueryname=bestroute+as-path-ignore) | After the command is run, BGP does not compare the AS\_Path attributes during route selection. |
| [**apply as-path**](cmdqueryname=apply+as-path) | You can run this command in a route-policy to clear, replace, or add AS numbers.  NOTE:  The configuration of the [**apply as-path**](cmdqueryname=apply+as-path) command may change the traffic forwarding path, or cause routing loops or route selection errors. Therefore, exercise caution when configuring the command. |
| [**peer public-as-only**](cmdqueryname=peer+public-as-only) | After the command is run, BGP removes all the private AS numbers (if any) from the AS\_Path attribute in each Update message to be sent. The private AS number ranges from 64512 to 65534 and from 4200000000 to 4294967294 (or from 64086.59904 to 65535.65534). |
| [**peer public-as-only import**](cmdqueryname=peer+public-as-only+import) | After the command is run, BGP removes all the private AS numbers (if any) from the AS\_Path attribute in each received Update message. The private AS number ranges from 64512 to 65534 and from 4200000000 to 4294967294 (or from 64086.59904 to 65535.65534). |
| [**peer fake-as**](cmdqueryname=peer+fake-as) | After the command is run, BGP can use a fake AS number to set up a BGP peer relationship.  If the local device uses the actual AS number to establish an EBGP peer relationship with a remote device, the actual AS number is carried in the AS\_Path of the route sent to the remote device. If the local device uses the fake AS number to establish the EBGP peer relationship, the fake AS number is carried in the AS\_Path of the route to be sent to the remote device. |
| [**peer substitute-as**](cmdqueryname=peer+substitute-as) | After the command is run, if the AS\_Path attribute in the route that a PE will send to a peer (CE) contains an AS number the same as that of the CE, the PE replaces the AS number in the AS\_Path attribute with its local AS number before advertising this route. NOTE:  The [**peer substitute-as**](cmdqueryname=peer+substitute-as) command applies only to PEs in BGP MPLS IP/VPN scenarios and may cause routing loops if it is improperly configured. Therefore, exercise caution when using the command. |


During BGP route selection, BGP compares the AS\_Path length by calculating the number of ASs included in the AS\_Sequence if AS\_Sequence is carried in a route. If both AS\_Sequence and AS\_Set are carried in the route, BGP considers the AS\_Path length to be the number of ASs included in the AS\_Sequence plus 1. The following describes some common commands in detail by using examples.

#### Deleting Private AS Numbers

As public AS resources are limited, carriers generally use private AS numbers when deploying VPNs. Private AS numbers, however, must not be advertised to the Internet because they may cause routing loops. In [Figure 1](#EN-US_CONCEPT_0172366326__fig_dc_vrp_bgp_path_selection_000901), both ISP1 and ISP2 use 65001 as a private AS number.**Figure 1** Networking in which a private AS needs to be deleted  
![](images/fig_dc_vrp_bgp_path_selection_000901.png)

In [Figure 1](#EN-US_CONCEPT_0172366326__fig_dc_vrp_bgp_path_selection_000901), Device A advertises the route 10.0.0.0/8 to Device D through ISP1 and ISP2. After receiving this route, Device D checks the AS\_Path attribute. This AS\_Path attribute carries AS 65001, which is the same as the AS number of Device D. As a result, Device D discards this route.

To address this problem, run the [**peer public-as-only**](cmdqueryname=peer+public-as-only) command on Device B so that Device B in ISP1 deletes AS 65001 (private AS number) before adding AS 100 (its own AS number) to the AS\_Path attribute and advertising the route to Device C in ISP2.

Before using the [**peer public-as-only**](cmdqueryname=peer+public-as-only) command, note the following restrictions: BGP does not remove private AS numbers in the following scenarios:

* The AS\_Path of a route carries the AS number of the remote peer. In this case, deleting private AS numbers may lead to a routing loop.
* The AS\_Path carries both public and private AS numbers, which indicates that the route has passed through the public network. In this case, deleting private AS numbers may lead to incorrect traffic forwarding.

The preceding limitations also apply to confederation scenarios.

#### Adding AS Numbers

In [Figure 2](#EN-US_CONCEPT_0172366326__fig_dc_vrp_bgp_path_selection_000902), AS 65005 imports three routes and advertises them to AS 65001 through two paths.**Figure 2** Networking in which new AS numbers are added to the AS\_Path  
![](images/fig_dc_vrp_bgp_path_selection_000902.png)

Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table) [ *ip-address* ] command to verify the configuration.

# Display the routing table of DeviceA.

```
[~DeviceA] display bgp routing-table
```
```
 BGP Local router ID is 10.1.1.1
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
               Origin : i - IGP, e - EGP, ? - incomplete
 RPKI validation codes: V - valid, I - invalid, N - not-found

 Total Number of Routes: 6
      Network            NextHop        MED        LocPrf    PrefVal Path/Ogn

 *>   172.16.1.0/24      10.1.3.2                              0      65003 65005?
 *                       10.1.1.2                              0      65002 65004 65005?
 *>   172.16.2.0/24      10.1.3.2                              0      65003 65005?
 *                       10.1.1.2                              0      65002 65004 65005?
 *>   172.16.3.0/24      10.1.3.2                              0      65003 65005?
 *                       10.1.1.2                              0      65002 65004 65005?
```
```
[~DeviceA] display bgp routing-table 172.16.1.0
```
```
 BGP local router ID : 10.1.1.1
 Local AS number : 65001
 Paths:   2 available, 1 best, 1 select
 BGP routing table entry information of 172.16.1.0/24:
 From: 10.1.3.2 (10.1.5.1)
 Route Duration: 00h00m56s
 Direct Out-interface: GigabitEthernet0/1/0
 Original nexthop: 10.1.3.2
 Qos information : 0x0
 AS-path 65003 65005, origin incomplete, pref-val 0, valid, external, best, select, active, pre 255
 Advertised to such 2 peers:
    10.1.3.2
    10.1.1.2
 BGP routing table entry information of 172.16.1.0/24:
 From: 10.1.1.2 (10.1.1.2)
 Route Duration: 00h34m43s
 Direct Out-interface: GigabitEthernet0/2/0
 Original nexthop: 10.1.1.2
 Qos information : 0x0
 AS-path 65002 65004 65005, origin incomplete, pref-val 0, valid, external, pre 255, not preferred for AS-Path
 Not advertised to any peer yet
```

The preceding command output shows that DeviceA selects the route learned from DeviceC because this route has a shorter AS\_Path length than that learned from DeviceB. To enable DeviceA to select the route learned from DeviceB, configure DeviceB to reduce the AS\_Path length of the route or configure DeviceC to increase the AS\_Path length of the route. In the following example, DeviceC is configured to increase the AS\_Path length of the route. The detailed configurations on DeviceC are as follows:

```
#
bgp 65003
 #
 ipv4-family unicast
  undo synchronization
   peer 10.1.3.1 route-policy add_asn export            //Apply export policy named add_asn to the routes to be advertised to BGP peer 10.1.3.1.
  #
route-policy add_asn permit node 10                     //Define the first node of add_asn.
 if-match ip-prefix prefix1                             //Configure IP prefix list named prefix1.
 apply as-path 65003 65003 65003 additive               //Add 65003, 65003, 65003 to the AS_Path of the route that matches the IP prefix list prefix1.
#
route-policy add_asn permit node 20                     //Define the second node of add_asn to permit all other routes.
#
ip ip-prefix prefix1 index 10 permit 172.16.1.0 24      //Define the first index of prefix1 to match the route 172.16.1.0/24.
ip ip-prefix prefix1 index 20 permit 172.16.2.0 24      //Define the second index of prefix1 to match the route 172.16.2.0/24.
ip ip-prefix prefix1 index 30 permit 172.16.3.0 24      //Define the third index of prefix1 to match the route 172.16.3.0/24.
#
```

Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table) [ *ip-address* ] command to verify the configuration.

# Display the routing table of DeviceA.

```
[~DeviceA] display bgp routing-table
```
```
 BGP Local router ID is 10.1.1.1
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
               Origin : i - IGP, e - EGP, ? - incomplete
 RPKI validation codes: V - valid, I - invalid, N - not-found

 Total Number of Routes: 6
      Network            NextHop        MED        LocPrf    PrefVal Path/Ogn

 *>   172.16.1.0/24      10.1.1.2                              0      65002 65004 65005?
 *                       10.1.3.2                              0      65003 65003 65003 65003 65005?
 *>   172.16.2.0/24      10.1.1.2                              0      65002 65004 65005?
 *                       10.1.3.2                              0      65003 65003 65003 65003 65005?
 *>   172.16.3.0/24      10.1.1.2                              0      65002 65004 65005?
 *                       10.1.3.2                              0      65003 65003 65003 65003 65005?
```
```
[~DeviceA] display bgp routing-table 172.16.1.0
```
```
 BGP local router ID : 10.1.1.1
 Local AS number : 65001
 Paths:   2 available, 1 best, 1 select
 BGP routing table entry information of 172.16.1.0/24:
 From: 10.1.1.2 (10.1.1.2)
 Route Duration: 00h33m30s
 Direct Out-interface: GigabitEthernet0/1/0
 Original nexthop: 10.1.1.2
 Qos information : 0x0
 AS-path 65002 65004 65005, origin incomplete, pref-val 0, valid, external, best, select, active, pre 255
 Advertised to such 2 peers:
    10.1.3.2
    10.1.1.2
 BGP routing table entry information of 172.16.1.0/24:
 From: 10.1.3.2 (10.1.5.1)
 Route Duration: 00h02m12s
 Direct Out-interface: GigabitEthernet0/2/0
 Original nexthop: 10.1.3.2
 Qos information : 0x0
 AS-path 65003 65003 65003 65003 65005, origin incomplete, pref-val 0, valid, external, pre 255, not preferred for AS-Path
 Not advertised to any peer yet
```
The preceding command output shows that the AS\_Path length of the route learned from DeviceB is shorter than that of the route learned from DeviceC and that the route learned from DeviceB is selected as the optimal route. [Table 2](#EN-US_CONCEPT_0172366326__tab_dc_vrp_bgp_path_selection_000902) shows the attribute comparison of the routes that DeviceA learns from DeviceB and DeviceC.

**Table 2** Attribute comparison of the routes that DeviceA learns from DeviceB and DeviceC
| Route Attribute | Route Learned from DeviceB | Route Learned from DeviceC | Comparison |
| --- | --- | --- | --- |
| PrefVal | 0 | 0 | The same. |
| Local\_Pref | - | - | The same. |
| Route type | Learned from a peer | Learned from a peer | The same. |
| AIGP | - | - | The same. |
| AS\_Path | 65002 65004 65005 | 65003 65003 65003 65003 65005 | The route learned from DeviceB is optimal. |


AS numbers can be added to the AS\_Path as required. However, if an AS number is added to the AS\_Path of a route, the route cannot be received by devices in this AS. Therefore, the local AS number is added in most cases. For example in [Figure 2](#EN-US_CONCEPT_0172366326__fig_dc_vrp_bgp_path_selection_000902), if DeviceC adds AS 65001 to the AS\_Path of a route before advertising the route to DeviceA, DeviceA will discard the route upon receipt because the route carries DeviceA's AS number.


#### Replacing AS Numbers

If **overwrite** is specified in the [**apply as-path**](cmdqueryname=apply+as-path+overwrite) command, the AS numbers in the AS\_Path attribute can be replaced. AS number replacement can be flexibly applied to serve the following purposes:

* Shield the actual path information.
* Prevent a route from being discarded by replacing the AS\_Path attribute of the route with a shorter one if the [**as-path-limit**](cmdqueryname=as-path-limit) command is run on the device that receives this route.
* Shorten the AS\_Path length so that the route is preferentially selected.

AS number replacement can also be used for the purpose of load balancing. Generally, BGP requires that the AS\_Path attributes of the routes be the same so that load balancing can be implemented. To meet load balancing requirements, AS numbers can be replaced. For example in [Figure 2](#EN-US_CONCEPT_0172366326__fig_dc_vrp_bgp_path_selection_000902), the **apply as-path 65002 65004 65005 overwrite** command can be run on DeviceA to replace the AS\_Path of the route learned from DeviceC so that the route has the same AS\_Path as that of the route learned from DeviceB, and the two routes are used to load-balance traffic. Detailed configurations on DeviceA are as follows:

```
#
bgp 65001
 #
 ipv4-family unicast
  undo synchronization
   peer 10.1.3.2 route-policy replace_asn import        //Apply export policy named replace_asn to routes to be advertised to BGP peer 10.1.3.2.
  #
route-policy replace_asn permit node 10                 //Define the first node of replace_asn.
 if-match as-path-filter filter1                        //Configure AS_Path filter named filter1.
 apply as-path 65002 65004 65005 overwrite              //Replace the AS_Path of the route that matches filter1 with 65002, 65004, 65005.
#
route-policy replace_asn permit node 20                 //Define the second node of replace_asn to permit all other routes.
#
ip as-path-filter filter1 permit ^65003                 //Define AS_Path filter named filter1 to match all the routes learned from AS 65003.
#
```

Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table) [ *ip-address* ] command to verify the configuration.

# Display the routing table of DeviceA.

```
[~DeviceA] display bgp routing-table
```
```
 BGP Local router ID is 10.1.1.1
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
               Origin : i - IGP, e - EGP, ? - incomplete
 RPKI validation codes: V - valid, I - invalid, N - not-found

 Total Number of Routes: 6
      Network            NextHop        MED        LocPrf    PrefVal Path/Ogn

 *>   172.16.1.0/24      10.1.1.2                              0      65002 65004 65005?
 *                       10.1.3.2                              0      65002 65004 65005?
 *>   172.16.2.0/24      10.1.1.2                              0      65002 65004 65005?
 *                       10.1.3.2                              0      65002 65004 65005?
 *>   172.16.3.0/24      10.1.1.2                              0      65002 65004 65005?
 *                       10.1.3.2                              0      65002 65004 65005?
```

The preceding command output shows that the AS\_Path of the route received from AS 65003 has been replaced. In this case, the routes sent from AS 65002 and AS 65003 have the same AS\_Path, which meets the load balancing conditions. Run the **maximum load-balancing 2** command on DeviceA to set the maximum number of routes for load balancing to 2. Then, check the detailed BGP route information. The route 172.16.1.0/24 is used in the following example:

```
[~DeviceA] display bgp routing-table 172.16.1.0
```
```
 BGP local router ID : 10.1.1.1
 Local AS number : 65001
 Paths:   2 available, 1 best, 2 select
 BGP routing table entry information of 172.16.1.0/24:
 From: 10.1.1.2 (10.1.1.2)
 Route Duration: 19h57m51s
 Direct Out-interface: GigabitEthernet0/1/0
 Original nexthop: 10.1.1.2
 Qos information : 0x0
 AS-path 65002 65004 65005, origin incomplete, pref-val 0, valid, external, best, select, active, pre 255
 Advertised to such 2 peers:
    10.1.1.2
    10.1.3.2
 BGP routing table entry information of 172.16.1.0/24:
 From: 10.1.3.2 (10.1.5.1)
 Route Duration: 00h10m21s
 Direct Out-interface: GigabitEthernet0/2/0
 Original nexthop: 10.1.3.2
 Qos information : 0x0
 AS-path 65002 65004 65005, origin incomplete, pref-val 0, valid, external, select, active, pre 255, not preferred for router ID
 Not advertised to any peer yet
```

The preceding command output shows that the route learned from DeviceB is optimal and is used by BGP along with the route learned from DeviceC (not optimal) for load balancing. Check the information about the route 172.16.1.0/24 in the IP routing table.

```
[~DeviceA] display ip routing-table
```
```
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table : _Public_
         Destinations : 9        Routes : 12

Destination/Mask    Proto   Pre  Cost      Flags NextHop         Interface

       10.1.1.0/30  Direct  0    0           D   10.1.1.1        GigabitEtherne0/2/0
       10.1.1.1/32  Direct  0    0           D   127.0.0.1       GigabitEthernet0/2/0
       10.1.3.0/30  Direct  0    0           D   10.1.3.1        GigabitEthernet0/1/0
       10.1.3.1/32  Direct  0    0           D   127.0.0.1       GigabitEthernet0/1/0
      127.0.0.0/8   Direct  0    0           D   127.0.0.1       InLoopBack0
      127.0.0.1/32  Direct  0    0           D   127.0.0.1       InLoopBack0
     172.16.1.0/24  EBGP    255  0           D   10.1.1.2        GigabitEthernet0/2/0
                    EBGP    255  0           D   10.1.3.2        GigabitEthernet0/1/0
     172.16.2.0/24  EBGP    255  0           D   10.1.1.2        GigabitEthernet0/2/0
                    EBGP    255  0           D   10.1.3.2        GigabitEthernet0/1/0
     172.16.3.0/24  EBGP    255  0           D   10.1.1.2        GigabitEthernet0/2/0
                    EBGP    255  0           D   10.1.3.2        GigabitEthernet0/1/0
```

The preceding command output shows that BGP has delivered the two routes with the same route prefix to the IP routing table for load balancing.


#### Clearing the AS\_Path

If **none** **overwrite** is specified in the [**apply as-path**](cmdqueryname=apply+as-path+none+overwrite) command, the device clears the AS\_Path attribute to shield the actual path information and shorten the AS\_Path length. If the AS\_Path attribute is empty, BGP considers its length as 0 during route selection.