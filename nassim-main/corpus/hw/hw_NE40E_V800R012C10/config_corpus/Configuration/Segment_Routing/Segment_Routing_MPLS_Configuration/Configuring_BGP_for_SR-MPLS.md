Configuring BGP for SR-MPLS
===========================

A controller orchestrates IGP SIDs and BGP SR-allocated BGP peer SIDs to implement inter-AS forwarding over the optimal path.

#### Context

BGP is a dynamic routing protocol used between ASs. BGP SR is a BGP extension for SR and is used for inter-AS source routing.

BGP SR uses BGP egress peer engineering (EPE) to allocate Peer-Node and Peer-Adj SIDs to peers or Peer-Set SIDs to peer groups. These SIDs can be reported to the controller through BGP-LS for orchestrating E2E SR-MPLS TE tunnels.


#### Procedure

* Configure MPLS on ASBRs.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**mpls lsr-id**](cmdqueryname=mpls+lsr-id) *lsr-id* command to configure an LSR ID for the local node.
  3. Run the [**mpls**](cmdqueryname=mpls) command to enter the MPLS view.
  4. (Optional) Run the [**mpls te**](cmdqueryname=mpls+te) command to enable MPLS TE globally on the local node.
  5. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
  6. Run the [**interface**](cmdqueryname=interface) *interface-type interface-number* command to enter the view of the interface connecting the ASBRs.
  7. Run the [**mpls**](cmdqueryname=mpls) command to enable MPLS on the interface.
  8. (Optional) Run the [**mpls te**](cmdqueryname=mpls+te) command to enable MPLS TE on the interface.
  9. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
* Configure BGP EPE.
  1. Run [**segment-routing**](cmdqueryname=segment-routing)
     
     
     
     SR is enabled.
  2. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  3. Run [**bgp**](cmdqueryname=bgp) { *as-number-plain* | *as-number-dot* }
     
     
     
     BGP is enabled, and the BGP view is displayed.
  4. Run [**peer**](cmdqueryname=peer+as-number) *ipv4-address* **as-number** { *as-number-plain* | *as-number-dot* }
     
     
     
     A BGP peer is created.
  5. Run [**peer**](cmdqueryname=peer+egress-engineering) *ipv4-address* **egress-engineering** [ **label** *static-label* ]
     
     
     
     BGP EPE is enabled.
  6. Run [**peer**](cmdqueryname=peer+egress-engineering) *ipv4-address* **egress-engineering** **link-down** { **relate-bfd-state** | **label-pop** }
     
     
     
     BGP EPE link fault association is enabled.
     
     
     
     The **relate-bfd-state** and **label-pop** parameters are mutually exclusive. Therefore, you can configure only one of them.
     
     + With the **relate-bfd-state** parameter configured, if the inter-AS link corresponding to a BGP EPE label fails, BGP EPE triggers SBFD for SR-MPLS TE tunnel in the local AS to go down. This enables the ingress of the involved SR-MPLS TE tunnel to rapidly detect the failure and switch traffic to another normal tunnel.
     + With the **label-pop** parameter configured, if the inter-AS link corresponding to a BGP EPE label fails, the ASBR in the local AS pops the BGP EPE label from the received data packet and searches the IP routing table based on the destination address of the packet for forwarding.
  7. (Optional) Configure a peer set.
     
     
     1. Run [**egress-engineering peer-set**](cmdqueryname=egress-engineering+peer-set) *peer-set-name* [ **label** *static-label* ]
        
        A BGP peer set is created.
     2. Run [**peer**](cmdqueryname=peer+peer-set) *ipv4-address* **peer-set** **name** *peer-set-name*
        
        A specified peer is added to the BGP peer set.
     3. Run [**egress-engineering peer-set**](cmdqueryname=egress-engineering+peer-set) *peer-set-name* **link-down** { **relate-bfd-state** | **label-pop** }
        
        Link fault association is configured for the BGP peer set.
  8. (Optional) Run [**egress-engineering confederation-id compatible**](cmdqueryname=egress-engineering+confederation-id+compatible)
     
     
     
     The device is configured to modify the BGP-LS packet format and fill the member AS number in the AS field of the BGP-LS route prefix in a BGP EPE confederation scenario.
  9. (Optional) Run [**egress-engineering traffic-statistics enable**](cmdqueryname=egress-engineering+traffic-statistics+enable)
     
     
     
     BGP EPE traffic statistics collection is enabled.
     
     
     
     To clear traffic statistics for re-collection, run the [**reset bgp egress-engineering traffic-statistics**](cmdqueryname=reset+bgp+egress-engineering+traffic-statistics) command.
  10. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
  11. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view
* Configure BGP-LS.
  
  
  
  BGP-LS provides a simple and efficient method of collecting topology information. You must configure a BGP-LS peer relationship between the controller and forwarder, so that topology information can be properly reported from the forwarder to the controller. This example provides the procedure for configuring a BGP-LS peer relationship on the forwarder. The procedure on the controller is similar to that on the forwarder.
  
  
  
  1. Run [**bgp**](cmdqueryname=bgp) { *as-number-plain* | *as-number-dot* }
     
     
     
     BGP is enabled, and the BGP view is displayed.
  2. Run [**peer**](cmdqueryname=peer+as-number) *ipv4-address* **as-number** *as-number-plain*
     
     
     
     A BGP peer is created.
  3. Run [**link-state-family unicast**](cmdqueryname=link-state-family+unicast)
     
     
     
     BGP-LS is enabled, and the BGP-LS address family view is displayed.
  4. Run [**peer**](cmdqueryname=peer+enable) { *group-name* | *ipv4-address* } **enable**
     
     
     
     The device is enabled to exchange BGP-LS routing information with a specified peer or peer group.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Verifying the Configuration

After configuring BGP SR, run the [**display bgp egress-engineering**](cmdqueryname=display+bgp+egress-engineering) command to check BGP EPE information and determine whether the configuration succeeds.

After BGP EPE traffic statistics collection is enabled, you can run the [**display bgp egress-engineering traffic-statistics outbound**](cmdqueryname=display+bgp+egress-engineering+traffic-statistics+outbound) command to check the outgoing traffic and the [**display bgp egress-engineering traffic-statistics inbound**](cmdqueryname=display+bgp+egress-engineering+traffic-statistics+inbound) command to check the incoming traffic.