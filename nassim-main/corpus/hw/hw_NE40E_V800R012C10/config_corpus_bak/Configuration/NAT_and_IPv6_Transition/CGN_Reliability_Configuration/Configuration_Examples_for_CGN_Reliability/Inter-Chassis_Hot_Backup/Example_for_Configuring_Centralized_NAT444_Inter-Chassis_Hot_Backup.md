Example for Configuring Centralized NAT444 Inter-Chassis Hot Backup
===================================================================

This section provides an example for configuring NAT444 inter-chassis hot backup in centralized deployment mode.

#### Networking Requirements

In the centralized networking scenario shown in [Figure 1](#EN-US_TASK_0172362481__fig_01), a NAT service board is deployed in slot 1 on CGN1 and another NAT service board is deployed in slot 1 on CGN2. CGN1 and CGN2, between which a VRRP channel is established over GE interfaces, are deployed close to two SRs on the MAN core as standalone devices. CPU0 of the NAT service board in slot 1 on CGN1 and CPU0 of the NAT service board in slot 1 on CGN2 implement NAT inter-chassis hot backup. VRRP enabled for the channel determines the master/backup status of the CGN devices, and the service board status is associated with VRRP.

**Figure 1** Networking diagram for centralized NAT444 inter-chassis hot backup![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent GE0/1/1, GE0/1/2, and GE0/1/3, respectively.


  
![](images/fig_dc_ne_cgn-reliability_cfg_0002.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Set the number of sessions supported by the service board in slot 1 to 6M.
2. Enable HA hot backup.
3. Create a service-location group, configure members for HA dual-device inter-chassis backup, and configure a VRRP channel.
4. Create and configure a VRRP group.
5. Associate HA with VRRP.
6. Bind the service-location group to the VRRP group.
7. Create a service-instance group and bind it to the service-location group.
8. Create a remote backup service (RBS) and bind the service-instance group to the RBS.
9. Create a NAT instance and bind it to the service-instance group.
10. Configure a NAT traffic policy and a NAT conversion policy.

#### Data Preparation

To complete the configuration, you need the following data:

| No. | Data |
| --- | --- |
| 1 | Index of a service-location group |
| 2 | CPU ID and slot ID of the active CPU on CGN1's service board (CPU 0 in slot 1 in this example) |
| 3 | CPU ID and slot ID of the standby CPU on CGN2's service board (CPU 0 in slot 1 in this example) |
| 4 | Names of VRRP interfaces on CGN1 and CGN2 |
| 5 | IP addresses of VRRP interfaces on CGN1 and CGN2 |
| 6 | ID of a VRRP group |
| 7 | Virtual IP address of a VRRP group |
| 8 | Priorities of VRRP group members |
| 9 | VRRP preemption delay |
| 10 | Name of a service-instance group |
| 11 | Name and index of a NAT instance |



#### Procedure

1. Configure interface IP addresses. For configuration details, see [Configuration Files](#EN-US_TASK_0172362481__li650430118214025) in this section.
2. Set the number of sessions supported by the service boards in slot 1 to 6M on CGN1 and CGN2.
   
   # Configure the master device CGN1.
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
   
   # Configure the backup device CGN2.
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
3. Enable HA hot backup on CGN1 and CGN2.
   
   
   
   # Enable HA hot backup on CGN1.
   
   ```
   [~CGN1] service-ha hot-backup enable
   ```
   ```
   [*CGN1] commit
   ```
   
   # Enable HA hot backup on CGN2.
   
   ```
   [~CGN2] service-ha hot-backup enable
   ```
   ```
   [*CGN2] commit
   ```
4. Create a service-location group on CGN1 and CGN2, configure members for HA dual-device inter-chassis backup, and configure a VRRP channel.
   
   
   
   # Create service-location group 1 on CGN1, add CPU 0 in slot 1 as an HA dual-device inter-chassis backup member, and set the local VRRP outbound interface to GE 0/1/1 and the peer IP address to 10.1.1.2.
   
   ```
   [~CGN1] service-location 1
   ```
   ```
   [*CGN1-service-location-1] location slot 1 
   ```
   ```
   [*CGN1-service-location-1] remote-backup interface GigabitEthernet 0/1/1 peer 10.1.1.2
   ```
   ```
   [*CGN1-service-location-1] commit
   ```
   ```
   [~CGN1-service-location-1] quit
   ```
   
   # Create service-location group 1 on CGN2, add CPU 0 in slot 1 as an HA dual-device inter-chassis backup member, and set the local VRRP outbound interface to GE 0/1/1 and the peer IP address to 10.1.1.1.
   
   ```
   [~CGN2] service-location 1
   ```
   ```
   [*CGN2-service-location-1] location slot 1 
   ```
   ```
   [*CGN2-service-location-1] remote-backup interface GigabitEthernet 0/1/1 peer 10.1.1.1
   ```
   ```
   [*CGN2-service-location-1] commit
   ```
   ```
   [~CGN2-service-location-1] quit
   ```
5. Configure a VRRP group on CGN1 and CGN2.
   
   
   
   # On CGN1, enter the view of GE0/1/1, create VRRP group 1, and set the virtual IP address of the VRRP group to 10.1.1.3. Configure the VRRP group as an mVRRP group, and set CGN1's priority in the VRRP group to 200, the VRRP preemption delay to 1500s, and the VRRP recovery delay to 15s.
   
   ```
   [~CGN1] interface GigabitEthernet0/1/1
   ```
   ```
   [~CGN1-GigabitEthernet0/1/1] vrrp vrid 1 virtual-ip 10.1.1.3
   ```
   ```
   [*CGN1-GigabitEthernet0/1/1] admin-vrrp vrid 1 ignore-if-down
   ```
   ```
   [*CGN1-GigabitEthernet0/1/1] vrrp vrid 1 priority 200
   ```
   ```
   [*CGN1-GigabitEthernet0/1/1] vrrp vrid 1 preempt-mode timer delay 1500
   ```
   ```
   [*CGN1-GigabitEthernet0/1/1] vrrp recover-delay 15
   ```
   ```
   [*CGN1-GigabitEthernet0/1/1] commit
   ```
   ```
   [~CGN1-GigabitEthernet0/1/1] quit
   ```
   
   # On CGN2, enter the view of GE0/1/1, create VRRP group 1, and set the virtual IP address of the VRRP group to 10.1.1.3. Configure the VRRP group as an mVRRP group, set CGN2's priority in the VRRP group to 150, and set the VRRP recovery delay to 15s.
   
   ```
   [~CGN2] interface GigabitEthernet0/1/1
   ```
   ```
   [*CGN2-GigabitEthernet0/1/1] vrrp vrid 1 virtual-ip 10.1.1.3
   ```
   ```
   [*CGN2-GigabitEthernet0/1/1] admin-vrrp vrid 1 ignore-if-down
   ```
   ```
   [*CGN2-GigabitEthernet0/1/1] vrrp vrid 1 priority 150
   ```
   ```
   [*CGN2-GigabitEthernet0/1/1] vrrp recover-delay 15
   ```
   ```
   [*CGN2-GigabitEthernet0/1/1] commit
   ```
   ```
   [~CGN2-GigabitEthernet0/1/1] quit
   ```
6. Associate the service-location group with the VRRP group on each device.
   
   
   
   # On CGN1, enter the view of GE0/1/1, and associate service-location group 1, user-side interface, and network-side interface with VRRP group 1.
   
   ```
   [~CGN1] interface GigabitEthernet 0/1/1
   ```
   ```
   [~CGN1-GigabitEthernet0/1/1] vrrp vrid 1 track service-location 1 reduced 60
   ```
   ```
   [*CGN1-GigabitEthernet0/1/1] vrrp vrid 1 track interface GigabitEthernet 0/1/2 reduced 60
   ```
   ```
   [*CGN1-GigabitEthernet0/1/1] vrrp vrid 1 track interface GigabitEthernet 0/1/3 reduced 60
   ```
   ```
   [*CGN1-GigabitEthernet0/1/1] commit
   ```
   ```
   [~CGN1-GigabitEthernet0/1/1] quit
   ```
   
   # On CGN2, enter the view of GE 0/1/1, and associate service-location group 1 with VRRP group 1.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This step is optional on the backup device. You can determine whether to perform this step based on network requirements.
   
   ```
   [~CGN2] interface GigabitEthernet 0/1/1
   ```
   ```
   [~CGN2-GigabitEthernet0/1/1] vrrp vrid 1 track service-location 1 reduced 60
   ```
   ```
   [*CGN2-GigabitEthernet0/1/1] commit
   ```
   ```
   [~CGN2-GigabitEthernet0/1/1] quit
   ```
   
   # Run the [**display vrrp 1**](cmdqueryname=display+vrrp+1) command on CGN1 and CGN2 to view the master/backup VRRP status, which reflects the master/backup status of the service-location group. **State** in the command output indicates the CGN device's status.
   
   ```
   [~CGN1] display vrrp 1
   GigabitEthernet 0/1/1 | Virtual Router 1                                                                                      
       State                  : Master  
       Virtual IP             : 10.1.1.3 
       Master IP              : 10.1.1.1  
       Local IP               : 10.1.1.1
       PriorityRun            : 200   
       PriorityConfig         : 200  
       MasterPriority         : 200  
       Preempt                : YES    Delay Time  : 1500 s  
       Hold Multiplier        : 3
       TimerRun               : 1 s   
       TimerConfig            : 1 s     
       Auth Type              : NONE  
       Virtual MAC            : 00e0-fc12-3456 
       Check TTL              : YES         
       Config Type            : admin-vrrp     
       Backup-forward         : disabled   
       Fast-resume            : disabled 
       Track IF               : GigabitEthernet0/1/2    Priority Reduced : 60
       IF State               : UP
       Track IF               : GigabitEthernet0/1/3    Priority Reduced : 60
       IF State               : UP
       Track Service-location : 1    Priority Reduced : 60                                                                              
       Service-location State : UP                                                                                                     
       Create Time            : 2011-10-18 11:14:48 UTC+10:59 
       Last Change Time       : 2011-10-18 14:02:46 UTC+10:59
   
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   **Master** in the command output indicates that CGN1 is the master device.
   
   ```
   [~CGN2] display vrrp 1
   GigabitEthernet0/1/1 | Virtual Router 1                                                                                       
       State                  : Backup  
       Virtual IP             : 10.1.1.3  
       Master IP              : 10.1.1.1 
       Local IP               : 10.1.1.2
       PriorityRun            : 150     
       PriorityConfig         : 150     
       MasterPriority         : 200      
       Preempt                : YES     Delay Time    : 0 s     
       Hold Multiplier        : 3                                                                                           
       TimerRun               : 1 s 
       TimerConfig            : 1 s    
       Auth Type              : NONE  
       Virtual MAC            : 00e0-fc12-3456 
       Check TTL              : YES         
       Config Type            : admin-vrrp  
       Backup-forward         : disabled   
       Fast-resume            : disabled
       Track Service-location : 1   Priority Reduced : 60                                                                              
       Service-location State : UP 
       Create Time            : 2011-10-18 11:26:40 UTC+08:00  
       Last Change Time       : 2011-10-18 14:02:22 UTC+08:00
   
   ```
7. Bind the service-location group to the VRRP group on CGN1 and CGN2.
   
   
   
   # Bind service-location group 1 to VRRP group 1 on CGN1.
   
   ```
   [~CGN1] service-location 1
   ```
   ```
   [~CGN1-service-location-1] vrrp vrid 1 interface GigabitEthernet 0/1/1
   ```
   ```
   [*CGN1-service-location-1] commit
   ```
   ```
   [~CGN1-service-location-1] quit
   ```
   
   # Bind service-location group 1 to VRRP group 1 on CGN2.
   
   ```
   [~CGN2] service-location 1
   ```
   ```
   [~CGN2-service-location-1] vrrp vrid 1 interface GigabitEthernet 0/1/1
   ```
   ```
   [*CGN2-service-location-1] commit
   ```
   ```
   [~CGN2-service-location-1] quit
   ```
8. Create a service-instance group on CGN1 and CGN2 and bind them to the service-location group.
   
   
   
   # Create a service-instance group named **group1** on CGN1 and bind it to service-location group 1.
   
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
   
   # Create a service-instance group named **group1** on CGN2 and bind it to service-location group 1.
   
   ```
   [~CGN2] service-instance-group group1
   ```
   ```
   [*CGN2-service-instance-group-group1] service-location 1
   ```
   ```
   [*CGN2-service-instance-group-group1] commit
   ```
   ```
   [~CGN2-service-instance-group-group1] quit
   ```
   
   # Run the [**display service-location 1**](cmdqueryname=display+service-location+1) command on CGN1 and CGN2 to view HA information. **Vrrp state** in the command output indicates the status of a service-location group, which must be consistent with the CGN device's VRRP status. **Batch-backup state** in the command output indicates whether batch backup has been finished.
   
   ```
   [~CGN1] display service-location 1
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
   [~CGN2] display service-location 1
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
9. Create a remote backup service (RBS) and bind the service-instance group to the RBS.
   
   
   
   # Configure CGN1.
   
   ```
   [~CGN1] remote-backup-service natrbs
   ```
   ```
   [*CGN1-rm-backup-srv-natrbs] peer 10.1.1.2 source 10.1.1.1 port 1024
   ```
   ```
   [*CGN1-rm-backup-srv-natrbs] commit
   ```
   ```
   [~CGN1-rm-backup-srv-natrbs] quit
   ```
   ```
   [~CGN1] service-instance-group group1
   ```
   ```
   [~CGN1-service-instance-group-group1] remote-backup-service natrbs
   ```
   ```
   [*CGN1-service-instance-group-group1] commit
   ```
   ```
   [~CGN1-service-instance-group-group1] quit
   ```
   
   # Configure CGN2.
   
   ```
   [~CGN2] remote-backup-service natrbs
   ```
   ```
   [*CGN2-rm-backup-srv-natrbs] peer 10.1.1.1 source 10.1.1.2 port 1024
   ```
   ```
   [*CGN2-rm-backup-srv-natrbs] commit
   ```
   ```
   [~CGN2-rm-backup-srv-natrbs] quit
   ```
   ```
   [~CGN2] service-instance-group group1
   ```
   ```
   [~CGN2-service-instance-group-group1] remote-backup-service natrbs
   ```
   ```
   [*CGN2-service-instance-group-group1] commit
   ```
   ```
   [~CGN2-service-instance-group-group1] quit
   ```
10. Create a NAT instance on each of CGN1 and CGN2 and bind the instances to a service-instance group.
    
    
    
    # Create a NAT instance named **nat** on CGN1 and bind it to the service-instance group named **group1**.
    
    ```
    [~CGN1] nat instance nat id 1
    ```
    ```
    [*CGN1-nat-instance-nat] service-instance-group group1
    ```
    ```
    [*CGN1-nat-instance-nat] nat address-group address-group1 group-id 1 11.11.11.100 11.11.11.105
    ```
    ```
    [*CGN1-nat-instance-nat] commit
    ```
    ```
    [~CGN1-nat-instance-nat] quit
    ```
    
    # Create a NAT instance named **nat** on CGN2 and bind it to the service-instance group named **group1**.
    
    ```
    [~CGN2] nat instance nat id 1
    ```
    ```
    [*CGN2-nat-instance-nat] service-instance-group group1
    ```
    ```
    [*CGN2-nat-instance-nat] nat address-group address-group1 group-id 1 11.11.11.100 11.11.11.105
    ```
    ```
    [*CGN2-nat-instance-nat] commit
    ```
    ```
    [~CGN2-nat-instance-nat] quit
    ```
11. Configure a NAT traffic diversion policy and a NAT conversion policy on CGN1 and CGN2. For details, see "Example for Configuring Centralized NAT" in *NAT and IPv6 Transition > NAT Configuration*.
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    CGN inter-chassis hot backup is mutually exclusive with outbound-interface NAT.
    
    # Configure a NAT traffic diversion policy and a NAT conversion policy on CGN1.
    
    1. Configure a NAT traffic diversion policy.
       
       1. Configure an ACL numbered 3001 and an ACL rule numbered 1 in an ACL-based traffic classification policy to allow only hosts with a network segment address of 192.168.10.0/24 to access the Internet.
          ```
          [~CGN1] acl 3001
          ```
          ```
          [*CGN1-acl4-advance-3001] rule 1 permit ip source 192.168.10.0 0.0.0.255
          ```
          ```
          [*CGN1-acl4-advance-3001] commit
          ```
          ```
          [~CGN1-acl4-advance-3001] quit
          ```
       2. Configure a traffic classifier.
          ```
          [~CGN1] traffic classifier classifier1
          ```
          ```
          [*CGN1-classifier-classifier1] if-match acl 3001
          ```
          ```
          [*CGN1-classifier-classifier1] commit
          ```
          ```
          [~CGN1-classifier-classifier1] quit
          ```
       3. Define a traffic behavior **behavior1** and bind it to the NAT instance **nat1**.
          ```
          [~CGN1] traffic behavior behavior1
          ```
          ```
          [*CGN1-behavior-behavior1] nat bind instance nat
          ```
          ```
          [*CGN1-behavior-behavior1] commit
          ```
          ```
          [~CGN1-behavior-behavior1] quit
          ```
       4. Create a traffic policy **policy1** to associate all ACL rules with the traffic behaviors.
          ```
          [~CGN1] traffic policy policy1
          ```
          ```
          [*CGN1-policy-policy1] classifier classifier1 behavior behavior1
          ```
          ```
          [*CGN1-policy-policy1] commit
          ```
          ```
          [~CGN1-policy-policy1] quit
          ```
       5. Apply the NAT traffic diversion policy in the GE 0/1/2 interface view.
          ```
          [~CGN1] interface gigabitEthernet 0/1/2
          ```
          ```
          [~CGN1-GigabitEthernet0/1/2] ip address 192.168.10.1 24
          ```
          ```
          [*CGN1-GigabitEthernet0/1/2] traffic-policy policy1 inbound
          ```
          ```
          [*CGN1-GigabitEthernet0/1/2] commit
          ```
          ```
          [~CGN1-GigabitEthernet0/1/2] quit
          ```
    2. Configure a NAT conversion policy.
       
       ```
       [~CGN1] nat instance nat
       ```
       ```
       [~CGN1-nat-instance-nat] nat outbound 3001 address-group address-group1
       ```
       ```
       [*CGN1-nat-instance-nat] commit
       ```
       ```
       [~CGN1-nat-instance-nat] quit
       ```![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    The configuration of CGN2 is similar to that of CGN1. For configuration details, see [CGN2 configuration file](#EN-US_TASK_0172362481__config_02) in this section.
    
    # Run the [**display nat instance nat**](cmdqueryname=display+nat+instance+nat) command on CGN1 and CGN2 to view NAT configurations.
    
    ```
    [~CGN1] display nat instance nat
    ```
    ```
    nat instance nat id 1                                                                                                               
     service-instance-group group1                                                                                                        
     nat address-group address-group1 group-id 1 11.11.11.100 11.11.11.105                                                                     
     nat outbound 3001 address-group address-group1
    ```
    ```
    [~CGN2] display nat instance nat
    ```
    ```
    nat instance nat id 1                                                                                                               
     service-instance-group group1                                                                                                         
     nat address-group address-group1 group-id 1 11.11.11.100 11.11.11.105                                                                     
     nat outbound 3001 address-group address-group1
    ```

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
  acl number 3001
   rule 1 permit ip source 192.168.10.0 0.0.0.255
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
  service-ha hot-backup enable
  #
  service-location 1
   location slot 1 
   vrrp vrid 1 interface GigabitEthernet 0/1/1
   remote-backup interface GigabitEthernet 0/1/1 peer 10.1.1.2
  #
  service-instance-group group1
   service-location 1
   remote-backup-service natrbs
  #
  remote-backup-service natrbs          
   peer 10.1.1.2 source 10.1.1.1 port 1024
  #
  nat instance nat id 1
   service-instance-group group1                                                              
   nat address-group address-group1 group-id 1 11.11.11.100 11.11.11.105                           
   nat outbound 3001 address-group address-group1
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   vrrp vrid 1 virtual-ip 10.1.1.3
   admin-vrrp vrid 1 ignore-if-down
   vrrp vrid 1 priority 200
   vrrp vrid 1 preempt-mode timer delay 1500
   vrrp vrid 1 track interface GigabitEthernet 0/1/2 reduced 60
   vrrp vrid 1 track interface GigabitEthernet 0/1/3 reduced 60
   vrrp vrid 1 track service-location 1 reduced 60
   vrrp recover-delay 15  
  #
  interface GigabitEthernet 0/1/2
   undo shutdown
   ip address 192.168.10.1 255.255.255.0
   traffic-policy policy1 inbound
  #
  interface GigabitEthernet 0/1/3
   ip address 11.2.1.1 255.255.0.0
  #
  ospf 10
   default cost inherit-metric
   import-route unr
   opaque-capability enable
   area 0.0.0.0
    network 11.2.0.0 0.0.255.255
    network 192.168.0.0 0.0.255.255
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
  acl number 3001
   rule 1 permit ip source 192.168.10.0 0.0.0.255
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
  service-ha hot-backup enable
  #
  service-location 1
   location slot 1 
   vrrp vrid 1 interface GigabitEthernet 0/1/1
   remote-backup interface GigabitEthernet 0/1/1 peer 10.1.1.1
  #
  service-instance-group group1
   service-location 1
   remote-backup-service natrbs
  #
  remote-backup-service natrbs          
   peer 10.1.1.1 source 10.1.1.2 port 1024
  #
  nat instance nat id 1
   service-instance-group group1                
   nat address-group address-group1 group-id 1 11.11.11.100 11.11.11.105                           
   nat outbound 3001 address-group address-group1
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
  interface GigabitEthernet 0/1/2
   undo shutdown
   ip address 192.168.20.1 255.255.255.0
   traffic-policy policy1 inbound
  #
  interface GigabitEthernet 0/1/3
   ip address 11.4.1.1 255.255.0.0
  #
  ospf 10
   default cost inherit-metric
   import-route unr
   opaque-capability enable
   area 0.0.0.0
    network 11.4.0.0 0.0.255.255
    network 192.169.0.0 0.0.255.255
  #
  return
  ```