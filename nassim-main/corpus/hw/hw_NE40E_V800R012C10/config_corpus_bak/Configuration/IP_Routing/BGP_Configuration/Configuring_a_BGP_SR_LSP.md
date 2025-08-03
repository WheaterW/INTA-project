Configuring a BGP SR LSP
========================

Deploying a complete BGP SR LSP on devices in the same AS helps implement end-to-end service interworking.

#### Usage Scenario

On the network shown in [Figure 1](#EN-US_TASK_0000001167360277__fig142771575412), OSPF runs between DeviceA and DeviceB, between DeviceB and DeviceC, and between DeviceD and DeviceE. IS-IS runs between DeviceC and DeviceD. Basic MPLS capabilities and MPLS LDP are configured on DeviceA through DeviceE so that LDP LSPs are established between loopback interfaces of devices in each IGP area. Therefore, traffic between loopback interfaces of devices in each IGP area is encapsulated using MPLS. However, traffic cannot be transmitted across IGP areas because devices cannot ping each other across IGP areas. For example, DeviceA cannot ping DeviceE. To solve this problem, you need to configure an inner MPLS tunnel (BGP SR LSP) from 1.1.1.1 to 5.5.5.5 so that the traffic from 1.1.1.1 to 5.5.5.5 is forwarded through MPLS.

**Figure 1** Configuring a BGP SR LSP  
![](figure/en-us_image_0000001120600478.png)

#### Procedure

* Configure an SRGB.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     BGP is started (with the local AS number specified), and the BGP view is displayed.
  3. Run [**segment-routing global-block**](cmdqueryname=segment-routing+global-block) *begin-value* *end-value*
     
     A BGP SRGB is configured.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure a BGP peer relationship.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     The BGP view is displayed.
  3. Run [**peer**](cmdqueryname=peer) *ipv4-address* [**as-number**](cmdqueryname=as-number) *as-number*
     
     The IP address of a peer and the number of the AS where the peer resides are specified.
  4. Run [**peer**](cmdqueryname=peer) *ipv4-address* [**connect-interface**](cmdqueryname=connect-interface) *interface-type* *interface-number* [ *ipv4-source-address* ]
     
     A source interface and a source address to set up a TCP connection with the BGP peer are specified.
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure DeviceC and DeviceD as RRs.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     The BGP view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
     
     The BGP-IPv4 unicast address family view is displayed.
  4. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } [**reflect-client**](cmdqueryname=reflect-client)
     
     An RR is configured, and its peer is specified as a client.
     
     Configure DeviceA and DeviceD as clients of DeviceC, and configure DeviceC and DeviceE as clients of DeviceD.
  5. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } [**next-hop-local**](cmdqueryname=next-hop-local)
     
     The device is configured to set the next hop address to its own address when advertising routes to clients.
     
     To enable DeviceC or DeviceD to change the next hop address of a route to the local address before advertising the route to clients, run the [**peer next-hop-local**](cmdqueryname=peer+next-hop-local) command on DeviceC or DeviceD for each related client.
  6. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Enable the function to exchange labeled IPv4 routes.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     The BGP view is displayed.
  3. Run [**peer**](cmdqueryname=peer+label-route-capability+check-tunnel-reachable) { *ipv4-address* | *group-name* } **label-route-capability** [ **check-tunnel-reachable** ]
     
     The device is configured to exchange labeled IPv4 routes with a specified BGP peer.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure the ingress for a BGP SR LSP.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**route-policy**](cmdqueryname=route-policy) *route-policy-name* *matchMode* **node** *node*
     
     A route-policy with a node is created, and the route-policy view is displayed.
  3. Run [**apply mpls-label**](cmdqueryname=apply+mpls-label)
     
     The device is configured to allocate labels to IPv4 routes.
  4. Run [**quit**](cmdqueryname=quit)
     
     Return to the system view.
  5. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     The BGP view is displayed.
  6. Run [**network**](cmdqueryname=network+route-policy+label-index) *ipv4-address* [ *mask* | *mask-length* ] [ **route-policy** *route-policy-name* | **route-filter** *route-filter-name* ] [ **non-relay-tunnel** ] **label-index**  *label-index-value*
     
     BGP is configured to import a local route, and an offset is specified for the SRGB.
  7. Run [**peer**](cmdqueryname=peer+route-policy+export) { *ipv4-address* | *group-name* } **route-policy** *route-policy-name* **export**
     
     The route-policy is applied to the routes to be advertised to the specified BGP peer.
  8. Run **ipv4-family unicast**
     
     The BGP-IPv4 unicast address family view is displayed.
  9. Run [**peer**](cmdqueryname=peer+prefix-sid) *peerIpv4Addr* **prefix-sid**
     
     The device is configured to exchange prefix SID information with the specified IPv4 peer.
  10. Run [**commit**](cmdqueryname=commit)
      
      The configuration is committed.
* Configure a transit node for the BGP SR LSP.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**route-policy**](cmdqueryname=route-policy+node) *route-policy-name* **matchMode** **node** *node*
     
     A route-policy with a node is created, and the route-policy view is displayed.
  3. Run [**if-match mpls-label**](cmdqueryname=if-match+mpls-label)
     
     Labeled IPv4 routes are matched.
  4. Run [**apply mpls-label**](cmdqueryname=apply+mpls-label)
     
     The device is configured to allocate labels to IPv4 routes.
  5. Run [**quit**](cmdqueryname=quit)
     
     Return to the system view.
  6. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     The BGP view is displayed.
  7. Run [**peer**](cmdqueryname=peer+route-policy+export) { *ipv4-address* | *group-name* } **route-policy** *route-policy-name* **export**
     
     The route-policy is applied to the routes to be advertised to the specified BGP peer.
  8. Run **ipv4-family unicast**
     
     The BGP-IPv4 unicast address family view is displayed.
  9. Run [**peer**](cmdqueryname=peer+prefix-sid) *peerIpv4Addr* **prefix-sid**
     
     The device is configured to exchange prefix SID information with the specified IPv4 peer.
  10. Run [**commit**](cmdqueryname=commit)
      
      The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, verify it.

* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table+prefix-sid+srgb) *ipv4-address* [ *mask* | *mask-length* ] **prefix-sid** **srgb** command to check SRGB information of the BGP routes with a specified destination address.

* Run the [**display mpls lsp**](cmdqueryname=display+mpls+lsp) command to check BGP SR LSP information.