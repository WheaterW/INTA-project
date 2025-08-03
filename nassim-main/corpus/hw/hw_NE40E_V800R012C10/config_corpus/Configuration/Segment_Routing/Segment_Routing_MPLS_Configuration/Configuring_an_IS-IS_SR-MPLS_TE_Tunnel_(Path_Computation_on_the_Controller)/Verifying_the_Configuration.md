Verifying the Configuration
===========================

After configuring an automatic SR-MPLS TE tunnel, verify information about the SR-MPLS TE tunnel and its status statistics.

#### Prerequisites

The SR-MPLS TE tunnel functions have been configured.


#### Procedure

* Run the following commands to check the IS-IS TE status:
  + [**display isis traffic-eng advertisements**](cmdqueryname=display+isis+traffic-eng+advertisements) [ *lspId* | **local** ] [ **level-1** | **level-2** | **level-1-2** ] [ *process-id* | **vpn-instance** *vpn-instance-name* ]
  + [**display isis traffic-eng statistics**](cmdqueryname=display+isis+traffic-eng+statistics) [ *process-id* | **vpn-instance** *vpn-instance-name* ]
* Run the [**display mpls te tunnel**](cmdqueryname=display+mpls+te+tunnel) [ **destination** *ip-address* ] [ **lsp-id** *lsr-id* *session-id* *local-lsp-id* | **lsr-role** { **all** | **egress** | **ingress** | **remote** | **transit** } ] [ **name** *tunnel-name* ] [ { **incoming-interface** | **interface** | **outgoing-interface** } *interface-type* *interface-number* ] [ **verbose** ] command to check tunnel information.
* Run the [**display mpls te tunnel statistics**](cmdqueryname=display+mpls+te+tunnel+statistics) or [**display mpls sr-te-lsp**](cmdqueryname=display+mpls+sr-te-lsp) command to check LSP statistics.
* Run the [**display mpls te tunnel-interface**](cmdqueryname=display+mpls+te+tunnel-interface) [ **tunnel** *tunnel-number* ] command to check information about a tunnel interface on the ingress.
* (Optional) If the label stack depth exceeds the upper limit supported by a forwarder, the controller needs to divide a label stack into multiple stacks for an entire path. After the controller assigns a stick label to a stick node, run the [**display mpls te stitch-label-stack**](cmdqueryname=display+mpls+te+stitch-label-stack) command to check information about the stick label stack mapped to the stick label.