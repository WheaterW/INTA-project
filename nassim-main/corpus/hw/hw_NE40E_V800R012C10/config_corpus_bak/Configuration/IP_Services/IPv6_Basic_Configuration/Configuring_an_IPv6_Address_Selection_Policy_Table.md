Configuring an IPv6 Address Selection Policy Table
==================================================

If multiple addresses are configured on an interface of the device, the IPv6 address selection policy table can be used to select source and destination addresses for packets.

#### Context

IPv6 addresses can be classified into different types based on different applications.

* Link local addresses and global unicast addresses based on the effective range of the IPv6 addresses
* Temporary addresses and public addresses based on security levels
* Home addresses and care-of addresses based on the application in the mobile IPv6 field
* Physical interface addresses and logical interface addresses based on the interface attributes

The preceding IPv6 addresses can be configured on the same interface of the Router. In this case, the device must select a source address or a destination addresses from multiple addresses on the interface. If the device supports the IPv4/IPv6 dual-stack, it also must select IPv4 addresses or IPv6 addresses for communication. For example, if a domain name maps both an IPv4 address and an IPv6 address, the system must select an address to respond to the DNS request of the client.

An IPv6 address selection policy table solves the preceding problems. It defines a group of address selection rules. The source and destination addresses of packets can be specified or planned based on these rules. This table, similar to a routing table, can be queried by using the longest matching rule. The address is selected based on the source and destination addresses.

* The *label* parameter can be used to determine the result of source address selection. The address whose *label* value is the same as the *label* value of the destination address is selected preferably as the source address.
* The destination address is selected based on both the *label* and the *precedence* parameters. If *label* values of the candidate addresses are the same, the address whose *precedence* value is largest is selected preferably as the destination address.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ipv6 address-policy**](cmdqueryname=ipv6+address-policy+vpn-instance) [ **vpn-instance** *vpn-instance-name* ] *ipv6-address* *prefix-length* *precedence* *label*
   
   
   
   The source or destination address selection policies are configured.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration of an IPv6 Address Selection Policy Table

After configuring an IPv6 address selection policy table, verify the configuration.

* Run the [**display ipv6 address-policy**](cmdqueryname=display+ipv6+address-policy+vpn-instance+all) [ **vpn-instance** *vpn-instance-name* ] { **all** | *ipv6-address* *prefix-length* } command to check the IPv6 address selection policy entry information.