Configuring an Interval for Updating Interface Statistics in the Cache
======================================================================

By configuring an interval for updating interface statistics in the cache, you can ensure that the cache holds the latest statistics.

#### Usage Scenario

An NMS can obtain interface statistics in get-next or get mode. In get-next mode, a device receives a request for interface statistics from the NMS, obtains the interface statistics from the cache, and then reports the statistics to the NMS. By default, the interval for updating statistics in the cache is 50 seconds.

When obtaining statistics on packets received or sent on an interface through the ifTable and ifXTable objects in the MIB table, you can reduce the interval for updating interface statistics in the cache to ensure that the cache holds the latest statistics.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**snmp-agent**](cmdqueryname=snmp-agent)
   
   
   
   The SNMP agent is enabled.
3. Run [**snmp-agent get-next-cache if-mib age-time**](cmdqueryname=snmp-agent+get-next-cache+if-mib+age-time) *time-value*
   
   
   
   An interval for updating interface statistics in the cache is configured in scenarios where an NMS obtains the statistics in get-next mode.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.