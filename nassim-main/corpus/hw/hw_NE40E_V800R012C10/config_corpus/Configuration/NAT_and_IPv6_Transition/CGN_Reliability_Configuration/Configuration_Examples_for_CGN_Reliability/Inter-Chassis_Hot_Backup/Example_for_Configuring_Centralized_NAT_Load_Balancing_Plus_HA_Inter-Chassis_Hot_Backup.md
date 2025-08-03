Example for Configuring Centralized NAT Load Balancing Plus HA Inter-Chassis Hot Backup
=======================================================================================

This section provides an example for configuring centralized NAT load balancing plus HA inter-chassis hot backup.

#### Networking Requirements

In the centralized networking scenario shown in [figure1](#EN-US_TASK_0279436213__fig19851104104917), CGN1 and CGN2 are deployed close to the CR on the MAN core as standalone devices, and a NAT service board is installed in slot 1 on each CGN device. Load balancing needs to be implemented between the different CPUs on the NAT service boards on both CGN devices. A VRRP channel also needs to be established between the two devices through GE interfaces. In addition, the master/backup states of the CGN devices need to be determined through VRRP, and the states of service CPUs need to be consistent with the VRRP states.

**Figure 1** Networking for configuring centralized NAT load balancing plus HA inter-chassis hot backup![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/2/1, GE 0/2/2, and GE 0/2/3, respectively.


  
![](figure/en-us_image_0279711999.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Set the number of sessions supported by the service board in slot 1 to 6M.
2. Enable HA hot backup.
3. Create a service-location group, configure members for HA dual-device inter-chassis backup, and configure a VRRP channel.
4. Create and configure VRRP groups.
5. Associate HA with the VRRP groups.
6. Bind the service-location groups to the VRRP groups.
7. Create service-instance groups and bind them to the service-location groups.
8. Create NAT instances and bind them to the service-instance groups.
9. Configure NAT traffic diversion policies and NAT conversion policies.
10. Import the desired default route.
11. Configure a route-policy on the user-side device.

#### Data Preparation

To complete the configuration, you need the following data:

| No. | Data |
| --- | --- |
| 1 | Index of the service-location group |
| 2 | Slot ID and CPU IDs of the service board on CGN1 |
| 3 | Slot ID and CPU IDs of the service board on CGN2 |
| 4 | Interfaces of the VRRP channel on the master and backup devices |
| 5 | IP address of the VRRP channel's interface on the master and backup devices |
| 6 | Indexes of the VRRP groups |
| 7 | Virtual IP addresses of the VRRP groups |
| 8 | Priorities of VRRP group members |
| 9 | VRRP preemption delay |
| 10 | Names of the service-instance groups |
| 11 | Names and indexes of the NAT instances |
| 12 | IDs of the NAT address pools and names of the global static address pools to be bound to the NAT address pools on the master and backup devices |
| 13 | Information about a NAT traffic diversion policy |
| 14 | User-side route-policy |




#### Procedure

1. Configure IP addresses for device interfaces. For configuration details, see [Configuration Files](#EN-US_TASK_0279436213__li328531304214026).
2. Set the number of sessions supported by the service boards in slot 1 to 6M on master and backup devices.
   
   
   
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
   [~CGN1-license] active nat session-table size 6 slot 1 0
   ```
   ```
   [*CGN1-license] active nat session-table size 6 slot 1 
   ```
   ```
   [*CGN1-license] active nat bandwidth-enhance 100 slot 1
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
   [*CGN2-license] active nat session-table size 6 slot 1 
   ```
   ```
   [*CGN2-license] active nat bandwidth-enhance 100 slot 1
   ```
   ```
   [*CGN2-license] commit
   ```
   ```
   [~CGN2-license] quit
   ```
3. Enable HA hot backup on the master and backup devices.
   
   
   
   # Configure CGN1.
   
   
   
   ```
   [~CGN1] service-ha hot-backup enable
   ```
   ```
   [*CGN1] commit
   ```
   
   
   
   # Configure CGN2.
   
   
   
   ```
   [~CGN2] service-ha hot-backup enable
   ```
   ```
   [*CGN2] commit
   ```
4. Create and configure VRRP groups on the master and backup devices.
   
   
   
   # On CGN1, enter the view of GE 0/2/1.1, create VRRP group 1, and set the virtual IP address of the VRRP group to 10.1.1.3. Configure the VRRP group as an mVRRP group, set CGN1's priority in the VRRP group to 200, and set the VRRP preemption delay to 1500s.
   
   ```
   [~CGN1] interface GigabitEthernet 0/2/1.1
   ```
   ```
   [~CGN1-GigabitEthernet0/2/1.1] vlan-type dot1q 2001
   ```
   ```
   [*CGN1-GigabitEthernet0/2/1.1] ip address 10.1.1.1 255.255.255.0
   ```
   ```
   [*CGN1-GigabitEthernet0/2/1.1] vrrp vrid 1 virtual-ip 10.1.1.3
   ```
   ```
   [*CGN1-GigabitEthernet0/2/1.1] admin-vrrp vrid 1 ignore-if-down
   ```
   ```
   [*CGN1-GigabitEthernet0/2/1.1] vrrp vrid 1 priority 200
   ```
   ```
   [*CGN1-GigabitEthernet0/2/1.1] vrrp vrid 1 preempt-mode timer delay 1500
   ```
   ```
   [*CGN1-GigabitEthernet0/2/1.1] vrrp recover-delay 20
   ```
   ```
   [*CGN1-GigabitEthernet0/2/1.1] commit
   ```
   ```
   [~CGN1-GigabitEthernet0/2/1.1] quit
   ```
   
   # On CGN1, enter the view of GE 0/2/1.2, create VRRP group 2, and set the virtual IP address of the VRRP group to 10.1.2.3. Configure the VRRP group as an mVRRP group, set CGN1's priority in the VRRP group to 200, and set the VRRP preemption delay to 1500s.
   
   ```
   [~CGN1] interface GigabitEthernet 0/2/1.2
   ```
   ```
   [~CGN1-GigabitEthernet0/2/1.2] vlan-type dot1q 2002
   ```
   ```
   [*CGN1-GigabitEthernet0/2/1.2] ip address 10.1.2.1 255.255.255.0
   ```
   ```
   [*CGN1-GigabitEthernet0/2/1.2] vrrp vrid 2 virtual-ip 10.1.2.3
   ```
   ```
   [*CGN1-GigabitEthernet0/2/1.2] admin-vrrp vrid 2 ignore-if-down
   ```
   ```
   [*CGN1-GigabitEthernet0/2/1.2] vrrp vrid 2 priority 200
   ```
   ```
   [*CGN1-GigabitEthernet0/2/1.2] vrrp vrid 2 preempt-mode timer delay 1500
   ```
   ```
   [*CGN1-GigabitEthernet0/2/1.2] vrrp recover-delay 20
   ```
   ```
   [*CGN1-GigabitEthernet0/2/1.2] commit
   ```
   ```
   [~CGN1-GigabitEthernet0/2/1.2] quit
   ```
   
   # On CGN2, enter the view of GE 0/2/1.1, create VRRP group 1, and set the virtual IP address of the VRRP group to 10.1.1.3. In addition, configure the VRRP group as an mVRRP group and set CGN2's priority in the VRRP group to 150.
   
   ```
   [~CGN2] interface GigabitEthernet 0/2/1.1
   ```
   ```
   [~CGN2-GigabitEthernet0/2/1.1] vlan-type dot1q 2001
   ```
   ```
   [*CGN2-GigabitEthernet0/2/1.1] ip address 10.1.1.2 255.255.255.0
   ```
   ```
   [*CGN2-GigabitEthernet0/2/1.1] vrrp vrid 1 virtual-ip 10.1.1.3
   ```
   ```
   [*CGN2-GigabitEthernet0/2/1.1] admin-vrrp vrid 1 ignore-if-down
   ```
   ```
   [*CGN2-GigabitEthernet0/2/1.1] vrrp vrid 1 priority 150
   ```
   ```
   [*CGN2-GigabitEthernet0/2/1.1] commit
   ```
   ```
   [~CGN2-GigabitEthernet0/2/1.1] quit
   ```
   
   # On CGN2, enter the view of GE 0/2/1.2, create VRRP group 2, and set the virtual IP address of the VRRP group to 10.1.2.3. In addition, configure the VRRP group as an mVRRP group and set CGN2's priority in the VRRP group to 150.
   
   ```
   [~CGN2] interface GigabitEthernet 0/2/1.2
   ```
   ```
   [~CGN2-GigabitEthernet0/2/1.2] vlan-type dot1q 2002
   ```
   ```
   [*CGN2-GigabitEthernet0/2/1.2] ip address 10.1.2.2 255.255.255.0
   ```
   ```
   [*CGN2-GigabitEthernet0/2/1.2] vrrp vrid 2 virtual-ip 10.1.2.3
   ```
   ```
   [*CGN2-GigabitEthernet0/2/1.2] admin-vrrp vrid 2 ignore-if-down
   ```
   ```
   [*CGN2-GigabitEthernet0/2/1.2] vrrp vrid 2 priority 150
   ```
   ```
   [*CGN2-GigabitEthernet0/2/1.2] commit
   ```
   ```
   [~CGN2-GigabitEthernet0/2/1.2] quit
   ```
5. On the master and backup devices, create a service-location group, configure members for HA dual-device inter-chassis backup, and configure a VRRP channel. Ensure that the direct link between the master and back devices is not interrupted. Otherwise, the backup channel cannot be established.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Service-location IDs and the number of service-location groups configured on the master and backup devices must be the same. Otherwise, backup may fail, affecting services.
   
   
   
   # On CGN1, create service-location group 1, add CPU 0 in slot 1 as an HA dual-device inter-chassis backup member, and set the local VRRP outbound interface is GE 0/2/1.1 and peer IP address is 10.1.1.2.
   
   ```
   [~CGN1] service-location 1
   ```
   ```
   [*CGN1-service-location-1] location slot 1 
   ```
   ```
   [*CGN1-service-location-1] remote-backup interface GigabitEthernet0/2/1.1 peer 10.1.1.2
   ```
   ```
   [*CGN1-service-location-1] commit
   ```
   ```
   [~CGN1-service-location-1] quit
   ```
   
   # On CGN1, create service-location group 2, add CPU 1 in slot 1 as an HA dual-device inter-chassis backup member, and set the local VRRP outbound interface is GE 0/2/1.2 and peer IP address is 10.1.2.2.
   
   ```
   [~CGN1] service-location 2
   ```
   ```
   [*CGN1-service-location-2] location slot 1 
   ```
   ```
   [*CGN1-service-location-2] remote-backup interface GigabitEthernet0/2/1.2 peer 10.1.2.2
   ```
   ```
   [*CGN1-service-location-2] commit
   ```
   ```
   [~CGN1-service-location-2] quit
   ```
   
   # On CGN2, create service-location group 1, add CPU 0 in slot 1 as an HA dual-device inter-chassis backup member, and set the local VRRP outbound interface is GE 0/2/1.1 and peer IP address is 10.1.1.1.
   
   ```
   [~CGN2] service-location 1
   ```
   ```
   [*CGN2-service-location-1] location slot 1 
   ```
   ```
   [*CGN2-service-location-1] remote-backup interface GigabitEthernet0/2/1.1 peer 10.1.1.1
   ```
   ```
   [*CGN2-service-location-1] commit
   ```
   ```
   [~CGN2-service-location-1] quit
   ```
   
   # On CGN2, create service-location group 2, add CPU 1 in slot 1 as an HA dual-device inter-chassis backup member, and set the local VRRP outbound interface is GE 0/2/1.2 and peer IP address is 10.1.2.1.
   
   ```
   [~CGN2] service-location 2
   ```
   ```
   [*CGN2-service-location-2] location slot 1 
   ```
   ```
   [*CGN2-service-location-2] remote-backup interface GigabitEthernet0/2/1.2 peer 10.1.2.1
   ```
   ```
   [*CGN2-service-location-2] commit
   ```
   ```
   [~CGN2-service-location-2] quit
   ```
6. Associate HA with the VRRP groups on CGN1.
   
   
   
   # Enter the GE 0/2/1.1 interface view and associate HA with VRRP group 1.
   
   ```
   [~CGN1] interface GigabitEthernet 0/2/1.1
   ```
   ```
   [~CGN1-GigabitEthernet0/2/1.1] vrrp vrid 1 track service-location 1 reduced 60
   ```
   ```
   [*CGN1-GigabitEthernet0/2/1.1] vrrp vrid 1 track interface GigabitEthernet 0/2/2 reduced 60
   ```
   ```
   [*CGN1-GigabitEthernet0/2/1.1] vrrp vrid 1 track interface GigabitEthernet 0/2/3 reduced 60
   ```
   ```
   [*CGN1-GigabitEthernet0/2/1.1] commit
   ```
   ```
   [~CGN1-GigabitEthernet0/2/1.1] quit
   ```
   
   # Enter the GE 0/2/1.2 interface view and associate HA with VRRP group 2.
   
   ```
   [~CGN1] interface GigabitEthernet 0/2/1.2
   ```
   ```
   [~CGN1-GigabitEthernet0/2/1.2] vrrp vrid 2 track service-location 2 reduced 60
   ```
   ```
   [*CGN1-GigabitEthernet0/2/1.2] vrrp vrid 2 track interface GigabitEthernet 0/2/2 reduced 60
   ```
   ```
   [*CGN1-GigabitEthernet0/2/1.2] vrrp vrid 2 track interface GigabitEthernet 0/2/3 reduced 60
   ```
   ```
   [*CGN1-GigabitEthernet0/2/1.2] commit
   ```
   ```
   [~CGN1-GigabitEthernet0/2/1.2] quit
   ```
   
   # Run the [**display vrrp 1**](cmdqueryname=display+vrrp+1) and [**display vrrp 2**](cmdqueryname=display+vrrp+2) commands on both CGN1 and CGN2 to check the VRRP master/backup state. This state reflects the master/backup state of the service-location groups on the CGN devices.
   
   ```
   [~CGN1] display vrrp 1
   GigabitEthernet 0/2/1.1 | Virtual Router 1                                                                                     
       State                  : Master 
       Virtual IP                : 10.1.1.3  
       Master IP                 : 10.1.1.1
       Local IP                  : 10.1.1.1
       PriorityRun               : 200     
       PriorityConfig            : 200    
       MasterPriority            : 200     
       Preempt                   : YES     Delay Time            : 400 s  
       Hold Multiplier           : 3                                                                   
       TimerRun                  : 1 s 
       TimerConfig               : 1 s     
       Auth Type                 : NONE    
       Virtual MAC               : 00e0-fc12-3456   
       Check TTL                 : YES        
       Config Type               : admin-vrrp    
       Backup-forward            : disabled     
       Fast-resume               : disabled                                                               
       Create Time               : 2011-10-18 11:14:48 UTC+10:59     
       Last Change Time          : 2011-10-18 14:02:46 UTC+10:59
   [~CGN1] display vrrp 2
   GigabitEthernet 0/2/1.2 | Virtual Router 1                                                                                     
       State                  : Master 
       Virtual IP                : 10.1.2.3  
       Master IP                 : 10.1.2.1
       Local IP                  : 10.1.2.1
       PriorityRun               : 200     
       PriorityConfig            : 200    
       MasterPriority            : 200     
       Preempt                   : YES     Delay Time        : 400 s  
       Hold Multiplier           : 3                                                                     
       TimerRun                  : 1 s 
       TimerConfig               : 1 s     
       Auth Type                 : NONE    
       Virtual MAC               : 00e0-fc12-3456   
       Check TTL                 : YES        
       Config Type               : admin-vrrp    
       Backup-forward            : disabled     
       Fast-resume               : disabled                                                         
       Create Time               : 2011-10-18 11:14:48 UTC+10:59     
       Last Change Time          : 2011-10-18 14:02:46 UTC+10:59
   ```
   ```
   [~CGN2] display vrrp 1
   GigabitEthernet 0/2/1.1 | Virtual Router 1                                                                                     
       State                  : Backup
       Virtual IP                : 10.1.1.3  
       Master IP                 : 10.1.1.1
       Local IP                  : 10.1.1.2
       PriorityRun               : 150     
       PriorityConfig            : 150    
       MasterPriority            : 200     
       Preempt                   : YES     Delay Time                : 0 s
       Hold Multiplier           : 3                                                                          
       TimerRun                  : 1 s 
       TimerConfig               : 1 s     
       Auth Type                 : NONE    
       Virtual MAC               : 00e0-fc12-3456   
       Check TTL                 : YES        
       Config Type               : admin-vrrp    
       Backup-forward            : disabled     
       Fast-resume               : disabled                                                                
       Create Time               : 2011-10-18 11:14:48 UTC+10:59     
       Last Change Time          : 2011-10-18 14:02:46 UTC+10:59
   [~CGN2] display vrrp 2
   GigabitEthernet 0/2/1.2 | Virtual Router 1                                                                                     
       State                  : Backup
       Virtual IP                : 10.1.2.3  
       Master IP                 : 10.1.2.1
       Local IP                  : 10.1.2.2
       PriorityRun               : 150     
       PriorityConfig            : 150    
       MasterPriority            : 200     
       Preempt                   : YES     Delay Time                : 0 s  
       Hold Multiplier           : 3                                                              
       TimerRun                  : 1 s 
       TimerConfig               : 1 s     
       Auth Type                 : NONE    
       Virtual MAC               : 00e0-fc12-3456   
       Check TTL                 : YES        
       Config Type               : admin-vrrp    
       Backup-forward            : disabled     
       Fast-resume               : disabled                                                                 
       Create Time               : 2011-10-18 11:14:48 UTC+10:59     
       Last Change Time          : 2011-10-18 14:02:46 UTC+10:59
   ```
7. Bind the service-location group to the VRRP group on each CGN device.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Corresponding one service-location group to one VRRP group is recommended.
   
   # Bind service-location group 1 to VRRP group 1 on CGN1.
   
   ```
   [~CGN1] service-location 1
   ```
   ```
   [*CGN1-service-location-1] vrrp vrid 1 interface GigabitEthernet 0/2/1.1
   ```
   ```
   [*CGN1-service-location-1] commit
   ```
   ```
   [~CGN1-service-location-1] quit
   ```
   
   # Bind service-location group 2 to VRRP group 2 on CGN1.
   
   ```
   [~CGN1] service-location 2
   ```
   ```
   [*CGN1-service-location-2] vrrp vrid 2 interface GigabitEthernet 0/2/1.2
   ```
   ```
   [*CGN1-service-location-2] commit
   ```
   ```
   [~CGN1-service-location-2] quit
   ```
   
   # Bind service-location group 1 to VRRP group 1 on CGN2.
   
   ```
   [~CGN2] service-location 1
   ```
   ```
   [*CGN2-service-location-1] vrrp vrid 1 interface GigabitEthernet 0/2/1.1
   ```
   ```
   [*CGN2-service-location-1] commit
   ```
   ```
   [~CGN2-service-location-1] quit
   ```
   
   # Bind service-location group 2 to VRRP group 2 on CGN2.
   
   ```
   [~CGN2] service-location 2
   ```
   ```
   [*CGN2-service-location-2] vrrp vrid 2 interface GigabitEthernet 0/2/1.2
   ```
   ```
   [*CGN2-service-location-2] commit
   ```
   ```
   [~CGN2-service-location-2] quit
   ```
8. Create a service-instance group on each of the master and backup devices and bind the service-instance group to the service-location group. (You must bind a service-instance group to an RBS. Otherwise, traffic is transmitted over the backup channel during a master/backup device switchover, affecting services.)
   
   # Configure CGN1.
   1. Configure an RBS named **rbs**.
      
      ```
      [~CGN1] remote-backup-service rbs
      ```
      ```
      [*CGN1-rm-backup-srv-rbs] peer 10.1.1.2 source 10.1.1.1 port 7000
      ```
      ```
      [*CGN1-rm-backup-srv-rbs] commit
      ```
      ```
      [~CGN1-rm-backup-srv-rbs] quit
      ```
   2. Create a service-instance group named **group1**, and bind it to service-location groups 1 and 2, and to RBS **rbs**.
      
      ```
      [~CGN1] service-instance-group group1
      ```
      ```
      [*CGN1-service-instance-group-group1] service-location 1
      ```
      ```
      [*CGN1-service-instance-group-group1] service-location 2
      ```
      ```
      [*CGN1-service-instance-group-group1] remote-backup-service rbs
      ```
      ```
      [*CGN1-service-instance-group-group1] commit
      ```
      ```
      [~CGN1-service-instance-group-group1] quit
      ```
   # Configure CGN2.
   1. Configure an RBS named **rbs**.
      
      ```
      [~CGN2] remote-backup-service rbs
      ```
      ```
      [*CGN2-rm-backup-srv-rbs] peer 10.1.1.1 source 10.1.1.2 port 7000
      ```
      ```
      [*CGN2-rm-backup-srv-rbs] commit
      ```
      ```
      [~CGN2-rm-backup-srv-rbs] quit
      ```
   2. Create a service-instance group named **group1**, and bind it to service-location groups 1 and 2, and to RBS **rbs**.
      
      ```
      [~CGN2] service-instance-group group1
      ```
      ```
      [*CGN2-service-instance-group-group1] service-location 1
      ```
      ```
      [*CGN2-service-instance-group-group1] service-location 2
      ```
      ```
      [*CGN2-service-instance-group-group1] remote-backup-service rbs
      ```
      ```
      [*CGN2-service-instance-group-group1] commit
      ```
      ```
      [~CGN2-service-instance-group-group1] quit
      ```
   
   # Run the [**display service-location**](cmdqueryname=display+service-location) command on the two CGN devices to check HA information. In the command output, **Vrrp state** must be consistent with the HA state, and **Batch-backup state** indicates whether batch backup is completed.
   
   ```
   [~CGN1] display service-location 1
   service-location 1                                                                                             
    Backup scene type: inter-box                                                                                     
    Location slot ID: 1                                                                                 
    Remote-backup interface: GigabitEthernet0/2/1.1                                                                   
    Peer: 10.1.1.2                                                                                           
    Vrrp ID: 1                                                                                       
    Vrrp bind interface: GigabitEthernet0/2/1.1                                                                    
    Vrrp state: master                                                                                            
    Bound service-instance-group number: 1                                                                          
    Batch-backup state: finished
   ```
   ```
   [~CGN1] display service-location 2
   service-location 2                                                                                              
    Backup scene type: inter-box                                                                                          
    Location slot ID: 1                                                                                        
    Remote-backup interface: GigabitEthernet0/2/1.2                                                                              
    Peer: 10.1.2.2                                                                                                    
    Vrrp ID: 2                                                                                                           
    Vrrp bind interface: GigabitEthernet0/2/1.2                                                                                 
    Vrrp state: master                                                                                            
    Bound service-instance-group number: 1                                                                              
    Batch-backup state: finished
   ```
   ```
   [~CGN2] display service-location 1
   service-location 1                                                                                               
    Backup scene type: inter-box 
    Location slot ID: 1                                                                                       
    Remote-backup interface: GigabitEthernet0/2/1.1                                                                        
    Peer: 10.1.1.1                                                                                                   
    Vrrp ID: 1                                                                                                        
    Vrrp bind interface: GigabitEthernet0/2/1.1                                                                              
    Vrrp state: slave                                                                                               
    Bound service-instance-group number: 1                                                                              
    Batch-backup state: NA
   ```
   ```
   [~CGN2] display service-location 2
   service-location 2                                                                                               
    Backup scene type: inter-box                                                                                          
    Location slot ID: 1                                                                                        
    Remote-backup interface: GigabitEthernet0/2/1.2                                                                              
    Peer: 10.1.2.1                                                                                                     
    Vrrp ID: 2                                                                                                    
    Vrrp bind interface: GigabitEthernet0/2/1.2                                                                          
    Vrrp state: slave                                                                                               
    Bound service-instance-group number: 1                                                                                  
    Batch-backup state: NA
   ```
9. Configure NAT instances.
   
   
   
   # Configure CGN1.
   
   Configure a CGN global static address pool as the master address pool.
   
   ```
   [~CGN1] nat ip-pool pool1
   ```
   ```
   [*CGN1-nat-ip-pool-pool1] section 0 11.11.11.1 mask 24
   ```
   ```
   [*CGN1-nat-ip-pool-pool1] nat-instance subnet length initial 25 extend 27
   ```
   ```
   [*CGN1-nat-ip-pool-pool1] commit
   ```
   ```
   [~CGN1-nat-ip-pool-pool1] quit
   ```
   
   Bind the NAT instance to the address pool.
   
   ```
   [~CGN1] nat instance nat id 1
   ```
   ```
   [*CGN1-nat-instance-nat] nat address-group group1 group-id 1 bind-ip-pool pool1
   ```
   ```
   [*CGN1-nat-instance-nat] commit
   ```
   ```
   [~CGN1-nat-instance-nat] quit
   ```
   
   # Configure CGN2.
   
   Configure a CGN global static address pool. (You must configure the **slave** parameter. Otherwise, services will be affected.)
   
   ```
   [~CGN2] nat ip-pool pool1 slave
   ```
   ```
   [*CGN2-nat-ip-pool-pool1] section 0 11.11.11.1 mask 24
   ```
   ```
   [*CGN2-nat-ip-pool-pool1] nat-instance subnet length initial 25 extend 27
   ```
   ```
   [*CGN2-nat-ip-pool-pool1] commit
   ```
   ```
   [~CGN2-nat-ip-pool-pool1] quit
   ```
   
   Bind the NAT instance to the address pool.
   
   ```
   [~CGN2] nat instance nat id 1
   ```
   ```
   [*CGN2-nat-instance-nat] nat address-group group1 group-id 1 bind-ip-pool pool1
   ```
   ```
   [*CGN2-nat-instance-nat] commit
   ```
   ```
   [~CGN2-nat-instance-nat] quit
   ```
10. Bind the NAT instance to the service-instance group on the master and backup devices.
    
    
    
    # On CGN1, bind the NAT instance named **nat** to the service-instance group named **group1**.
    
    ```
    [~CGN1] nat instance nat id 1
    ```
    ```
    [*CGN1-nat-instance-nat] port-range 4096
    ```
    ```
    [*CGN1-nat-instance-nat] service-instance-group group1
    ```
    ```
    [*CGN1-nat-instance-nat] commit
    ```
    ```
    [~CGN1-nat-instance-nat] quit
    ```
    
    # On CGN2, bind the NAT instance named **nat** to the service-instance group named **group1**.
    
    ```
    [~CGN2] nat instance nat id 1
    ```
    ```
    [*CGN1-nat-instance-nat] port-range 4096
    ```
    ```
    [*CGN2-nat-instance-nat] service-instance-group group1
    ```
    ```
    [*CGN2-nat-instance-nat] commit
    ```
    ```
    [~CGN2-nat-instance-nat] quit
    ```
11. Configure a traffic classification rule, a traffic behavior, and a NAT traffic diversion policy on the master and backup devices, and apply the NAT traffic diversion policy.
    
    # On CGN1, configure a NAT traffic diversion policy and a NAT conversion policy.
    1. Configure an ACL traffic classification rule.
       
       ```
       [~CGN1] acl 3001
       ```
       ```
       [*CGN1-acl4-advance-3001] rule 1 permit ip source 10.0.0.0 0.0.0.255
       ```
       ```
       [*CGN1-acl4-advance-3001] commit
       ```
       ```
       [~CGN1-acl4-advance-3001] quit
       ```
    2. Configure a traffic classifier.
       
       ```
       [*CGN1] traffic classifier classifier1
       ```
       ```
       [*CGN1-classifier-c1] if-match acl 3001
       ```
       ```
       [*CGN1-classifier-c1] commit
       ```
       ```
       [~CGN1-classifier-c1] quit
       ```
    3. Define a traffic behavior, in which the action is configured as binding NAT instance **nat**.
       
       ```
       [~CGN1] traffic behavior behavior1
       ```
       ```
       [*CGN1-behavior-b1] nat bind instance nat
       ```
       ```
       [*CGN1-behavior-b1] commit
       ```
       ```
       [~CGN1-behavior-b1] quit
       ```
    4. Define a NAT traffic diversion policy to associate the traffic classifier with the traffic behavior.
       
       ```
       [~CGN1] traffic policy policy1
       ```
       ```
       [*CGN1-trafficpolicy-p1] classifier classifier1 behavior behavior1
       ```
       ```
       [*CGN1-trafficpolicy-p1] commit
       ```
       ```
       [~CGN1-trafficpolicy-p1] quit
       ```
    5. Apply the NAT traffic diversion policy in the GE 0/2/2 interface view. In VS mode, the [**traffic-policy**](cmdqueryname=traffic-policy) command is supported only by the admin VS.
       
       ```
       [~CGN1] interface GigabitEthernet 0/2/2
       ```
       ```
       [*CGN1-GigabitEthernet0/2/2] ip address 10.1.6.1 24
       ```
       ```
       [*CGN1-GigabitEthernet0/2/2] traffic-policy policy1 inbound
       ```
       ```
       [*CGN1-GigabitEthernet0/2/2] commit
       ```
       ```
       [~CGN1] quit
       ```
    6. Configure a NAT traffic conversion policy.
       
       ```
       [~CGN1] nat instance nat
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
    
    # The configuration of CGN2 is similar to the configuration of CGN1. For configuration details, see Configuration Files.
    
    
    
    # Run the [**display nat instance nat**](cmdqueryname=display+nat+instance+nat) command on the two CGN devices to check NAT configurations.
    
    ```
    [~CGN1] display nat instance nat
    nat instance nat id 1  
     port-range 4096                                                                                                   
     service-instance-group group1                                                                                             
     nat address-group group1 group-id 1 bind-ip-pool pool1                                                     
     nat outbound any address-group1
    ```
    ```
    [~CGN2] display nat instance nat
    nat instance nat id 1 
     port-range 4096                                                                                                   
     service-instance-group group1                                                                                             
     nat address-group group1 group-id 1 bind-ip-pool pool1                                                     
     nat outbound any address-group1
    ```
12. Configure the master and backup devices to establish a BGP peer relationship with the user-side CE and import the default route advertised by the CR. Configure a local-preference-based route-policy on the user-side CE to allow the CE to preferentially select the default route from CGN1.
    
    
    
    # Configure CGN1.
    
    ```
    [~CGN1] bgp 200
    ```
    ```
    [*CGN1-bgp] peer 10.2.2.2 as-number 200
    ```
    ```
    [*CGN1-bgp] peer 10.2.2.2 connect-interface LoopBack0
    ```
    ```
    [*CGN1-bgp] ipv4-family unicast
    ```
    ```
    [*CGN1-bgp-af-ipv4] peer 10.2.2.2 default-route-advertise
    ```
    ```
    [*CGN1-bgp-af-ipv4] commit
    ```
    ```
    [~CGN1-bgp-af-ipv4] quit
    ```
    ```
    [~CGN1-bgp] import-route unr
    ```
    ```
    [*CGN1-bgp] commit
    ```
    ```
    [~CGN1-bgp] quit
    ```
    
    # Configure CGN2.
    
    ```
    [~CGN2] bgp 200
    ```
    ```
    [*CGN2-bgp] peer 10.2.2.2 as-number 200
    ```
    ```
    [*CGN2-bgp] peer 10.2.2.2 connect-interface LoopBack0
    ```
    ```
    [*CGN2-bgp] ipv4-family unicast
    ```
    ```
    [*CGN2-bgp-af-ipv4] peer 10.2.2.2 default-route-advertise
    ```
    ```
    [*CGN2-bgp-af-ipv4] commit
    ```
    ```
    [~CGN2-bgp-af-ipv4] quit
    ```
    ```
    [~CGN2-bgp] import-route unr
    ```
    ```
    [*CGN2-bgp] commit
    ```
    ```
    [~CGN2-bgp] quit
    ```
    
    # Configure the user-side CE.
    
    ```
    [~CE] route-policy local_pre permit node 10
    ```
    ```
    [*CE-route-policy] apply local-preference 200
    ```
    ```
    [*CE-route-policy] commit
    ```
    ```
    [~CE-route-policy] quit
    ```
    ```
    [~CE] bgp 200
    ```
    ```
    [*CE-bgp] peer 10.3.3.3 as-number 200
    ```
    ```
    [*CE-bgp] peer 10.3.3.3 connect-interface LoopBack0
    ```
    ```
    [*CE-bgp] peer 10.4.4.4 as-number 200
    ```
    ```
    [*CE-bgp] peer 10.4.4.4 connect-interface LoopBack0
    ```
    ```
    [*CE-bgp] ipv4-family unicast
    ```
    ```
    [*CE-bgp-af-ipv4] peer 10.3.3.3 route-policy local_pre import
    ```
    ```
    [*CE-bgp-af-ipv4] commit
    ```
    ```
    [~CE-bgp-af-ipv4] quit
    ```
    ```
    [~CE-bgp] import-route unr
    ```
    ```
    [*CE-bgp] commit
    ```
    ```
    [~CE-bgp] quit
    ```

#### Configuration Files

* CGN1 configuration file
  
  ```
  #
  sysname CGN1
  #
  vsm on-board-mode disable
  #
  service-ha hot-backup enable
  #
  service-location 1
   location slot 1 
   remote-backup interface GigabitEthernet 0/2/1.1 peer 10.1.1.2
   vrrp vrid 1 interface GigabitEthernet 0/2/1.1
  #
  service-location 2
   location slot 1 
   remote-backup interface GigabitEthernet 0/2/1.2 peer 10.1.2.2
   vrrp vrid 2 interface GigabitEthernet 0/2/1.2
  #
  service-instance-group group1
   service-location 1
   service-location 2
   remote-backup-service rbs
  #
  nat ip-pool pool1
   nat-instance subnet length initial 25 extend 27
   section 0 11.11.11.1 mask 24
  #
  nat instance nat id 1
   port-range 4096
   service-instance-group group1
   nat address-group group1 group-id 1 bind-ip-pool pool1
   nat outbound any address-group group1
  #
  remote-backup-service rbs
   peer 10.1.1.2 source 10.1.1.1 port 7000
  #
  acl number 3001
   rule 1 permit ip source 10.0.0.0 0.0.0.255
  #
  traffic classifier classifier1 operator or
   if-match acl 3001 precedence 1
  #
  traffic behavior behavior1
   nat bind instance nat
  #
  traffic policy policy1
   share-mode
   classifier classifier1 behavior behavior1 precedence 1
  #
  license
   active nat session-table size 6 slot 1 
   active nat session-table size 6 slot 1 
   active nat bandwidth-enhance 100 slot 1
  #
  interface GigabitEthernet0/2/1.1
   undo shutdown
   vlan-type dot1q 2001
   ip address 10.1.1.1 255.255.255.0
   vrrp vrid 1 virtual-ip 10.1.1.3
   admin-vrrp vrid 1 ignore-if-down
   vrrp vrid 1 priority 200
   vrrp vrid 1 track service-location 1 reduced 60
   vrrp vrid 1 track interface GigabitEthernet0/2/2 reduced 60
   vrrp vrid 1 track interface GigabitEthernet0/2/3 reduced 60
   vrrp vrid 1 preempt-mode timer delay 1500
   vrrp recover-delay 20
  #
  interface GigabitEthernet0/2/1.2
   undo shutdown
   vlan-type dot1q 2002
   ip address 10.1.2.1 255.255.255.0
   vrrp vrid 2 virtual-ip 10.1.2.3
   admin-vrrp vrid 2 ignore-if-down
   vrrp vrid 2 priority 200
   vrrp vrid 2 track service-location 2 reduced 60
   vrrp vrid 2 track interface GigabitEthernet0/2/2 reduced 60
   vrrp vrid 2 track interface GigabitEthernet0/2/3 reduced 60
   vrrp vrid 2 preempt-mode timer delay 1500
   vrrp recover-delay 20
  #
  interface GigabitEthernet0/2/2
   undo shutdown
   ip address 10.1.6.1 255.255.255.0
   traffic-policy policy1 inbound
  #
  interface GigabitEthernet0/2/3
   undo shutdown
   ip address 10.1.3.1 255.255.255.0
  #
  interface LoopBack0
   ip address 10.3.3.3 255.255.255.255
  #
  bgp 200
   peer 10.2.2.2 as-number 200
   peer 10.2.2.2 connect-interface Loopback0
   #
   ipv4-family unicast
    undo synchronization
    import-route unr
    peer 10.2.2.2 enable
    peer 10.2.2.2 default-route-advertise
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
  service-ha hot-backup enable
  #
  service-location 1
   location slot 1 
   remote-backup interface GigabitEthernet 0/2/1.1 peer 10.1.1.1
   vrrp vrid 1 interface GigabitEthernet 0/2/1.1
  #
  service-location 2
   location slot 1 
   remote-backup interface GigabitEthernet 0/2/1.2 peer 10.1.2.1
   vrrp vrid 2 interface GigabitEthernet 0/2/1.2
  #
  service-instance-group group1
   service-location 1
   service-location 2
   remote-backup-service rbs
  #
  nat ip-pool pool1 slave
   nat-instance subnet length initial 25 extend 27
   section 0 11.11.11.1 mask 24
  #
  nat instance nat id 1
   port-range 4096
   service-instance-group group1
   nat address-group group1 group-id 1 bind-ip-pool pool1
   nat outbound any address-group group1
  #
  remote-backup-service natbras
   peer 10.1.1.1 source 10.1.1.2 port 7000
  #
  acl number 3001
   rule 1 permit ip source 10.0.0.0 0.0.0.255
  #
  traffic classifier classifier1 operator or
   if-match acl 3001 precedence 1
  #
  traffic behavior behavior1
   nat bind instance nat
  #
  traffic policy policy1
   share-mode
   classifier classifier1 behavior behavior1 precedence 1
  #
  license
   active nat session-table size 6 slot 1 
   active nat session-table size 6 slot 1 
   active nat bandwidth-enhance 100 slot 1 
  #
  interface GigabitEthernet0/2/1.1
   undo shutdown
   vlan-type dot1q 2001
   ip address 10.1.1.2 255.255.255.0
   vrrp vrid 1 virtual-ip 10.1.1.3
   admin-vrrp vrid 1 ignore-if-down
   vrrp vrid 1 priority 150
   vrrp vrid 1 track service-location 1 reduced 60
   vrrp vrid 1 track interface GigabitEthernet0/2/2 reduced 60
   vrrp vrid 1 track interface GigabitEthernet0/2/3 reduced 60
  #
  interface GigabitEthernet0/2/1.2
   undo shutdown
   vlan-type dot1q 2002
   ip address 10.1.2.2 255.255.255.0
   vrrp vrid 2 virtual-ip 10.1.2.3
   admin-vrrp vrid 2 ignore-if-down
   vrrp vrid 2 priority 150
   vrrp vrid 2 track service-location 2 reduced 60
   vrrp vrid 2 track interface GigabitEthernet0/2/2 reduced 60
   vrrp vrid 2 track interface GigabitEthernet0/2/3 reduced 60
  #
  interface GigabitEthernet0/2/2
   undo shutdown
   ip address 10.1.4.1 255.255.255.0
   traffic-policy policy1 inbound
  #
  interface GigabitEthernet0/2/3
   undo shutdown
   ip address 10.1.5.1 255.255.255.0
  #
  interface LoopBack0
   ip address 10.4.4.4 255.255.255.255
  #
  bgp 200
   peer 10.2.2.2 as-number 200
   peer 10.2.2.2 connect-interface Loopback0
   #
   ipv4-family unicast
    undo synchronization
    import-route unr
    peer 10.2.2.2 enable
    peer 10.2.2.2 default-route-advertise
  #
  return
  ```
* CE configuration file
  ```
  #
  sysname CE
  #
  interface GigabitEthernet0/2/1
   undo shutdown
   ip address 10.11.11.2 255.255.255.0
  #
  interface GigabitEthernet0/2/2
   undo shutdown
   ip address 10.11.12.2 255.255.255.0
  #
  interface LoopBack0
   ip address 10.2.2.2 255.255.255.255
  #
  route-policy local_pre permit node 10
   apply local-preference 200
  #
  bgp 200
   peer 10.3.3.3 as-number 200
   peer 10.3.3.3 connect-interface Loopback0
   peer 10.4.4.4 as-number 200
   peer 10.4.4.4 connect-interface Loopback0
   #
   ipv4-family unicast
    undo synchronization
    import-route unr
    peer 10.3.3.3 enable
    peer 10.3.3.3 route-policy local_pre import
    peer 10.4.4.4 enable
  #
  return
  ```