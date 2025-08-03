Creating a VRRP Group
=====================

You can create a Virtual Router Redundancy Protocol (VRRP) backup group and set VRRP priorities to determine the master and backup Routers. The master Router transmits data traffic. You can create multiple VRRP groups to load-balance data traffic.

#### Context

VRRP load balancing is classified as multi-gateway load balancing.

* Multi-gateway load balancing: Multiple VRRP groups with virtual IP addresses are created and specified as gateways for different users to implement load balancing.
  
  **Figure 1** Multi-gateway load balancing  
  ![](images/fig_dc_vrp_vrrp_cfg_010501.png)
  As shown in [Figure 1](#EN-US_TASK_0172361749__fig_dc_vrp_vrrp_cfg_010501), VRRP groups 1 and 2 are deployed on the network.
  + VRRP group 1: Device A is the master device, and Device B is the backup device.
  + VRRP group 2: Device B is the master device, and Device A is the backup device.
  
  Some users access the Internet using VRRP group 1, and others access the Internet using VRRP group 2. The backup groups can load-balance service traffic and back up each other.


#### Procedure

* Create a VRRP group working in master/backup mode.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* **virtual-ip** *virtual-address*
     
     
     
     A VRRP group is created and assigned a virtual IP address.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + VRRP groups cannot share virtual IP addresses.
     + Two devices in a single VRRP group must be configured with the same virtual router ID (VRID).
     + VRRP groups on different interfaces of a device can be configured with the same VRID.
     
     Multiple virtual IP addresses can be assigned to a VRRP group. A single virtual IP address serves a separate user group, in which users have the same reliability requirements. This setting helps prevent the default gateway addresses from varying according to changes in VRRP device locations.
     
     A VRRP group is created and assigned the first virtual IP address at the same time. If another virtual IP address is assigned to the VRRP group, the system only adds the virtual IP address to the virtual IP address list for the VRRP group.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Direct routes destined for virtual IP addresses of a VRRP group can be imported to OSPF, IS-IS, and RIP. On a live network, there may be a large number of routes destined for virtual IP addresses of VRRP groups; therefore, if OSPF, IS-IS, or RIP imports and advertises these routes to neighbors, some devices on the network may be overloaded, and network performance may be impacted. To resolve this issue, run the [**vrrp virtual-ip route-advertise disable**](cmdqueryname=vrrp+virtual-ip+route-advertise+disable) command to disable OSPF, IS-IS, and RIP from advertising the routes destined for virtual IP addresses of VRRP groups to neighbors.
  4. Run [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* **priority** *priority-value*
     
     
     
     A VRRP priority is set for the Router.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + The master device's priority must be higher than a backup device's priority. Using the default priority on a backup device is recommended.
     + If devices have the same VRRP priority, the device that enters the Master state earlier than others is the master device. Other devices are backup devices and stop preempting the Master state.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Create VRRP groups working in multi-gateway load balancing mode.
  
  
  
  If VRRP groups need to work in multi-gateway load balancing mode, repeat the steps to configure two or more VRRP groups on the interface and assign different VRIDs to them.