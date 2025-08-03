Configuring RIP Timers
======================

Configuring RIP Timers

#### Context

RIP timer can prevent routing loops and reduce the possibility of received incorrect routes resulting in incorrect routing information. When the hop count of a route increases, the device starts the Suppress timer, and the device does not update the route in the routing table until this timer expires.

![](public_sys-resources/note_3.0-en-us.png) 

As well as delaying the addition of incorrect routes to the routing table, the Suppress timer also slows down route convergence on the entire network. Therefore, exercise caution when configuring the Suppress timer based on the live network conditions.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a RIP process and enter the RIP view.
   
   
   ```
   [rip](cmdqueryname=rip) [ process-id ]
   ```
3. Configure the Suppress timer.
   
   
   ```
   [timers rip](cmdqueryname=timers+rip) update age suppress garbage-collect
   ```
   
   
   The default value of the Suppress timer is 0 seconds.![](public_sys-resources/note_3.0-en-us.png) 
   
   The value of *update* should be less than that of *age*, and the value of *suppress* should be less than that of *garbage-collect*.
   
   Changing the values of timers affects the RIP route convergence speed, and can even lead to route flapping on the network. For example, if the value of the update timer is greater than that of the age timer and RIP routes are changed, a routing device cannot immediately notify its neighbors of the change.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```