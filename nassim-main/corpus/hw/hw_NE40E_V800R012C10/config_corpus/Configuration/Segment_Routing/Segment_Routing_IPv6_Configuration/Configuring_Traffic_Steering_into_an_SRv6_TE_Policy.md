Configuring Traffic Steering into an SRv6 TE Policy
===================================================

After configuring an SRv6 TE Policy, you need to configure traffic steering for services to use the SRv6 TE Policy.

#### Context

The main process of configuring traffic steering is as follows:

1. Configure a BGP extended community for route coloring.
2. Configure a tunnel policy to steer traffic based on the color, DSCP, service class, or TE-Class values.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In SRv6 TE Policy scenarios, you can only configure an IPv6 tunnel policy according to the specified tunnel selection sequence (Select-seq).
3. Apply the tunnel policy to specific services.

[Figure 1](#EN-US_TASK_0000001173128738__fig2062912661819) shows the configuration flowchart.

**Figure 1** Configuration flowchart  
![](figure/en-us_image_0000001228456248.png)


[Configuring a BGP Extended Community](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_srv6_cfg_all_0113.html)

This section describes how to add a BGP extended community, that is, the color extended community, to routes through a route-policy, enabling the routes to perform SRv6 recursion based on the color value.

[Configuring Color-based Traffic Steering into an SRv6 TE Policy](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_srv6_cfg_all_0291.html)

You can configure color-based traffic steering to recurse a route to an SRv6 TE Policy based on the color attribute, so that traffic can be forwarded through a path in the SRv6 TE Policy.

[Configuring DSCP-based Traffic Steering into an SRv6 TE Policy](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_srv6_cfg_all_0292.html)

You can configure DSCP-based traffic steering to recurse a route to an SRv6 TE Policy based on DSCP values, so that traffic can be forwarded through a path in the SRv6 TE Policy.

[Configuring Service Class-based Traffic Steering into an SRv6 TE Policy](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_srv6_cfg_all_0293.html)

You can configure service class-based traffic steering to recurse a route to an SRv6 TE Policy based on service class values, so that traffic can be forwarded through a path in the SRv6 TE Policy.

[Configuring TE-Class-based Traffic Steering into an SRv6 TE Policy](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_srv6_cfg_all_0294.html)

You can configure TE-Class-based traffic steering to recurse a route to an SRv6 TE Policy based on TE-Class IDs, so that traffic can be forwarded through a path in the SRv6 TE Policy.

[Applying a Tunnel Policy to Services](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_srv6_cfg_all_0114.html)

After configuring a traffic steering policy, you can apply a tunnel policy to specified services for them to recurse to an SRv6 TE Policy.