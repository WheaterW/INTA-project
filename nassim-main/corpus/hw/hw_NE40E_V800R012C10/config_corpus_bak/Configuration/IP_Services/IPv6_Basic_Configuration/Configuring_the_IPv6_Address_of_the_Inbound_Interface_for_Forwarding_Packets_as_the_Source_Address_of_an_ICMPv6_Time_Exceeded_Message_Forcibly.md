Configuring the IPv6 Address of the Inbound Interface for Forwarding Packets as the Source Address of an ICMPv6 Time Exceeded Message Forcibly
==============================================================================================================================================

To easily observe the inbound interface of a device along the path, you can configure the IPv6 address of the inbound interface for forwarding packets as the source address of an ICMPv6 Time Exceeded message.

#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**ipv6 icmp hop-limit-exceeded source-address ingress-interface**](cmdqueryname=ipv6+icmp+hop-limit-exceeded+source-address+ingress-interface) command to forcibly configure the IPv6 address of the inbound interface for forwarding packets as the source address of an ICMPv6 Time Exceeded message.
3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.