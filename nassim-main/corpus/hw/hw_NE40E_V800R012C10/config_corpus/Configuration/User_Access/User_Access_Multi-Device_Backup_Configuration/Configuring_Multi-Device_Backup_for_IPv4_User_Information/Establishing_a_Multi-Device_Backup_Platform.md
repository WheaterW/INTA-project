Establishing a Multi-Device Backup Platform
===========================================

A multi-device backup platform runs Huawei proprietary Redundancy User Information (RUI) protocol to back up user information between devices in a Virtual Router Redundancy Protocol (VRRP) group. This allows fast service switching to be performed if a network node or link fails, enhancing service reliability.

#### Prerequisites

Before establishing a multi-device backup platform, complete the following tasks:

* Configure peer BFD, link BFD, or Ethernet OAM on the user side.
* Configure peer BFD on the network side.
* Configure a local or remote address pool. The same address pool must be configured on devices that back up one another.

#### Context

Establishing a multi-device backup platform includes configuring basic VRRP group functions, an RBP, and an RBS.

* Configure basic VRRP functions to control the master/backup state of the RBP.
* Configure an RBS to back up user information between the master and backup devices. If shared address pool mode is used, configure route control for the shared address pool and a traffic protection tunnel between the master and backup devices.
  
  For details about how to configure route control for the shared address pool, see [Controlling Advertisement of Address Pool UNRs](../ne/dc_ne_cfg_rui_0012.html).
  
  For details about how to configure a traffic protection tunnel between the master and backup devices configured with shared address pool, see [Configuring RUI in Shared Address Pool Mode](../ne/dc_ne_cfg_rui_0009.html).
* Configure an RBP and bind it to VRRP and an RBS. If exclusive address pool mode is used, bind the RBP to an exclusive address pool.

Perform the following steps on both the master and backup devices:


#### Procedure

