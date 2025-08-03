Configuring the IPv4/IPv6 Dual Stack
====================================

The IPv4/IPv6 dual stack needs to be configured on the Router at the edge of an IPv6 network and an IPv4 network.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* }
   
   
   
   An IPv4 address is configured for the interface.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
5. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The interface view is displayed.
6. Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
   
   
   
   IPv6 is enabled on the interface.
7. Run [**ipv6 address**](cmdqueryname=ipv6+address+eui-64) { *ipv6-address prefix-length* | *ipv6-address* | *prefix-length* } **eui-64** or [**ipv6 address**](cmdqueryname=ipv6+address) { *ipv6-address prefix-length* | *ipv6-address* | *prefix-length* }
   
   
   
   An IPv6 address is configured for the interface.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.