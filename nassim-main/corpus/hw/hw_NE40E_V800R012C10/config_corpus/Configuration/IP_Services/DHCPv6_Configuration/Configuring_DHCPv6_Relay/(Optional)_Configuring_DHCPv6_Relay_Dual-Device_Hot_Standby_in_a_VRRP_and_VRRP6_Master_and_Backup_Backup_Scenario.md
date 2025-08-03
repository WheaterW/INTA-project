(Optional) Configuring DHCPv6 Relay Dual-Device Hot Standby in a VRRP/VRRP6 Master/Backup Backup Scenario
=========================================================================================================

DHCPv6 relay dual-device hot standby can be enabled to back up user entries between devices. If a network node or link fails, a rapid user service switchover is triggered, improving service reliability.

#### Prerequisites

Before configuring DHCPv6 relay dual-device hot standby, complete the following tasks:

* Ensure that the same DHCPv6 relay configurations have been performed on the master and backup devices (the DHCPv6 relay interface types and VLANs configured on the master and backup devices must be the same).
* Ensure that the system time of the master device is the same as that of the backup device (you are advised to configure clock synchronization).

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0208478032__fig631274682315), a VRRP or VRRP6 group is configured on DeviceA and DeviceB to establish a master/backup relationship. DeviceA and DeviceB are the master and backup, respectively. Both DeviceA and DeviceB are DHCPv6 relay agents that forward DHCPv6 client and server messages.

In normal situations, DeviceA forwards user packets, and DeviceB receives user entries synchronized from DeviceA and generates PD routes based on the user entries. If DeviceA or the link between DeviceA and the switch fails, a master/backup VRRP or VRRP6 switchover is performed, and DeviceB becomes the master. In this case, user packets are switched to DeviceB for forwarding. Users are unaware of the fault.

**Figure 1** DHCPv6 relay dual-device hot standby  
![](figure/en-us_image_0202292078.png)

Perform the following steps on the DHCPv6 relay agents that back up each other. The following uses a VRRP6 group as an example to describe how to configure DHCPv6 relay dual-device hot standby. The procedure for configuring a VRRP group is similar to that for configuring a VRRP6 group.


#### Procedure

1. Configure basic VRRP6 group functions.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number* [ .*subinterface-number* ]
      
      
      
      The view of the interface where a VRRP6 group needs to be configured is displayed.
   3. Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
      
      
      
      IPv6 is enabled for the interface.
   4. Run [**ipv6 address**](cmdqueryname=ipv6+address) { *ipv6-address prefix-length* | *ipv6-address-mask* }
      
      
      
      An IPv6 address is configured for the interface.
   5. Run [**vrrp6 vrid**](cmdqueryname=vrrp6+vrid) *virtual-router-id* **virtual-ip** *virtual-address* **link-local**
      
      
      
      A VRRP6 group is created and assigned the first virtual IPv6 address.
      
      
      
      When a VRRP6 group is created on an interface, the first virtual IPv6 address assigned to the VRRP6 group must be a link-local address.
      
      When the first virtual IPv6 address is assigned to a VRRP6 group, the system creates the VRRP6 group. If another virtual IPv6 address is assigned to the VRRP6 group, the system adds the address to the virtual IPv6 address list.
   6. Run [**vrrp6 vrid**](cmdqueryname=vrrp6+vrid) *virtual-router-id* **virtual-ip** *virtual-address*
      
      
      
      A virtual IPv6 address is configured for the VRRP6 group.
      
      
      
      Multiple virtual IPv6 addresses can be assigned to a VRRP6 group. A single virtual IPv6 address serves a separate user group, in which users have the same reliability requirements. This setting helps prevent the default gateway addresses from varying according to changes in VRRP6 device locations.
   7. Run [**vrrp6 vrid**](cmdqueryname=vrrp6+vrid) *virtual-router-id* **preempt-mode** **timer** **delay** *delay-time*
      
      
      
      A preemption delay is set for the device in the VRRP6 group.
      
      
      
      You are advised to set the preemption delay to 0 on a backup device to allow it to preempt the master role immediately after the master device fails or set the preemption delay to a non-0 value on the master device so that it can preempt the master role after a specified delay if a master/backup VRRP6 switchover is performed.
      
      ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
      * The interface on which a VRRP6 group is created and the interface on which DHCPv6 relay is configured must belong to the same main interface. Otherwise, VRRP6 cannot detect link faults on the DHCPv6 relay interface.
      * In DHCPv6 relay dual-device hot standby scenarios, to ensure that the master device can completely back up user session information to the backup device, you are advised to set a preemption delay greater than or equal to 1800s for the master device.
   8. Run [**vrrp6 vrid**](cmdqueryname=vrrp6+vrid) *virtual-router-id* **priority** *priority-value*
      
      
      
      A priority is configured for the device in the VRRP6 group.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      Before running this command to perform a master/backup VRRP6 switchover, ensure that the routing entries on the master and backup devices are the same. If they are different, user packet loss may occur.
   9. (Optional) Run [**vrrp6 vrid**](cmdqueryname=vrrp6+vrid) *virtual-router-id* **timer** **advertise** *advertise-interval*
      
      
      
      An interval for sending VRRP6 Advertisement packets is set.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      The interval at which a device sends VRRP6 Advertisement packets cannot be less than the time that the device takes to perform a master/slave main control board switchover. If the interval is less than the switchover time, protocol flapping may occur during a master/slave main control board switchover. It is recommended that the interval be set to a value greater than 1s.
   10. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
   11. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the interface view.
