Configuring OSPFv3 Between an MCE and a PE
==========================================

Configuring OSPFv3 Between an MCE and a PE

#### Prerequisites

Before configuring MCE, complete the following tasks:

* Configure a VPN instance for each service on the MCE and its connected PE. For details, see [Configuring an IPv6 VPN Instance on a PE](vrp_L3VPNv6_cfg_0006.html).
* Configure link and network layer protocols for LAN interfaces, and connect the LAN interface for each type of service to the MCE.
* Bind the MCE's interfaces and the PE's interface connected to the MCE to VPN instances and configure IP addresses for these interfaces. For details, see [Binding an Interface to the IPv6 VPN Instance](vrp_L3VPNv6_cfg_0007.html).

#### Context

Deleting a VPN instance or disabling the IPv6 address family of a VPN instance will also delete the related OSPFv3 processes.


#### Procedure

* Configure the PE.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Create an OSPFv3 process, bind it to a VPN instance, and enter the OSPFv3 view.
     
     
     ```
     [ospfv3](cmdqueryname=ospfv3) [ process-id ] vpn-instance vpnname
     ```
     
     An OSPFv3 process can be bound to only one VPN instance.
     
     A router ID needs to be specified when an OSPF process is started after it is bound to a VPN instance. The router ID must be different from the public network router ID configured in the system view. If the router ID is not specified, OSPFv3 selects the IP address of one of the interfaces bound to the VPN instance as the router ID based on a certain rule.
  3. Configure a router ID.
     
     
     ```
     [router-id](cmdqueryname=router-id) router-id
     ```
     
     A router ID uniquely identifies an OSPFv3 process in an AS. If no router ID is configured, the OSPFv3 process cannot run.
  4. (Optional) Configure a domain ID for the OSPFv3 process.
     
     
     ```
     [domain-id](cmdqueryname=domain-id) domain-idvalue [ secondary ]
     ```
     
     The domain ID can be either an integer or a dotted decimal number.
     
     Generally, the routes that are imported from a PE are advertised as External-LSAs. The routes that belong to different nodes of the same OSPFv3 domain are advertised as Type-3 LSAs (intra-domain routes). This requires that different nodes in the same OSPFv3 domain have the same domain ID.
  5. Import BGP routes.
     
     
     ```
     [import-route](cmdqueryname=import-route) bgp [ cost cost | tag tag | type type | route-policy route-policy-name ]*
     ```
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
  10. Enable OSPFv3 on the interface.
      
      
      ```
      [ospfv3](cmdqueryname=ospfv3) process-id area area-id [ instance instance-id ]
      ```
  11. Return to the system view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
  12. Enter the BGP view.
      
      
      ```
      [bgp](cmdqueryname=bgp) as-number
      ```
  13. Enter the BGP VPN instance IPv6 address family view.
      
      
      ```
      [ipv6-family](cmdqueryname=ipv6-family) vpn-instance vpn-instance-name
      ```
  14. Import OSPFv3 routes into the routing table for the BGP VPN instance IPv6 address family.
      
      
      ```
      [import-route](cmdqueryname=import-route) ospfv3 process-id [ med med-value | route-policy route-policy-name ] *
      ```
  15. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```
* Configure the MCE.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Create an OSPFv3 process, bind it to a VPN instance, and enter the OSPFv3 view.
     
     
     ```
     [ospfv3](cmdqueryname=ospfv3) [ process-id ] vpn-instance vpnname
     ```
     
     An OSPFv3 process can be bound to only one VPN instance.
     
     A router ID needs to be specified when an OSPF process is started after it is bound to a VPN instance. The router ID must be different from the public network router ID configured in the system view. If the router ID is not specified, OSPFv3 selects the IP address of one of the interfaces bound to the VPN instance as the router ID based on a certain rule.
  3. Configure a router ID.
     
     
     ```
     [router-id](cmdqueryname=router-id) router-id
     ```
     
     A router ID uniquely identifies an OSPFv3 process in an AS. If no router ID is configured, the OSPFv3 process cannot run.
  4. (Optional) Configure a domain ID for the OSPFv3 process.
     
     
     ```
     [domain-id](cmdqueryname=domain-id) domain-idvalue [ secondary ]
     ```
     
     The domain ID can be either an integer or a dotted decimal number.
     
     Generally, the routes that are imported from a PE are advertised as External-LSAs. The routes that belong to different nodes of the same OSPFv3 domain are advertised as Type 3 LSAs (intra-domain routes). This requires that different nodes in the same OSPFv3 domain have the same domain ID.
  5. Disable routing loop detection.
     
     
     ```
     [vpn-instance-capability simple](cmdqueryname=vpn-instance-capability+simple)
     ```
     
     If OSPFv3 multi-instance is deployed on the MCE, the MCE receives LSAs with the Down (DN) bit set to 1 from the PE. Because routing loop detection has been enabled for VPN instances on the MCE, the MCE cannot use these LSAs to calculate routes. In this case, run the [**vpn-instance-capability simple**](cmdqueryname=vpn-instance-capability+simple) command to disable OSPFv3 routing loop detection. The MCE can then use LSAs to calculate OSPFv3 routes without checking the DN bits and route tags carried in these LSAs.
  6. Enter the view of the interface bound to a VPN instance.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  7. Switch the interface working mode from Layer 2 to Layer 3.
     
     
     ```
     [undo portswitch](cmdqueryname=undo+portswitch)
     ```
     
     Determine whether to perform this step based on the current interface working mode.
  8. Enable IPv6 on the interface.
     
     
     ```
     [ipv6 enable](cmdqueryname=ipv6+enable)
     ```
  9. Enable OSPFv3 on the interface.
     
     
     ```
     [ospfv3](cmdqueryname=ospfv3) process-id area area-id [ instance instance-id ]
     ```
  10. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```

#### Verifying the Configuration

Run the [**display ipv6 routing-table vpn-instance**](cmdqueryname=display+ipv6+routing-table+vpn-instance) *vpn-instance-name* [ **verbose** ] command on the MCE to check the IPv6 routing table of the VPN instance.