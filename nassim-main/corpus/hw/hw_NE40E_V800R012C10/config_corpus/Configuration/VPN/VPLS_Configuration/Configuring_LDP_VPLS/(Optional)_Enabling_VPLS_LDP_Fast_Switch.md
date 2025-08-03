(Optional) Enabling VPLS LDP Fast Switch
========================================

In LDP FRR scenarios or scenarios where two LDP LSPs work in load-balancing mode, you can enable VPLS LDP fast switch to accelerate unicast convergence.

#### Context

After VPLS LDP fast switch is enabled, unicast convergence will accelerate when one LDP LSP fails and traffic switches to the other LDP LSP.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls vpls-ldp fast-switch enable**](cmdqueryname=mpls+vpls-ldp+fast-switch+enable)
   
   
   
   VPLS LDP fast switch is enabled.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.