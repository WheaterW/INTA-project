Configuring Poison Reverse
==========================

You can configure poison reverse to prevent routing loops.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
   
   If both split horizon and
   poison reverse are configured, only poison reverse takes effect.
3. Run [**ripng poison-reverse**](cmdqueryname=ripng+poison-reverse)
   
   
   
   Poison reverse is enabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is
   submitted.