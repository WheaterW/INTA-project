Configuring Split Horizon
=========================

You can configure split horizon to prevent routing loops.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run **interface** *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**rip split-horizon**](cmdqueryname=rip+split-horizon)
   
   
   
   Split horizon is enabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

If both split horizon and poison reverse are configured, only poison reverse takes effect.