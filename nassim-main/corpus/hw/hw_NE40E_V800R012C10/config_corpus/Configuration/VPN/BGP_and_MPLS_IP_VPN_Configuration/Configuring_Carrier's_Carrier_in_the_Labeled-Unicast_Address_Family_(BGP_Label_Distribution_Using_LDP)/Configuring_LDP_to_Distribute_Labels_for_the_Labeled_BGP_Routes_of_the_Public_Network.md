Configuring LDP to Distribute Labels for the Labeled BGP Routes of the Public Network
=====================================================================================

By allocating labels for labeled BGP routes, you can establish LDP LSPs for labeled BGP routes in the Level 2 carrier' network.

#### Context

To configure LDP to distribute labels for the BGP-labeled routes of the public network, Perform the following steps on the Level 1 carrier CE.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
3. Run [**lsp-trigger bgp-label-route**](cmdqueryname=lsp-trigger+bgp-label-route) [ **ip-prefix** *ip-prefix-name* ] [ **not-only-host** ]
   
   
   
   LDP is configured to allocate labels to labeled BGP routes of the public network.
   
   
   
   If **not-only-host** is not specified, LDP allocates labels to only the BGP routes with 32-bit masks and establishes LSPs. If you want to assign labels to all the labeled BGP routes with non-32-bit masks and establish LSPs, specify the **not-only-host** parameter.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.