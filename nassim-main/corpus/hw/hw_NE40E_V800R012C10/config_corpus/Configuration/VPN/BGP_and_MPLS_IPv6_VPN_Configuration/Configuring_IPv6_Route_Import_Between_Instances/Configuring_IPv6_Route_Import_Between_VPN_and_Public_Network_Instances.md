Configuring IPv6 Route Import Between VPN and Public Network Instances
======================================================================

IPv6 route import between VPN and public network instances enables IPv6 VPN users to communicate with IPv6 public network users.

#### Context

Perform the following steps for target VPN and public network instances. ![](../../../../public_sys-resources/note_3.0-en-us.png) 

If you do not want a VPN instance to change the next hops of imported routes when advertising these routes to its IBGP peers, run the [**import-rib route next-hop-invariable**](cmdqueryname=import-rib+route+next-hop-invariable) command for the VPN instance.




#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure the device to import different types of IPv6 VPN routes to the public network instance's corresponding routing tables. 
   
   
   * Run the [**ipv6 import-rib vpn-instance**](cmdqueryname=ipv6+import-rib+vpn-instance) *vpn-instance-name* **protocol** { **direct** | **vlink-direct-route** | { **static** | **isis** *process-id* | **ospfv3** *process-id* } [ **valid-route** ] } [ **route-policy** *route-policy-name* | **route-filter** *route-filter-name* ] command to configure the device to import direct routes, Vlink direct routes, IGP routes, or static routes from a VPN instance to the public network instance's corresponding routing table.
   * Configure the device to import VPN BGP4+ routes to the public network instance's BGP4+ routing table.
     1. Run [**bgp**](cmdqueryname=bgp) *as-number*
        
        The BGP view is displayed.
     2. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
        
        The BGP-IPv6 unicast address family view is displayed.
     3. Run [**import-rib vpn-instance**](cmdqueryname=import-rib+vpn-instance) *vpn-instance-name* [ **include-label-route** ] [ **valid-route** ] [ **route-policy** *route-policy-name* ]
        
        The device is enabled to import VPN BGP4+ routes to the public network instance's BGP4+ routing table.
     4. Run [**quit**](cmdqueryname=quit)
        
        Return to the BGP view.
     5. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
3. Configure the device to import different types of IPv6 public network routes to a VPN instance's corresponding routing tables. 
   
   
   * Configure the device to import IPv6 public network direct routes, static routes, or IGP routes to a VPN instance's corresponding routing table.
     1. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
        
        The VPN instance view is displayed.
     2. Run [**ipv6-family**](cmdqueryname=ipv6-family)
        
        The VPN instance IPv6 address family view is displayed.
     3. Run [**import-rib**](cmdqueryname=import-rib) **public** **protocol** { **direct** | **vlink-direct-route** | { **static** | **isis** *process-id* | **ospfv3** *process-id* } [ **valid-route** ] } [ **route-policy** *route-policy-name* | **route-filter** *route-filter-name* ]
        
        The device is configured to import direct routes, Vlink direct routes, static routes, or IGP routes from the public network instance to a VPN instance's corresponding routing table.
   * Configure the device to import public network BGP4+ routes to a VPN instance's BGP4+ routing table.
     1. Run [**bgp**](cmdqueryname=bgp) *as-number*
        
        The BGP view is displayed.
     2. Run [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name*
        
        The BGP-VPN instance IPv6 address family view is displayed.
     3. Run [**import-rib**](cmdqueryname=import-rib) **public** [ **include-label-route** ] [ **valid-route** ] [ **route-policy** *route-policy-name* ]
        
        The device is enabled to import public network BGP routes to the VPN instance's BGP routing table.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.