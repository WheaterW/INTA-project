Configuring Sub-interface-based Traffic Suppression
===================================================

This section describes how to configure sub-interface-based traffic suppression in order to reduce the traffic burden on a network.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** ]
   
   
   
   A VSI is created.
3. Run [**suppression**](cmdqueryname=suppression) { **inbound** | **outbound** } **enable**
   
   
   
   Traffic suppression is enabled for the VSI.
4. Run [**pwsignal**](cmdqueryname=pwsignal) **ldp**
   
   
   
   A signaling mode is configured for the VSI.
5. Run [**vsi-id**](cmdqueryname=vsi-id) *vsi-id*
   
   
   
   An ID is configured for the VSI.
6. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the VSI view.
7. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
8. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number.subinterface-number*
   
   
   
   The sub-interface view is displayed.
9. Run [**vlan-type**](cmdqueryname=vlan-type) **dot1q** *vlan-id*
   
   
   
   The sub-interface is associated with a VLAN, and a VLAN encapsulation mode is configured for the sub-interface.
10. Run [**l2 binding**](cmdqueryname=l2+binding) **vsi** *vsi-name* [ **access-port** ]
    
    
    
    The sub-interface is bound to the VSI.
11. Run [**broadcast-suppression**](cmdqueryname=broadcast-suppression) **cir** *cirVal* [ **cbs** *cbsVal* ] { **inbound** | **outbound** }
    
    
    
    The maximum volume of broadcast traffic allowed on the sub-interface is configured.
12. Run [**multicast-suppression**](cmdqueryname=multicast-suppression) **cir** *cirVal* [ **cbs** *cbsVal* ] { **inbound** | **outbound** }
    
    
    
    The maximum volume of multicast traffic allowed on the sub-interface is configured.
13. Run [**unknown-unicast-suppression**](cmdqueryname=unknown-unicast-suppression) **cir** *cirVal* [ **cbs** *cbsVal* ] { **inbound** | **outbound** }
    
    
    
    The maximum volume of unknown unicast traffic allowed on the sub-interface is configured.
14. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.