Configuring Ring Network Topology Isolation
===========================================

In scenarios where multiple ring networks that belong to the same BD but different VLANs connect to an EVPN, you can configure ring network topology isolation on AC sub-interfaces. This configuration isolates the topologies of these ring networks and reduces the number of Layer 2 protocol packets transparently transmitted between the networks. In this way, the sub-interfaces transparently transmit Layer 2 protocol packets only after the packets pass the VLAN check on these sub-interfaces.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-name*
   
   
   
   The interface view is displayed.
3. Run [**link-protocol transport**](cmdqueryname=link-protocol+transport) **bpdu untag-vlan-check**
   
   
   
   Ring network topology isolation is configured. The sub-interface can transparently transmit Layer 2 protocol packets only after these packets pass the VLAN check on the sub-interface.