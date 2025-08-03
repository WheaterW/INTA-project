Configuring Split Horizon
=========================

You can configure split horizon to prevent routing loops.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ripng split-horizon**](cmdqueryname=ripng+split-horizon)
   
   
   
   Split horizon is enabled.
   
   If both split
   horizon and poison reverse are configured, only poison reverse takes
   effect.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is
   submitted.