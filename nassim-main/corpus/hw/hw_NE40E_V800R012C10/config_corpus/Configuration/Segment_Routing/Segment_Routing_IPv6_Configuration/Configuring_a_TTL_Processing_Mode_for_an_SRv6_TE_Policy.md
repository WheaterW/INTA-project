Configuring a TTL Processing Mode for an SRv6 TE Policy
=======================================================

Configure an SRv6 TE Policy to process time to live (TTL) in pipe or uniform mode.

#### Context

In a scenario where a public IP route recurses to an SRv6 TE Policy, perform the following operations at both ends of the policy to configure a TTL processing mode for the policy.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6)
   
   
   
   SRv6 is enabled, and the SRv6 view is displayed.
3. Run [**ttl-mode**](cmdqueryname=ttl-mode) { **pipe** | **uniform** }
   
   
   
   A TTL processing mode is configured for the SRv6 TE Policy.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.