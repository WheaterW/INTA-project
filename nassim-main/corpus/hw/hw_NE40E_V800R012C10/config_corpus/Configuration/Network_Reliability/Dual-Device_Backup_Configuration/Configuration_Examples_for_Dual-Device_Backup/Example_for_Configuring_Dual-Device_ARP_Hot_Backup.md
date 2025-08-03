Example for Configuring Dual-Device ARP Hot Backup
==================================================

This section provides an example for configuring dual-device ARP hot backup in a VRRP group. With dual-device ARP hot backup deployed, after a master/backup switchover is performed, the new master device forwards downlink traffic without needing to relearn ARP entries, ensuring downlink traffic continuity.

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0172362259__fig125654388184), users access Device A and Device B through a LAN switch (LSW). Configure a Virtual Router Redundancy Protocol (VRRP) group on Device A and Device B. Device A is a master device, and Device B is a backup device. In normal circumstances, Device A learns ARP entries from the users and periodically updates them, and forwards both uplink and downlink traffic.

If Device A or the link between Device A and the switch fails, a master/backup VRRP switchover is triggered to switch Device B to the Master state. Device B needs to advertise a network segment route to network-side devices so that the devices will transmit downlink traffic to Device B. If Device B has not learned ARP entries from user-side devices, the downlink traffic is interrupted. Device B forwards the downlink traffic only after it learns ARP entries from user-side devices.

**Figure 1** Dual-device ARP hot backup networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent Device A's GE 0/1/0 and Device B's GE 0/1/0, respectively.


  
![](images/fig_dc_vrp_rbs_cfg_001101.png)  

To ensure downlink traffic continuity, deploy dual-device ARP hot backup on Device A and Device B to enable Device A to back up ARP entries and host routing information to Device B in real time. After a master/backup VRRP switchover is performed, Device B forwards downlink traffic without needing to relearn ARP entries.


#### Data Preparation

To complete the configuration, you need the following data:

* VRRP group ID: 1; virtual IP address: 10.1.1.100
* Device A's priority: 120; Device B's priority: 100 (default value)
* Device A's and Device B's preemption delays: 600 seconds
* Remote backup service (RBS) name: service1; remote backup profile (RBP) name: profile1; backup ID: 10
* Device A's IP address: 1.1.1.1/32; Device B's IP address: 2.2.2.2/32; TCP port number: 2046

#### Procedure

1. Assign IP addresses to Device A's and Device B's interfaces and configure OSPF on Device A and Device B. For detailed configurations, see Configuration Files.
2. Configure basic VRRP group functions.
   
   # Create VRRP group 1 on Device A, and set Device A's priority and preemption delay to 120 and 600 seconds, respectively.
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceA
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] vrrp vrid 1 virtual-ip 10.1.1.100
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] admin-vrrp vrid 1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] vrrp vrid 1 priority 120
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] vrrp vrid 1 preempt-mode timer delay 600
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] vrrp recover-delay 20
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] quit
   ```
   
   # Create VRRP group 1 on Device B, set Device B's preemption delay to 600 seconds, and retain the default priority for Device B.
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceB
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceB] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] vrrp vrid 1 virtual-ip 10.1.1.100
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] admin-vrrp vrid 1
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] vrrp vrid 1 preempt-mode timer delay 600
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] vrrp recover-delay 20
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] quit
   ```
