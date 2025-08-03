Disabling an Interface from Receiving RIP Messages
==================================================

Disabling an Interface from Receiving RIP Messages

#### Context

On an enterprise network where certain departments are not permitted to communicate with one other, you can disable interfaces from receiving RIP messages. As shown in [Figure 1](#EN-US_TASK_0000001176742623__fig_dc_vrp_rip_cfg_001601), if Department 1 is not expected to learn the routing information of Department 2, you can disable the interfaces on DeviceA from receiving RIP messages.

**Figure 1** Network diagram of disabling an interface from receiving RIP messages  
![](figure/en-us_image_0000001176742641.png)

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
4. Disable an interface from accepting RIP messages.
   
   
   ```
   [undo rip input](cmdqueryname=undo+rip+input)
   ```
   
   
   
   By default, an interface is allowed to accept RIP messages.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```