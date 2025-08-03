Configuring Interface- and VLAN-based Traffic Suppression
=========================================================

This section describes how to configure interface- and VLAN-based traffic suppression in order to reduce the traffic burden on a network.

#### Context

Traffic suppression can be implemented only on a Layer 2 interface.

If you configure broadcast packet suppression on an interface for multiple times, the latest configuration overrides the previous one. However, if you reconfigure traffic suppression on an interface that is added to a VLAN, the previous configuration needs to be deleted before the reconfiguration.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**portswitch**](cmdqueryname=portswitch)
   
   
   
   The interface is configured to work in Layer 2 mode.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
5. Run [**vlan batch**](cmdqueryname=vlan+batch) { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10>
   
   
   
   A VLAN is created.
6. Run [**port**](cmdqueryname=port) *interface-type* { *interface-number1* [ **to** *interface-number2* ] } &<1-10>
   
   
   
   The interface is added to the VLAN.
7. Run [**suppression**](cmdqueryname=suppression) { **inbound** | **outbound** } **enable**
   
   
   
   Traffic suppression is enabled for the VLAN.
8. Run [**unknown-multicast discard**](cmdqueryname=unknown-multicast+discard)
   
   
   
   Interfaces in the VLAN are disabled from forwarding unknown multicast packets.
9. Run [**unknown-unicast discard**](cmdqueryname=unknown-unicast+discard)
   
   
   
   Interfaces in the VLAN are disabled from forwarding unknown unicast packets.
10. Run [**quit**](cmdqueryname=quit)
    
    
    
    Return to the system view.
11. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
    
    
    
    The interface view is displayed.
12. Run [**broadcast-suppression**](cmdqueryname=broadcast-suppression) **cir** *cir-value* [ **cbs** *cbs-value* ] { **inbound** | **outbound** } {**vlan** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10> }
    
    
    
    Interface- and VLAN-based broadcast traffic suppression is configured.
13. Run [**multicast-suppression**](cmdqueryname=multicast-suppression) **cir** *cir-value* [ **cbs** *cbs-value* ] { **inbound** | **outbound** } {**vlan** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10> }
    
    
    
    Interface- and VLAN-based multicast traffic suppression is configured.
14. Run [**unknown-unicast-suppression**](cmdqueryname=unknown-unicast-suppression) **cir** *cir-value* [ **cbs** *cbs-value* ] { **inbound** | **outbound** } {**vlan** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10> }
    
    
    
    Interface- and VLAN-based unknown unicast traffic suppression is configured.
15. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.