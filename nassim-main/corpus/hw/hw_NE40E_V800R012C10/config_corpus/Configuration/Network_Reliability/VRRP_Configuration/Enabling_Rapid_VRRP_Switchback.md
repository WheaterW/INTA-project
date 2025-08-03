Enabling Rapid VRRP Switchback
==============================

This section describes how to enable rapid Virtual Router Redundancy Protocol (VRRP) switchback.

#### Context

The master device in a VRRP group monitors an interface with VRRP disabled or a session, for example, a Bidirectional Forwarding Detection (BFD) session. If the interface or session goes Down, the master device reduces its own VRRP priority to trigger a master/backup VRRP switchover. As shown in [Figure 1](#EN-US_TASK_0172361783__fig_dc_vrp_vrrp_cfg_013701), the network provider edges (NPEs) with VRRP enabled are connected to the provider edges (PEs) over the active and standby links. User-side traffic is transmitted to NPE1 (master) over the active link. NPE1 then forwards the user-side traffic to the Internet.

If the interface monitored by NPE1 or the active link to NPE1 fails, NPE1 reduces its own VRRP priority and enters the Backup state. User-side traffic then switches to the standby link. After the fault is rectified, the monitored interface or active link goes Up and NPE1 increases its own VRRP priority. NPE1 can switch back to the Master state only after NPE1's VRRP priority is higher than NPE2's and NPE1 receives VRRP Advertisement packets from NPE2. If the active/standby link switchback is finished before the master/backup VRRP switchback, user-side traffic is lost. To resolve this issue, enable rapid VRRP switchback.

When NPE1's VRRP priority is higher than NPE2's, rapid VRRP switchback enables NPE1 to immediately preempt the Master state without waiting for VRRP Advertisement packets from NPE2.

**Figure 1** Enabling rapid VRRP switchback  
![](images/fig_dc_vrp_vrrp_cfg_013701.png)  

![](../../../../public_sys-resources/note_3.0-en-us.png) Rapid VRRP switchback takes effect only when all of the following conditions are true:

* The VRRP group is a management VRRP (mVRRP) group.
* The master device is monitoring an interface with VRRP disabled or a session.
* The master device reduces its own VRRP priority if the interface or session goes Down.

Perform the following steps on the master device in an mVRRP group:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of the interface on which an mVRRP group is configured is displayed.
3. (Optional) Run [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* [**preempt-mode timer delay**](cmdqueryname=preempt-mode+timer+delay) **0**
   
   
   
   The preemption delay is set to 0 seconds.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This step is required only when you have set the preemption delay to a non-zero value.
4. Run [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* **fast-resume**
   
   
   
   Rapid VRRP switchback is enabled.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The [**vrrp vrid fast-resume**](cmdqueryname=vrrp+vrid+fast-resume) command takes precedence over the [**vrrp recover-delay**](cmdqueryname=vrrp+recover-delay) command. For example, if you enable rapid VRRP switchback for VRRP group 1 and globally set the recovery delay to a non-zero value, the configured recovery delay does not take effect.
   
   After you run the [**vrrp vrid fast-resume**](cmdqueryname=vrrp+vrid+fast-resume) command to enable rapid VRRP switchback, this function is disabled if any of the following conditions is true:
   * The preemption delay is set to a non-zero value.
   * VRRP devices are disabled from preempting the Master state.
   * The mVRRP group is deleted.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.