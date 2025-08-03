(Optional) Configuring IKE Peer Detection
=========================================

The IKE peer detection function detects invalid IKE peers to avoid black holes due to unreachable SA peers that discard data flows.

#### Context

Dead Peer Detection (DPD), as an alternative IKE keepalive mechanism, can minimize the number of messages used to detect peer state by using IPsec traffic. The DPD mechanism does not use the periodic message sending mechanism.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ike dpd**](cmdqueryname=ike+dpd+interval) **interval** *check-interval* [ *retry-interval* ] or [**ike dpd**](cmdqueryname=ike+dpd+on-demand+immediately) [ **on-demand** ] *check-interval* [ *retry-interval* ] [ **immediately** ]
   
   
   
   The DPD function is configured.
   
   * If **interval** is specified, the DPD function works in periodic mode. Within the period specified by *check-interval*, if the local end does not receive any traffic from the peer end, the local end periodically sends DPD packets.
   * If **on-demand** is specified, the DPD function works in On-demand mode. Within the period specified by *check-interval*, if the local end does not receive any traffic from the peer end, the local end sends a DPD packet.
   * If **interval** or **on-demand** is not specified, the DPD function works in On-demand mode.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.