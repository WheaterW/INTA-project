Disabling Active/Standby Board Switching Triggered by Abnormal OSPF Aging
=========================================================================

By default, active/standby board switching triggered by abnormal OSPF aging is enabled. To disable this function, perform this task.

#### Context

When the local device's aging timer expires, the local device incorrectly clears all Router LSAs received from the peer device, which causes large-scale route flapping and service interruptions. To resolve this issue, active/standby board switching triggered by abnormal OSPF aging is automatically enabled. Such switching is triggered to restore network connections and service traffic when the following condition is met:

(Number of incorrectly cleared Router LSAs/Total number of Router LSAs) x 100% â¥ 80% (Router LSAs are those sent by the peer device to the local device)


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospf maxage-lsa auto-protect disable**](cmdqueryname=ospf+maxage-lsa+auto-protect+disable)
   
   
   
   Active/standby board switching triggered by abnormal OSPF aging is disabled.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.