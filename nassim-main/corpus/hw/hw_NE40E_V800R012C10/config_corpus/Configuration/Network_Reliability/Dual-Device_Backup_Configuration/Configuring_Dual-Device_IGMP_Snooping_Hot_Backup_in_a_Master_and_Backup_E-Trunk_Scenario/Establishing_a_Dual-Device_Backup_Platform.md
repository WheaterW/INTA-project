Establishing a Dual-Device Backup Platform
==========================================

This section describes how to establish a dual-device backup platform to back up IGMP snooping entries. If a network node or link fails, a rapid Layer 2 multicast service switchover is triggered, improving service reliability.

#### Prerequisites

An Eth-Trunk interface has been created using the [**interface eth-trunk**](cmdqueryname=interface+eth-trunk) *trunk-id* command, and an Ethernet interface has been added to the Eth-Trunk interface using the [**eth-trunk**](cmdqueryname=eth-trunk) *trunk-id* command.

An E-Trunk has been created using the [**e-trunk**](cmdqueryname=e-trunk) *e-trunk-id* command, and the Eth-Trunk interface has been added to the E-Trunk using the [**e-trunk**](cmdqueryname=e-trunk) *e-trunk-id* [ **remote-eth-trunk** *eth-trunk-id* ] command.


#### Context

In a master/backup E-Trunk scenario, a dual-device backup platform enables the master device to back up IGMP snooping entries to the backup device through a remote backup service (RBS) channel, ensuring multicast service continuity. Establishing a dual-device backup platform includes configuring an RBS, a remote backup profile (RBP), and a dual-device E-Trunk backup platform.

Perform the following steps on both the master and backup devices:


#### Procedure

1. Configure an RBS.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**remote-backup-service**](cmdqueryname=remote-backup-service) *remote-backup-service-name*
      
      
      
      An RBS is created, and the RBS view is displayed.
   3. Run [**peer**](cmdqueryname=peer) *peer-ip-address* [**source**](cmdqueryname=source) *source-ip-address* [**port**](cmdqueryname=port) *port-id*
      
      
      
      TCP connection parameters are set for the RBS.
      
      The *source-ip-address* and *peer-ip-address* parameters specify the IP addresses of the local and remote devices, respectively. The IP addresses of the local and remote devices must have been configured on their own interfaces, sub-interfaces, or logical interfaces (such as loopback interfaces) and be able to ping each other.
      
      The *port-id* parameter specifies a TCP port number. The TCP port numbers configured on the local and remote devices must be the same.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
2. Configure an RBP.
   1. Run [**remote-backup-profile**](cmdqueryname=remote-backup-profile) *profile-name*
      
      
      
      An RBP is created, and the RBP view is displayed.
   2. Run [**backup-id**](cmdqueryname=backup-id) *backup-id* [**remote-backup-service**](cmdqueryname=remote-backup-service) *service-name*
      
      
      
      A user backup ID is configured for the RBP, and the RBP is associated with a specified RBS.
      
      The *backup-id* parameter specifies a user backup ID. You can use a backup ID and an RBS to determine an RBP. The backup IDs configured for the same RBP must be the same on the master and backup devices and can no longer be configured for other RBPs.
   3. Run [**peer-backup**](cmdqueryname=peer-backup) **hot**
      
      
      
      The backup type of the master device and backup device is set to hot backup mode.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
3. Configure a dual-device E-Trunk backup platform.
   1. Run [**remote-backup-profile**](cmdqueryname=remote-backup-profile) *profile-name*
      
      
      
      The RBP view is displayed.
   2. Run [**e-trunk**](cmdqueryname=e-trunk) *e-trunk-id* **eth-trunk** *eth-trunk-id*
      
      
      
      The E-Trunk master/backup protocol is configured, and the Eth-Trunk interface is bound to the RBP.
   3. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   4. Run [**e-trunk**](cmdqueryname=e-trunk) *e-trunk-id*
      
      
      
      The E-Trunk view is displayed.
   5. Run [**peer-address**](cmdqueryname=peer-address) *peer-ip-address* **source-address** *source-ip-address*
      
      
      
      IP addresses are assigned to the local and peer ends of the E-Trunk.
      
      The peer IP address of the local end is the local IP address of the peer end. For example, an E-Trunk is established between device A and device B. On device A, the peer IP address is 2.2.2.2 and the local IP address is 1.1.1.1. Then, on device B, the peer IP address is 1.1.1.1 and the local IP address is 2.2.2.2.
   6. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
4. (Optional) Configure rapid service link switching.
   1. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   2. Run [**bfd**](cmdqueryname=bfd)
      
      
      
      BFD is globally enabled.
   3. Run [**bfd**](cmdqueryname=bfd) *session-name* **bind** **peer-ip** *peer-ip*
      
      
      
      A BFD session for detecting the peer end is created.
   4. Run [**discriminator**](cmdqueryname=discriminator) [**local**](cmdqueryname=local) *discr-value*
      
      
      
      The local discriminator is set.
   5. Run [**discriminator**](cmdqueryname=discriminator) [**remote**](cmdqueryname=remote) *discr-value*
      
      
      
      The remote discriminator is set.
   6. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   7. Run [**bfd**](cmdqueryname=bfd) *sessname-value* **bind** **peer-ip** **default-ip** **interface** { *interface-name* | *interface-type* *interface-number* } [ **source-ip** *source-ip* ]
      
      
      
      A BFD session for detecting faults on the Eth-Trunk interface is created.
   8. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   9. Run [**e-trunk**](cmdqueryname=e-trunk) *e-trunk-id*
      
      
      
      The E-Trunk view is displayed.
   10. Run [**e-trunk track bfd-session**](cmdqueryname=e-trunk+track+bfd-session) **session-name***bfd-session-name*
       
       
       
       The BFD process is bound to the E-Trunk.
   11. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.