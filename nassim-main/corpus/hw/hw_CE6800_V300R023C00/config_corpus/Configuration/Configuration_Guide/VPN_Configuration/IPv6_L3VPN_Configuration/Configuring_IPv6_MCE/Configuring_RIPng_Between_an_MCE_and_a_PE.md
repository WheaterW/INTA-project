Configuring RIPng Between an MCE and a PE
=========================================

Configuring RIPng Between an MCE and a PE

#### Prerequisites

Before configuring MCE, complete the following tasks:

* Configure a VPN instance for each service on the MCE and its connected PE. For details, see [Configuring an IPv6 VPN Instance on a PE](vrp_L3VPNv6_cfg_0006.html).
* Configure link and network layer protocols for LAN interfaces, and connect the LAN interface for each type of service to the MCE.
* Bind the MCE's interfaces and the PE's interface connected to the MCE to VPN instances and configure IP addresses for these interfaces. For details, see [Binding an Interface to the IPv6 VPN Instance](vrp_L3VPNv6_cfg_0007.html).

#### Context

Deleting a VPN instance or disabling the IPv6 address family of a VPN instance will also delete the related RIPng processes.


#### Procedure

* Configure the PE.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Create a RIPng process, bind it to a VPN instance, and enter the RIPng view.
     
     
     ```
     [ripng](cmdqueryname=ripng) process-id vpn-instance vpn-instance-name
     ```
     
     A RIPng process can be bound to only one VPN instance.
  3. Import BGP routes.
     
     
     ```
     [import-route](cmdqueryname=import-route) bgp [ permit-ibgp ] [ cost cost | inherit-cost | route-policy route-policy-name ] *
     ```
  4. Return to the system view.
     
     
     ```
     [quit](cmdqueryname=quit)
     ```
  5. Enter the view of the interface connected to the MCE.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  6. Switch the interface working mode from Layer 2 to Layer 3.
     
     
     ```
     [undo portswitch](cmdqueryname=undo+portswitch)
     ```
     
     Determine whether to perform this step based on the current interface working mode.
  7. Enable IPv6 on the interface.
     
     
     ```
     [ipv6 enable](cmdqueryname=ipv6+enable)
     ```
  8. Enable RIPng on the interface.
     
     
     ```
     [ripng](cmdqueryname=ripng) process-id enable
     ```
  9. Enter the BGP view.
     
     
     ```
     [bgp](cmdqueryname=bgp) as-number
     ```
  10. Enter the BGP VPN instance IPv6 address family view.
      
      
      ```
      [ipv6-family](cmdqueryname=ipv6-family) vpn-instance vpn-instance-name
      ```
  11. Import RIP routes into the routing table for the BGP VPN instance IPv6 address family.
      
      
      ```
      [import-route](cmdqueryname=import-route) rip process-id [ med med-value | route-policy route-policy-name ] *
      ```
  12. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```
* Configure the MCE.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Create a RIP process, bind it to a VPN instance, and enter the RIP view.
     
     
     ```
     [rip](cmdqueryname=rip) process-id vpn-instance vpn-instance-name
     ```
     
     A RIP process can be bound to only one VPN instance.
     
     If a RIP process is not bound to any VPN instance before it is started, this process becomes a public network process and cannot be bound to a VPN instance later.
  3. Return to the system view.
     
     
     ```
     [quit](cmdqueryname=quit)
     ```
  4. Enter the view of the interface connected to the PE.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  5. Switch the interface working mode from Layer 2 to Layer 3.
     
     
     ```
     [undo portswitch](cmdqueryname=undo+portswitch)
     ```
     
     Determine whether to perform this step based on the current interface working mode.
  6. Enable IPv6 on the interface.
     
     
     ```
     [ipv6 enable](cmdqueryname=ipv6+enable)
     ```
  7. Enable RIPng on the interface.
     
     
     ```
     [ripng](cmdqueryname=ripng) process-id enable
     ```
  8. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Verifying the Configuration

Run the [**display ipv6 routing-table vpn-instance**](cmdqueryname=display+ipv6+routing-table+vpn-instance) *vpn-instance-name* [ **verbose** ] command on the MCE to check the IPv6 routing table of the VPN instance.