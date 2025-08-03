Configuring a Manual IPv6 over IPv4 Tunnel
==========================================

A manual IPv6 over IPv4 tunnel is a P2P tunnel. The source address and destination address of a manual IPv6 over IPv4 tunnel are both manually assigned and must be unique on the same device. A manual IPv6 over IPv4 tunnel acts as a permanent link that connects two IPv6 networks across an IPv4 network. Border Routers can communicate with each other securely and regularly through manual IPv6 over IPv4 tunnels.

#### Usage Scenario

To enable IPv6 networks to communicate with each other through an IPv4 network, configure IPv6 over IPv4 tunnels on the Routers where IPv6 networks border an IPv4 network.

A manual IPv6 over IPv4 tunnel can be established between two border Routers to provide a stable connection for separated IPv6 networks. It can also be established between a terminal system and a border Router to provide a connection for the terminal system to access an IPv6 network. The devices at the two ends of an IPv6 over IPv4 tunnel must support the IPv4/IPv6 dual stack. The intermediate devices do not need to support the IPv4/IPv6 dual stack. You can configure multiple manual IPv6 over IPv4 tunnels on the border Router to communicate with multiple IPv6 networks.


#### Pre-configuration Tasks

Before configuring a manual IPv6 over IPv4 tunnel, complete the following tasks:

* Connect interfaces and configure physical parameters for the interfaces to ensure that the physical status of the interfaces is Up.
* Configure link layer protocol parameters for the interfaces to ensure that the link layer protocol status of the interfaces is Up.
* Assign an IPv4 address to each border Router.
* Configure IPv6 globally and on interfaces.
* Assign an IPv6 address to each border Router.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *interface-number*
   
   
   
   A tunnel interface is created.
3. Run [**tunnel-protocol**](cmdqueryname=tunnel-protocol) **ipv6-ipv4**
   
   
   
   The tunnel mode is set to manual IPv6 over IPv4 tunnel mode.
4. Run [**source**](cmdqueryname=source) { *ip-address* | *interface-type* *interface-number* }
   
   
   
   A source address or source interface is specified for the tunnel.
5. Run [**destination**](cmdqueryname=destination) *ip-address*
   
   
   
   A destination address is specified for the tunnel.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The destination address of an IPv6 over IPv4 tunnel can be a physical or loopback interface address.
6. Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
   
   
   
   IPv6 is configured on the interface.
7. Run [**ipv6 address**](cmdqueryname=ipv6+address) { *ipv6-address* *prefix-length* | *ipv6-address/prefix-length* }
   
   
   
   An IPv6 address is configured for the tunnel interface.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After configuring a manual IPv6 over IPv4 tunnel, verify the configuration.

* Run the [**display ipv6 interface tunnel**](cmdqueryname=display+ipv6+interface+tunnel) *interface-number* command to check the IPv6 configuration of a tunnel interface.