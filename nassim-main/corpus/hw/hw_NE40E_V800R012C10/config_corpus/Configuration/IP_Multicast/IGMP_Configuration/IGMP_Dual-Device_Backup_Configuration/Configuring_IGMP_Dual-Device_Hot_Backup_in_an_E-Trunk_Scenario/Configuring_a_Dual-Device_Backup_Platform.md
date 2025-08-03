Configuring a Dual-Device Backup Platform
=========================================

This section describes how to configure a dual-device backup platform to back up IGMP entries. If a network node or link fails, a rapid multicast service switchover is triggered, improving service reliability.

#### Prerequisites

An Eth-Trunk interface has been created using the [**interface eth-trunk**](cmdqueryname=interface+eth-trunk) *trunk-id* command, and Ethernet interfaces have been added to the Eth-Trunk interface using the [**eth-trunk**](cmdqueryname=eth-trunk) *trunk-id* command.

An E-Trunk has been created using the [**e-trunk**](cmdqueryname=e-trunk) *e-trunk-id* command, and the Eth-Trunk interface has been added to the E-Trunk using the [**e-trunk**](cmdqueryname=e-trunk) *e-trunk-id* [ **remote-eth-trunk** *eth-trunk-id* ] command.

The Eth-Trunk interfaces on the master and backup devices have been configured to work in master mode using the [**e-trunk mode force-master**](cmdqueryname=e-trunk+mode+force-master) command if the E-Trunk works in active-active mode.


#### Context

In a master/backup E-Trunk scenario, a dual-device backup platform enables the master device to back up IGMP entries to the backup device through a remote backup service (RBS) channel, ensuring multicast service continuity. Configuring a dual-device backup platform includes configuring an RBS, a remote backup profile (RBP), and a dual-device E-Trunk backup platform.

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
3. Configure a dual-device E-Trunk backup platform.
   1. Run [**remote-backup-profile**](cmdqueryname=remote-backup-profile) *profile-name*
      
      
      
      An RBP is created, and the RBP view is displayed.
   2. Run [**e-trunk**](cmdqueryname=e-trunk) *e-trunk-id* **eth-trunk** *eth-trunk-id*
      
      
      
      An Eth-Trunk interface of an E-Trunk is bound to the RBP, enabling the RBP to use the Eth-Trunk interface status as the master/backup status.
   3. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   4. Run [**e-trunk**](cmdqueryname=e-trunk) *e-trunk-id*
      
      
      
      The E-Trunk view is displayed.
   5. Run [**peer-address**](cmdqueryname=peer-address) *peer-ip-address* **source-address** *source-ip-address*
      
      
      
      Peer and local IP addresses are set for the E-Trunk.
      
      
      
      The two IP addresses are peers for each other. For example, an E-Trunk is created between device A with IP address 1.1.1.1 and device B with IP address 2.2.2.2. Then, the peer IP address of device A is 2.2.2.2, and the peer IP address of device B is 1.1.1.1.
   6. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
4. (Optional) Configure rapid service link switchover.
   1. Run [**bfd**](cmdqueryname=bfd)
      
      
      
      BFD is enabled globally.
   2. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   3. Run [**bfd**](cmdqueryname=bfd) *session-name* **bind** **peer-ip** *ip-address*
      
      
      
      A BFD session is created to monitor a specified peer.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   5. Run [**bfd**](cmdqueryname=bfd) *session-name* **bind** **peer-ip** **default-ip** **interface** { *interface-name* | *interface-type* *interface-number* } 
      
      
      
      A BFD session is created to monitor a specified Eth-Trunk interface.
   6. Run [**discriminator**](cmdqueryname=discriminator) { **local** | **remote** } *discr-value*
      
      
      
      The local and remote discriminators are set.
   7. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   8. Run [**e-trunk**](cmdqueryname=e-trunk) *e-trunk-id*
      
      
      
      The E-Trunk view is displayed.
   9. Run [**e-trunk track bfd-session**](cmdqueryname=e-trunk+track+bfd-session) **session-name** *bfd-session-name*
      
      
      
      The E-Trunk is bound to the BFD session.
   10. Run [**quit**](cmdqueryname=quit)
       
       
       
       Return to the system view.
   11. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.