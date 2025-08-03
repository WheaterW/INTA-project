Defining a Traffic Behavior and Configuring Actions
===================================================

This section describes the traffic behaviors supported by a device and how to configure actions for a traffic behavior.

#### Context

A device supports various types of actions for a traffic behavior. You can configure one or more types of actions as required.


#### Procedure

* Configure traffic scheduling.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**traffic behavior**](cmdqueryname=traffic+behavior) *behavior-name*
     
     
     
     A traffic behavior is configured and its view is displayed.
  3. Run [**car**](cmdqueryname=car) { **cir** *cir-value* [ **pir** *pir-value* ] } [ **cbs** *cbs-value* [ **pbs** *pbs-value* ] ] [ **adjust** *adjust-value* ] [ **green** { **discard** | **pass** [ **remark dscp** *dscp* | **service-class** *class* **color** *color* ] } | **yellow** { **discard** | **pass** [ **remark dscp** *dscp* | **service-class** *class* **color** *color* ] } | **red** { **discard** | **pass** [ **remark dscp** *dscp* | **service-class** *class* **color** *color* ] } ] \* [ **summary** ] [ **color-aware** ] [ **limit-type pps** ]
     
     
     
     A traffic policing action is configured.
     
     
     
     If this command is run more than once, the last configuration overrides the previous one.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If the CoS of a packet is re-marked as EF, BE, CS6, or CS7, the packet can be re-marked only green.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure forcible traffic classification.
  1. Run [**service-class**](cmdqueryname=service-class) *service-class* **color** *color*
     
     
     
     Packets with a certain CoS are colored.
  2. (Optional) Run [**service-class**](cmdqueryname=service-class) *service-class* **color** *color* **track** { **master** | **slave** } **bfd-session** **session-name** *bfd-session-name*
     
     
     
     The CoS and color of packets matching the traffic policy are marked based on the status of a specified BFD session.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Set a packet priority.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**traffic behavior**](cmdqueryname=traffic+behavior) *behavior-name*
     
     
     
     A traffic behavior is configured and its view is displayed.
  3. Perform the following configurations as required.
     
     
     + To re-mark the DSCP value of VXLAN packets, run the [**remark**](cmdqueryname=remark) **dscp** *dscp-value* command.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a cascaded traffic policy.
  
  
  
  ACL rules are generally used for redirection in a traffic behavior. However, the specifications of ACL rules are limited. When ACL rules defined for MF classification do not meet the live network requirements, you can redirect the traffic behavior to a configured traffic policy to implement cascaded MF classification.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**traffic behavior**](cmdqueryname=traffic+behavior) *behavior-name*
     
     
     
     A traffic behavior is configured and its view is displayed.
  3. Run [**traffic-policy**](cmdqueryname=traffic-policy) *policy-name*
     
     
     
     A cascaded traffic policy is configured.
     
     
     
     + Configuring a cascaded traffic policy will cause device forwarding performance to deteriorate.
     + When the traffic on an interface matches a cascaded traffic policy:
       - The behaviors of the cascaded traffic policy are performed.
       - If the traffic behaviors in the two traffic policies are different, they can be individually performed.
       - If the traffic behaviors in the two traffic policies are the same, the behaviors of the cascaded traffic policy are performed.
     + The parameters specified for a traffic policy to be applied to an interface, such as **inbound**, **outbound**, **link-layer**, **all-layer**, and **mpls-layer**, are inherited by a cascaded traffic policy.
     + When the traffic behaviors for two-level ACLs are **service-class**, level-1 **service-class** preferentially takes effect. However, if level-1 **service-class** carries **no-remark**, level-2 **service-class** preferentially takes effect.
  4. (Optional) Run [**hierarchical-car enable**](cmdqueryname=hierarchical-car+enable)
     
     
     
     Hierarchical CAR is enabled in the cascaded traffic policy.
     
     
     
     When a traffic policy is configured in a traffic behavior, CAR can also be configured in the traffic policy to implement hierarchical CAR.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.