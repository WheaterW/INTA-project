Configuring Transparent Transmission of PDUs on a VLL/EVPL/VPLS/EVPN Network
============================================================================

This section describes how to transparently transmit untagged Layer 2 protocol data units (PDUs), such as LACP, LLDP, BPDU, CDP, and UDLD packets, on a VLL/EVPL/VPLS/EVPN network to implement Layer 2 negotiation with remote users.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) { *interface-name* | *interface-type* *interface-number* }
   
   
   
   The sub-interface view is displayed
3. Run [**link-protocol transport**](cmdqueryname=link-protocol+transport) { **lacp** | **lldp** | **bpdu** | **cdp** | **udld** } { **untag** | **untag-vlan-check** }
   
   
   
   The types of Layer 2 protocols that the interface can transparently transmit are configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.