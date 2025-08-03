(Optional) Configuring IPv6 VXLAN Gateways to Advertise Specific Types of Routes
================================================================================

To enable communication between VMs on different subnets, configure IPv6 VXLAN gateways to exchange IRB or IP prefix routes. This configuration enables the gateways to learn the IP routes of the related hosts or the subnets where the hosts reside.

#### Context

By default, IPv6 VXLAN gateways can exchange MAC routes, but must be configured to exchange IRB or IP prefix routes if VMs need to communicate across different subnets. If an RR is deployed on the network, IRB or IP prefix routes must be exchanged only between the VXLAN gateways and RR.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Host routes can be advertised through IRB routes (recommended), IP prefix routes, or both. In contrast, subnet routes of hosts can be advertised only through IP prefix routes.



#### Procedure

* Configure IRB route advertisement.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
     
     
     
     The BGP-EVPN address family view is displayed.
  4. Run either of the following commands based on the overlay network type to configure IRB route advertisement:
     
     
     + For an IPv4 overlay network, run the [**peer**](cmdqueryname=peer+advertise+%28BGP-EVPN+address+family+view%29) { *ipv6-address* | *group-name* } **advertise** **irb** command.
     + For an IPv6 overlay network, run the [**peer**](cmdqueryname=peer+advertise+%28BGP-EVPN+address+family+view%29) { *ipv6-address* | *group-name* } **advertise** **irbv6** command.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure IP prefix route advertisement.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run either of the following commands based on the overlay network type:
     
     
     + For an IPv4 overlay network, run the [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name* command to enter the BGP-VPN instance IPv4 address family view.
     + For an IPv6 overlay network, run the [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name* command to enter the BGP-VPN instance IPv6 address family view.
  4. Run either of the following commands based on the overlay network type:
     
     
     + For an IPv4 overlay network, run the [**import-route**](cmdqueryname=import-route) { **direct** | **isis** *process-id* | **ospf** *process-id* | **rip** *process-id* | **static** } [ **med** *med* | **route-policy** *route-policy-name* ] \* command to import routes of other protocols to the BGP-VPN instance IPv4 address family.
     + For an IPv6 overlay network, run the [**import-route**](cmdqueryname=import-route) { **direct** | **isis** *process-id* | **ospfv3** *process-id* | **ripng** *process-id* | **static** } [ **med** *med* | **route-policy** *route-policy-name* ] \* command to import routes of other protocols to the BGP-VPN instance IPv6 address family.
     
     To advertise host IP routes, configure import of direct routes. To advertise the route of a subnet where hosts reside, configure a dynamic routing protocol (such as OSPF or OSPFv3) and then run one of the preceding commands based on the overlay network type to import the route into the dynamic routing protocol.
  5. Run [**advertise l2vpn evpn**](cmdqueryname=advertise+l2vpn+evpn)
     
     
     
     IP prefix route advertisement is configured.
     
     
     
     IP prefix routes are used to advertise host IP routes as well as the route of the subnet where the hosts reside. If many specific host routes exist, a VXLAN gateway can be configured to advertise an IP prefix route, which carries the routing information of the subnet where the hosts reside. After route advertisement, import the route to the target BGP-VPN instance address family. This reduces the number of routes to be saved on the involved VXLAN gateway.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + A VXLAN gateway can advertise subnet routes only if the subnets attached to the gateway are unique on the entire network.
     + After IP prefix route advertisement is configured, run the [**arp vlink-direct-route advertise**](cmdqueryname=arp+vlink-direct-route+advertise) or [**nd vlink-direct-route advertise**](cmdqueryname=nd+vlink-direct-route+advertise) command to advertise host routes. After this configuration, VM migration is restricted.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.