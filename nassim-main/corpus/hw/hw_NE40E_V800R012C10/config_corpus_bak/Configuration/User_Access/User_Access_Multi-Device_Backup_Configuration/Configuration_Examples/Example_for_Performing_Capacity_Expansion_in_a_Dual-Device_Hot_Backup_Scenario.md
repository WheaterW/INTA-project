Example for Performing Capacity Expansion in a Dual-Device Hot Backup Scenario
==============================================================================

This section describes how to expand the interface capacity and change a user access interface in a dual-device hot backup scenario.

#### Networking Requirements

In a dual-device hot backup scenario, a pair of RBP instances in master/backup mode must be configured on the master and backup devices to back up services between the two devices.

On the example network, users access BRAS 1 and BRAS 2 through the LAN switch (LSW). The user access interfaces on the two devices are GE or Eth-Trunk interfaces.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The dual-device hot backup mechanism determines the corresponding RBP instance based on the backup ID and RBS values in the backup table, and then determines the user access interface based on the RBP instance and user VLAN ID. The values of the backup ID, RBS, and VLAN ID cannot be changed.


**Figure 1** Performing capacity expansion in an IPv6 dual-device hot backup scenario![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent GE 0/1/0 and GE 0/3/0, respectively.


  
![](images/fig_dc_ne_cfg_rui_003101.png)  

| **Device** | **Interface** | **IP Address** |
| --- | --- | --- |
| BRAS1 | GE0/1/0.1 | Interface through which users go online |
| BRAS1 | GE0/3/0 | 10.1.1.1/24 |
| BRAS2 | GE0/1/0.1 | Interface through which users go online |
| BRAS2 | GE0/3/0 | 10.1.1.2/24 |




#### Configuration Roadmap

You can use either of the following methods for capacity expansion in dual-device hot backup scenarios.

* Add an Eth-Trunk member interface for capacity expansion.
  1. Expand the capacity of BRAS 1. Shut down the original Eth-Trunk member interface on BRAS 1. Then, a master/backup device switchover is performed. BRAS 1 functions as the backup device, and users on BRAS 1 are switched to BRAS 2.
  2. Add a new member interface to the Eth-Trunk interface on BRAS 1.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Ensure that the new member interface is of the same type as the existing member interface. Otherwise, the new member interface fails to be added. For example, if the existing member interface is a 10GE interface but the new member interface is a 100GE interface, the new member interface fails to be added to the Eth-Trunk interface. You must remove the existing member interface and then add the new member interface.
  3. Enable the existing Eth-Trunk member interface on BRAS 1 to restore user services.
* Create a BAS interface to replace the original one for capacity expansion.
  1. Expand the capacity of BRAS 1. Disconnect the RBS channel between the master and backup devices, and shut down the user access interface on BRAS 1. Then, a master/backup device switchover is performed. BRAS 1 functions as the backup device, and users on BRAS 1 are switched to BRAS 2.
  2. Log out online users.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Online users can be logged out only after the RBS channel between the master and backup devices is disconnected. Otherwise, users on the peer device are logged out.
  3. Delete the binding configurations of the original BAS interface on BRAS 1, create a BAS interface on BRAS 1, and synchronize the configurations of the original BAS interface to the new BAS interface.
  4. Restore the RBS channel between the master and backup devices.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The configuration on BRAS2 is similar to the configuration on BRAS1. The configuration on BRAS1 is used in this example. For details about the configuration on BRAS2, see the BRAS2 configuration file.

The BAS interface can be a GE or an Eth-Trunk interface. When an Eth-Trunk interface is used for capacity expansion, adding an Eth-Trunk member interface is recommended.



#### Data Preparation

To complete the configuration, you need the following data:

* VRRP parameters (VRRP ID and preemption delay)
* RBS channel parameters
* IP address of each interface on BRAS 1 and BRAS 2
* Backup ID, which works together with an RBS to identify an RBP to which users belong

#### Procedure

* Add an Eth-Trunk member interface for capacity expansion.
  1. Expand the capacity of BRAS 1. Shut down the existing Eth-Trunk member interface on BRAS 1. Then, users on BRAS 1 are switched to BRAS 2, and BRAS 1 functions as the backup device.
     
     
     
     # In this example, the **interface GigabitEthernet 0/1/0** command has been configured before capacity expansion is performed.
     
     ```
     [~BRAS1] interface GigabitEthernet 0/1/0               
     [*BRAS1-GigabitEthernet0/1/0] shutdown                           
     [*BRAS1-GigabitEthernet0/1/0] commit            
     [~BRAS1-GigabitEthernet0/1/0] quit                             
     ```
  2. Add a new member interface to the Eth-Trunk interface on BRAS 1.
     
     
     
     # In this example, **interface GigabitEthernet 0/1/1** is used as the new Eth-Trunk member interface.
     
     ```
     [~BRAS1] interface GigabitEthernet 0/1/1               
     [*BRAS1-GigabitEthernet0/1/1] eth-trunk 1                           
     [*BRAS1-GigabitEthernet0/1/1] commit            
     [~BRAS1-GigabitEthernet0/1/1] quit                             
     ```
  3. Enable the existing Eth-Trunk member interface on BRAS 1 to restore user services.
     
     
     ```
     [~BRAS1] interface GigabitEthernet 0/1/0               
     [*BRAS1-GigabitEthernet0/1/0] undo shutdown                           
     [*BRAS1-GigabitEthernet0/1/0] commit            
     [~BRAS1-GigabitEthernet0/1/0] quit                             
     ```
  4. Verify the configuration.
     
     
     ```
     [BRAS1] display interface eth-trunk 1
     ```
     ```
      -----------------------------------------------
      Eth-Trunk1 current state : UP (ifindex: 33)
      Line protocol current state : DOWN 
      Link quality grade : GOOD
      Description: 
      Route Port,Hash arithmetic : According to flow, Maximal BW: 100Mbps, Current BW: 100Mbps, The Maximum Transmit Unit is 1500
      Internet protocol processing : disabled
      IP Sending Frames' Format is PKTFMT_ETHNT_2, Hardware address is 00e0-fc12-3456
      Current system time: 2019-01-03 03:13:49
      Physical is ETH_TRUNK
         Last 300 seconds input rate 0 bits/sec, 0 packets/sec
         Last 300 seconds output rate 1054 bits/sec, 0 packets/sec
         Input: 0 packets,0 bytes
                0 unicast,0 broadcast,0 multicast
                0 errors,0 drops
         Output:5 packets,0 bytes
                0 unicast,3 broadcast,2 multicast
                0 errors,0 drops
         Last 300 seconds input utility rate:  0.00%
         Last 300 seconds output utility rate: 0.01%
      ----------------------------------------------------------
      PortName                      Status              Weight   
      ----------------------------------------------------------
      GigabitEthernet0/1/0          UP                  1        
      GigabitEthernet0/1/1          UP                  1        
     ----------------------------------------------------------
      The Number of Ports in Trunk : 1
      The Number of UP Ports in Trunk : 1
     
     ```
* Create a BAS interface to replace the original one for capacity expansion.
  1. Expand the capacity of BRAS 1. Disconnect the RBS channel between the master and backup devices, and shut down the user access interface on BRAS 1. Then, users on BRAS 1 are switched to BRAS 2, and BRAS 1 functions as the backup device.
     
     
     ```
     [~BRAS1] interface GigabitEthernet 0/1/0               
     [*BRAS1-GigabitEthernet0/1/0] shutdown                           
     [*BRAS1-GigabitEthernet0/1/0] commit            
     [~BRAS1-GigabitEthernet0/1/0] quit                             
     ```
  2. Log out online users.
     
     
     ```
     [~BRAS1] remote-backup-service s1               
     [*BRAS1-rm-backup-srv-s1] shutdown                           
     Warning: This operation will cause the TCP connection to be interrupted. Continue? [Y/N]:Y
     [*BRAS1-rm-backup-srv-s1] commit            
     [~BRAS1-rm-backup-srv-s1] quit                             
     [~BRAS1] aaa
     [~BRAS1-aaa] cut access-user interface GigabitEthernet 0/1/0
     [*BRAS1-aaa] commit
     [~BRAS1-aaa] quit 
     ```
  3. Delete the binding configurations of the original BAS interface on BRAS 1, create a BAS interface on BRAS 1, and synchronize the configurations of the original BAS interface to the new BAS interface.
     
     
     ```
     [~BRAS1] interface GigabitEthernet 0/1/0.1               
     [*BRAS1-GigabitEthernet0/1/0.1] shutdown                           
     [*BRAS1-GigabitEthernet0/1/0.1] commit
     [~BRAS1-GigabitEthernet0/1/0.1] undo user-vlan 2
     [~BRAS1-GigabitEthernet0/1/0.1] undo remote-backup-profile p1
     [*BRAS1-GigabitEthernet0/1/0.1] commit
     [~BRAS1-GigabitEthernet0/1/0.1] quit
     [~BRAS1] interface GigabitEthernet 0/1/1.1
     [~BRAS1-GigabitEthernet0/1/1.1] ipv6 enable
     [*BRAS1-GigabitEthernet0/1/1.1] ipv6 address auto link-local
     [*BRAS1-GigabitEthernet0/1/1.1] ipv6 nd autoconfig managed-address-flag
     [*BRAS1-GigabitEthernet0/1/1.1] ipv6 nd autoconfig other-flag
     [*BRAS1-GigabitEthernet0/1/1.1] user-vlan 2
     [*BRAS1-GigabitEthernet0/1/1.1] remote-backup-profile p1
     [*BRAS1-GigabitEthernet0/1/1.1] bas
     [*BRAS1-GigabitEthernet0/1/1.1-bas] access-type layer2-subscriber default-domain authentication huawei
     [*BRAS1-GigabitEthernet0/1/1.1-bas] authentication-method-ipv6 bind
     [*BRAS1-GigabitEthernet0/1/1.1-bas] commit
     [~BRAS1-GigabitEthernet0/1/1.1-bas] quit
     [~BRAS1-GigabitEthernet0/1/1.1] quit
     ```
  4. Restore the RBS channel between the master and backup devices.
     
     
     ```
     [~BRAS1] remote-backup-service s1               
     [*BRAS1-rm-backup-srv-s1] undo shutdown                           
     [*BRAS1-rm-backup-srv-s1] commit            
     [~BRAS1-rm-backup-srv-s1] quit                             
     ```

#### Configuration Files

* Add an Eth-Trunk member interface for capacity expansion.
  + BRAS 1 configuration file
    
    ```
    #
    sysname BRAS1
    #
    bfd
    #
    mpls
    #
    mpls ldp
    #
    ipv6 prefix prefix1 local
     prefix 2001:db8:1::2013/64
    #
    ipv6 pool pool1 bas local
     prefix prefix1
    #
    aaa
     domain huawei   
      authentication-scheme default0                    
      accounting-scheme default0                  
      ipv6-pool pool1
    #
    remote-backup-service s1                      
     peer 10.1.2.2 source 10.1.2.1 port 6001       
     protect lsp-tunnel for-all-instance peer-ip 10.1.2.2   
     track interface GigabitEthernet0/2/1          
     ipv6-pool pool1
    #
    remote-backup-profile p1                       
     service-type bras         
     backup-id 1 remote-backup-service s1                   
     peer-backup hot                    
     vrrp-id 1 interface Eth-Trunk1.2
    #
    #
    interface GigabitEthernet 0/1/0
     shutdown
     eth-trunk 1
    #
    interface GigabitEthernet 0/1/1
     undo shutdown
     eth-trunk 1
    #
    #
    interface Eth-Trunk1.2              
     vlan-type dot1q 1                             
     ip address 10.1.1.1 255.255.255.0            
     vrrp vrid 1 virtual-ip 10.1.1.100            
     admin-vrrp vrid 1                             
     vrrp vrid 1 priority 180                      
     vrrp vrid 1 preempt-mode timer delay 60       
     vrrp vrid 1 track interface GigabitEthernet0/2/0 reduced 50                    
     vrrp vrid 1 track bfd-session session-name bfd1 peer
    #
    interface Eth-Trunk1.1            
     ipv6 enable  
     ipv6 address auto link-local                  
     ipv6 nd autoconfig managed-address-flag       
     ipv6 nd autoconfig other-flag                           
     user-vlan 2   
     remote-backup-profile p1                       
     bas          
      access-type layer2-subscriber default-domain authentication huawei   
      authentication-method-ipv6 bind
    #
    interface LoopBack1
     ip address 10.1.2.1 255.255.255.255
    #
    bfd bfd1 bind peer-ip 10.1.1.2
     discriminator local 8
     discriminator remote 6
    #
    ospf 1        
     import-route direct                           
     area 0.0.0.0 
     network 10.1.2.1 0.0.0.0
    #
    return
    #
    
    ```
  + BRAS 2 configuration file
    
    ```
    #
    sysname BRAS2
    #
    bfd
    #
    mpls
    #
    mpls ldp
    #
    ipv6 prefix prefix1 local
     prefix 2001:db8:1::2013/64
    #
    ipv6 pool pool1 bas local
     prefix prefix1
    #
    aaa
     domain huawei   
      authentication-scheme default0                    
      accounting-scheme default0                  
      ipv6-pool pool1
    #
    remote-backup-service s1
     peer 10.1.2.1 source 10.1.2.2 port 6001
     protect lsp-tunnel for-all-instance peer-ip 10.1.2.1
     track interface GigabitEthernet0/2/1
     ipv6-pool pool1
    #
    remote-backup-profile p1
     service-type bras
     backup-id 1 remote-backup-service s1
     peer-backup hot
     vrrp-id 1 interface Eth-Trunk1.2
    #
    #
    interface GigabitEthernet 0/1/0
     shutdown
     eth-trunk 1
    #
    interface GigabitEthernet 0/1/1
     undo shutdown
     eth-trunk 1
    #
    interface Eth-Trunk1.2              
     vlan-type dot1q 1                             
     ip address 10.1.1.2 255.255.255.0           
     vrrp vrid 1 virtual-ip 10.1.1.100            
     admin-vrrp vrid 1                             
     vrrp vrid 1 priority 150                      
     vrrp vrid 1 track interface GigabitEthernet0/2/0 reduced 50                    
     vrrp vrid 1 track bfd-session session-name bfd1 peer
    #
    interface Eth-Trunk1.1          
     ipv6 enable  
     ipv6 address auto link-local                  
     ipv6 nd autoconfig managed-address-flag       
     ipv6 nd autoconfig other-flag                            
     user-vlan 2   
     remote-backup-profile p1                 
     bas          
      access-type layer2-subscriber default-domain authentication huawei
      authentication-method-ipv6 bind
    #
    interface LoopBack1
     ip address 10.1.2.2 255.255.255.255
    #
    bfd bfd2 bind peer-ip 10.1.2.1                
     discriminator local 6                         
     discriminator remote 8                        
    #
    ospf 1
     import-route direct
     area 0.0.0.0
     network 10.1.2.2 0.0.0.0
    #
    return
    #
    ```
* Create a BAS interface to replace the original one for capacity expansion.
  + BRAS 1 configuration file
    
    ```
    #
    sysname BRAS1
    #
    bfd
    #
    mpls
    #
    mpls ldp
    #
    ipv6 prefix prefix1 local
     prefix 2001:db8:1::2013/64
    #
    ipv6 pool pool1 bas local
     prefix prefix1
    #
    aaa
     domain huawei   
      authentication-scheme default0                    
      accounting-scheme default0                  
      ipv6-pool pool1
    #
    remote-backup-service s1                      
     peer 10.1.2.2 source 10.1.2.1 port 6001       
     protect lsp-tunnel for-all-instance peer-ip 10.1.2.2   
     track interface GigabitEthernet0/2/0          
     ipv6-pool pool1
    #
    remote-backup-profile p1                       
     service-type bras         
     backup-id 1 remote-backup-service s1                   
     peer-backup hot                    
     vrrp-id 1 interface GigabitEthernet0/1/0.2
     nas logic-port GigabitEthernet 0/1/0
     nas logic-sysname huawei
     nas logic-ip 1.1.1.1
    #
    interface GigabitEthernet0/1/0.2              
     vlan-type dot1q 1                             
     ip address 10.1.1.1 255.255.255.0            
     vrrp vrid 1 virtual-ip 10.1.1.100            
     admin-vrrp vrid 1                             
     vrrp vrid 1 priority 180                      
     vrrp vrid 1 preempt-mode timer delay 60       
     vrrp vrid 1 track interface GigabitEthernet0/2/0 reduced 50                    
     vrrp vrid 1 track bfd-session session-name bfd1 peer
    #
    interface GigabitEthernet0/1/0.1    
     shutdown        
     ipv6 enable 
     ipv6 address auto link-local 
     ipv6 nd autoconfig managed-address-flag 
     ipv6 nd autoconfig other-flag 
     bas
      access-type layer2-subscriber default-domain authentication huawei
      authentication-method-ipv6 bind
    #
    interface GigabitEthernet0/1/1.1            
     ipv6 enable  
     ipv6 address auto link-local                  
     ipv6 nd autoconfig managed-address-flag       
     ipv6 nd autoconfig other-flag                           
     user-vlan 2   
     remote-backup-profile p1                       
     bas          
      access-type layer2-subscriber default-domain authentication huawei   
      authentication-method-ipv6 bind
    #
    interface LoopBack1
     ip address 10.1.2.1 255.255.255.255
    #
    bfd bfd1 bind peer-ip 10.1.1.2
     discriminator local 8
     discriminator remote 6
    #
    ospf 1        
     import-route direct                           
     area 0.0.0.0 
     network 10.1.2.1 0.0.0.0
    #
    return
    #
    
    ```
  + BRAS 2 configuration file
    
    ```
    #
    sysname BRAS2
    #
    bfd
    #
    mpls
    #
    mpls ldp
    #
    ipv6 prefix prefix1 local
     prefix 2001:db8:1::2013/64
    #
    ipv6 pool pool1 bas local
     prefix prefix1
    #
    aaa
     domain huawei   
      authentication-scheme default0                    
      accounting-scheme default0                  
      ipv6-pool pool1
    #
    remote-backup-service s1
     peer 10.1.2.1 source 10.1.2.2 port 6001
     protect lsp-tunnel for-all-instance peer-ip 10.1.2.1
     track interface GigabitEthernet0/2/0
    #
    remote-backup-profile p1
     service-type bras
     backup-id 1 remote-backup-service s1
     peer-backup hot
     vrrp-id 1 interface GigabitEthernet0/1/0.2
     nas logic-port GigabitEthernet 0/1/0
     nas logic-sysname huawei
     nas logic-ip 1.1.1.1
    #
    interface GigabitEthernet0/1/0.2              
     vlan-type dot1q 1                             
     ip address 10.1.1.2 255.255.255.0           
     vrrp vrid 1 virtual-ip 10.1.1.100            
     admin-vrrp vrid 1                             
     vrrp vrid 1 priority 150                      
     vrrp vrid 1 track interface GigabitEthernet0/2/0 reduced 50                    
     vrrp vrid 1 track bfd-session session-name bfd1 peer
    #
    interface GigabitEthernet0/1/0.1        
     shutdown  
     ipv6 enable 
     ipv6 address auto link-local 
     ipv6 nd autoconfig managed-address-flag 
     ipv6 nd autoconfig other-flag 
     bas
      access-type layer2-subscriber default-domain authentication huawei
      authentication-method-ipv6 bind
    #
    interface GigabitEthernet0/1/1.1          
     ipv6 enable  
     ipv6 address auto link-local                  
     ipv6 nd autoconfig managed-address-flag       
     ipv6 nd autoconfig other-flag                            
     user-vlan 2   
     remote-backup-profile p1                 
     bas          
      access-type layer2-subscriber default-domain authentication huawei
      authentication-method-ipv6 bind
    #
    interface LoopBack1
     ip address 10.1.2.2 255.255.255.255
    #
    bfd bfd2 bind peer-ip 10.1.2.1                
     discriminator local 6                         
     discriminator remote 8                        
    #
    ospf 1
     import-route direct
     area 0.0.0.0
     network 10.1.2.2 0.0.0.0
    #
    return
    #
    ```