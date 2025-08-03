Configuring Traffic Policing (Level-2 CAR)
==========================================

Configuring Traffic Policing (Level-2 CAR)

#### Prerequisites

Traffic policing (level-1 CAR) has been configured. For details, see [Configuring MQC-based Traffic Policing (Level-1 CAR)](galaxy_qos_trafficpolicy_trafficshaping_cfg_0031.html).


#### Context

The device supports 2-level traffic policing. After using MQC to implement traffic policing (level-1 CAR) for service flows matching a traffic classifier in a traffic policy, the device aggregates all the service flows matching the traffic classifiers associated with the level-1 CAR in the same traffic policy and performs traffic policing (level-2 CAR) for the aggregated flow. 2-level traffic policing implements multiplexing of traffic statistics and provides fine-grained service control.

![](public_sys-resources/note_3.0-en-us.png) 

This function is not supported by the CE6885-LL (low latency mode).



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. (Optional) Disable the device from counting the inter-frame gaps and preambles when the device calculates the traffic policing rate.
   
   
   ```
   [qos car ifg disable](cmdqueryname=qos+car+ifg+disable)
   ```
3. Configure a CAR profile.
   
   
   ```
   [qos car](cmdqueryname=qos+car) car-name { [percent](cmdqueryname=percent) percent-value | cir cir-value [ kbps | mbps | gbps ] [ cbs cbs-value [ bytes | kbytes | mbytes ] [ pbs pbs-value [ bytes | kbytes | mbytes ] ] | pir pir-value [ kbps | mbps | gbps ] [ cbs cbs-value [ bytes | kbytes | mbytes ] pbs pbs-value [ bytes | kbytes | mbytes ] ] ] }
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The CIR of the QoS CAR profile must be greater than the CIR of the CAR configured in level-1 CAR.
4. Configure aggregated CAR.
   1. Enter the traffic behavior view.
      
      
      ```
      [traffic behavior](cmdqueryname=traffic+behavior) behavior-name
      ```
   2. Configure aggregated CAR.
      
      
      ```
      [car](cmdqueryname=car) car-name share
      ```
      ![](public_sys-resources/note_3.0-en-us.png) 
      
      A traffic policy containing the aggregated CAR action can be applied only to the inbound direction.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```