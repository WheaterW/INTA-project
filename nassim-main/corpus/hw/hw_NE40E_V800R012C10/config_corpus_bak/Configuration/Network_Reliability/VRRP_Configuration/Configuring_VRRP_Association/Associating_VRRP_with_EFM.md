Associating VRRP with EFM
=========================

You can associate the Virtual Router Redundancy Protocol (VRRP) with Ethernet in the First Mile (EFM) to implement a rapid master/backup VRRP switchover.

#### Context

You can configure a VRRP group to monitor a Bidirectional Forwarding Detection (BFD) session to implement a rapid master/backup VRRP switchover. However, this method does not apply to some networks or devices that do not support BFD. If a device does not support BFD but supports EFM, you can use EFM to implement rapid master/backup VRRP switchovers.

On the network shown in [Figure 1](#EN-US_TASK_0172361775__fig_dc_vrp_vrrp_cfg_013601), the user-end provider edge (UPE) does not support BFD. Therefore, EFM is used to monitor the link between a local network provider edge (NPE) and the UPE, and peer BFD is used to monitor the link between the local and remote NPEs. After you associate VRRP with EFM, a rapid master/backup VRRP switchover can be implemented based on the status of EFM and peer BFD sessions.

**Figure 1** VRRP association with EFM  
![](images/fig_dc_vrp_vrrp_cfg_013601.png)  

Perform the following steps on the device in a VRRP group:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of the interface on which the VRRP group is configured is displayed.
3. Run [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* **track efm** **interface** *interface-type interface-number*
   
   
   
   The VRRP group is configured to monitor the specified EFM session.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.