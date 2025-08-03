Configuring Alarm Suppression for a Dynamic BFD Session
=======================================================

This section describes how to configure alarm suppression for a dynamic BFD session. After the configuration is complete, no alarm is reported when the dynamic BFD session goes down. For the NMS, this not only reduces the alarm processing pressure, but also ensures the alarm processing capability.

#### Usage Scenario

A dynamic BFD session is triggered by an upper-layer application, such as OSPF. If a fault (for example, a link fault) occurs on the network, the dynamic BFD session reports an alarm to the NMS. The upper-layer application associated with the dynamic BFD also reports an alarm to the NMS. When the number of alarms exceeds the processing capability of the NMS, some other alarms are discarded, meaning that users cannot detect fault alarms quickly enough. After alarm suppression is configured for the dynamic BFD session, only the upper-layer application reports alarms upon network faults. For the NMS, this not only reduces the alarm processing pressure, but also ensures the alarm processing capability. It also ensures network reliability.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bfd**](cmdqueryname=bfd)
   
   
   
   BFD is enabled globally and the BFD view is displayed.
3. Run [**bfd suppress-alarm dynamic**](cmdqueryname=bfd+suppress-alarm+dynamic)
   
   
   
   Alarm suppression is enabled for dynamic BFD sessions.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.