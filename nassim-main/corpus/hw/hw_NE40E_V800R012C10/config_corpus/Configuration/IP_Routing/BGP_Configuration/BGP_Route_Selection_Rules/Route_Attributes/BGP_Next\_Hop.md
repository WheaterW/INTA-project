BGP Next\_Hop
=============

BGP ignores routes with an unreachable next hop address during BGP route selection.

Unlike the Next\_Hop attribute in an IGP, the Next\_Hop attribute in BGP is not necessarily the IP address of a neighboring device. In most cases, the Next\_Hop attribute in BGP complies with the following rules:

* When advertising a route to an EBGP peer, the BGP speaker sets the Next\_Hop of the route to the address of the local interface through which the BGP peer relationship is established.
* When advertising a locally generated route to an IBGP peer, the BGP speaker sets the Next\_Hop of the route to the address of the local interface through which the BGP peer relationship is established.
* When advertising a route learned from an EBGP peer to an IBGP peer, the BGP speaker does not change the Next\_Hop of the route.
* When advertising a route learned from an IBGP peer to another IBGP peer, the BGP speaker does not change the Next\_Hop of the route.

#### Modifying the Next\_Hop

In some scenarios, the Next\_Hop needs to be modified. [Table 1](#EN-US_CONCEPT_0172366307__table_dc_vrp_bgp_path_selection_000401) describes whether the Next\_Hop needs to be modified in specific scenarios.

**Table 1** Next\_Hop processing
| Objectives | Command | Usage Scenarios | Remarks |
| --- | --- | --- | --- |
| To enable the device to modify the Next\_Hop of the routes to be advertised to an IBGP peer | [**peer**](cmdqueryname=peer+next-hop-local) { *ipv4-address* | *group-name* } **next-hop-local** | By default, a device does not change the next hop address of a route learned from an EBGP peer before forwarding the route to IBGP peers. The next hop address of a route advertised by an EBGP peer to this device is the peer address of the EBGP peer. After being forwarded to IBGP peers in the local AS, this route is not active because the next hop is unreachable. To address this problem, the relevant ASBR needs to be configured to change the Next\_Hop of the route learned from an EBGP peer to the ASBR's own address before the ASBR advertises the route to an IBGP peer. As an IGP runs within the AS, the next hop of the route is reachable to the IBGP peer. As such, the route received by the IBGP peer is active. | NOTE:  If BGP load balancing is configured using the [**maximum load-balancing**](cmdqueryname=maximum+load-balancing) *number* command, the Router changes the next hop address of a route to the IP address used to establish an IBGP peer relationship when advertising the route to the IBGP peer or peer group, regardless of whether the [**peer next-hop-local**](cmdqueryname=peer+next-hop-local) command is run. |
| To configure a device to retain the original Next\_Hop of imported IGP routes when the device advertises the routes to an IBGP peer | [**peer**](cmdqueryname=peer+next-hop-invariable) { *ipv4-address* | *group-name* } **next-hop-invariable** | In an intra-AS scenario, if a device is configured to retain the original Next\_Hop of IGP routes when advertising them to a peer, the peer can directly use the original Next\_Hop for recursion, which reduces the number of hops. | - |
| To configure a BGP device to retain the original Next\_Hop of imported static routes when advertising the routes to an IBGP peer | [**peer**](cmdqueryname=peer+next-hop-invariable+include-static-route) { *ipv4-address* | *group-name* } **next-hop-invariable** **include-static-route** | In an intra-AS scenario, if a device is configured to retain the original Next\_Hop of imported static routes when advertising the routes to an IBGP peer, the peer can use the original Next\_Hop for recursion, which reduces the number of hops. | - |
| To configure a BGP device to retain the original Next\_Hop when the device advertises to an EBGP peer the unicast routes learned from another peer | [**peer**](cmdqueryname=peer+next-hop-invariable+include-unicast-route) { *ipv4-address* | *group-name* } **next-hop-invariable** **include-unicast-route** | In an intra-AS scenario, if a device is configured to retain the original Next\_Hop of unicast routes when advertising them to a peer, the peer can directly use the original Next\_Hop for recursion, which reduces the number of hops. | - |
| To prevent a device from modifying the Next\_Hops of routes before advertising the routes to an EBGP peer | [**peer**](cmdqueryname=peer+next-hop-invariable) { *ipv4-address* | *group-name* } **next-hop-invariable** | In an inter-AS VPN Option C scenario where RRs are used, the [**peer next-hop-invariable**](cmdqueryname=peer+next-hop-invariable) command needs to be run on the RRs to prevent them from modifying the Next\_Hops of routes before advertising the routes to an EBGP peer. This ensures that the remote PE can implement recursion to the BGP LSP to the local PE during traffic transmission. | -  By default, a BGP device changes the Next\_Hop of routes to its local interface IP address before advertising the routes to EBGP peers.  In addition, a BGP device does not modify the Next\_Hop of unlabeled routes if the routes are learned from EBGP peers and are to be advertised to IBGP peers; however, the device changes the Next\_Hop to its own interface IP address if these routes are labeled routes. |
| To configure route-policy-based next hop recursion | [**nexthop recursive-lookup**](cmdqueryname=nexthop+recursive-lookup+route-policy) **route-policy** *route-policy-name* | Route-policy-based next hop recursion helps flexibly control the recursion result based on specific conditions. If a route does not match the specified route-policy, the route fails to recurse. | - |
| To enable a device to modify the Next\_Hops of BGP routes using a route-policy | [**apply ip-address next-hop**](cmdqueryname=apply+ip-address+next-hop+peer-address) { *ipv4-address* | **peer-address** } | The Next\_Hops of BGP routes can be modified using a route-policy in the following situations:   * For an IBGP peer, the route-policy can be an import or export policy. Even if the next hop address configured in the route-policy is unreachable, the IBGP peer still adds the routes whose next hop addresses have been changed to the address configured in the route-policy to the BGP routing table. However, the routes are invalid. * For an EBGP peer, to modify the next hop address of routes, an import policy is configured in most cases. If the route-policy is configured as an export policy, the routes whose next hop addresses have been changed to the address configured in the route-policy are discarded by the EBGP peer because the next hop address is unreachable. | If a route-policy has been specified in the [**import-route**](cmdqueryname=import-route) or [**network**](cmdqueryname=network) command, the apply clause configured for the route-policy using the [**apply ip-address next-hop**](cmdqueryname=apply+ip-address+next-hop) command does not take effect. |




#### Obtaining a Reachable BGP Next Hop

During route selection, BGP first checks whether the next hop addresses of routes are reachable. Routes carrying unreachable next hop addresses are inactive and are not selected. As described in [Table 2](#EN-US_CONCEPT_0172366307__table_dc_vrp_bgp_path_selection_000402), the next hop is unreachable in the following situations:

**Table 2** Unreachable next hop
| Item | Description | Solutions |
| --- | --- | --- |
| Unreachable next hop IP address | A next hop IP address is obtained through route recursion, but no active routes to the IP address are available in the IP routing table. | Common solutions are as follows:  * Configure static routes or an IGP. * Run the [**import-route**](cmdqueryname=import-route) command. * Run the [**network**](cmdqueryname=network) command.  * Run the [**peer next-hop-local**](cmdqueryname=peer+next-hop-local) command to change the next hop of the route to the local address so that the next hop is reachable. |
| Unreachable next hop tunnel | Routes fail to recurse to tunnels. | Configure a tunnel policy or a tunnel selector to ensure that the routes can recurse to tunnels. |
| A next hop tunnel is obtained through route recursion, but the tunnel is unavailable. | Ensure that the tunnel is correctly configured and is Up. |



[Figure 1](#EN-US_CONCEPT_0172366307__fig_dc_vrp_bgp_path_selection_000401) is used to show how to obtain a reachable next hop IP address. In [Figure 1](#EN-US_CONCEPT_0172366307__fig_dc_vrp_bgp_path_selection_000401), an IBGP peer relationship is established between DeviceA and DeviceB, and an EBGP peer relationship is established between DeviceB and DeviceC. DeviceA imports the route 1.1.1.9/32, and DeviceC imports the route 3.3.3.9/32.**Figure 1** BGP route unreachability  
![](images/fig_dc_vrp_bgp_path_selection_000401.png)

# Display the BGP routing table of DeviceA.

```
[~DeviceA] display bgp routing-table
```
```
 BGP Local router ID is 10.1.1.1
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
               Origin : i - IGP, e - EGP, ? - incomplete
 RPKI validation codes: V - valid, I - invalid, N - not-found

 Total Number of Routes: 2
      Network            NextHop        MED        LocPrf    PrefVal Path/Ogn

 *>   1.1.1.9/32         0.0.0.0         0                     0      i
   i  3.3.3.9/32         10.1.2.1        0          100        0      65001i
```

The preceding command output shows that no asterisk (\*) is in front of the route 3.3.3.9/32, which indicates that the route is invalid.

# Display the IP routing table of DeviceA.

```
[~DeviceA] display ip routing-table
```
```
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table : _public_
         Destinations : 5        Routes : 5

Destination/Mask    Proto   Pre  Cost      Flags NextHop         Interface

        1.1.1.9/32  Direct  0    0           D   127.0.0.1       LoopBack1
       10.1.1.0/30  Direct  0    0           D   10.1.1.1        GigabitEthernet0/1/0
       10.1.1.1/32  Direct  0    0           D   127.0.0.1       GigabitEthernet0/1/0
      127.0.0.0/8   Direct  0    0           D   127.0.0.1       InLoopBack0
      127.0.0.1/32  Direct  0    0           D   127.0.0.1       InLoopBack0
```
The preceding command output shows that the next hop 10.1.2.1 of the route 3.3.3.9/32 is not in the IP routing table. This indicates that the route 3.3.3.9/32 becomes invalid because its next hop is unreachable. The following methods can be used for the route 3.3.3.9/32 to become valid:

* Configure a static route destined for 10.1.2.1/30 on DeviceA.
* Configure an IGP on DeviceB and DeviceC and configure BGP on DeviceB to import the route 10.1.2.1. However, this method is not applicable to this scenario because DeviceB and DeviceC are located in different ASs.
* Run the **import-route direct** command on DeviceB. This solution is not optimal because unnecessary routes may be imported.
* Run the **network 10.1.2.0 30** command on DeviceB to configure BGP to advertise the route 10.1.2.0/30 to DeviceA.
* Run the **peer 10.1.1.1 next-hop-local** command on DeviceB to configure DeviceB to modify the Next\_Hop of the route 3.3.3.9/32 before advertising the route to DeviceA.

In this example, the **network 10.1.2.0 30** command is run on DeviceB. After the command is run, check the BGP routing table of DeviceA.

```
[~DeviceA] display bgp routing-table
```
```
 BGP Local router ID is 10.1.1.1
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
               Origin : i - IGP, e - EGP, ? - incomplete
 RPKI validation codes: V - valid, I - invalid, N - not-found

 Total Number of Routes: 3
      Network            NextHop        MED        LocPrf    PrefVal Path/Ogn

 *>   1.1.1.9/32         0.0.0.0         0                     0      i
 *>i  3.3.3.9/32         10.1.2.1        0          100        0      65001i
 *>i  10.1.2.0/30        10.1.1.2        0          100        0      i
```

The preceding command output shows that both **\*** and **>** are in front of the route 3.3.3.9/32, which indicates that the route is valid and optimal.