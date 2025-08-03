Configuring Route Import Between VPN Instances
==============================================

Route import between VPN instances enables users in different VPNs to communicate.

#### Context

The following steps must be performed for all target VPN instances.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If you do not want a VPN instance to change the next hops of routes imported from the public network instance or other VPN instances when advertising these routes to its IBGP peers, run the [**import-rib route next-hop-invariable**](cmdqueryname=import-rib+route+next-hop-invariable) command for the VPN instance.



#### Procedure

* Configure the device to import direct routes, static routes, or IGP routes from one VPN instance into another VPN instance's corresponding routing table.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name* command to create a VPN instance and enter the VPN instance view.
  3. Run the [**ipv4-family**](cmdqueryname=ipv4-family) command to enter the VPN instance IPv4 address family view.
  4. Run the [**import-rib**](cmdqueryname=import-rib) **vpn-instance** *vpn-instance-name* **protocol** { **direct** | **vlink-direct-route** | { **static** | **isis** *process-id* | **ospf** *process-id* } [ **valid-route** ] } [ **route-policy** *route-policy-name* | **route-filter** *route-filter-name* ] command to import direct routes, Vlink direct routes, IGP routes, or static routes from the current VPN instance into a specified VPN instance's corresponding routing table.
  5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure the device to import BGP routes from another VPN instance to the specified VPN instance's BGP routing table for the BGP VPN instance IPv4 address family.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
  3. Run the [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name* command to enter the BGP VPN instance IPv4 address family view.
  4. Run the [**import-rib**](cmdqueryname=import-rib) { **vpn-instance** *vpn-instance-name* } [ **include-label-route** ] [ **valid-route** ] [ **route-policy** *route-policy-name* | **route-filter** *route-filter-name* ] command to configure the device to import BGP routes from another VPN instance to the specified VPN instance's BGP routing table for the BGP VPN instance IPv4 address family.
  5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure the device to import BGP labeled routes from a VPN instance's labeled address family to the specified VPN instance's BGP routing table.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
  3. Run the [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name* command to enter the BGP VPN instance IPv4 address family view.
  4. Run the [**import-rib vpn-instance**](cmdqueryname=import-rib+vpn-instance) *vpn-instance-name* **labeled-unicast** [ **valid-route** ] { **route-policy** *route-policy-name* | **route-filter** *route-filter-name* } command to enable the device to import BGP labeled routes from the VPN instance's labeled address family to another VPN instance's BGP routing table.
  5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure the device to import BGP labeled routes from a VPN instance's labeled address family to the specified VPN instance's routing table for the BGP labeled address family.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
  3. Run the [**ipv4-labeled-unicast**](cmdqueryname=ipv4-labeled-unicast) **vpn-instance** *vpn-instance-name* command to enter the BGP labeled VPN instance IPv4 address family view.
  4. Run the [**import-rib vpn-instance**](cmdqueryname=import-rib+vpn-instance) *vpn-instance-name* **labeled-unicast** [ **valid-route** ] { **route-policy** *route-policy-name* | **route-filter** *route-filter-name* } command to configure the device to import BGP labeled routes from a VPN instance's labeled address family to the specified VPN instance's routing table for the BGP labeled address family.
  5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure the device to import BGP routes from another VPN instance to the specified VPN instance's routing table for the BGP labeled address family.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
  3. Run the [**ipv4-labeled-unicast**](cmdqueryname=ipv4-labeled-unicast) **vpn-instance** *vpn-instance-name* command to enter the BGP labeled VPN instance IPv4 address family view.
  4. Run the [**import-rib**](cmdqueryname=import-rib) **vpn-instance** *vpn-instance-name* [ **include-label-route** ] [ **valid-route** ] [ **route-policy** *route-policy-name* | **route-filter** *route-filter-name* ] command to configure the device to import BGP routes from another VPN instance into the specified VPN instance's routing table for the BGP labeled address family.
  5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.