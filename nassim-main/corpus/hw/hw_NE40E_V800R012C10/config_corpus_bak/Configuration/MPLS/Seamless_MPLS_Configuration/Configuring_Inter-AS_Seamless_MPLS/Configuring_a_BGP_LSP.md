Configuring a BGP LSP
=====================

Before a BGP LSP is established, a routing policy must be configured to control label distribution. The egress of the BGP LSP to be established needs to assign an MPLS label to the route advertised to an upstream node. If a transit node receives a labeled IPv4 route from downstream, the downstream node must re-assign an MPLS label to the transit node and advertises the label upstream.

#### Procedure

* Perform the following steps on each CSG and MASG:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**route-policy**](cmdqueryname=route-policy+node) *route-policy-name* *matchMode* **node** *node*
     
     
     
     A Route-Policy node is created.
  3. Run [**apply mpls-label**](cmdqueryname=apply+mpls-label)
     
     
     
     The local device is enabled to assign a label to an IPv4 route.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  5. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  6. Run [**peer**](cmdqueryname=peer+route-policy+export) { *ipv4-address* | *group-name* } **route-policy** *route-policy-name* **export**
     
     
     
     A routing policy for advertising routes matching Route-Policy conditions to a BGP peer or a BGP peer group is configured.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Repeat this step for each BGP peer.
  7. Run [**network**](cmdqueryname=network+route-policy) *ip-address* [ *mask* | *mask-length* ] [ **route-policy** *route-policy-name* ]
     
     
     
     The route destined for the loopback interface address is advertised.
     
     This route is labeled and advertised along a path over which a BGP LSP is established.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Perform the following steps on each AGG, AGG ASBR, and core ASBR:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**route-policy**](cmdqueryname=route-policy+node) *route-policy-name* *matchMode* **node** *node*
     
     
     
     A Route-Policy node is created.
  3. Run [**if-match mpls-label**](cmdqueryname=if-match+mpls-label)
     
     
     
     An IPv4 route is enabled to match an MPLS label.
  4. Run [**apply mpls-label**](cmdqueryname=apply+mpls-label)
     
     
     
     The local device is enabled to assign a label to an IPv4 route.
  5. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  6. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  7. Run [**peer**](cmdqueryname=peer+route-policy+export) { *ipv4-address* | *group-name* } **route-policy** *route-policy-name* **export**
     
     
     
     A routing policy for advertising routes matching Route-Policy conditions to a BGP peer or a BGP peer group is configured.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Repeat this step for each BGP peer.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If the MTU of LDP LSPs is different from that of BGP LSPs, traffic may fail to be forwarded. To set an MTU for BGP LSPs, run the **bgp-lsp mtu** *mtu* command.
  
  If the MTU of LDP LSPs is different from that of BGP local IFNET tunnels, traffic may fail to be forwarded. To set an MTU for BGP local IFNET tunnels, run the [**bgp-local-ifnet mtu**](cmdqueryname=bgp-local-ifnet+mtu) *lifnmtuVal* command.