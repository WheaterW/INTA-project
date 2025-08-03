Configuring a Global Unicast Address for an Interface
=====================================================

Global unicast addresses function the same as public IPv4 addresses. They are used for links whose route prefixes can be aggregated, reducing the number of routing entries.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
   
   
   
   IPv6 is enabled for the interface.
4. Run [**ipv6 address**](cmdqueryname=ipv6+address+tag) { *ipv6-address* *prefix-length* | *ipv6-address/prefix-length* } [ **tag** *tag-value* ] or [**ipv6 address**](cmdqueryname=ipv6+address+eui-64+tag) { *ipv6-address* *prefix-length* | *ipv6-address/prefix-length* } **eui-64** [ **tag** *tag-value* ]
   
   
   
   A global unicast address is configured for the interface.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.