(Optional) Configuring a Policy of Triggering LSP Establishment Using Labeled BGP Routes of the Public Network
==============================================================================================================

A policy can be configured to allow LDP to use eligible labeled BGP routes of the public network to trigger LSP establishment.

#### Context

A policy can be configured to enable LDP to use eligible routes to trigger the establishment of public-network ingress and egress LSPs.

Both the [**lsp-trigger bgp-label-route**](cmdqueryname=lsp-trigger+bgp-label-route) and [**lsp-trigger**](cmdqueryname=lsp-trigger) commands can be used to configure policies to trigger the establishment of LDP LSPs. The former applies only to labeled BGP routes of the public network, and the latter applies to static and IGP routes.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

During LDP GR, changing the policy for triggering LSP establishment does not take effect.



#### Procedure

1. Configure a policy for triggering LSP establishment in the MPLS view.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**mpls**](cmdqueryname=mpls)
      
      
      
      The MPLS view is displayed.
   3. Run [**lsp-trigger bgp-label-route**](cmdqueryname=lsp-trigger+bgp-label-route+ip-prefix+not-only-host) [ **ip-prefix** *ip-prefix-name* ] [ **not-only-host** ]
      
      
      
      A policy of triggering LSP establishment using labeled BGP routes of the public network is configured.
      
      
      
      * If the **ip-prefix** parameter is specified, LDP can only use labeled BGP routes of the public network that match the IP prefix list to trigger LSP establishment.
      * If **not-only-host** is not specified, LDP allocates labels only to labeled public network BGP routes with 32-bit masks for LSP establishment. To enable LDP to allocate labels to all labeled public network BGP routes (including those with non-32-bit masks) for LSP establishment, specify the **not-only-host** parameter.
   4. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.