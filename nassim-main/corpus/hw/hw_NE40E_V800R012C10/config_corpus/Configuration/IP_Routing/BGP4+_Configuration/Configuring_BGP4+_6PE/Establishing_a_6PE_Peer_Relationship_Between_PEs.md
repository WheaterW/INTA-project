Establishing a 6PE Peer Relationship Between PEs
================================================

6PE peers can exchange IPv6 routes learned from their attached CEs.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**peer**](cmdqueryname=peer) *ipv4-address* [**as-number**](cmdqueryname=as-number) *as-number*
   
   
   
   The IP address of the peer and the number of the AS where the peer resides are specified.
4. Run [**peer**](cmdqueryname=peer) *ipv4-address* [**connect-interface**](cmdqueryname=connect-interface) *interface-type interface-number*
   
   
   
   The interface that is used to establish a connection with the remote PE is specified.
5. Run [**ipv6-family**](cmdqueryname=ipv6-family+unicast) **unicast**
   
   
   
   The BGP-IPv6 unicast address family view is displayed.
6. Run [**peer**](cmdqueryname=peer) *ipv4-address* [**enable**](cmdqueryname=enable)
   
   
   
   A 6PE peer relationship is established.
7. Run [**peer**](cmdqueryname=peer) *peerIpv4Addr* [**label-route-capability-only**](cmdqueryname=label-route-capability-only)
   
   
   
   The 6PE labeled route exchange capability is enabled.
   
   
   
   In the 6PE scenario, after the [**peer label-route-capability**](cmdqueryname=peer+label-route-capabilit) command is run, peers negotiate the label and unicast capabilities and advertise labeled routes only to the specified peer. However, in the 6PE scenario, peers do not need to negotiate the unicast capability. If the [**peer label-route-capability-only**](cmdqueryname=peer+label-route-capability-only) command is run, the device negotiates only the label capability and advertises labeled routes only to the specified peer. Therefore, the [**peer**](cmdqueryname=peer) [**label-route-capability-only**](cmdqueryname=label-route-capability-only) command is recommended in the 6PE scenario.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
9. Run [**quit**](cmdqueryname=quit)
   
   
   
   Exit the BGP-IPv6 unicast address family view.
10. Run [**quit**](cmdqueryname=quit)
    
    
    
    Exit the BGP view.
11. (Optional) Run [**mpls 6pe ttl-mode**](cmdqueryname=mpls+6pe+ttl-mode+pipe+uniform) { **pipe** | **uniform** }
    
    
    
    A mode of processing MPLS TTLs in 6PE route labels is configured.
12. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.