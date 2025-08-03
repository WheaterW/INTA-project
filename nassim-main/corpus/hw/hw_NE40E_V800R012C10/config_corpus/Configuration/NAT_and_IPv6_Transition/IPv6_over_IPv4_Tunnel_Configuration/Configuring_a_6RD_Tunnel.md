Configuring a 6RD Tunnel
========================

A 6RD tunnel is a point-to-multipoint (P2MP) tunnel that connects IPv6 sites through a carrier's IPv4 network. 6RD tunnels have been widely deployed on carriers' networks.

#### Usage Scenario

A 6RD tunnel is a P2MP tunnel and is an enhancement to the 6to4 solution. 6RD tunneling allows carriers to use one of their own IPv6 prefixes as the 6RD prefix, mitigating the IPv4 address shortage of the 6to4 solution.

6RD is used in the following scenarios:

* 6RD domain-6RD domain
  
  Connects different 6RD domains. 6RD CEs are deployed at either end of a tunnel, which enables hosts or devices in different 6RD domains to communicate with each other.
* 6RD domain-IPv6 network
  
  Connects a 6RD domain to a native IPv6 network. A 6RD CE and a 6RD BR are deployed at either end of a tunnel, which enables hosts or devices in the 6RD domain and on the IPv6 network to access each other.
#### Pre-configuration Tasks

Before configuring a 6RD tunnel, complete the following tasks:

* Connect interfaces and set their physical parameters to ensure that the physical status of the interfaces is Up.
* Configure link-layer protocol parameters for interfaces to go Up at the link layer.
* Ensure reachable routes between the source and destination interfaces.
* Enable IPv4/IPv6 dual stack on the interfaces.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *interface-number*
   
   
   
   A tunnel interface is created, and the tunnel interface view is displayed.
3. Run [**tunnel-protocol**](cmdqueryname=tunnel-protocol) **ipv6-ipv4** **6rd**
   
   
   
   The tunnel encapsulation mode is set to 6RD.
4. Run [**source**](cmdqueryname=source) { *ip-address* | *interface-type interface-number* }
   
   
   
   The source address or source interface is specified for the 6RD tunnel interface.
5. Run [**ipv6-prefix**](cmdqueryname=ipv6-prefix) { *ipv6-address* *prefix-length* | *i**pv6-prefix-mask* }
   
   
   
   The 6RD prefix and 6RD prefix length are configured.
   
   
   
   A 6RD prefix is the IPv6 prefix assigned by a carrier for a 6RD address. The 6RD delegated prefix is calculated by combining the 6RD prefix and part or all bits of an IPv4 address. The 6RD delegated prefix is used to assign IPv6 address prefixes to devices or hosts in a 6RD domain.
   
   The 6RD prefix for each 6RD domain must be unique.
6. Run [**ipv4-prefix length**](cmdqueryname=ipv4-prefix+length) *ipv4-prefix-length*
   
   
   
   The IPv4 prefix length of the 6RD tunnel is configured.
   
   
   
   The IPv4 prefix length indicates the number of high-order bits to be deleted from the source tunnel address (an IPv4 address). The remaining bits of the IPv4 address and the 6RD prefix together form the 6RD delegated prefix.
   
   You are advised to set *ipv4-prefix-length* to 0 when the carrier network is an IPv4 network. On an IPv4 carrier network, the source tunnel address is entirely embedded in the 6RD delegated prefix, which is used to search for the destination tunnel address.
   
   The IPv4 prefix length of the 6RD tunnel in each 6RD domain must be unique.
   
   The 6RD delegated prefix can be automatically calculated based on the configured source tunnel address or source interface, 6RD prefix, IPv6 prefix length, and IPv4 prefix length. You can run the [**display this interface**](cmdqueryname=display+this+interface) command in the tunnel interface view to check the calculated 6RD delegated prefix.
7. Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
   
   
   
   IPv6 is enabled on the interface.
8. Run [**ipv6 address**](cmdqueryname=ipv6+address) { *ipv6-address prefix-length* | *i**pv6-address-mask* }
   
   
   
   An IPv6 address is configured for the tunnel interface, and the address prefix is the 6RD delegated prefix.
9. (Optional) Run [**border-relay address**](cmdqueryname=border-relay+address) *br-ipv4-address* The IPv4 address of the 6RD BR is configured.
   
   
   
   The IPv4 address of the 6RD BR needs to be configured on a 6RD CE only in a relay scenario where a 6RD domain interworks with a native IPv6 network.

#### Verify the configuration.

After configuring the 6RD tunnel, check the configurations.

Run the [**display ipv6 interface tunnel**](cmdqueryname=display+ipv6+interface+tunnel) *interface-number* command to check the IPv6 attribute on the tunnel interface.