* Configure basic VRRP group functions.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number* [.*subinterface-number* ]
     
     
     
     The view of the interface on which a VRRP group is configured is displayed.
  3. Run [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* **virtual-ip** *virtual-address*
     
     
     
     A VRRP group is created, and a virtual IP address is assigned to the VRRP group.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The same VRID and virtual IP address must be set on each of the devices that back up one another.
  4. Run [**admin-vrrp vrid**](cmdqueryname=admin-vrrp+vrid) *virtual-router-id* [ **ignore-if-down** ]
     
     
     
     The VRRP group is configured as an mVRRP group.
  5. Run [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* **priority** *priority-value*
     
     
     
     The priority of a device in the VRRP group is configured.
     
     The devices in the VRRP group must be assigned different VRRP priorities. The device with a higher priority serves as the master device.
  6. Run [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* **preempt-mode** **timer** **delay** *delay-time*
     
     
     
     A preemption delay is set for the master device in the VRRP group.
     
     
     
     This ensures that the device preempts the master role after the fault is rectified and services are fully restored.
     
     The preemption delay is related to service types on the live network in the following scenarios:
     
     + In an IPv4 single-stack scenario, the minimum preemption delay is 10 minutes. Increase the value by 1 for every 6K users. If 256K users go online through a device, setting the value to 40 minutes is recommended.
     + In an IPv4 and IPv6 dual-stack scenario, the minimum preemption delay is 10 minutes. Increase the value by 1 for every 6K users. If 128K users go online through a device, setting the value to 40 minutes is recommended.
     + When both IPv4 single-stack and EDSG services are configured, the minimum preemption delay is 15 minutes. Increase the value by 1 for every 4K users. If 256K users go online through a device, setting the value to 60 minutes is recommended.
     + When both IPv4 and IPv6 dual-stack and EDSG services are configured, the minimum preemption delay is 15 minutes. Increase the value by 1 for every 4K users. If 128K dual-stack users go online through a device, setting the value to 60 minutes is recommended.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure an RBS.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**remote-backup-service**](cmdqueryname=remote-backup-service) *service-name*
     
     
     
     An RBS is created, and its view is displayed.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If both a dynamic BFD session and a static BFD session are configured on a BRAS to detect the same link, BFD parameters of one BFD session take effect. Specifically, when an RBS is configured, a dynamic BFD session is created, and BFD parameters are generated. The system compares BFD parameters of the static BFD session with dynamically generated BFD parameters, and BFD parameters with smaller values take effect.
  3. (Optional) Run [**bind ssl-policy**](cmdqueryname=bind+ssl-policy) *ssl-policy-name*
     
     
     
     An SSL policy is bound to a TCP connection.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     You are advised to bind an SSL policy to the RBS to enhance RBS security. If no SSL policy is bound to the RBS, data may be leaked or tampered with.
  4. Run [**peer**](cmdqueryname=peer) *peer-ip-address* [**source**](cmdqueryname=source) *source-ip-address* [**port**](cmdqueryname=port) *port-id*
     
     
     
     TCP connection parameters are set for the RBS.
     
     
     
     *peer-ip-address* sets the IP address of a remote device that backs up the local device. *source-ip-address* sets the IP address of a local device. The remote IP address must be already assigned to the remote device's main interface, sub-interface, or logical interface (for example, loopback interface). The local IP address must be already assigned to the local device's main interface, sub-interface, or logical interface (for example, loopback interface). The local and remote IP addresses must be able to ping each other.
     
     *port-id* indicates the listening port number of a server. The same TCP port number must be set on devices that back up one another.
  5. (Optional) Run [**batch-backup**](cmdqueryname=batch-backup) **service-type**  { **arp** | **all**| **bras** | **l2tp** | **multicast** | **igmp-snooping** | **dhcp-server** | **nd** } **now**
     
     
     
     User services configured in the RBS are immediately backed up.
  6. (Optional) Run [**track bfd-session**](cmdqueryname=track+bfd-session) *bfd-session*
     
     
     
     The RBS tracks the BFD status so that the RBS can rapidly monitor the remote device status.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     This step is recommended. Before running this command, ensure that a peer BFD session is established between the master and backup devices on the network side.
  7. (Optional) Run [**radius-authorization source**](cmdqueryname=radius-authorization+source) **same-as** **nas-logic-ip**
     
     
     
     The device is configured to reply to the RADIUS authorization server with packets in which the source IP address is the same as the NAS IP address.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure an RBP.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. (Optional) Run [**peer-backup batch access enable**](cmdqueryname=peer-backup+batch+access+enable)
     
     
     
     The device is configured to allow users to go online during batch backup.
  3. Run [**remote-backup-profile**](cmdqueryname=remote-backup-profile) *profile-name*
     
     
     
     An RBP is created, and its view is displayed.
  4. Run [**peer-backup**](cmdqueryname=peer-backup) { **hot** | **virtual** }
     
     
     
     Inter-device hot or virtual backup is enabled.
  5. Run [**vrrp-id**](cmdqueryname=vrrp-id) *vrid* **interface** { *interface-name* | *interface-type* *interface-number* } 
     
     
     
     The RBP is bound to the VRRP group.
     
     
     
     + In multi-device backup networking, load balancing improves link usage. To control the MAC address range of the terminals connected with the VRRP sub-interface and load-balance traffic, use either of the following parameters:
       - **odd-mac**: user packets with odd MAC addresses
       - **even-mac**: user packets with even MAC addresses
     + If **odd-mac** or **even-mac** is not configured, the [**vrrp-id**](cmdqueryname=vrrp-id) command only binds a single VRRP group ID to an RBP and associates the RBP with a single VRRP sub-interface. If load balancing is required, run the [**vrrp-id**](cmdqueryname=vrrp-id) command twice, with **odd-mac** and **even-mac** configured, respectively. Two VRRP group IDs must be bound to the same RBP and be associated with different VRRP sub-interfaces. In addition, **odd-mac** and **even-mac** must be configured for different VRRP groups with specific IDs. The two devices that load-balance traffic must have the same configuration, including the binding between the VRRP group ID and even or odd MAC address type.
     + Before modifying the setting of **odd-mac** or **even-mac**, run the [**undo vrrp-id**](cmdqueryname=undo+vrrp-id) *vrid* command to delete the configuration. Then run the [**vrrp-id**](cmdqueryname=vrrp-id) *vrid* command to reconfigure the setting.
  6. Run [**backup-id**](cmdqueryname=backup-id) *backup-id* [**remote-backup-service**](cmdqueryname=remote-backup-service) *service-name*
     
     
     
     The RBP is associated with the RBS, and the user backup ID in the RBP is set.
     
     
     
     *backup-id* sets a user backup ID. The RBP to which a user belongs can be determined based on the *backup-id* and RBS. Note that the same *backup-id* value must be set for devices that back up one another in the same RBP, and different *backup-id* values must be set in other RBPs.
  7. Run [**service-type**](cmdqueryname=service-type) { **arp** | **l2tp**| **bras** | **multicast** | **igmp** | **igmp-snooping** | **no-host-multicast** | **dhcp-server** | **nd** }
     
     
     
     Remote backup is enabled for user services.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  9. (Optional) Run [**acct-session-id nas-logic-sysname**](cmdqueryname=acct-session-id+nas-logic-sysname) *host-name*
     
     
     
     A logic host name used to generate RUI user accounting IDs is configured.
  10. (Optional) Run [**load-balance hash-arithmetic**](cmdqueryname=load-balance+hash-arithmetic) { **arithmetic1** | **arithmetic2** } [ **hash-fields** **mac offset** *mac-offset* ]
      
      
      
      A hash algorithm for load balancing based on odd and even MAC addresses is configured on the interface board.
  11. (Optional) Run [**bras access remark mac**](cmdqueryname=bras+access+remark+mac) *mac-address* { **odd-mac** | **even-mac** }
      
      
      
      The device is enabled to mark a specified MAC address as an odd or even MAC address.
  12. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.