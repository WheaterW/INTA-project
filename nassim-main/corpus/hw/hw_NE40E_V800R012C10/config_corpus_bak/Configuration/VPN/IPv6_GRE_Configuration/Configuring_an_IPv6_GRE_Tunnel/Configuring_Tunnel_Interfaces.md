Configuring Tunnel Interfaces
=============================

After creating a tunnel interface, you need to specify IPv6 GRE as the encapsulation type and configure a source address and a destination address for the tunnel interface. To enable the tunnel to support dynamic routing protocols, you aso need to configure an IP address for the tunnel interface.

#### Context

An IPv6 GRE tunnel is established between tunnel interfaces on the two ends of the tunnel. Therefore, you need to configure tunnel interfaces on devices at the two ends of the tunnel. For an IPv6 GRE tunnel interface, you need to specify the protocol type as IPv6 GRE and configure a source address or source interface and a destination address for the tunnel interface. To enable a tunnel to support routes, you also need to configure a network address for the tunnel interface.

A tunnel interface, which is a logical interface, goes down in any of the following situations:

* The destination address configured for the tunnel interface is unreachable or is set to the IP address of the tunnel interface.
* The source interface configured for the tunnel interface is down.
* The IP address configured on the tunnel interface is invalid.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If the tunnel interface is deleted, all configurations on the tunnel interface are also deleted.

Perform the following steps on the endpoint Routers of a tunnel.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**interface tunnel**](cmdqueryname=interface+tunnel) *interface-number* command to create a tunnel interface and enter its view.
3. Run the [**tunnel-protocol**](cmdqueryname=tunnel-protocol) **gre ipv6** command to encapsulate the tunnel with IPv6 GRE.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Changing, deleting, or initially configuring the tunnel mode of a tunnel interface will delete all tunnel-related configurations on the interface, such as the MTU. Exercise caution when performing this operation.
4. Run the [**source**](cmdqueryname=source) { *ipv6-address* | *ifName* | *ifTypeifNum* } command to configure a source address or source interface for the tunnel interface.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The [**binding tunnel gre**](cmdqueryname=binding+tunnel+gre) command needs to be run to bind GRE to the source interface or the interface where the source address resides. The GRE tunnel can use these interfaces to transmit GRE-encapsulated packets only after GRE is bound to them.
5. Run the [**destination**](cmdqueryname=destination) [ **vpn-instance** *vpn-instance-name* ] *des-ipv6-address* command to configure a destination address for the tunnel interface.
6. Run the [**ipv6 address**](cmdqueryname=ipv6+address) { *ipv6-address prefix-length* | *ipv6-address/prefix-length* } command to configure an IPv6 address for the tunnel interface.
   
   
   
   To enable a tunnel to support routes, you also need to configure a network address for the tunnel interface. The IP addresses of the tunnel interfaces on both ends of the GRE tunnel can be either public or private addresses and must be on the same network segment.
7. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.