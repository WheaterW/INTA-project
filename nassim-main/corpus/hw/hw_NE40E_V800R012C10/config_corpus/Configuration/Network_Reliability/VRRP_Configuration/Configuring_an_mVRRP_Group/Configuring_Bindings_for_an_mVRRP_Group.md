Configuring Bindings for an mVRRP Group
=======================================

VRRP groups, service interfaces, and service PWs can be bound to an mVRRP group. After the bindings are configured, the mVRRP group determines the status of the bound objects.

#### Context

[Table 1](#EN-US_TASK_0172361769__tab_dc_vrp_vrrp_cfg_014201) describes objects that can be bound to an mVRRP group and usage scenarios.

**Table 1** Objects that can be bound to an mVRRP group and usage scenarios
| Object | Usage Scenario |
| --- | --- |
| Common VRRP group | If multiple VRRP groups are configured to forward traffic, large numbers of VRRP Advertisement packets are generated, which consumes network bandwidth resources and affects CPU performance. To resolve this issue, configure an mVRRP group and bind common VRRP groups to the mVRRP group. The mVRRP group sends VRRP Advertisement packets to determine the master/backup status of the common VRRP groups. |
| VRRP-disabled interface | VRRP-disabled interfaces can be bound to an mVRRP group. A master/backup mVRRP switchover can trigger an active/standby switchover on these interfaces, preventing traffic loss. |
| Service PW | Service PWs can be bound to an mVRRP group. A master/backup mVRRP switchover can trigger a primary/secondary switchover on these service PWs, preventing traffic loss. |




#### Procedure

* Bind a common VRRP group to an mVRRP group.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number* [ *subinterface-number* ]
     
     
     
     The view of the interface on which a common VRRP group is configured is displayed.
     
     
     
     A common VRRP group and an mVRRP group must be configured on different interfaces.
  3. Run [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id1* **track** **admin-vrrp** **interface** *interface-type interface-number* **vrid** *virtual-router-id2* [ **unflowdown** ]
     
     
     
     The common VRRP group is bound to an mVRRP group.
     
     
     
     Member VRRP groups can be bound to the mVRRP group in flowdown or unflowdown mode.
     + flowdown: This mode is used on a network where the upstream and downstream traffic forwarding paths must be the same. On a network configured with a firewall and a VRRP group, upstream traffic flows through the master device and the downstream traffic flows through either the master or backup device. If downstream traffic flows through the backup device and the firewall detects inconsistency between the upstream traffic path and downstream traffic path, the backup device has to discard downstream traffic. The default flowdown mode is used to allow the downstream traffic to be forwarded through the master device so that the firewall allows the packets to pass through.
     + unflowdown: This mode is used on a network where the upstream and downstream traffic forwarding paths do not need to be the same. **unflowdown** can be configured to allow the mVRRP group to determine the states of its bound VRRP group. This means that upstream traffic travels through the master device and then reaches the upper-layer network and downstream traffic travels through either the master or backup device and reaches the user.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Bind a VRRP-disabled interface to an mVRRP group.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number* [ *subinterface-number* ]
     
     
     
     The view of the VRRP-disabled interface is displayed.
  3. Run [**track admin-vrrp**](cmdqueryname=track+admin-vrrp) **interface** *interface-type* *interface-number* **vrid** *virtual-router-id*
     
     
     
     The VRRP-disabled interface is bound to an mVRRP group.
     
     
     
     After the binding is complete, the status of the VRRP-disabled interface depends on the status of the mVRRP group.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Bind a service PW to an mVRRP group.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the interface on which a service PW is configured is displayed.
  3. Run [**mpls l2vc track admin-vrrp**](cmdqueryname=mpls+l2vc+track+admin-vrrp) **interface** *interface-type* *interface-number* **vrid** *virtual-router-id* **pw-redundancy**
     
     
     
     The service PW is bound to an mVRRP group.
     
     
     
     After the binding is complete, the status of the service PW depends on the status of the mVRRP group.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.