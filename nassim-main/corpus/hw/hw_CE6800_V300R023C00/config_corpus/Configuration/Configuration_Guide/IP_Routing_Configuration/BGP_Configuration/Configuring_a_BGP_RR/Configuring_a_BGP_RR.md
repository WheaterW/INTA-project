Configuring a BGP RR
====================

Configuring a BGP RR

#### Prerequisites

Before configuring a BGP RR, you have completed the following task:

* [Configure basic BGP functions.](vrp_bgp_cfg_0014.html)

#### Context

In an AS, one BGP device functions as an RR, and the other BGP devices function as clients. The clients establish IBGP connections to the RR. The RR and its clients form a cluster. The RR reflects routes among the clients, and therefore the clients do not need to establish any IBGP connection.

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
3. Enter the BGP-IPv4 unicast address family view.
   
   
   ```
   [ipv4-family](cmdqueryname=ipv4-family+unicast) unicast
   ```
4. Specify an RR and its clients.
   
   
   ```
   [peer](cmdqueryname=peer) { ipv4-address | group-name | ipv6-address } [reflect-client](cmdqueryname=reflect-client)
   ```
   
   The device with the [**peer reflect-client**](cmdqueryname=peer+reflect-client) command configuration functions as an RR, and the specified peer or peer group functions as a client.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The configuration of an RR and its clients in an address family is valid only in this address family and cannot be used in other address families. Therefore, configure RRs and clients in a required address family.
5. Disable route reflection between clients through the RR.
   
   
   ```
   [undo reflect between-clients](cmdqueryname=undo+reflect+between-clients)
   ```
   
   By default, route reflection between clients through an RR is enabled.
   
   If the clients of an RR have established full-mesh connections with each other, you can run the [**undo reflect between-clients**](cmdqueryname=undo+reflect+between-clients) command to disable route reflection between clients through the RR to reduce the overhead. The [**undo reflect between-clients**](cmdqueryname=undo+reflect+between-clients) command is run only on RRs.
6. (Optional) Set a cluster ID of the RR.
   
   
   ```
   [reflector cluster-id](cmdqueryname=reflector+cluster-id) { cluster-id-value | cluster-id-ipv4 }
   ```
   
   If a cluster has multiple RRs, you can use this command to set the same cluster ID for these RRs to prevent routing loops.
   
   The [**reflector cluster-id**](cmdqueryname=reflector+cluster-id) command is run only on RRs.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   To prevent clients' failures to learn routes reflected by RRs, ensure that the cluster ID of the RRs is different from the router ID of any client. If the cluster ID of the RRs is the same as the router ID of a client, the client will discard received routes.
7. (Optional) Disable the device from adding preferred BGP routes to the IP routing table.
   
   
   ```
   [routing-table rib-only](cmdqueryname=routing-table+rib-only+route-policy) [ route-policy route-policy-name ]
   ```
   
   By default, preferred BGP routes are added to the IP routing table. If the device is not required to forward packets, you can disable BGP routes from being added to the IP routing table.
   
   If the **route-policy** *route-policy-name* parameter is specified in the [**routing-table rib-only**](cmdqueryname=routing-table+rib-only) command, the routes that match the route-policy are not delivered to the IP routing table, and the routes that do not match the route-policy are delivered to the IP routing table with their route attributes unchanged.
   
   Preventing a device from adding BGP routes to the IP routing table is mainly used in RR scenarios. An RR transmits routes and forwards traffic within an AS. If an RR is connected to many clients and non-clients, route transmission will consume a lot of CPU resources of the RR and cause the RR to be unable to implement traffic forwarding. To improve route transmission efficiency, prevent the RR from adding BGP routes to the IP routing table.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The [**routing-table rib-only**](cmdqueryname=routing-table+rib-only) and [**active-route-advertise**](cmdqueryname=active-route-advertise) commands are mutually exclusive.
8. (Optional) Enable the RR to modify path attributes of routes to be advertised based on the export policy.
   
   
   ```
   [reflect change-path-attribute](cmdqueryname=reflect+change-path-attribute)
   ```
   
   By default, an RR is disabled from modifying path attributes based on an export policy.
   
   The route attributes on the RR cannot be modified using the export route-policy because routing loops may occur. By default, the RR is disabled from modifying the route attributes based on the export route-policy. If you need to re-plan the network traffic, you can enable the RR to modify the path attributes based on the export policy.
   
   After the [**reflect change-path-attribute**](cmdqueryname=reflect+change-path-attribute) command is run on an RR, path attributes can be modified by performing the following operations:
   * Run the [**apply as-path**](cmdqueryname=apply+as-path) command to modify the AS\_Path attribute of BGP routes.
   * Run the [**apply comm-filter delete**](cmdqueryname=apply+comm-filter+delete) command to delete community attributes from BGP routes.
   * Run the [**apply community**](cmdqueryname=apply+community) command to modify the community attribute of BGP routes.
   * Run the [**apply large-community**](cmdqueryname=apply+large-community) command to modify the Large-Community attribute of BGP routes.
   * Run the [**apply cost**](cmdqueryname=apply+cost) command to modify the MED value (cost) of BGP routes.
   * Run the [**apply ip-address next-hop**](cmdqueryname=apply+ip-address+next-hop) command to modify the next hops of BGP routes.
   * Run the [**apply local-preference**](cmdqueryname=apply+local-preference) command to modify the local preference value of BGP routes.
   * Run the [**apply origin**](cmdqueryname=apply+origin) command to modify the Origin attribute of BGP routes.
   * Run the [**apply extcommunity**](cmdqueryname=apply+extcommunity) command to modify the VPN target extended community attribute of BGP routes.
   * Run the [**apply extcommunity soo**](cmdqueryname=apply+extcommunity+soo) { *site-of-origin* } &<1-16> **additive** command to modify the SoO extended community attribute of BGP routes.
   * Run the [**apply extcommunity bandwidth**](cmdqueryname=apply+extcommunity+bandwidth) { *extCmntyString* | **none** } or [**apply extcommunity bandwidth**](cmdqueryname=apply+extcommunity+bandwidth) **aggregate** [ **limit** *bandwidth-value* ] command to modify the Link Bandwidth extended community attribute of BGP routes.
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   After the [**reflect change-path-attribute**](cmdqueryname=reflect+change-path-attribute) command is run on the RR, the [**peer route-policy**](cmdqueryname=peer+route-policy) **export** command takes precedence over the [**peer next-hop-invariable**](cmdqueryname=peer+next-hop-invariable) and [**peer next-hop-local**](cmdqueryname=peer+next-hop-local) commands.
9. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display bgp group**](cmdqueryname=display+bgp+group) [ *group-name* ] command to check information about a specified peer group.
* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table) [ *network* ] [ *mask* | *mask-length* ] [ **longer-prefixes** ] command to check information about routes in the BGP routing table.