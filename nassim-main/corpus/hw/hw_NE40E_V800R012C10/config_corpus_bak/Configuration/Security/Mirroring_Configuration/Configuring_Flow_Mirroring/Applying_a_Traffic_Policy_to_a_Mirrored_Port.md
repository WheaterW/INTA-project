Applying a Traffic Policy to a Mirrored Port
============================================

A traffic policy must be applied to an interface for the configured traffic behavior to take effect when the traffic passing through the interface matches the specified traffic classification rule.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
   
   
   
   This interface functions as the mirrored port.
3. Run [**traffic-policy**](cmdqueryname=traffic-policy) *policy-name* { **inbound** | **outbound** } [ **all-layer** | **link-layer** | **mpls-layer** ]
   
   
   
   The specified traffic policy is applied to the interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.