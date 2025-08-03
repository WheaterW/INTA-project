Configuring Static Routes Between an MCE and a PE
=================================================

Configuring Static Routes Between an MCE and a PE

#### Prerequisites

Before configuring MCE, you have completed the following tasks:

* Configure a VPN instance for each service on the MCE and its connected PE. For details, see [Configuring an IPv4 VPN Instance on a PE](vrp_L3VPNv4_cfg_0007.html).
* Configure link and network layer protocols for LAN interfaces, and connect the LAN interface for each type of service to the MCE.
* Bind each MCE interface and the PE interface connecting to the MCE to the VPN instance, and configure IP addresses for the interfaces. For detailed configurations, see [Binding an Interface to an IPv4 VPN Instance](vrp_L3VPNv4_cfg_0008.html).

#### Context

![](public_sys-resources/note_3.0-en-us.png) 

The CE6885-LL working in low latency mode does not support this function.



#### Procedure

* Configure the PE.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure a static route for a specified VPN instance IPv4 address family.
     
     
     ```
     [ip route-static vpn-instance](cmdqueryname=ip+route-static+vpn-instance) vpn-source-name destination-address { mask | mask-length } interface-type interface-number [ nexthop-address ] [ preference preference | tag tag ] *
     ```
  3. Enter the BGP view.
     
     
     ```
     [bgp](cmdqueryname=bgp) as-number
     ```
  4. Enter the BGP VPN instance IPv4 address family view.
     
     
     ```
     [ipv4-family](cmdqueryname=ipv4-family) vpn-instance vpn-instance-name
     ```
  5. Import the configured static route to the routing table of the BGP VPN instance IPv4 address family.
     
     
     ```
     [import-route](cmdqueryname=import-route) static [ med med-value | route-policy route-policy-name ] *
     ```
  6. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure the MCE.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure a static route for a specified VPN instance IPv4 address family.
     
     
     ```
     [ip route-static vpn-instance](cmdqueryname=ip+route-static+vpn-instance) vpn-source-name destination-address { mask | mask-length } interface-type interface-number [ nexthop-address ] [ preference preference | tag tag ] *
     ```
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```