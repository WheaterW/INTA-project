Example for Configuring Distributed NAT444 Inter-Chassis Hot Backup
===================================================================

This section provides an example for configuring NAT444 inter-chassis hot backup in distributed deployment mode.

#### Networking Requirements

On the distributed deployment network shown in [Figure 1](#EN-US_TASK_0172362484__fig_01), a NAT service board is installed in slot 1 on BRAS1 and another NAT service board is installed in slot 1 on BRAS2. A VRRP channel is configured between GE interfaces of BRAS1 and BRAS2. NAT inter-chassis hot backup is implemented on CPU 0 of the NAT service board in slot 1 on BRAS1 and CPU 0 of the NAT service board in slot 1 on BRAS2. The BRASs' master/backup status is determined by VRRP, and the service board status is associated with VRRP.

**Figure 1** Networking diagram for configuring distributed dual-device inter-chassis backup![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/1 and GE 0/1/2, respectively.


  
![](images/fig_dc_ne_cgn-reliability_cfg_0003.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Set the number of sessions supported by the service board in slot 1 to 6M.
2. Configure HA hot backup, with NAT service information backed up between CGN devices.
3. Create a service-location group, configure members for HA dual-device inter-chassis backup, and configure a VRRP channel between BRAS1 and BRAS2.
4. Create and configure VRRP groups.
5. Associate HA with VRRP.
6. Bind the service-location group to the VRRP groups.
7. Create a service-instance group and bind it to the service-location group.
8. Create a NAT instance.
9. Configure user information (user group, IP address pool, user domain, and AAA), configure RADIUS authentication on the BRAS, and bind the user group to the NAT instance.
10. Configure a NAT traffic diversion policy and a NAT conversion policy on the master and backup devices.
11. Configure a user-side VRRP group on BRAS1 and BRAS2 that are connected to the switch.
12. Configure RUI to back up user BRAS information on CGN devices.
13. Bind the service-instance group to an RBS.
14. Bind the NAT instance to the service-instance group.
15. Configure a user-side sub-interface.

#### Data Preparation

To complete the configuration, you need the following data:

| No. | Data |
| --- | --- |
| 1 | Index of the service-location group |
| 2 | Slot ID and CPU ID of the active CPU on a service board of BRAS1 (CPU 0 in slot 1 in this example) |
| 3 | Slot ID and CPU ID of the standby CPU on a service board of BRAS2 (CPU 0 in slot 1 in this example) |
| 4 | Names of VRRP interfaces on BRAS1 and BRAS2 |
| 5 | IP addresses of VRRP interfaces on BRAS1 and BRAS2 |
| 6 | Index of a VRRP group |
| 7 | Virtual IP address of a VRRP group |
| 8 | Priorities of VRRP group members |
| 9 | VRRP preemption delay |
| 10 | Name of a service-instance group |
| 11 | Name and index of a NAT instance |
| 12 | IP address pool, IP address of the address pool gateway, and IP address segment of BRAS1 and BRAS2 |
| 13 | Names of the user group and user domain, and AAA schemes on the devices at both ends |
| 14 | Remote backup identifiers for RUI backup of BRAS1 and BRAS2 |
| 15 | Names of user-side interfaces on BRAS1 and BRAS2 |
| 16 | IP addresses of user-side interfaces on BRAS1 and BRAS2 |
| 17 | Index of the user-side VRRP groups on BRAS1 and BRAS2 |
| 18 | Virtual IP address of the user-side VRRP groups on BRAS1 and BRAS2 |
| 19 | User-side VRRP priorities on BRAS1 and BRAS2 |
| 20 | Preemption delay of the user-side VRRP groups on BRAS1 and BRAS2 |



#### Procedure

1. Set the number of sessions supported by the service boards in slot 1 on the master and backup devices to 6M.
   
   # Configure the master device (BRAS1).
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname BRAS1
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~BRAS1] vsm on-board-mode disable
   ```
   ```
   [*BRAS1] commit
   ```
   ```
   [~BRAS1] license
   ```
   ```
   [~BRAS1-license] active nat session-table size 6 slot 1 
   ```
   ```
   [*BRAS1-license] active nat bandwidth-enhance 40 slot 1
   ```
   ```
   [*BRAS1-license] commit
   ```
   ```
   [~BRAS1-license] quit
   ```
   # Configure the backup device (BRAS2).
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname BRAS2
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~BRAS2] vsm on-board-mode disable
   ```
   ```
   [*BRAS2] commit
   ```
   ```
   [~BRAS2] license
   ```
   ```
   [~BRAS2-license] active nat session-table size 6 slot 1 
   ```
   ```
   [*BRAS2-license] active nat bandwidth-enhance 40 slot 1
   ```
   ```
   [*BRAS2-license] commit
   ```
   ```
   [~BRAS2-license] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The method for configuring bandwidth resources varies according to the board type. As such, determine whether to run the **active nat bandwidth-enhance** command and the corresponding parameters based on the board type.
2. Enable HA hot backup on BRAS1 and BRAS2.
   
   
   
   # Enable HA hot backup on BRAS1.
   
   ```
   [~BRAS1] service-ha hot-backup enable
   ```
   ```
   [*BRAS1] commit
   ```
   
   # Enable HA hot backup on BRAS2.
   
   ```
   [~BRAS2] service-ha hot-backup enable
   ```
   ```
   [*BRAS2] commit
   ```
3. Create a service-location group on BRAS1 and BRAS2, configure members for HA dual-device inter-chassis backup, and configure a VRRP channel.
   
   
   
   # Create service-location group 1 on BRAS1, add CPU 0 in slot 1 as an HA dual-device inter-chassis backup member, and set the local VRRP outbound interface to GE 0/1/1 and the peer IP address to 10.1.1.2.
   
   ```
   [~BRAS1] service-location 1
   ```
   ```
   [*BRAS1-service-location-1] location slot 1 
   ```
   ```
   [*BRAS1-service-location-1] remote-backup interface GigabitEthernet 0/1/1 peer 10.1.1.2
   ```
   ```
   [*BRAS1-service-location-1] commit
   ```
   ```
   [~BRAS1-service-location-1] quit
   ```
   
   # Create service-location group 1 on BRAS2, add CPU 0 in slot 1 as an HA dual-device inter-chassis backup member, and set the local VRRP outbound interface to GE 0/1/1 and the peer IP address to 10.1.1.1.
   
   ```
   [~BRAS2] service-location 1
   ```
   ```
   [*BRAS2-service-location-1] location slot 1 
   ```
   ```
   [*BRAS2-service-location-1] remote-backup interface GigabitEthernet 0/1/1 peer 10.1.1.1
   ```
   ```
   [*BRAS2-service-location-1] commit
   ```
   ```
   [~BRAS2-service-location-1] quit
   ```
4. Configure a VRRP group on BRAS1 and BRAS2.
   
   
   
   # On BRAS1, enter the view of GE 0/1/1, create VRRP group 1, and set the virtual IP address of the VRRP group to 10.1.1.3. Configure the VRRP group as an mVRRP group, and set BRAS1's priority in the VRRP group to 200, the VRRP preemption delay to 1500s, and the VRRP recovery delay to 20s.
   
   ```
   [~BRAS1] interface GigabitEthernet 0/1/1
   ```
   ```
   [~BRAS1-GigabitEthernet0/1/1] vrrp vrid 1 virtual-ip 10.1.1.3
   ```
   ```
   [*BRAS1-GigabitEthernet0/1/1] admin-vrrp vrid 1 ignore-if-down
   ```
   ```
   [*BRAS1-GigabitEthernet0/1/1] vrrp vrid 1 priority 200
   ```
   ```
   [*BRAS1-GigabitEthernet0/1/1] vrrp vrid 1 preempt-mode timer delay 1500
   ```
   ```
   [*BRAS1-GigabitEthernet0/1/1] vrrp recover-delay 20
   ```
   ```
   [*BRAS1-GigabitEthernet0/1/1] commit
   ```
   ```
   [~BRAS1-GigabitEthernet0/1/1] quit
   ```
   
   # On BRAS2, enter the view of GE 0/1/1, create VRRP group 1, and set the virtual IP address of the VRRP group to 10.1.1.3. Configure the VRRP group as an mVRRP group, set BRAS2's priority in the VRRP group to 150, and set the VRRP recovery delay to 15s.
   
   ```
   [~BRAS2] interface GigabitEthernet 0/1/1
   ```
   ```
   [*BRAS2-GigabitEthernet0/1/1] vrrp vrid 1 virtual-ip 10.1.1.3
   ```
   ```
   [*BRAS2-GigabitEthernet0/1/1] admin-vrrp vrid 1 ignore-if-down
   ```
   ```
   [*BRAS2-GigabitEthernet0/1/1] vrrp vrid 1 priority 150
   ```
   ```
   [*BRAS2-GigabitEthernet0/1/1] vrrp recover-delay 15
   ```
   ```
   [*BRAS2-GigabitEthernet0/1/1] commit
   ```
   ```
   [~BRAS2-GigabitEthernet0/1/1] quit
   ```
5. Associate HA with VRRP on each device.
   
   
   
   # On BRAS1, enter the view of GE 0/1/1, and associate service-location group 1 with VRRP group 1.
   
   ```
   [~BRAS1] interface GigabitEthernet 0/1/1
   ```
   ```
   [~BRAS1-GigabitEthernet0/1/1] vrrp vrid 1 track service-location 1 reduced 60
   ```
   ```
   [*BRAS1-GigabitEthernet0/1/1] commit
   ```
   ```
   [~BRAS1-GigabitEthernet0/1/1] quit
   ```
   
   # On BRAS2, enter the view of GE 0/1/1, and associate service-location group 1 with VRRP group 1.
   
   ```
   [~BRAS2] interface GigabitEthernet 0/1/1
   ```
   ```
   [~BRAS2-GigabitEthernet0/1/1] vrrp vrid 1 track service-location 1 reduced 60
   ```
   ```
   [*BRAS2-GigabitEthernet0/1/1] commit
   ```
   ```
   [~BRAS2-GigabitEthernet0/1/1] quit
   ```
   
   # Run the [**display vrrp 1**](cmdqueryname=display+vrrp+1) command on BRAS1 and BRAS2 to view the master/backup VRRP status, which reflects the master/backup status of the service-location group. **State** in the command output indicates the BRAS status.
   
   ```
   [~BRAS1] display vrrp 1
   GigabitEthernet 0/1/1 | Virtual Router 1                                                                                      
       State                    : Master 
       Virtual IP               : 10.1.1.3  
       Master IP                : 10.1.1.1 
       Local IP                 : 10.1.1.1
       PriorityRun              : 200    
       PriorityConfig           : 200    
       MasterPriority           : 200    
       Preempt                  : YES      Delay Time    : 400 s    
       Hold Multiplier          : 3                                                           
       TimerRun                 : 1 s    
       TimerConfig              : 1 s   
       Auth Type                : NONE    
       Virtual MAC              : 00e0-fc12-3456 
       Check TTL                : YES      
       Config Type              : admin-vrrp 
       Backup-forward           : disabled   
       Fast-resume              : disabled     
       Track Service-location   : 1   Priority Reduced : 60                                                    
       Service-location State   : UP                                                                
       Create Time              : 2011-10-18 11:14:48 UTC+10:59   
       Last Change Time         : 2011-10-18 14:02:46 UTC+10:59
   
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   **Master** in the command output indicates that BRAS1 is the master device.
   
   ```
   [~BRAS2] display vrrp 1
   GigabitEthernet0/1/1 | Virtual Router 1                                                                                       
       State                   : Backup  
       Virtual IP              : 10.1.1.3   
       Master IP               : 10.1.1.1
       Local IP                : 10.1.1.2
       PriorityRun             : 150      
       PriorityConfig          : 150     
       MasterPriority          : 200    
       Preempt                 : YES    Delay Time  : 0 s  
       Hold Multiplier         : 3                                                                        
       TimerRun                : 1 s     
       TimerConfig             : 1 s     
       Auth Type               : NONE    
       Virtual MAC             : 00e0-fc12-3456  
       Check TTL               : YES       
       Config Type             : admin-vrrp   
       Backup-forward          : disabled    
       Fast-resume             : disabled
       Track Service-location  : 1   Priority Reduced : 60                                                       
       Service-location State : UP   
       Create Time            : 2011-10-18 11:26:40 UTC+08:00  
       Last Change Time       : 2011-10-18 14:02:22 UTC+08:00
   ```
6. Bind the service-location group to the VRRP group on BRAS1 and BRAS2.
   
   
   
   # Bind service-location group 1 to VRRP group 1 on BRAS1.
   
   ```
   [~BRAS1] service-location 1
   ```
   ```
   [~BRAS1-service-location-1] vrrp vrid 1 interface GigabitEthernet 0/1/1
   ```
   ```
   [*BRAS1-service-location-1] commit
   ```
   ```
   [~BRAS1-service-location-1] quit
   ```
   
   # Bind service-location group 1 to VRRP group 1 on BRAS2.
   
   ```
   [~BRAS2] service-location 1
   ```
   ```
   [~BRAS2-service-location-1] vrrp vrid 1 interface GigabitEthernet 0/1/1
   ```
   ```
   [*BRAS2-service-location-1] commit
   ```
   ```
   [~BRAS2-service-location-1] quit
   ```
7. Create a service-instance group on BRAS1 and BRAS2 and bind them to the service-location group.
   
   
   
   # Create a service-instance group named **group1** on BRAS1 and bind it to service-location group 1.
   
   ```
   [~BRAS1] service-instance-group group1
   ```
   ```
   [*BRAS1-service-instance-group-group1] service-location 1
   ```
   ```
   [*BRAS1-service-instance-group-group1] commit
   ```
   ```
   [~BRAS1-service-instance-group-group1] quit
   ```
   
   # Create a service-instance group named **group1** on BRAS2 and bind it to service-location group 1.
   
   ```
   [~BRAS2] service-instance-group group1
   ```
   ```
   [*BRAS2-service-instance-group-group1] service-location 1
   ```
   ```
   [*BRAS2-service-instance-group-group1] commit
   ```
   ```
   [~BRAS2-service-instance-group-group1] quit
   ```
   
   # Run the [**display service-location 1**](cmdqueryname=display+service-location+1) command on BRAS1 and BRAS2 to view HA information. **Vrrp state** in the command output indicates the status of the service-location group, which must be consistent with the BRAS's VRRP status. **Batch-backup state** in the command output indicates whether batch backup is completed.
   
   ```
   [~BRAS1] display service-location 1
    service-location 1                                                                         
    Backup scene type: inter-box                                                              
    Location slot ID: 1                                                                  
    Remote-backup interface: GigabitEthernet0/1/1                                          
    Peer: 10.1.1.2                                                                             
    Vrrp ID: 1                                                                                                  
    Vrrp bind interface: GigabitEthernet0/1/1                                                            
    Vrrp state: master                                                                                  
    Bound service-instance-group number: 1                                                                
    Batch-backup state: finished
   ```
   ```
   [~BRAS2] display service-location 1
    service-location 1                                                                                            
    Backup scene type: inter-box                                                                                     
    Location slot ID: 1                                                                   
    Remote-backup interface: GigabitEthernet0/1/1                                                     
    Peer: 10.1.1.1                                                                                     
    Vrrp ID: 1                                                                                                   
    Vrrp bind interface: GigabitEthernet0/1/1                                                                        
    Vrrp state: slave                                                                                             
    Bound service-instance-group number: 1                                                              
    Batch-backup state: NA
   ```
8. Create a NAT instance on both master and backup devices.
   
   
   
   # Create a NAT instance named **nat** on BRAS1.
   
   ```
   [~BRAS1] nat instance nat id 1
   ```
   ```
   [*BRAS1-nat-instance-nat] commit
   ```
   ```
   [~BRAS1-nat-instance-nat] quit
   ```
   
   # Create a NAT instance on BRAS2.
   
   ```
   [~BRAS2] nat instance nat id 1
   ```
   ```
   [*BRAS2-nat-instance-nat] commit
   ```
   ```
   [~BRAS2-nat-instance-nat] quit
   ```
9. Configure user information (user group named **natbras**, IP address pool named **natbras**, user domain named **natbras**, and AAA) and bind the user group to the NAT instance named **nat** on each of the master and backup devices.
   
   
   
   # Configure BRAS1.
   
   ```
   [~BRAS1] user-group natbras
   ```
   ```
   [~BRAS1] commit
   ```
   ```
   [~BRAS1] ip pool natbras bas local
   ```
   ```
   [*BRAS1-ip-pool-natbras] gateway 192.168.0.1 255.255.255.0
   ```
   ```
   [*BRAS1-ip-pool-natbras] commit
   ```
   ```
   [~BRAS1-ip-pool-natbras] section 0 192.168.0.2 192.168.0.254
   ```
   ```
   [~BRAS1-ip-pool-natbras] quit
   ```
   ```
   [~BRAS1] radius-server group rd1
   ```
   ```
   [*BRAS1-radius-rd1] radius-server authentication 192.168.7.249 1645 weight 0
   ```
   ```
   [*BRAS1-radius-rd1] radius-server accounting 192.168.7.249 1646 weight 0
   ```
   ```
   [*BRAS1-radius-rd1] radius-server shared-key YsHsjx_202206
   ```
   ```
   [*BRAS1-radius-rd1] commit
   ```
   ```
   [~BRAS1-radius-rd1] radius-server type plus11
   ```
   ```
   [~BRAS1-radius-rd1] radius-server traffic-unit kbyte
   ```
   ```
   [~BRAS1-radius-rd1] quit
   ```
   ```
   [~BRAS1] aaa
   ```
   ```
   [~BRAS1-aaa] authentication-scheme auth1
   ```
   ```
   [*BRAS1-aaa-authen-auth1] authentication-mode radius
   ```
   ```
   [*BRAS1-aaa-authen-auth1] commit
   ```
   ```
   [~BRAS1-aaa-authen-auth1] quit
   ```
   ```
   [~BRAS1-aaa] accounting-scheme acct1
   ```
   ```
   [*BRAS1-aaa-accounting-acct1] accounting-mode radius
   ```
   ```
   [~BRAS1-aaa-accounting-acct1] commit
   ```
   ```
   [~BRAS1-aaa-accounting-acct1] quit
   ```
   ```
   [~BRAS1-aaa] domain natbras
   ```
   ```
   [*BRAS1-aaa-domain-natbras] authentication-scheme auth1
   ```
   ```
   [*BRAS1-aaa-domain-natbras] accounting-scheme acct1
   ```
   ```
   [*BRAS1-aaa-domain-natbras] radius-server group rd1
   ```
   ```
   [*BRAS1-aaa-domain-natbras] commit
   ```
   ```
   [~BRAS1-aaa-domain-natbras] ip-pool natbras
   ```
   ```
   [~BRAS1-aaa-domain-natbras] user-group natbras bind nat instance nat
   ```
   ```
   [*BRAS1-aaa-domain-natbras] quit
   ```
   ```
   [~BRAS1-aaa] quit
   ```
   
   # Configure BRAS2.
   
   ```
   [~BRAS2] user-group natbras
   ```
   ```
   [~BRAS2] commit
   ```
   ```
   [~BRAS2] ip pool natbras bas local
   ```
   ```
   [*BRAS2-ip-pool-natbras] gateway 192.168.0.1 255.255.255.0
   ```
   ```
   [*BRAS2-ip-pool-natbras] commit
   ```
   ```
   [~BRAS2-ip-pool-natbras] section 0 192.168.0.2 192.168.0.254
   ```
   ```
   [~BRAS2-ip-pool-natbras] quit
   ```
   ```
   [~BRAS2] radius-server group rd1
   ```
   ```
   [*BRAS2-radius-rd1] radius-server authentication 192.168.7.249 1645 weight 0
   ```
   ```
   [*BRAS2-radius-rd1] radius-server accounting 192.168.7.249 1646 weight 0
   ```
   ```
   [*BRAS2-radius-rd1] radius-server shared-key YsHsjx_202206
   ```
   ```
   [*BRAS2-radius-rd1] commit
   ```
   ```
   [~BRAS2-radius-rd1] radius-server type plus11
   ```
   ```
   [~BRAS2-radius-rd1] radius-server traffic-unit kbyte
   ```
   ```
   [~BRAS2-radius-rd1] quit
   ```
   ```
   [~BRAS2] aaa
   ```
   ```
   [~BRAS2-aaa] authentication-scheme auth1
   ```
   ```
   [*BRAS2-aaa-authen-auth1] authentication-mode radius
   ```
   ```
   [*BRAS2-aaa-authen-auth1] commit
   ```
   ```
   [~BRAS2-aaa-authen-auth1] quit
   ```
   ```
   [~BRAS2-aaa] accounting-scheme acct1
   ```
   ```
   [*BRAS2-aaa-accounting-acct1] accounting-mode radius
   ```
   ```
   [~BRAS2-aaa-accounting-acct1] commit
   ```
   ```
   [~BRAS2-aaa-accounting-acct1] quit
   ```
   ```
   [~BRAS2-aaa] domain natbras
   ```
   ```
   [*BRAS2-aaa-domain-natbras] authentication-scheme auth1
   ```
   ```
   [*BRAS2-aaa-domain-natbras] accounting-scheme acct1
   ```
   ```
   [*BRAS2-aaa-domain-natbras] radius-server group rd1
   ```
   ```
   [*BRAS2-aaa-domain-natbras] commit
   ```
   ```
   [~BRAS2-aaa-domain-natbras] ip-pool natbras
   ```
   ```
   [~BRAS2-aaa-domain-natbras] user-group natbras bind nat instance nat
   ```
   ```
   [*BRAS2-aaa-domain-natbras] quit
   ```
   ```
   [~BRAS2-aaa] quit
   ```
10. Configure a traffic classification rule, a NAT behavior, and a NAT traffic policy and apply the NAT traffic policy on each of the master and backup devices. For details, see "Example for Configuring Distributed NAT" in *IPv6 Transition > NAT Configuration*.
    
    
    
    # Configure a NAT conversion policy on BRAS1.
    
    1. Configure an ACL numbered 6001 and an ACL rule numbered 1.
       
       ```
       [~BRAS1] acl 6001
       ```
       ```
       [*BRAS1-acl-ucl-6001] rule 1 permit ip source user-group natbras
       ```
       ```
       [*BRAS1-acl-ucl-6001] commit
       ```
       ```
       [~BRAS1-acl-ucl-6001] quit
       ```
    2. Configure an ACL numbered 3001.
       
       ```
       [~BRAS1] acl 3001
       ```
       ```
       [*BRAS1-acl4-advance-3001] rule 10 permit ip source 192.168.0.0 0.0.255.255
       ```
       ```
       [*BRAS1-acl4-advance-3001] commit
       ```
       ```
       [~BRAS1-acl4-advance-3001] quit
       ```
    3. Configure a traffic classifier.
       
       ```
       [~BRAS1] traffic classifier c1
       ```
       ```
       [*BRAS1-classifier-c1] if-match acl 6001
       ```
       ```
       [*BRAS1-classifier-c1] commit
       ```
       ```
       [~BRAS1-classifier-c1] quit
       ```
    4. Configure a traffic behavior.
       
       ```
       [~BRAS1] traffic behavior b1 
       ```
       ```
       [*BRAS1-behavior-b1] nat bind instance nat
       ```
       ```
       [*BRAS1-behavior-b1] commit
       ```
       ```
       [~BRAS1-behavior-b1] quit
       ```
    5. Define a traffic policy to associate the traffic classifier with the traffic behavior.
       
       ```
       [~BRAS1] traffic policy p1
       ```
       ```
       [*BRAS1-trafficpolicy-p1] classifier c1 behavior b1
       ```
       ```
       [*BRAS1-trafficpolicy-p1] commit
       ```
       ```
       [~BRAS1-trafficpolicy-p1] quit
       ```
    6. Apply the NAT traffic diversion policy in the system view.
       
       ```
       [~BRAS1] traffic-policy p1 inbound
       ```
       ```
       [*BRAS1] commit
       ```
    7. Configure a NAT traffic conversion policy.
       
       ```
       [~BRAS1] nat instance nat
       ```
       ```
       [~BRAS1-nat-instance-nat] nat address-group address-group1 group-id 1 11.11.11.100 11.11.11.105
       ```
       ```
       [*BRAS1-nat-instance-nat] nat outbound 3001 address-group address-group1
       ```
       ```
       [*BRAS1-nat-instance-nat] commit
       ```![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    The configuration of BRAS2 is similar to that of BRAS1. For configuration details, see [BRAS2 configuration file](#EN-US_TASK_0172362484__config_02) in this section.
11. On each of the master and backup devices, configure a user-side VRRP group (between BRAS1/BRAS2 and SWITCH) and enable it to track the service-location group. If the service-location group is not tracked, a CGN board failure cannot trigger a master/backup BRAS switchover. As a result, new distributed NAT users cannot go online.
    
    
    
    # Configure BRAS1 (between BRAS1 and SWITCH).
    
    ```
    [~BRAS1] interface GigabitEthernet0/1/2.2
    ```
    ```
    [~BRAS1-GigabitEthernet0/1/2.2] vlan-type dot1q 2002
    ```
    ```
    [*BRAS1-GigabitEthernet0/1/2.2] ip address 192.168.2.10 255.255.255.0
    ```
    ```
    [*BRAS1-GigabitEthernet0/1/2.2] vrrp vrid 2 virtual-ip 192.168.2.200
    ```
    ```
    [*BRAS1-GigabitEthernet0/1/2.2] admin-vrrp vrid 2
    ```
    ```
    [*BRAS1-GigabitEthernet0/1/2.2] vrrp vrid 2 priority 150
    ```
    ```
    [*BRAS1-GigabitEthernet0/1/2.2] vrrp vrid 2 preempt-mode timer delay 1500
    ```
    ```
    [*BRAS1-GigabitEthernet0/1/2.2] vrrp recover-delay 20
    ```
    ```
    [*BRAS1-GigabitEthernet0/1/2.2] vrrp vrid 2 track service-location 1 reduced 50
    ```
    ```
    [*BRAS1-GigabitEthernet0/1/2.2] commit
    ```
    ```
    [~BRAS1-GigabitEthernet0/1/2.2] quit
    ```
    
    # Configure BRAS2 (between BRAS2 and SWITCH).
    
    ```
    [~BRAS2] interface GigabitEthernet0/1/2.2
    ```
    ```
    [~BRAS2-GigabitEthernet0/1/2.2] vlan-type dot1q 2002
    ```
    ```
    [*BRAS2-GigabitEthernet0/1/2.2] ip address 192.168.2.100 255.255.255.0
    ```
    ```
    [*BRAS2-GigabitEthernet0/1/2.2] vrrp vrid 2 virtual-ip 192.168.2.200
    ```
    ```
    [*BRAS2-GigabitEthernet0/1/2.2] admin-vrrp vrid 2
    ```
    ```
    [*BRAS2-GigabitEthernet0/1/2.2] vrrp vrid 2 priority 120
    ```
    ```
    [*BRAS2-GigabitEthernet0/1/2.2] vrrp vrid 2 track service-location 1
    ```
    ```
    [*BRAS2-GigabitEthernet0/1/2.2] commit
    ```
    ```
    [~BRAS2-GigabitEthernet0/1/2.2] quit
    ```
12. Configure RUI to back up BRAS information on BRAS1 and BRAS2.
    1. Configure an RBS on BRAS1 and BRAS2.
       
       
       
       # Configure an RBS on BRAS1.
       
       ```
       [~BRAS1] remote-backup-service natbras
       ```
       ```
       [*BRAS1-rm-backup-srv-natbras] peer 10.1.1.2 source 10.1.1.1 port 7000
       ```
       ```
       [*BRAS1-rm-backup-srv-natbras] protect redirect ip-nexthop 10.1.1.2 interface GigabitEthernet0/1/1
       ```
       ```
       [*BRAS1-rm-backup-srv-natbras] ip-pool natbras
       ```
       ```
       [*BRAS1-rm-backup-srv-natbras] commit
       ```
       ```
       [~BRAS1-rm-backup-srv-natbras] quit
       ```
       
       # Configure an RBS on BRAS2.
       
       ```
       [~BRAS2] remote-backup-service natbras
       ```
       ```
       [*BRAS2-rm-backup-srv-natbras] peer 10.1.1.1 source 10.1.1.2 port 7000
       ```
       ```
       [*BRAS2-rm-backup-srv-natbras] protect redirect ip-nexthop 10.1.1.1 interface GigabitEthernet0/1/1
       ```
       ```
       [*BRAS2-rm-backup-srv-natbras] ip-pool natbras
       ```
       ```
       [*BRAS2-rm-backup-srv-natbras] commit
       ```
       ```
       [~BRAS2-rm-backup-srv-natbras] quit
       ```
    2. Configure a remote backup profile (RBP) on BRAS1 and BRAS2.
       
       
       
       # Configure an RBP named **natbras** on BRAS1.
       
       ```
       [~BRAS1] remote-backup-profile natbras
       ```
       ```
       [*BRAS1-rm-backup-prf-natbras] service-type bras
       ```
       ```
       [*BRAS1-rm-backup-prf-natbras] backup-id 10 remote-backup-service natbras
       ```
       ```
       [*BRAS1-rm-backup-prf-natbras] peer-backup hot
       ```
       ```
       [*BRAS1-rm-backup-prf-natbras] vrrp-id 2 interface GigabitEthernet0/1/2.2
       ```
       ```
       [*BRAS1-rm-backup-prf-natbras] commit
       ```
       ```
       [~BRAS1-rm-backup-prf-natbras] quit
       ```
       
       # Configure an RBP named **natbras** on BRAS2.
       
       ```
       [~BRAS2] remote-backup-profile natbras
       ```
       ```
       [*BRAS2-rm-backup-prf-natbras] service-type bras
       ```
       ```
       [*BRAS2-rm-backup-prf-natbras] backup-id 10 remote-backup-service natbras
       ```
       ```
       [*BRAS2-rm-backup-prf-natbras] peer-backup hot
       ```
       ```
       [*BRAS2-rm-backup-prf-natbras] vrrp-id 2 interface GigabitEthernet0/1/2.2
       ```
       ```
       [*BRAS2-rm-backup-prf-natbras] commit
       ```
       ```
       [~BRAS2-rm-backup-prf-natbras] quit
       ```
13. Bind the service-instance group to the RBS.
    
    
    
    # Configure BRAS1.
    
    ```
    [~BRAS1] service-instance-group group1
    ```
    ```
    [*BRAS1-service-instance-group-group1] remote-backup-service natbras
    ```
    ```
    [*BRAS1-service-instance-group-group1] commit
    ```
    ```
    [~BRAS1-service-instance-group-group1] quit
    ```
    
    # Configure BRAS2.
    
    ```
    [~BRAS2] service-instance-group group1
    ```
    ```
    [*BRAS2-service-instance-group-group1] remote-backup-service natbras
    ```
    ```
    [*BRAS2-service-instance-group-group1] commit
    ```
    ```
    [~BRAS2-service-instance-group-group1] quit
    ```
14. Bind service-instance groups to NAT instances.
    
    
    
    # Configure BRAS1.
    
    ```
    [~BRAS1] nat instance nat id 1
    ```
    ```
    [~BRAS1-nat-instance-nat] service-instance-group group1
    ```
    ```
    [*BRAS1-nat-instance-nat] commit
    ```
    ```
    [~BRAS1-nat-instance-nat] quit
    ```
    
    # Configure BRAS2.
    
    ```
    [~BRAS2] nat instance nat id 1
    ```
    ```
    [~BRAS2-nat-instance-nat] service-instance-group group1
    ```
    ```
    [*BRAS2-nat-instance-nat] commit
    ```
    ```
    [~BRAS2-nat-instance-nat] quit
    ```
15. Configure user-side sub-interfaces on BRAS1 and BRAS2.
    
    
    
    # Configure a user-side sub-interface on BRAS1.
    
    ```
    [~BRAS1] interface GigabitEthernet0/1/2.10
    ```
    ```
    [*BRAS1-GigabitEthernet0/1/2.10] commit
    ```
    ```
    [~BRAS1-GigabitEthernet0/1/2.10] user-vlan 2010
    ```
    ```
    [~BRAS1-GigabitEthernet0/1/2.10-vlan-2010-2010] quit
    ```
    ```
    [~BRAS1-GigabitEthernet0/1/2.10] remote-backup-profile natbras
    ```
    ```
    [*BRAS1-GigabitEthernet0/1/2.10] commit
    ```
    ```
    [~BRAS1-GigabitEthernet0/1/2.10] bas
    ```
    ```
    [~BRAS1-GigabitEthernet0/1/2.10-bas] access-type layer2-subscriber default-domain authentication natbras
    ```
    ```
    [*BRAS1-GigabitEthernet0/1/2.10-bas] commit
    ```
    ```
    [~BRAS1-GigabitEthernet0/1/2.10-bas] quit
    ```
    ```
    [~BRAS1-GigabitEthernet0/1/2.10] quit
    ```
    
    # Configure a user-side sub-interface on BRAS2.
    
    ```
    [~BRAS2] interface GigabitEthernet0/1/2.10
    ```
    ```
    [*BRAS2-GigabitEthernet0/1/2.10] commit
    ```
    ```
    [~BRAS2-GigabitEthernet0/1/2.10] user-vlan 2010
    ```
    ```
    [~BRAS2-GigabitEthernet0/1/2.10-vlan-2010-2010] quit
    ```
    ```
    [~BRAS2-GigabitEthernet0/1/2.10] remote-backup-profile natbras
    ```
    ```
    [*BRAS2-GigabitEthernet0/1/2.10] commit
    ```
    ```
    [~BRAS2-GigabitEthernet0/1/2.10] bas
    ```
    ```
    [~BRAS2-GigabitEthernet0/1/2.10-bas] access-type layer2-subscriber default-domain authentication natbras
    ```
    ```
    [*BRAS2-GigabitEthernet0/1/2.10-bas] commit
    ```
    ```
    [~BRAS2-GigabitEthernet0/1/2.10-bas] quit
    ```
    ```
    [~BRAS2-GigabitEthernet0/1/2.10] quit
    ```

#### Configuration Files

* BRAS1 configuration file
  
  ```
  #
  sysname BRAS1
  #
  vsm on-board-mode disable
  #
  license
   active nat session-table size 6 slot 1 
   active nat bandwidth-enhance 40 slot 1
  #
  radius-server group rd1
   radius-server authentication 192.168.7.249 1645 weight 0
   radius-server accounting 192.168.7.249 1646 weight 0
   radius-server shared-key %^%#x*CgITP4C~;q,*+DEW'JBWe#)"Q&|7bX]b:Y<{w'%^%#
   radius-server type plus11
   radius-server traffic-unit kbyte
  #
  acl number 3001
   rule 10 permit ip source 192.168.0.0 0.0.255.255
  #
  acl number 6001
   rule 1 permit ip source user-group natbras
  #
  traffic classifier c1 operator or
   if-match acl 6001 precedence 1
  #
  traffic behavior b1
   nat bind instance nat
  #
  traffic policy p1
   share-mode 
   classifier c1 behavior b1 precedence 1
  #
  traffic-policy p1 inbound
  #
  service-ha hot-backup enable
  service-ha delay-time 10
  #
  service-location 1
   location slot 1 
   vrrp vrid 1 interface GigabitEthernet 0/1/1
   remote-backup interface GigabitEthernet 0/1/1 peer 10.1.1.2
  #
  service-instance-group group1
   service-location 1
   remote-backup-service natbras
  #
  nat instance nat id 1
   service-instance-group group1
   nat address-group address-group1 group-id 1 11.11.11.100 11.11.11.105
   nat outbound 3001 address-group address-group1
  #
  user-group natbras
  #
  ip pool natbras bas local
   gateway 192.168.0.1 255.255.255.0
   section 0 192.168.0.2 192.168.0.254
  #
  aaa
   authentication-scheme auth1
    authentication-mode radius
   accounting-scheme acct1
    accounting-mode radius
   domain natbras
    authentication-scheme auth1
    accounting-scheme acct1
    radius-server group rd1
    ip-pool natbras
    user-group natbras bind nat instance nat
  #
  remote-backup-service natbras
   peer 10.1.1.2 source 10.1.1.1 port 7000
   protect redirect ip-nexthop 10.1.1.2 interface GigabitEthernet0/1/1
   ip-pool natbras
  #
  remote-backup-profile natbras
   service-type bras
   backup-id 10 remote-backup-service natbras
   peer-backup hot
   vrrp-id 2 interface GigabitEthernet0/1/2.2
  #
  interface Virtual-Template1
   ppp authentication-mode auto
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   vrrp vrid 1 virtual-ip 10.1.1.3
   admin-vrrp vrid 1 ignore-if-down
   vrrp vrid 1 priority 200
   vrrp vrid 1 preempt-mode timer delay 1500
   vrrp recover-delay 20
   vrrp vrid 1 track service-location 1 reduced 60
  #
  interface GigabitEthernet0/1/2.10
   user-vlan 2010
   remote-backup-profile natbras
   pppoe-server bind Virtual-Template 1
   bas
    access-type layer2-subscriber default-domain authentication natbras
    authentication-method ppp
  #
  interface GigabitEthernet0/1/2.2
   vlan-type dot1q 2002
   ip address 192.168.2.10 255.255.255.0
   vrrp vrid 2 virtual-ip 192.168.2.200
   admin-vrrp vrid 2
   vrrp vrid 2 priority 150
   vrrp vrid 2 preempt-mode timer delay 1500
   vrrp recover-delay 20
   vrrp vrid 2 track service-location 1 reduced 50
  #
  return
  ```
* BRAS2 configuration file
  
  ```
  #
  sysname BRAS2
  #
  vsm on-board-mode disable
  #
  license
   active nat session-table size 6 slot 1 
   active nat bandwidth-enhance 40 slot 1
  #
  radius-server group rd1
   radius-server authentication 192.168.7.249 1645 weight 0
   radius-server accounting 192.168.7.249 1646 weight 0
   radius-server shared-key %^%#x*CgITP4C~;q,*+DEW'JBWe#)"Q&|7bX]b:Y<{w'%^%#
   radius-server type plus11
   radius-server traffic-unit kbyte
  #
  acl number 3001
   rule 10 permit ip source 192.168.0.0 0.0.255.255
  #
  acl number 6001
   rule 1 permit ip source user-group natbras
  #
  traffic classifier c1 operator or
   if-match acl 6001 precedence 1
  #
  traffic behavior b1
   nat bind instance nat
  #
  traffic policy p1
   share-mode
   classifier c1 behavior b1 precedence 1
  #
  traffic-policy p1 inbound
  #
  service-ha hot-backup enable
  #
  service-location 1
   location slot 1 
   vrrp vrid 1 interface GigabitEthernet 0/1/1
   remote-backup interface GigabitEthernet 0/1/1 peer 10.1.1.1
  #
  service-instance-group group1
   service-location 1
   remote-backup-service natbras
  #
  nat instance nat id 1
   service-instance-group group1
   nat address-group address-group1 group-id 1 11.11.11.100 11.11.11.105
   nat outbound 3001 address-group address-group1
  #
  user-group natbras
  #
  ip pool natbras bas local
   gateway 192.168.0.1 255.255.255.0
   section 0 192.168.0.2 192.168.0.254
  #
  aaa
   authentication-scheme auth1
    authentication-mode radius
   accounting-scheme acct1
    accounting-mode radius
   domain natbras
    authentication-scheme auth1
    accounting-scheme acct1
    radius-server group rd1
    ip-pool natbras
    user-group natbras bind nat instance nat
  #
  remote-backup-service natbras
   peer 10.1.1.1 source 10.1.1.2 port 7000
   protect redirect ip-nexthop 10.1.1.1 interface GigabitEthernet0/1/1
   ip-pool natbras
  #
  remote-backup-profile natbras
   service-type bras
   backup-id 10 remote-backup-service natbras
   peer-backup hot
   vrrp-id 2 interface GigabitEthernet0/1/2.2
  #
  interface Virtual-Template1
   ppp authentication-mode auto
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
   vrrp vrid 1 virtual-ip 10.1.1.3
   admin-vrrp vrid 1 ignore-if-down
   vrrp vrid 1 priority 150
   vrrp vrid 1 track service-location 1 reduced 60
   vrrp recover-delay 15
  #
  interface GigabitEthernet0/1/2.10
   user-vlan 2010
   pppoe-server bind Virtual-Template 1
   remote-backup-profile natbras
   bas
    access-type layer2-subscriber default-domain authentication natbras
    authentication-method ppp
  #
  interface GigabitEthernet0/1/2.2
   vlan-type dot1q 2002
   ip address 192.168.2.100 255.255.255.0
   vrrp vrid 2 virtual-ip 192.168.2.200
   admin-vrrp vrid 2
   vrrp vrid 2 priority 120
   vrrp vrid 2 track service-location 1
  #
  return
  ```