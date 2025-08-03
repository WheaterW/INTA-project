Configuring a Layer 3 VXLAN Gateway
===================================

To enable communication between VMs on different subnets, configure Layer 3 gateways on the VXLAN, enable the distributed gateway function, and configure host route advertisement.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) **vbdif** *bd-id*
   
   
   
   A VBDIF interface is created, and its view is displayed.
3. Run [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) *vpn-instance-name*
   
   
   
   The VBDIF interface is bound to a VPN instance.
4. Configure an IP address for the VBDIF interface to implement Layer 3 communication.
   * For an IPv4 overlay network, run the [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } [ **sub** ] command to configure an IPv4 address.
   * For an IPv6 overlay network, perform the following operations:
     1. Run the [**ipv6 enable**](cmdqueryname=ipv6+enable) command to enable the IPv6 function for the interface.
     2. Run the [**ipv6 address**](cmdqueryname=ipv6+address) { *ipv6-address* *prefix-length* | *ipv6-address*/*prefix-length* } or [**ipv6 address**](cmdqueryname=ipv6+address) { *ipv6-address* *prefix-length* | *ipv6-address*/*prefix-length* } **eui-64** command to configure a global unicast address for the interface.
5. (Optional) Run [**bandwidth**](cmdqueryname=bandwidth) *bandwidth*
   
   
   
   Bandwidth is configured for the VBDIF interface.
6. (Optional) Run [**mac-address**](cmdqueryname=mac-address) *mac-address*
   
   
   
   A MAC address is configured for the VBDIF interface.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If VMs on the same network segment connect to different Layer 3 gateways on a VXLAN, the VBDIF interfaces of the Layer 3 gateways must have the same IP address and same MAC address configured. In this way, the configurations of the Layer 3 gateways do not need to be changed when the VMs' locations are changed, reducing the maintenance workload.
7. Run [**vxlan anycast-gateway enable**](cmdqueryname=vxlan+anycast-gateway+enable)
   
   
   
   The distributed gateway function is enabled.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After the distributed gateway function is enabled, the gateway discards network-side ARP or NS messages and learns only those from the user side.
8. Perform one of the following steps to configure host route advertisement.
   
   
   
   **Table 1** Configuring host route advertisement
   | Overlay Network Type | Type of Route to Be Advertised Between Gateways | Host Route Advertisement Configuration |
   | --- | --- | --- |
   | IPv4 | IRB route | Run the [**arp collect host enable**](cmdqueryname=arp+collect+host+enable) command in the VBDIF interface view. |
   | IP prefix route | Run the [**arp vlink-direct-route advertise**](cmdqueryname=arp+vlink-direct-route+advertise) [ **route-policy** *route-policy-name* | **route-filter** *route-filter-name* ] command in the IPv4 address family view of the VPN instance to which the VBDIF interface is bound. |
   | IPv6 | IRB route | Run the [**ipv6 nd collect host enable**](cmdqueryname=ipv6+nd+collect+host+enable) command in the VBDIF interface view. |
   | IP prefix route | Run the [**nd vlink-direct-route advertise**](cmdqueryname=nd+vlink-direct-route+advertise) [ **route-policy** *route-policy-name* | **route-filter** *route-filter-name* ] command in the IPv6 address family view of the VPN instance to which the VBDIF interface is bound. |
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.