Configuring Route Import Between VPN and Public Network Instances
=================================================================

Route import between VPN and public network instances enables VPN users and public network users to communicate.

#### Procedure

* Configure route import between VPN and public network instances.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If you do not want a VPN instance to change the next hops of routes imported from the public network instance or other VPN instances when advertising these routes to its IBGP peers, run the [**import-rib route next-hop-invariable**](cmdqueryname=import-rib+route+next-hop-invariable) command for the VPN instance.
  
  
  
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Configure the device to import different types of VPN routes to the public network instance's corresponding routing tables.
     
     
     + To configure the device to import direct routes from a VPN instance into the public network instance's corresponding routing table, run the [**ip import-rib vpn-instance**](cmdqueryname=ip+import-rib+vpn-instance) *vpn-instance-name* **protocol** **direct** [ **route-policy** *route-policy-name* | **route-filter** *route-filter-name* ] command.
     + To configure the device to import Vlink direct routes from a VPN instance into the public network instance's corresponding routing table, run the [**ip import-rib vpn-instance**](cmdqueryname=ip+import-rib+vpn-instance) *vpn-instance-name* **protocol** **vlink-direct-route** [ **route-policy** *route-policy-name* | **route-filter** *route-filter-name* ] command.
     + To configure the device to import static routes or IGP routes from a VPN instance into the public network instance's corresponding routing table, run the [**ip import-rib vpn-instance**](cmdqueryname=ip+import-rib+vpn-instance) *vpn-instance-name* **protocol** { **static** | **isis** *process-id* | **ospf** *process-id* } [ **valid-route** ] [ **route-policy** *route-policy-name* | **route-filter** *route-filter-name* ] command.
     + Configure the device to import BGP routes from a VPN instance into the public network instance's BGP routing table.
       1. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
       2. Run the [**ipv4-family**](cmdqueryname=ipv4-family) **unicast** command to enter the BGP-IPv4 unicast address family view.
       3. Run the [**import-rib vpn-instance**](cmdqueryname=import-rib+vpn-instance) *vpn-instance-name* [ **include-label-route** ] [ **valid-route** ] [ **route-policy** *route-policy-name* | **route-filter** *route-filter-name* ] command to configure the device to import BGP routes from a VPN instance to the public network instance's BGP routing table.
       4. Run the [**quit**](cmdqueryname=quit) command to return to the BGP view.
       5. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
  3. Configure the device to import different types of routes from the public network instance into a VPN instance's corresponding routing tables.
     
     
     + Configure the device to import direct routes, static routes, or IGP routes from the public network instance into a VPN instance's corresponding routing table.
       1. Run the [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name* command to create a VPN instance and enter the VPN instance view.
       2. Run the [**ipv4-family**](cmdqueryname=ipv4-family) command to enter the VPN instance IPv4 address family view.
       3. To configure the device to import direct routes, Vlink direct routes, IGP routes, or static routes from the public network instance into a VPN instance's corresponding routing table, run the [**import-rib**](cmdqueryname=import-rib) **public** **protocol** { **direct** | **vlink-direct-route** | { **static** | **isis** *process-id* | **ospf** *process-id* } [ **valid-route** ] } [ **route-policy** *route-policy-name* ] command.
     + Configure the device to import BGP routes from the public network instance into a VPN instance's BGP routing table.
       1. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
       2. Run the [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name* command to enter the BGP VPN instance IPv4 address family view.
       3. Run the [**import-rib**](cmdqueryname=import-rib) **public** [ **include-label-route** ] [ **valid-route** ] [ **route-policy** *route-policy-name* | **route-filter** *route-filter-name* ] command to configure the device to import BGP routes from the public network instance to a VPN instance's BGP routing table.
     + Configure the device to import BGP labeled routes from the public network instance's labeled address family to a VPN instance's BGP routing table.
       1. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
       2. Run the [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name* command to enter the BGP VPN instance IPv4 address family view.
       3. Run the [**import-rib public labeled-unicast**](cmdqueryname=import-rib+public+labeled-unicast) [ **valid-route** ] { **route-policy** *route-policy-name* | **route-filter** *route-filter-name* } command to configure the device to import BGP labeled routes from the public network instance's labeled address family to a VPN instance's BGP routing table.
     + Configure the device to import BGP labeled routes from the public network instance's labeled address family to a VPN instance's routing table for the BGP labeled address family.
       1. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
       2. Run the [**ipv4-labeled-unicast**](cmdqueryname=ipv4-labeled-unicast) **vpn-instance** *vpn-instance-name* command to enter the BGP labeled VPN instance IPv4 address family view.
       3. Run the [**import-rib public labeled-unicast**](cmdqueryname=import-rib+public+labeled-unicast) [ **valid-route** ] { **route-policy** *route-policy-name* | **route-filter** *route-filter-name* } command to configure the device to import BGP labeled routes from the public network instance's labeled address family to a VPN instance's routing table for the BGP labeled address family.
     + Configure the device to import BGP routes from the public network instance to a VPN instance's routing table for the BGP labeled address family.
       1. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
       2. Run the [**ipv4-labeled-unicast**](cmdqueryname=ipv4-labeled-unicast) **vpn-instance** *vpn-instance-name* command to enter the BGP labeled VPN instance IPv4 address family view.
       3. Run the [**import-rib**](cmdqueryname=import-rib) **public** [ **include-label-route** ] [ **valid-route** ] [ **route-policy** *route-policy-name* | **route-filter** *route-filter-name* ] command to configure the device to import BGP routes from the public network instance to a VPN instance's routing table for the BGP labeled address family.
  4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.