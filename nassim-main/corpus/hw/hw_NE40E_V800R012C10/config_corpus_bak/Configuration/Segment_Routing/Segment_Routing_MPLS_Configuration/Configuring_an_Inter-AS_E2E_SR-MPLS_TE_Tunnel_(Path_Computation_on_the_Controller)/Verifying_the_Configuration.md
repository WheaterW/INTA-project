Verifying the Configuration
===========================

After configuring an inter-AS E2E SR-MPLS TE tunnel, verify information about the SR-MPLS TE tunnel and its status statistics.

#### Prerequisites

The inter-AS E2E SR-MPLS TE tunnel has been configured.


#### Procedure

1. Run the [**display mpls te tunnel**](cmdqueryname=display+mpls+te+tunnel) [ **destination** *ip-address* ] [ **lsp-id** *lsr-id* *session-id* *local-lsp-id* | **lsr-role** { **all** | **egress** | **ingress** | **remote** | **transit** } ] [ **name** *tunnel-name* ] [ { **incoming-interface** | **interface** | **outgoing-interface** } *interface-type* *interface-number* ] [ **verbose** ] command to check tunnel information.
2. Run the [**display mpls te tunnel-interface**](cmdqueryname=display+mpls+te+tunnel-interface) [ **tunnel** *tunnel-number* ] command to check information about a tunnel interface on the ingress.
3. Run the [**display mpls te binding-sid**](cmdqueryname=display+mpls+te+binding-sid) [ **label** *label-value* ] command to check the mapping between binding SIDs and tunnels.