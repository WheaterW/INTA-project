Configuring LDP Extension for Inter-Area LSPs
=============================================

Before configuring LDP extension for inter-area LSPs, familiarize yourself with the usage scenario, complete the pre-configuration tasks, and obtain the data required for the configuration.

#### Usage Scenario

On a large-scale network, multiple IGP areas need to be configured for flexible deployment and fast convergence. To prevent excessive resource consumption caused by a large number of routes, an area border router (ABR) needs to summarize the routes in an area and advertise the summary routes to neighboring IGP areas. By default, when establishing an LSP, LDP searches the routing table for the route that exactly matches the FEC carried in a received Label Mapping message. For summary routes, LDP can establish only liberal LSPs, but cannot establish LDP LSPs across IGP areas.

In this case, you can run the [**longest-match**](cmdqueryname=longest-match) command to enable LDP to search for routes based on the longest match rule and establish inter-area LDP LSPs.


#### Pre-configuration Tasks

Before configuring LDP extension for inter-area LSPs, complete the following task:

* Configure addresses for interfaces to ensure that neighboring devices are reachable at the network layer.
* Configure an IGP to advertise the route to the network segment of each interface and to advertise the host route to each LSR ID.
* Configure a policy for summarizing routes.
* Configure MPLS and MPLS LDP.


[Configuring LDP Extension for Inter-Area LSPs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0102.html)

LDP extension for inter-area LSPs can be configured on the ingress and transit nodes.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0103.html)

After configuring LDP extension for inter-area LSPs, you can view information about the establishment of inter-Area LSPs.