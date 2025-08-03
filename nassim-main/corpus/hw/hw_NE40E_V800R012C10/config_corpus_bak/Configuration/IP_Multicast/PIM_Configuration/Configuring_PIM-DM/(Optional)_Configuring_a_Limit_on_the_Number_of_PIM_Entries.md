(Optional) Configuring a Limit on the Number of PIM Entries
===========================================================

PIM-DM allows you to limit the number of (S, G) and (\*, G) entries separately. After a specified limit is reached, new entries of the corresponding type cannot be created.

#### Context

Limit the number of PIM entries to prevent a device from generating excessive multicast routing entries when attackers send numerous multicast data or IGMP/PIM protocol messages. Therefore, this function helps prevent high memory and CPU usage and improve multicast service security.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**multicast global limit**](cmdqueryname=multicast+global+limit) **pim dm** { **star-group-number** | **source-group-number** } *limit-count* [ **threshold-alarm upper-limit** *upper-limit-value* **lower-limit** *lower-limit-value* ]
   
   
   
   A limit on the number of PIM entries and alarm trigger and clear thresholds are set. After the command is run:
   
   
   
   * After the specified limit is reached, new entries cannot be created, and the PIM\_1.3.6.1.4.1.2011.5.25.149.4.0.23 routeExceed alarm is generated.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     New (\*, G) entries can be manually added.
   * If **threshold-alarm upper-limit** *upper-limit-value* is set, the PIM\_1.3.6.1.4.1.2011.5.25.149.4.0.21 routeThresholdExceed alarm is generated when the percentage ratio of created PIM entries to the specified limit reaches *upper-limit-value*.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.