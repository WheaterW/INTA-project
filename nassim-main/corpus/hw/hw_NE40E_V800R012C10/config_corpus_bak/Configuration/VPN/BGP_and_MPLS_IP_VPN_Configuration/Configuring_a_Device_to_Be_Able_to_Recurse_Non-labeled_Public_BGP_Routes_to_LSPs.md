Configuring a Device to Be Able to Recurse Non-labeled Public BGP Routes to LSPs
================================================================================

By default, non-labeled public BGP routes can recurse to outbound interfaces and next hops, but not to LSPs. You can configure the system to be able to recurse non-labeled public BGP routes to LSPs.

#### Usage Scenario

If an Internet user uses a carrier network that performs IP forwarding to access the Internet, core carrier devices on the forwarding path need to learn many Internet routes. This imposes a heavy load on core carrier devices and affects their performance. To solve this problem, configure the corresponding access device to be able to recurse non-labeled public BGP routes to LSPs, so that packets can be forwarded over a tunnel. This configuration frees core carrier devices from learning Internet routes, saving their routing table entries and CPU resources.


#### Pre-configuration Tasks

Before configuring the device to be able to recurse non-labeled public BGP routes to LSPs, complete the following tasks:

* Configure the routing protocol or static routes.
* Establish an MPLS LSP, BGP LSP, or MPLS local IFNET tunnel.
* Configure an IP prefix list, tunnel selector or tunnel policy to allow only desired non-labeled public BGP routes to recurse to the LSP.

#### Procedure

* Configure the device to be able to recurse non-labeled public BGP routes and static routes to LSPs.
  
  
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**route recursive-lookup tunnel**](cmdqueryname=route+recursive-lookup+tunnel) [ **ip-prefix** *ip-prefix-name* ] [ **tunnel-policy** *policy-name* ] command to configure non-labeled public network routes to recurse to LSPs for MPLS forwarding.
     
     The [**route recursive-lookup tunnel**](cmdqueryname=route+recursive-lookup+tunnel) command can be used to recurse non-labeled public network BGP routes and static routes to BGP LSPs, LDP LSPs, SR LSPs, or MPLS local IFNET tunnels.
     + LDP LSP: Non-labeled public BGP routes and static routes can recurse to LDP LSPs and can carry unicast and multicast services.
     + BGP LSP: Non-labeled public BGP routes and static routes can recurse to BGP LSPs, supporting the bearer of unicast services but not multicast services.
     + SR LSP: Both non-labeled public network BGP routes and static routes can be recursed to SR-MPLS BE tunnels and carry unicast services rather than multicast services.
     + MPLS local IFNET tunnel: Only non-labeled public BGP routes can recurse to MPLS local IFNET tunnels, supporting the bearer of unicast and multicast services.
     
     If neither **ip-prefix** *ip-prefix-name* or **tunnel-policy** *policy-name* is specified, all static routes and non-labeled public BGP routes preferentially recurse to LSPs.
  3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure static routes to recurse to LSPs.
  
  
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**ip route-static recursive-lookup tunnel**](cmdqueryname=ip+route-static+recursive-lookup+tunnel) [ **ip-prefix** *ip-prefix-name* ] [ **tunnel-policy** *policy-name* ] command to allow static routes to recurse to LSPs for MPLS forwarding.
  3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure the device to be able to recurse non-labeled public BGP routes to LSPs.
  
  
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
  3. Run the [**unicast-route recursive-lookup tunnel**](cmdqueryname=unicast-route+recursive-lookup+tunnel) [ **tunnel-selector** *tunnel-selector-name* ] command to allow non-labeled public BGP routes to recurse to LSPs for MPLS forwarding.
  4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  The [**ip route-static recursive-lookup tunnel**](cmdqueryname=ip+route-static+recursive-lookup+tunnel) and [**unicast-route recursive-lookup tunnel**](cmdqueryname=unicast-route+recursive-lookup+tunnel) commands are mutually exclusive with the [**route recursive-lookup tunnel**](cmdqueryname=route+recursive-lookup+tunnel) command. The [**ip route-static recursive-lookup tunnel**](cmdqueryname=ip+route-static+recursive-lookup+tunnel) and [**unicast-route recursive-lookup tunnel**](cmdqueryname=unicast-route+recursive-lookup+tunnel) commands can be used together.

#### Verifying the Configuration

After non-labeled public network routes recurse to LSPs, you can run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table) *network* command to view route recursion information.