Verifying the Configuration
===========================

After configuring LDP LSPs, you can view information about LDP configurations, LDP LSPs, and LSPs.

#### Prerequisites

All LDP LSP configurations have been completed.


#### Procedure

* Run the [**display mpls ldp**](cmdqueryname=display+mpls+ldp+all+all+verbose) [ **all** | **all** **verbose** ] command to check LDP information.
* Run the [**display mpls ldp lsp**](cmdqueryname=display+mpls+ldp+lsp+all) [ *destination-address* *mask-length* | **all** ] command to check information about LDP LSPs.
* Run the [**display mpls ldp lsp inbound-policy**](cmdqueryname=display+mpls+ldp+lsp+inbound-policy) command to check information about the liberal LSPs that have passed an inbound policy.
* Run the [**display mpls lsp**](cmdqueryname=display+mpls+lsp+verbose) [ **verbose** ] command to check LSP information.
* Run the [**display mpls ldp lsp fault-analysis**](cmdqueryname=display+mpls+ldp+lsp+fault-analysis) *ip-address* *mask* command to check the cause for an LDP LSP establishment failure.