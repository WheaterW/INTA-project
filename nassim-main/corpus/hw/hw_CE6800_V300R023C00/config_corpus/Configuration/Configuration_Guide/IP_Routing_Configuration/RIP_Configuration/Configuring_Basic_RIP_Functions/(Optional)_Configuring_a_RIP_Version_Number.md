(Optional) Configuring a RIP Version Number
===========================================

(Optional) Configuring a RIP Version Number

#### Procedure

* Configure the global RIP version number.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Create a RIP process and enter the RIP view.
     
     
     ```
     [rip](cmdqueryname=rip) [ process-id ]
     ```
  3. Specify the global RIP version number.
     
     
     ```
     [version](cmdqueryname=version) version-num
     ```
     
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     RIP-2 is more secure than RIP-1, and therefore is recommended.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure the RIP version number on an interface.
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
  4. Configure the RIP version number for the RIP messages to be accepted by the interface.
     
     
     ```
     [rip version](cmdqueryname=rip+version) { 1 | 2 [ broadcast | multicast ] }
     ```
     
     By default, an interface can send and receive RIP-2 messages. If the RIP version number is not configured on the interface, the global RIP version number takes effect. If the RIP version number on the interface is set to 2, you can also configure the RIP message sending mode as either broadcast or multicast.
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```