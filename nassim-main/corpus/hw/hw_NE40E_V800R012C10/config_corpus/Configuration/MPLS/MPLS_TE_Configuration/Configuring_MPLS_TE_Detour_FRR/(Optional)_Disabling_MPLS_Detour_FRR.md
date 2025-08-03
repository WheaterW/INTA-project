(Optional) Disabling MPLS Detour FRR
====================================

If MPLS detour FRR is disabled on a transit node or egress node, the ingress node excludes the node when calculating a detour LSP and does not occupy forwarding resources of the node.

#### Context

After MPLS detour FRR is enabled on a tunnel, the ingress node calculates a detour LSP to protect the tunnel if the tunnel fails. Some transit nodes or the egress node may not support MPLS detour FRR, but they can still function as protection nodes along a detour LSP.

To disable MPLS detour FRR, run the [**mpls rsvp-te detour disable**](cmdqueryname=mpls+rsvp-te+detour+disable) command in the MPLS view. After the [**mpls rsvp-te detour disable**](cmdqueryname=mpls+rsvp-te+detour+disable) command is run, detour LSPs that are not in the FRR-in-use state are deleted.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
3. Run [**mpls rsvp-te detour disable**](cmdqueryname=mpls+rsvp-te+detour+disable)
   
   
   
   MPLS detour FRR is disabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.