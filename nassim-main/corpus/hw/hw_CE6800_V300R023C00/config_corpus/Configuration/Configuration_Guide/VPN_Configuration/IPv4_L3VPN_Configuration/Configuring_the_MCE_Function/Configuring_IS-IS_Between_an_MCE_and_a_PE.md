Configuring IS-IS Between an MCE and a PE
=========================================

Configuring IS-IS Between an MCE and a PE

#### Prerequisites

Before configuring MCE, you have completed the following tasks:

* Configure a VPN instance for each service on the MCE and its connected PE. For details, see [Configuring an IPv4 VPN Instance on a PE](vrp_L3VPNv4_cfg_0007.html).
* Configure link and network layer protocols for LAN interfaces, and connect the LAN interface for each type of service to the MCE.
* Bind each MCE interface and the PE interface connecting to the MCE to the VPN instance, and configure IP addresses for the interfaces. For detailed configurations, see [Binding an Interface to an IPv4 VPN Instance](vrp_L3VPNv4_cfg_0008.html).

#### Context

Deleting a VPN instance or disabling a VPN instance IPv4 address family will delete all the IS-IS processes bound to the VPN instance and the VPN instance IPv4 address family.


#### Procedure

* Configure the PE.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Create an IS-IS process, bind it to a VPN instance, and enter the IS-IS view.
     
     
     ```
     [isis](cmdqueryname=isis) process-id vpn-instance vpn-instance-name
     ```
     
     An IS-IS process can be bound to only one VPN instance.
  3. Set a network entity title (NET).
     
     
     ```
     [network-entity](cmdqueryname=network-entity) net-addr
     ```
     
     A NET specifies the current IS-IS area address and the system ID.
  4. (Optional) Set an IS-IS level.
     
     
     ```
     [is-level](cmdqueryname=is-level) { level-1 | level-1-2 | level-2 }
     ```
     
     The default level is Level-1-2.
  5. Import BGP routes.
     
     
     ```
     [import-route](cmdqueryname=import-route) bgp [ cost-type { external | internal } | cost cost | tag tag | route-policy route-policy-name | [ level-1 | level-2 | level-1-2 ] ] *
     ```
     
     If the IS-IS level is not specified in the command, BGP routes will be imported into the Level-2 IS-IS routing table.
  6. Return to the system view.
     
     
     ```
     [quit](cmdqueryname=quit)
     ```
  7. Enter the view of the interface to be bound to the VPN instance.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  8. Switch the interface working mode from Layer 2 to Layer 3.
     
     
     ```
     [undo portswitch](cmdqueryname=undo+portswitch)
     ```
     
     Determine whether to perform this step based on the current interface working mode.
  9. Enable IS-IS on the interface.
     
     
     ```
     [isis enable](cmdqueryname=isis+enable) [ process-id ]
     ```
  10. Return to the system view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
  11. Enter the BGP view.
      
      
      ```
      [bgp](cmdqueryname=bgp) as-number
      ```
  12. Enter the BGP VPN instance IPv4 address family view.
      
      
      ```
      [ipv4-family](cmdqueryname=ipv4-family) vpn-instance vpn-instance-name
      ```
  13. Import IS-IS routes into the routing table of the BGP VPN instance IPv4 address family.
      
      
      ```
      [import-route](cmdqueryname=import-route) isis process-id [ med med-value | route-policy route-policy-name ] *
      ```
  14. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```
* Configure the MCE.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Create an IS-IS process, bind it to a VPN instance, and enter the IS-IS view.
     
     
     ```
     [isis](cmdqueryname=isis) process-id vpn-instance vpn-instance-name
     ```
     
     An IS-IS process can be bound to only one VPN instance. If an IS-IS process is not bound to any VPN instance before it is started, this process becomes a public network process and cannot be bound to a VPN instance later.
  3. Set a NET.
     
     
     ```
     [network-entity](cmdqueryname=network-entity) net-addr
     ```
     
     A NET specifies the current IS-IS area address and the system ID.
  4. (Optional) Set an IS-IS level.
     
     
     ```
     [is-level](cmdqueryname=is-level) { level-1 | level-1-2 | level-2 }
     ```
     
     The default level is Level-1-2.
  5. Return to the system view.
     
     
     ```
     [quit](cmdqueryname=quit)
     ```
  6. Enter the view of the interface to be bound to the VPN instance.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  7. Switch the interface working mode from Layer 2 to Layer 3.
     
     
     ```
     [undo portswitch](cmdqueryname=undo+portswitch)
     ```
     
     Determine whether to perform this step based on the current interface working mode.
  8. Enable IS-IS on the interface.
     
     
     ```
     [isis enable](cmdqueryname=isis+enable) [ process-id ]
     ```
  9. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```