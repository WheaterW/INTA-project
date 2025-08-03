Enabling or Disabling an Interface
==================================

Enabling or Disabling an Interface

#### Context

To implement the modifications made to an interface's parameters, run the [**shutdown**](cmdqueryname=shutdown) and [**undo shutdown**](cmdqueryname=undo+shutdown) commands, or run the [**restart**](cmdqueryname=restart) command.

When an interface is not connected to a cable or a fiber, disable the interface by using the [**shutdown**](cmdqueryname=shutdown) command to prevent exceptions caused by interference.

![](public_sys-resources/note_3.0-en-us.png) 

* Running the [**shutdown**](cmdqueryname=shutdown) and [**undo shutdown**](cmdqueryname=undo+shutdown) commands is equivalent to running the [**restart**](cmdqueryname=restart) command and does not modify or delete interface configurations.
* A NULL interface is always up and cannot be enabled or disabled by commands.
* A loopback interface is always up after it is configured and cannot be enabled or disabled by commands.


#### Procedure

* Disable an interface.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the interface view.
     
     
     ```
     [interface](cmdqueryname=interface) { interface-name | interface-type interface-number }
     ```
  3. Disable the interface.
     
     
     ```
     [shutdown](cmdqueryname=shutdown)
     ```
     By default, an interface is enabled.![](public_sys-resources/note_3.0-en-us.png) 
     
     In the scenario where an interface has a large number of sub-interfaces, if you run the **shutdown** command in the sub-interface view to shut down the sub-interfaces one after another, the work load is huge. To shut down the sub-interfaces in batches, run the **shutdown interface** command in the system view.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Enable an interface.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the interface view.
     
     
     ```
     [interface](cmdqueryname=interface) { interface-name | interface-type interface-number }
     ```
  3. Enable the interface.
     
     
     ```
     [undo shutdown](cmdqueryname=undo+shutdown)
     ```
     
     By default, an interface is enabled.
  4. (Optional) Switch the interface working mode to Layer 3.
     
     
     ```
     [undo portswitch](cmdqueryname=undo+portswitch)
     ```
     
     Determine whether to perform this step based on the current interface working mode.
  5. (Optional) Disable the protocol status of the interface.
     
     
     ```
     [shutdown network-layer](cmdqueryname=shutdown+network-layer)
     ```
     When users require that only the protocol status of an interface becomes down whereas the physical and link layer status remains unchanged for troubleshooting optical modules or fibers, run the [**shutdown network-layer**](cmdqueryname=shutdown+network-layer) command to disable the interface's protocol status. After faults are rectified at the physical and link layers, run the [**undo shutdown network-layer**](cmdqueryname=undo+shutdown+network-layer) command to reactivate the interface's protocol status. ![](public_sys-resources/note_3.0-en-us.png) 
     
     The **shutdown network-layer** and **protocol up-delay-time** commands cannot be configured together.
  6. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```