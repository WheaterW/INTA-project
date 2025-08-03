Configuring MLD Dual-Device Hot Backup in an E-Trunk Master/Backup Active-Active Scenario
=========================================================================================

MLD dual-device backup backs up multicast user join information between devices, improving multicast service continuity and reliability.

#### Procedure

1. Configure an RBS.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**remote-backup-service**](cmdqueryname=remote-backup-service) *remote-backup-service-name*
      
      
      
      An RBS is created, and the RBS view is displayed.
   3. Run [**peer-ipv6**](cmdqueryname=peer-ipv6) *peer-ipv6-address* [**source-ipv6**](cmdqueryname=source-ipv6) *source-ipv6-address* [**port**](cmdqueryname=port) *port-id*
      
      
      
      TCP connection parameters are configured for the RBS.
      
      
      
      *peer-ipv6-address* specifies the IP address of the peer device that backs up the local device. *source-ipv6-address* specifies the IP address of the local device. The IP address of the peer device must have been configured on a main interface, sub-interface, or logical interface (such as a loopback interface) of the peer device. The IP address of the local device must have been configured on a main interface, sub-interface, or logical interface (such as a loopback interface) of the local device. In addition, the two devices must be able to ping each other through the two IP addresses.
      
      *port-id* specifies a TCP port number. The TCP port numbers configured on the master and backup devices must be the same.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
2. Configure an RBP.
   1. Run [**remote-backup-profile**](cmdqueryname=remote-backup-profile) *profile-name*
      
      
      
      An RBP is created, and the RBP view is displayed.
   2. Run [**backup-id**](cmdqueryname=backup-id) *backup-id* [**remote-backup-service**](cmdqueryname=remote-backup-service) *service-name*
      
      
      
      A backup ID is configured for the RBP, and the RBP is associated with a specified RBS.
      
      
      
      *backup-id* specifies a backup ID. You can use a backup ID and an RBS to determine an RBP. The backup IDs configured for the same RBP must be the same on the master and backup devices and cannot be configured for other RBPs.
   3. Run [**peer-backup**](cmdqueryname=peer-backup) **hot**
      
      
      
      Hot backup is configured for information backup between the master and backup devices.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
3. Configure a dual-device E-Trunk backup platform.
   1. Run [**remote-backup-profile**](cmdqueryname=remote-backup-profile) *profile-name*
      
      
      
      The RBP view is displayed.
   2. Run [**e-trunk**](cmdqueryname=e-trunk) *e-trunk-id* **eth-trunk** *eth-trunk-id*
      
      
      
      The E-Trunk master/backup protocol is configured, and an Eth-Trunk interface is bound to the RBP.
   3. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   4. Run [**e-trunk**](cmdqueryname=e-trunk) *e-trunk-id*
      
      
      
      The E-Trunk view is displayed.
   5. Run [**priority**](cmdqueryname=priority) **priority**
      
      
      
      An E-Trunk priority is configured.
   6. Run **[**security-key**](cmdqueryname=security-key)** { ****simple**** **simple-key** | ****cipher**** **cipher-key** }
      
      
      
      An E-Trunk encryption password is configured.
   7. Run [**peer-ipv6**](cmdqueryname=peer-ipv6) *peer-ipv6-address* **source-ipv6** *source-ipv6-address*
      
      
      
      Peer and local IP addresses are set for the E-Trunk.
      
      
      
      The peer IP address of the local end is the local IP address of the peer end.
   8. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
4. Configure the E-Trunk interface to work in the master state.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**interface eth-trunk**](cmdqueryname=interface+eth-trunk) *trunk-id*
      
      
      
      The Eth-Trunk interface view is displayed.
   3. Run **[**e-trunk**](cmdqueryname=e-trunk) **mode force-master****
      
      
      
      The E-Trunk member interface is configured to work in the master state.
      
      
      
      In an active-active scenario, this command must be configured on Eth-Trunk interfaces of both the master and backup devices.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
5. (Optional) Configure rapid service link switching.
   1. Run [**bfd**](cmdqueryname=bfd)
      
      
      
      BFD is enabled globally.
   2. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   3. Run **[**bfd**](cmdqueryname=bfd)** **session-name** **[**bind**](cmdqueryname=bind)** **[**peer-ipv6**](cmdqueryname=peer-ipv6)** **peer-ipv6** [ **vpn-instance****vpn-name** ] [ **source-ipv6****source-ipv6** ] **[**track-interface**](cmdqueryname=track-interface)** **interface** { **interface-name** | *interface-type* *i*nterface-number**}
      
      
      
      A BFD for IPv6 session is created, related information is bound to the session, and the BFD session view is displayed.
   4. Run [**discriminator**](cmdqueryname=discriminator) { **local** | **remote** } *discr-value*
      
      
      
      Local and remote discriminators are configured.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   6. Run [**e-trunk**](cmdqueryname=e-trunk) *e-trunk-id*
      
      
      
      The E-Trunk view is displayed.
   7. Run [**e-trunk track bfd-session**](cmdqueryname=e-trunk+track+bfd-session)
      
      
      
      The E-Trunk is bound to the BFD session.
   8. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   9. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
6. Enable remote backup for MLD.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**remote-backup-profile**](cmdqueryname=remote-backup-profile) *profile-name*
      
      
      
      The RBP view is displayed.
   3. Run [**service-type mld**](cmdqueryname=service-type+mld)
      
      
      
      Remote backup is enabled for MLD services.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   5. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
      
      
      
      The interface view is displayed.
   6. (On the interface connected to a downstream device) Run [**remote-backup-profile**](cmdqueryname=remote-backup-profile) *profile-name*
      
      
      
      The RBP is bound to the interface.
   7. (On the interface connected to a downstream device) Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   8. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.