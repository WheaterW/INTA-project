Establishing an EBGP Peer Relationship Between ASBRs
====================================================

An EBGP peer relationship is established between ASBRs
to advertise routes destined for the loopback interfaces on PEs.

#### Procedure

* Perform the following steps on each ASBR:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* }
     
     
     
     The IP address is configured.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  5. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  6. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number*
     
     
     
     The remote ASBR is configured as the EBGP peer.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.