Configuring NetStream Sampling
==============================

Configuring NetStream Sampling

#### Context

You can configure NetStream sampling to sample packets at a specified sampling rate so that only statistics about sampled packets are collected. Such statistics can present a sufficiently accurate representation of the states of network-wide flows. Setting an appropriate sampling rate is critical to reducing the impact of NetStream on the performance of the device.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure NetStream sampling using one of the following methods:
   
   
   * Configure NetStream sampling in the system view. The sampling configuration will take effect on all interfaces.
     
     ```
     [netstream sampler](cmdqueryname=netstream+sampler) random-packets packet-number { inbound | outbound }
     ```
     
     By default, NetStream sampling is not configured on any interface.
   * Configure NetStream sampling in the interface view. The sampling configuration will take effect only on this interface.
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     [netstream sampler](cmdqueryname=netstream+sampler) random-packets packet-number { inbound | outbound }
     [quit](cmdqueryname=quit)
     ```![](public_sys-resources/note_3.0-en-us.png) 
   * If NetStream sampling is configured in both the system view and interface view, the configuration in the interface view takes precedence.
   * Packets of all types are sampled during NetStream sampling. However, when a NetStream flow is created, the device discards sampled packets that do not match certain conditions configured in the NetStream flow statistics collection function.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```