(Optional) Configuring Graceful Deletion for LDP Sessions
=========================================================

LDP graceful deletion can be configured to speed up traffic switching using LDP-IGP synchronization, improving network reliability.

#### Context

LDP graceful deletion can be configured in the LDP-IGP synchronization or LDP FRR scenario to speed up traffic switching. It helps implement uninterrupted traffic transmission during traffic switching, which improves reliability of the entire network.

If the physical and protocol status of the primary link is normal but the LDP session on the primary link is down, LDP-IGP synchronization enables LDP to inform the IGP of the primary link fault, and the IGP advertises the maximum cost of the primary link. After that, LDP immediately instructs the upstream device to withdraw labels and assigns labels to the upstream device because a new LSP is established on the backup link, which prolongs LSP convergence. As a result, packet loss occurs.

After the LDP session on the faulty link goes down, LDP does not immediately instruct the upstream device to withdraw labels; instead, it keeps the labels and LSP and allows traffic to be transmitted on the primary link until LSP convergence is complete on the backup link. This ensures uninterrupted traffic transmission and speeds up LDP-IGP synchronization.

Perform the following configuration on the LSR configured with LDP-IGP synchronization.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
   
   
   
   The MPLS-LDP view is displayed.
3. Run [**graceful-delete**](cmdqueryname=graceful-delete)
   
   
   
   LDP graceful deletion is enabled.
4. (Optional) Run [**graceful-delete timer**](cmdqueryname=graceful-delete+timer) *timer* The graceful deletion timer value is set.
   
   
   
   After the LDP session goes down, LDP does not instruct the upstream device to withdraw labels until the graceful delete timer expires.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the value of the graceful delete timer is too large, the invalid LSP will be kept for a long time, consuming system resources.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.