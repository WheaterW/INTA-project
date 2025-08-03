Verifying the Automatic RSVP-TE Tunnel Configuration
====================================================

After configuring an automatic RSVP-TE tunnel, you can check information about the RSVP-TE tunnel and its status statistics.

#### Prerequisites

The automatic RSVP-TE tunnel functions have been configured.


#### Procedure

* Run the following commands to check the IS-IS-related label allocation information:
  + [**display isis traffic-eng advertisements**](cmdqueryname=display+isis+traffic-eng+advertisements) [ { **level-1** | **level-2** | **level-1-2** } | { *lsp-id* | **local** } ] \* [ *process-id* | [ **vpn-instance** *vpn-instance-name* ] ]
  + [**display isis traffic-eng statistics**](cmdqueryname=display+isis+traffic-eng+statistics) [ *process-id* | [ **vpn-instance** *vpn-instance-name* ] ]
* Run the [**display mpls te tunnel**](cmdqueryname=display+mpls+te+tunnel) [ **destination** *ip-address* ] [ **lsp-id** *lsr-id* *session-id* *local-lsp-id* | **lsr-role** { **all** | **egress** | **ingress** | **remote** | **transit** } ] [ **name** *tunnel-name* ] [ { **incoming-interface** | **interface** | **outgoing-interface** } *interface-type* *interface-number* ] [ **verbose** ] command to check tunnel information.
* Run the [**display mpls te tunnel statistics**](cmdqueryname=display+mpls+te+tunnel+statistics) command to view TE tunnel statistics.
* Run the [**display mpls te tunnel-interface**](cmdqueryname=display+mpls+te+tunnel-interface) [ **tunnel** *tunnel-number* ] command to check information about a tunnel interface on the ingress.