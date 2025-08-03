Checking Connectivity of a TE Tunnel
====================================

Check the connectivity of a TE tunnel from the ingress to the egress.

#### Context

After configuring an MPLS TE tunnel, you can run the [**ping lsp**](cmdqueryname=ping+lsp) command on the tunnel ingress to check whether the egress can be pinged. If the ping fails, run the [**tracert lsp**](cmdqueryname=tracert+lsp) command to locate the fault.


#### Procedure

* Run the [**ping
  lsp**](cmdqueryname=ping+lsp) [ **-a** *source-ip* | **-c** *count* | **-exp** *exp-value* | **-h** *ttl-value* | **-m** *interval* | **-r** *reply-mode* | **-s** *packet-size* | **-t** *time-out* | **-v** ] \* **te** **tunnel** *tunnel-number* [ **hot-standby** ] [ **compatible-mode** ] command to check the connectivity of the TE tunnel from the ingress to the egress.
  
  
  
  If **hot-standby** is configured, a backup CR-LSP is checked.
* Run the [**tracert lsp**](cmdqueryname=tracert+lsp) [ **-a** *source-ip* | **-exp** *exp-value* | **-h** *ttl-value* | **-r** *reply-mode* | **-t** *time-out* | **-s** *size* ] \* **te** **tunnel** *tunnel-number* [ **hot-standby** ] [ **compatible-mode** ] [ **detail** ] command to check the gateways that the data packets pass through from the ingress to the egress of the TE tunnel.
  
  
  
  If **hot-standby** is configured, a backup CR-LSP is checked.