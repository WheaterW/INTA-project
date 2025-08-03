Configuring the Ingress of the Static CR-LSP
============================================

This section describes how to configure the ingress of a static CR-LSP. Before you establish a static CR-LSP, specify the ingress of the CR-LSP.

#### Context

Perform the following steps on the ingress of a static CR-LSP:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**static-cr-lsp ingress**](cmdqueryname=static-cr-lsp+ingress) { **tunnel-interface** **tunnel** *interface-number* | *tunnel-name* } **destination** *destination-address* { **nexthop** *next-hop-address* | **outgoing-interface** *interface-type* *interface-number* } \* **out-label** *out-label* [ **bandwidth** [ **ct0** ] *bandwidth* ]
   
   
   
   The LSR is configured as the ingress of the specified static CR-LSP.
   
   To modify the **destination** *destination-address*, **nexthop** *next-hop-address*, **outgoing-interface** *interface-type interface-number*, or **out-label** *out-label*, run the [**static-cr-lsp ingress**](cmdqueryname=static-cr-lsp+ingress) command to set a new value. There is no need to run the [**undo static-cr-lsp ingress**](cmdqueryname=undo+static-cr-lsp+ingress) command before changing a configured value.
   
   **tunnel** *interface-number* specifies the MPLS TE tunnel interface that uses this static CR-LSP. By default, the Bandwidth Constraints value is **ct0**, and the value of bandwidth is 0. The bandwidth used by the tunnel cannot be higher than the maximum reservable bandwidth of the link.
   
   The next hop or outgoing interface is determined by the route from the ingress to the egress. For the difference between the next hop and outbound interface, see "Static Route Configuration" in *Configuration Guide - IP Routing*.
   
   If an Ethernet interface is used as an outbound interface, the **nexthop** *next-hop-address* parameter must be configured.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.