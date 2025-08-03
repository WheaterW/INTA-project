Configuring an IPv6 Multicast Forwarding Boundary
=================================================

After an interface is configured with a forwarding boundary for a specific group, the interface does not forward or receive any IPv6 multicast packet for this group.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The IPv6 PIM interface view is displayed.
3. Run [**multicast ipv6 boundary**](cmdqueryname=multicast+ipv6+boundary) *ipv6-group-address* *ipv6-group-mask-length*
   
   
   
   An IPv6 multicast forwarding boundary is configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Checking the Configurations

Run the [**display multicast ipv6 boundary**](cmdqueryname=display+multicast+ipv6+boundary) [ *ipv6-group-address* [ *ipv6-group-mask-length* ] ] [ **interface** *interface-type* *interface-number* ] command to check information about the multicast boundaries configured on all the interfaces of a device.