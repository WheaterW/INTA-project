(Optional) Configuring an Aging Time for ND Entries in the Incomplete State
===========================================================================

Configuring a short aging time for ND entries in the Incomplete state can speed up their aging.

#### Context

By default, ND probe is performed for ND entries in the Incomplete state. The status of an ND entry changes to Reachable when a neighbor is reachable. The local device ages out an ND entry after failing to receive a response to a probe packet from the peer device within a specified number of probes. If the rate at which NS messages are sent is limited, ND entries in the Incomplete state cannot be effectively probed for a long time, occupying entry resources. To speed up entry aging and release entry resources, configure a short aging time for ND entries in the Incomplete state.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
   
   
   
   IPv6 is enabled.
4. Run [**ipv6 nd neighbor-incomplete expire-time**](cmdqueryname=ipv6+nd+neighbor-incomplete+expire-time) *expire-time-value*
   
   
   
   An aging time is configured for ND entries in the Incomplete state.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.