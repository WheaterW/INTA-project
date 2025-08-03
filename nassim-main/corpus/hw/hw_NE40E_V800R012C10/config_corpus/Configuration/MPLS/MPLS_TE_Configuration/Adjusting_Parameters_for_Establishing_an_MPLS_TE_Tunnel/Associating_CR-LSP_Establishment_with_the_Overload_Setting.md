Associating CR-LSP Establishment with the Overload Setting
==========================================================

CR-LSP establishment can be associated with the overload setting. This association ensures that CR-LSPs are established over paths excluding overloaded nodes.

#### Context

A node becomes overloaded in the following situations:

* When the node is transmitting a large number of services and its system resources are exhausted, the node marks itself overloaded.
* When the node is transmitting a large number of services and its CPU is overburdened, an administrator can run the [**set-overload**](cmdqueryname=set-overload) command to mark the node overloaded.

If there are overloaded nodes on an MPLS TE network, associate CR-LSP establishment with the IS-IS overload setting to ensure that CR-LSPs are established over paths excluding overloaded nodes. This configuration prevents overloaded nodes from being further burdened and improves CR-LSP reliability.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
3. Run [**mpls te path-selection overload**](cmdqueryname=mpls+te+path-selection+overload)
   
   
   
   CR-LSP establishment is associated with the IS-IS overload setting. This association allows CSPF to calculate paths excluding overloaded IS-IS nodes.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Before the association is configured, the [**mpls te cspf**](cmdqueryname=mpls+te+cspf) command must be run to enable CSPF and the [**mpls te record-route**](cmdqueryname=mpls+te+record-route) command must be run to enable the route and label record.
   
   Traffic travels through an existing CR-LSP before a new CR-LSP is established. After the new CR-LSP is established, traffic switches to the new CR-LSP and the original CR-LSP is deleted. This traffic switchover is performed based on the make-before-break mechanism. Traffic is not dropped during the switchover.
   
   
   The [**mpls te path-selection overload**](cmdqueryname=mpls+te+path-selection+overload) command has the following influences on the CR-LSP establishment:
   * CSPF recalculates paths excluding overloaded nodes for established CR-LSPs.
   * CSPF calculates paths excluding overloaded nodes for new CR-LSPs.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This command does not take effect on bypass tunnels or P2MP TE tunnels.
   
   If the ingress or egress is marked overloaded, the [**mpls te path-selection overload**](cmdqueryname=mpls+te+path-selection+overload) command does not take effect. This means that the established CR-LSPs associated with the ingress or egress will not be reestablished and new CR-LSPs associated with the ingress or egress will also not be established.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.