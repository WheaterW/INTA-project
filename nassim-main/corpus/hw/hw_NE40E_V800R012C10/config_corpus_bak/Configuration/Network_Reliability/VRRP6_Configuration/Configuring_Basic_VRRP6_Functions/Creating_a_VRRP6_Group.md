Creating a VRRP6 Group
======================

You can create a VRRP6 group and set VRRP6 priorities to determine the master and backup Routers. The master Router transmits service traffic. You can create multiple VRRP6 groups to load-balance service traffic.

#### Context

* Multi-gateway load balancing: Multiple VRRP6 groups with virtual IPv6 addresses are created and specified as gateways for different users to implement load balancing.
  
  **Figure 1** Multi-gateway load balancing  
  ![](images/fig_dc_vrp_vrrp6_cfg_010401.png)
  As shown in [Figure 1](#EN-US_TASK_0172361846__fig_dc_vrp_vrrp6_cfg_010401), VRRP6 groups 1 and 2 have been deployed on the network.
  + VRRP6 group 1: Device1 is the master device, and Device2 is the backup device.
  + VRRP6 group 2: Device2 is the master device, and Device1 is the backup device.
  
  Some users access the Internet using VRRP6 group 1, and others access the Internet using VRRP6 group 2. The groups can load-balance service traffic and back up each other.


#### Procedure

* Create a VRRP6 group working in master/backup mode.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
     
     
     
     IPv6 is enabled on the interface.
  4. Run [**ipv6 address**](cmdqueryname=ipv6+address) { *ipv6-address prefix-length* | *ipv6-address-mask* }
     
     
     
     An IPv6 address is configured for the interface.
  5. Run [**vrrp6 vrid**](cmdqueryname=vrrp6+vrid) *virtual-router-id* [ **virtual-ip** *virtual-address* [ **link-local** ] ]
     
     
     
     A VRRP6 group is created and assigned the first virtual IPv6 address.
     
     
     
     When a VRRP6 group is created on an interface, the first virtual IPv6 address assigned to the VRRP6 group must be a **link-local** address.
     
     When the first virtual IPv6 address is assigned to a VRRP6 group, the system creates the VRRP6 group. If another virtual IPv6 address is assigned to the VRRP6 group, the system adds the address to the virtual IPv6 address list.
  6. Run [**vrrp6 vrid**](cmdqueryname=vrrp6+vrid) *virtual-router-id* **virtual-ip** *virtual-address*
     
     
     
     A virtual IPv6 address is assigned to the VRRP6 group.
     
     
     
     Multiple virtual IPv6 addresses can be assigned to a VRRP6 group. A single virtual IPv6 address serves a separate user group, in which users have the same reliability requirements. This setting helps prevent the default gateway addresses from varying according to changes in VRRP6 device locations.
  7. Run [**vrrp6 vrid**](cmdqueryname=vrrp6+vrid) *virtual-router-id* **priority** *priority-value*
     
     
     
     A priority is configured for the Router in the VRRP6 group.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + The master device's priority must be higher than a backup device's priority.
     + If devices have the same priority, the device that enters the Master state earlier than others is the master device. Other devices are backup devices and stop preempting the Master state.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Create VRRP6 groups working in multi-gateway load balancing mode.
  
  
  
  If VRRP6 groups need to work in multi-gateway load balancing mode, repeat the steps to configure two or more VRRP6 groups on the interface and assign different VRIDs to them.