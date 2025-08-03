Globally Enabling the SR Capability
===================================

Globally enabling the SR capability on forwarders is a prerequisite for configuring an SR-MPLS TE tunnel.

#### Context

SR must be enabled globally before the SR function becomes available.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**segment-routing**](cmdqueryname=segment-routing)
   
   
   
   SR is enabled globally.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.