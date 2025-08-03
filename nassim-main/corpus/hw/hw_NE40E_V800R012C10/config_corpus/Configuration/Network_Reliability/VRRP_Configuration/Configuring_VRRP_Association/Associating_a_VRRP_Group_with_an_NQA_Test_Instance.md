Associating a VRRP Group with an NQA Test Instance
==================================================

You can associate a VRRP group with an NQA test instance. If the status of the NQA test instance becomes Failed, NQA notifies the VRRP group of the status change to implement a rapid master/backup VRRP switchover.

#### Context

VRRP can detect an uplink VRRP-disabled interface fault on a VRRP-enabled Router. However, if Device C's Interface2 shown in [Figure 1](#EN-US_TASK_0172361779__fig_dc_vrp_vrrp_cfg_014001) goes Down and its IP address is unreachable, VRRP cannot detect the fault. As a result, user traffic is lost.

The NE40E supports NQA. NQA uses a test instance to send probe packets to check destination IP address reachability.

You can associate VRRP with an NQA test instance to track the master device's uplink (cross-device). If the uplink fails and hosts on the LAN cannot access the external network through the master Router, NQA instructs VRRP to reduce the master Router's priority by a specified value. In this way, another Router in the group has a higher priority, becomes the master, and takes over services, ensuring communication continuity between hosts on a LAN and an external network. After the uplink recovers, NQA instructs VRRP to restore the Router's priority.

[Figure 1](#EN-US_TASK_0172361779__fig_dc_vrp_vrrp_cfg_014001) shows VRRP association with an NQA test instance.

**Figure 1** VRRP association with an NQA test instance  
![](images/fig_dc_vrp_vrrp_cfg_014001.png)
![](../../../../public_sys-resources/note_3.0-en-us.png) 

* Before associating VRRP with an NQA test instance on a device, perform the following operations:
  + Create an NQA test instance on the device. For details, see *NE40E Configuration Guide - System Monitor*.
  + Create a VRRP group on the device.
* VRRP can be associated only with an ICMP NQA test instance.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of the interface on which the VRRP group is configured is displayed.
3. Run [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* **track nqa** *admin-name* *test-name* [ **reduced** *value-reduced* ]
   
   
   
   VRRP is associated with an NQA test instance.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.