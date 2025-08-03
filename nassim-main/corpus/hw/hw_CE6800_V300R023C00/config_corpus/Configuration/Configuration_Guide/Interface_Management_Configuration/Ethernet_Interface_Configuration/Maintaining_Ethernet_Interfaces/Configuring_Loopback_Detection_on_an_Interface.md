Configuring Loopback Detection on an Interface
==============================================

Configuring Loopback Detection on an Interface

#### Context

Before testing some special functions such as locating an Ethernet fault, enable loopback detection on the desired Ethernet interface to check whether the interface is working properly. If no fault occurs on the Ethernet interface, the physical and protocol statuses of the interface are always up after loopback detection is enabled. If a fault occurs, the statuses remain down.

![](public_sys-resources/notice_3.0-en-us.png) 

The loopback detection function affects other functions and may prevent the interface or link from working properly. When the test is complete, run the [**undo loopback**](cmdqueryname=undo+loopback) command to disable loopback detection. The original configuration is restored after loopback detection is disabled.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Configure loopback detection on the Ethernet interface.
   
   
   ```
   [loopback](cmdqueryname=loopback) internal
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display interface**](cmdqueryname=display+interface) [ *interface-type* [ *interface-number* ] ] command in any view or the [**display this interface**](cmdqueryname=display+this+interface) command in the interface view to check the current interface status. The **Loopback** field in the command output shows the loopback status.