Establishing a Dual-Device Backup Platform
==========================================

This section describes how to establish a dual-device backup platform to back up user information between devices. This allows fast service switching if a network node or link fails, enhancing service reliability.

#### Prerequisites

Before binding an SSL policy to a TCP connection, an SSL policy has been configured and a digital certificate has been loaded.


#### Context

Dual-device backup provides a unified platform for backing up user information between devices in a VRRP group through a remote backup service (RBS) channel. This facilitates flexible control and management of user services and improves service continuity. Establishing a dual-device backup platform includes configuring basic Virtual Router Redundancy Protocol (VRRP) group functions, a remote backup service (RBS), and a remote backup profile (RBP).

Perform the following steps on both the master and backup devices:


#### Procedure

* Configure basic VRRP group functions.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) { *interface-name* | *interface-type* *interface-number* }
     
     
     
     The interface view for a VRRP group is displayed.
  3. Run [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* **virtual-ip** *virtual-address*
     
     
     
     A VRRP group is created, and a virtual IP address is assigned to the VRRP group.
  4. Run [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* **preempt-mode** **timer** **delay** *delay-time*
     
     
     
     A preemption delay is set for devices in the VRRP group.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     In ARP dual-device hot backup scenarios, to ensure that the master device can completely back up ARP entries to the backup device, setting a preemption delay greater than or equal to 600s for the devices in the VRRP group is recommended.
  5. Run [**admin-vrrp vrid**](cmdqueryname=admin-vrrp+vrid) *virtual-router-id* [ **ignore-if-down** ]
     
     
     
     The VRRP group is configured as an mVRRP group.
  6. Run [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* **priority** *priority-value*
     
     
     
     A priority is configured for a device in the VRRP group.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure an RBP.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**remote-backup-profile**](cmdqueryname=remote-backup-profile) *profile-name*
     
     
     
     An RBP is created, and the RBP view is displayed.
  3. Run [**peer-backup**](cmdqueryname=peer-backup) **hot**
     
     
     
     A backup mode is configured for user information backup.
  4. Run [**vrrp-id**](cmdqueryname=vrrp-id) *vrid* **interface** { *interface-name* | *interface-type* *interface-number* } { **odd-mac** | **even-mac** }
     
     
     
     A binding relationship between the RBP and the VRRP group is configured.
     
     
     
     *vrid* specifies the ID of a VRRP group. The ID must be the same as the VRRP group's ID that was configured using the [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* [ **virtual-ip** *virtual-address* ] command in the corresponding interface view.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     In a dual-device backup scenario where load balancing is implemented based on odd and even MAC addresses, if the **mac-address** parameter is not set under the **static-user** command but the **initiative detect static user** parameter is configured, only static users with odd MAC addresses can go online.
     
     When load balancing based on odd and even MAC addresses is deployed in a dual-device backup scenario, two VRRP groups need to be configured in the same RBP. One of the VRRP groups is bound to an odd MAC address, and the other is bound to an even MAC address. The same VRRP group on two BNGs must be bound to the same odd or even MAC address. Otherwise, the BNGs with the same odd or even MAC address will be master or backup in the two VRRP groups at the same time, and users cannot go online.
  5. Run [**backup-id**](cmdqueryname=backup-id) *backup-id* [**remote-backup-service**](cmdqueryname=remote-backup-service) *service-name*
     
     
     
     A user backup ID is configured for the RBP, and the RBP is associated with a specified RBS.
     
     The *backup-id* parameter specifies a user backup ID for an RBP. You can use a backup ID and an RBS to determine an RBP. The backup IDs configured for the same RBP must be the same on the master and backup devices and can no longer be configured for other RBPs.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure an RBS.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**remote-backup-service**](cmdqueryname=remote-backup-service) *remote-backup-service-name*
     
     
     
     An RBS is created, and the RBS view is displayed.
  3. (Optional) Run [**bind ssl-policy**](cmdqueryname=bind+ssl-policy) *ssl-policy-name*
     
     
     
     An SSL policy is bound to a TCP connection.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     You are advised to bind an SSL policy to the RBS to enhance RBS security. If no SSL policy is bound to the RBS, data may be leaked or tampered with.
  4. Run [**peer**](cmdqueryname=peer) *peer-ip-address* [**source**](cmdqueryname=source) *source-ip-address* [**port**](cmdqueryname=port) *port-id*
     
     
     
     TCP connection parameters are set for the RBS.
     
     The *source-ip-address* and *peer-ip-address* parameters specify the IP addresses of the local and remote devices, respectively. The IP addresses must have been configured on their own interfaces, sub-interfaces, or logical interfaces (such as loopback interfaces) and can ping each other.
     
     The *port-id* parameter specifies a TCP port number. The TCP port numbers configured on the local and remote devices must be the same.
  5. (Optional) Run [**batch-backup service-type**](cmdqueryname=batch-backup+service-type) { **arp** | **all** | **ipsec** | **bras** | **l2tp** | **dhcp-server** | **nd** | **dhcpv6-relay** } **now**
     
     
     
     The device is enabled to immediately back up user services configured in the RBS.
     
     
     
     The **multicast**, **l2tp,** and **bras** parameters are supported only by the admin VS.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a delay for disabling the forwarding function when the master device becomes the backup device.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  The configuration is supported only on the NE40E-M2F, NE40E-M2H, NE40E-M2K, and NE40E-M2K-B.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**peer-backup download-vrrp-table delay-time**](cmdqueryname=peer-backup+download-vrrp-table+delay-time) *delay-time-value*
     
     
     
     The delay for disabling the forwarding function when the master device becomes the backup device is configured.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.