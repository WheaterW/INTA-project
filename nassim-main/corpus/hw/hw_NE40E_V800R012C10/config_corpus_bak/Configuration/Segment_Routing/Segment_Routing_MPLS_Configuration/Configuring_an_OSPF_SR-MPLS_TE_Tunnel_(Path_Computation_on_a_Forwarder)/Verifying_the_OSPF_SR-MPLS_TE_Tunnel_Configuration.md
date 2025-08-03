Verifying the OSPF SR-MPLS TE Tunnel Configuration
==================================================

After configuring an automatic SR-MPLS TE tunnel, verify information about the SR-MPLS TE tunnel and its status statistics.

#### Prerequisites

The SR-MPLS TE tunnel functions have been configured.


#### Procedure

1. Run the [**display ospf**](cmdqueryname=displayospf+segment-routing+routing) [ *process-id* ] **segment-routing** **routing** [ *ip-address* [ *mask* | *mask-length* ] ] command to check OSPF SR-MPLS routing table information.
2. Run the [**display mpls te tunnel**](cmdqueryname=display+mpls+te+tunnel) [ **destination** *ip-address* ] [ **lsp-id** *lsr-id* *session-id* *local-lsp-id* | **lsr-role** { **all** | **egress** | **ingress** | **remote** | **transit** } ] [ **name** *tunnel-name* ] [ { **incoming-interface** | **interface** | **outgoing-interface** } *interface-type* *interface-number* ] [ **verbose** ] command to check tunnel information.
3. Run the [**display mpls te tunnel statistics**](cmdqueryname=display+mpls+te+tunnel+statistics) or [**display mpls sr-te-lsp**](cmdqueryname=display+mpls+sr-te-lsp) command to check LSP statistics.
4. Run the [**display mpls te tunnel-interface**](cmdqueryname=display+mpls+te+tunnel-interface) [ **tunnel** *tunnel-number* ] command to check information about a tunnel interface on the ingress.