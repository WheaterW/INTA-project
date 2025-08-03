Configuring HSB for SRv6 TE Policy
==================================

This section describes how to configure hot standby (HSB) for SRv6 TE Policy.

#### Usage Scenario

SBFD for SRv6 TE Policy and U-BFD for SRv6 TE Policy can quickly detect segment list failures. If all the segment lists of the primary path fail, SBFD or U-BFD triggers a candidate path HSB switchover to minimize the impact on services.


#### Pre-configuration Tasks

Before configuring HSB for SRv6 TE Policy, complete the following tasks:

* Configure an SRv6 TE Policy.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6)
   
   
   
   SRv6 is enabled globally, and the SRv6 view is displayed.
3. Enable HSB for the SRv6 TE Policy.
   
   
   
   HSB for SRv6 TE Policy supports both global configuration and single-policy configuration. Select either of the following configuration modes as needed:
   
   * Global configuration
     
     1. Run [**srv6-te-policy backup hot-standby enable**](cmdqueryname=srv6-te-policy+backup+hot-standby+enable)
        
        HSB is enabled for all SRv6 TE Policies.
   * Single-policy configuration
     
     1. Run [**srv6-te policy**](cmdqueryname=srv6-te+policy) *policy-name*
        
        The SRv6 TE Policy view is displayed.
     2. Run [**backup hot-standby**](cmdqueryname=backup+hot-standby) { **enable** | **disable** }
        
        HSB is configured for the SRv6 TE Policy.
   
   If an SRv6 TE Policy has both global and single-policy configurations, the single-policy configuration takes precedence.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.