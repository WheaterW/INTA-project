Enabling RIP on Specified Network Segments
==========================================

To enable a RIP process to receive and send RIP routes
on specified network segments, enable RIP for the network segments first.

#### Context

You can perform either of the following operations to
enable RIP on specified network segments:

* Run the [**network**](cmdqueryname=network) command in the RIP process view to enable
  a RIP process to receive and send routes on a specified network segment.
* Run the [**rip enable**](cmdqueryname=rip+enable) command in the interface view to enable
  a RIP process to receive and send routes on all the network segments
  where a specified interface is located.![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  The [**rip enable**](cmdqueryname=rip+enable) command takes precedence over the [**network**](cmdqueryname=network) command.


#### Procedure

* Enable a RIP process to receive and send routes on a specified
  network segment.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**rip**](cmdqueryname=rip) [ *process-id* ]
     
     
     
     A RIP process is created, and the view of the RIP process is displayed.
  3. Run [**network**](cmdqueryname=network) *network-address*
     
     
     
     RIP is enabled on a specified
     network segment.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is
     committed.
     
     RIP runs only on interfaces on the specified network
     segment.
* Enable a RIP process to receive and send routes on all
  specified network segments where a specified interface is located.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**rip enable**](cmdqueryname=rip+enable) *process-id*
     
     
     
     RIP is enabled on all the network
     segments where the interface is located.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is
     committed.