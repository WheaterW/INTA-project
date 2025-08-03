Example for Configuring Distributed NAT Inter-Board Load Balancing+Inter-Chassis Hot Backup
===========================================================================================

This section provides an example for configuring distributed NAT inter-board load balancing+HA inter-chassis hot backup.

#### Networking Requirements

In distributed networking, NAT service boards are equipped in slot 1 of BRAS1 and slot 1 of BRAS2 and each of them provides two CPUs to balance NAT traffic. A VRRP channel is established between BRAS1 and BRAS2 through GE interfaces. CPU0 and CPU1 of the service board in slot 1 on BRAS1 work together with CPU0 and CPU1 of the service board in slot 1 on BRAS2 to implement inter-chassis hot backup. The NAT service's master/backup status is determined by VRRP, and the service board status is associated with VRRP.

**Figure 1** Inter-board load balancing+NAT inter-chassis hot backup![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/1 and GE 0/1/2, respectively.


  
![](figure/en-us_image_0270989509.png)

#### Context

The configuration roadmap is as follows:

1. Enable the license function for the NAT service boards on BRAS1 and BRAS2 and configure NAT session resources.
2. Create a NAT load balancing instance.
3. Configure HA hot backup, with NAT service information backed up between BRAS1 and BRAS2.
4. Create a service-location group, configure members for HA dual-device inter-chassis backup, and configure a VRRP channel between BRAS1 and BRAS2.
5. Create and configure a VRRP group.
6. Associate HA with VRRP.
7. Bind the service-location group to the VRRP group.
8. Create a service-instance group and an RBS, and bind the service-instance group to the service-location group.
9. Bind the NAT instance to the service-instance group.
10. Configure a user-side VRRP group on BRAS1 and BRAS2 that are connected to the switch.
11. Configure RUI to back up BRAS information.
12. Configure user information (user group, IP address pool, user domain, and AAA), configure RADIUS authentication on the BRAS, and bind the user group to the NAT instance.
13. Configure a user-side sub-interface.
14. Configure a NAT traffic diversion policy.

#### Data Preparation

To complete the configuration, you need the following data:

| No. | Data |
| --- | --- |
| 1 | Index of the service-location group |
| 2 | Slot ID and CPU ID of the active CPU on the service board on BRAS1 |
| 3 | Slot ID and CPU ID of the standby CPU on the service board on BRAS2 |
| 4 | Interfaces of the VRRP channel on the master and backup devices |
| 5 | IP addresses of VRRP interfaces on BRAS1 and BRAS2 |
| 6 | Index of a VRRP group |
| 7 | Virtual IP address of a VRRP group |
| 8 | Priorities of VRRP group members |
| 9 | VRRP preemption delay |
| 10 | Name of a service-instance group |
| 11 | Name and index of a NAT load balancing instance |
| 12 | IP address pool, IP address of the address pool gateway, and IP address segment of BRAS1 and BRAS2 |
| 13 | User group names, user domain names and AAA schemes on BRAS1 and BRAS2 |
| 14 | Remote backup identifiers for RUI backup of BRAS1 and BRAS2 |
| 15 | Names of user-side interfaces on BRAS1 and BRAS2 |
| 16 | IP addresses of user-side interfaces on BRAS1 and BRAS2 |
| 17 | Index of the user-side VRRP groups on BRAS1 and BRAS2 |
| 18 | Virtual IP address of the user-side VRRP groups on BRAS1 and BRAS2 |
| 19 | Priority of the user-side VRRP groups on BRAS1 and BRAS2 |
| 20 | Preemption delay of the user-side VRRP groups on BRAS1 and BRAS2 |
| 22 | ID of the NAT address pool and name of the global static address pool bound to the NAT address pool on BRAS1 and BRAS2 |
| 23 | Information about a NAT traffic diversion policy |




#### Procedure

1. Configure interface IP addresses and basic routes on each device to ensure reachability between the devices and the CR. For configuration details, see Configuration Files.
2. Enable the license function for the NAT service boards on BRAS1 and BRAS2 and configure NAT session resources.
   
   
   
   # Configure BRAS1.
   
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
   [*BRAS1-license] active nat session-table size 6 slot 1 
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
   
   # Configure BRAS2.
   
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
   [*BRAS2-license] active nat session-table size 6 slot 1 
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
3. Configure a distributed NAT instance for load balancing.
   
   
   
   # Configure BRAS1.
   
   1. Configure a CGN global static address pool (master address pool).
      
      ```
      [~BRAS1] nat ip-pool pool1
      ```
      ```
      [*BRAS1-nat-ip-pool-pool1] section 0 11.11.11.1 mask 24
      ```
      ```
      [*BRAS1-nat-ip-pool-pool1] nat-instance subnet length initial 25 extend 27
      ```
      ```
      [*BRAS1-nat-ip-pool-pool1] nat-instance ip used-threshold upper-limit 60 lower-limit 40
      ```
      ```
      [*BRAS1-nat-ip-pool-pool1] nat alarm ip threshold 60
      ```
      ```
      [*BRAS1-nat-ip-pool-pool1] commit
      ```
      ```
      [~BRAS1-nat-ip-pool-pool1] quit
      ```
   2. Bind the NAT instance to the global static address pool.
      
      # Bind the address pool named **address-group** in the NAT instance named **nat** to the global static address pool named **pool1**.
      
      ```
      [~BRAS1] nat instance nat id 1
      ```
      ```
      [~BRAS1-nat-instance-nat] nat address-group group1 group-id 1 bind-ip-pool pool1
      ```
      ```
      [*BRAS1-nat-instance-nat] commit
      ```
      ```
      [~BRAS1-nat-instance-nat] quit
      ```
   
   # Configure BRAS2.
   
   1. Configure a CGN global static address pool. (You must configure the **slave** parameter. Otherwise, services will be affected.)
      
      ```
      [~BRAS2] nat ip-pool pool1 slave
      ```
      ```
      [*BRAS2-nat-ip-pool-pool1] section 0 11.11.11.1 mask 24
      ```
      ```
      [*BRAS2-nat-ip-pool-pool1] nat-instance subnet length initial 25 extend 27
      ```
      ```
      [*BRAS2-nat-ip-pool-pool1] nat-instance ip used-threshold upper-limit 60 lower-limit 40
      ```
      ```
      [*BRAS2-nat-ip-pool-pool1] nat alarm ip threshold 60
      ```
      ```
      [*BRAS2-nat-ip-pool-pool1] commit
      ```
      ```
      [~BRAS2-nat-ip-pool-pool1] quit
      ```
   2. Bind the NAT instance to the global static address pool.
      
      # Bind the address pool named **address-group** in the NAT instance named **nat** to the global static address pool named **pool1**.
      
      ```
      [~BRAS1] nat instance nat id 1
      ```
      ```
      [*BRAS1-nat-instance-nat] nat address-group group1 group-id 1 bind-ip-pool pool1
      ```
      ```
      [*BRAS1-nat-instance-nat] commit
      ```
      ```
      [~BRAS1-nat-instance-nat] quit
      ```
4. Enable HA hot backup on the master and backup devices.
   
   
   
   # Configure BRAS1.
   
   ```
   [~BRAS1] service-ha hot-backup enable
   ```
   ```
   [*BRAS1] commit
   ```
   
   # Configure BRAS2.
   
   ```
   [~BRAS2] service-ha hot-backup enable
   ```
   ```
   [*BRAS2] commit
   ```
5. Configure a VRRP group on BRAS1 and BRAS2.
   
   
   
   # On BRAS1, enter the view of GE 0/1/1.1, create VRRP group 1, and set the virtual IP address of the VRRP group to 10.1.1.3. Configure the VRRP group as an mVRRP group, set BRAS1's priority in the VRRP group to 200, and set the VRRP preemption delay to 1500s.
   
   ```
   [~BRAS1] interface GigabitEthernet 0/1/1.1
   ```
   ```
   [~BRAS1-GigabitEthernet0/1/1.1] vlan-type dot1q 2001
   ```
   ```
   [*BRAS1-GigabitEthernet0/1/1.1] ip address 10.1.1.1 255.255.255.0
   ```
   ```
   [*BRAS1-GigabitEthernet0/1/1.1] vrrp vrid 1 virtual-ip 10.1.1.3
   ```
   ```
   [*BRAS1-GigabitEthernet0/1/1.1] admin-vrrp vrid 1 ignore-if-down
   ```
   ```
   [*BRAS1-GigabitEthernet0/1/1.1] vrrp vrid 1 priority 200
   ```
   ```
   [*BRAS1-GigabitEthernet0/1/1.1] vrrp vrid 1 preempt-mode timer delay 1500
   ```
   ```
   [*BRAS1-GigabitEthernet0/1/1.1] vrrp recover-delay 20
   ```
   ```
   [*BRAS1-GigabitEthernet0/1/1.1] commit
   ```
   ```
   [~BRAS1-GigabitEthernet0/1/1.1] quit
   ```
   
   # On BRAS1, enter the view of GE 0/1/1.2, create VRRP group 2, and set the virtual IP address of the VRRP group to 10.1.2.3. Configure the VRRP group as an mVRRP group, set BRAS1's priority in the VRRP group to 200, and set the VRRP preemption delay to 1500s.
   
   ```
   [~BRAS1] interface GigabitEthernet 0/1/1.2
   ```
   ```
   [~BRAS1-GigabitEthernet0/1/1.2] vlan-type dot1q 2002
   ```
   ```
   [*BRAS1-GigabitEthernet0/1/1.2] ip address 10.1.2.1 255.255.255.0
   ```
   ```
   [*BRAS1-GigabitEthernet0/1/1.2] vrrp vrid 2 virtual-ip 10.1.2.3
   ```
   ```
   [*BRAS1-GigabitEthernet0/1/1.2] admin-vrrp vrid 2 ignore-if-down
   ```
   ```
   [*BRAS1-GigabitEthernet0/1/1.2] vrrp vrid 2 priority 200
   ```
   ```
   [*BRAS1-GigabitEthernet0/1/1.2] vrrp vrid 2 preempt-mode timer delay 1500
   ```
   ```
   [*BRAS1-GigabitEthernet0/1/1.2] vrrp recover-delay 20
   ```
   ```
   [*BRAS1-GigabitEthernet0/1/1.2] commit
   ```
   ```
   [~BRAS1-GigabitEthernet0/1/1.2] quit
   ```
   
   # On BRAS2, enter the view of GE 0/1/1.1, create VRRP group 1, and set the virtual IP address of the VRRP group to 10.1.1.3. Configure the VRRP group as an mVRRP group, and set BRAS2's priority in the VRRP group to 150.
   
   ```
   [~BRAS2] interface GigabitEthernet 0/1/1.1
   ```
   ```
   [~BRAS2-GigabitEthernet0/1/1.1] vlan-type dot1q 2001
   ```
   ```
   [*BRAS2-GigabitEthernet0/1/1.1] ip address 10.1.1.2 255.255.255.0
   ```
   ```
   [*BRAS2-GigabitEthernet0/1/1.1] vrrp vrid 1 virtual-ip 10.1.1.3
   ```
   ```
   [*BRAS2-GigabitEthernet0/1/1.1] admin-vrrp vrid 1 ignore-if-down
   ```
   ```
   [*BRAS2-GigabitEthernet0/1/1.1] vrrp vrid 1 priority 150
   ```
   ```
   [*BRAS2-GigabitEthernet0/1/1.1] commit
   ```
   ```
   [~BRAS2-GigabitEthernet0/1/1.1] quit
   ```
   
   # On BRAS2, enter the view of GE 0/1/1.2, create VRRP group 2, and set the virtual IP address of the VRRP group to 10.1.2.3. Configure the VRRP group as an mVRRP group, and set BRAS2's priority in the VRRP group to 150.
   
   ```
   [~BRAS2] interface GigabitEthernet 0/1/1.2
   ```
   ```
   [~BRAS2-GigabitEthernet0/1/1.2] vlan-type dot1q 2002
   ```
   ```
   [~BRAS2-GigabitEthernet0/1/1.2] ip address 10.1.2.2 255.255.255.0
   ```
   ```
   [*BRAS2-GigabitEthernet0/1/1.2] vrrp vrid 2 virtual-ip 10.1.2.3
   ```
   ```
   [*BRAS2-GigabitEthernet0/1/1.2] admin-vrrp vrid 2 ignore-if-down
   ```
   ```
   [*BRAS2-GigabitEthernet0/1/1.2] vrrp vrid 2 priority 150
   ```
   ```
   [*BRAS2-GigabitEthernet0/1/1.2] commit
   ```
   ```
   [~BRAS2-GigabitEthernet0/1/1.2] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   It is recommended that a service-location group be mapped to a single VRRP group.
6. On the master and backup devices, create a service-location group, configure members for HA dual-device inter-chassis backup, and configure a VRRP channel. Ensure that the direct link between the master and back devices is not interrupted. Otherwise, the backup channel cannot be established.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Service-location IDs and the number of service-location groups configured on the master and backup devices must be the same. Otherwise, backup may fail, affecting services.
   
   
   
   # Create service-location group 1 on BRAS1, add CPU 0 in slot 1 as an HA dual-device inter-chassis backup member, and set the local VRRP outbound interface to GE 0/1/1.1 and the peer IP address to 10.1.1.2.
   
   ```
   [~BRAS1] service-location 1
   ```
   ```
   [*BRAS1-service-location-1] location slot 1 
   ```
   ```
   [*BRAS1-service-location-1] remote-backup interface GigabitEthernet0/1/1.1 peer 10.1.1.2
   ```
   ```
   [*BRAS1-service-location-1] commit
   ```
   ```
   [~BRAS1-service-location-1] quit
   ```
   
   # Create service-location group 2 on BRAS1, add CPU 1 in slot 1 as an HA dual-device inter-chassis backup member, and set the local VRRP outbound interface to GE 0/1/1.2 and the peer IP address to 10.1.2.2.
   
   ```
   [~BRAS1] service-location 2
   ```
   ```
   [*BRAS1-service-location-2] location slot 1 
   ```
   ```
   [*BRAS1-service-location-2] remote-backup interface GigabitEthernet 0/1/1.2 peer 10.1.2.2
   ```
   ```
   [*BRAS1-service-location-2] commit
   ```
   ```
   [~BRAS1-service-location-2] quit
   ```
   
   # Create service-location group 1 on BRAS2, add CPU 0 in slot 1 as an HA dual-device inter-chassis backup member, and set the local VRRP outbound interface to GE 0/1/1.1 and the peer IP address to 10.1.1.1.
   
   ```
   [~BRAS2] service-location 1
   ```
   ```
   [*BRAS2-service-location-1] location slot 1 
   ```
   ```
   [*BRAS2-service-location-1] remote-backup interface GigabitEthernet0/1/1.1 peer 10.1.1.1
   ```
   ```
   [*BRAS2-service-location-1] commit
   ```
   ```
   [~BRAS2-service-location-1] quit
   ```
   
   # Create service-location group 2 on BRAS2, add CPU 1 in slot 1 as an HA dual-device inter-chassis backup member, and set the local VRRP outbound interface to GE 0/1/1.2 and the peer IP address to 10.1.2.1.
   
   ```
   [~BRAS2] service-location 2
   ```
   ```
   [*BRAS2-service-location-2] location slot 1 
   ```
   ```
   [*BRAS2-service-location-2] remote-backup interface GigabitEthernet0/1/1.2 peer 10.1.2.1
   ```
   ```
   [*BRAS2-service-location-2] commit
   ```
   ```
   [~BRAS2-service-location-2] quit
   ```
7. Bind the service-location group to the VRRP group on BRAS1 and BRAS2.
   
   
   
   # On BRAS1, enter the view of GE 0/1/1.1, and associate service-location group 1 with VRRP group 1.
   
   ```
   [~BRAS1] interface GigabitEthernet 0/1/1.1
   ```
   ```
   [~BRAS1-GigabitEthernet0/1/1.1] vrrp vrid 1 track service-location 1 reduced 60
   ```
   ```
   [*BRAS1-GigabitEthernet0/1/1.1] commit
   ```
   ```
   [~BRAS1-GigabitEthernet0/1/1.1] quit
   ```
   
   # On BRAS1, enter the view of GE 0/1/1.2, and associate service-location group 2 with VRRP group 2.
   
   ```
   [~BRAS1] interface GigabitEthernet 0/1/1.2
   ```
   ```
   [~BRAS1-GigabitEthernet0/1/1.2] vrrp vrid 2 track service-location 2 reduced 60
   ```
   ```
   [*BRAS1-GigabitEthernet0/1/1.2] commit
   ```
   ```
   [~BRAS1-GigabitEthernet0/1/1.2] quit
   ```
   
   # On BRAS2, enter the view of GE 0/1/1.1, and associate service-location group 1 with VRRP group 1.
   
   ```
   [~BRAS2] interface GigabitEthernet 0/1/1.1
   ```
   ```
   [~BRAS2-GigabitEthernet0/1/1.1] vrrp vrid 1 track service-location 1 reduced 60
   ```
   ```
   [*BRAS2-GigabitEthernet0/1/1.1] commit
   ```
   ```
   [~BRAS2-GigabitEthernet0/1/1.1] quit
   ```
   
   # On BRAS2, enter the view of GE 0/1/1.2, and associate service-location group 2 with VRRP group 2.
   
   ```
   [~BRAS2] interface GigabitEthernet 0/1/1.2
   ```
   ```
   [~BRAS2-GigabitEthernet0/1/1.2] vrrp vrid 2 track service-location 2 reduced 60
   ```
   ```
   [*BRAS2-GigabitEthernet0/1/1.2] commit
   ```
   ```
   [~BRAS2-GigabitEthernet0/1/1.2] quit
   ```
   
   # Run the [**display vrrp 1**](cmdqueryname=display+vrrp+1) and [**display vrrp 2**](cmdqueryname=display+vrrp+2) commands on BRAS1 and BRAS2, respectively, to view the master/backup VRRP status, which reflects the master/backup status of the service-location groups. **State** in the command output indicates the BRAS status.
   
   ```
   [~BRAS1] display vrrp 1
   GigabitEthernet 0/1/1.1 | Virtual Router 1                                                                                      
       State                     : Master 
       Virtual IP                : 10.1.1.3  
       Master IP                 : 10.1.1.1
       Local IP                  : 10.1.1.1
       PriorityRun               : 200     
       PriorityConfig            : 200    
       MasterPriority            : 200     
       Preempt                   : YES   Delay Time     : 1500 s 
       Hold Multiplier           : 3                                                              
       TimerRun                  : 1 s 
       TimerConfig               : 1 s     
       Auth Type                 : NONE    
       Virtual MAC               : 00e0-fc12-3456   
       Check TTL                 : YES        
       Config Type               : admin-vrrp    
       Backup-forward            : disabled     
       Fast-resume               : disabled     
       Track Service-location    : 1   Priority Reduced : 60                                               
       Service-location State    : UP                                                                       
       Create Time               : 2011-10-18 11:14:48 UTC+10:59     
       Last Change Time          : 2011-10-18 14:02:46 UTC+10:59
   ```
   ```
   [~BRAS1] display vrrp 2
   GigabitEthernet 0/1/1.2 | Virtual Router 1                                                                                      
       State                     : Master  
       Virtual IP                : 10.1.2.3     
       Master IP                 : 10.1.2.1
       Local IP                  : 10.1.2.1
       PriorityRun               : 200     
       PriorityConfig            : 200          
       MasterPriority            : 200           
       Preempt                   : YES    Delay Time     : 1500 s
       Hold Multiplier           : 3                                                                          
       TimerRun                  : 1 s   
       TimerConfig               : 1 s         
       Auth Type                 : NONE        
       Virtual MAC               : 00e0-fc12-3456   
       Check TTL                 : YES       
       Config Type               : admin-vrrp    
       Backup-forward            : disabled   
       Fast-resume               : disabled     
       Track Service-location    : 2   Priority Reduced : 60                                                    
       Service-location State    : UP                                                                            
       Create Time               : 2011-10-18 11:14:48 UTC+10:59   
       Last Change Time          : 2011-10-18 14:02:46 UTC+10:59
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   **Master** in the command output indicates that BRAS1 is the master device.
   
   ```
   [~BRAS2] display vrrp 1
   GigabitEthernet0/1/1.1 | Virtual Router 1                                                                                       
       State                    : Backup   
       Virtual IP               : 10.1.1.3  
       Master IP                : 10.1.1.1 
       Local IP                 : 10.1.1.2
       PriorityRun              : 150    
       PriorityConfig           : 150   
       MasterPriority           : 200   
       Preempt                  : YES   Delay Time       : 0 s        
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
       Create Time              : 2011-10-18 11:26:40 UTC+08:00  
       Last Change Time         : 2011-10-18 14:02:22 UTC+08:00
   ```
   ```
   [~BRAS2] display vrrp 2
   GigabitEthernet0/1/1.2 | Virtual Router 1                                                                                       
       State                    : Backup  
       Virtual IP               : 10.1.2.3      
       Master IP                : 10.1.2.1 
       Local IP                 : 10.1.2.2
       PriorityRun              : 150        
       PriorityConfig           : 150      
       MasterPriority           : 200        
       Preempt                  : YES   Delay Time      : 0 s   
       Hold Multiplier          : 3                                                                   
       TimerRun                 : 1 s     
       TimerConfig              : 1 s    
       Auth Type                : NONE  
       Virtual MAC              : 00e0-fc12-3456   
       Check TTL                : YES        
       Config Type              : admin-vrrp   
       Backup-forward           : disabled    
       Fast-resume              : disabled
       Track Service-location   : 2   Priority Reduced : 60                                                          
       Service-location State   : UP 
       Create Time              : 2011-10-18 11:26:40 UTC+08:00  
       Last Change Time         : 2011-10-18 14:02:22 UTC+08:00
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   **Master** in the command output indicates that BRAS1 is the master device.
8. Bind the service-location group to the VRRP group on BRAS1 and BRAS2.
   
   
   
   # Bind service-location group 1 to VRRP group 1 on BRAS1.
   
   ```
   [~BRAS1] service-location 1
   ```
   ```
   [*BRAS1-service-location-1] vrrp vrid 1 interface GigabitEthernet 0/1/1.1
   ```
   ```
   [*BRAS1-service-location-1] commit
   ```
   ```
   [~BRAS1-service-location-1] quit
   ```
   
   # Bind service-location group 1 to VRRP group 2 on BRAS1.
   
   ```
   [~BRAS1] service-location 2
   ```
   ```
   [*BRAS1-service-location-2] vrrp vrid 2 interface GigabitEthernet 0/1/1.2
   ```
   ```
   [*BRAS1-service-location-2] commit
   ```
   ```
   [~BRAS1-service-location-2] quit
   ```
   
   # Bind service-location group 1 to VRRP group 1 on BRAS2.
   
   ```
   [~BRAS2] service-location 1
   ```
   ```
   [*BRAS2-service-location-1] vrrp vrid 1 interface GigabitEthernet 0/1/1.1
   ```
   ```
   [*BRAS2-service-location-1] commit
   ```
   ```
   [~BRAS2-service-location-1] quit
   ```
   
   # Bind service-location group 1 to VRRP group 2 on BRAS2.
   
   ```
   [~BRAS2] service-location 2
   ```
   ```
   [*BRAS2-service-location-2] vrrp vrid 2 interface GigabitEthernet 0/1/1.2
   ```
   ```
   [*BRAS2-service-location-2] commit
   ```
   ```
   [~BRAS2-service-location-2] quit
   ```
9. Create a service-instance group on BRAS1 and BRAS2 and bind the service-location groups to the service-instance groups.
   
   
   
   # Configure BRAS1.
   
   Create a service-instance group named **group1** and bind it to service-location groups 1 and 2.
   ```
   [~BRAS1] service-instance-group group1
   ```
   ```
   [*BRAS1-service-instance-group-group1] service-location 1
   ```
   ```
   [*BRAS1-service-instance-group-group1] service-location 2
   ```
   ```
   [*BRAS1-service-instance-group-group1] commit
   ```
   ```
   [~BRAS1-service-instance-group-group1] quit
   ```
   
   # Configure BRAS2.
   
   Create a service-instance group named **group1** and bind it to service-location groups 1 and 2.
   ```
   [~BRAS2] service-instance-group group1
   ```
   ```
   [*BRAS2-service-instance-group-group1] service-location 1
   ```
   ```
   [*BRAS2-service-instance-group-group1] service-location 2
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
    Remote-backup interface: GigabitEthernet0/1/1.1                                                                                      
    Peer: 10.1.1.2                                                                                                                   
    Vrrp ID: 1                                                                                                                       
    Vrrp bind interface: GigabitEthernet0/1/1.1                                                                                          
    Vrrp state: master                                                                                                                 
    Bound service-instance-group number: 1                                                                                             
    Batch-backup state: finished
   
   ```
   ```
   [~BRAS1] display service-location 2
   service-location 2                                                                                                                
    Backup scene type: inter-box                                                                                                       
    Location slot ID: 1                                                                                                    
    Remote-backup interface: GigabitEthernet0/1/1.2                                                                                      
    Peer: 10.1.2.2                                                                                                                   
    Vrrp ID: 2                                                                                                                       
    Vrrp bind interface: GigabitEthernet0/1/1.2                                                                                          
    Vrrp state: master                                                                                                                 
    Bound service-instance-group number: 1                                                                                             
    Batch-backup state: finished
   
   ```
   ```
   [~BRAS2] display service-location 1
   service-location 1                                                                                                                
    Backup scene type: inter-box                                                                                                       
    Location slot ID: 1                                                                                                    
    Remote-backup interface: GigabitEthernet0/1/1.1                                                                                      
    Peer: 10.1.1.1                                                                                                                   
    Vrrp ID: 1                                                                                                                       
    Vrrp bind interface: GigabitEthernet0/1/1.1                                                                                          
    Vrrp state: slave                                                                                                                 
    Bound service-instance-group number: 1                                                                                             
    Batch-backup state: NA
   
   ```
   ```
   [~BRAS2] display service-location 2
   service-location 2                                                                                                                
    Backup scene type: inter-box                                                                                                       
    Location slot ID: 1                                                                                                    
    Remote-backup interface: GigabitEthernet0/1/1.2                                                                                      
    Peer: 10.1.2.1                                                                                                                   
    Vrrp ID: 2                                                                                                                       
    Vrrp bind interface: GigabitEthernet0/1/1.2                                                                                          
    Vrrp state: slave                                                                                                                 
    Bound service-instance-group number: 1                                                                                             
    Batch-backup state: NA
   
   ```
10. Create a NAT instance on each of BRAS1 and BRAS2 and bind the instances to a service-instance group.
    
    
    
    # Create a NAT instance named **nat** on BRAS1 and bind it to the service-instance group named **group1**.
    
    ```
    [~BRAS1] nat instance nat id 1
    ```
    ```
    [*BRAS1-nat-instance-nat] service-instance-group group1
    ```
    ```
    [*BRAS1-nat-instance-nat] commit
    ```
    ```
    [~BRAS1-nat-instance-nat] quit
    ```
    
    # Create a NAT instance named **nat** on BRAS2 and bind it to the service-instance group named **group1**.
    
    ```
    [~BRAS2] nat instance nat id 1
    ```
    ```
    [*BRAS2-nat-instance-nat] service-instance-group group1
    ```
    ```
    [*BRAS2-nat-instance-nat] commit
    ```
    ```
    [~BRAS2-nat-instance-nat] quit
    ```
    
    # Run the [**display nat instance nat**](cmdqueryname=display+nat+instance+nat) command on BRAS1 and BRAS2 to view NAT configurations.
    
    ```
    [~BRAS1] display nat instance nat
    ```
    ```
    nat instance nat id 1                                                                                                               
     service-instance-group group1                                                                                                         
     nat address-group group1 group-id 1 bind-ip-pool pool1                                                                     
    
    ```
    ```
    [~BRAS2] display nat instance nat
    ```
    ```
    nat instance nat id 1                                                                                                               
     service-instance-group group1                                                                                                         
     nat address-group group1 group-id 1 bind-ip-pool pool1                                                                     
    
    ```
11. On each of the master and backup devices, configure a user-side VRRP group and configure it to track the service-location group. If the service-location group is not tracked, a CGN board failure cannot trigger a master/backup BRAS switchover. As a result, new distributed NAT users cannot go online.
    
    
    
    # Configure BRAS1.
    
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
    [*BRAS1-GigabitEthernet0/1/2.2] vrrp vrid 3 virtual-ip 192.168.2.200
    ```
    ```
    [*BRAS1-GigabitEthernet0/1/2.2] admin-vrrp vrid 3
    ```
    ```
    [*BRAS1-GigabitEthernet0/1/2.2] vrrp vrid 3 priority 150
    ```
    ```
    [*BRAS1-GigabitEthernet0/1/2.2] vrrp vrid 3 preempt-mode timer delay 1500
    ```
    ```
    [*BRAS1-GigabitEthernet0/1/2.2] vrrp recover-delay 20
    ```
    ```
    [*BRAS1-GigabitEthernet0/1/2.2] vrrp vrid 3 track service-location 1 reduced 50
    ```
    ```
    [*BRAS1-GigabitEthernet0/1/2.2] commit
    ```
    ```
    [~BRAS1-GigabitEthernet0/1/2.2] quit
    ```
    
    # Configure BRAS2.
    
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
    [*BRAS2-GigabitEthernet0/1/2.2] vrrp vrid 3 virtual-ip 192.168.2.200
    ```
    ```
    [*BRAS2-GigabitEthernet0/1/2.2] admin-vrrp vrid 3
    ```
    ```
    [*BRAS2-GigabitEthernet0/1/2.2] vrrp vrid 3 priority 120
    ```
    ```
    [*BRAS2-GigabitEthernet0/1/2.2] vrrp vrid 3 track service-location 1 reduced 50
    ```
    ```
    [*BRAS2-GigabitEthernet0/1/2.2] commit
    ```
    ```
    [~BRAS2-GigabitEthernet0/1/2.2] quit
    ```
12. Configure user information (user group named **natbras**, IP address pool named **natbras**, user domain named **natbras**, and AAA) and bind the user group to the NAT instance named **nat** on each of the master and backup devices.
    
    
    
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
    [~BRAS1-aaa-domain-natbras] quit
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
    [~BRAS2] ip pool natbras bas local rui-slave
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
    [~BRAS2-aaa-domain-natbras] quit
    ```
    ```
    [~BRAS2-aaa] quit
    ```
13. Configure an RBS and bind the RBS to the service-instance group on each device.
    
    
    1. Configure an RBS on BRAS1 and BRAS2.
       
       # Configure an RBS on BRAS1.
       
       ```
       [~BRAS1] remote-backup-service natbras
       ```
       ```
       [*BRAS1-rm-backup-srv-natbras] peer 10.1.1.2 source 10.1.1.1 port 7000
       ```
       ```
       [*BRAS1-rm-backup-srv-natbras] protect redirect ip-nexthop 10.1.1.2 interface GigabitEthernet0/1/1.1
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
       [*BRAS2-rm-backup-srv-natbras] protect redirect ip-nexthop 10.1.1.1 interface GigabitEthernet0/1/1.1
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
    2. Bind the RBS to the service-instance group on each device. (The RBS must be bound to the service-instance group. Otherwise, traffic is transmitted over the inter-chassis backup channel during a master/backup service switchover, affecting services.)
       
       # Configure BRAS1.
       
       ```
       [~BRAS1] service-instance-group group1
       ```
       ```
       [~BRAS1-service-instance-group-group1] remote-backup-service natbras
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
       [~BRAS2-service-instance-group-group1] remote-backup-service natbras
       ```
       ```
       [*BRAS2-service-instance-group-group1] commit
       ```
       ```
       [~BRAS2-service-instance-group-group1] quit
       ```
14. Configure RUI to back up BRAS information on BRAS1 and BRAS2.
    
    
    
    # Configure an RBS on BRAS1.
    
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
    [*BRAS1-rm-backup-prf-natbras] vrrp-id 3 interface GigabitEthernet0/1/2.2
    ```
    ```
    [*BRAS1-rm-backup-prf-natbras] commit
    ```
    ```
    [~BRAS1-rm-backup-prf-natbras] quit
    ```
    
    # Configure an RBS on BRAS2.
    
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
    [*BRAS2-rm-backup-prf-natbras] vrrp-id 3 interface GigabitEthernet0/1/2.2
    ```
    ```
    [*BRAS2-rm-backup-prf-natbras] commit
    ```
    ```
    [~BRAS2-rm-backup-prf-natbras] quit
    ```
15. Configure user-side sub-interfaces on the master and backup devices.
    
    
    
    # Configure BRAS1.
    
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
    
    # Configure BRAS2.
    
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
    [~BRAS2-GigabitEthernet0/1/2.10-user-vlan-2010] quit
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
16. Configure a traffic classification rule, a NAT behavior, and a NAT traffic policy. Then apply the policy.
    1. Configure a NAT traffic diversion policy.
       
       
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
       2. Configure an ACL numbered 3001 and an ACL rule numbered 1.
          
          ```
          [~BRAS1] acl 3001
          ```
          ```
          [*BRAS1-acl4-advance-3001] rule 1 permit ip source 192.168.0.0 0.0.255.255
          ```
          ```
          [*BRAS1-acl4-advance-3001] commit
          ```
          ```
          [~BRAS1-acl4-advance-3001] quit
          ```
       3. Configure a traffic classifier.
          
          ```
          [*BRAS1] traffic classifier c1
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
       5. Define a NAT traffic policy to associate the traffic classifier with the traffic behavior.
          
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
       6. Apply the NAT traffic diversion policy in the system view. In VS mode, the [**traffic-policy**](cmdqueryname=traffic-policy) command is supported only by the admin VS.
          
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
          [~BRAS1-nat-instance-nat] nat outbound 3001 address-group group1
          ```
          ```
          [*BRAS1-nat-instance-nat] commit
          ```
          ```
          [~BRAS1-nat-instance-nat] quit
          ```![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       Perform the preceding operations on BRAS2.

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
  service-ha hot-backup enable
  service-ha delay-time 10
  #
  user-group natbras
  #
  acl number 6001
   rule 1 permit ip source user-group natbras
  #
  acl number 3001
   rule 1 permit ip source 192.168.0.0 0.0.255.255
  #
  nat ip-pool pool1
   section 0 11.11.11.1 mask 24
   nat-instance subnet length initial 25 extend 27
   nat-instance ip used-threshold upper-limit 60 lower-limit 40
   nat alarm ip threshold 60
  #
  service-location 1
   location slot 1 
   vrrp vrid 1 interface GigabitEthernet 0/1/1.1
   remote-backup interface GigabitEthernet 0/1/1.1 peer 10.1.1.2
  #
  service-location 2
   location slot 1 
   vrrp vrid 2 interface GigabitEthernet 0/1/1.2
   remote-backup interface GigabitEthernet 0/1/1.2 peer 10.1.2.2
  #
  service-instance-group group1
   service-location 1
   service-location 2
   remote-backup-service natbras
  #
  nat instance nat id 1
   service-instance-group group1
   nat address-group group1 group-id 1 bind-ip-pool pool1
   nat outbound 3001 address-group group1
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
   protect redirect ip-nexthop 10.1.1.2 interface GigabitEthernet0/1/1.1
   ip-pool natbras
  #
  remote-backup-profile natbras
   service-type bras
   backup-id 10 remote-backup-service natbras
   peer-backup hot
   vrrp-id 3 interface GigabitEthernet0/1/2.2
  #
  interface GigabitEthernet0/1/1.1
   undo shutdown
   vlan-type dot1q 2001
   ip address 10.1.1.1 255.255.255.0
   vrrp vrid 1 virtual-ip 10.1.1.3
   admin-vrrp vrid 1 ignore-if-down
   vrrp vrid 1 priority 200
   vrrp vrid 1 track service-location 1 reduced 60
   vrrp vrid 1 preempt-mode timer delay 1500
   vrrp recover-delay 20
  #
  interface GigabitEthernet0/1/1.2
   undo shutdown
   vlan-type dot1q 2002
   ip address 10.1.2.1 255.255.255.0
   vrrp vrid 2 virtual-ip 10.1.2.3
   admin-vrrp vrid 2 ignore-if-down
   vrrp vrid 2 priority 200
   vrrp vrid 2 preempt-mode timer delay 1500
   vrrp recover-delay 20
   vrrp vrid 2 track service-location 2 reduced 60
  #
  interface GigabitEthernet0/1/2.10
   user-vlan 2010
   remote-backup-profile natbras
   bas
    access-type layer2-subscriber default-domain authentication natbras
  #
  interface GigabitEthernet0/1/2.2
   vlan-type dot1q 2002
   ip address 192.168.2.10 255.255.255.0
   vrrp vrid 3 virtual-ip 192.168.2.200
   admin-vrrp vrid 3
   vrrp vrid 3 priority 150
   vrrp vrid 3 preempt-mode timer delay 1500
   vrrp recover-delay 20
   vrrp vrid 3 track service-location 1 reduced 50
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
  service-ha hot-backup enable
  #
  user-group natbras
  #
  acl number 6001
   rule 1 permit ip source user-group natbras
  #
  acl number 3001
   rule 1 permit ip source 192.168.0.0 0.0.255.255
  #
  nat ip-pool pool1 slave
   section 0 11.11.11.1 mask 24
   nat-instance subnet length initial 25 extend 27
   nat-instance ip used-threshold upper-limit 60 lower-limit 40
   nat alarm ip threshold 60
  #
  service-location 1
   location slot 1 
   vrrp vrid 1 interface GigabitEthernet 0/1/1.1
   remote-backup interface GigabitEthernet 0/1/1.1 peer 10.1.1.1
  #
  service-location 2
   location slot 1 
   vrrp vrid 1 interface GigabitEthernet 0/1/1.2
   remote-backup interface GigabitEthernet 0/1/1.2 peer 10.1.2.1
  #
  service-instance-group group1
   service-location 1
   service-location 2
   remote-backup-service natbras
  #
  nat instance nat id 1
   service-instance-group group1
   nat address-group group1 group-id 1 bind-ip-pool pool1
   nat outbound 3001 address-group group1
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
  ip pool natbras bas local rui-slave
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
   protect redirect ip-nexthop 10.1.1.1 interface GigabitEthernet0/1/1.1
   ip-pool natbras
  #
  remote-backup-profile natbras
   service-type bras
   backup-id 10 remote-backup-service natbras
   peer-backup hot
   vrrp-id 3 interface GigabitEthernet0/1/2.2
  #
  
  interface GigabitEthernet0/1/1.1
   undo shutdown
   vlan-type dot1q 2001
   ip address 10.1.1.2 255.255.255.0
   vrrp vrid 1 virtual-ip 10.1.1.3
   admin-vrrp vrid 1 ignore-if-down
   vrrp vrid 1 priority 150
   vrrp vrid 1 track service-location 1 reduced 60
  #
  interface GigabitEthernet0/1/1.2
   undo shutdown
   vlan-type dot1q 2002
   ip address 10.1.2.2 255.255.255.0
   admin-vrrp vrid 2 ignore-if-down
   vrrp vrid 2 virtual-ip 10.1.2.3
   vrrp vrid 2 priority 150
   vrrp vrid 2 track service-location 2 reduced 60
  #
  interface GigabitEthernet0/1/2.10
   user-vlan 2010
   remote-backup-profile natbras
   bas
    access-type layer2-subscriber default-domain authentication natbras
  #
  interface GigabitEthernet0/1/2.2
   vlan-type dot1q 2002
   ip address 192.168.2.100 255.255.255.0
   vrrp vrid 3 virtual-ip 192.168.2.200
   admin-vrrp vrid 3
   vrrp vrid 3 priority 120
   vrrp vrid 3 track service-location 1 reduced 50
  #
  return
  ```