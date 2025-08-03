Configuring a Global Traffic Policy and Enabling Global QPPB
============================================================

A global traffic policy must be configured for global QPPB implementation.

#### Context

To implement global QPPB, configure a global traffic policy and configure QoS policy ID-based rules in the traffic classifier.

For detailed traffic policy configurations, see [Class-based QoS Configuration](dc_ne_qos_cfg_0037.html).

In VS mode, this configuration is supported only by the admin VS.


#### Procedure

1. Define a traffic classifier based on Layer 3 or Layer 4 information.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**traffic classifier**](cmdqueryname=traffic+classifier) *classifier-name* [ **operator** { **and** | **or** } ]
      
      
      
      A traffic classifier is defined, and the traffic classifier view is displayed.
   3. Run [**if-match qos-local-id**](cmdqueryname=if-match+qos-local-id) *qos-local-id*
      
      
      
      A source or destination QoS policy ID-based rule is configured in the traffic classifier.
   4. Run [**if-match qos-local-id**](cmdqueryname=if-match+qos-local-id) **source** *source-local-id* **destination** *destination-local-id*
      
      
      
      A source and destination QoS policy ID-based rule is configured in the traffic classifier.
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
2. Define a traffic behavior and configure actions.
   
   
   
   For details, see [Defining a Traffic Behavior and Configuring Actions](dc_ne_qos_cfg_0043.html).
3. Define a traffic policy and configure traffic behaviors.
   
   
   
   For details, see [Configuring a Traffic Policy](dc_ne_qos_cfg_0044.html).
4. Run **quit**
   
   
   
   Return to the system view.
5. Run [**traffic-policy**](cmdqueryname=traffic-policy) *policy-name* { **inbound** | **outbound** } **global-acl**
   
   
   
   A global traffic policy is configured.
6. Run [**qppb qos-local-id**](cmdqueryname=qppb+qos-local-id) { **source** | **destination** | **both inbound** }
   
   
   
   Global QPPB is enabled.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.