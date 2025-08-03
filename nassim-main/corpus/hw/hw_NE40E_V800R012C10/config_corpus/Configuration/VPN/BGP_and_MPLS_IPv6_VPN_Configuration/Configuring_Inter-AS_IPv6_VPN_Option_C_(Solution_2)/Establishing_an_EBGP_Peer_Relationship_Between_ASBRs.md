Establishing an EBGP Peer Relationship Between ASBRs
====================================================

An EBGP peer relationship is established between ASBRs to advertise routes destined for the loopback interfaces on PEs.

#### Procedure

* Perform the following steps on each ASBR:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the interface connected to the peer ASBR is displayed.
  3. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* }
     
     
     
     The IP address is configured.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  5. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  6. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number*
     
     
     
     The remote ASBR is configured as the EBGP peer.
  7. (Optional) Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } **ebgp-max-hop** [ *hop-count* ]
     
     
     
     The maximum number of hops is set for the EBGP connection. This step is mandatory if the EBGP peers are not directly connected.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.