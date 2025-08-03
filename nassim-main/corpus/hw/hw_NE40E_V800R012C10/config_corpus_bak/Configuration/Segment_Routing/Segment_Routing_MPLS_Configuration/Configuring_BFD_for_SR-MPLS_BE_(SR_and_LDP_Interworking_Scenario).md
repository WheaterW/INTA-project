Configuring BFD for SR-MPLS BE (SR and LDP Interworking Scenario)
=================================================================

This section describes how to use BFD to detect an LSP fault in an SR+LDP interworking scenario.

#### Usage Scenario

SR and LDP interworking enables SR and LDP to work together on the same network. SR-MPLS BE and LDP networks can be connected through this technology to implement MPLS forwarding.

If BFD for SR-MPLS BE detects a fault on the primary tunnel when SR communicates with LDP, an application, such as VPN FRR, rapidly switches traffic to minimize the impact on traffic.


#### Pre-configuration Tasks

Before configuring BFD for SR-MPLS BE (in the SR and LDP interworking scenario), complete the following tasks:

* [Configure IS-IS SR to communicate with LDP](dc_vrp_sr_all_cfg_0018.html) or [OSPF SR to communicate with LDP](dc_vrp_sr_all_cfg_0032.html).
* Set each LSR ID using the [**mpls lsr-id**](cmdqueryname=mpls+lsr-id) *lsr-id* command. Ensure that the route to the local *lsr-id* is reachable.

#### Procedure

* Create a BFD session on the SR side.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bfd**](cmdqueryname=bfd)
     
     
     
     The BFD view is displayed.
  3. Run [**mpls-passive**](cmdqueryname=mpls-passive)
     
     
     
     The egress is enabled to create a BFD session passively.
     
     The egress has to receive an LSP ping request carrying a BFD TLV before creating a BFD session.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  5. Run [**segment-routing**](cmdqueryname=segment-routing)
     
     
     
     The Segment Routing view is displayed.
  6. Run [**bfd enable**](cmdqueryname=bfd+enable) **mode** **tunnel** [ **filter-policy** **ip-prefix** *ip-prefix-name* | **effect-sr-lsp** | **nil-fec** ] \*
     
     
     
     BFD is enabled for SR LSPs.
     
     
     
     If **effect-sr-lsp** is specified and BFD goes down, the SR LSPs are withdrawn.
     
     In an SR and LDP interworking scenario, the ingress node cannot detect whether LDP LSPs are stitched to SR LSPs in the LDP to SR direction. In the LSP ping packet triggered by BFD, the encapsulated FEC type is LDP. When the packet arrives at the egress node (SR node), the FEC type fails to be verified, preventing BFD from going Up. To resolve this issue, configure the **nil-fec** parameter.
  7. (Optional) Run [**bfd**](cmdqueryname=bfd) **tunnel** { **min-rx-interval** *receive-interval* | **min-tx-interval** *transmit-interval* | **detect-multiplier** *multiplier-value* } \*
     
     
     
     BFD parameters are set for SR tunnels.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Create a BFD session on the LDP side.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bfd**](cmdqueryname=bfd)
     
     
     
     The BFD view is displayed.
  3. Run [**mpls-passive**](cmdqueryname=mpls-passive)
     
     
     
     The egress is enabled to create a BFD session passively.
     
     The egress has to receive an LSP ping request carrying a BFD TLV before creating a BFD session.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  5. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     The MPLS view is displayed.
  6. Run [**mpls bfd enable**](cmdqueryname=mpls+bfd+enable)
     
     
     
     An MPLS device to dynamically establish a BFD session.
  7. Run [**mpls bfd-trigger**](cmdqueryname=mpls+bfd-trigger) **host**
     
     
     
     Host IP routes are used as the policy for triggering LDP BFD sessions.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a device that connects the LDP area to the SR area.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     The MPLS view is displayed.
  3. Run [**lsp-trigger segment-routing-interworking best-effort host**](cmdqueryname=lsp-trigger+segment-routing-interworking+best-effort+host)
     
     
     
     A device is enabled to stitch SR LSPs to the proxy egress LSPs and transit LSPs that are established over non-local host routes with a 32-bit mask.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Verifying the Configuration

After successfully configuring BFD for SR-MPLS BE, run the [**display segment-routing bfd tunnel session**](cmdqueryname=display+segment-routing+bfd+tunnel+session) [ **prefix** *ip-address* { *mask* | *mask-length* } ] command to check information about the BFD session that monitors SR LSPs.