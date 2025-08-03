Applying the Traffic Policy
===========================

The traffic policy must be applied to an interface for the configured traffic behavior to take effect on the traffic passing through the interface.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**traffic-policy**](cmdqueryname=traffic-policy) *policy-name* { **inbound** | **outbound** } [ **all-layer** | **link-layer** | **mpls-layer** ]
   
   
   
   The traffic policy is applied to the interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.