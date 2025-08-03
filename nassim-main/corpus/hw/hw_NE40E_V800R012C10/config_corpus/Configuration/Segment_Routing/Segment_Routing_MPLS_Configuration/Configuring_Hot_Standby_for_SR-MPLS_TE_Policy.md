Configuring Hot Standby for SR-MPLS TE Policy
=============================================

This section describes how to configure hot standby (HSB) for SR-MPLS TE Policy.

#### Usage Scenario

SBFD for SR-MPLS TE Policy can quickly detect segment list faults. If all the segment lists of the primary path are faulty, SBFD triggers a candidate path HSB switchover to reduce impacts on services.


#### Pre-configuration Tasks

Before configuring HSB for SR-MPLS TE Policy, configure one or more SR-MPLS TE Policies.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**segment-routing**](cmdqueryname=segment-routing)
   
   
   
   SR is enabled globally and the Segment Routing view is displayed.
3. Enable HSB for SR-MPLS TE Policy.
   
   
   
   HSB for SR-MPLS TE Policy supports both global configuration and individual configuration. Select either of the following configuration modes as needed:
   
   * Global configuration
     
     1. Run [**sr-te-policy backup hot-standby enable**](cmdqueryname=sr-te-policy+backup+hot-standby+enable)
        
        HSB is enabled for all SR-MPLS TE Policies.
   * Individual configuration
     
     1. Run [**sr-te policy**](cmdqueryname=sr-te+policy) *policy-name*
        
        The SR-MPLS TE Policy view is displayed.
     2. Run [**backup hot-standby**](cmdqueryname=backup+hot-standby) { **enable** | **disable** }
        
        HSB is enabled or disabled for a single SR-MPLS TE Policy.
   
   If an SR-MPLS TE Policy has both global configuration and individual configuration, the individual configuration takes effect.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.