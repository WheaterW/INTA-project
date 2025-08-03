(Optional) Setting the FRR Switching Delay Time
===============================================

After the FRR switching delay time is set, FRR entry delivery is delayed, preventing traffic from being switched twice when both HSB and FRR are enabled.

#### Context

The FRR switching delay time can be set to delay FRR entry delivery. This allows traffic to be switched to the HSB path, not the FRR path, preventing traffic from being switched twice.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
3. Run [**mpls te**](cmdqueryname=mpls+te)
   
   
   
   MPLS TE is globally enabled.
4. Run [**mpls te frr-switch-delay**](cmdqueryname=mpls+te+frr-switch-delay) *value*
   
   
   
   The FRR switching delay time (in ms) is set.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.