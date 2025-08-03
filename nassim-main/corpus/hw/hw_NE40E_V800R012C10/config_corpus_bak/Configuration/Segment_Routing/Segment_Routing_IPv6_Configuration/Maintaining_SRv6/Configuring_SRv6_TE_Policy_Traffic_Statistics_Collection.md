Configuring SRv6 TE Policy Traffic Statistics Collection
========================================================

This section describes how to configure SRv6 TE Policy traffic statistics collection.

#### Context

SRv6 TE Policy traffic statistics collection enables you to collect statistics about the traffic forwarded through a specified or all SRv6 TE Policies.

This function supports both global configuration and single-policy configuration. If global configuration and single-policy configuration both exist, the single-policy configuration takes effect.


#### Procedure

1. Global configuration
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6)
      
      
      
      The SRv6 view is displayed.
   3. Run [**srv6-te-policy traffic-statistics enable**](cmdqueryname=srv6-te-policy+traffic-statistics+enable)
      
      
      
      Traffic statistics collection is enabled for all SRv6 TE Policies.
   4. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
2. Single-policy configuration
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6)
      
      
      
      The SRv6 view is displayed.
   3. Run [**srv6-te policy**](cmdqueryname=srv6-te+policy) *name-value*
      
      
      
      The SRv6 TE Policy view is displayed.
   4. Run [**traffic-statistics**](cmdqueryname=traffic-statistics) { **enable** | **disable** }
      
      
      
      Traffic statistics collection is configured for the specified SRv6 TE Policy.
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.

#### Verifying the Configuration

After configuring SRv6 TE Policy traffic statistics collection, run the [**display srv6-te policy traffic-statistics**](cmdqueryname=display+srv6-te+policy+traffic-statistics) [ [**endpoint**](cmdqueryname=endpoint) *ipv6-address* **color** *color-value* | **policy-name** *name-value* | **binding-sid** *binding-sid* ] command to check collected SRv6 TE Policy traffic statistics.


#### Follow-up Procedure

To clear existing SRv6 TE Policy traffic statistics, run the [**reset srv6-te policy traffic-statistics**](cmdqueryname=reset+srv6-te+policy+traffic-statistics) [ [**endpoint**](cmdqueryname=endpoint) *ipv6-address* **color** *color-value* | **policy-name** *name-value* | **binding-sid** *binding-sid* ] command.