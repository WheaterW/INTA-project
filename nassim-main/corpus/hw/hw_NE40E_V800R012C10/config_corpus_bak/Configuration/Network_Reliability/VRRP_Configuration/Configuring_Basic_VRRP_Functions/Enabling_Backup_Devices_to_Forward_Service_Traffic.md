Enabling Backup Devices to Forward Service Traffic
==================================================

To meet carrier-class reliability requirements, enable backup devices to forward service traffic.

#### Context

On the mobile bearer network shown in [Figure 1](#EN-US_TASK_0000001145980460__fig_dc_vrp_vrrp_cfg_013501), the User attached to the cell site gateway (CSG) is connected to PE1 and PE2 over the primary and secondary pseudo wires (PWs) and to PE3 and PE4 over the active and standby links. A Virtual Router Redundancy Protocol (VRRP) backup group is deployed on both PE3 and PE4. If PE1 fails, service traffic switches from the active link to the standby link immediately, but a master/backup VRRP switchover is performed between PE3 and PE4 after a delay. Therefore, service traffic is lost before the master/backup VRRP switchover is performed.

To resolve this issue and meet carrier-class reliability requirements, enable PE4 (the backup device) to forward service traffic. After the configuration is complete, PE4 forwards service traffic before a master/backup VRRP switchover is performed, which prevents service traffic loss.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

You can enable backup devices to forward service traffic on the master and backup devices in a VRRP group.


**Figure 1** Enabling backup devices to forward service traffic  
![](images/fig_dc_vrp_vrrp_cfg_013501.png)  

Perform the following steps on each device in a VRRP group:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of the interface on which the VRRP group is configured is displayed.
3. Run [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* **backup-forward**
   
   
   
   The backup devices in the VRRP group are enabled to forward service traffic.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.