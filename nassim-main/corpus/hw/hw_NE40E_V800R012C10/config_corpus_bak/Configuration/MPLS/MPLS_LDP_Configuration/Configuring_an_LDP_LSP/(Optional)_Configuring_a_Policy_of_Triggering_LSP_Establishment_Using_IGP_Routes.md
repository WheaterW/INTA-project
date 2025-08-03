(Optional) Configuring a Policy of Triggering LSP Establishment Using IGP Routes
================================================================================

A policy can be configured to allow LDP to use eligible static and IGP routes to trigger LSP establishment.

#### Context

A policy can be configured to allow LDP to use eligible static and IGP routes to trigger the establishment of public-network ingress and egress LSPs.![](../../../../public_sys-resources/note_3.0-en-us.png) 

A policy for triggering LSP establishment can be configured in either the MPLS or MPLS-LDP-IPv4 view. If such a policy is configured in both views, the configuration in the MPLS-LDP-IPv4 view takes effect.

The LSR must have route entries that exactly match the FECs for the LSPs to be established.




#### Procedure

* Configure a policy for triggering LSP establishment in the MPLS view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     The MPLS view is displayed.
  3. Run [**lsp-trigger**](cmdqueryname=lsp-trigger+all+host+ip-prefix+none) { **all** | **host** | **ip-prefix** *ip-prefix-name* | **none** }
     
     
     
     The policy of triggering LSP establishment using static and IGP routes is configured.
     
     
     
     + If the **all** parameter is specified, all IGP routes can trigger LDP to establish LSPs. However, public-network BGP routes or default routes cannot trigger LDP to establish LSPs.
     + If **host** is specified, only host IP routes with 32-bit addresses can trigger LDP to establish LSPs.
     + If the **ip-prefix** parameter is specified, only FECs matching a specified IP address prefix list can trigger LDP to establish LSPs.
     + If the **none** parameter is specified, LDP cannot be triggered to establish LSPs.![](../../../../public_sys-resources/note_3.0-en-us.png) 
       - By default, IP routes with 32-bit addresses are used to trigger LDP to establish LSPs. The default configuration is recommended. Running the [**lsp-trigger all**](cmdqueryname=lsp-trigger+all) command is not recommended, as this command enables LDP LSPs to be established for all static routes and IGP routes. As a result, a large number of LSPs are established, consuming excessive label resources and slowing down LSP convergence on the entire network. You are advised to run the [**lsp-trigger ip-prefix**](cmdqueryname=lsp-trigger+ip-prefix) command instead.
       - If the triggering policy is changed from **all** to **host**, LSPs that have been established using host routes are not reestablished.
  4. Run [**proxy-egress disable**](cmdqueryname=proxy-egress+disable)
     
     
     
     A policy for triggering proxy egress LSP establishment is configured.
     
     
     
     If a policy allows LDP to establish LSPs for static and IGP routes or for routes within a specified IP prefix list, the policy also allows LDP to establish proxy egress LSPs. However, these proxy egress LSPs may be useless and unnecessarily consume system resources. To prevent such an issue, run this command to disable the device from establishing proxy egress LSPs.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a policy for triggering LSP establishment in the MPLS-LDP-IPv4 view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     The MPLS view is displayed.
  3. Run [**proxy-egress disable**](cmdqueryname=proxy-egress+disable)
     
     
     
     A policy for triggering proxy egress LSP establishment is configured.
     
     
     
     If a policy allows LDP to establish LSPs for static and IGP routes or for routes within a specified IP prefix list, the policy also allows LDP to establish proxy egress LSPs. However, these proxy egress LSPs may be useless and unnecessarily consume system resources. To prevent such an issue, run this command to disable the device from establishing proxy egress LSPs.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  5. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
     
     
     
     The MPLS-LDP view is displayed.
  6. Run [**ipv4-family**](cmdqueryname=ipv4-family)
     
     
     
     The MPLS-LDP-IPv4 view is displayed.
  7. Run [**lsp-trigger**](cmdqueryname=lsp-trigger+all+host+ip-prefix+none) { **all** | **host** | **ip-prefix** *prefix-name* | **none** }
     
     
     
     A policy for triggering LSP establishment is configured.
     
     
     
     + If the **all** parameter is specified, all IGP routes can trigger LDP to establish LSPs. However, public-network BGP routes or default routes cannot trigger LDP to establish LSPs.
     + If the **ip-prefix** parameter is specified, only FECs matching a specified IP address prefix list can trigger LDP to establish LSPs.
     + If the **none** parameter is specified, LDP cannot be triggered to establish LSPs.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If the triggering policy is changed from **all** to **host**, LSPs that have been established using host routes are not reestablished.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.