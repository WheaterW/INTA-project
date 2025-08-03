Verifying the Configuration
===========================

After configuring LDP Auto FRR, you can view information about the LDP Auto FRR LSP.

#### Prerequisites

LDP Auto FRR has been configured.
#### Procedure

* Run the [**display mpls lsp**](cmdqueryname=display+mpls+lsp) command to check information about LSPs generated after LDP Auto FRR is enabled.
* Run the [**display mpls ldp event session-down verbose**](cmdqueryname=display+mpls+ldp+event+session-down+verbose) command to check LDP session down causes. The cause value **IGP delete the RLFA IID** indicates that an LDP session is down because the RLFA route is deleted.
* Run the [**display mpls ldp event adjacency-down verbose**](cmdqueryname=display+mpls+ldp+event+adjacency-down+verbose) command to check adjacency down causes. The cause value **IGP delete the RLFA IID** indicates that the adjacency is down because the RLFA route is deleted.