3. Establish a dual-device backup platform.
   
   # Establish a dual-device backup platform on Device A.
   1. Configure an SSL policy.
      ```
      [~DeviceA] pki domain domain1
      ```
      ```
      [*DeviceA-pki-domain-domain1] commit
      ```
      ```
      [~DeviceA-pki-domain-domain1] quit
      ```
      ```
      [~DeviceA] pki import-certificate ca domain domain1 filename test.crt
      ```
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      The following uses CA certificate as an example. During the actual configuration, you need to replace **ca** and **test.crt** with the existing certificate type and name on the device. The user can directly upload the certificate to the device for installation, or apply for and download the certificate for installation. For details, see "Obtaining a Certificate" in *PKI Configuration*.
      
      ```
      [*DeviceA] ssl policy policy1
      ```
      ```
      [*DeviceA-ssl-policy-policy1] pki-domain domain1
      ```
      ```
      [*DeviceA-ssl-policy-policy1] commit
      ```
      ```
      [~DeviceA-ssl-policy-policy1] quit
      ```
   2. Configure an RBS.
      ```
      [~DeviceA] remote-backup-service service1
      ```
      ```
      [*DeviceA-rm-backup-srv-service1] bind ssl-policy policy1
      ```
      ```
      [*DeviceA-rm-backup-srv-service1] batch-backup service-type arp now
      ```
      ```
      [*DeviceA-rm-backup-srv-service1] peer 2.2.2.2 source 1.1.1.1 port 2046
      ```
      ```
      [*DeviceA-rm-backup-srv-service1] commit
      ```
      ```
      [~DeviceA-rm-backup-srv-service1] quit
      ```
   3. Configure an RBP.
      ```
      [~DeviceA] remote-backup-profile profile1
      ```
      ```
      [*DeviceA-rm-backup-prf-profile1] peer-backup hot
      ```
      ```
      [*DeviceA-rm-backup-prf-profile1] vrrp-id 1 interface gigabitethernet 0/1/0
      ```
      ```
      [*DeviceA-rm-backup-prf-profile1] vrrp vrid 1 authentication-mode md5 YsH_2022
      ```
      ```
      [*DeviceA-rm-backup-prf-profile1] backup-id 10 remote-backup-service service1
      ```
      ```
      [*DeviceA-rm-backup-prf-profile1] commit
      ```
      ```
      [~DeviceA-rm-backup-prf-profile1] quit
      ```
   # Establish a dual-device backup platform on Device B.
   1. Configure an SSL policy.
      ```
      [~DeviceB] pki domain domain1
      ```
      ```
      [*DeviceB-pki-domain-domain1] commit
      ```
      ```
      [~DeviceB-pki-domain-domain1] quit
      ```
      ```
      [~DeviceB] pki import-certificate ca domain domain1 filename test.crt
      ```
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      The following uses CA certificate as an example. During the actual configuration, you need to replace **ca** and **test.crt** with the existing certificate type and name on the device. The user can directly upload the certificate to the device for installation, or apply for and download the certificate for installation. For details, see "Obtaining a Certificate" in *PKI Configuration*.
      
      ```
      [*DeviceB] ssl policy policy1
      ```
      ```
      [*DeviceB-ssl-policy-policy1] pki-domain domain1
      ```
      ```
      [*DeviceB-ssl-policy-policy1] commit
      ```
      ```
      [~DeviceB-ssl-policy-policy1] quit
      ```
   2. Configure an RBS.
      ```
      [~DeviceB] remote-backup-service service1
      ```
      ```
      [*DeviceB-rm-backup-srv-service1] bind ssl-policy policy1
      ```
      ```
      [*DeviceB-rm-backup-srv-service1] peer 1.1.1.1 source 2.2.2.2 port 2046
      ```
      ```
      [*DeviceB-rm-backup-srv-service1] batch-backup service-type arp now
      ```
      ```
      [*DeviceB-rm-backup-srv-service1] commit
      ```
      ```
      [~DeviceB-rm-backup-srv-service1] quit
      ```
   3. Configure an RBP.
      ```
      [~DeviceB] remote-backup-profile profile1
      ```
      ```
      [*DeviceB-rm-backup-prf-profile1] peer-backup hot
      ```
      ```
      [*DeviceB-rm-backup-prf-profile1] vrrp-id 1 interface gigabitethernet 0/1/0
      ```
      ```
      [*DeviceB-rm-backup-prf-profile1] vrrp vrid 1 authentication-mode md5 YsH_2022
      ```
      ```
      [*DeviceB-rm-backup-prf-profile1] backup-id 10 remote-backup-service service1
      ```
      ```
      [*DeviceB-rm-backup-prf-profile1] commit
      ```
      ```
      [~DeviceB-rm-backup-prf-profile1] quit
      ```
