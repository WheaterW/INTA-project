(Optional) Configuring Graceful Deletion for LDP Sessions
=========================================================

LDP graceful deletion can be configured to speed up LDP FRR traffic switching.

#### Context

LDP graceful deletion can be configured in the LDP-IGP synchronization or LDP FRR scenario to speed up traffic switching. It helps implement uninterrupted traffic transmission during traffic switching, which improves reliability of the entire network.

If both the primary link and the LDP session on that link also go down, LDP immediately instructs the upstream device to withdraw labels and triggers LDP Auto FRR. LSP convergence on the backup link requires LDP to distribute labels to the upstream device again, which prolongs convergence and FRR traffic switching. As a result, packet loss occurs.

If LDP graceful deletion is configured and the LDP session goes down, LDP delays deleting the LDP session and keeps the relevant labels and LSP. The LSP on the backup link does not require LDP to distribute labels to the upstream device again, which shortens FRR traffic switching and reduces packet loss.

Perform the following configuration on the LDP FRR-enabled LSR.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
   
   
   
   The MPLS-LDP view is displayed.
3. [**graceful-delete**](cmdqueryname=graceful-delete)
   
   
   
   LDP graceful deletion is enabled.
4. (Optional) Run [**graceful-delete timer**](cmdqueryname=graceful-delete+timer) *timer*
   
   
   
   The graceful deletion timer value is set.
   
   
   
   After the LDP session goes down, forwarding entries on the LSR remain before the graceful deletion timer expires.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the value of the graceful delete timer is too large, the invalid LSP will be kept for a long time, consuming system resources.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.