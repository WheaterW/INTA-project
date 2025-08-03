Configuring the Suppress Timer
==============================

Configuring the Suppress Timer

#### Context

The Suppress timer can prevent routing loops and reduce the possibility of learning incorrect routing information after incorrect routes are received.

When a device receives an Update message in which the hop count of a route increases but is still lower than 16, the device starts the Suppress timer. The device does not update its routing table until the Suppress timer expires.

As well as delaying the addition of incorrect routes to the routing table, the Suppress timer also slows down route convergence on the entire network. Therefore, exercise caution when configuring the Suppress timer based on the live network conditions.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a RIPng process and enter the RIPng view.
   
   
   ```
   [ripng](cmdqueryname=ripng) [ process-id ]
   ```
3. Configure the Suppress timer.
   
   
   ```
   [timers ripng](cmdqueryname=timers+ripng) update age suppress garbage-collect
   ```
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The value of *update* should be less than that of *age*, and the value of *suppress* should be less than that of *garbage-collect*. Setting these values improperly affects RIPng convergence speed and can even cause route flapping on the network. For example, if the value of the update timer is greater than that of the age timer, a routing device cannot immediately inform its neighbors of the RIPng route change.
   
   For the configurations of the update, age, suppress, and garbage-collect timers, see [Configuring RIPng Timers](vrp_ripng_cfg_0040.html).
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```