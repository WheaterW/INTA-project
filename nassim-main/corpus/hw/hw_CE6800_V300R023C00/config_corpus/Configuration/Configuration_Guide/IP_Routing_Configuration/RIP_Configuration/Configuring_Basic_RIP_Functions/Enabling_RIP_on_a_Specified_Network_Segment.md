Enabling RIP on a Specified Network Segment
===========================================

Enabling RIP on a Specified Network Segment

#### Context

Before enabling a device to send and receive RIP messages on a specified network segment in a RIP process, you must enable RIP on the network segment.

This can be done using either of the following methods:

* Run the [**network**](cmdqueryname=network) command in the RIP view to enable the function to send and receive routes in a RIP process.
* Run the [**rip enable**](cmdqueryname=rip+enable) command in the interface view to enable the function to send and receive routes on all network segments of a specified interface in a RIP process.![](public_sys-resources/note_3.0-en-us.png) 
  
  The [**rip enable**](cmdqueryname=rip+enable) command takes precedence over the [**network**](cmdqueryname=network) command.


#### Procedure

* In the RIP view, enable the function to send and receive routes in a RIP process.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Create a RIP process and enter the RIP view.
     
     
     ```
     [rip](cmdqueryname=rip) [ process-id ]
     ```
  3. Enable RIP on a specified network segment.
     
     
     ```
     [network](cmdqueryname=network) network-address
     ```
     
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     RIP runs only on the interfaces of a specified network segment, and does not send, receive, or forward routes on any other interfaces.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* In the interface view, enable the function to send and receive routes on all network segments on the specified interface in the RIP process.
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
  4. Enable RIP on all network segments of the interface.
     
     
     ```
     [rip enable](cmdqueryname=rip+enable) process-id
     ```
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```