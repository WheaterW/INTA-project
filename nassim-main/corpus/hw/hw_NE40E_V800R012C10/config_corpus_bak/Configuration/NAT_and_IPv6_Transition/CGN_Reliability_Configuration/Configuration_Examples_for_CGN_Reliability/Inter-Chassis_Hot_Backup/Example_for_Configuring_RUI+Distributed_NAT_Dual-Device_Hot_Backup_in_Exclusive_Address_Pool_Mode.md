Example for Configuring RUI+Distributed NAT Dual-Device Hot Backup in Exclusive Address Pool Mode
=================================================================================================

This section provides an example for configuring Redundancy User Information (RUI) and distributed network address translation (NAT) dual-device hot backup in exclusive address pool mode.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172362494__fig_01), in distributed deployment mode, a terminal user dials up through PPPoE, and BRAS1 and BRAS2 are interconnected through a switch. RUI is used to achieve user information backup in exclusive address pool mode. A NAT service board is deployed in slot 1 on BRAS1 and another NAT service board is deployed in slot 1 on BRAS2. A VRRP channel is established on the GE interfaces of BRAS1 and BRAS2. NAT inter-chassis hot backup is implemented on CPU 0 of the NAT service board in slot 1 on BRAS1 and CPU 0 of the NAT service board in slot 1 on BRAS2. The NAT service's master/backup status is determined by VRRP, and the service board status is associated with VRRP.

