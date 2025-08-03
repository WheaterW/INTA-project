(Optional) Configuring a Policy for Triggering LSP Establishment
================================================================

A policy can be configured to allow LDP to establish LSPs for eligible routes.

#### Context

A policy can be configured to enable LDP to use eligible routes to trigger the establishment of public-network ingress and egress LSPs.![](../../../../public_sys-resources/note_3.0-en-us.png) 

Each LSR must have route entries that exactly match the FECs for the LSPs to be established.




#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
3. Run [**lsp-trigger**](cmdqueryname=lsp-trigger) { **all** | **host** | **ip-prefix** *prefix-name* | **none** }
   
   
   
   A policy for triggering LSP establishment is configured.
   
   
   
   * If the triggering policy is **all**, all static routes and IGP routes are used to trigger LDP to establish LSPs. The device does not use public network BGP routes to trigger LDP LSP establishment.
   * If **host** is specified, only host IP routes with 32-bit addresses can trigger LDP to establish LSPs.
   * If the **ip-prefix** parameter is specified, only FECs matching a specified IP address prefix list can trigger LDP to establish LSPs.
   * If the **none** parameter is specified, LDP cannot be triggered to establish LSPs.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * By default, IP routes with 32-bit addresses are used to trigger LDP to establish LSPs. The default configuration is recommended. Running the [**lsp-trigger**](cmdqueryname=lsp-trigger) **all** command is not recommended, as this command enables LDP LSPs to be established for all static routes and IGP routes. As a result, a large number of LSPs are established, consuming excessive label resources and slowing down LSP convergence on the entire network. You are advised to run the [**lsp-trigger ip-prefix**](cmdqueryname=lsp-trigger+ip-prefix) **ip-prefix** *ip-prefix-name* command instead.
   * If the triggering policy is changed from **all** to **host**, LSPs that have been established using host routes are not reestablished.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.