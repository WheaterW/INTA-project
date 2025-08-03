Configuring Interface-based Traffic Suppression
===============================================

This section describes how to configure interface-based traffic suppression in order to reduce the traffic burden on a network.

#### Context

Traffic suppression can be implemented only on a Layer 2 interface.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**portswitch**](cmdqueryname=portswitch)
   
   
   
   The interface is configured to work in Layer 2 mode.
4. Run [**broadcast discard**](cmdqueryname=broadcast+discard)
   
   
   
   The interface is disabled from forwarding broadcast packets.
5. Run [**unknown-multicast discard**](cmdqueryname=unknown-multicast+discard)
   
   
   
   The interface is disabled from forwarding unknown multicast packets.
6. Run [**unknown-unicast discard**](cmdqueryname=unknown-unicast+discard)
   
   
   
   The interface is disabled from forwarding unknown unicast packets.
7. Run [**broadcast-suppression**](cmdqueryname=broadcast-suppression) { *percent-value* | **value** *bw-value* } { **inbound** | **outbound** }
   
   
   
   The maximum volume of broadcast traffic allowed on the interface is configured.
8. Run [**multicast-suppression**](cmdqueryname=multicast-suppression) { *percent-value* | **value** *bw-value* } { **inbound** | **outbound** }
   
   
   
   The maximum volume of multicast traffic allowed on the interface is configured.
9. Run [**unknown-unicast-suppression**](cmdqueryname=unknown-unicast-suppression) { *percent-value* | **value** *bw-value* } { **inbound** | **outbound** }
   
   
   
   The maximum volume of unknown unicast traffic allowed on the interface is configured.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.