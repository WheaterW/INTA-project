Configuring RIPng Timers
========================

Configuring RIPng Timers

#### Context

RIPng timers can prevent routing loops and reduce the possibility of received incorrect routes resulting in incorrect routing information. When the hop count of a route increases, a routing device starts the suppress timer. The routing device does not update the routing table within the period specified by the timer and updates the routing table until the suppress timer expires.


#### Prerequisites

Before configuring RIPng timers, you have completed the following tasks:

* Assign an IPv6 address to each interface to ensure that neighboring nodes are reachable at the network layer.
* [Configuring Basic RIPng Functions](vrp_ripng_cfg_0013.html)

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a RIPng process and enter the RIPng view.
   
   
   ```
   [ripng](cmdqueryname=ripng) [ process-id ]
   ```
3. Configure RIPng timers.
   
   
   ```
   [timers ripng](cmdqueryname=timers+ripng) update age suppress garbage-collect
   ```
   
   
   
   By default, the update timer is 30s, the age timer is 180s, the suppress timer is 0s, and the garbage-collect timer is 120s (four times the update timer).
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```