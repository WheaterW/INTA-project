Configuring a Dual-Device Backup Platform
=========================================

This section describes how to configure a dual-device backup platform to back up IGMP entries. If a network node or link fails, a rapid multicast service switchover is triggered, improving service reliability.

#### Prerequisites

A VRRP group has been created using the [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* [ **virtual-ip** *virtual-address* ] command.

An mVRRP group has been created using the [**admin-vrrp vrid**](cmdqueryname=admin-vrrp+vrid) *virtual-router-id* [ **ignore-if-down** ] command.


#### Context

In a VRRP master/backup scenario, a dual-device backup platform enables the master device to back up IGMP entries to the backup device through a remote backup service (RBS) channel, ensuring multicast service continuity. Configuring a dual-device backup platform includes configuring an RBS, a remote backup profile (RBP), and a dual-device VRRP backup platform.

Perform the following steps on both the master and backup devices:


#### Procedure

1. Configure an RBS.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**remote-backup-service**](cmdqueryname=remote-backup-service) *remote-backup-service-name*
      
      
      
      An RBS is created, and the RBS view is displayed.
   3. Run [**peer**](cmdqueryname=peer) *peer-ip-address* [**source**](cmdqueryname=source) *source-ip-address* [**port**](cmdqueryname=port) *port-id*
      
      
      
      TCP connection parameters are set for the RBS.
      
      
      
      *peer-ip-address* specifies the IP address of the peer device that backs up the local device. *source-ip-address* specifies the IP address of the local device. The IP addresses of the master and backup devices must have been configured on their own interfaces, sub-interfaces, or logical interfaces (such as loopback interfaces) and be able to ping each other.
      
      *port-id* specifies a TCP port number. The TCP port numbers configured on the master and backup devices must be the same.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
2. Configure an RBP.
   1. Run [**remote-backup-profile**](cmdqueryname=remote-backup-profile) *profile-name*
      
      
      
      An RBP is created, and the RBP view is displayed.
   2. Run [**backup-id**](cmdqueryname=backup-id) *backup-id* [**remote-backup-service**](cmdqueryname=remote-backup-service) *service-name*
      
      
      
      A backup ID is set for the RBP, and the RBP is associated with a specified RBS.
      
      
      
      *backup-id* specifies a backup ID for an RBP. You can use a backup ID and an RBS to determine an RBP. The backup IDs configured for the same RBP must be the same on the master and backup devices and can no longer be configured for other RBPs.
   3. Run [**peer-backup**](cmdqueryname=peer-backup) **hot**
      
      
      
      Hot backup is configured for user information backup between the master and backup devices.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
3. Configure a dual-device VRRP backup platform.
   1. Run [**remote-backup-profile**](cmdqueryname=remote-backup-profile) *profile-name*
      
      
      
      An RBP is created, and the RBP view is displayed.
   2. Run [**vrrp-id**](cmdqueryname=vrrp-id) *vrid* **interface** *interface-type* *interface-number*
      
      
      
      The ID and interface of a VRRP group are associated with the RBP.
   3. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   4. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
4. Configure rapid service link switching.
   1. Run [**monitor-group**](cmdqueryname=monitor-group) *monitor-group-name*
      
      
      
      An interface monitoring group is created, and the group view is displayed.
   2. Run [**monitor enable**](cmdqueryname=monitor+enable)
      
      
      
      The monitoring function is enabled for the interface monitoring group.
   3. Run [**binding interface**](cmdqueryname=binding+interface) *interface-name*
      
      
      
      The interface to be monitored is added to the interface monitoring group.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   5. Run [**multicast routing-enable**](cmdqueryname=multicast+routing-enable)
      
      
      
      IP multicast routing is enabled.
   6. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
      
      
      
      The interface view is displayed.
   7. Run [**pim sm**](cmdqueryname=pim+sm)
      
      
      
      PIM-SM is enabled on the interface.
   8. Run [**igmp enable**](cmdqueryname=igmp+enable)
      
      
      
      IGMP is enabled.
   9. (On the interface that connects the master and backup devices) Run [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* **track** **monitor-group** [ *monitor-group-name* ] **failure-ratio** *failure-ratio-value* [ **link** | [ **reduced** *priority-value* ] ]
      
      
      
      The service VRRP group is enabled to track the interface monitoring group.
   10. (On the interface that connects to a downstream device) Run [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id1* **track** **admin-vrrp** **interface** *interface-type* *interface-number* **vrid** *virtual-router-id2*
       
       
       
       The service VRRP group is bound to the mVRRP group in flowdown mode.
   11. (On the interface that connects to a downstream device) Run [**multicast track admin-vrrp**](cmdqueryname=multicast+track+admin-vrrp) **interface** *interface-type* *interface-number* **vrid** *vrid-value*
       
       
       
       The multicast service interface is bound to the mVRRP group.
   12. (On the interface that connects to a downstream device) Run [**pim ignore dr-state**](cmdqueryname=pim+ignore+dr-state)
       
       
       
       The interface is enabled to ignore the PIM DR state.
   13. (On the interface that connects to a downstream device) Run [**pim ignore assert-state**](cmdqueryname=pim+ignore+assert-state)
       
       
       
       The interface is enabled to ignore the PIM Assert state.
   14. (On the interface that connects to a downstream device) Run [**remote-backup-profile**](cmdqueryname=remote-backup-profile) *profile-name*
       
       
       
       The interface is bound to the RBP.
   15. (On the interface that connects to a downstream device) Run [**quit**](cmdqueryname=quit)
       
       
       
       Return to the system view.
   16. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.