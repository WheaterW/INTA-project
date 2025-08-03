(Optional) Setting Leaf Switching and Deletion Delays
=====================================================

To prevent two copies of traffic on a P2MP TE tunnel's egress, a leaf CR-LSP switchover hold-off time and a deletion hold-off time can be set for MBB.

#### Context

Before the primary sub-LSP is deleted, both the primary sub-LSP and Modified sub-LSP carry traffic. If the egress cannot receive traffic only from one sub-LSP, two copies of traffic exist. To prevent two copies of traffic, perform the following steps to reset the leaf CR-LSP switchover hold-off time and deletion hold-off time.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   MPLS is enabled globally and the MPLS view is displayed.
3. Run [**mpls te**](cmdqueryname=mpls+te)
   
   
   
   MPLS TE is enabled globally.
   
   
   
   A leaf CR-LSP switchover hold-off time and deletion hold-off time can be set only after MPLS TE is enabled globally.
4. Run [**mpls te p2mp-te leaf**](cmdqueryname=mpls+te+p2mp-te+leaf) **switch-delay***switch-time* **delete-delay** *delete-time*
   
   
   
   The leaf MBB switchover delay and deletion delay are set.
   
   
   
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) After the [**mpls te p2mp-te leaf**](cmdqueryname=mpls+te+p2mp-te+leaf) **switch-delay** *switch-time* **delete-delay** *delete-time* command is run, traffic may be interrupted in the following scenarios:
   * The modified sub-LSP has been ready on the ingress and the primary sub-LSP has been deleted, but the modified sub-LSP is not ready on the egress. If this occurs, when the ingress switches traffic to the modified sub-LSP, traffic is temporarily interrupted.
   * The primary sub-LSP has been deleted, but the modified sub-LSP failure message cannot be immediately sent to the ingress. If this occurs, traffic is temporarily interrupted.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.