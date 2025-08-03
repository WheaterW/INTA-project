Configuring a Layer 3 IPv6 VXLAN Gateway
========================================

To allow users on different network segments to communicate, deploy a Layer 3 gateway and specify the IP address of its VBDIF interface as the default gateway address of the users.

#### Context

On an IPv6 VXLAN, a BD can be mapped to a VNI (identifying a tenant) in 1:1 mode to transmit VXLAN data packets. VBDIF interfaces, which are Layer 3 logical interfaces created for a BD, can be used to implement communication between VXLANs on different network segments or between VXLANs and non-VXLANs, or they can be used for Layer 2 network access to a Layer 3 network. Each BD corresponds to a VBDIF interface. After an IP address is configured for a VBDIF interface, the interface functions as the gateway for tenants in the BD to forward packets at Layer 3 based on IP addresses.

A VBDIF interface needs to be configured on the Layer 3 gateway of an IPv6 VXLAN for communication between different network segments only; it is not needed for communication on the same network segment.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The DHCP relay function can be configured on a VBDIF interface so that hosts can request IP addresses from an external DHCP server.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) **vbdif** *bd-id*
   
   
   
   A VBDIF interface is created, and its view is displayed.
3. Configure an IP address for the VBDIF interface to implement Layer 3 interworking.
   * For an IPv4 overlay network, run the [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } [ **sub** ] command to configure an IPv4 address for the VBDIF interface.
   * For an IPv6 overlay network, perform the following operations:
     1. Run the [**ipv6 enable**](cmdqueryname=ipv6+enable) command to enable the IPv6 function for the interface.
     2. Run the [**ipv6 address**](cmdqueryname=ipv6+address) { *ipv6-address* *prefix-length* | *ipv6-address*/*prefix-length* } or [**ipv6 address**](cmdqueryname=ipv6+address) { *ipv6-address* *prefix-length* | *ipv6-address*/*prefix-length* } **eui-64** command to configure a global unicast address for the interface.
4. (Optional) Run [**mac-address**](cmdqueryname=mac-address) *mac-address*
   
   
   
   A MAC address is configured for the VBDIF interface.
5. (Optional) Run [**bandwidth**](cmdqueryname=bandwidth) *bandwidth*
   
   
   
   Bandwidth is configured for the VBDIF interface.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

Configure a static route to the IP address of the VBDIF interface, or configure a dynamic routing protocol to advertise this IP address, so that Layer 3 connectivity can be achieved on the overlay network.