Configuring the Number of DAD Attempts
======================================

A device can send NS messages to detect whether the IPv6 address to be configured is being used by another device. The number of DAD attempts refers to the number of times NS messages are sent. DAD is similar to gratuitous ARP in IPv4, but implemented using NS and NA messages.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of the interface on which the number of DAD attempts needs to be configured is displayed.
3. Run **ipv6 enable**
   
   
   
   IPv6 is enabled.
4. Run [**ipv6 nd dad attempts**](cmdqueryname=ipv6+nd+dad+attempts) *value*
   
   
   
   The number of DAD attempts is configured.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.