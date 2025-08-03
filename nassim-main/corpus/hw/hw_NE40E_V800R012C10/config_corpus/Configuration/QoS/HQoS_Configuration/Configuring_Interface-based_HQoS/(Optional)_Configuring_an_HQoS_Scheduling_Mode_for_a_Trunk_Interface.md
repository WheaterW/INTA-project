(Optional) Configuring an HQoS Scheduling Mode for a Trunk Interface
====================================================================

(Optional) Configuring an HQoS Scheduling Mode for a Trunk Interface

#### Context

Trunk interfaces support the following HQoS scheduling modes:

* Member interface-based HQoS scheduling (that is, distribute mode): Each trunk member interface is independently scheduled, and scheduling resources are independently allocated to them. In this mode, if service congestion occurs on a member interface, services on other member interfaces are not affected. However, this mode consumes many scheduling resources. When downstream HQoS rate limiting is configured, the effective bandwidth is the configured bandwidth multiplied by the number of member interfaces.
* TM-based HQoS scheduling (that is, merge mode): The trunk interface is scheduled as a whole (meaning that member interfaces are not scheduled independently), and scheduling resources are allocated in a unified manner. However, in this mode, member interfaces affect each other if service congestion occurs.

Configure an HQoS scheduling mode for a trunk interface as required.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *trunk-type* *trunk-number*
   
   
   
   The trunk interface view is displayed.
3. Run [**qos schedule-tree distribute-mode outbound**](cmdqueryname=qos+schedule-tree+distribute-mode+outbound)
   
   
   
   The HQoS scheduling mode of the trunk interface is set to distribute, meaning that HQoS scheduling is performed based on trunk member interfaces.
   
   
   
   By default, TM-based HQoS scheduling is performed on a trunk interface. If traffic congestion occurs on some member interfaces, packet loss may occur on other non-congested member interfaces. In this case, the device reports an hwXQoSTrunkTrafficCongestionAlarm alarm (you can run the [**qos trunk traffic-congestion-alarm disable**](cmdqueryname=qos+trunk+traffic-congestion-alarm+disable) command in the system view to disable the alarm function). To resolve the preceding problem, perform this step.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.