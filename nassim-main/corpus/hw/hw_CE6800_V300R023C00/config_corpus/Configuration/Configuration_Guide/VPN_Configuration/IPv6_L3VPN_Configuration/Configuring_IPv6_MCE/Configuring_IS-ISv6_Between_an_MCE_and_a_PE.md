Configuring IS-ISv6 Between an MCE and a PE
===========================================

Configuring IS-ISv6 Between an MCE and a PE

#### Prerequisites

Before configuring MCE, complete the following tasks:

* Configure a VPN instance for each service on the MCE and its connected PE. For details, see [Configuring an IPv6 VPN Instance on a PE](vrp_L3VPNv6_cfg_0006.html).
* Configure link and network layer protocols for LAN interfaces, and connect the LAN interface for each type of service to the MCE.
* Bind the MCE's interfaces and the PE's interface connected to the MCE to VPN instances and configure IP addresses for these interfaces. For details, see [Binding an Interface to the IPv6 VPN Instance](vrp_L3VPNv6_cfg_0007.html).

#### Context

Deleting a VPN instance or disabling the IPv6 address family of a VPN instance will also delete the related IS-ISv6 processes.


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
     
     A NET specifies the current IS-IS area address and the system ID of the device.
  4. (Optional) Set an IS-IS level.
     
     
     ```
     [is-level](cmdqueryname=is-level) { level-1 | level-1-2 | level-2 }
     ```
     
     The default level is Level-1-2.
  5. Enable IPv6 for the IS-IS process.
     
     
     ```
     [ipv6 enable](cmdqueryname=ipv6+enable+%28IS-IS+view%29) [ topology { compatible [ enable-mt-spf ] | ipv6 | standard } ]
     ```
     
     Before enabling IPv6 for the IS-IS process, enable IPv6 in the system view first.
  6. Import BGP routes.
     
     
     ```
     [ipv6 import-route](cmdqueryname=ipv6+import-route) bgp inherit-cost [ { level-1 | level-2 | level-1-2 } | tag tag | route-policy route-policy-name ] *
     ```
     
     If the IS-IS level is not specified in the command, BGP routes will be imported into the Level-2 IS-IS routing table.
  7. Return to the system view.
     
     
     ```
     [quit](cmdqueryname=quit)
     ```
  8. Enter the view of the interface bound to the VPN instance.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  9. Switch the interface working mode from Layer 2 to Layer 3.
     
     
     ```
     [undo portswitch](cmdqueryname=undo+portswitch)
     ```
     
     Determine whether to perform this step based on the current interface working mode.
  10. Enable IPv6 on the interface.
      
      
      ```
      [ipv6 enable](cmdqueryname=ipv6+enable)
      ```
  11. Enable IS-ISv6 on the interface.
      
      
      ```
      [isis ipv6 enable](cmdqueryname=isis+ipv6+enable) [ process-id ]
      ```
  12. Return to the system view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
  13. Enter the BGP view.
      
      
      ```
      [bgp](cmdqueryname=bgp) as-number
      ```
  14. Enter the BGP VPN instance IPv6 address family view.
      
      
      ```
      [ipv6-family](cmdqueryname=ipv6-family) vpn-instance vpn-instance-name
      ```
  15. Import IS-IS routes into the routing table for the BGP VPN instance IPv6 address family.
      
      
      ```
      [import-route](cmdqueryname=import-route) isis process-id [ med med-value | route-policy route-policy-name ] *
      ```
  16. Commit the configuration.
      
      
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
     
     A NET specifies the current IS-IS area address and the system ID of the device.
  4. (Optional) Set an IS-IS level.
     
     
     ```
     [is-level](cmdqueryname=is-level) { level-1 | level-1-2 | level-2 }
     ```
     
     The default level is Level-1-2.
  5. Enable IPv6 for the IS-IS process.
     
     
     ```
     [ipv6 enable](cmdqueryname=ipv6+enable+%28IS-IS+view%29) [ topology { compatible [ enable-mt-spf ] | ipv6 | standard } ]
     ```
     
     Before enabling IPv6 for the IS-IS process, enable IPv6 in the system view first.
  6. Return to the system view.
     
     
     ```
     [quit](cmdqueryname=quit)
     ```
  7. Enter the view of the interface bound to the VPN instance.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  8. Switch the interface working mode from Layer 2 to Layer 3.
     
     
     ```
     [undo portswitch](cmdqueryname=undo+portswitch)
     ```
     
     Determine whether to perform this step based on the current interface working mode.
  9. Enable IPv6 on the interface.
     
     
     ```
     [ipv6 enable](cmdqueryname=ipv6+enable)
     ```
  10. Enable IS-ISv6 on the interface.
      
      
      ```
      [isis ipv6 enable](cmdqueryname=isis+ipv6+enable) [ process-id ]
      ```
  11. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```

#### Verifying the Configuration

Run the [**display ipv6 routing-table vpn-instance**](cmdqueryname=display+ipv6+routing-table+vpn-instance) *vpn-instance-name* [ **verbose** ] command on the MCE to check the IPv6 routing table of the VPN instance.