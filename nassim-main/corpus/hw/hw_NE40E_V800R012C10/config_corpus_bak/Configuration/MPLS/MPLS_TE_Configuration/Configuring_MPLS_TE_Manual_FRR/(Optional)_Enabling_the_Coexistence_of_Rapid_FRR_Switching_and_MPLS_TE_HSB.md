(Optional) Enabling the Coexistence of Rapid FRR Switching and MPLS TE HSB
==========================================================================

When FRR and HSB are enabled for MPLS TE tunnels, enabling the coexistence of MPLS TE HSB and rapid FRR switching improves switching performance.

#### Context

To enable the coexistence of FRR switching and MPLS TE HSB, TE FRR must be deployed on the entire network. HSB must be deployed on the ingress, BFD for TE LSP must be enabled, and the delayed down function must be enabled on the outbound interface of the P. Otherwise, rapid switching cannot be performed in case of the dual points of failure.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls te multi-protect fast-switch enable**](cmdqueryname=mpls+te+multi-protect+fast-switch+enable)
   
   Coexistence of rapid FRR switching and MPLS TE HSB is enabled.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.