Configuring Static Routes Between an MCE and a PE
=================================================

Configuring Static Routes Between an MCE and a PE

#### Prerequisites

Before configuring MCE, complete the following tasks:

* Configure a VPN instance for each service on the MCE and its connected PE. For details, see [Configuring an IPv6 VPN Instance on a PE](vrp_L3VPNv6_cfg_0006.html).
* Configure link and network layer protocols for LAN interfaces, and connect the LAN interface for each type of service to the MCE.
* Bind the MCE's interfaces and the PE's interface connected to the MCE to VPN instances and configure IP addresses for these interfaces. For details, see [Binding an Interface to the IPv6 VPN Instance](vrp_L3VPNv6_cfg_0007.html).

#### Procedure

* Configure the PE.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure a static route for the IPv6 address family of a specified VPN instance.
     
     
     ```
     [ipv6 route-static vpn-instance](cmdqueryname=ipv6+route-static+vpn-instance) vpn-source-name dest-ipv6-address prefix-length interface-type interface-number [ nexthop-ipv6-address ] [ preference preference | tag tag ] *
     ```
  3. Enter the BGP view.
     
     
     ```
     [bgp](cmdqueryname=bgp) as-number
     ```
  4. Enter the BGP VPN instance IPv6 address family view.
     
     
     ```
     [ipv6-family](cmdqueryname=ipv6-family) vpn-instance vpn-instance-name
     ```
  5. Import the configured static route into the routing table for the BGP VPN instance IPv6 address family.
     
     
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
  2. Configure a static route for the IPv6 address family of a specified VPN instance.
     
     
     ```
     [ipv6 route-static vpn-instance](cmdqueryname=ipv6+route-static+vpn-instance) vpn-source-name destination-ipv6-address prefix-length interface-type interface-number [ nexthop-ipv6-address ] [ preference preference | tag tag ] *
     ```
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Verifying the Configuration

Run the [**display ipv6 routing-table vpn-instance**](cmdqueryname=display+ipv6+routing-table+vpn-instance) *vpn-instance-name* [ **verbose** ] command on the MCE to check the IPv6 routing table of the VPN instance.