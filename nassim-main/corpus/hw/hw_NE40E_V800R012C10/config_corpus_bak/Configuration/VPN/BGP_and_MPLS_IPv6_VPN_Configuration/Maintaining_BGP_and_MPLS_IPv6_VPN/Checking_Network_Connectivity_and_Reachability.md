Checking Network Connectivity and Reachability
==============================================

This section describes how to use the **ping ipv6** command to check the network connectivity between the source and destination, and how to use the **tracert ipv6** command to check the devices through which data packets are sent from the source to the destination.

#### Procedure

* Run the [**ping ipv6**](cmdqueryname=ping+ipv6) command to check whether the IPv6 network between the source and destination is properly connected.
* Run the [**tracert ipv6**](cmdqueryname=tracert+ipv6) command to check the gateways through which the IPv6 packets are sent from the source to the destination.

#### Example

After completing IPv6 VPN configurations, run the [**ping ipv6**](cmdqueryname=ping+ipv6) command with [**ipv6 vpn-instance**](cmdqueryname=ipv6+vpn-instance) *vpn-instance-name* on a PE to check whether the PE can communicate with a CE in the same IPv6 VPN. If the ping fails, run the [**tracert ipv6**](cmdqueryname=tracert+ipv6) command with **vpn-instance** *vpn-instance-name* to locate the fault.

If multiple interfaces on a PE are bound to the same VPN instance enabled with an IPv6 address family, specify the source IP address when you ping the remote CE that accesses the peer PE. This means that the parameter **-a** *source-ipv6-address* needs to be specified in the [**ping ipv6**](cmdqueryname=ping+ipv6) command. If you do not specify a source IP address, the PE selects the address of its interface bound to the VPN instance as the source address of the ICMPv6 packet. If the CE does not have a route to the selected IPv6 address, the ICMPv6 packet sent back from the peer PE will be discarded.