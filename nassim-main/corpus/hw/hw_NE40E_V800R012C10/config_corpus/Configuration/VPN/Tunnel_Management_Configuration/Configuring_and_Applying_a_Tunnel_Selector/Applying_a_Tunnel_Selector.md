Applying a Tunnel Selector
==========================

After a tunnel selector is configured, it needs to be applied to VPNv4 routes, VPNv6 routes, or labeled BGP routes. The mode in which a tunnel selector is applied to routes varies according to the route type.

#### Context

A PE or ASBR can recurse routes to appropriate tunnels only after a tunnel selector is applied to these routes.

A tunnel selector applies to the following types of routes:

* VPNv4 routes: A tunnel selector can be applied to the BGP-VPNv4 address family so that the ASBR in inter-AS VPN Option B networking can apply tunnel policies to VPNv4 routes and recurse these routes to appropriate tunnels.
* VPNv6 routes: A tunnel selector can be applied to the BGP-VPNv6 address family so that the ASBR in inter-AS VPN Option B networking can apply tunnel policies to VPNv6 routes and recurse these routes to appropriate tunnels.
* Labeled BGP-IPv4 routes: A tunnel selector can be applied to the BGP-IPv4 unicast address family so that the PE in inter-AS VPN Option C networking can apply tunnel policies to labeled BGP-IPv4 routes.
* BGP-EVPN routes: A tunnel selector can be applied to the BGP-EVPN address family so that the PE in inter-AS EVPN Option B networking can apply tunnel policies to labeled BGP-EVPN routes.
* L2VPN-AD routes: A tunnel selector can be applied to the BGP-L2VPN-AD address family so that the ASBR in the inter-AS VPLS Option B networking can apply tunnel policies to BGP L2VPN-AD routes.

Perform the following steps on the PE or ASBR where a tunnel selector needs to be applied:


#### Procedure

* Apply a tunnel selector to VPNv4 routes.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
  3. Run the [**ipv4-family**](cmdqueryname=ipv4-family) **vpnv4** command to enter the BGP-VPNv4 address family view.
  4. Run the [**tunnel-selector**](cmdqueryname=tunnel-selector) *tunnel-selector-name* command to apply a tunnel selector to VPNv4 routes on the local device.
     
     
     
     After the tunnel selector is applied to VPNv4 routes, the VPNv4 routes that match the **if-match** clause recurse to tunnels according to the tunnel policy specified in the **apply** clause. The VPNv4 routes that do not match the **if-match** clause recurse to LSPs by default.
  5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Apply a tunnel selector to VPNv6 routes.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
  3. Run the [**ipv6-family**](cmdqueryname=ipv6-family) **vpnv6** command to enter the BGP-VPNv6 address family view.
  4. Run the [**tunnel-selector**](cmdqueryname=tunnel-selector) *tunnel-selector-name* command to apply a tunnel selector to VPNv6 routes on the local device.
     
     
     
     After the tunnel selector is applied to VPNv6 routes, the VPNv6 routes that match the **if-match** clause recurse to tunnels according to the tunnel policy specified in the **apply** clause. The VPNv6 routes that do not match the **if-match** clause recurse to LSPs by default.
  5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Apply a tunnel selector to labeled BGP-IPv4 routes.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
  3. Run the [**tunnel-selector**](cmdqueryname=tunnel-selector) *tunnel-selector-name* [ **all** ] command to apply a tunnel selector to BGP-IPv4 routes on the local device.
     
     
     
     After the tunnel selector is applied to BGP-IPv4 labeled routes, the labeled routes that match the **if-match** clause recurse to tunnels according to the tunnel policy specified in the **apply** clause. The labeled BGP-IPv4 routes that do not match the **if-match** clause recurse to LSPs by default.
     
     In an inter-AS VPN Option C scenario, to implement tunnel-based load-balancing among labeled BGP routes on the ASBR, run the [**tunnel-selector**](cmdqueryname=tunnel-selector) *tunnel-selector-name* **all** command to configure a tunnel selector on the ASBR. If the **all** parameter is used, the tunnel selector applies to all BGP IPv4 unicast routes, including labeled routes, imported routes, and network segment routes.
  4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Apply a tunnel selector to BGP-EVPN routes.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
  3. Run the [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn) command to enter the BGP-EVPN address family view.
  4. Run the [**tunnel-selector**](cmdqueryname=tunnel-selector) *tunnel-selector-name* command to apply a tunnel selector to BGP-EVPN routes on the local device.
     
     
     
     After the tunnel selector is applied to BGP-EVPN routes, the BGP-EVPN routes that match the **if-match** clause recurse to tunnels according to the tunnel policy specified in the **apply** clause. BGP-EVPN routes that do not match the **if-match** clause recurse to LSPs by default.
  5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Apply a tunnel selector to BGP L2VPN-AD routes.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
  3. Run the [**l2vpn-ad-family**](cmdqueryname=l2vpn-ad-family) command to enter the BGP L2VPN-AD address family view.
  4. Run the [**tunnel-selector**](cmdqueryname=tunnel-selector) *tunnel-selector-name* command to apply a tunnel selector to L2VPN-AD routes on the local device.
     
     
     
     After the tunnel selector is applied to L2VPN-AD routes, the L2VPN-AD routes that match the **if-match** clause recurse to tunnels according to the tunnel policy specified in the **apply** clause. L2VPN-AD routes that do not match the **if-match** clause recurse to LSPs by default.
  5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.