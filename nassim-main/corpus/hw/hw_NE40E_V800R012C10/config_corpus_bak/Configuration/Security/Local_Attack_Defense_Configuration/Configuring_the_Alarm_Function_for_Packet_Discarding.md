Configuring the Alarm Function for Packet Discarding
====================================================

You can set the interval for checking the number of discarded packets and the alarm threshold for the packet discarding rate.

#### Context

To view the status of a device that drops too many packets, configure the alarm function for packet discarding. When the alarm function is enabled, the Router checks the number of the packets dropped within a specified time period. If the number of dropped packets reaches or exceeds the set alarm threshold, an alarm is reported.

In VS mode, this feature is supported only by the admin VS.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**cpu-defend policy**](cmdqueryname=cpu-defend+policy) *policy-number*
   
   
   
   The attack defense policy view is displayed.
3. Run [**alarm drop-rate**](cmdqueryname=alarm+drop-rate+application-apperceive+blacklist+index+ma-defend) { **application-apperceive** | **blacklist** | **index** *index* | **ma-defend** | **tcpip-defend** | **tcpip-defend-v6** | **total-packet** | **user-defined-flow** *flow-id* | **whitelist** | **whitelist-v6** | **urpf** } **enable**
   
   
   
   The alarm for the discarding of the packets sent to the CPU is enabled.
4. Run [**alarm drop-rate**](cmdqueryname=alarm+drop-rate+application-apperceive+index+tcpip-defend) { **application-apperceive** | **index** *index* | **tcpip-defend** | **tcpip-defend-v6** | **user-defined-flow** *flow-id* | **whitelist** | **whitelist-v6** | **urpf** } { **threshold** *threshold-value* | **interval** *interval-value* | **speed-threshold** *speed-value* } \*
   
   
   
   The alarm threshold of discarding the packets to be sent to the CPU is set.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
   
   The configured alarm threshold and intervals still take effect after the [**undo alarm drop-rate enable**](cmdqueryname=undo+alarm+drop-rate+enable) and then [**alarm drop-rate enable**](cmdqueryname=alarm+drop-rate+enable) commands are used.