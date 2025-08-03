(Optional) Configuring a Neighbor Reachability Detection Interval
=================================================================

A device can send NS messages to detect whether its neighbors are reachable. Therefore, you can set the NS message transmission interval to control the neighbor reachability detection frequency. Frequent NS message transmissions help rapidly determine whether neighbors are reachable, but also affect system performance. Therefore, it is recommended that the interval not be set too short.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. (Optional) Run [**ipv6 nd pre-detect**](cmdqueryname=ipv6+nd+pre-detect)
   
   
   
   The pre-detection of ND entries is enabled.
3. (Optional) Run [**ipv6 nd auto-detect enable**](cmdqueryname=ipv6+nd+auto-detect+enable)
   
   
   
   The auto-detection of ND entries is enabled.
4. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
5. Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
   
   
   
   IPv6 is enabled.
6. Run [**ipv6 nd ns retrans-timer**](cmdqueryname=ipv6+nd+ns+retrans-timer) *interval*
   
   
   
   A neighbor reachability detection interval is configured.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.