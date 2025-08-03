Configuring an Interface to Enter the Error-Down State When the Receive Optical Power Is Low
============================================================================================

Configuring an Interface to Enter the Error-Down State When the Receive Optical Power Is Low

#### Context

A device records the status of an interface as Error-Down when it detects a fault on the interface. An interface in Error-Down state cannot receive or send packets and the interface indicator is off. Low receive optical power is one of the possible causes of an interface entering the Error-Down state, which may subsequently lead to issues such as packet loss. If this function is not enabled, an interface that encounters a fault may be still up, preventing traffic from being switched to a configured backup link. To avoid impact on services, you can configure the interface to change to the Error-Down state when the receive optical power is low. After this configuration is complete, when the receive optical power on the interface falls below the lower alarm threshold, the device disables the interface and records the interface status as **ERROR DOWN(transceiver-power-low)**. Services are then switched to the backup link immediately.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Configure the interface to enter the Error-Down state when the receive optical power is low.
   
   
   ```
   [port transceiver-power-low trigger error-down](cmdqueryname=port+transceiver-power-low+trigger+error-down)
   ```
   
   By default, an Ethernet optical interface does not enter the Error-Down state when the receive optical power is low.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display error-down recovery**](cmdqueryname=display+error-down+recovery) [ **interface** *interface-type* *interface-number* ] command in any view to check information about the interface in Error-Down state.


#### Follow-up Procedure

If an interface is in Error-Down state, you are advised to find out the cause first.

An interface in Error-Down state can be recovered using either of the following methods:

* Manual recovery (after an Error-Down event occurs):
  
  If few interfaces need to be recovered, run the [**shutdown**](cmdqueryname=shutdown) and [**undo shutdown**](cmdqueryname=undo+shutdown) commands in the interface view, or restart the interface by running the [**restart**](cmdqueryname=restart) command in the interface view.
* Automatic recovery (before an Error-Down event occurs):
  
  If a large number of interfaces need to be recovered, manual recovery is time consuming, and some interfaces may be omitted. To avoid these problems, run the [**error-down auto-recovery**](cmdqueryname=error-down+auto-recovery) **cause transceiver-power-low** **interval** command in the system view to enable automatic interface recovery and set the delay time for recovery. You can run the [**display error-down recovery**](cmdqueryname=display+error-down+recovery) command to view information about automatic interface recovery.
  
  ![](public_sys-resources/note_3.0-en-us.png) 
  
  This method does not take effect on interfaces that are already in Error-Down state. It takes effect only on interfaces that enter the Error-Down state after this configuration is complete.