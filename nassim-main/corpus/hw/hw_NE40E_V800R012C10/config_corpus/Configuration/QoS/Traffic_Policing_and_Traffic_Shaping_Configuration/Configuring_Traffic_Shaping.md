Configuring Traffic Shaping
===========================

The function of traffic shaping is similar to that of traffic policing. Traffic shaping mainly buffers packets that need to be dropped by traffic policing by means of buffer and token bucket.

#### Usage Scenario

When the traffic volume on a network is heavy, nonconforming packets are directly discarded. If the upstream Router sends a large volume of data traffic, the downstream network may be congested or a great number of packets are dropped. To prevent this situation, configure traffic shaping on the outbound interface of the upstream Router to limit the traffic. Traffic shaping enables packets to be transmitted at an even rate and improves the allocation of bandwidth resources between the upstream and downstream networks.

Traffic shaping is carried out using buffers and token buckets. If packets are sent at a high rate, nonconforming packets are not dropped. Instead, such packets are placed in buffer queues. Under the control of token buckets, buffered packets are sent at an even rate by queue scheduling priority when the network is idle. As a result, packet retransmissions in case of packet dropping is prevented.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The NE40E uses the pre-defined queue scheduling mechanism to allocate resources to the services of different classes, such as EF and AF. You do not need to configure queue management.

Currently, the NE40E supports traffic shaping only for the outgoing traffic on interfaces.


#### Pre-configuration Tasks

Before configuring traffic shaping, complete the following tasks:

* Configure parameters for physical interfaces.
* Configure link layer attributes for interfaces to ensure their normal operating.
* Configure IP addresses for interfaces.
* Enable a routing protocol for communication between devices.

#### Procedure

* Configure interface-based traffic shaping.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run 
     [**interface**](cmdqueryname=interface)
     *interface-type*
     *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**port shaping**](cmdqueryname=port+shaping)
     { 
     *shaping-value*
      | **shaping-percentage**
     *shaping-percentage-value* } [ **network-header-length**
     *network-header-length-value* ]
      [ **pbs**
     *pbs-value* ] [ **weight-mode** ]
     
     
     
     Traffic shaping is configured for outgoing traffic on the interface
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     To allocate shaping values based on the weights of trunk member interfaces, run the [**port shaping**](cmdqueryname=port+shaping)
     *shaping-value* [ **weight-mode** ] command.
  4. (Optional) Run **qos port-shaping member-link-scheduler distribute**
     
     
     
     The device is configured to allocate shaping bandwidth based on the weights of trunk member interfaces when the interfaces reside on different NPs.
     
     
     
     By default, if trunk member interfaces reside on the same NP, they share the shaping bandwidth configured on the trunk interface. However, if they reside on different NPs, the shaping bandwidth of each member interface is the bandwidth configured on the trunk interface. In such a scenario, the traffic rate on the trunk interface is the configured shaping bandwidth multiplied by the number of member interfaces. Consequently, the traffic shaping is not as expected. You are therefore advised to perform this configuration in such a scenario to avoid unexpected traffic shaping results.
  5. Run [**port-queue**](cmdqueryname=port-queue)
     *cos-value* { { **pq** | **wfq**
     **weight**
     *weight-value*
     | **lpq**
     } | **shaping** { *shaping-value* | **shaping-percentage**
     *shaping-percentage-value* } [ **pbs**
     *pbs-value* ] | **port-wred**
     *wred-name*
      
     | **low-latency**
     
      } \*
     **outbound**
     or [**port-queue**](cmdqueryname=port-queue)
     *cos-value*
     
     **cir** { { *cir-value* [ **cbs**
     *cbs-value* ] **cir-schedule**
     **pq**
     **pir**
     *pir-value* } | { **cir-percentage**
     *cir-percentage-value* [ **cbs**
     *cbs-value* ] **cir-schedule**
     **pq**
     **pir**
     **pir-percentage**
     *pir-percentage-value* } } [ **pbs**
     *pbs-value* ] **pir-schedule** { **pq** | **wfq** 
     **weight** 
     *weight-value* | **lpq** } [ **port-wred**
     *wred-name* ] **outbound**
     
     
     
     A scheduling policy is configured for a specific port queue.
  6. Run [**port-queue-alarm**](cmdqueryname=port-queue-alarm)
     *cos-value* { **discard-packet** 
     *discard-packet-number* | **discard-byte** 
     *discard-byte-number* | **discard-packet-ratio** 
     *discard-packet-coefficient*
     *discard-packet-exponent* } [ **interval** 
     *interval-time* ]
     
     
     
     The packet loss alarm function for port queues is enabled.
  7. Run 
     [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure traffic shaping based on a sub-interface queue.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**sub-port-queue**](cmdqueryname=sub-port-queue)
     *sub-port-queue-name*
     
     
     
     The sub-interface queue profile view is displayed.
  3. Run [**shaping**](cmdqueryname=shaping)
     *shaping-value* [ **pbs**
     *pbs-value* ] **outbound**
     
     
     
     A shaping value is configured for sub-interface queues.
  4. Run [**weight**](cmdqueryname=weight)
     *weight-value*
     **outbound**
     
     
     
     A weight is configured for sub-interface queues.
  5. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  6. Run [**interface**](cmdqueryname=interface)
     *interface-type*
     *interface-number*
     
     
     
     The interface view is displayed.
  7. Run [**sub-port-queue**](cmdqueryname=sub-port-queue)
     *sub-port-queue-name*
     **outbound** [ **group**
     *group-name* ]
     
     
     
     The sub-interface queue profile is applied to the interface.
  8. (Optional) Run **qos default sub-port-queue**
     **shaping** 
     *shaping-value* [ **pbs**
     *pbs-value* ] **outbound**
     
     
     
     Traffic shaping parameters of the default sub-interface queue are modified.
  9. (Optional) Run **bas-load-balance exclude sub-port-queue outbound**
     
     
     
     Route selection based on sub-interface queues is disabled for downstream traffic.
     
     
     
     If an Eth-Trunk interface is used for traffic forwarding, the system performs route selection for downstream traffic of a given sub-interface queue based on that queue by default. This means that downstream traffic of the sub-interface queue is forwarded through the same Eth-Trunk member interface. Consequently, traffic load imbalance may occur among Eth-Trunk member interfaces. To load-balance downstream traffic among Eth-Trunk member interfaces, run this command.
  10. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
  11. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
