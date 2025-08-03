Binding a Service-Location Group to a VRRP Group
================================================

In the service-location group view, bind the service-location group to a configured VRRP group.

#### Context

Before the master/backup relationship of VRRP group members is bound to service-location group members, the service-location group must be bound to the VRRP group. Perform the following operations on both the master and backup devices.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* **virtual-ip** *virtual-address*
   
   
   
   A VRRP group is created, and a virtual IP address is configured for the VRRP group.
   
   The *virtual-router-id* and *virtual-address* values configured on both devices must be the same.
4. (Optional) Run [**admin-vrrp vrid**](cmdqueryname=admin-vrrp+vrid) *virtual-router-id*
   
   
   
   The VRRP group is configured as an mVRRP group.
5. Run [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* **priority** *priority-value*
   
   
   
   A priority is configured for the device in the VRRP group.
   
   Different priorities must be configured for devices in a VRRP group. The device with the highest priority is the master device.
6. Run [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* **preempt-mode** **timer** **delay** *delay-**time*
   
   
   
   A preemption delay is set for the device in the VRRP group.
   
   
   
   To ensure that NAT information is completely backed up, you are advised to perform this step to set the VRRP preemption delay to 1500s.
7. Run [**vrrp recover-delay**](cmdqueryname=vrrp+recover-delay) *delay-value*
   
   
   
   A recovery delay is set for the VRRP group.
   
   
   
   To ensure VRRP stability, you are advised to perform this step. The recovery delay of 15s is recommended.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
9. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
10. Run [**service-location**](cmdqueryname=service-location) *service-location-id*
    
    
    
    The service-location group view is displayed.
    
    The *service-location-id* values configured on both devices must be the same.
11. Run [**vrrp vrid**](cmdqueryname=vrrp+vrid) *vrrp-id* [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
    
    
    
    The service-location group is bound to the VRRP group.
    
    
    
    The *vrrp-id* values configured on both devices must be the same.
12. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.