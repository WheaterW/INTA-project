Configuring a Manual mLDP P2MP Tunnel
=====================================

A manual mLDP P2MP tunnel can be manually triggered and transmit multicast services, excluding multicast VPN services.

#### Context

Manually configure the root and leaf nodes to trigger the establishment of a manual mLDP P2MP tunnel.


#### Procedure

* Enable mLDP P2MP globally.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
     
     
     
     The MPLS-LDP view is displayed.
  3. Run [**mldp p2mp**](cmdqueryname=mldp+p2mp)
     
     
     
     mLDP P2MP is enabled globally.
  4. (Optional) Run [**mldp make-before-break**](cmdqueryname=mldp+make-before-break)
     
     
     
     The mLDP make-before-break (MBB) capability is enabled.
     
     
     
     If the optimal route between a non-root node and a root node on an mLDP P2MP network changes, the non-root node re-selects an upstream node and by default tears down the current P2MP LSP. As a result, traffic is dropped before a new P2MP LSP is established. To prevent traffic loss, the mLDP MBB capability can be enabled. If the optimal route to the root node changes, the node does not delete the original P2MP LSP until a new P2MP LSP is established. This minimizes traffic loss.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* (Optional) Disable mLDP P2MP on an interface.
  
  
  
  To flexibly control the path of a P2MP LSP, you can disable mLDP P2MP on a specified interface.
  
  Disabling mLDP P2MP on an interface helps you plan a network. For example, if links balance traffic on a network, to enable P2MP traffic to travel along a specific link, disable mLDP P2MP on the interfaces connected to other links.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**mpls mldp p2mp disable**](cmdqueryname=mpls+mldp+p2mp+disable)
     
     
     
     mLDP P2MP is disabled on the interface.
     
     
     
     Disabling mLDP P2MP on an interface affects the establishment of P2MP LSPs, but does not cause the reestablishment of other P2P LDP sessions.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure each leaf node to trigger mLDP P2MP LSP establishment.
  
  
  
  After mLDP P2MP is enabled on all nodes, configure each leaf node to trigger mLDP P2MP LSP establishment.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
     
     
     
     The MPLS-LDP view is displayed.
  3. Run [**mldp p2mp-lsp**](cmdqueryname=mldp+p2mp-lsp+name+root-ip+lsp-id) **name** *p2mp-lsp-name* **root-ip** *root-ip-address* **lsp-id** *lsp-id*
     
     
     
     The leaf node is configured to trigger the establishment of an mLDP P2MP LSP from the specified root node to the current leaf node.
     
     
     
     *p2mp-lsp-name* specifies the name of the P2MP LSP, *root-ip-address* specifies the IP address of the root node, and *lsp-id* specifies the ID of the P2MP LSP. The *root-ip-address* and *lsp-id* parameters together uniquely identify an mLDP P2MP LSP.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* (Optional) Configure an mLDP P2MP tunnel interface.
  
  
  
  Before multicast traffic can be steered into an mLDP P2MP LSP, the mLDP P2MP LSP must be bound to an mLDP P2MP tunnel interface so that the tunnel interface can be statically added to an Internet Group Management Protocol (IGMP) multicast group.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mldp-p2mp-tunnel**](cmdqueryname=mldp-p2mp-tunnel) *tunnel-name*
     
     
     
     An mLDP P2MP tunnel interface is configured.
  3. Run [**root-ip**](cmdqueryname=root-ip+lsp-id) *root-ip-address* **lsp-id** *lsp-id*
     
     
     
     An mLDP P2MP LSP is bound to the tunnel interface.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* (Optional) Configure a tunnel establishment policy that allows mLDP to select an upstream node based on peer IDs.
  
  
  
  By default, a leaf or transit node selects the next hop on the optimal route to the root node as its upstream node during P2MP tunnel establishment. If routes work in load balancing mode, more than one such upstream node exists, and a leaf or transit node randomly selects an upstream node among the candidates. If you want a leaf or transit node to select a specific upstream node, configure a tunnel establishment policy that allows mLDP to select an upstream node based on peer IDs â an upstream node with the largest or smallest peer ID.
  
  Both NG MVPN over mLDP P2MP and VPLS over mLDP P2MP have the dual-root 1+1 protection mechanism. If the routes to the primary and backup roots work in load balancing mode and share some links, an upstream node may be selected by mLDP for both the primary and backup mLDP tunnels. In this case, if the shared link where the selected upstream node resides becomes faulty, dual-root 1+1 protection fails to take effect. To prevent such a protection failure in the scenario with co-routed primary and backup mLDP tunnels, run the [**mldp upstream-lsr-select highest**](cmdqueryname=mldp+upstream-lsr-select+highest) command for one tunnel and the [**mldp upstream-lsr-select lowest**](cmdqueryname=mldp+upstream-lsr-select+lowest) command for the other tunnel.
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**ip ip-prefix**](cmdqueryname=ip+ip-prefix+permit+deny)*ip-prefix-name*{ **permit** | **deny** } *ip-address*
     
     A policy for selecting tunnels to specified root nodes is configured.
  3. Run [**mpls**](cmdqueryname=mpls)
     
     MPLS is enabled, and the MPLS view is displayed.
  4. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
     
     The MPLS-LDP view is displayed.
  5. Run [**mldp p2mp**](cmdqueryname=mldp+p2mp)
     
     mLDP P2MP is enabled globally.
  6. Configure a tunnel establishment policy that allows mLDP to select an upstream node based on peer IDs.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If both the [**mldp upstream-lsr-select highest**](cmdqueryname=mldp+upstream-lsr-select+highest) and [**mldp upstream-lsr-select lowest**](cmdqueryname=mldp+upstream-lsr-select+lowest) commands are run and the same mLDP root node is specified in them, only the [**mldp upstream-lsr-select highest**](cmdqueryname=mldp+upstream-lsr-select+highest) command configuration takes effect.
     
     + Run the [**mldp upstream-lsr-select lowest ip-prefix**](cmdqueryname=mldp+upstream-lsr-select+lowest+ip-prefix) *ip-prefix-name* command to configure a tunnel establishment policy that allows mLDP to select an upstream node with the smallest peer ID.
     + Run the [**mldp upstream-lsr-select highest ip-prefix**](cmdqueryname=mldp+upstream-lsr-select+highest+ip-prefix) *ip-prefix-name* command to configure a tunnel establishment policy that allows mLDP to select an upstream node with the largest peer ID.
  7. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* (Optional) Disabling mLDP from Using the Default Route to Establish Tunnels
  
  
  
  In a scenario where mLDP P2MP uses intra-AS routes or inter-AS BGP routes to tunnel root nodes to establish mLDP tunnels, you can configure mLDP not to use the default route 0.0.0.0/0 to establish an mLDP tunnel if such a tunnel is not expected.
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**mpls**](cmdqueryname=mpls)
     
     MPLS is enabled, and the MPLS view is displayed.
  3. Run [**quit**](cmdqueryname=quit)
     
     Return to the system view.
  4. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
     
     The MPLS-LDP view is displayed.
  5. Run [**mldp p2mp**](cmdqueryname=mldp+p2mp)
     
     mLDP P2MP is enabled globally.
  6. Run **[**mldp default-route-match ignore**](cmdqueryname=mldp+default-route-match+ignore)**
     
     mLDP is disabled from using the default route to establish tunnels.
  7. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.

#### Follow-up Procedure

Statically add the tunnel interface to an IGMP multicast group to allow multicast traffic to be steered into the mLDP tunnel.