(Optional) Configuring a Device to Check the Source Interface of a Static CR-LSP
================================================================================

A device uses the static CR-LSP's source interface check function to check whether the inbound interface of labeled packets is the same as that of a configured static CR-LSP. If the inbound interfaces match, the device forwards the packets. If the inbound interfaces do not match, the device discards the packets.

#### Context

A static CR-LSP is established using manually configured forwarding and resource information. Signaling protocols and path calculation are not used during the setup of CR-LSPs. Setting up a static CR-LSP consumes few resources because the two ends of the CR-LSP do not need to exchange MPLS control packets. However, the static CR-LSP cannot be adjusted dynamically in a changeable network topology. A static CR-LSP configuration error may cause protocol packets of different NEs and statuses to interfere one another, which adversely affects services. To address the preceding problem, a device can be enabled to check source interfaces of static CR-LSPs. With this function configured, the device can forward packets only when both labels and inbound interfaces are correct.


#### Procedure

* Perform the following steps on the P node of a static CR-LSP:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     The MPLS view is displayed.
  3. Run [**mpls te**](cmdqueryname=mpls+te)
     
     
     
     MPLS TE is enabled globally.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  5. Run [**static-cr-lsp transit**](cmdqueryname=static-cr-lsp+transit) *lsp-name* **incoming-interface** *interface-type* *interface-number* **in-label** *in-label* **outgoing-interface** *interface-type* *interface-number* **out-label** *out-label*
     
     
     
     An incoming label value, inbound interface name, outgoing label value, and outbound interface name are specified for a static CR-LSP.
  6. Enable the device to check the source interface of the static CR-LSP. To disable the function, run the [**static-cr-lsp rpf disable**](cmdqueryname=static-cr-lsp+rpf+disable) command. To enable this function again, run the [**undo static-cr-lsp rpf disable**](cmdqueryname=undo+static-cr-lsp+rpf+disable) command.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Perform the following steps on the egress of the static CR-LSP:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     The MPLS view is displayed.
  3. Run [**mpls te**](cmdqueryname=mpls+te)
     
     
     
     MPLS TE is enabled globally.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  5. Run [**static-cr-lsp egress**](cmdqueryname=static-cr-lsp+egress) *lsp-name* **incoming-interface** *interface-type* *interface-number* **in-label** *in-label*
     
     
     
     An incoming label and inbound interface are specified for the static CR-LSP.
  6. Enable the device to check the source interface of the static CR-LSP. To disable the function, run the [**static-cr-lsp rpf disable**](cmdqueryname=static-cr-lsp+rpf+disable) command. To enable this function again, run the [**undo static-cr-lsp rpf disable**](cmdqueryname=undo+static-cr-lsp+rpf+disable) command.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.