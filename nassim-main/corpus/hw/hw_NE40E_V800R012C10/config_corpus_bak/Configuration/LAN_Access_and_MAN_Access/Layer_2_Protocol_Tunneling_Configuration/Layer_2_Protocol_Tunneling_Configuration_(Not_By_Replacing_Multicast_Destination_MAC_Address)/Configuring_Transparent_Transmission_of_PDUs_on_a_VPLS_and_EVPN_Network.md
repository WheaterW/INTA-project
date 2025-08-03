Configuring Transparent Transmission of PDUs on a VPLS/EVPN Network
===================================================================

This section describes how to transparently transmit untagged Layer 2 protocol data units (PDUs), such as LACP, LLDP, BPDU, CDP, and UDLD packets, on a VPLS/EVPN network to implement Layer 2 negotiation with remote users.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) { *interface-name* | *interface-type* *interface-number* }
   
   
   
   The sub-interface view of the AC interface is displayed.
3. Run [**link-protocol transport**](cmdqueryname=link-protocol+transport) { **lacp** | **lldp** | **bpdu** | **cdp** | **udld** }
   
   
   
   The type of Layer 2 PDUs that can be transparently transmitted through the sub-interface is specified.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.