(Optional) Configuring RA Message Advertisement Intervals
=========================================================

You can set a smaller RA message advertisement interval to speed up the RA process.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run **ipv6 enable**
   
   
   
   IPv6 is enabled.
4. Run [**ipv6 nd ra**](cmdqueryname=ipv6+nd+ra) { **max-interval** *maximum-interval* | **min-interval** *minimum-interval* }
   
   
   
   RA message advertisement intervals are configured.
   
   
   
   The maximum interval cannot be shorter than 4/3 of the minimum interval.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.