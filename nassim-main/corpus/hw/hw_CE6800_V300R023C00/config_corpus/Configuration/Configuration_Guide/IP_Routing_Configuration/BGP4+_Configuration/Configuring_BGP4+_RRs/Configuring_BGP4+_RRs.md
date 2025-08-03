Configuring BGP4+ RRs
=====================

Configuring BGP4+ RRs

#### Prerequisites

Before configuring BGP4+ RRs, you have completed the following task:

* [Configure basic BGP4+ functions](vrp_bgp6_cfg_0006.html).

#### Context

A full mesh of IBGP connections is needed to implement connectivity between IBGP peers within an AS. When there are many IBGP peers, it is costly to establish a fully-meshed network. An RR can be used to solve the problem.

Using RRs reduces the total number of IBGP connections to be established. On a large network, however, multiple RRs need to be configured to reduce the number of clients to be connected to each RR. Therefore, there are still a large number of IBGP connections on the network because a full mesh of connections needs to be established between the RRs. In this situation, configure hierarchical BGP4+ RRs to further reduce the number of IBGP connections to be established.

[Figure 1](#EN-US_TASK_0000001130782222__fig_dc_vrp_bgp6_cfg_004002) shows a typical hierarchical BGP4+ RR networking. DeviceA, DeviceB, DeviceC, and DeviceD function as level-2 RRs; DeviceE, DeviceF, DeviceG, and DeviceH function as level-1 RRs and level-2 RRs' clients. Level-2 RRs are not the clients of any RR and therefore must be fully meshed. Level-1 RRs function as the clients of level-2 RRs and do not need to be fully meshed.

**Figure 1** Network diagram of hierarchical BGP4+ RRs  
![](figure/en-us_image_0000001130782244.png)

The RR is simple to configure. You only need to configure the route reflection function on the BGP device that is to function as the RR. The clients do not need to know that they are clients of the RR.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. Enter the IPv6 unicast address family view.
   
   
   ```
   [ipv6-family](cmdqueryname=ipv6-family+unicast) unicast
   ```
4. Specify an RR and its clients.
   
   
   ```
   [peer](cmdqueryname=peer) { ipv6-address | group-name | ipv4-address } [reflect-client](cmdqueryname=reflect-client)
   ```
   
   The device with the [**peer reflect-client**](cmdqueryname=peer+reflect-client) command configuration functions as an RR, and the specified peer or peer group functions as a client.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The reflect-client configuration in an address family is valid only in this address family and cannot be inherited by other address families.
5. (Optional) Disable route reflection between clients through the RR.
   
   
   ```
   [undo reflect between-clients](cmdqueryname=undo+reflect+between-clients)
   ```
   
   By default, route reflection between clients through an RR is enabled.
   
   If the clients of an RR have established full-mesh connections with each other, you can run the [**undo reflect between-clients**](cmdqueryname=undo+reflect+between-clients) command to disable route reflection between clients through the RR to reduce the overhead. The [**undo reflect between-clients**](cmdqueryname=undo+reflect+between-clients) command is run only on RRs.
6. (Optional) Set the ID of a cluster where RRs belong.
   
   
   ```
   [reflector cluster-id](cmdqueryname=reflector+cluster-id) { cluster-id-value | cluster-id-ipv4 }
   ```
   
   If a cluster has multiple RRs, you can use this command to set the same cluster ID for these RRs to prevent routing loops.
   
   The [**reflector cluster-id**](cmdqueryname=reflector+cluster-id) command is run only on RRs.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   To prevent clients' failures to learn routes reflected by RRs, ensure that the cluster ID of the RRs is different from the router ID of any client. If the cluster ID of the RRs is the same as the router ID of a client, the client will discard received routes.
7. (Optional) Disable the RR from adding preferred BGP4+ routes to the IP routing table.
   
   
   ```
   [routing-table rib-only](cmdqueryname=routing-table+rib-only+route-policy) [ route-policy route-policy-name ]
   ```
   
   By default, preferred BGP4+ routes are added to the IP routing table. If the device is not required to forward packets, you can disable BGP4+ routes from being added to the IP routing table.
   
   If the **route-policy** *route-policy-name* parameter is specified in the [**routing-table rib-only**](cmdqueryname=routing-table+rib-only) command, the routes that match the route-policy are not delivered to the IP routing table, and the routes that do not match the route-policy are delivered to the IP routing table with their route attributes unchanged.
   
   Preventing a device from adding BGP4+ routes to the IP routing table is mainly used in RR scenarios. An RR transmits routes and forwards traffic within an AS. If the RR is connected to many clients and non-clients, route transmission will consume a lot of CPU resources of the RR and cause the RR to be unable to implement traffic forwarding. To improve route transmission efficiency, prevent the RR from adding BGP4+ routes to the IP routing table.
8. (Optional) Enable the RR to modify attributes of BGP4+ routes to be advertised based on the export route-policy.
   
   
   ```
   [reflect change-path-attribute](cmdqueryname=reflect+change-path-attribute)
   ```
   
   By default, the RR cannot modify route attributes using an export route-policy.
   
   The route attributes on the RR cannot be modified using the export route-policy because routing loops may occur. By default, the RR is disabled from modifying the route attributes based on the export route-policy. If you need to re-plan the network traffic, you can enable the RR to modify the route attributes based on the export route-policy.
   
   After the [**reflect change-path-attribute**](cmdqueryname=reflect+change-path-attribute) command is run on an RR, route attributes can be modified by performing the following operations:
   * Run the [**apply as-path**](cmdqueryname=apply+as-path) command to modify the AS\_Path attribute of BGP4+ routes.
   * Run the [**apply comm-filter delete**](cmdqueryname=apply+comm-filter+delete) command to delete all community attributes from BGP4+ routes.
   * Run the [**apply community**](cmdqueryname=apply+community) command to modify the community attribute of BGP4+ routes.
   * Run the [**apply large-community**](cmdqueryname=apply+large-community) command to modify the Large-Community attribute of BGP4+ routes.
   * Run the [**apply cost**](cmdqueryname=apply+cost) command to modify the MED (cost) values of BGP4+ routes.
   * Run the [**apply ipv6 next-hop**](cmdqueryname=apply+ipv6+next-hop) command to modify the next-hop IP addresses of BGP4+ routes.
   * Run the [**apply local-preference**](cmdqueryname=apply+local-preference) command to modify the local preferences of BGP4+ routes.
   * Run the [**apply origin**](cmdqueryname=apply+origin) command to modify the Origin attribute of BGP4+ routes.
   * Run the [**apply extcommunity**](cmdqueryname=apply+extcommunity) command to modify the VPN target extended community attribute of BGP4+ routes.
   * Run the [**apply extcommunity bandwidth**](cmdqueryname=apply+extcommunity+bandwidth) { *extCmntyString* | **none** } or [**apply extcommunity bandwidth**](cmdqueryname=apply+extcommunity+bandwidth) **aggregate** [ **limit** *bandwidth-value* ] command to modify the Link Bandwidth extended community attribute of BGP4+ routes.![](public_sys-resources/note_3.0-en-us.png) 
   
   After the [**reflect change-path-attribute**](cmdqueryname=reflect+change-path-attribute) command is run on the RR, the [**peer route-policy**](cmdqueryname=peer+route-policy) **export** command takes precedence over the [**peer next-hop-invariable**](cmdqueryname=peer+next-hop-invariable) command and[**peer next-hop-local**](cmdqueryname=peer+next-hop-local) command.
9. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

After completing the configuration, perform the following operations to verify it:

* Run the [**display bgp**](cmdqueryname=display+bgp) **ipv6** [**peer**](cmdqueryname=peer) [ **verbose** ] command to check information about BGP4+ peers and check whether the peer relationships with the RR are successfully established.
* Run the [**display bgp ipv6 routing-table**](cmdqueryname=display+bgp+ipv6+routing-table) command to check information about BGP4+ routes reflected by the RR.