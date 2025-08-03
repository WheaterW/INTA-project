Example for Configuring Centralized DS-Lite Inter-Chassis Hot Backup
====================================================================

This section provides an example for configuring inter-chassis HA backup for DS-Lite services in centralized deployment scenarios.

#### Networking Requirements

In centralized deployment scenarios, CGN1 and CGN2 are deployed close to two CRs on the MAN core as the standalone devices. CGN boards are installed on the CGN devices. The two CGN devices use GE interfaces to establish a VRRP channel. To implement inter-chassis HA backup for DS-Lite services, configure VRRP to determine the master/backup CGN status, and associate HA with VRRP. As shown in [Figure 1](#EN-US_TASK_0172362470__fig_dc_ne_cgn-reliability_cfg_003801), home users using private IPv4 addresses access an IPv6 MAN through the CPE that supports dual stack and DS-Lite. A DS-Lite tunnel is established between the CPE and DS-Lite device. The CPE transmits traffic with the private IPv4 address along the DS-Lite tunnel to the DS-Lite device. The DS-Lite device decapsulates traffic, uses NAT to translate the private IPv4 address to a public IPv4 address, and forwards the traffic to the IPv4 Internet.

**Figure 1** Inter-chassis backup networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface1, interface2, and interface3 in this example represent GE0/1/1, GE0/1/2, and GE0/1/3, respectively.


  
![](images/fig_dc_ne_cgn-reliability_cfg_003801.png)
#### Scenario Requirements

A service board is installed on CGN1 and is located in slot 1. A service board is installed on CGN2 and is located in slot 2. Configure the two CGN devices to implement HA backup for DS-Lite services between CPU 0 in CGN1's slot 1 and CPU 0 in CGN2's slot 2.

**Figure 2** Inter-chassis HA backup  
![](images/fig_fig_dc_ne_cgn-reliability_cfg_003802.png)


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable HA hot backup.
2. Create and configure a VRRP group.
3. Create an HA backup group, add members to the group, and configure a VRRP channel.
4. Associate HA with VRRP.
5. Bind the HA backup group to the VRRP group.
6. Create a service-instance group and bind it to the HA backup group.
7. Create a DS-Lite instance, bind the DS-Lite instance to the service-instance group, and configure an address pool and an address translation policy.

#### Data Preparation

To complete the configuration, you need the following data:

| No. | Data |
| --- | --- |
| 1 | ID of an HA backup group |
| 2 | Slot ID and CPU ID of CGN1's active service board (CPU 0 in slot 1) |
| 3 | Slot ID and CPU ID of CGN2's standby service board (CPU 0 in slot 2) |
| 4 | VRRP interfaces on CGN1 and CGN2 |
| 5 | IP addresses of VRRP interfaces on CGN1 and CGN2 |
| 6 | Index of a VRRP group |
| 7 | Virtual IP address of the VRRP group |
| 8 | Priorities of VRRP group members |
| 9 | VRRP preemption delay |
| 10 | Name of a service-instance group |
| 11 | Name and index of a DS-Lite instance |



#### Procedure

1. Enable HA hot backup in the system view of master and backup devices.
   
   
   
   # Enable HA hot backup on CGN1.
   
   ```
   [~CGN1] vsm on-board-mode disable
   ```
   ```
   [*CGN1] commit
   ```
   ```
   [~CGN1] service-ha hot-backup enable
   ```
   ```
   [*CGN1] commit
   ```
   
   
   
   # Enable HA hot backup on CGN2.
   
   ```
   [~CGN2] vsm on-board-mode disable
   ```
   ```
   [*CGN2] commit
   ```
   ```
   [~CGN2] service-ha hot-backup enable
   ```
   ```
   [*CGN2] commit
   ```
2. Create and configure a VRRP group on CGN1 and CGN2.
   
   
   
   # Enter the GE 0/1/3 interface view on CGN1, create VRRP group 10, and set the virtual IP address of the VRRP group to 10.0.0.3. Configure the VRRP group as an mVRRP group and enable the VRRP group to ignore an interface Down event. Set CGN1's priority in the VRRP group to 150 and the VRRP preemption delay to 1500s. Configure the VRRP group to monitor GE 0/1/2 and GE 0/1/1, and set the value by which CGN1's priority decreases to 50 if the status of GE 0/1/2 or GE 0/1/1 changes to Down.
   
   ```
   [~CGN1] interface GigabitEthernet 0/1/3
   [~CGN1-GigabitEthernet0/1/3] ip address 10.0.0.1 255.255.255.0
   [*CGN1-GigabitEthernet0/1/3] vrrp vrid 10 virtual-ip 10.0.0.3
   [*CGN1-GigabitEthernet0/1/3] admin-vrrp vrid 10 ignore-if-down
   [*CGN1-GigabitEthernet0/1/3] vrrp vrid 10 priority 150
   [*CGN1-GigabitEthernet0/1/3] vrrp vrid 10 preempt-mode timer delay 1500
   [*CGN1-GigabitEthernet0/1/3] vrrp recover-delay 20
   [*CGN1-GigabitEthernet0/1/3] vrrp vrid 10 track interface GigabitEthernet 0/1/2 reduced 50
   [*CGN1-GigabitEthernet0/1/3] vrrp vrid 10 track interface GigabitEthernet 0/1/1 reduced 50
   [*CGN1-GigabitEthernet0/1/3] quit
   [*CGN1] commit
   ```
   
   # Enter the GE 0/1/3 interface view on CGN2, create VRRP group 10, and set the virtual IP address of the VRRP group to 10.0.0.3. Configure the VRRP group as an mVRRP group and enable the VRRP group to ignore an interface Down event. Set CGN2's priority in the VRRP group to 120.
   
   ```
   [~CGN2] interface GigabitEthernet 0/1/3
   [~CGN2-GigabitEthernet0/1/3] ip address 10.0.0.2 255.255.255.0
   [*CGN2-GigabitEthernet0/1/3] vrrp vrid 10 virtual-ip 10.0.0.3
   [*CGN2-GigabitEthernet0/1/3] admin-vrrp vrid 10 ignore-if-down
   [*CGN2-GigabitEthernet0/1/3] vrrp vrid 10 priority 120
   [*CGN2-GigabitEthernet0/1/3] quit
   [*CGN2] commit
   ```
3. Create an HA backup group on CGN1 and CGN2, add members to the group, and configure a VRRP channel.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Service-location IDs and the number of service-location groups configured on the master and backup devices must be the same. Otherwise, backup may fail, affecting services.
   
   
   
   # Create HA backup group 21 on CGN1, add CPU 0 in slot 1 to the group, and set the local VRRP outbound interface to GE 0/1/3 and the peer IP address to 10.0.0.2.
   
   ```
   [~CGN1] service-location 21
   [*CGN1-service-location-21] location slot 1 
   [*CGN1-service-location-21] remote-backup interface GigabitEthernet 0/1/3 peer 10.0.0.2
   [*CGN1-service-location-21] quit
   [*CGN1] commit
   ```
   
   # Create HA backup group 21 on CGN2, add CPU 0 in slot 2 to the group, and set the local VRRP outbound interface to GE 0/1/3 and the peer IP address to 10.0.0.1.
   
   ```
   [~CGN2] service-location 21
   [*CGN2-service-location-21] location slot 2 
   [*CGN2-service-location-21] remote-backup interface GigabitEthernet 0/1/3 peer 10.0.0.1
   [*CGN2-service-location-21] quit
   [*CGN2] commit
   ```
4. Associate HA with VRRP on CGN1 and CGN2.
   
   
   
   # Enter the GE 0/1/3 interface view on CGN1, and associate HA backup group 21 with VRRP group 10.
   
   ```
   [~CGN1] interface GigabitEthernet 0/1/3
   [~CGN1-GigabitEthernet0/1/3] vrrp vrid 10 track service-location 21 reduced 50
   [*CGN1-GigabitEthernet0/1/3] quit
   [*CGN1] commit
   ```
   
   # Enter the GE 0/1/3 interface view on CGN2, and associate HA backup group 21 with VRRP group 10.
   
   ```
   [~CGN2] interface GigabitEthernet 0/1/3
   [~CGN2-GigabitEthernet0/1/3] vrrp vrid 10 track service-location 21 reduced 50
   [*CGN2-GigabitEthernet0/1/3] quit
   [*CGN2] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Run the [**display vrrp 10**](cmdqueryname=display+vrrp+10) command on CGN1 and CGN2 to view the master/backup VRRP status, which reflects the master/backup status of the HA backup group. Master in the command output indicates that CGN1 is the master device.
5. Bind the HA backup group to the VRRP group on CGN1 and CGN2.
   
   
   
   # Bind HA backup group 21 to VRRP group 10 on CGN1, and specify the interface for establishing a VRRP connection with CGN2 as GE 0/1/3.
   
   ```
   [~CGN1] service-location 21
   [~CGN1-service-location-21] vrrp vrid 10 interface GigabitEthernet 0/1/3
   [*CGN1-service-location-21] quit
   [*CGN1] commit
   ```
   
   # Bind HA backup group 21 to VRRP group 10 on CGN2, and specify the interface for establishing a VRRP connection with CGN1 as GE 0/1/3.
   
   ```
   [~CGN2] service-location 21
   [~CGN2-service-location-21] vrrp vrid 10 interface GigabitEthernet 0/1/3
   [*CGN2-service-location-21] quit
   [*CGN2] commit
   ```
6. Create a service-instance group on CGN1 and CGN2 and bind it to the HA backup group.
   
   
   
   # Create service-instance group 21 on CGN1 and bind it to HA backup group 21.
   
   ```
   [~CGN1] service-instance-group 21
   [*CGN1-service-instance-group-21] service-location 21
   [*CGN1-service-instance-group-21] quit
   [*CGN1] commit
   ```
   
   # Create service-instance group 21 on CGN2 and bind it to HA backup group 21.
   
   ```
   [~CGN2] service-instance-group 21
   [*CGN2-service-instance-group-21] service-location 21
   [*CGN2-service-instance-group-21] quit
   [*CGN2] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Run the [**display service-location 21**](cmdqueryname=display+service-location+21) command on CGN1 and CGN2 to view HA information. **Vrrp state** in the command output reflects the status of HA backup group 21, which must be consistent with the CGN's VRRP status. **Batch-backup state** in the command output indicates whether batch backup has been finished.
7. Create a DS-Lite instance on CGN1 and CGN2, bind the DS-Lite instance to the service-instance group, and configure an address pool and an address translation policy.
   
   
   
   # Create a DS-Lite instance named **dslite1** on CGN1, bind the DS-Lite instance to service-instance group 21, and set the port range to 4096. Configure a DS-Lite address pool named **group1** in dslite1, and configure an address segment for the DS-Lite address pool. Set the DS-Lite action to **any** so that traffic does not need to match any ACL rule and DS-Lite translation is performed for traffic using addresses from the DS-Lite address pool. Configure local and remote IP addresses for the DS-Lite tunnel, enable DS-Lite ALG for all protocols, and set the DS-Lite address translation mode to **full-cone**.
   
   ```
   [~CGN1] ds-lite instance dslite1 id 21
   [*CGN1-ds-lite-instance-dslite1] port-range 4096
   [*CGN1-ds-lite-instance-dslite1] service-instance-group 21
   [*CGN1-ds-lite-instance-dslite1] ds-lite address-group group1 group-id 1
   [*CGN1-ds-lite-instance-dslite1-ds-lite-address-group-group1] section 0 1.1.1.1 mask 24
   [*CGN1-ds-lite-instance-dslite1-ds-lite-address-group-group1] quit
   [*CGN1-ds-lite-instance-dslite1] ds-lite outbound any address-group group1
   [*CGN1-ds-lite-instance-dslite1] local-ipv6 2001:db8:2::12 prefix-length 128
   [*CGN1-ds-lite-instance-dslite1] remote-ipv6 2001:db8:1:: prefix-length 41
   [*CGN1-ds-lite-instance-dslite1] ds-lite alg all
   [*CGN1-ds-lite-instance-dslite1] ds-lite filter mode full-cone
   [*CGN1-ds-lite-instance-dslite1] quit
   [*CGN1] commit
   ```
   
   # Create a DS-Lite instance named **dslite1** on CGN2, bind the DS-Lite instance to service-instance group 21, and set the port range to 4096. Configure a DS-Lite address pool named **group1** in dslite1, and configure an address segment for the DS-Lite address pool. Set the DS-Lite action to **any** so that traffic does not need to match any ACL rule and DS-Lite translation is performed for traffic using addresses from the DS-Lite address pool. Configure local and remote IP addresses for the DS-Lite tunnel, enable DS-Lite ALG for all protocols, and set the DS-Lite address translation mode to **full-cone**.
   
   ```
   [~CGN2] ds-lite instance dslite1 id 21
   [*CGN2-ds-lite-instance-dslite1] port-range 4096
   [*CGN2-ds-lite-instance-dslite1] service-instance-group 21
   [*CGN2-ds-lite-instance-dslite1] ds-lite address-group group1 group-id 1
   [*CGN2-ds-lite-instance-dslite1-ds-lite-address-group-group1] section 0 1.1.1.1 mask 24
   [*CGN2-ds-lite-instance-dslite1-ds-lite-address-group-group1] quit
   [*CGN2-ds-lite-instance-dslite1] ds-lite outbound any address-group group1
   [*CGN2-ds-lite-instance-dslite1] local-ipv6 2001:db8:2::12 prefix-length 128
   [*CGN2-ds-lite-instance-dslite1] remote-ipv6 2001:db8:1:: prefix-length 41
   [*CGN2-ds-lite-instance-dslite1] ds-lite alg all
   [*CGN2-ds-lite-instance-dslite1] ds-lite filter mode full-cone
   [*CGN2-ds-lite-instance-dslite1] quit
   [*CGN2] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   For details about how to configure basic DS-Lite services, see *DS-Lite Configuration*.

#### Configuration Files

CGN1 configuration file

```
#
sysname CGN1
#
vsm on-board-mode disable
#
interface GigabitEthernet0/1/3
 ip address 10.0.0.1 255.255.255.0
 vrrp vrid 10 virtual-ip 10.0.0.3
 admin-vrrp vrid 10 ignore-if-down 
 vrrp vrid 10 priority 150
 vrrp vrid 10 preempt-mode timer delay 1500
 vrrp recover-delay 20
 vrrp vrid 10 track interface GigabitEthernet0/1/2 reduced 50
 vrrp vrid 10 track interface GigabitEthernet0/1/1 reduced 50
 vrrp vrid 10 track service-location 21 reduced 50 
#
service-ha hot-backup enable
#
service-location 21
 location slot 1  
 remote-backup interface GigabitEthernet0/1/3 peer 10.0.0.2 
 vrrp vrid 10 interface GigabitEthernet0/1/3    
#
service-instance-group 21                    
 service-location 21
#
ds-lite instance dslite1 id 21
 port-range 4096    
 service-instance-group 21
 ds-lite address-group group1 group-id 1  
 section 0 1.1.1.1 mask  24  
 ds-lite outbound any address-group group1
 local-ipv6 2001:db8:2::12 prefix-length 128 
 remote-ipv6 2001:db8:1:: prefix-length 41        
 ds-lite alg all   
 ds-lite filter mode full-cone 
#
return
```

CGN2 configuration file

```
#
sysname CGN2
#
vsm on-board-mode disable
#
interface GigabitEthernet0/1/3
 ip address 10.0.0.2 255.255.255.0
 vrrp vrid 10 virtual-ip 10.0.0.3
 admin-vrrp vrid 10 ignore-if-down
 vrrp vrid 10 priority 120
 vrrp vrid 10 track service-location 21 reduced 50
#
service-ha hot-backup enable
#   
service-location 21
 location slot 2  
 remote-backup interface GigabitEthernet0/1/3 peer 10.0.0.1     
 vrrp vrid 10 interface GigabitEthernet0/1/3 
#                        
service-instance-group 21              
 service-location 21
#
ds-lite instance dslite1 id 21
 port-range 4096    
 service-instance-group 21
 ds-lite address-group group1 group-id 1  
 section 0 1.1.1.1 mask  24  
 ds-lite outbound any address-group group1
 local-ipv6 2001:db8:2::12 prefix-length 128 
 remote-ipv6 2001:db8:1:: prefix-length 41     
 ds-lite alg all   
 ds-lite filter mode full-cone  
#
return
```