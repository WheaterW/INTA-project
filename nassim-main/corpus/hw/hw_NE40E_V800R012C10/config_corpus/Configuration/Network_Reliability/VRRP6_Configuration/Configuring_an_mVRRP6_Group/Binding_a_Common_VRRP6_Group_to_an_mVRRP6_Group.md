Binding a Common VRRP6 Group to an mVRRP6 Group
===============================================

A common VRRP6 group can be bound to an mVRRP6 group. The mVRRP6 group determines the master/backup status of the common VRRP6 group.

#### Context

After you create an mVRRP6 group, bind a common VRRP6 group to the mVRRP6 group. After the binding is complete, the common VRRP6 group no longer sends VRRP6 Advertisement packets and its status is determined by the mVRRP6 group and the status of the interface on which the common VRRP6 group is configured.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of the interface where a common VRRP6 group resides is displayed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   A common VRRP6 group and an mVRRP6 group must be configured on different interfaces.
3. Run [**vrrp6 vrid**](cmdqueryname=vrrp6+vrid) *virtual-router-id1* **track** **admin-vrrp6** **interface** *interface-type* *interface-number* **vrid** *virtual-router-id2* [ **unflowdown** ]
   
   
   
   The common VRRP6 group is bound to a specified mVRRP6 group.
   
   
   
   A common VRRP6 group can be bound to an mVRRP6 group in either of the following modes:
   * Flowdown mode: When an mVRRP6 group is in the Backup or Initialize state, the interface on which a service VRRP6 group bound to the mVRRP6 group goes down and the service VRRP6 group switches to the Initialize state. The flowdown mode applies to networks on which both user-to-network and network-to-user traffic is transmitted over the same path. When a firewall is deployed in VRRP6 networking scenarios, it checks the paths for transmitting user-to-network and network-to-user traffic. Network-to-user traffic cannot pass through the firewall if it travels over a path different from the one used by user-to-network traffic. As a result, a backup router discards network-to-user traffic. To ensure that traffic is forwarded properly, specify the flowdown mode to enable network-to-user traffic to be forwarded over the same path as user-to-network traffic.
   * Unflowdown mode: When an mVRRP6 group is in the Backup or Initialize state, the interface on which a service VRRP6 group bound to the mVRRP6 group does not go down and the service VRRP6 group remains in the same state as the mVRRP6 group. The unflowdown mode applies to networks on which user-to-network and network-to-user traffic can be transmitted over different paths. User-to-network traffic is forwarded only through the master router, whereas network-to-user traffic can be forwarded through the master or backup router.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.