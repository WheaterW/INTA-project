Configuring Traffic Shaping for a Queue
=======================================

Configuring Traffic Shaping for a Queue

#### Context

Packets received on an interface enter queues based on priority mapping. Then the device uses different traffic shaping parameter settings for queues of different priorities, providing differentiated services.

Before configuring traffic shaping for queues on an interface, configure priority mapping to map packet priorities to per hop behaviors (PHBs) so that packets of different services enter different queues.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) { interface-type interface-number | interface-name }
   ```
3. Configure the traffic shaping rate for queues on an interface.
   
   
   ```
   [qos queue](cmdqueryname=qos+queue) queue-index shaping { percent cir cir-percent-value [ pir pir-percent-value ] | cir cir-value [ kbps | mbps | gbps ] [ cbs cbs-value [ bytes | kbytes | mbytes ] | pir pir-value [ kbps | mbps | gbps ] [ cbs cbs-value [ bytes | kbytes | mbytes ] pbs pbs-value [ bytes | kbytes | mbytes ] ] ] }
   ```
   
   By default, the traffic shaping rate for a queue is the maximum bandwidth of the interface.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```