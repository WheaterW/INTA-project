Disabling Flow Mirroring
========================

When the flow mirroring function is not required, disable it so that it does not adversely affect user services.

#### Context

When disabling flow mirroring, you can delete the observing port configuration of the specified interface, the observing port configuration for mirroring, and the traffic policy applied to the corresponding interface in any sequence.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
   
   
   
   This interface functions as the observing port.
3. Run [**undo port-observing observe-index**](cmdqueryname=undo+port-observing+observe-index) *observe-index*
   
   
   
   The observing port configuration is deleted.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
5. Run [**slot**](cmdqueryname=slot) *slot-id*
   
   
   
   The slot view is displayed.
6. Run [**undo mirror to observe-index**](cmdqueryname=undo+mirror+to+observe-index) *observe-index*
   
   
   
   The observing port configuration for mirroring is deleted.
7. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
8. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
   
   
   
   This interface functions as the mirrored port.
9. Run [**undo traffic-policy**](cmdqueryname=undo+traffic-policy) { **inbound** | **outbound** } [ **link-layer** | **mpls-layer** ]
   
   
   
   The traffic policy applied to the interface is deleted.
10. Run [**quit**](cmdqueryname=quit)
    
    
    
    Return to the system view.
11. Run [**traffic behavior**](cmdqueryname=traffic+behavior) *behavior-name*
    
    
    
    The traffic behavior view is displayed.
12. Run [**undo port-mirroring to**](cmdqueryname=undo+port-mirroring+to) { **observe-index** *observe-index* &<1-8> }
    
    
    
    The configuration of the observing port specified for interface-based flow mirroring is deleted.
13. Run [**undo port-mirroring enable**](cmdqueryname=undo+port-mirroring+enable)
    
    
    
    Flow mirroring is disabled.
14. Run [**quit**](cmdqueryname=quit)
    
    
    
    Return to the system view.
    
    
    
    The traffic policy, behavior, and classifier defined for mirrored packets can be deleted if they are no longer required.
15. Run [**undo traffic policy**](cmdqueryname=undo+traffic+policy) *policy-name*
    
    
    
    The traffic policy defined for flow mirroring is deleted.
16. Run [**undo traffic behavior**](cmdqueryname=undo+traffic+behavior) *behavior-name*
    
    
    
    The traffic behavior defined for flow mirroring is deleted.
17. Run [**undo traffic classifier**](cmdqueryname=undo+traffic+classifier) *classifier-name*
    
    
    
    The traffic classifier defined for flow mirroring is deleted.
18. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.