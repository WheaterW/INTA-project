Configuring LDP to Distribute Labels for the Labeled Public Network BGP Routes
==============================================================================

Allocating labels to labeled BGP routes enables the establishment of LDP LSPs for these routes on the Level 2 carrier network.

#### Context

To configure LDP to distribute labels for labeled public network BGP routes,

perform the following steps on Level 1 carrier CEs.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
3. Run [**lsp-trigger bgp-label-route**](cmdqueryname=lsp-trigger+bgp-label-route) [ **ip-prefix** *ip-prefix-name* ] [ **not-only-host** ]
   
   
   
   LDP is configured to allocate labels to labeled public network BGP routes.
   
   
   
   If **not-only-host** is not specified, LDP allocates labels to only the labeled public network BGP routes with 32-bit masks and establishes LSPs for these routes. If you want to allocate labels to all the labeled public network BGP routes (including those with non-32-bit masks) and establish LSPs for these routes, specify the **not-only-host** keyword.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.