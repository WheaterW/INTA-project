Example for Configuring VPN over Centralized NAT Inter-chassis Hot Backup (One to Many)
=======================================================================================

This section provides an example for configuring VPN over centralized NAT inter-chassis HA backup in centralized deployment mode.

#### Networking Requirements

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The [**remote-backup-service**](cmdqueryname=remote-backup-service) command is applicable to VPN over centralized and distributed NAT inter-chassis backup scenarios. This method is recommended.

On the network shown in [Figure 1](#EN-US_TASK_0172362490__fig_dc_ne_cfg_nat_005701), one-to-many address translation is performed on user traffic between one network-side VPN and multiple user-side VPNs. A VRRP channel is established between CGN1 and CGN2 over GE interfaces. CGN1 and CGN2 work in master/backup mode and their master/backup status is determined by VRRP. HA is associated with VRRP. CGN1 is equipped with a service board in slot 1, and CGN2 is equipped with a service board in slot 1. VPN over inter-chassis hot backup is implemented between CPU 0 of the service board in slot 1 on CGN1 and CPU 0 of the service board in slot 1 on CGN2.

**Figure 1** VPN over centralized NAT inter-chassis hot backup![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface1, interface2, and interface3 in this example represent GE0/2/0, GE0/2/1, and GE0/3/0, respectively.


  
![](images/fig_dc_ne_cgn-reliability_cfg_0004.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable the license function on CGN devices and configure NAT session table resources.
2. Configure a user-side VPN instance and a network-side VPN instance on each CGN device and bind the VPN instances.
3. Enable HA hot backup.
4. Create a service-location group, configure members for HA dual-device inter-chassis backup, and configure a VRRP channel.
5. Bind an RBS group to a service-instance group to implement NAT on the user-side VPN.
6. Create a VRRP group and associate HA with VRRP.
7. Bind the service-location group to the VRRP group.
8. Create a service-instance group and bind the service-location group to the service-instance group.
9. Create a NAT instance, enable the VPN NAT function, bind the NAT instance to the service-instance group and allowed VPN instance, and configure an address pool and a traffic conversion policy.
10. Configure a NAT traffic diversion policy.

#### Data Preparation

| No. | Data |
| --- | --- |
| 1 | User-side VPN and network-side VPN on CGN devices |
| 2 | ACL name and rule |
| 1 | Index of the service-location group |
| 2 | CPU ID and slot ID of the active CPU on CGN1's service board (CPU 0 in slot 1 in this example) |
| 3 | CPU ID and slot ID of the standby CPU on CGN2's service board (CPU 0 in slot 1 in this example) |
| 4 | Name of an RBS |
| 5 | VRRP interfaces on CGN1 and CGN2 |
| 6 | IP addresses of VRRP interfaces on CGN1 and CGN2 |
| 7 | ID of a VRRP group |
| 8 | Virtual IP address of the VRRP group |
| 9 | Priorities of VRRP group members |
| 10 | VRRP preemption delay |
| 11 | Name of a service-instance group |
| 12 | NAT instance name and index |
| 13 | NAT address pool name and index |
| 14 | Name of a private VPN instance |
| 15 | Name of a public VPN instance |
| 16 | RDs of the VPN instances |
| 17 | VPN-Target of the VPN instances |



#### Procedure

1. Enable the license function on CGN devices and configure NAT session table resources.
   
   
   
   # Configure CGN1.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname CGN1
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~CGN1] vsm on-board-mode disable
   ```
   ```
   [*CGN1] commit
   ```
   ```
   [~CGN1] license
   ```
   ```
   [~CGN1-license] active nat session-table size 6 slot 1
   ```
   ```
   [*CGN1-license] active nat bandwidth-enhance 40 slot 1
   ```
   ```
   [*CGN1-license] commit
   ```
   ```
   [~CGN1-license] quit
   ```
   
   # Configure CGN2.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname CGN2
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~CGN2] vsm on-board-mode disable
   ```
   ```
   [*CGN2] commit
   ```
   ```
   [~CGN2] license
   ```
   ```
   [~CGN2-license] active nat session-table size 6 slot 1 
   ```
   ```
   [*CGN2-license] active nat bandwidth-enhance 40 slot 1
   ```
   ```
   [*CGN2-license] commit
   ```
   ```
   [~CGN2-license] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The method for configuring bandwidth resources varies according to the board type. As such, determine whether to run the **active nat bandwidth-enhance** command and the corresponding parameters based on the board type.
2. Configure a user-side VPN instance and a network-side VPN instance on each CGN device and bind the VPN instances.
   
   
   
   # Configure CGN1.
   
   1. Configure user-side VPN instances named **inside-vpn1** and **inside-vpn2** on CGN1.
      
      ```
      [~CGN1] ip vpn-instance inside-vpn1
      ```
      ```
      [*CGN1-vpn-instance-inside-vpn1] ipv4-family
      ```
      ```
      [*CGN1-vpn-instance-inside-vpn1-af-ipv4] route-distinguisher 200:1
      ```
      ```
      [*CGN1-vpn-instance-inside-vpn1-af-ipv4] vpn-target 101:101 export-extcommunity
      ```
      ```
      [*CGN1-vpn-instance-inside-vpn1-af-ipv4] vpn-target 101:101 import-extcommunity
      ```
      ```
      [*CGN1-vpn-instance-inside-vpn1-af-ipv4] commit
      ```
      ```
      [~CGN1-vpn-instance-inside-vpn1-af-ipv4] quit
      ```
      ```
      [~CGN1-vpn-instance-inside-vpn1] quit
      ```
      ```
      [~CGN1] ip vpn-instance inside-vpn2
      ```
      ```
      [*CGN1-vpn-instance-inside-vpn2] ipv4-family
      ```
      ```
      [*CGN1-vpn-instance-inside-vpn2-af-ipv4] route-distinguisher 200:2
      ```
      ```
      [*CGN1-vpn-instance-inside-vpn2-af-ipv4] vpn-target 102:102 export-extcommunity
      ```
      ```
      [*CGN1-vpn-instance-inside-vpn2-af-ipv4] vpn-target 102:102 import-extcommunity
      ```
      ```
      [*CGN1-vpn-instance-inside-vpn2-af-ipv4] commit
      ```
      ```
      [~CGN1-vpn-instance-inside-vpn2-af-ipv4] quit
      ```
      ```
      [~CGN1-vpn-instance-inside-vpn2] quit
      ```
   2. Configure a network-side VPN instance named **outside-vpn** on CGN1.
      
      ```
      [~CGN1] ip vpn-instance outside-vpn
      ```
      ```
      [*CGN1-vpn-instance-outside-vpn] ipv4-family
      ```
      ```
      [*CGN1-vpn-instance-outside-vpn-af-ipv4] route-distinguisher 200:3
      ```
      ```
      [*CGN1-vpn-instance-outside-vpn-af-ipv4] vpn-target 103:103 export-extcommunity
      ```
      ```
      [*CGN1-vpn-instance-outside-vpn-af-ipv4] vpn-target 103:103 import-extcommunity
      ```
      ```
      [*CGN1-vpn-instance-outside-vpn-af-ipv4] commit
      ```
      ```
      [~CGN1-vpn-instance-outside-vpn-af-ipv4] quit
      ```
      ```
      [~CGN1-vpn-instance-outside-vpn] quit
      ```
   3. On CGN1, bind the private VPN instances on the user side.
      
      ```
      [~CGN1] interface GigabitEthernet 0/2/1.1
      ```
      ```
      [*CGN1-GigabitEthernet0/2/1.1] vlan-type dot1q 200
      ```
      ```
      [*CGN1-GigabitEthernet0/2/1.1] ip binding vpn-instance inside-vpn1
      ```
      ```
      [*CGN1-GigabitEthernet0/2/1.1] ip address 172.16.10.1 24
      ```
      ```
      [*CGN1-GigabitEthernet0/2/1.1] commit
      ```
      ```
      [~CGN1-GigabitEthernet0/2/1.1] quit
      ```
      ```
      [~CGN1] interface GigabitEthernet 0/2/1.2
      ```
      ```
      [*CGN1-GigabitEthernet0/2/1.2] vlan-type dot1q 202
      ```
      ```
      [*CGN1-GigabitEthernet0/2/1.2] ip binding vpn-instance inside-vpn2
      ```
      ```
      [*CGN1-GigabitEthernet0/2/1.2] ip address 172.16.11.1 24
      ```
      ```
      [*CGN1-GigabitEthernet0/2/1.2] commit
      ```
      ```
      [~CGN1-GigabitEthernet0/2/1.2] quit
      ```
   4. On CGN1, bind the public VPN instances on the network side.
      
      ```
      [~CGN1] interface GigabitEthernet 0/3/0
      ```
      ```
      [~CGN1-GigabitEthernet0/3/0] ip binding vpn-instance outside-vpn
      ```
      ```
      [*CGN1-GigabitEthernet0/3/0] ip address 172.16.9.1 24
      ```
      ```
      [*CGN1-GigabitEthernet0/3/0] commit
      ```
      ```
      [~CGN1-GigabitEthernet0/3/0] quit
      ```
   
   # Configure CGN2.
   
   1. Configure user-side VPN instances named **inside-vpn1** and **inside-vpn2** on CGN2.
      
      ```
      [~CGN2] ip vpn-instance inside-vpn1
      ```
      ```
      [*CGN2-vpn-instance-inside-vpn1] ipv4-family
      ```
      ```
      [*CGN2-vpn-instance-inside-vpn1-af-ipv4] route-distinguisher 200:1
      ```
      ```
      [*CGN2-vpn-instance-inside-vpn1-af-ipv4] vpn-target 101:101 export-extcommunity
      ```
      ```
      [*CGN2-vpn-instance-inside-vpn1-af-ipv4] vpn-target 101:101 import-extcommunity
      ```
      ```
      [*CGN2-vpn-instance-inside-vpn1-af-ipv4] commit
      ```
      ```
      [~CGN2-vpn-instance-inside-vpn1-af-ipv4] quit
      ```
      ```
      [~CGN2-vpn-instance-inside-vpn1] quit
      ```
      ```
      [~CGN2] ip vpn-instance inside-vpn2
      ```
      ```
      [*CGN2-vpn-instance-inside-vpn2] ipv4-family
      ```
      ```
      [*CGN2-vpn-instance-inside-vpn2-af-ipv4] route-distinguisher 200:2
      ```
      ```
      [*CGN2-vpn-instance-inside-vpn2-af-ipv4] vpn-target 102:102 export-extcommunity
      ```
      ```
      [*CGN2-vpn-instance-inside-vpn2-af-ipv4] vpn-target 102:102 import-extcommunity
      ```
      ```
      [*CGN2-vpn-instance-inside-vpn2-af-ipv4] commit
      ```
      ```
      [~CGN2-vpn-instance-inside-vpn2-af-ipv4] quit
      ```
      ```
      [~CGN2-vpn-instance-inside-vpn2] quit
      ```
   2. Configure a network-side VPN instance named **outside-vpn** on CGN2.
      
      ```
      [~CGN2] ip vpn-instance outside-vpn
      ```
      ```
      [*CGN2-vpn-instance-outside-vpn] ipv4-family
      ```
      ```
      [*CGN2-vpn-instance-outside-vpn-af-ipv4] route-distinguisher 200:3
      ```
      ```
      [*CGN2-vpn-instance-outside-vpn-af-ipv4] vpn-target 103:103 export-extcommunity
      ```
      ```
      [*CGN2-vpn-instance-outside-vpn-af-ipv4] vpn-target 103:103 import-extcommunity
      ```
      ```
      [*CGN2-vpn-instance-outside-vpn-af-ipv4] commit
      ```
      ```
      [~CGN2-vpn-instance-outside-vpn-af-ipv4] quit
      ```
      ```
      [~CGN2-vpn-instance-outside-vpn] quit
      ```
   3. On CGN2, bind the private VPN instances on the user side.
      
      ```
      [~CGN2] interface GigabitEthernet 0/2/1.1
      ```
      ```
      [*CGN2-GigabitEthernet0/2/1.1] vlan-type dot1q 200
      ```
      ```
      [*CGN2-GigabitEthernet0/2/1.1] ip binding vpn-instance inside-vpn1
      ```
      ```
      [*CGN2-GigabitEthernet0/2/1.1] ip address 172.16.6.1 24
      ```
      ```
      [*CGN2-GigabitEthernet0/2/1.1] commit
      ```
      ```
      [~CGN2-GigabitEthernet0/2/1.1] quit
      ```
      ```
      [~CGN2] interface GigabitEthernet 0/2/1.2
      ```
      ```
      [*CGN2-GigabitEthernet0/2/1.2] vlan-type dot1q 202
      ```
      ```
      [*CGN2-GigabitEthernet0/2/1.2] ip binding vpn-instance inside-vpn2
      ```
      ```
      [*CGN2-GigabitEthernet0/2/1.2] ip address 172.16.7.1 24
      ```
      ```
      [*CGN2-GigabitEthernet0/2/1.2] commit
      ```
      ```
      [~CGN2-GigabitEthernet0/2/1.2] quit
      ```
   4. On CGN2, bind the public VPN instances on the network side.
      
      ```
      [~CGN2] interface GigabitEthernet 0/3/0
      ```
      ```
      [~CGN2-GigabitEthernet0/3/0] ip binding vpn-instance outside-vpn
      ```
      ```
      [*CGN2-GigabitEthernet0/3/0] ip address 172.16.8.1 24
      ```
      ```
      [*CGN2-GigabitEthernet0/3/0] commit
      ```
      ```
      [~CGN2-GigabitEthernet0/3/0] quit
      ```
3. Enable HA hot backup.
   
   
   
   # Configure CGN1.
   
   ```
   [~CGN1] service-ha hot-backup enable
   ```
   ```
   [*CGN1] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The configuration on CGN2 is similar to that on CGN1.
4. Create a service-location group, configure members for HA dual-device inter-chassis backup, and configure a VRRP channel.
   
   
   
   # Create service-location group 1 on CGN1, add CPU 0 of the service board in slot 1 as an HA dual-device inter-chassis backup member, and set the local VRRP outbound interface to GE 0/2/0 and the peer IP address to 172.16.5.2.
   
   ```
   [~CGN1] service-location 1
   ```
   ```
   [*CGN1-service-location-1] location slot 1 
   ```
   ```
   [*CGN1-service-location-1] remote-backup interface GigabitEthernet 0/2/0 peer 172.16.5.2
   ```
   ```
   [*CGN1-service-location-1] commit
   ```
   ```
   [~CGN1-service-location-1] quit
   ```
   
   
   
   # Create service-location group 1 on CGN2, add CPU 0 of the service board in slot 1 as an HA dual-device inter-chassis backup member, and set the local VRRP outbound interface to GE 0/2/0 and the peer IP address to 172.16.5.1.
   
   ```
   [~CGN2] service-location 1
   ```
   ```
   [*CGN2-service-location-1] location slot 1 
   ```
   ```
   [*CGN2-service-location-1] remote-backup interface GigabitEthernet 0/2/0 peer 172.16.5.1
   ```
   ```
   [*CGN2-service-location-1] commit
   ```
   ```
   [~CGN2-service-location-1] quit
   ```
5. Bind an RBS group to a service-instance group to implement NAT on the user-side VPN.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The [**remote-backup-service**](cmdqueryname=remote-backup-service) command is applicable to VPN over centralized and distributed NAT inter-chassis backup scenarios. This method is recommended.
   
   # Create an RBS named **vpn\_nat** on CGN1, configure the peer IP address as 172.16.5.2, and bind the HA service-instance group named **group1** to the RBS named **vpn\_nat**.
   
   ```
   [~CGN1] remote-backup-service vpn_nat
   ```
   ```
   [*CGN1-rm-backup-srv-vpn_nat] peer 172.16.5.2 source 172.16.5.1 port 1024
   ```
   ```
   [*CGN1-rm-backup-srv-vpn_nat] commit
   ```
   ```
   [~CGN1-rm-backup-srv-vpn_nat] quit
   ```
   ```
   [~CGN1] service-instance-group group1
   ```
   ```
   [*CGN1-instance-group-group1] remote-backup-service vpn_nat
   ```
   ```
   [*CGN1-instance-group-group1] commit
   ```
   ```
   [~CGN1-instance-group-group1] quit
   ```
   
   # Create an RBS named **vpn\_nat** on CGN2, configure the peer IP address as 172.16.5.1, and bind the HA service-instance group named **group1** to the RBS named **vpn\_nat**.
   
   ```
   [~CGN2] remote-backup-service vpn_nat
   ```
   ```
   [*CGN2-rm-backup-srv-vpn_nat] peer 172.16.5.1 source 172.16.5.2 port 1024
   ```
   ```
   [*CGN2-rm-backup-srv-vpn_nat] commit
   ```
   ```
   [~CGN2-rm-backup-srv-vpn_nat] quit
   ```
   ```
   [~CGN2] service-instance-group group1
   ```
   ```
   [*CGN2-instance-group-group1] remote-backup-service vpn_nat
   ```
   ```
   [*CGN2-instance-group-group1] commit
   ```
   ```
   [~CGN2-instance-group-group1] quit
   ```
6. Create a VRRP group and configure HA and VRRP association. Set the VRRP preemption delay to 1500s to ensure that the NAT information is backed up completely. Set the VRRP recovery delay to 15s.
   
   
   
   # Configure CGN1.
   
   ```
   [~CGN1] interface GigabitEthernet 0/2/0
   ```
   ```
   [~CGN1-GigabitEthernet0/2/0] ip address 172.16.5.1 24
   ```
   ```
   [*CGN1-GigabitEthernet0/2/0] vrrp vrid 1 virtual-ip 172.16.5.100
   ```
   ```
   [*CGN1-GigabitEthernet0/2/0] admin-vrrp vrid 1 ignore-if-down
   ```
   ```
   [*CGN1-GigabitEthernet0/2/0] vrrp vrid 1 priority 200
   ```
   ```
   [*CGN1-GigabitEthernet0/2/0] vrrp vrid 1 preempt-mode timer delay 1500
   ```
   ```
   [*CGN1-GigabitEthernet0/2/0] vrrp vrid 1 track service-location 1 reduced 60
   ```
   ```
   [*CGN1-GigabitEthernet0/2/0] vrrp vrid 1 track interface GigabitEthernet 0/2/1.1 reduced 60
   ```
   ```
   [*CGN1-GigabitEthernet0/2/0] vrrp vrid 1 track interface GigabitEthernet 0/2/1.2 reduced 60
   ```
   ```
   [*CGN1-GigabitEthernet0/2/0] vrrp vrid 1 track interface GigabitEthernet 0/3/0 reduced 60
   ```
   ```
   [*CGN1-GigabitEthernet0/2/0] vrrp recover-delay 15
   ```
   ```
   [*CGN1-GigabitEthernet0/2/0] commit
   ```
   ```
   [~CGN1-GigabitEthernet0/2/0] quit
   ```
   
   # Configure CGN2.
   
   ```
   [~CGN2] interface GigabitEthernet 0/2/0
   ```
   ```
   [~CGN2-GigabitEthernet0/2/0] ip address 172.16.5.2 24
   ```
   ```
   [*CGN2-GigabitEthernet0/2/0] vrrp vrid 1 virtual-ip 172.16.5.100
   ```
   ```
   [*CGN2-GigabitEthernet0/2/0] admin-vrrp vrid 1 ignore-if-down
   ```
   ```
   [*CGN2-GigabitEthernet0/2/0] vrrp vrid 1 priority 150
   ```
   ```
   [*CGN2-GigabitEthernet0/2/0] vrrp vrid 1 track service-location 1 reduced 60
   ```
   ```
   [*CGN2-GigabitEthernet0/2/0] vrrp recover-delay 15
   ```
   ```
   [*CGN2-GigabitEthernet0/2/0] commit
   ```
   ```
   [~CGN2-GigabitEthernet0/2/0] quit
   ```
   
   After the configuration, the master/backup status of CGN1 and CGN2 can be determined by VRRP. You can run the [**display vrrp 1**](cmdqueryname=display+vrrp+1) command to check the master/backup VRRP status, which reflects the master/backup status of the service-location groups on CGN1 and CGN2. **State** in the command output indicates the CGN device's status.
   
   The following example uses the command output on CGN1:
   
   ```
   [~CGN1] display vrrp 1
   ```
   ```
   GigabitEthernet 0/2/0 | Virtual Router 1                                                                                      
       State                  : Master     
       Virtual IP             : 172.16.5.100   
       Master IP              : 172.16.5.1
       Local IP               : 172.16.5.1
       PriorityRun            : 200      
       PriorityConfig         : 200    
       MasterPriority         : 200     
       Preempt                : YES   Delay Time   : 420 s 
       Hold Multiplier        : 3                                                                             
       TimerRun               : 1 s     
       TimerConfig            : 1 s    
       Auth Type              : NONE    
       Virtual MAC            : 00e0-fc12-3456  
       Check TTL              : YES      
       Config Type            : admin-vrrp   
       Backup-forward         : disabled     
       Fast-resume            : disabled     
       Track IF               : GigabitEthernet0/2/1.1    Priority Reduced :60
       IF State               : UP  
       Track IF               : GigabitEthernet0/2/1.2    Priority Reduced :60
       IF State               : UP
       Track IF               : GigabitEthernet0/3/0      Priority Reduced :60
       IF State               : UP
       Track Service-location : 1   Priority Reduced : 60                                                  
       Service-location State : UP 
       Create Time            : 2016-10-18 11:14:48 UTC+10:59    
       Last Change Time       : 2016-10-18 14:02:46 UTC+10:59
   ```
7. Bind the service-location group to the VRRP group.
   
   
   
   # Configure CGN1.
   
   ```
   [~CGN1] service-location 1
   ```
   ```
   [~CGN1-service-location-1] vrrp vrid 1 interface GigabitEthernet 0/2/0
   ```
   ```
   [*CGN1-service-location-1] commit
   ```
   ```
   [~CGN1-service-location-1] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The configuration on CGN2 is similar to that on CGN1.
8. Create a service-instance group and bind the service-location group to the service-instance group.
   
   
   
   # Configure CGN1.
   
   ```
   [~CGN1] service-instance-group group1
   ```
   ```
   [*CGN1-service-instance-group-group1] service-location 1
   ```
   ```
   [*CGN1-service-instance-group-group1] commit
   ```
   ```
   [~CGN1-service-instance-group-group1] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The configuration on CGN2 is similar to that on CGN1.
   
   Run the [**display service-location 1**](cmdqueryname=display+service-location+1) command on the CGN devices to check the HA information. **VRRP State** in the command output indicates the status of the HA backup group, which must be consistent with the CGN devices' VRRP status. **Batch-backup state** in the command output indicates whether batch backup has completed.
   
   The following example uses the command output on CGN1:
   
   ```
   [~CGN1] display service-location 1
   ```
   ```
    service-location 1                                                                                                                
    Backup scene type: inter-box                                                                       
    Location slot ID: 1                                                                  
    Remote-backup interface: GigabitEthernet0/2/0                                                        
    Peer: 172.16.5.2                                                                                 
    Vrrp ID: 1                                            
    Vrrp bind interface: GigabitEthernet0/2/0                                                              
    Vrrp state: master                                                                           
    Bound service-instance-group number: 1                                                                  
    Batch-backup state: finished
   ```
9. Create a NAT instance, enable the VPN NAT function, bind the NAT instance to the service-instance group and allowed VPN instance, and configure an address pool and a traffic conversion policy.
   
   
   
   # Configure CGN1.
   
   ```
   [~CGN1] nat instance nat id 1
   ```
   ```
   [*CGN1-nat-instance-nat] port-range 64
   ```
   ```
   [*CGN1-nat-instance-nat] service-instance-group group1
   ```
   ```
   [*CGN1-nat-instance-nat] nat address-group group1 group-id 1 vpn-instance outside-vpn
   ```
   ```
   [*CGN1-nat-instance-nat-nat-address-group-group1] section 0 11.11.11.0 mask 24
   ```
   ```
   [*CGN1-nat-instance-nat-nat-address-group-group1] commit
   ```
   ```
   [~CGN1-nat-instance-nat-nat-address-group-group1] quit
   ```
   ```
   [~CGN1-nat-instance-nat] nat outbound any address-group group1
   ```
   ```
   [*CGN1-nat-instance-nat] commit
   ```
   ```
   [~CGN1-nat-instance-nat] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) The configuration on CGN2 is similar to that on CGN1. Pay attention to the following points:
   * Ensure that the VPN instance before NAT is the same as that bound to the user-side inbound interface (GE0/2/1 on PE1).
   * Ensure that the VPN instance after NAT is the same as that bound to the network-side outbound interface (GE0/3/0 on PE2).
10. Configure a NAT traffic diversion policy.
    
    
    
    # Configure an ingress NAT traffic diversion policy on CGN1.
    
    1. Configure an ACL numbered 3001, an ACL rule numbered 5, and an ACL-based traffic classification rule to allow only hosts with a network segment address of 10.1.1.0/24 to access the Internet.
       
       ```
       [~CGN1] acl number 3001
       ```
       ```
       [*CGN1-acl-adv-3001] rule 5 permit ip source 10.1.1.0 0.0.0.255
       ```
       ```
       [*CGN1-acl-adv-3001] commit
       ```
       ```
       [~CGN1-acl-adv-3001] quit
       ```
    2. Configure a traffic classifier.
       
       ```
       [~CGN1] traffic classifier vpn_nat1 operator or
       ```
       ```
       [*CGN1-classifier-vpn_nat1] if-match acl 3001
       ```
       ```
       [*CGN1-classifier-vpn_nat1] commit
       ```
       ```
       [~CGN1-classifier-vpn_nat1] quit
       ```
    3. Configure a traffic behavior **vpn\_nat1** and bind it to the NAT instance named **nat**.
       
       ```
       [~CGN1] traffic behavior vpn_nat1 
       ```
       ```
       [*CGN1-behavior-vpn_nat1] nat bind instance nat
       ```
       ```
       [*CGN1-behavior-vpn_nat1] commit
       ```
       ```
       [~CGN1-behavior-vpn_nat1] quit
       ```
    4. Define a NAT traffic policy named **vpn\_nat1** to associate all ACL rules with the traffic behaviors.
       
       ```
       [~CGN1] traffic policy vpn_nat1
       ```
       ```
       [*CGN1-trafficpolicy-vpn_nat1] classifier vpn_nat1 behavior vpn_nat1
       ```
       ```
       [*CGN1-trafficpolicy-vpn_nat1] commit
       ```
       ```
       [~CGN1-trafficpolicy-vpn_nat1] quit
       ```
    5. Apply the NAT traffic policy on the user side.
       
       ```
       [~CGN1] interface GigabitEthernet 0/2/1.1
       ```
       ```
       [~CGN1-GigabitEthernet0/2/1.1] traffic-policy vpn_nat1 inbound
       ```
       ```
       [*CGN1-GigabitEthernet0/2/1.1] commit
       ```
       ```
       [~CGN1-GigabitEthernet0/2/1.1] quit
       ```
       ```
       [~CGN1] interface GigabitEthernet 0/2/1.2
       ```
       ```
       [~CGN1-GigabitEthernet0/2/1.2] traffic-policy vpn_nat1 inbound
       ```
       ```
       [*CGN1-GigabitEthernet0/2/1.2] commit
       ```
       ```
       [~CGN1-GigabitEthernet0/2/1.2] quit
       ```![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    The configuration on CGN2 is similar to that on CGN1.

#### Configuration Files

* CGN1 configuration file
  ```
  #
  sysname CGN1
  #
  vsm on-board-mode disable
  #
  license
   active nat session-table size 6 slot 1 
   active nat bandwidth-enhance 40 slot 1
  #
  ip vpn-instance inside-vpn1
   ipv4-family
    route-distinguisher 200:1   
    apply-label per-instance 
    vpn-target 101:101 export-extcommunity                                                                  
    vpn-target 101:101 import-extcommunity                                                             
  #
  ip vpn-instance inside-vpn2
   ipv4-family
    route-distinguisher 200:2   
    apply-label per-instance 
    vpn-target 102:102 export-extcommunity                                             
    vpn-target 102:102 import-extcommunity                                          
  #
  ip vpn-instance outside-vpn
   ipv4-family
    route-distinguisher 200:3    
    apply-label per-instance                                                                                        
    vpn-target 103:103 export-extcommunity                                                                                         
    vpn-target 103:103 import-extcommunity
  #
  ospf 101 vpn-instance inside-vpn1
   default cost inherit-metric
   import-route unr
   opaque-capability enable
   area 0.0.0.0
    network 172.16.10.0 0.0.0.255
  #
  ospf 102 vpn-instance inside-vpn2
   default cost inherit-metric
   import-route unr
   opaque-capability enable
   area 0.0.0.0
    network 172.16.11.0 0.0.0.255
  #
  bgp 300
   private-4-byte-as enable
   #
   ipv4-family unicast
    undo synchronization
   #
   ipv4-family vpn-instance outside-vpn
    import-route direct
    import-route unr
    peer 172.16.9.2 as-number 400
    peer 172.16.9.2 connect-interface GigabitEthernet0/3/0
  #
  remote-backup-service vpn_nat
   peer 172.16.5.2 source 172.16.5.1 port 1024
  #
  service-ha hot-backup enable
  #
  service-location 1
   location slot 1 
   vrrp vrid 1 interface GigabitEthernet 0/2/0
   remote-backup interface GigabitEthernet 0/2/0 peer 172.16.5.2
  #
  service-instance-group group1
   service-location 1
   remote-backup-service vpn_nat
  #
  nat instance nat id 1
   port-range 64
   service-instance-group group1
   nat address-group group1 group-id 1 vpn-instance outside-vpn
    section 0 11.11.11.0 mask 24
   nat outbound any address-group group1
  #
  acl number 3001 
   rule 5 permit ip source 10.1.1.0 0.0.0.255 
  #
  traffic classifier vpn_nat1 operator or
   if-match acl 3001 precedence 1
  #
  traffic behavior vpn_nat1
    nat bind instance nat
  #
  traffic policy vpn_nat1
   share-mode
   classifier vpn_nat1 behavior vpn_nat1 precedence 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 172.16.5.1 255.255.255.0
   vrrp vrid 1 virtual-ip 172.16.5.100
   admin-vrrp vrid 1 ignore-if-down
   vrrp vrid 1 priority 200
   vrrp vrid 1 preempt-mode timer delay 1500
   vrrp vrid 1 track service-location 1 reduced 60
   vrrp vrid 1 track interface GigabitEthernet 0/2/1.1 reduced 60
   vrrp vrid 1 track interface GigabitEthernet 0/2/1.2 reduced 60
   vrrp vrid 1 track interface GigabitEthernet 0/3/0 reduced 60
   vrrp recover-delay 15
  #
  interface GigabitEthernet0/3/0
   ip binding vpn-instance outside-vpn
   ip address 172.16.9.1 255.255.255.0
  #
  interface GigabitEthernet0/2/1.1
   vlan-type dot1q 200
   ip binding vpn-instance inside-vpn1
   ip address 172.16.10.1 255.255.255.0
   traffic-policy vpn_nat1 inbound
  #
  interface GigabitEthernet0/2/1.2
   vlan-type dot1q 202
   ip binding vpn-instance inside-vpn2
   ip address 172.16.11.1 255.255.255.0
   traffic-policy vpn_nat1 inbound
  #
  return
  
  ```
* CGN2 configuration file
  
  ```
  #
  sysname CGN2
  #
  vsm on-board-mode disable
  #
  license
   active nat session-table size 6 slot 1 
   active nat bandwidth-enhance 40 slot 1
  #
  ip vpn-instance inside-vpn1
   ipv4-family
    route-distinguisher 200:1  
    apply-label per-instance                                                           
    vpn-target 101:101 export-extcommunity                                                    
    vpn-target 101:101 import-extcommunity                                                       
  #
  ip vpn-instance inside-vpn2
   ipv4-family
    route-distinguisher 200:2
    apply-label per-instance                                                                   
    vpn-target 102:102 export-extcommunity                                                      
    vpn-target 102:102 import-extcommunity                                           
  #
  ip vpn-instance outside-vpn
   ipv4-family
    route-distinguisher 200:3   
    apply-label per-instance                                                            
    vpn-target 103:103 export-extcommunity                                                            
    vpn-target 103:103 import-extcommunity                                                        
  #
  ospf 101 vpn-instance inside-vpn1
   default cost inherit-metric
   import-route unr
   opaque-capability enable
   area 0.0.0.0
    network 172.16.6.0 0.0.0.255
  #
  ospf 102 vpn-instance inside-vpn2
   default cost inherit-metric
   import-route unr
   opaque-capability enable
   area 0.0.0.0
    network 172.16.7.0 0.0.0.255
  #
  bgp 300
   private-4-byte-as enable
   #
   ipv4-family unicast
    undo synchronization
   #
   ipv4-family vpn-instance outside-vpn
    import-route direct
    import-route unr
    peer 172.16.8.2 as-number 400
    peer 172.16.8.2 connect-interface GigabitEthernet0/3/0
  #
  remote-backup-service vpn_nat
   peer 172.16.5.1 source 172.16.5.2 port 1024
  #
  service-ha hot-backup enable
  #
  service-location 1
   location slot 1 
   vrrp vrid 1 interface GigabitEthernet 0/2/0
   remote-backup interface GigabitEthernet 0/2/0 peer 172.16.5.1
  #
  service-instance-group group1
   service-location 1
   remote-backup-service vpn_nat
  #
  nat instance nat id 1
   port-range 64
   service-instance-group group1
   nat address-group group1 group-id 1 vpn-instance outside-vpn
    section 0 11.11.11.0 mask 24
   nat outbound any address-group group1
  #
  acl number 3001 
   rule 5 permit ip source 10.1.1.0 0.0.0.255 
  #
  traffic classifier vpn_nat1 operator or
   if-match acl 3001 precedence 1
  #
  traffic policy vpn_nat1
   share-mode
   classifier vpn_nat1 behavior vpn_nat1 precedence 1 
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 172.16.5.2 255.255.255.0
   vrrp vrid 1 virtual-ip 172.16.5.100
   admin-vrrp vrid 1 ignore-if-down
   vrrp vrid 1 priority 150
   vrrp vrid 1 track service-location 1 reduced 60
   vrrp recover-delay 15
  #
  interface GigabitEthernet0/3/0
   ip binding vpn-instance outside-vpn
   ip address 172.16.8.1 255.255.255.0
  #
  interface GigabitEthernet0/2/1.1
   vlan-type dot1q 200
   ip binding vpn-instance inside-vpn1
   ip address 172.16.6.1 255.255.255.0
   traffic-policy vpn_nat1 inbound
  #
  interface GigabitEthernet0/2/1.2
   vlan-type dot1q 202
   ip binding vpn-instance inside-vpn2
   ip address 172.16.7.1 255.255.255.0
   traffic-policy vpn_nat1 inbound
  #
  return
  
  ```