* Configure traffic shaping based on a PQ.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**port-queue-template**](cmdqueryname=port-queue-template)
     *port-queue-name*
     
     
     
     A PQ profile is created and its view is displayed.
  3. Run [**queue**](cmdqueryname=queue)
     *cos-value* { { **pq** | **wfq**
     **weight**
     *weight-value* | **lpq** } | **shaping** { *shaping-value* | **shaping-percentage**
     *shaping-percentage-value* } [ **pbs**
     *pbs-value* ] | **port-wred**
     *wred-name* | **low-latency** } \*
     
     
     
     Scheduling parameters are configured for PQs in the PQ profile.
  4. Run [**share-shaping**](cmdqueryname=share-shaping) { **af1** | **af2** | **af3** | **af4** | **be** | **cs6** | **cs7** | **ef** } \* [ **pq** | **wfq**
     **weight**
     *weight-value* | **lpq** ] { *shaping-value* | **shaping-percentage**
     *shaping-percentage-value* } [ **pbs**
     *pbs-value* ]
     
     
     
     Share shaping is configured for PQs.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The [**port share-shaping**](cmdqueryname=port+share-shaping) and [**share-shaping (port queue view)**](cmdqueryname=share-shaping+%28port+queue+view%29) commands are mutually exclusive on an interface.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  6. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  7. Run [**interface**](cmdqueryname=interface)
     *interface-type*
     *interface-number*
     
     
     
     The interface view is displayed.
  8. Run [**port-queue-template**](cmdqueryname=port-queue-template)
     *port-queue-name*
     **outbound**
     
     
     
     The PQ profile is applied to the interface.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The [**port-queue**](cmdqueryname=port-queue) and [**port-queue-template**](cmdqueryname=port-queue-template) commands are mutually exclusive on an interface.
     
     A PQ profile can be applied to a tunnel interface only when the protocol of the tunnel interface is set to GRE or GRE IPv6 and the **port-shaping** command is configured.
  9. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure traffic shaping in the slot view.
  1. Run 
     [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run 
     [**slot**](cmdqueryname=slot)
     *slot-id*
     
     
     
     The slot view is displayed.
  3. Run [**port shaping**](cmdqueryname=port+shaping)
     *shaping-value*
     **bind**
     **mtunnel**
     
     
     
     A peak rate is set at which the MTunnel interface in the distributed multicast VPN can send data.
  4. Run 
     [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the network header length for a service profile.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**service-template**](cmdqueryname=service-template)
     *service-template-name*
     
     
     
     The service profile view is displayed.
  3. Run [**network-header-length**](cmdqueryname=network-header-length)
     *network-header-length*
     { **inbound** | **outbound** }
     
     
     
     A network header length is configured for the service profile.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  5. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  6. Run [**interface**](cmdqueryname=interface)
     *interface-type*
     *interface-number*
     
     
     
     The interface view is displayed.
  7. Run [**shaping service-template**](cmdqueryname=shaping+service-template)
     *service-template-name*
     
     
     
     The defined service profile is applied to the interface.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Verifying the Configuration

After completing the configuration, perform the following operations to verify the configuration:

* Run the [**display interface**](cmdqueryname=display+interface) [ *interface-type* [ *interface-number* ] ] command to check traffic information on interfaces.
* Run the [**display service-template configuration**](cmdqueryname=display+service-template+configuration) [ **verbose** [ *service-template-name* ] ] command to check information about user-defined service profiles.
* Run the [**display port-wred configuration**](cmdqueryname=display+port-wred+configuration) [ **verbose** [ *port*-*wred*-*name* ] ] command to check the configuration of a port WRED object.
* Run the [**display port-queue configuration**](cmdqueryname=display+port-queue+configuration)
  **interface**
  *interface-type*
  *interface-number*
  **outbound** command to check the detailed PQ configuration.
* Run the [**display port-queue statistics**](cmdqueryname=display+port-queue+statistics) [ **slot**
  *slot-id* | **interface**
  *interface-type*
  *interface-number* ] [ *cos-value* ] **outbound** command to check PQ statistics.
* Run the [**display sub-port-queue configuration**](cmdqueryname=display+sub-port-queue+configuration) [ **verbose** [ *sub-port-queue-name* ] ] command to check information about sub-interface queues.
* Run the [**display sub-port-queue configuration**](cmdqueryname=display+sub-port-queue+configuration) [ **verbose** [ *sub-port-queue-name* ] ] command to check information about sub-interface queues.