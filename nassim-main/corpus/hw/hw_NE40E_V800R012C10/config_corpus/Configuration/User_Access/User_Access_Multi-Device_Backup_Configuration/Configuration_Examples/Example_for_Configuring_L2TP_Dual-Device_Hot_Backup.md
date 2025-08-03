Example for Configuring L2TP Dual-Device Hot Backup
===================================================

This section provides an example for configuring L2TP dual-device hot backup on the LACs, including networking requirements, configuration roadmap, configuration procedure, and configuration files.

#### Networking Requirements

L2TP tunnels can be used to provide enterprise user access services and wholesale services. As these services are the major services that operators provide and have high user experience requirements, L2TP tunnels must support high reliability. In addition to BRAS user information backup, L2TP dual-device hot backup must be configured on the master and backup Routers for high reliability.

On the network shown in [Figure 1](#EN-US_TASK_0172374410__fig_dc_ne_cfg_rui_001201), users log in to LAC1 and LAC2 through a LAN switch (LSW). The two LACs run VRRP to determine the master/backup status. Basic user access functions are configured on the LACs so that the users go online through the master device. Each of LACs sets up an L2TP tunnel with the LNS. To allow rapid service restoration without the need of re-dialing up if a fault occurs on the access or network side, L2TP dual-device hot backup needs to be configured on LAC1 and LAC2.

**Figure 1** L2TP dual-device hot backup![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](images/dc_ne_cfg_rui_l2tp_sl_fig01.png)  

| Device Name | Interface Name | IP Address |
| --- | --- | --- |
| LAC1 | GE0/1/0.2 | 10.0.1.1/24 (IP address of the interface running VRRP) |
| LAC1 | GE0/2/0 | 10.0.2.1/24 |
| LAC1 | Loopback1 | 7.7.7.7/32 (source IP address for LAC1 to establish a tunnel) |
| LAC1 | Loopback2 | 8.8.8.8/32 (source IP address for LAC2 to establish a tunnel) |
| LAC1 | Loopback3 | 10.0.0.1/32 (IP address of the data backup channel between LACs) |
| LAC2 | GE0/1/0.2 | 10.0.1.2/24 (IP address of the interface running VRRP) |
| LAC2 | GE0/2/0 | 10.0.3.1/24 |
| LAC2 | Loopback1 | 7.7.7.7/32 (source IP address for LAC1 to establish a tunnel) |
| LAC2 | Loopback2 | 8.8.8.8/32 (source IP address for LAC2 to establish a tunnel) |
| LAC2 | Loopback3 | 10.0.0.2/32 (IP address of the data backup channel between LACs) |




#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure routes to ensure IP connectivity between devices and a routing policy on LAC1 and LAC2. For details, see *HUAWEI NE40E-M2 seriesUniversal Service Router Configuration Guide - IP Routing*.
2. Configure basic user access functions and ensure that the two LACs have the same configuration. For details, see *HUAWEI NE40E-M2 seriesUniversal Service Router Configuration Guide - User Access*.
3. Configure each of LACs to set up an L2TP tunnel with the LNS.
4. Establish a multi-node backup platform. Configure an RBS on the network side of LAC1 and LAC2. LAC1 is the master, and LAC2 is the backup device.
5. Configure a VRRP group on the access side of LAC1 and LAC2 to determine the master/backup status. Create a BFD session, and configure the VRRP group to track the BFD session.
6. Configure an RBP for backing up BRAS user information and L2TP services.
7. Bind the RBP to the interface from which users go online.
8. Enable automatic route advertisement.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This example provides the configuration of LAC1. The configuration of LAC2 is similar to the configuration of LAC1. For configuration details, see Configuration Files in this section.



#### Data Preparation

To complete the configuration, you need the following data:

* VRRP parameters such as a VRID and a preemption delay
* BFD parameters such as the local and remote discriminators and expected minimum interval at which BFD packets are sent and received
* Interface IP addresses of LAC1 and LAC2
* Backup ID, which is used together with an RBS to identify the RBP to which the users belong
* User access parameters
* L2TP group parameters such as an authentication password and an interval at which Hello packets are sent

#### Procedure

1. Assign an IP address to each loopback interface and configure a VT interface and a BAS interface.
   
   
   ```
   <Device> system-view
   [~Device] sysname LAC1
   [*Device] commit
   ```
   
   # Assign an IP address to a loopback interface directly connecting LAC1 to the LNS so that the route to the loopback interface can be advertised.
   
   ```
   [~LAC1] interface loopback1
   [*LAC1-loopback1] ip address 7.7.7.7 32
   [*LAC1-loopback1] commit
   [~LAC1-loopback1] quit
   ```
   
   # Assign an IP address to a loopback interface directly connecting LAC1 to the LAC2 so that the route to the loopback interface can be advertised.
   
   ```
   [~LAC1] interface loopback2
   [*LAC1-loopback2] ip address 8.8.8.8 32
   [*LAC1-loopback2] commit
   [~LAC1-loopback2] quit
   ```
   
   # Configure VT interface 1 on LAC1.
   
   ```
   [~LAC1] interface virtual-template 1
   [*LAC1-Virtual-Template1] ppp authentication-mode chap
   [*LAC1-Virtual-Template1] commit
   [~LAC1-Virtual-Template1] quit
   ```
   
   # Bind VT interface 1 to GE 0/1/0.1 and configure a user-side VLAN.
   
   ```
   [~LAC1] interface gigabitethernet 0/1/0.1
   [*LAC1-GigabitEthernet0/1/0.1] pppoe-server bind virtual-template 1
   [*LAC1-GigabitEthernet0/1/0.1] user-vlan 1 100
   [*LAC1-GigabitEthernet0/1/0.1] commit
   [*LAC1-GigabitEthernet0/1/0.1-vlan-1-100] quit
   ```
   
   # Configure a BAS interface.
   
   ```
   [~LAC1-GigabitEthernet0/1/0.1] bas
   [*LAC1-GigabitEthernet0/1/0.1-bas] access-type layer2-subscriber
   [*LAC1-GigabitEthernet0/1/0.1-bas] authentication-method ppp
   [*LAC1-GigabitEthernet0/1/0.1-bas] commit
   [~LAC1-GigabitEthernet0/1/0.1-bas] quit
   [~LAC1-GigabitEthernet0/1/0.1] quit
   ```
2. Set up an L2TP tunnel between LAC1 and the LNS.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In the dual-device hot backup scenario, run the [**set l2tp tunnel base-id**](cmdqueryname=set+l2tp+tunnel+base-id) *base-id* command on one of the LACs to set a base value for generating an L2TP tunnel ID. The other LAC uses the default base value 0. The settings ensure to a certain extent that tunnel IDs are unique on the devices that back up each other.
   
   # Assign an IP address to a loopback interface directly connecting LAC1 to the LNS so that the route to the loopback interface can be advertised.
   
   ```
   [~LAC1] interface gigabitethernet 0/2/0
   [*LAC1-GigabitEthernet0/2/0] ip address 10.0.2.1 255.255.255.0
   [*LAC1-GigabitEthernet0/2/0] commit
   [~LAC1-GigabitEthernet0/2/0] quit
   ```
   
   # Configure an L2TP group and its attributes.
   
   ```
   [~LAC1] l2tp enable
   [*LAC1] l2tp-group lac1
   [*LAC1-l2tp-lac1] tunnel name lac1
   [*LAC1-l2tp-lac1] start l2tp ip 3.3.3.3
   [*LAC1-l2tp-lac1] tunnel authentication
   [*LAC1-l2tp-lac1] tunnel password cipher YsHsjx_202206
   [*LAC1-l2tp-lac1] tunnel source loopback1 rui
   [*LAC1-l2tp-lac1] tunnel timer hello 200
   [*LAC1-l2tp-lac1] commit
   [~LAC1-l2tp-lac1] quit
   ```
   
   # Configure a RADIUS server group.
   
   ```
   [~LAC1] radius-server group radius1
   [*LAC1-radius-radius1] radius-server authentication 10.1.20.1 1812
   [*LAC1-radius-radius1] radius-server accounting 10.1.20.1 1813
   [*LAC1-radius-radius1] radius-server shared-key itellin
   [*LAC1-radius-radius1] commit
   [~LAC1-radius-radius1] quit
   ```
   
   # Configure a domain to which the users belong.
   
   ```
   [~LAC1] aaa
   [~LAC1-aaa] domain domain1
   [*LAC1-aaa-domain-domain1] l2tp-group lac1
   [*LAC1-aaa-domain-domain1] radius-server group radius1
   [*LAC1-aaa-domain-domain1] authentication-scheme default1
   [*LAC1-aaa-domain-domain1] accounting-scheme default1
   [*LAC1-aaa-domain-domain1] commit
   [~LAC1-aaa-domain-domain1] quit
   [~LAC1-aaa] quit
   ```
3. Configure a VRRP group on the access side of LAC1 and LAC2 to determine the master/backup status. Create a BFD session, and configure the VRRP group to track the BFD session.
   
   
   
   # Configure a VRRP-link-BFD session to rapidly detect faults in interfaces or links for triggering a master/backup VRRP switchover.
   
   ```
   [~LAC1] bfd
   [*LAC1-bfd] commit
   [~LAC1-bfd] bfd bfd-acc bind peer-ip 10.0.1.2
   [*LAC1-bfd-session-bfd-acc] discriminator local 1
   [*LAC1-bfd-session-bfd-acc] discriminator remote 1
   [*LAC1-bfd-session-bfd-acc] commit
   [~LAC1-bfd-session-bfd-acc] quit
   ```
   
   # Configure the interface (GE 0/1/0.2 in this example) bound to the VRRP group. Set the preemption delay of the master device in the VRRP group to 30 minutes.
   
   ```
   [~LAC1] interface gigabitethernet 0/1/0.2
   [*LAC1-GigabitEthernet0/1/0.2] vlan-type dot1q 200
   [*LAC1-GigabitEthernet0/1/0.2] ip address 10.0.1.1 255.255.255.0
   [*LAC1-GigabitEthernet0/1/0.2] vrrp vrid 1 virtual-ip 10.0.1.100
   [*LAC1-GigabitEthernet0/1/0.2] admin-vrrp vrid 1
   [*LAC1-GigabitEthernet0/1/0.2] vrrp vrid 1 priority 120
   [*LAC1-GigabitEthernet0/1/0.2] vrrp vrid 1 preempt-mode timer delay 1800
   [*LAC1-GigabitEthernet0/1/0.2] vrrp vrid 1 track interface gigabitethernet 0/2/0 reduced 50
   [*LAC1-GigabitEthernet0/1/0.2] vrrp recover-delay 20
   [*LAC1-GigabitEthernet0/1/0.2] commit
   [~LAC1-GigabitEthernet0/1/0.2] quit
   ```
4. Configure an RBS and an RBP.
   
   
   
   # Configure an IP address for the backup channel. The route needs to be advertised.
   
   ```
   [~LAC1] interface loopback3
   [*LAC1-loopback3] ip address 10.0.0.1 32
   [*LAC1-loopback3] commit
   [~LAC1-loopback3] quit
   ```
   
   # Configure an RBS.
   
   ```
   [~LAC1] remote-backup-service s1
   [*LAC1-rm-backup-srv-s1] peer 10.0.0.2 source 10.0.0.1 port 4500
   [*LAC1-rm-backup-srv-s1] l2tp-tunnel source loopback1
   [*LAC1-rm-backup-srv-s1] commit
   [~LAC1-rm-backup-srv-s1] quit
   ```
   
   # Configure an RBP for backing up BRAS user information and L2TP services.
   
   ```
   [~LAC1] remote-backup-profile p1
   [*LAC1-rm-backup-prf-p1] peer-backup hot
   [*LAC1-rm-backup-prf-p1] vrrp-id 1 interface gigabitethernet 0/1/0.2
   [*LAC1-rm-backup-prf-p1] backup-id 10 remote-backup-service s1
   [*LAC1-rm-backup-prf-p1] service-type bras
   [*LAC1-rm-backup-prf-p1] service-type l2tp
   [*LAC1-rm-backup-prf-p1] commit
   [~LAC1-rm-backup-prf-p1] quit
   ```
   
   # Bind the RBP to the interface from which users go online.
   
   ```
   [~LAC1] interface gigabitethernet 0/1/0.1
   [*LAC1-GigabitEthernet0/1/0.1] remote-backup-profile p1
   [*LAC1-GigabitEthernet0/1/0.1] commit
   [~LAC1-GigabitEthernet0/1/0.1] quit
   ```
5. Configure a policy to filter OSPF routes to be advertised.
   
   
   
   # Configure a policy to filter OSPF routes to be advertised on LAC1.
   
   ```
   [~LAC1] system-view
   [*LAC1-ospf-1] ospf 1
   [*LAC1-ospf-1] preference 100
   [*LAC1-ospf-1] default cost inherit-metric
   [*LAC1-ospf-1] import-route direct
   [*LAC1-ospf-1] area 0.0.0.0
   [*LAC1-ospf-1-area-0.0.0.0] network 10.0.0.0 0.0.0.255
   [*LAC1-ospf-1-area-0.0.0.0] network 10.0.2.0 0.0.0.255
   [*LAC1-ospf-1-area-0.0.0.0] network 10.0.3.0 0.0.0.255
   [*LAC1-ospf-1-area-0.0.0.0] commit
   ```
   
   
   
   # Configure automatic route advertisement.
   
   ```
   [~LAC1] peer-backup route-cost auto-advertising
   [*LAC1] commit
   ```
6. Verify the configuration.
   
   
   
   Run the **display vrrp** command to check the VRRP state of the devices. The command output shows that LAC1 is in the **Master** state, its BFD session is **UP**, the preemption delay is **1800**, and LAC2 is in the **Backup** state.
   
   ```
   <lac1> display vrrp
   ```
   ```
     Eth-Trunk1.2 | Virtual Router 1
       State : Master
       Virtual IP : 10.0.1.100
       Master IP : 10.0.1.1
       Local IP : 10.0.1.1
       PriorityRun : 120
       PriorityConfig : 120
       MasterPriority : 120
       Preempt : YES   Delay Time : 1800s
       Hold Multiplier : 4
       TimerRun : 5 s
       TimerConfig : 5 s
       Auth Type : NONE
       Virtual Mac : 00e0-fc12-3456
       Check TTL : YES
       Config type : admin-vrrp
       Track IF : GigabitEthernet0/2/0   Priority reduced : 100
       IF State : UP
       Create time : 2000-05-11 17:38:16
       Last change time : 2000-05-13 12:58:20    
   ```
   ```
   <lac2> display vrrp
   ```
   ```
   Eth-Trunk1.2 | Virtual Router 1
       State : Backup
       Virtual IP : 10.0.1.100
       Master IP : 10.0.1.1
       Local IP : 10.0.1.1
       PriorityRun : 100
       PriorityConfig : 100
       MasterPriority : 120
       Preempt : YES   Delay Time : 0s
       Hold Multiplier : 4
       TimerRun : 5 s
       TimerConfig : 5 s
       Auth Type : NONE
       Virtual Mac : 00e0-fc12-3456
       Check TTL : YES
       Config type : admin-vrrp
       Config track link-bfd down-number : 0
       Track BFD : 1  type: peer
       BFD-session state : UP
       Create time : 2011-08-02 16:13:43
       Last change time : 2011-08-04 12:01:58
   
   ```
   
   After successfully configuring L2TP dual-device hot backup, run the **display remote-backup-profile** command. The command output shows that the RBS type is **bras l2tp**, LAC1 is in the **Master** state, LAC2 is in the **Slave** state.
   
   ```
   <lac1> display remote-backup-profile p1
   ```
   ```
    -----------------------------------------------
    Profile-Index : 0x800
    Profile-Name : p1
    Service: bras l2tp
    Remote-backup-service : s1
    Backup-ID    : 10
    track protocol : VRRP
    VRRP-ID: 1
    VRRP-Interface : Gigabitethernet 0/1/0.2
    Interface    :
   Gigabitethernet 0/1/0.1
    State : Master
    Peer State    : Slave
    Backup mode : hot
    Slot-Number  : --
    Card-Number  : --
    Port-Number  : --
    Traffic threshold : --
    Traffic interval : 1(minutes)  
   ```
   ```
   <lac2> display remote-backup-profile p1
   ```
   ```
    -----------------------------------------------
    Profile-Index: 0x800
    Profile-Name : p1
    Service: bras l2tp
    Remote-backup-service: s1
    Backup-ID    : 10
    track protocol : VRRP
    VRRP-ID: 1
    VRRP-Interface : Gigabitethernet 0/1/0.2
    Interface    :
    Gigabitethernet 0/1/0.1
    State : Slave
    Peer State   : Master
    Backup mode  : hot
    Slot-Number  : --
    Card-Number  : --
    Port-Number  : --
    Traffic threshold    : --
    Traffic interval     : 1(minutes)
   ```

#### Configuration Files

* LAC1 configuration file
  
  ```
  #
  sysname LAC1
  #
  bfd
  #
  radius-server group radius1
   radius-server authentication 10.1.20.1 1812
   radius-server accounting 10.1.20.1 1813
   radius-server shared-key itellin
  # 
  aaa 
   local-user a password cipher %^%#knf^-3(!.J6L])YX0t>~M0[B*y7=d!y/iuOS@9-X%^%#   
   local-user a service-type ftp    
   local-user a ftp-directory cfcard: 
   local-user b password cipher %^%#s3=!HY9:#;<oNUWE%MO@SYnaFYKQ(.gD=[&>s*l"%^%#   
   local-user b service-type ftp    
   local-user c password cipher %^%#pAX[0k.N/"7!&E.8/W^OD-x//CRf'DHjM`9T%g:5%^%#   
   local-user c service-type ftp 
   authentication-scheme default1   
    authentication-mode radius local   
   #
   domain domain1    
    l2tp-group lac1
    radius-server group radius1
    authentication-scheme default1
    accounting-scheme default1
   # 
  remote-backup-service s1
   peer 10.0.0.2 source 10.0.0.1 port 4500
   l2tp-tunnel source loopback1
  #
  remote-backup-profile p1
   service-type bras
   service-type l2tp
   peer-backup hot
   vrrp-id 1 interface gigabitethernet 0/1/0.2
   backup-id 10 remote-backup-service s1
  #
  interface virtual-template 1
   ppp authentication-mode chap      
  #   
  interface GigabitEthernet 0/1/0.1
   pppoe-server bind virtual-template 1
   user-vlan 1 100
   remote-backup-profile p1
   #
   bas
    access-type layer2-subscriber
   #
  #
  interface gigabitethernet 0/1/0.2
   vlan-type dot1q 200
   ip address 10.0.1.1 255.255.255.0
   vrrp vrid 1 virtual-ip 10.0.1.100
   admin-vrrp vrid 1
   vrrp vrid 1 priority 120
   vrrp vrid 1 preempt-mode timer delay 1800
   vrrp vrid 1 track bfd-session 1 link
   vrrp vrid 1 track interface gigabitethernet 0/2/0 reduced 50
   vrrp recover-delay 20
  #  
  interface gigabitethernet 0/2/0
   ip address 10.0.2.1 255.255.255.0
   quit
  #
  interface LoopBack1
   ip address 7.7.7.7 255.255.255.255 
  #     
  interface LoopBack2 
   ip address 8.8.8.8 255.255.255.255 
  #
  interface LoopBack3
   ip address 10.0.0.1 255.255.255.255
  # 
  l2tp enable
  l2tp-group lac1
   tunnel name lac1
   start l2tp ip 3.3.3.3
   tunnel authentication
   tunnel password cipher %^%#pAX[0k.N/"7!&E.8/W^OD-x//CRf'DHjM`9T%g:5%^%#
   tunnel source loopback1 rui
   tunnel timer hello 200
  #
  bfd bfd-acc bind peer-ip 10.0.1.2
   discriminator local 1
   discriminator remote 1
   commit   
  #   
  ospf 1
   preference 100    
   default cost inherit-metric
   import-route direct
   area 0.0.0.0
    network 10.0.0.0 0.0.0.255  
    network 10.0.2.0 0.0.0.255 
    network 10.0.3.0 0.0.0.255    
  #   
  peer-backup route-cost auto-advertising
  #
  ```
* LAC2 configuration file
  
  ```
  #
  sysname LAC2
  #
  bfd
  #
  radius-server group radius1
   radius-server authentication 10.1.20.1 1812
   radius-server accounting 10.1.20.1 1813
   radius-server shared-key itellin
  #
  aaa 
   local-user a password cipher %^%#knf^-3(!.J6L])YX0t>~M0[B*y7=d!y/iuOS@9-X%^%#   
   local-user a service-type ftp    
   local-user a ftp-directory cfcard: 
   local-user b password cipher %^%#s3=!HY9:#;<oNUWE%MO@SYnaFYKQ(.gD=[&>s*l"%^%#   
   local-user b service-type ftp    
   local-user c password cipher %^%#pAX[0k.N/"7!&E.8/W^OD-x//CRf'DHjM`9T%g:5%^%#   
   local-user c service-type ftp 
   authentication-scheme default1   
    authentication-mode radius local   
   #
   domain domain1    
    l2tp-group lac1
    radius-server group radius1
    authentication-scheme default1
    accounting-scheme default1
   # 
  remote-backup-service s1
   peer 10.0.0.1 source 10.0.0.2 port 4500
   l2tp-tunnel source loopback2
  #
  remote-backup-profile p1
   service-type bras
   service-type l2tp
   peer-backup hot
   vrrp-id 1 interface gigabitethernet 0/1/0.2
   backup-id 10 remote-backup-service s1
  #
  interface virtual-template 1
   ppp authentication-mode chap      
  #   
  interface GigabitEthernet 0/1/0.1
   pppoe-server bind virtual-template 1
   user-vlan 1 100
   remote-backup-profile p1
   #
   bas
    access-type layer2-subscriber
   #
  #
  interface gigabitethernet 0/1/0.2
   vlan-type dot1q 200
   ip address 10.0.1.2 255.255.255.0
   vrrp vrid 1 virtual-ip 10.0.1.100
   admin-vrrp vrid 1
   vrrp vrid 1 preempt-mode timer delay 300
   vrrp vrid 1 track bfd-session 1 peer
  #  
  interface gigabitethernet 0/2/0
   ip address 10.0.2.2 255.255.255.0
   quit
  #
  interface LoopBack1
   ip address 7.7.7.7 255.255.255.255 
  #     
  interface LoopBack2 
   ip address 8.8.8.8 255.255.255.255 
  #
  interface LoopBack3
   ip address 10.0.0.2 255.255.255.255
  # 
  l2tp enable
  l2tp-group lac1
   tunnel name lac1
   start l2tp ip 3.3.3.3
   tunnel authentication
   tunnel password cipher %^%#pAX[0k.N/"7!&E.8/W^OD-x//CRf'DHjM`9T%g:5%^%#
   tunnel source loopback2 rui
   tunnel timer hello 0
  #
  bfd bfd-acc bind peer-ip 10.0.1.1
   discriminator local 1
   discriminator remote 1
   commit  
  #    
  ospf 1
    default cost inherit-metric
    import-route direct
   preference 100    
   area 0.0.0.0
    network 10.0.0.0 0.0.0.255  
    network 10.0.2.0 0.0.0.255 
    network 10.0.3.0 0.0.0.255    
  #   
  peer-backup route-cost auto-advertising
  #
  ```