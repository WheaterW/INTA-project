Configuring and Applying a Tunnel Selector
==========================================

A tunnel selector can apply a tunnel policy to routes, improving the flexibility of using tunnels.

#### Context

In BGP/MPLS IP VPN networking, after a tunnel policy is applied to a VPN instance, all the routes of the VPN instance recurse to the same tunnel according to the tunnel policy. In inter-AS VPN Option B networking, ASBRs receive all VPNv4 or VPNv6 routes from PE peers. Currently, the system recurses VPNv4 or VPNv6 routes to LSPs. Sometimes, these VPNv4 or VPNv6 routes need to recurse to TE tunnels to guarantee bandwidth. If you do not want to create VPN instances on ASBRs, tunnel policies cannot be used.

Moreover, in inter-AS VPN Option C networking, a device cannot recurse labeled routes to TE tunnels to guarantee bandwidth or implement load balancing among BGP LSPs by default.

This is where the tunnel selector comes in.

A tunnel selector can apply a tunnel policy to VPNv4/VPNv6 routes or BGP-IPv4 labeled routes so that expected tunnels can be selected based on the tunnel policy.


#### Pre-configuration Tasks

Before configuring a tunnel selector, complete the following tasks:

* Configure a tunnel binding policy.
* Configure an RD filter if routes need to be filtered based on RDs.
* Configure an ACL or IPv4 prefix list if routes need to be filtered based on the next hop IPv4 address.
* Configure an IPv6 access control list (ACL6) or IPv6 prefix list if routes need to be filtered based on the next hop IPv6 address.


[Configuring a Tunnel Selector](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_tnlm_cfg_0022_1.html)

A tunnel selector comprises **if-match** and **apply** clauses. The **if-match** clause defines route filtering rules, whereas the **apply** clause applies a tunnel policy to routes that match the **if-match** clause.

[Applying a Tunnel Selector](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_tnlm_cfg_0023_1.html)

After a tunnel selector is configured, it needs to be applied to VPNv4 routes, VPNv6 routes, or labeled BGP routes. The mode in which a tunnel selector is applied to routes varies according to the route type.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_tnlm_cfg_0024_1.html)

After configuring and applying a tunnel selector, run the following commands to check tunnel selector and tunnel policy information in the system.