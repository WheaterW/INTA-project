Establishing an LDP LSP for the Labeled BGP Routes of the Public Network
========================================================================

By enabling LDP on ASBRs to allocate labels for BGP routes, you can establish LDP LSPs for labeled BGP routes of the public network that are filtered in the IP prefix list.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
3. Run [**lsp-trigger bgp-label-route**](cmdqueryname=lsp-trigger+bgp-label-route) [ **ip-prefix** *ip-prefix-name* ] [ **not-only-host** ]
   
   
   
   An LDP LSP is established for the labeled BGP routes of the public network that are filtered by the IP prefix list.
   
   
   
   If the **not-only-host** parameter is not configured, LDP assigns labels only to public network labeled BGP routes with 32-bit masks and establishes LSPs for them. To enable LDP to assign labels to all public network labeled BGP routes, configure the **not-only-host** parameter.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.