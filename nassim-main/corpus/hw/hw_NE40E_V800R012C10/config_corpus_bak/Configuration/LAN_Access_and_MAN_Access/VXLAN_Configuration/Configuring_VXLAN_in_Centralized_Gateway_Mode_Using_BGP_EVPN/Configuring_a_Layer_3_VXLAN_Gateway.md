Configuring a Layer 3 VXLAN Gateway
===================================

To allow users on different network segments to communicate, a Layer 3 VXLAN gateway must be deployed, and the default gateway address of the users must be the IP address of the VBDIF interface of the Layer 3 gateway.

#### Context

A tenant is identified by a VNI. VNIs can be mapped to BDs in 1:1 mode so that a BD can function as a VXLAN network entity to transmit VXLAN data packets. A VBDIF interface is a Layer 3 logical interface created for a BD. After an IP address is configured for a VBDIF interface of a BD, the VBDIF interface can function as the gateway for tenants in the BD for Layer 3 forwarding. VBDIF interfaces allow Layer 3 communication between VXLANs on different network segments and between VXLANs and non-VXLANs, and implement Layer 2 network access to a Layer 3 network.

VBDIF interfaces are configured on Layer 3 VXLAN gateways for inter-segment communication, and are not needed in the case of intra-segment communication.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The DHCP relay function can be configured on the VBDIF interface so that hosts can request IP addresses from the external DHCP server.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) **vbdif** *bd-id*
   
   
   
   A VBDIF interface is created, and its view is displayed.
3. Configure an IP address for the VBDIF interface to implement Layer 3 interworking.
   * On IPv4 overlay networks, run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } [ **sub** ].
     
     An IPv4 address is configured.
   * On IPv6 overlay networks, perform the following operations:
     1. Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
        
        IPv6 is enabled for the interface.
     2. Run [**ipv6 address**](cmdqueryname=ipv6+address) { *ipv6-address* *prefix-length* | *ipv6-address*/*prefix-length* }
        
        Or, [**ipv6 address**](cmdqueryname=ipv6+address) { *ipv6-address* *prefix-length* | *ipv6-address*/*prefix-length* } **eui-64**
        
        A global unicast address is configured for the interface.
4. (Optional) Run [**mac-address**](cmdqueryname=mac-address) *mac-address*
   
   
   
   A MAC address is configured for the VBDIF interface.
5. (Optional) Run [**bandwidth**](cmdqueryname=bandwidth) *bandwidth*
   
   
   
   Bandwidth is configured for the VBDIF interface.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.