**Figure 1** Networking diagram for configuring distributed dual-device inter-chassis backup![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/1/1, GE 0/1/2, and GE 0/1/3, respectively.


  
![](images/fig_dc_ne_cgn-reliability_cfg_0003.png)

**Table 1** IP address plan
| Device Name | Interface Name | IP Address and Mask |
| --- | --- | --- |
| BRAS1 | GE0/1/1 | 10.1.1.1/24 |
| GE0/1/2.2 | 192.168.2.10/24 |
| GE0/1/3 | 10.12.1.0/24 |
| Loopback0 | 10.10.10.100/32 |
| BRAS2 | GE0/1/1 | 10.1.1.2/24 |
| GE0/1/2.2 | 192.168.2.100/24 |
| GE0/1/3 | 10.12.2.0/24 |
| Loopback0 | 99.99.99.99/32 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable HA hot backup on BRAS1 and BRAS2.
2. Configure a session table size for the NAT service board's CPU on BRAS1 and BRAS2.
3. Create a service-location group on BRAS1 and BRAS2, configure members for HA dual-device inter-chassis backup, and configure a VRRP channel.
4. Configure a VRRP group on BRAS1 and BRAS2.
5. Associate HA with VRRP on the direct-connect interfaces on the master and backup devices.
6. Bind the service-location group to the VRRP group on BRAS1 and BRAS2.
7. Create a service-instance group on BRAS1 and BRAS2 and bind them to the service-location group.
8. Create a NAT instance on BRAS1 and BRAS2 and bind it to the service-instance group and NAT address pool.
9. Configure a NAT conversion policy on BRAS1 and BRAS2.
10. Configure PPPoE user access and RADIUS authentication on the BRASs and bind the user groups to NAT instances.
11. Configure the route of the NAT address pool as a static blackhole route and advertise it to a routing protocol. Set the ID of an OSPF process to 1.
12. Configure a user-side VRRP group on BRAS1 and BRAS2 that are connected to the switch.
13. Establish a BFD session named **bfd** on BRAS1 and BRAS2 to quickly detect interface or link exceptions and trigger a master/backup VRRP switchover.
14. Configure RUI backup on BRAS1 and BRAS2 and back up BRAS user information in exclusive address pool mode.
15. Check BRAS user backup information.

#### Data Preparation

To complete the configuration, you need the following data:

* Index of a service-location group
* CPU IDs and slot IDs of the service boards on BRAS1 and BRAS2 (CPU 0 in slot 1 in this example)
* Interface and its IP address of a VRRP channel over the direct link between BRAS1 and BRAS2
* Index, virtual IP address, member priorities, and preemption delay of a VRRP group over the direct link
* Name of a service-instance group
* Index of a service-location group
* Index and name of a NAT instance, NAT address pool name, and address range
* ACL number, traffic classifier name, traffic behavior name, and traffic policy name of the NAT traffic conversion policy
* IPv4 address pool, IP address of the address pool gateway, and IP address segment allocated for user access
* User group name, user domain name, and AAA authentication scheme and accounting scheme
* Name and IP address of a RADIUS server group
* Remote backup identifier for RUI backup
* User-side interfaces and their IP addresses on BRAS1 and BRAS2
* Interface and its IP address of a user-side VRRP channel
* Index, virtual IP address, member priorities, and preemption delay of the user-side VRRP group


#### Procedure

1. Enable HA hot backup on the master and backup devices.
   
   
   
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
   [~BRAS1] service-ha hot-backup enable
   ```
   ```
   [*BRAS1] commit
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
   [~BRAS1] service-ha hot-backup enable
   ```
   ```
   [*BRAS1] commit
   ```
2. Configure a session table size for the NAT service board's CPU on BRAS1 and BRAS2.
   
   
   
   # Set the number of session tables supported by the NAT service board's CPU in slot 1 on BRAS1 to 6M.
   
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
   
   # Set the number of session tables supported by the NAT service board's CPU in slot 1 on BRAS2 to 6M.
   
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
   
   
   
   # On BRAS1, enter the view of GE 0/1/1, create VRRP group 1, and set the virtual IP address of the VRRP group to 10.1.1.3. Configure the VRRP group as an mVRRP group, and set BRAS1's priority in the VRRP group to 200, the VRRP preemption delay to 1500s, and the VRRP recovery delay to 15s.
   
   ```
   [~BRAS1] interface GigabitEthernet 0/1/1
   ```
   ```
   [~BRAS1-GigabitEthernet0/1/1] ip address 10.1.1.1 24
   ```
   ```
   [*BRAS1-GigabitEthernet0/1/1] vrrp vrid 1 virtual-ip 10.1.1.3
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
   [*BRAS1-GigabitEthernet0/1/1] vrrp recover-delay 15
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
   [~BRAS2-GigabitEthernet0/1/1] ip address 10.1.1.2 24
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
5. Associate HA with VRRP on the direct-connect interfaces on the master and backup devices.
   
   
   
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
       Preempt                  : YES    Delay Time      : 400 s  
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
       Preempt                 : YES   Delay Time       : 0 s  
       Hold Multiplier         : 4                                                                         
       TimerRun                : 1 s     
       TimerConfig             : 1 s   
       Auth Type               : NONE       
       Virtual MAC             : 00e0-fc12-3456   
       Check TTL               : YES          
       Config Type             : admin-vrrp   
       Backup-forward          : disabled    
       Fast-resume             : disabled
       Track Service-location  : 1   Priority Reduced : 60                                                     
       Service-location State  : UP 
       Create Time             : 2011-10-18 11:26:40 UTC+08:00   
       Last Change Time        : 2011-10-18 14:02:22 UTC+08:00
   ```
6. Bind the service-location group to the VRRP group on BRAS1 and BRAS2.
   
   
   
   # Bind service-location group 1 to VRRP group 1 on BRAS1.
   
   ```
   [~BRAS1] service-location 1
   ```
   ```
   [*BRAS1-service-location-1] vrrp vrid 1 interface GigabitEthernet 0/1/1
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
   [*BRAS2-service-location-1] vrrp vrid 1 interface GigabitEthernet 0/1/1
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
   
   # Run the [**display service-location 1**](cmdqueryname=display+service-location+1) command on BRAS1 and BRAS2 to view HA information. **Vrrp state** in the command output indicates the status of the service-location group, which must be consistent with the BRAS's VRRP status. **Batch-backup** **state** in the command output indicates whether batch backup is completed.
   
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
8. Create a NAT instance on BRAS1 and BRAS2 and bind it to the service-instance group and NAT address pool.
   
   
   
   # Create a NAT instance named **nat** on BRAS1, bind it to the service-instance group named **group1**, and configure the IP addresses in the NAT address pool to range from 11.11.11.100 to 11.11.11.105.
   
   ```
   [~BRAS1] nat instance nat id 1
   ```
   ```
   [*BRAS1-nat-instance-nat] service-instance-group group1
   ```
   ```
   [*BRAS1-nat-instance-nat] nat address-group address-group1 group-id 1 11.11.11.100 11.11.11.105
   ```
   ```
   [*BRAS1-nat-instance-nat] nat outbound any address-group address-group1
   ```
   ```
   [*BRAS1-nat-instance-nat] commit
   ```
   ```
   [~BRAS1-nat-instance-nat] quit
   ```
   
   # Create a NAT instance named **nat** on BRAS2, bind it to the service-instance group named **group1**, and configure the IP addresses in the NAT address pool to range from 11.11.11.100 to 11.11.11.105.
   
   ```
   [~BRAS2] nat instance nat id 1
   ```
   ```
   [*BRAS2-nat-instance-nat] service-instance-group group1
   ```
   ```
   [*BRAS2-nat-instance-nat] nat address-group address-group1 group-id 1 11.11.11.100 11.11.11.105
   ```
   ```
   [*BRAS2-nat-instance-nat] nat outbound any address-group address-group1
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
    nat address-group address-group1 group-id 1 11.11.11.100 11.11.11.105                                                                     
    nat outbound any address-group address-group1
   ```
   ```
   [~BRAS2] display nat instance nat
   ```
   ```
   nat instance nat id 1                                                                                                               
    service-instance-group group1                                                                                                        
    nat address-group address-group1 group-id 1 11.11.11.100 11.11.11.105                                                                     
    nat outbound any address-group address-group1
   ```
9. Configure PPPoE user access on BRAS1 and BRAS2 and bind the user group to the NAT instance.
   
   
   
   For details about how to configure a user group and IP address pool in a domain, see [Configuring PPPoE Access](dc_ne_pppoe_cfg_0004.html) in *HUAWEI NE40E-M2 series User Access-PPPoE Access Configuration*.
   
   # On BRAS1, configure user information (user group named **natbras**, IP address pool named **natbras**, user domain named **natbras**, and AAA) and bind the user group to the NAT instance named **nat**.
   1. Configure VT 1.
      
      ```
      [~BRAS1] interface virtual-template 1
      ```
      ```
      [*BRAS1-Virtual-Template1] ppp authentication-mode chap
      ```
      ```
      [*BRAS1-Virtual-Template1] commit
      ```
      ```
      [~BRAS1-Virtual-Template1] quit
      ```
   2. Configure the authentication scheme named **auth1** and the accounting scheme named **acct1**.
      
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
      [*BRAS1-aaa-authen-auth1] quit
      ```
      ```
      [*BRAS1-aaa] accounting-scheme acct1
      ```
      ```
      [*BRAS1-aaa-accounting-acct1] accounting-mode radius
      ```
      ```
      [*BRAS1-aaa-accounting-acct1] quit
      ```
   3. Configure a RADIUS server group named **rd1**.
      
      ```
      [~BRAS1] radius-server group rd1
      ```
      ```
      [*BRAS1-radius-rd1] radius-server authentication 192.168.7.249 1645
      ```
      ```
      [*BRAS1-radius-rd1] radius-server accounting 192.168.7.249 1646
      ```
      ```
      [*BRAS1-radius-rd1] radius-server type plus11
      ```
      ```
      [*BRAS1-radius-rd1] radius-server shared-key-cipher YsHsjx_202206 
      ```
      ```
      [*BRAS1-radius-rd1] commit
      ```
      ```
      [~BRAS1-radius-rd1] quit
      ```
   4. Configure an address pool named **natbras** for users to go online.
      
      ```
      [~BRAS1] ip pool natbras bas local
      ```
      ```
      [*BRAS1-ip-pool-natbras] gateway 192.168.0.1 255.255.255.0
      ```
      ```
      [*BRAS1-ip-pool-natbras] section 0 192.168.0.2 192.168.0.254
      ```
      ```
      [*BRAS1-ip-pool-natbras] commit
      ```
      ```
      [~BRAS1-ip-pool-natbras] quit
      ```
   5. Configure a user group named **natbras**.
      
      ```
      [~BRAS1] user-group natbras
      ```
      ```
      [*BRAS1] commit
      ```
   6. Configure a user domain named **natbras** and bind it to the NAT instance named **nat**.
      
      ```
      [~BRAS1] aaa
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
      [*BRAS1-aaa-domain-natbras] ip-pool natbras
      ```
      ```
      [*BRAS1-aaa-domain-natbras] user-group natbras bind nat instance nat
      ```
      ```
      [*BRAS1-aaa-domain-natbras] quit
      ```
      ```
      [*BRAS1-aaa] commit
      ```
      ```
      [~BRAS1-aaa] quit
      ```
   7. Configure a VLAN for the user-side sub-interface GE 0/1/2.10, specify a VT interface for the sub-interface, and configure the BAS interface.
      
      ```
      [~BRAS1] interface GigabitEthernet0/1/2.10
      ```
      ```
      [~BRAS1-GigabitEthernet0/1/2.10] user-vlan 2010
      ```
      ```
      [~BRAS1-GigabitEthernet0/1/2.10-vlan-2010-2010] quit
      ```
      ```
      [~BRAS1-GigabitEthernet0/1/2.10] pppoe-server bind virtual-template 1
      ```
      ```
      [*BRAS1-GigabitEthernet0/1/2.10] commit
      ```
      ```
      [~BRAS1-GigabitEthernet0/1/2.10] bas
      ```
      ```
      [*BRAS1-GigabitEthernet0/1/2.10-bas] access-type layer2-subscriber default-domain authentication natbras
      ```
      ```
      [*BRAS1-GigabitEthernet0/1/2.10-bas] authentication-method ppp
      ```
      ```
      [*BRAS1-GigabitEthernet0/1/2.10-bas] commit
      ```
      ```
      [~BRAS1-GigabitEthernet0/1/2.10-bas] quit
      ```
      ```
      [~BRAS1-GigabitEthernet0/1/2.10] quit
      ```![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The configuration of BRAS2 is similar to that of BRAS1. For configuration details, see [BRAS2 configuration file](#EN-US_TASK_0172362494__config_02) in this section.
10. Configure a NAT policy on BRAS1 and BRAS2.
    
    
    
    # Configure a traffic classification rule, NAT behavior, and a NAT traffic policy on BRAS1. Then apply the NAT traffic policy.
    
    1. Configure an ACL numbered 6001 and an ACL rule numbered 1.
       
       ```
       [~BRAS1] acl 6001
       ```
       ```
       [*BRAS1-ucl-6001] rule 1 permit ip source user-group natbras
       ```
       ```
       [*BRAS1-ucl-6001] commit
       ```
       ```
       [~BRAS1-ucl-6001] quit
       ```
    2. Configure a traffic classifier.
       
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
    3. Configure a traffic behavior.
       
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
    4. Define a NAT traffic policy to associate the traffic classifier with the traffic behavior.
       
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
    5. Apply the NAT traffic diversion policy in the system view.
       
       ```
       [~BRAS1] traffic-policy p1 inbound
       ```
       ```
       [*BRAS1] commit
       ```![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    The configuration of BRAS2 is similar to that of BRAS1. For configuration details, see [BRAS2 configuration file](#EN-US_TASK_0172362494__config_02) in this section.
11. Configure the route of the NAT address pool as a static blackhole route and advertise it to a routing protocol. Set the ID of an OSPF process to 1. OSPF is used as an IGP to advertise routes.
    
    
    
    # Configure BRAS1.
    
    ```
    [~BRAS1] ip route-static 11.11.11.0 27 null 0
    ```
    ```
    [*BRAS1] commit
    ```
    ```
    [~BRAS1] ospf 1
    ```
    ```
    [*BRAS1-ospf-1] import-route static
    ```
    ```
    [*BRAS1-ospf-1] commit
    ```
    ```
    [~BRAS1-ospf-1] quit
    ```
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    The configuration of BRAS2 is similar to that of BRAS1. For configuration details, see [BRAS2 configuration file](#EN-US_TASK_0172362494__config_02).
12. On each of the master and backup devices, configure a user-side VRRP group (between BRAS1/BRAS2 and SWITCH) and enable it to track the service-location group. If the service-location group is not tracked, a CGN board failure cannot trigger a master/backup BRAS switchover. As a result, new distributed NAT users cannot go online.
    
    
    
    # On BRAS1, enter the view of GE 0/1/2.2, create VRRP group 2, and set the virtual IP address of the VRRP group to 192.168.2.200. Configure the VRRP group as an mVRRP group, set BRAS1's priority in the VRRP group to 150 and the VRRP preemption delay to 1500s, and associate the VRRP group with service-location group 1.
    
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
    [*BRAS1-GigabitEthernet0/1/2.2] vrrp vrid 2 track service-location 1 reduced 50
    ```
    ```
    [*BRAS1-GigabitEthernet0/1/2.2] commit
    ```
    ```
    [~BRAS1-GigabitEthernet0/1/2.2] quit
    ```
    
    # On BRAS2, enter the view of GE 0/1/2.2, create VRRP group 2, and set the virtual IP address of the VRRP group to 192.168.2.200. Configure the VRRP group as an mVRRP group, set BRAS1's priority in the VRRP group to 120, and associate the VRRP group with service-location group 1.
    
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
    [*BRAS2-GigabitEthernet0/1/2.2] vrrp vrid 2 track service-location 1 reduced 50
    ```
    ```
    [*BRAS2-GigabitEthernet0/1/2.2] commit
    ```
    ```
    [~BRAS2-GigabitEthernet0/1/2.2] quit
    ```
13. Establish a BFD session named **bfd** on BRAS1 and BRAS2 to quickly detect interface or link exceptions and trigger a master/backup VRRP switchover.
    
    
    
    # Configure a BFD session on BRAS1 and associate a VRRP group with the BFD session.
    
    1. Establish a BFD session named **bfd** at the access side to rapidly detect interface or link faults and trigger a master/backup VRRP switchover. The IP address of GE 0/1/2.2 on BRAS2 is 192.168.2.100.
       
       ```
       [~BRAS1] bfd
       ```
       ```
       [~BRAS1-bfd] quit
       ```
       ```
       [*BRAS1] bfd bfd bind peer-ip 192.168.2.100
       ```
       ```
       [*BRAS1-bfd-session-bfd] discriminator local 100
       ```
       ```
       [*BRAS1-bfd-session-bfd] discriminator remote 200
       ```
       ```
       [*BRAS1-bfd-session-bfd] commit
       ```
       ```
       [*BRAS1-bfd-session-bfd] quit
       ```
    2. On GE 0/1/2.2, associate the VRRP group with the BFD session.
       
       ```
       [~BRAS1] interface GigabitEthernet0/1/2.2
       ```
       ```
       [~BRAS1-GigabitEthernet0/1/2.2] vrrp vrid 2 track bfd-session 100 peer
       ```
       ```
       [~BRAS1-GigabitEthernet0/1/2.2] commit
       ```
       ```
       [~BRAS1-GigabitEthernet0/1/2.2] quit
       ```
    
    # Configure a BFD session on BRAS2 and associate a VRRP group with the BFD session.
    
    1. Establish a BFD session named **bfd** at the access side to rapidly detect interface or link faults and trigger a master/backup VRRP switchover. The IP address of GE 0/1/2.2 on BRAS2 is 192.168.2.100.
       
       ```
       [~BRAS2] bfd
       ```
       ```
       [~BRAS2-bfd] quit
       ```
       ```
       [*BRAS2] bfd bfd bind peer-ip 192.168.2.10
       ```
       ```
       [*BRAS2-bfd-session-bfd] discriminator local 200
       ```
       ```
       [*BRAS2-bfd-session-bfd] discriminator remote 100
       ```
       ```
       [*BRAS2-bfd-session-bfd] commit
       ```
       ```
       [*BRAS2-bfd-session-bfd] quit
       ```
    2. On GE 0/1/2.2, associate the VRRP group with the BFD session.
       
       ```
       [~BRAS2] interface GigabitEthernet0/1/2.2
       ```
       ```
       [~BRAS2-GigabitEthernet0/1/2.2] vrrp vrid 2 track bfd-session 200 peer
       ```
       ```
       [~BRAS2-GigabitEthernet0/1/2.2] commit
       ```
       ```
       [~BRAS2-GigabitEthernet0/1/2.2] quit
       ```
14. Configure RUI backup on BRAS1 and BRAS2 and back up BRAS user information in exclusive address pool mode.
    1. Configure an RBS on BRAS1 and BRAS2.
       
       
       
       # Configure an RBS named **natbras** on BRAS1.
       
       ```
       [~BRAS1] remote-backup-service natbras
       ```
       ```
       [*BRAS1-rm-backup-srv-natbras] peer 10.1.1.2 source 10.1.1.1 port 7000
       ```
       ```
       [*BRAS1-rm-backup-srv-natbras] track interface gigabitethernet0/1/1
       ```
       ```
       [*BRAS1-rm-backup-srv-natbras] commit
       ```
       ```
       [~BRAS1-rm-backup-srv-natbras] quit
       ```
       
       # Configure an RBS named **natbras** on BRAS2.
       
       ```
       [~BRAS2] remote-backup-service natbras
       ```
       ```
       [*BRAS2-rm-backup-srv-natbras] peer 10.1.1.1 source 10.1.1.2 port 7000
       ```
       ```
       [*BRAS2-rm-backup-srv-natbras] track interface GigabitEthernet0/1/1
       ```
       ```
       [*BRAS2-rm-backup-srv-natbras] commit
       ```
       ```
       [~BRAS2-rm-backup-srv-natbras] quit
       ```
    2. Configure a remote backup profile (RBP) named **natbras** on each of BRAS1 and BRAS2.
       
       
       
       # Configure an RBS named **natbras** on BRAS1 and enable BRAS user backup.
       
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
       [*BRAS1-rm-backup-prf-natbras] ip-pool natbras
       ```
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       The configuration of BRAS2 is similar to that of BRAS1. For configuration details, see [BRAS2 configuration file](#EN-US_TASK_0172362494__config_02) in this section.
    3. On BRAS1 and BRAS2, configure NAS parameters and the traffic backup interval in the RBS view.
       
       
       
       # On BRAS1, configure the logical IP address of NAS as 1.2.3.4, the logical interface as GE 0/1/2, logical host name as **huawei**, and the user traffic backup interval as 10 minutes.
       
       ```
       [*BRAS1-rm-backup-prf-natbras] nas logic-ip 1.2.3.4
       ```
       ```
       [*BRAS1-rm-backup-prf-natbras] nas logic-port GigabitEthernet 0/1/2
       ```
       ```
       [*BRAS1-rm-backup-prf-natbras] nas logic-sysname huawei
       ```
       ```
       [*BRAS1-rm-backup-prf-natbras] traffic backup interval 10
       ```
       ```
       [*BRAS1-rm-backup-prf-natbras] commit
       ```
       ```
       [~BRAS1-rm-backup-prf-natbras] quit
       ```
       
       # On BRAS2, configure the logical IP address of NAS as 1.2.3.4, the logical interface as GE 0/1/2, logical host name as **huawei**, and the user traffic backup interval as 10 minutes.
       
       ```
       [*BRAS2-rm-backup-prf-natbras] nas logic-ip 1.2.3.4
       ```
       ```
       [*BRAS2-rm-backup-prf-natbras] nas logic-port GigabitEthernet 0/1/2
       ```
       ```
       [*BRAS2-rm-backup-prf-natbras] nas logic-sysname huawei
       ```
       ```
       [*BRAS2-rm-backup-prf-natbras] traffic backup interval 10
       ```
       ```
       [*BRAS2-rm-backup-prf-natbras] commit
       ```
       ```
       [~BRAS2-rm-backup-prf-natbras] quit
       ```
    4. Configure the user-side sub-interface on BRAS1 and BRAS2 and bind the sub-interface to an RBP.
       
       
       
       # On BRAS1, configure GE 0/1/2.10 as the user-side sub-interface and bind the sub-interface to the RBP named **natbras**.
       
       ```
       [~BRAS1] interface GigabitEthernet0/1/2.10
       ```
       ```
       [*BRAS1-GigabitEthernet0/1/2.10] remote-backup-profile natbras
       ```
       ```
       [*BRAS1-GigabitEthernet0/1/2.10] commit
       ```
       ```
       [~BRAS1-GigabitEthernet0/1/2.10] quit
       ```
    5. Configure routes to be advertised by OSPF.
       
       
       ```
       [~BRAS1] peer-backup route-cost auto-advertising
       ```
       ```
       [*BRAS1] commit
       ```
       ```
       [~BRAS1] ospf 1
       ```
       ```
       [~BRAS1-ospf-1] default cost 10 tag 100 type 2
       ```
       ```
       [*BRAS1-ospf-1] import-route unr
       ```
       ```
       [*BRAS1-ospf-1] commit
       ```
       ```
       [~BRAS1-ospf-1] quit
       ```
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       The configuration of BRAS2 is similar to that of BRAS1. For configuration details, see [BRAS2 configuration file](#EN-US_TASK_0172362494__config_02) in this section.
15. Check the configuration result of BRAS user information backup.
    
    
    
    # After successfully configuring the RBP, run the **display remote-backup-profile** command. The RBS type is **bras**. The RBP named **natbras** is bound to GE 0/1/2.10 from which users attempt to get online. BRAS1 is in the **Master** state, and the TCP connection is in the **Connected** state.
    
    ```
    [~BRAS1] display remote-backup-profile natbras
    -----------------------------------------------
     Profile-Index        : 0x802
     Profile-Name         : natbras
     Service              : bras
     Remote-backup-service: natbras
     Backup-ID            : 10
     track protocol       : VRRP
     VRRP-ID              : 1
     VRRP-Interface       : GigabitEthernet0/1/2.2
     State           	 : Master
     Peer-state      	 : Slave
     Backup mode          : hot
     Slot-Number          : 1
     Card-Number          : 0
     Port-Number          : 0
     Nas logic-port       : Gigabitethernet 0/1/2
     Nas logic-ip         : 1.2.3.4
     Nas logic-sysname    : huawei
     Traffic interval     : 10(minutes)
    ```
    ```
    [~BRAS1] display remote-backup-service natbras
    ----------------------------------------------------------
     Service-Index    : 0
     Service-Name     : natbras
     TCP-State        : Connected
     Peer-ip          : 10.1.1.2
     Source-ip        : 10.1.1.1
     TCP-Port         : 7000
     Track-BFD        : --
     Track-interface0 : GigabitEthernet0/1/1
     Track-interface1 : --
     Last up time     : 2016-06-02 16:15:8 
     Last down time   : 2016-06-02 16:3:36 
     Last down reason : TCP closed for packet error. 
    --------------------------------------------------------
    ```
    
    # After the user goes online, check user backup information.
    
    ```
    [~BRAS1] display backup-user
    ```
    ```
      Remote-backup-service: natbras
      Total Users Number: 10
    ------------------------------------------------------------------------
     100     101     102     103     104     105     106     107     108     109
    ------------------------------------------------------------------------
    
    ```
    
    # Display information about the online user on the specified interface.
    
    ```
    [~BRAS1] display access-user interface GigabitEthernet 0/1/2.10
    ```
    ```
    ------------------------------------------------------------------------------
      UserID  Username                Interface      IP address       MAC          IPv6 address
      ------------------------------------------------------------------------------
      --------------------------------------------------------------------------
      100      user@lsh                GE0/1/2.10      192.168.0.10         00e0-fc12-0101          -
      101      user@lsh                GE0/1/2.10      192.168.0.9          00e0-fc12-0102          -
      102      user@lsh                GE0/1/2.10      192.168.0.8          00e0-fc12-0103          -
      103      user@lsh                GE0/1/2.10      192.168.0.7          00e0-fc12-0104          -
      104      user@lsh                GE0/1/2.10      192.168.0.6          00e0-fc12-0105          -
      105      user@lsh                GE0/1/2.10      192.168.0.5          00e0-fc12-0106          -
      106      user@lsh                GE0/1/2.10      192.168.0.4          00e0-fc12-0107          -
      107      user@lsh                GE0/1/2.10      192.168.0.3          00e0-fc12-0108          -
      108      user@lsh                GE0/1/2.10      192.168.0.2          00e0-fc12-0109          -
      109      user@lsh                GE0/1/2.10      192.168.0.11         00e0-fc12-0110          -
      --------------------------------------------------------------------------
      Total users                        : 10
    ```

#### Configuration Files

* BRAS1 configuration file
  
  ```
  #
  sysname BRAS1
  #
  vsm on-board-mode disable
  #
  ip route-static 11.11.11.0 27 null 0
  #
  peer-backup route-cost auto-advertising
  #
  ospf 1
   import-route static
   default cost 10 tag 100 type 2
   import-route unr
  #
  bfd
  #
  bfd bfd bind peer-ip 192.168.2.100
   discriminator local 100
   discriminator remote 200
  #
  license
   active nat session-table size 6 slot 1 
   active nat bandwidth-enhance 40 slot 1
  #
  radius-server group rd1
   radius-server authentication 192.168.7.249 1645
   radius-server accounting 192.168.7.249 1646
   radius-server shared-key %^%#x*CgITP4C~;q,*+DEW'JBWe#)"Q&|7bX]b:Y<{w'%^%#
   radius-server type plus11
  #
  interface Virtual-Template1
   ppp authentication-mode chap
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
  #
  nat instance nat id 1
   service-instance-group group1
   nat address-group address-group1 group-id 1 11.11.11.100 11.11.11.105
   nat outbound any address-group address-group1
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   vrrp vrid 1 virtual-ip 10.1.1.3
   admin-vrrp vrid 1 ignore-if-down
   vrrp vrid 1 priority 200
   vrrp vrid 1 preempt-mode timer delay 1500
   vrrp vrid 1 track service-location 1 reduced 60
  #
  user-group natbras
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
   track interface gigabitethernet0/1/1
  #
  remote-backup-profile natbras
   service-type bras
   backup-id 10 remote-backup-service natbras
   peer-backup hot
   vrrp-id 2 interface GigabitEthernet0/1/2.2
   ip-pool natbras
   nas logic-ip 1.2.3.4
   nas logic-port GigabitEthernet0/1/2
   nas logic-sysname huawei
   traffic backup interval 10
  #
  interface GigabitEthernet0/1/2.10
   user-vlan 2010
   pppoe-server bind virtual-template 1
   remote-backup-profile natbras
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
   vrrp vrid 2 track service-location 1 reduced 50
   vrrp vrid 2 track bfd-session 100 peer
   vrrp recover-delay 15
  #
  interface loopback0
   ip address 10.10.10.100 255.255.255.255
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
  ip route-static 11.11.11.0 27 null 0
  #
  peer-backup route-cost auto-advertising
  #
  ospf 1
   import-route static
   default cost 10 tag 100 type 2
   import-route unr
  #
  bfd
  #
  bfd bfd bind peer-ip 192.168.2.10
   discriminator local 200
   discriminator remote 100
  #
  interface GigabitEthernet0/1/2.2
   vrrp vrid 2 track bfd-session 200 peer
  #
  license
   active nat session-table size 6 slot 1 
   active nat bandwidth-enhance 40 slot 1
  #
  radius-server group rd1
   radius-server authentication 192.168.7.249 1645
   radius-server accounting 192.168.7.249 1646
   radius-server shared-key %^%#x*CgITP4C~;q,*+DEW'JBWe#)"Q&|7bX]b:Y<{w'%^%#
   radius-server type plus11
  #
  interface Virtual-Template1
   ppp authentication-mode chap
  #nas logic-sysname huawei
  service-ha hot-backup enable
  #
  service-location 1
   location slot 1 
   vrrp vrid 1 interface GigabitEthernet 0/1/1
   remote-backup interface GigabitEthernet 0/1/1 peer 10.1.1.1
  #
  service-instance-group group1
   service-location 1
  #
  nat instance nat id 1
   service-instance-group group1
   nat address-group address-group1 group-id 1 11.11.11.100 11.11.11.105
   nat outbound any address-group address-group1
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
  user-group natbras
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
   track interface GigabitEthernet0/1/1
  #
  remote-backup-profile natbras
   service-type bras
   backup-id 10 remote-backup-service natbras
   peer-backup hot
   vrrp-id 2 interface GigabitEthernet0/1/2.2
   ip-pool natbras
   nas logic-ip 1.2.3.4
   nas logic-port GigabitEthernet0/1/2
   nas logic-sysname huawei
   traffic backup interval 10
  #
  interface GigabitEthernet0/1/2.10
   user-vlan 2010
   pppoe-server bind virtual-template 1
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
   vrrp vrid 2 track service-location 1 reduced 50
  #
  interface loopback0
   ip address 99.99.99.99 255.255.255.255
  #
  return
  ```