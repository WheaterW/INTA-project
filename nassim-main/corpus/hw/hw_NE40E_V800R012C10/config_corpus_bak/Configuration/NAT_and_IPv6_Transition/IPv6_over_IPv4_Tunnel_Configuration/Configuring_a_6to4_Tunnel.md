Configuring a 6to4 Tunnel
=========================

A 6to4 tunnel can interconnect isolated IPv6 networks through an IPv4 network.

#### Usage Scenario

To enable IPv6 networks to communicate with each other through an IPv4 network, configure IPv6 over IPv4 tunnels on the Routers where IPv6 networks border the IPv4 network.

6to4 tunnels use special 6to4 addresses that are in the format of 2002:a.b.c.d::/48, in which a.b.c.d represents the source address of the tunnel interface. During communication, the IPv4 address in a 6to4 address is used to encapsulate packets. The 6to4 tunnel does not need to be configured with a destination address.


#### Pre-configuration Tasks

Before configuring a 6to4 tunnel, complete the following tasks:

* Connect interfaces and configure physical parameters for the interfaces to ensure that the physical status of the interfaces is Up.
* Configure link layer protocol parameters for the interfaces to ensure that the link layer protocol status of the interfaces is Up.
* Configure the IPv4/IPv6 dual stack.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *interface-number*
   
   
   
   A tunnel interface is created.
3. Run [**tunnel-protocol**](cmdqueryname=tunnel-protocol) **ipv6-ipv4** **6to4**
   
   
   
   The tunnel mode is set to 6to4 tunnel mode.
4. Run [**source**](cmdqueryname=source) { *ip-address* | *interface-type interface-number* }
   
   
   
   The source address or source interface of the tunnel is specified.
5. Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
   
   
   
   IPv6 is configured on the interface.
6. Run [**ipv6 address**](cmdqueryname=ipv6+address) { *ipv6-address* *prefix-length* | *i**pv6-address-mask* }
   
   
   
   An IPv6 address is configured for the tunnel interface.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The IPv6 address prefix specified in this command must be the same as the prefix of the address of the 6to4 network where the border Router resides.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Checking the Configurations

After configuring a 6to4 tunnel, check the configurations.

* Run the [**display ipv6 interface tunnel**](cmdqueryname=display+ipv6+interface+tunnel) *interface-number* command to check the IPv6 configuration of a tunnel interface.