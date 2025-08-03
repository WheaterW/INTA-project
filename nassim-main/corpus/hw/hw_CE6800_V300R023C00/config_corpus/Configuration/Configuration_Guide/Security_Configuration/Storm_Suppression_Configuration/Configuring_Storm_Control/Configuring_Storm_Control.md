Configuring Storm Control
=========================

Configuring Storm Control

#### Context

To rate-limit broadcast packets, unknown multicast packets, or unknown unicast packets on an interface so as to prevent broadcast storms, configure storm control for these types of packets on the interface.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode to Layer 2.
   
   
   ```
   [portswitch](cmdqueryname=portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Configure the upper and lower thresholds for broadcast packets, unknown multicast packets, or unknown unicast packets on the interface. The device supports the following configuration modes based on the measurement units of the upper and lower thresholds:
   * Specify the lower threshold *min-rate-value* and upper threshold *max-rate-value*, which is expressed in pps.
     ```
     [storm control](cmdqueryname=storm+control) { broadcast | multicast | unknown-unicast } min-rate min-rate-value max-rate max-rate-value
     ```
   * Specify the lower threshold *min-rate-value-kbps* and upper threshold *max-rate-value-kbps*, which is expressed in kbit/s.
     ```
     [storm control](cmdqueryname=storm+control) { broadcast | multicast | unknown-unicast } min-rate kbps min-rate-value-kbps max-rate kbps max-rate-value-kbps
     ```
   * Specify the lower threshold *min-rate-value-percent* and upper threshold *max-rate-value-percent*. The threshold is expressed in percentage, that is, the percentage of the interface bandwidth occupied by packets.
     ```
     [storm control](cmdqueryname=storm+control) { broadcast | multicast | unknown-unicast } min-rate percent min-rate-value-percent max-rate percent max-rate-value-percent
     ```
5. Configure a storm control action.
   1. Configure the storm control action as **error-down**, **block**, or **suppress**.
      
      
      ```
      [storm control action](cmdqueryname=storm+control+action) { error-down | block | suppress }
      ```
   2. (Optional) Enable an interface to automatically go up before the interface enters the error-down state, and set the recovery delay (this step is only applicable to the **error-down** action).
      
      This function should be used if a large number of interfaces may enter the error-down state, as manually recovering so many error-down interfaces is time-consuming and error-prone. To prevent this problem, you can configure interfaces in error-down state to automatically go up, and set the recovery delay. ![](public_sys-resources/note_3.0-en-us.png) 
      
      This method does not take effect on interfaces that are already in error-down state. It takes effect only on interfaces that enter the error-down state after the [**error-down auto-recovery**](cmdqueryname=error-down+auto-recovery) command is run.
      
      You can run the **display error-down recovery** command to check information about automatic interface recovery.
      
      
      
      
      ```
      [error-down auto-recovery](cmdqueryname=error-down+auto-recovery) cause storm-control interval interval-value
      ```
6. Configure the storm detection interval.
   
   
   ```
   [storm control interval](cmdqueryname=storm+control+interval) interval-value
   ```
7. (Optional) Enable the device to record logs or report traps during storm control.
   
   
   ```
   [storm control enable](cmdqueryname=storm+control+enable) { log | trap }
   ```
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display storm control**](cmdqueryname=display+storm+control) [ **interface** *interface-type* *interface-number* [ **verbose** ] ] command to check storm control information on an interface.


#### Follow-up Procedure

After the storm control action is set to **error-down** on an interface, the interface is shut down when the average rate of received broadcast packets, unknown multicast packets, or unknown unicast packets exceeds the specified upper threshold within the detection interval. If an interface is in error-down state, run the **shutdown** and **undo shutdown** commands in the interface view, or run the **restart** command to restart the interface.