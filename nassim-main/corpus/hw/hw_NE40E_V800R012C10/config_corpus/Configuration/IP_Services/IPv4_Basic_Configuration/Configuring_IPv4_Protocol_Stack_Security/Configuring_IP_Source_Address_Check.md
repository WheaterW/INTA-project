Configuring IP Source Address Check
===================================

This section describes how to configure IP source address check to prevent routers from network attacks.

#### Usage Scenario

By default, an interface does not perform source address validity check on the received packets. The reason for this is that broadcast or multicast addresses may be used as the source address in actual situations. However, hackers may use a broadcast or multicast address as the source address to launch a network attack. You can enable source address validity check to filter this type of illegitimate packets with the purpose of improving device security.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ip verify source-address**](cmdqueryname=ip+verify+source-address)
   
   
   
   Source address validity check is enabled on the interface, and the interface will drop packets with an illegitimate source address.