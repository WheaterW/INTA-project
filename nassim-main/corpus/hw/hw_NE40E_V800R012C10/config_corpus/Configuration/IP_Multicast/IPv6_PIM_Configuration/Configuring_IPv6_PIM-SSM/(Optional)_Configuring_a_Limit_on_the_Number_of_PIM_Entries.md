(Optional) Configuring a Limit on the Number of PIM Entries
===========================================================

IPv6 PIM-SSM allows you to limit the number of (S, G) entries. After a specified limit is reached, new (S, G) entries cannot be created.

#### Context

Limit the number of PIM entries to prevent a device from generating excessive multicast routing entries when attackers send numerous multicast data or IGMP/PIM protocol messages. Therefore, this function helps prevent high memory and CPU usage and improve multicast service security.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**multicast ipv6 global limit**](cmdqueryname=multicast+ipv6+global+limit) **pim sm** **source-group-number** *limit-count6* [ **threshold-alarm upper-limit** *upper-limit-value* **lower-limit** *lower-limit-value* ]
   
   
   
   The limit on the number of PIM entries and alarm thresholds are set. After the command is run:
   
   
   
   * If the specified limit is reached, new entries cannot be created, and the alarm PIM\_1.3.6.1.4.1.2011.5.25.149.4.0.23 routeExceed is generated.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Statically created (S, G) entries are not affected.
   * If **threshold-alarm upper-limit** *upper-limit-value* is set, the PIM\_1.3.6.1.4.1.2011.5.25.149.4.0.21 routeThresholdExceed alarm is generated when the percentage ratio of entries to the specified limit reaches *upper-limit-value*.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.