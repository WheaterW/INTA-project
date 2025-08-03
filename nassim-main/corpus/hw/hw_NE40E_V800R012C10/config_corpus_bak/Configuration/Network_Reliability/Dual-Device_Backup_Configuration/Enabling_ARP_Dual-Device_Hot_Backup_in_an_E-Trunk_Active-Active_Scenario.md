Enabling ARP Dual-Device Hot Backup in an E-Trunk Active-Active Scenario
========================================================================

ARP dual-device hot backup is configured. The E-Trunk protocol is configured. Dual-homing PEs on the access side are configured to work in active-active mode.

#### Usage Scenario

ARP dual-device hot backup is manually triggered to back up ARP entries if a link fails in an E-Trunk backup group, which prevents service interruptions in an E-Trunk active-active scenario.

**Figure 1** ARP dual-device hot backup in an E-Trunk active-active scenario  
![](images/fig_feature_image_0003991765.png)

#### Procedure

1. Create an RBS.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**remote-backup-service**](cmdqueryname=remote-backup-service) *remote-backup-service-name*
      
      
      
      An RBS is created, and the RBS view is displayed.
   3. Parameters of a TCP connection for the RBS are set.
      
      
      * On an IPv4 network, run:
        ```
        [peer](cmdqueryname=peer) peer-ip-address [source](cmdqueryname=source) source-ip-address [port](cmdqueryname=port) port-id
        ```
      * On an IPv6 network, run:
        ```
        [peer-ipv6](cmdqueryname=peer-ipv6)  peerIpv6 source-ipv6 source-ipv6-address port port-id
        ```
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
2. Configure a dual-device E-Trunk backup platform.
   1. Run [**e-trunk**](cmdqueryname=e-trunk) *e-trunk-id*
      
      
      
      An E-Trunk was created, and the E-Trunk view is displayed.
   2. IP addresses are configured for the source and peer ends of an E-Trunk link.
      
      
      * On an IPv4 network, run:
        ```
        [peer-address](cmdqueryname=peer-address) peer-ip-address source-address source-ip-address
        ```
      * On an IPv6 network, run:
        ```
        [peer-ipv6](cmdqueryname=peer-ipv6) peer-ipv6-address source-ipv6 source-ipv6-address
        ```
   3. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   4. Run [**interface eth-trunk**](cmdqueryname=interface+eth-trunk) *trunk-id*
      
      
      
      An Eth-Trunk interface is created.
   5. Run [**e-trunk**](cmdqueryname=e-trunk) *e-trunk-id*
      
      
      
      The Eth-Trunk interface is added to the E-Trunk interface.
   6. Run [**e-trunk mode**](cmdqueryname=e-trunk+mode) **force-master**
      
      
      
      The E-Trunk member interface is configured to work in the active state.
   7. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
3. Configuring the RBP.
   1. Run [**remote-backup-profile**](cmdqueryname=remote-backup-profile) *profile-name*
      
      
      
      The RBP view is displayed.
   2. Run [**backup-id**](cmdqueryname=backup-id) *backup-id* [**remote-backup-service**](cmdqueryname=remote-backup-service) *service-name*
      
      
      
      The RBP is associated with the RBS, and the user backup ID in the RBP is set.
      
      The *backup-id* parameter specifies a user backup ID. You can use a backup ID and an RBS to determine an RBP. The backup IDs configured for the same RBP must be the same on the master and backup devices and can no longer be configured for other RBPs.
   3. Run [**service-type arp**](cmdqueryname=service-type+arp)
      
      
      
      Remote backup is enabled for ARP services.
   4. Run [**e-trunk**](cmdqueryname=e-trunk) *e-trunk-id* **eth-trunk** *eth-trunk-id*
      
      
      
      The E-Trunk master/backup protocol is configured, and the E-Trunk is bound to the RBP.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
4. Bind the RBP to the Eth-Trunk interface.
   1. Run [**interface eth-trunk**](cmdqueryname=interface+eth-trunk) *trunk-id*
      
      
      
      The view of the created Eth-Trunk interface is displayed.
   2. Run [**remote-backup-profile**](cmdqueryname=remote-backup-profile) *profile-name*
      
      
      
      The RBP is bound to the Eth-Trunk interface.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.