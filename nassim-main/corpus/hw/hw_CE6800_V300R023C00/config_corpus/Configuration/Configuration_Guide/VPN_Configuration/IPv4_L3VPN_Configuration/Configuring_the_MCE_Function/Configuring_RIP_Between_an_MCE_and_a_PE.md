Configuring RIP Between an MCE and a PE
=======================================

Configuring RIP Between an MCE and a PE

#### Prerequisites

Before configuring MCE, you have completed the following tasks:

* Configure a VPN instance for each service on the MCE and its connected PE. For details, see [Configuring an IPv4 VPN Instance on a PE](vrp_L3VPNv4_cfg_0007.html).
* Configure link and network layer protocols for LAN interfaces, and connect the LAN interface for each type of service to the MCE.
* Bind each MCE interface and the PE interface connecting to the MCE to the VPN instance, and configure IP addresses for the interfaces. For detailed configurations, see [Binding an Interface to an IPv4 VPN Instance](vrp_L3VPNv4_cfg_0008.html).

#### Context

Deleting a VPN instance or disabling a VPN instance IPv4 address family will delete all the RIP processes bound to the VPN instance and the VPN instance IPv4 address family.


#### Procedure

* Configure the PE.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Create a RIP process and enter the RIP view.
     
     
     ```
     [rip](cmdqueryname=rip) process-id vpn-instance vpn-instance-name
     ```
     
     A RIP process can be bound to only one VPN instance.
  3. Enable RIP on the network segment of the interface to which the VPN instance is bound.
     
     
     ```
     [network](cmdqueryname=network) network-address
     ```
  4. Import BGP routes.
     
     
     ```
     [import-route](cmdqueryname=import-route) bgp [ cost { cost | transparent } | route-policy route-policy-name ] *
     ```
  5. Return to the system view.
     
     
     ```
     [quit](cmdqueryname=quit)
     ```
  6. Enter the BGP view.
     
     
     ```
     [bgp](cmdqueryname=bgp) as-number
     ```
  7. Enter the BGP VPN instance IPv4 address family view.
     
     
     ```
     [ipv4-family](cmdqueryname=ipv4-family) vpn-instance vpn-instance-name
     ```
  8. Import RIP routes into the routing table of the BGP VPN instance IPv4 address family.
     
     
     ```
     [import-route](cmdqueryname=import-route) rip process-id [ med med-value | route-policy route-policy-name ] *
     ```
  9. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure the MCE.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Create a RIP process and enter the RIP view.
     
     
     ```
     [rip](cmdqueryname=rip) process-id vpn-instance vpn-instance-name
     ```
     
     A RIP process can be bound to only one VPN instance.
     
     If a RIP process is not bound to any VPN instance before it is started, this process becomes a public network process and cannot be bound to a VPN instance later.
  3. Enable RIP on the network segment of the interface to which the VPN instance is bound.
     
     
     ```
     [network](cmdqueryname=network) network-address
     ```
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```