2. Configure an RBS.
   1. Run [**remote-backup-service**](cmdqueryname=remote-backup-service) *remote-backup-service-name*
      
      
      
      An RBS is created, and the RBS view is displayed.
   2. (Optional) Run [**bind ssl-policy**](cmdqueryname=bind+ssl-policy) *ssl-policy-name*
      
      
      
      An SSL policy is bound to a TCP connection.
   3. Run [**peer**](cmdqueryname=peer) *peer-ip-address* [**source**](cmdqueryname=source) *source-ip-address* [**port**](cmdqueryname=port) *port-id*
      
      
      
      TCP connection parameters are configured for the RBS.
      
      
      
      *source-ip-address* and *peer-ip-address* specify the IP addresses of the master and backup devices, respectively. The IP addresses must have been configured on their own interfaces, sub-interfaces, or logical interfaces (such as loopback interfaces) and be able to ping each other.
      
      *port-id* specifies a TCP port number. The TCP port numbers configured on the master and backup devices must be the same.
   4. (Optional) Run [**batch-backup**](cmdqueryname=batch-backup) **service-type** **dhcpv6-relay** **now**
      
      
      
      The DHCPv6 relay service configured in the RBS is immediately backed up.
   5. (Optional) Run [**batch-backup service-type dhcpv6-relay daily**](cmdqueryname=batch-backup+service-type+dhcpv6-relay+daily) *daytime*
      
      
      
      The DHCPv6 relay service configured in the RBS is backed up at a specified time on a daily basis.
   6. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   7. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the RBS view.
3. Configure an RBP.
   1. Run [**remote-backup-profile**](cmdqueryname=remote-backup-profile) *profile-name*
      
      
      
      An RBP is created, and the RBP view is displayed.
   2. Run [**peer-backup**](cmdqueryname=peer-backup) **hot**
      
      
      
      A backup mode is configured for user information backup.
   3. Run [**vrrp6-id**](cmdqueryname=vrrp6-id) *vrid* **interface** *interface-type* *interface-number*
      
      
      
      The RBP is bound to a VRRP6 group.
      
      
      
      *vrid* specifies the ID of a VRRP6 group. The ID must be the same as the VRRP6 group's ID that was configured using the [**vrrp6 vrid**](cmdqueryname=vrrp6+vrid) *virtual-router-id* [ **virtual-ip** *virtual-address* ] command in the corresponding interface view.
   4. Run [**backup-id**](cmdqueryname=backup-id) *backup-id* [**remote-backup-service**](cmdqueryname=remote-backup-service) *service-name*
      
      
      
      A backup ID is configured for the RBP, and the RBP is associated with a specified RBS.
      
      
      
      *backup-id* specifies a backup ID for an RBP. You can use a backup ID and an RBS to determine an RBP. The backup IDs configured for the same RBP must be the same on the master and backup devices and can no longer be configured for other RBPs.
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   6. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the RBP view.
4. Enable DHCPv6 relay remote backup.
   1. Run [**remote-backup-profile**](cmdqueryname=remote-backup-profile) *profile-name*
      
      
      
      The RBP view is displayed.
   2. Run [**service-type dhcpv6-relay**](cmdqueryname=service-type+dhcpv6-relay)
      
      
      
      DHCPv6 relay remote backup is enabled.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the RBP view.
5. Bind the RBP to an interface.
   1. Run **interface** *interface-type* *interface-number* [ .*subinterface-number* ]
      
      
      
      The view of the DHCPv6 relay interface where DHCPv6 relay dual-device hot standby needs to be configured is displayed.
   2. Run [**remote-backup-profile**](cmdqueryname=remote-backup-profile) *profile-name*
      
      
      
      The RBP is bound to the DHCPv6 relay interface.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      DHCPv6 relay must be configured on the interface to which the RBP is to be bound. Otherwise, DHCPv6 relay dual-device hot standby does not take effect.
   3. (Optional) Run [**dhcpv6 relay pd-route degrade-cost**](cmdqueryname=dhcpv6+relay+pd-route+degrade-cost) *cost-value*
      
      
      
      A cost value is configured for PD routes generated by the backup device in the DHCPv6 relay dual-device hot standby scenario.
   4. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.