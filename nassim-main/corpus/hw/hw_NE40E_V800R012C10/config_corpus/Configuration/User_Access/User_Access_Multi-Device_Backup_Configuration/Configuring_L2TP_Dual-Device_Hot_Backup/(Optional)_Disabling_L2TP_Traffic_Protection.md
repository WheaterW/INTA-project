(Optional) Disabling L2TP Traffic Protection
============================================

In some L2TP hot backup scenarios, L2TP traffic protection can be disabled to prevent traffic switching from affecting customer services.

#### Context

On a high-bandwidth network, traffic switching does not affect customer services. In this situation, you do not need to disable L2TP traffic protection.

However, on a low-bandwidth network where L2TP hot backup is configured, if a fault occurs on the access side, traffic is switched to a backup device through an L2TP protection tunnel. The traffic switching may worsen network congestion, affecting customer services, such as fixed-line services. To prevent traffic switching, L2TP traffic
protection needs to be disabled to prevent establishment of any L2TP protection tunnel.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**remote-backup-service**](cmdqueryname=remote-backup-service) *service-name*
   
   
   
   The RBS view is displayed.
3. Run [**l2tp protect-tunnel disable**](cmdqueryname=l2tp+protect-tunnel+disable)
   
   
   
   L2TP traffic protection is disabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.