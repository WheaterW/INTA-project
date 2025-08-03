Configuring SR-MPLS TE Policy Traffic Statistics Collection
===========================================================

This section describes how to configure SR-MPLS TE Policy traffic statistics collection.

#### Context

Traffic statistics collection for an SR-MPLS TE Policy helps you collect statistics about traffic forwarded through the SR-MPLS TE Policy.

This function supports both global configuration and individual configuration. If global configuration and individual configuration both exist, the individual configuration takes effect.

Perform the following steps on the Router:


#### Procedure

* Global configuration
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**segment-routing**](cmdqueryname=segment-routing)
     
     
     
     The Segment Routing view is displayed.
  3. Run [**sr-te-policy traffic-statistics enable**](cmdqueryname=sr-te-policy+traffic-statistics+enable)
     
     
     
     Traffic statistics collection is enabled for all SR-MPLS TE Policies.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Individual configuration
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**segment-routing**](cmdqueryname=segment-routing)
     
     
     
     The Segment Routing view is displayed.
  3. Run [**sr-te policy**](cmdqueryname=sr-te+policy) *policy-name*
     
     
     
     The SR-MPLS TE Policy view is displayed.
  4. Run [**traffic-statistics**](cmdqueryname=traffic-statistics) { **enable** | **disable** }
     
     
     
     Traffic statistics collection is configured for the specified SR-MPLS TE Policy.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Verifying the Configuration

After configuring SR-MPLS TE Policy traffic statistics collection, run the [**display sr-te policy traffic-statistics**](cmdqueryname=display+sr-te+policy+traffic-statistics) [ [**endpoint**](cmdqueryname=endpoint) *ipv4-address* **color** *color-value* | **policy-name** *name-value* | **binding-sid** *binding-sid* ] command to check collected SR-MPLS TE Policy traffic statistics.


#### Follow-up Procedure

To clear existing SR Policy traffic statistics, run the [**reset sr-te policy traffic-statistics**](cmdqueryname=reset+sr-te+policy+traffic-statistics) [ [**endpoint**](cmdqueryname=endpoint) *ipv4-address* **color** *color-value* | **policy-name** *name-value* | **binding-sid** *binding-sid* ] command.