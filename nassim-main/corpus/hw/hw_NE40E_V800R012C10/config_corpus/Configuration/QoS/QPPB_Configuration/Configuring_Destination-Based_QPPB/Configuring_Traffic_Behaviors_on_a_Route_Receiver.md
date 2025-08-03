Configuring Traffic Behaviors on a Route Receiver
=================================================

You can configure different traffic behaviors for different traffic classifiers on a BGP receiver to implement differentiated services.

#### Context

Perform the following operations on the BGP route receiver:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**traffic behavior**](cmdqueryname=traffic+behavior) *behavior-name*
   
   
   
   A traffic behavior is configured and the traffic behavior view is displayed.
3. Run one of the following commands as needed:
   
   
   * To configure a traffic policing action, run the [**car**](cmdqueryname=car) { **cir** *cir-value* [ **pir** *pir-value* ] } [ **cbs** *cbs-value* [ **pbs** *pbs-value* ] ] [ **adjust** *adjust-value* ] [ **green** { **discard** | **pass** [ **remark dscp** *dscp-value* | **service-class** *class* **color** *color* ] } | **yellow** { **discard** | **pass** [ **remark dscp** *dscp-value* | **service-class** *class* **color** *color* ] } | **red** { **discard** | **pass** [ **remark dscp** *dscp-value* | **service-class** *class* **color** *color* ] } ] \* [ **summary** ] [ **color-aware** ] [ **limit-type pps** ]  command.
   * To re-mark the DSCP value of an IP packet, run the [**remark**](cmdqueryname=remark) [ **ipv6** ] **dscp** { *dscp-value* | **af11** | **af12** | **af13** | **af21** | **af22** | **af23** | **af31** | **af32** | **af33** | **af41** | **af42** | **af43** | **cs1** | **cs2** | **cs3** | **cs4** | **cs5** | **cs6** | **cs7** | **default** | **ef** } command.
   * To re-configure the precedence of IP packets, run the [**remark ip-precedence**](cmdqueryname=remark+ip-precedence) *ip-precedence*.
   * To allow all the packets that meet the matching rule to pass, run the [**permit**](cmdqueryname=permit) command.
   * To prevent all the packets that meet the matching rule from passing, run the [**deny**](cmdqueryname=deny) command.
   * To color packets with a certain CoS, run the [**service-class**](cmdqueryname=service-class) *service-class* **color** *color* command.
   * To configure user-queue scheduling parameters to implement HQoS scheduling for user services, run the [**user-queue**](cmdqueryname=user-queue) **cir** *cir-value* [ [ **pir** *pir-value* ] | [ **flow-queue** *flow-queue-name* ] | [ **flow-mapping** *mapping-name* ] | [ **user-group-queue** *group-name* ] | [ **service-template** *service-template-name* ] ]\* command.
   * To redirect packets to a specified VPN group, run the [**redirect vpn-group**](cmdqueryname=redirect+vpn-group) *vpn-group-name* command.
   * To configure the traffic behavior redirecting to the traffic policy, run the command [**traffic-policy**](cmdqueryname=traffic-policy) *policy-name*.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     You can run the [**hierarchical-car enable**](cmdqueryname=hierarchical-car+enable) command in the traffic behavior view to enable hierarchical CAR in a cascaded traffic policy scenario.
     
     
     + Cascading a traffic policy over another will cause the device forwarding performance to deteriorate.
     + When the traffic on an interface matches the cascaded traffic policy:
       - The forwarding behavior and cascading a traffic policy are mutually exclusive.
       - If the traffic behaviors in the two traffic policies are different, they can be individually implemented.
       - If the traffic behaviors in the two traffic policies are the same, the specific behavior configuration in the cascaded traffic policy takes effect.
     + On an interface, only one traffic policy can be applied to outgoing or incoming packets. If the traffic policy cascades over another traffic policy and is applied to an interface, both traffic policies take effect on the direction-specific interface.
     + The parameters specified for a traffic policy to be applied to an interface, such as **inbound**, **outbound**, **link-layer**, all-layer, and **mpls-layer**, are inherited by a cascaded traffic policy.
     + When the traffic behaviors for two-level ACLs are **service-class**, level-1 **service-class** preferentially takes effect. However, if level 1 **service-class** carries **no-remark**, level-2 **service-class** preferentially takes effect.
   * To increase the priority of the traffic action, run the [**increase-priority**](cmdqueryname=increase-priority) command.
     
     If a traffic action is configured for both BGP Flow Specification and QPPB on a device, you can run this command to allow the traffic action configured for QPPB to preferentially take effect.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.