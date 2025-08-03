Configuring an IPv6 Anycast Address for an Interface
====================================================

An anycast address is used to identify a group of interfaces.

#### Context

Anycast addresses and unicast addresses are in the same address range. An anycast address is used to identify a group of interfaces on different nodes.

* Similar to a multicast address, an anycast address is listened to by multiple nodes. Therefore, it is only used as a destination address.
* The packets destined for an anycast address are transmitted to an interface that is in the interface group identified by the anycast address and is closest to the source node. (The distance between an interface and the source node is calculated based on the routing protocol). The packets destined for a multicast address are transmitted to a group of interfaces with the multicast address.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
   
   
   
   IPv6 is enabled for the interface.
4. Run [**ipv6 address**](cmdqueryname=ipv6+address) { *ipv6-address* *prefix-length* | *ipv6-address/prefix-length* } **anycast** [ **tag** *tag-value* ]
   
   
   
   An IPv6 anycast address is configured for the interface.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.