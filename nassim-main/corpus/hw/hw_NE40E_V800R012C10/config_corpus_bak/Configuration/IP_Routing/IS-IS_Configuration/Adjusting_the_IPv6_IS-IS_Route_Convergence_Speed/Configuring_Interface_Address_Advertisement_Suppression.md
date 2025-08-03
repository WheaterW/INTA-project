Configuring Interface Address Advertisement Suppression
=======================================================

Interface address advertisement suppression ensures that interface addresses can be reused.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The IS-IS interface view is displayed.
3. Run [**isis ipv6 enable**](cmdqueryname=isis+ipv6+enable) [ *process-id* ]
   
   
   
   IPv6 is enabled for the IS-IS process.
4. Run [**isis ipv6 suppress-reachability**](cmdqueryname=isis+ipv6+suppress-reachability)
   
   
   
   The interface is suppressed from advertising interface addresses.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.