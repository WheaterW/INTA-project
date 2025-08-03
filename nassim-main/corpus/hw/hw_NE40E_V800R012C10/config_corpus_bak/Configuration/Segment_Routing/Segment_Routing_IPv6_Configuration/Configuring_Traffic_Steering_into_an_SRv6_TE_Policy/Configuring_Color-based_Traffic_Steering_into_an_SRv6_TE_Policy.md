Configuring Color-based Traffic Steering into an SRv6 TE Policy
===============================================================

You can configure color-based traffic steering to recurse a route to an SRv6 TE Policy based on the color attribute, so that traffic can be forwarded through a path in the SRv6 TE Policy.

#### Prerequisites

Before configuring color-based traffic steering into an SRv6 TE Policy, complete the following task:

* Configure an SRv6 TE Policy.

#### Context

After an SRv6 TE Policy is configured, traffic needs to be steered into it for forwarding. This process is called traffic steering. Currently, SRv6 TE Policies can be used for various services, such as BGP L3VPN and EVPN services. This section describes how to configure services to recurse to an SRv6 TE Policy through a specified tunnel policy.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**tunnel-policy**](cmdqueryname=tunnel-policy) *policy-name*
   
   
   
   A tunnel policy is created, and its view is displayed.
3. (Optional) Run [**description**](cmdqueryname=description) *description-text*
   
   
   
   A description is configured for the tunnel policy.
4. Run [**tunnel select-seq**](cmdqueryname=tunnel+select-seq) **ipv6 srv6-te-policy** **load-balance-number** *loadBalanceNumber*
   
   
   
   The tunnel selection sequence and the number of tunnels for load balancing are configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After the preceding configurations are complete, routes are allowed to recurse to SRv6 TE Policies. If the color and next hop of a route are the same as the color and endpoint of an SRv6 TE Policy, respectively, the route can successfully recurse to the SRv6 TE Policy. In this case, the traffic forwarded through the route can be steered into the SRv6 TE Policy.
   
   Because there can be only one effective SRv6 TE Policy with the endpoint and color specified, load balancing is not involved.
   
   If the endpoint configured for an SRv6 TE Policy is ::, traffic steering is implemented in color-only mode. In this case, a route can recurse to an SRv6 TE Policy as long as their colors match.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.