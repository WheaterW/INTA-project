Disabling an Interface from Sending RIP Messages
================================================

Disabling an Interface from Sending RIP Messages

#### Context

If an interface connected to an external network is not required to send routing information, you can disable the interface from sending RIP messages. As shown in [Figure 1](#EN-US_TASK_0000001130782974__fig9617161144619), a RIP-enabled network (Network 1) connects to another network (Network 2) through an edge device (DeviceA). You can disable the interface connecting the edge device to the external network from sending RIP messages.

**Figure 1** Network diagram of disabling an interface from sending RIP messages  
![](figure/en-us_image_0000001176662751.png)

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface mode.
4. Disable the interface from sending RIP messages.
   
   
   ```
   [undo rip output](cmdqueryname=undo+rip+output)
   ```
   
   
   
   By default, an interface is allowed to send RIP messages.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```