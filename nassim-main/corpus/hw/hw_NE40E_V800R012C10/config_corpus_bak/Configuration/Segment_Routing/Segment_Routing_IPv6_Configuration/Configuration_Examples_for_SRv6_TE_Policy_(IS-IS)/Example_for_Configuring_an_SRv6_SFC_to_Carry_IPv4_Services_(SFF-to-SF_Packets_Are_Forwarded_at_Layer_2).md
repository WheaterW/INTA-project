Example for Configuring an SRv6 SFC to Carry IPv4 Services (SFF-to-SF Packets Are Forwarded at Layer 2)
=======================================================================================================

This section provides an example for configuring an SRv6 TE Policy to carry IPv4 services in an SRv6 SFC scenario (SFF-to-SF packets are forwarded at Layer 2).

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0223624848__fig184238288365), SF1 and SF2 are connected to SFF1 and SFF2, respectively. SF1 and SF2 provide different SFC functions. For the service flow direction from the SC to the tail end, it is required that the SFC function be configured on the network to ensure that IPv4 service packets are processed by SF1 and SF2 in sequence.

**Figure 1** Configuring an SRv6 SFC to carry IPv4 services (SFF-to-SF packets are forwarded at Layer 2)![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/1/0, GE 0/2/0, and GE 0/3/0, respectively.


  
![](figure/en-us_image_0223626265.png "Click to enlarge")

#### Precautions

Before configuring an SRv6 SFC to carry IPv4 services (SFF-to-SF packets are forwarded at Layer 2), note the following:

* The configuration in this example focuses on the SC, SFFs, and tail end. The configuration on the SFs is not mentioned.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable IPv6 forwarding and configure an IPv6 address for each interface.
2. Enable IS-IS, configure an IS-IS level, and specify a network entity title (NET) on each device.
3. Configure basic SRv6 functions on each device.
4. Configure SF access on SFFs.
5. Configure SFC on SFFs.
6. Configure an SRv6 TE Policy on the SC.
7. Configure a traffic policy on the SC to redirect traffic to the SRv6 TE Policy.

#### Data Preparation

To complete the configuration, you need the following data:

* Interface IPv6 addresses on each device
* IS-IS process ID of each device
* IS-IS level of each device
* Locators of each device

#### Procedure

1. Enable IPv6 forwarding and configure an IP address for each interface.
   
   
   
   # Configure SFF1. The configurations of other devices are similar to the configuration of SFF1. For configuration details, see [Configuration Files](#EN-US_TASK_0223624848__example201171946201118) in this section.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname SFF1
   [*HUAWEI] commit
   [~SFF1] interface gigabitethernet 0/1/0
   [~SFF1-GigabitEthernet0/1/0] ipv6 enable
   [*SFF1-GigabitEthernet0/1/0] ipv6 address 2001:db8:1::2 96
   [*SFF1-GigabitEthernet0/1/0] quit
   [*SFF1] interface gigabitethernet 0/2/0
   [*SFF1-GigabitEthernet0/2/0] ipv6 enable
   [*SFF1-GigabitEthernet0/2/0] ipv6 address 2001:db8:2::1 96
   [*SFF1-GigabitEthernet0/2/0] quit
   [*SFF1] interface loopback1
   [*SFF1-LoopBack1] ipv6 enable
   [*SFF1-LoopBack1] ipv6 address 2001:db8:22::2 128
   [*SFF1-LoopBack1] commit
   [~SFF1-LoopBack1] quit
   ```
2. Configure IS-IS.
   
   
   
   # Configure SFF1. The configurations of other devices are similar to the configuration of SFF1. For configuration details, see [Configuration Files](#EN-US_TASK_0223624848__example201171946201118) in this section.
   
   ```
   [~SFF1] isis 1
   [*SFF1-isis-1] is-level level-1
   [*SFF1-isis-1] cost-style wide
   [*SFF1-isis-1] network-entity 10.0000.0000.0002.00
   [*SFF1-isis-1] ipv6 enable topology ipv6
   [*SFF1-isis-1] quit
   [*SFF1] interface gigabitethernet 0/1/0
   [*SFF1-GigabitEthernet0/1/0] isis ipv6 enable 1
   [*SFF1-GigabitEthernet0/1/0] quit
   [*SFF1] interface gigabitethernet 0/2/0
   [*SFF1-GigabitEthernet0/2/0] isis ipv6 enable 1
   [*SFF1-GigabitEthernet0/2/0] quit
   [*SFF1] interface loopback1
   [*SFF1-LoopBack1] isis ipv6 enable 1
   [*SFF1-LoopBack1] commit
   [~SFF1-LoopBack1] quit
   ```
3. Configure SRv6 SIDs and enable IS-IS SRv6.
   
   
   
   # Configure the SC.
   
   ```
   [~SC] segment-routing ipv6
   [*SC-segment-routing-ipv6] encapsulation source-address 2001:db8:10::1
   [*SC-segment-routing-ipv6] locator as1 ipv6-prefix 2001:db8:11:: 64 static 32
   [*SC-segment-routing-ipv6-locator] opcode ::1 end psp
   [*SC-segment-routing-ipv6-locator] quit
   [*SC-segment-routing-ipv6] quit
   [*SC] isis 1
   [*SC-isis-1] segment-routing ipv6 locator as1 auto-sid-disable
   [*SC-isis-1] commit
   [~SC-isis-1] quit
   ```
   
   # Configure SFF1.
   
   ```
   [~SFF1] segment-routing ipv6
   [*SFF1-segment-routing-ipv6] encapsulation source-address 2001:db8:22::2
   [*SFF1-segment-routing-ipv6] locator as1 ipv6-prefix 2001:db8:12:: 64 static 32
   [*SFF1-segment-routing-ipv6-locator] opcode ::1 end psp
   [*SFF1-segment-routing-ipv6-locator] quit
   [*SFF1-segment-routing-ipv6] quit
   [*SFF1] isis 1
   [*SFF1-isis-1] segment-routing ipv6 locator as1 auto-sid-disable
   [*SFF1-isis-1] commit
   [~SFF1-isis-1] quit
   ```
   
   # Configure SFF2.
   
   ```
   [~SFF2] segment-routing ipv6
   [*SFF2-segment-routing-ipv6] encapsulation source-address 2001:db8:33::3
   [*SFF2-segment-routing-ipv6] locator as1 ipv6-prefix 2001:db8:13:: 64 static 32
   [*SFF2-segment-routing-ipv6-locator] opcode ::1 end psp
   [*SFF2-segment-routing-ipv6-locator] quit
   [*SFF2-segment-routing-ipv6] quit
   [*SFF2] isis 1
   [*SFF2-isis-1] segment-routing ipv6 locator as1 auto-sid-disable
   [*SFF2-isis-1] commit
   [~SFF2-isis-1] quit
   ```
   
   # Configure the tail end.
   
   ```
   [~Tail] ip vpn-instance vpna
   [*Tail-vpn-instance-vpna] ipv4-family
   [*Tail-vpn-instance-vpna-af-ipv4] route-distinguisher 500:1
   [*Tail-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
   [*Tail-vpn-instance-vpna-af-ipv4] quit
   [*Tail-vpn-instance-vpna] quit
   [*Tail] segment-routing ipv6
   [*Tail-segment-routing-ipv6] encapsulation source-address 2001:db8:55::5
   [*Tail-segment-routing-ipv6] locator as1 ipv6-prefix 2001:db8:15:: 64 static 32
   [*Tail-segment-routing-ipv6-locator] opcode ::1 end psp
   [*Tail-segment-routing-ipv6-locator] opcode ::100 end-dt4 vpn-instance vpna
   [*Tail-segment-routing-ipv6-locator] quit
   [*Tail-segment-routing-ipv6] quit
   [*Tail] isis 1
   [*Tail-isis-1] segment-routing ipv6 locator as1 auto-sid-disable
   [*Tail-isis-1] commit
   [~Tail-isis-1] quit
   ```
   
   After the configuration is complete, run the [**display segment-routing ipv6 locator**](cmdqueryname=display+segment-routing+ipv6+locator) [ *locator-name* ] **verbose** command to check SRv6 locator information.
4. Configure SF access on SFFs.
   
   
   
   # Configure SFF1.
   
   ```
   [~SFF1] interface gigabitethernet 0/3/0.1 mode l2
   [*SFF1-GigabitEthernet0/3/0.1] encapsulation dot1q vid 1
   [*SFF1-GigabitEthernet0/3/0.1] quit
   [*SFF1] commit
   ```
   
   
   
   # Configure SFF2.
   
   ```
   [~SFF2] interface gigabitethernet 0/3/0.1 mode l2
   [*SFF2-GigabitEthernet0/3/0.1] encapsulation dot1q vid 1
   [*SFF2-GigabitEthernet0/3/0.1] quit
   [*SFF2] commit
   ```
5. Configure basic SFC functions on SFFs.
   
   
   
   # Configure SFF1.
   
   ```
   [~SFF1] segment-routing ipv6
   [*SFF1-segment-routing-ipv6] locator as1
   [*SFF1-segment-routing-ipv6-locator] opcode ::100 end-as
   [*SFF1-segment-routing-ipv6-locator-endas-::100] inner-type ipv4
   [*SFF1-segment-routing-ipv6-locator-endas-::100] encapsulation eth out-interface gigabitethernet 0/3/0.1 out-vlan 1 in-interface gigabitethernet 0/3/0.1 in-vlan 1
   [*SFF1-segment-routing-ipv6-locator-endas-::100] cache source-address 2001:db8:10::1
   [*SFF1-segment-routing-ipv6-locator-endas-::100] cache list 2001:db8:15::100 2001:db8:15::1 2001:db8:13::100 2001:db8:12::100
   [*SFF1-segment-routing-ipv6-locator-endas-::100] quit
   [*SFF1-segment-routing-ipv6-locator] quit
   [*SFF1-segment-routing-ipv6] quit
   [*SFF1] commit
   ```
   
   
   
   # Configure SFF2.
   
   ```
   [~SFF2] segment-routing ipv6
   [*SFF2-segment-routing-ipv6] locator as1
   [*SFF2-segment-routing-ipv6-locator] opcode ::100 end-as
   [*SFF2-segment-routing-ipv6-locator-endas-::100] inner-type ipv4
   [*SFF2-segment-routing-ipv6-locator-endas-::100] encapsulation eth out-interface gigabitethernet 0/3/0.1 out-vlan 1 in-interface gigabitethernet 0/3/0.1 in-vlan 1
   [*SFF2-segment-routing-ipv6-locator-endas-::100] cache source-address 2001:db8:10::1
   [*SFF2-segment-routing-ipv6-locator-endas-::100] cache list 2001:db8:15::100 2001:db8:15::1 2001:db8:13::100 2001:db8:12::100
   [*SFF2-segment-routing-ipv6-locator-endas-::100] quit
   [*SFF2-segment-routing-ipv6-locator] quit
   [*SFF2-segment-routing-ipv6] quit
   [*SFF2] commit
   ```
6. Configure an SRv6 TE Policy on the SC.
   
   
   
   # Configure the SC.
   
   ```
   [~SC] segment-routing ipv6 
   [~SC-segment-routing-ipv6] segment-list list1 
   [*SC-segment-routing-ipv6-segment-list-list1] index 5 sid ipv6 2001:db8:12::100
   [*SC-segment-routing-ipv6-segment-list-list1] index 10 sid ipv6 2001:db8:13::100
   [*SC-segment-routing-ipv6-segment-list-list1] index 15 sid ipv6 2001:db8:15::1
   [*SC-segment-routing-ipv6-segment-list-list1] commit
   [~SC-segment-routing-ipv6-segment-list-list1] quit
   [~SC-segment-routing-ipv6] srv6-te-policy locator as1 
   [*SC-segment-routing-ipv6] srv6-te policy policy1 endpoint 2001:db8:55::5 color 101
   [*SC-segment-routing-ipv6-policy-policy1] binding-sid 2001:db8:11::11
   [*SC-segment-routing-ipv6-policy-policy1] candidate-path preference 100
   [*SC-segment-routing-ipv6-policy-policy1-path] segment-list list1 
   [*SC-segment-routing-ipv6-policy-policy1-path] commit
   [~SC-segment-routing-ipv6-policy-policy1-path] quit
   [~SC-segment-routing-ipv6-policy-policy1] quit
   [~SC-segment-routing-ipv6] quit
   ```
   
   
   
   After the configuration is complete, run the [**display srv6-te policy**](cmdqueryname=display+srv6-te+policy) command to check SRv6 TE Policy information.
7. Configure a traffic policy on the SC to redirect traffic to the SRv6 TE Policy.
   
   
   
   # Configure the SC.
   
   ```
   [~SC] traffic classifier c1
   [*SC-classifier-c1] if-match any
   [*SC-classifier-c1] commit
   [~SC-classifier-c1] quit
   [~SC] traffic behavior b1
   [*SC-behavior-b1] redirect srv6-te policy 2001:db8:55::5 101 vpnsid 2001:db8:15::100
   [*SC-behavior-b1] commit
   [~SC-behavior-b1] quit
   [~SC] traffic policy p1
   [*SC-trafficpolicy-p1] classifier c1 behavior b1
   [*SC-trafficpolicy-p1] statistic enable
   [*SC-trafficpolicy-p1] commit
   [~SC-trafficpolicy-p1] quit
   [~SC] bridge-domain 1
   [*SC-bd1] quit
   [*SC] interface gigabitethernet 0/1/0.1 mode l2
   [*SC-GigabitEthernet0/1/0.1] encapsulation dot1q vid 1
   [*SC-GigabitEthernet0/1/0.1] rewrite pop single
   [*SC-GigabitEthernet0/1/0.1] bridge-domain 1
   [*SC-GigabitEthernet0/1/0.1] quit
   [*SC] interface Vbdif1
   [*SC-Vbdif1] ip binding vpn-instance vpna
   [*SC-Vbdif1] ip address 10.0.0.1 30
   [*SC-Vbdif1] traffic-policy p1 inbound
   [*SC-Vbdif1] commit
   [~SC-Vbdif1] quit
   ```

#### Configuration Files

* SC configuration file
  
  ```
  #
  sysname SC
  #
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  #                
  segment-routing ipv6
   encapsulation source-address 2001:db8:10::1
   locator as1 ipv6-prefix 2001:db8:11:: 64 static 32 
    opcode ::1 end psp
   srv6-te-policy locator as1
   segment-list list1
    index 5 sid ipv6 2001:db8:12::100
    index 10 sid ipv6 2001:db8:13::100
    index 15 sid ipv6 2001:db8:15::1
   srv6-te policy policy1 endpoint 2001:db8:55::5 color 101
    binding-sid 2001:db8:11::11
    candidate-path preference 100
     segment-list list1
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0001.00
   #              
   ipv6 enable topology ipv6
   segment-routing ipv6 locator as1 auto-sid-disable
   #              
  # 
  bridge-domain 1
  #
  traffic classifier c1
   if-match any
  #
  traffic behavior b1
    redirect srv6-te policy 2001:db8:55::5 101 vpnsid 2001:db8:15::100
  #
  traffic policy p1
   classifier c1 behavior b1
   statistic enable
  #
  interface Vbdif1
   ip binding vpn-instance vpna
   ip address 10.0.0.1 255.255.255.252
   traffic-policy p1 inbound
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
  #
  interface GigabitEthernet0/1/0.1 mode l2
   encapsulation dot1q vid 1
   rewrite pop single
   bridge-domain 1
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:db8:1::1/96
   isis ipv6 enable 1
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:db8:10::1/128
   isis ipv6 enable 1
  #                             
  return
  ```
* SFF1 configuration file
  
  ```
  #
  sysname SFF1
  #               
  segment-routing ipv6
   encapsulation source-address 2001:db8:22::2
   locator as1 ipv6-prefix 2001:db8:12:: 64 static 32
    opcode ::1 end psp
    opcode ::100 end-as
     inner-type ipv4
     encapsulation eth out-interface GigabitEthernet0/3/0.1 out-vlan 1 in-interface GigabitEthernet0/3/0.1 in-vlan 1
     cache source-address 2001:db8:10::1
     cache list 2001:db8:15::100 2001:db8:15::1 2001:db8:13::100 2001:db8:12::100
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0002.00
   #              
   ipv6 enable topology ipv6
   segment-routing ipv6 locator as1 auto-sid-disable
   #
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:db8:1::2/96
   isis ipv6 enable 1
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:db8:2::1/96
   isis ipv6 enable 1
  #               
  interface GigabitEthernet0/3/0
   undo shutdown  
  #
  interface GigabitEthernet0/3/0.1 mode l2
   encapsulation dot1q vid 1
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:db8:22::2/128
   isis ipv6 enable 1
  #               
  return 
  ```
* SFF2 configuration file
  
  ```
  #
  sysname SFF2
  #               
  segment-routing ipv6
   encapsulation source-address 2001:db8:33::3
   locator as1 ipv6-prefix 2001:db8:13:: 64 static 32
    opcode ::1 end psp
    opcode ::100 end-as
     inner-type ipv4
     encapsulation eth out-interface GigabitEthernet0/3/0.1 out-vlan 1 in-interface GigabitEthernet0/3/0.1 in-vlan 1
     cache source-address 2001:db8:10::1
     cache list 2001:db8:15::100 2001:db8:15::1 2001:db8:13::100 2001:db8:12::100
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0003.00
   #              
   ipv6 enable topology ipv6
   segment-routing ipv6 locator as1 auto-sid-disable
   #              
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:db8:2::2/96
   isis ipv6 enable 1
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:db8:3::1/96
   isis ipv6 enable 1
  #               
  interface GigabitEthernet0/3/0
   undo shutdown  
  #
  interface GigabitEthernet0/3/0.1 mode l2
   encapsulation dot1q vid 1
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:db8:33::3/128
   isis ipv6 enable 1
  #               
  return 
  ```
* Tail end configuration file
  
  ```
  #
  sysname Tail End
  #
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 500:1
    apply-label per-instance
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  #               
  segment-routing ipv6
   encapsulation source-address 2001:db8:55::5
   locator as1 ipv6-prefix 2001:db8:15:: 64 static 32
    opcode ::1 end psp
    opcode ::100 end-dt4 vpn-instance vpna
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0004.00
   #              
   ipv6 enable topology ipv6
   segment-routing ipv6 locator as1 auto-sid-disable
   #              
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:db8:3::2/96
   isis ipv6 enable 1
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip binding vpn-instance vpna    
   ip address 10.5.1.2 255.255.255.252
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:db8:55::5/128
   isis ipv6 enable 1
  #               
  return 
  ```