Configuring Scheduling Parameters for User-Queue
================================================

Configuring_Scheduling_Parameters_for_User-Queue

#### Context

By default, HQoS is disabled on an interface. You can enable HQoS on an interface by configuring user-queue.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run the corresponding command to configure scheduling parameters for user-queue based on the interface type.
   
   
   * For a serial interface configured with HDLC or PPP or an MP group interface, run the [**user-queue cir**](cmdqueryname=user-queue+cir) *cir-value* [ [ **pir** *pir-value* ] | [ **flow-queue** *flow-queue-name* ] | [ **flow-mapping** *mapping-name* ] | [ **user-group-queue** *group-name* ] ] \* { **inbound** | **outbound** } [ **service-template** *template-name* ] command.
   * For other types of interfaces, run the [**user-queue cir**](cmdqueryname=user-queue+cir) *cir-value* [ [ **pir** *pir-value* ] | [ **flow-queue** *flow-queue-name* ] | [ **user-group-queue** *group-name* ] ] \* { **inbound** **car-mode** | **outbound** } [ **service-template** *template-name* [ **adjust-on-card** ] ] or [**user-queue cir**](cmdqueryname=user-queue+cir) *cir-value* **flow-mapping** *mapping-name* { **inbound** | **outbound** } [ **service-template** *template-name* ] command.
4. (Optional) Run [**user-queue shaping ldp-traffic outbound**](cmdqueryname=user-queue+shaping+ldp-traffic+outbound)
   
   
   
   HQoS is configured to take effect for L3VPN, IP, VLL, VPLS, and EVPN traffic on the interface.
5. (Optional) Run [**user-queue shaping bgp-local-ifnet-traffic outbound**](cmdqueryname=user-queue+shaping+bgp-local-ifnet-traffic+outbound)
   
   
   
   HQoS is enabled for traffic transmitted over a BGP local IFNET tunnel on the interface.
   
   
   
   When HQoS has been configured on interfaces along a BGP local IFNET tunnel and the outbound interface resides on a downstream non-eTM subcard, perform this step for the HQoS configuration to take effect.
6. (Optional) Run [**qos default user-queue**](cmdqueryname=qos+default+user-queue) { **cir** *cir-value* | **pir** *pir-value* | **cbs** *cbs-value* | **pbs** *pbs-value* | **weight** *weight-value* } \* **outbound**
   
   
   
   The default user-queue scheduling parameters are modified.
7. (Optional) Run [**qos default user-group-queue**](cmdqueryname=qos+default+user-group-queue) **shaping** *shaping-value* [ **pbs** *pbs-value* ] [ **weight** *weight-value* ] **outbound**
   
   
   
   Traffic shaping parameters of the default GQ are configured.
8. (Optional) Run [**qos default user-group-queue**](cmdqueryname=qos+default+user-group-queue) { **cir** *cir-value* [ **cbs** *cbs-value* ] [ **pir** *pir-value* [ **pbs** *pbs-value* ] ] | [ **weight** *weight-value* ] } \* **outbound**
   
   
   
   Scheduling parameters of the default GQ are configured.
9. Run [**quit**](cmdqueryname=quit)
   
   
   
   Exit the interface view.
10. (Optional) Run [**slot**](cmdqueryname=slot) *slot-id*
    
    
    
    The slot view is displayed.
11. (Optional) Run [**qos pir-precision user-queue precision**](cmdqueryname=qos+pir-precision+user-queue+precision) *precision-value*
    
    
    
    The allowed deviation between the actual and configured bandwidth values of user-queue is configured.
12. (Optional) Run [**qos user-queue burst-size bytes**](cmdqueryname=qos+user-queue+burst-size+bytes) *min-bytes* **time** *burst-time*
    
    
    
    The minimum default burst size and burst time are configured for user-queue.
13. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.