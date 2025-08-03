Configuring a Limit on the Number of PIM Entries
================================================

Configuring a Limit on the Number of PIM Entries

#### Context

If a large number of multicast routing entries are generated due to attacks from multicast data or IGMP/PIM messages, the memory or CPU usage of the device will be high. To prevent this problem, configure a limit on the number of PIM entries (for PIM-SM, the number of (S, G) and (\*, G) entries can be limited). If the number of entries exceeds the limit, no more entries can be created. In this way, multicast services can run properly.


#### Procedure

* In a public network scenario, configure a limit on the number of PIM entries and alarm thresholds.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure a limit on the number of PIM entries and alarm thresholds.
     
     
     ```
     [multicast global limit](cmdqueryname=multicast+global+limit) pim sm { star-group-number | source-group-number } limit-count [ threshold-alarm upper-limit upper-limit-value lower-limit lower-limit-value ] 
     ```
     
     **star-group-number** indicates the limit on the number of (\*, G) entries. **source-group-number** indicates the limit on the number of (S, G) entries. After the command is run:
     
     
     
     + If the specified limit is reached, new entries cannot be created, and the alarm (routeExceed) is generated.
     + If an alarm threshold is set using the **threshold-alarm upper-limit** *upper-limit-value* command, the alarm (routeThresholdExceed) is generated when the number of entries reaches the alarm threshold.
     
     However, static (\*, G) and (S, G) entries are not limited by the configuration.
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```