Configuring MLD Dual-Device Hot Backup in a VRRP6 Master/Backup Backup Scenario
===============================================================================

MLD dual-device backup backs up multicast user join information between devices, improving multicast service continuity and reliability.

#### Prerequisites

Before configuring MLD dual-device hot backup in a VRRP6 master/backup backup scenario, complete the following tasks:

* Assign IP addresses to loopback interfaces on the master and backup devices and configure routing protocols to ensure network-layer route reachability.
* Configure common VRRP6 and mVRRP6 groups.

#### Context

MLD dual-device hot backup in a VRRP6 master/backup backup scenario uses an RBS channel to back up MLD information between devices. Such implementation helps the system control and manage multicast services more flexibly, improving reliability of the services.


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
3. Configure a dual-device VRRP backup platform.
   1. Run [**remote-backup-profile**](cmdqueryname=remote-backup-profile) *profile-name*
      
      
      
      The RBP view is displayed.
   2. Run [**vrrp6-id**](cmdqueryname=vrrp6-id) *vrid* **interface** *interface-type* *interface-number*
      
      
      
      The ID and interface of a VRRP6 backup group are associated with the RBP.
   3. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   4. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
4. Configure rapid service link switching.
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
   6. Run [**multicast ipv6 routing-enable**](cmdqueryname=multicast+ipv6+routing-enable)
      
      
      
      IPv6 multicast routing is enabled.
   7. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
      
      
      
      The interface view is displayed.
   8. Run **pim ipv6 sm**
      
      
      
      IPv6 PIM is enabled on the interface.
   9. Run [**mld enable**](cmdqueryname=mld+enable)
      
      
      
      MLD is enabled.
   10. Run **[**vrrp6 vrid**](cmdqueryname=vrrp6+vrid)** **virtual-router-id** [ ****virtual-ip******virtual-address**[ **link-local** ] ]
       
       
       
       A VRRP6 group and a virtual IPv6 address are configured.
   11. (On the master device) Run [**vrrp6 vrid**](cmdqueryname=vrrp6+vrid) *virtual-router-id* **track** **bfd-session** *bfd-session-id* [ **increased** *value-increased* | [ **reduced** *value-reduced* ] ]
       
       
       
       The VRRP6 group is configured to track a BFD session.
   12. (On the backup device) Run **[**vrrp6 vrid**](cmdqueryname=vrrp6+vrid)** *virtual-router-id*[**track bfd-session**](cmdqueryname=track+bfd-session) **bfd-session-id** { ****peer**** | ****link**** }
       
       
       
       The VRRP6 group is configured to track a BFD session.
   13. (On the interface connected to a downstream device) Run [**vrrp6 vrid**](cmdqueryname=vrrp6+vrid) *virtual-router-id1* **track** **admin-vrrp6** **interface** *interface-type* *interface-number* **vrid** *virtual-router-id2*
       
       
       
       A service VRRP6 group is configured to track the mVRRP6 group in flowdown mode.
   14. (On the interface connected to a downstream device) Run [**multicast ipv6 track admin-vrrp6**](cmdqueryname=multicast+ipv6+track+admin-vrrp6) **interface** *interface-type* *interface-number* **vrid** *vrid-value*
       
       
       
       The multicast service interface is bound to the mVRRP6 group.
   15. (On the interface connected to a downstream device) Run [**multicast ipv6 track vrrp6**](cmdqueryname=multicast+ipv6+track+vrrp6) **vrid** *vrid-value*
       
       
       
       The multicast service interface is bound to a VRRP6 group.
       
       
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       A multicast service interface can be bound to only one type of VRRP6 group, either mVRRP6 or common VRRP6 group. You can select one type as required.
   16. (On the interface connected to a downstream device) Run [**pim ipv6 ignore dr-state**](cmdqueryname=pim+ipv6+ignore+dr-state)
       
       
       
       The interface is enabled to ignore the IPv6 PIM DR state.
   17. (On the interface connected to a downstream device) Run [**pim ipv6 ignore assert-state**](cmdqueryname=pim+ipv6+ignore+assert-state)
       
       
       
       The interface is enabled to ignore the IPv6 PIM Assert state.
   18. (On the interface connected to a downstream device) Run [**remote-backup-profile**](cmdqueryname=remote-backup-profile) *profile-name*
       
       
       
       The RBP is bound to the interface.
   19. (On the interface connected to a downstream device) Run [**quit**](cmdqueryname=quit)
       
       
       
       Return to the system view.
   20. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.