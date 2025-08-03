(Optional) Configuring the RADIUS Server Status Detection Function
==================================================================

(Optional) Configuring the RADIUS Server Status Detection Function

#### Context

The device detects the RADIUS server status through the RADIUS server status detection function.


#### Procedure

* Configure conditions for setting the RADIUS server status to down. The RADIUS server status is set to down if either of the following conditions is met:
  
  Condition 1: The RADIUS server status is set to down during RADIUS server status detection. This condition depends on the following settings on the device, including the RADIUS server detection interval, maximum number of consecutive unacknowledged packets in each detection interval, and number of times the detection interval cycles. You can perform the following operations to adjust these parameters.
  1. Enter the system view.
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Set the RADIUS server detection interval, maximum number of consecutive unacknowledged packets in each detection interval, and number of times the detection interval cycles.
     ```
     [radius-server](cmdqueryname=radius-server) { dead-interval dead-interval | dead-count dead-count | detect-cycle detect-cycle }
     ```
     
     By default, the RADIUS server detection interval is 5 seconds, the maximum number of consecutive unacknowledged packets in each detection interval is 2, and the number of times the detection interval cycles is 2.
  3. Return to the user view.
     
     ```
     [return](cmdqueryname=return)
     ```
  4. Commit the configuration.
     ```
     commit
     ```
  Condition 2: The RADIUS server does not respond for a specified period of time. By default, this specified period of time is 300 seconds. You can perform the following operations to adjust the period.
  1. Enter the system view.
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Set the maximum period during which the RADIUS server does not respond.
     ```
     [radius-server max-unresponsive-interval](cmdqueryname=radius-server+max-unresponsive-interval) max-unresponsive-interval
     ```
     
     By default, the maximum period during which the RADIUS server does not respond is 300 seconds.
  3. Return to the user view.
     
     ```
     [return](cmdqueryname=return)
     ```
  4. Commit the configuration.
     ```
     commit
     ```
* (Optional) Configure automatic detection.
  
  
  1. Enter the system view.
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the RADIUS server template view.
     ```
     [radius-server template](cmdqueryname=radius-server+template) template-name
     ```
  3. Create a user account for automatic detection.
     
     ```
     [radius-server testuser](cmdqueryname=radius-server+testuser) [username](cmdqueryname=username) username password cipher password
     ```
     
     By default, no user account is configured for automatic detection in a RADIUS server template. After a user account is configured for automatic detection, the automatic detection function is enabled automatically. By default, the automatic detection function takes effect only for RADIUS servers in down state.
  4. (Optional) Set the automatic RADIUS server detection interval.
     
     ```
     [radius-server detect-server interval](cmdqueryname=radius-server+detect-server+interval) interval
     ```
     
     By default, the automatic RADIUS server detection interval is 60 seconds.
  5. (Optional) Enable automatic detection of RADIUS servers in up state and set the automatic detection interval.
     
     ```
     [radius-server detect-server up-server interval](cmdqueryname=radius-server+detect-server+up-server+interval) interval
     ```
     
     By default, the device does not automatically detect RADIUS servers in up state.
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     On a large enterprise network, you are advised not to enable automatic detection of RADIUS servers in up state. This is because if automatic detection is enabled on multiple NAS devices, RADIUS servers periodically receive a large number of probe packets when processing RADIUS Access-Request packets from users, which may deteriorate processing performance of the RADIUS servers.
     
     After the automatic detection function is configured using the [**radius-server testuser**](cmdqueryname=radius-server+testuser) command, the dead-time timer configured using the [**radius-server dead-time**](cmdqueryname=radius-server+dead-time) command does not take effect.
  6. (Optional) Set the timeout interval of RADIUS probe packets.
     
     ```
     [radius-server detect-server timeout](cmdqueryname=radius-server+detect-server+timeout) timeout
     ```
     
     By default, the timeout interval of RADIUS probe packets is 3 seconds.
  7. Return to the user view.
     
     ```
     [return](cmdqueryname=return)
     ```
  8. Commit the configuration.
     ```
     commit
     ```
* (Optional) Configure the duration for which a RADIUS server can remain down, namely, configure the Force-up timer.
  
  ![](public_sys-resources/note_3.0-en-us.png) 
  
  After setting the RADIUS server status to Force-up and automatic detection is enabled, the device immediately sends a probe packet. If the device receives a response packet from the RADIUS server within the Force-up timer period, the device sets the RADIUS server status to up; otherwise, the device sets the RADIUS server status to down.
  
  1. Enter the system view.
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the RADIUS server template view.
     ```
     [radius-server template](cmdqueryname=radius-server+template) template-name
     ```
  3. Configure the RADIUS server Force-up timer.
     
     ```
     [radius-server dead-time](cmdqueryname=radius-server+dead-time) dead-time
     ```
     
     By default, the RADIUS server Force-up timer is 5 minutes.
  4. Return to the user view.
     
     ```
     [return](cmdqueryname=return)
     ```
  5. Commit the configuration.
     ```
     commit
     ```