4. Enable remote backup for ARP services.
   
   # Enable remote backup for ARP services in the RBP view of Device A and bind the RBP to GE 0/1/0.
   ```
   [~DeviceA] remote-backup-profile profile1
   ```
   ```
   [*DeviceA-rm-backup-prf-profile1] service-type arp
   ```
   ```
   [*DeviceA-rm-backup-prf-profile1] commit
   ```
   ```
   [~DeviceA-rm-backup-prf-profile1] quit
   ```
   ```
   [~DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] remote-backup-profile profile1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   
   # Enable remote backup for ARP services in the RBP view of Device B and bind the RBP to GE 0/1/0.
   ```
   [~DeviceB] remote-backup-profile profile1
   ```
   ```
   [*DeviceB-rm-backup-prf-profile1] service-type arp
   ```
   ```
   [*DeviceB-rm-backup-prf-profile1] commit
   ```
   ```
   [~DeviceB-rm-backup-prf-profile1] quit
   ```
   ```
   [~DeviceB] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] remote-backup-profile profile1
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] commit
   ```
5. Verify the configuration.
   
   After completing the configurations, run the [**display remote-backup-profile**](cmdqueryname=display+remote-backup-profile) command on Device A. The command output shows that the RBP **profile1** has been created and bound to GE 0/1/0.
   ```
   <DeviceA> display remote-backup-profile profile1
   ```
   ```
   -----------------------------------------------
    Profile-Index        : 0x1001
    Profile-Name         : profile1
    Service              : arp
    Remote-backup-service: service1
    Backup-ID            : 10
    track protocol       : VRRP
    VRRP-ID              : 1
    VRRP-Interface       : GigabitEthernet0/1/0
    Access-Control       : --
    State                : Master
    Peer State           : --
    Interface            :
                           GigabitEthernet0/1/0
    Backup mode          : hot
    Slot-Number          : 1
    Card-Number          : 0
    Port-Number          : 0
   ```
   
   Run the [**display remote-backup-profile**](cmdqueryname=display+remote-backup-profile) command on Device B. The command output shows that the RBP **profile1** has been created and bound to GE 0/1/0.
   ```
   <DeviceB> display remote-backup-profile profile1
   ```
   ```
   -----------------------------------------------
    Profile-Index        : 0x1001
    Profile-Name         : profile1
    Service              : arp
    Remote-backup-service: service1
    Backup-ID            : 10
    track protocol       : VRRP
    VRRP-ID              : 1
    VRRP-Interface       : GigabitEthernet0/1/0
    Access-Control       : --
    State                : Slave
    Peer State           : --
    Interface            :
                           GigabitEthernet0/1/0
    Backup mode          : hot
    Slot-Number          : 1
    Card-Number          : 0
    Port-Number          : 0
   ```
   
   Run the [**display remote-backup-service**](cmdqueryname=display+remote-backup-service) command on Device A. The command output shows that the RBS **service1** has been created.
   ```
   <DeviceA> display remote-backup-service service1
   ```
   ```
   ----------------------------------------------------------
    Service-Index    : 2
    Service-Name     : service1
    TCP-State        : Connected
    Peer-ip          : 1.1.1.1
    Source-ip        : 2.2.2.2
    TCP-Port         : 2046
    Track-BFD        : --
    SSL-Policy-Name  : policy1
    SSL-State        : --
   ----------------------------------------------------------
   ```
   
   Run the [**display remote-backup-service**](cmdqueryname=display+remote-backup-service) command on Device B. The command output shows that the RBS **service1** has been created.
   ```
   <DeviceB> display remote-backup-service service1
   ```
   ```
   ----------------------------------------------------------
    Service-Index    : 2
    Service-Name     : service1
    TCP-State        : Connected
    Peer-ip          : 2.2.2.2
    Source-ip        : 1.1.1.1
    TCP-Port         : 2046
    Track-BFD        : --
    SSL-Policy-Name  : policy1
    SSL-State        : --
   ----------------------------------------------------------
   ```

#### Configuration Files

* Configuration file of Device A
  
  ```
  #
  sysname DeviceA
  # 
  pki domain domain1 
  #
  pki import-certificate ca domain domain1 filename test.crt
   ssl policy policy1
   pki-domain domain1
  #
  remote-backup-service service1
   bind ssl-policy policy1
   peer 2.2.2.2 source 1.1.1.1 port 2046
  #
  remote-backup-profile profile1
   service-type arp  
   backup-id 10 remote-backup-service service1
   peer-backup hot 
   vrrp-id 1 interface GigabitEthernet0/1/0 
   vrrp vrid 1 authentication-mode md5 YsH_2022 
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0 
   vrrp vrid 1 virtual-ip 10.1.1.100 
   admin-vrrp vrid 1 
   vrrp vrid 1 priority 120
   vrrp vrid 1 preempt-mode timer delay 600
   vrrp recover-delay 20
   remote-backup-profile profile1
  #
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
  #
  ospf 1
   area 0.0.0.0 
    network 1.1.1.1 0.0.0.0 
    network 10.1.1.0 0.0.0.255
  #
  return
  ```
* Device B configuration file
  
  ```
  #
  sysname DeviceB
  #  
  pki domain domain1 
  #
  pki import-certificate ca domain domain1 filename test.crt
   ssl policy policy1
   pki-domain domain1
  #
  remote-backup-service service1
   bind ssl-policy policy1
   peer 1.1.1.1 source 2.2.2.2 port 2046
  #
  remote-backup-profile profile1
   service-type arp
   backup-id 10 remote-backup-service service1
   peer-backup hot
   vrrp-id 1 interface GigabitEthernet0/1/0
   vrrp vrid 1 authentication-mode md5 YsH_2022
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
   vrrp vrid 1 virtual-ip 10.1.1.100
   admin-vrrp vrid 1
   vrrp vrid 1 preempt-mode timer delay 600
   vrrp recover-delay 20
   remote-backup-profile profile1
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
  #
  ospf 1
   area 0.0.0.0 
    network 2.2.2.2 0.0.0.0 
    network 10.1.1.0 0.0.0.255
  #
  return
  ```