Example for Configuring Networking Service ETH-Test
===================================================

Y.1731 ETH-Test functions can be used in VLL, VPLS, and VLAN scenarios. This section provides an example for configuring the ETH-Test function for a VLL network.

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0172362188__fig_dc_vrp_y1731_cfg_007601), MEP1 is configured on an AC interface of PE1, and MEP2 is configured on an AC interface of PE2. MEP1 initiates an ETH-Test and sends test packets with a specified size and code type at a specified rate and interval. Then check the number of packets MEP1 sends and the number of packets MEP2 receives. If MEP1 sends more packets than MEP2 receives, some packets have been dropped. Then MEP1 is configured to use the bisection method to continue the test and send test packets at a lower rate. In addition, check for bit errors on MEP2 that receives test packets. The bisection method is used to send test packets at different rates between the upper and lower rate thresholds. The test process repeats until a maximum bandwidth is found when no packets are dropped in a test.

**Figure 1** ETH-Test function for a VLL network![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 in this example represents GE 0/1/1.


  
![](images/fig_dc_vrp_y1731_cfg_007601.png)

#### Data Preparation

To complete the configuration, you need the following data:

* L2VC ID used to establish a VLL between PEs
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  + VLAN ID used in VLAN networking
  + VSI name used in VSI networking
* MD name, MA name, and MEP ID on each PE

#### Procedure

1. Configure a VLL connection.
   
   
   
   Configure a VLL connection between PE1 and PE2. For configuration details, see the section "VLL Configuration" in *Configuration Guide - VPN*.
   
   By default, the interface type is tagged. You can successfully configure the **raw** parameter in the [**map mpls l2vc**](cmdqueryname=map+mpls+l2vc) command to bind the MA to the L2VC only after you configure the **raw** parameter in the [**mpls l2vc**](cmdqueryname=mpls+l2vc) command to create a dynamic VLL connection.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * When VLAN networking is used, configure a VLAN between PE1 and PE2. For configuration details, see the section "VLAN Configuration" in *Configuration Guide - LAN Access and MAN Access*.
   * Configure a VPLS connection between PE1 and PE2. For configuration details, see the section "VPLS Configuration" in *Configuration Guide - VPN*.
2. Configure basic Ethernet CFM functions.
   
   
   
   Configure basic Ethernet CFM functions on each PE. Create an MD named **md1** and an MA named **ma1** and bind the MA to the VLL.
   
   # Configure PE1.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE1
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~PE1] cfm enable
   ```
   ```
   [*PE1] cfm md md1 level 3
   ```
   ```
   [*PE1-md-md1] ma ma1
   ```
   ```
   [*PE1-md-md1-ma-ma1] map mpls l2vc 201 tagged
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * In the VLAN, associate the MA with the VLAN.
     
     ```
     [*PE1-md-md1-ma-ma1] map vlan 2
     ```
   * On the VPLS network, associate the MA with the VSI.
     ```
     [*PE1-md-md1-ma-ma1] map vsi ldp1
     ```
   ```
   [*PE1-md-md1-ma-ma1] mep mep-id 1 interface gigabitEthernet0/1/1.1 inward
   ```
   ```
   [*PE1-md-md1-ma-ma1] mep ccm-send mep-id 1 enable
   ```
   ```
   [*PE1-md-md1-ma-ma1] remote-mep mep-id 2
   ```
   ```
   [*PE1-md-md1-ma-ma1] remote-mep ccm-receive mep-id 2 enable
   ```
   
   # Configure PE2.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE2
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~PE2] cfm enable
   ```
   ```
   [*PE2] cfm md md1 level 3
   ```
   ```
   [*PE2-md-md1] ma ma1
   ```
   ```
   [*PE2-md-md1-ma-ma1] map mpls l2vc 201 tagged
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * In the VLAN, associate the MA with the VLAN.
     
     ```
     [*PE2-md-md1-ma-ma1] map vlan 2
     ```
   * On the VPLS network, associate the MA with the VSI.
     ```
     [*PE2-md-md1-ma-ma1] map vsi ldp1
     ```
   ```
   [*PE2-md-md1-ma-ma1] mep mep-id 2 interface gigabitEthernet0/1/1.1 inward
   ```
   ```
   [*PE2-md-md1-ma-ma1] mep ccm-send mep-id 2 enable
   ```
   ```
   [*PE2-md-md1-ma-ma1] remote-mep mep-id 1
   ```
   ```
   [*PE2-md-md1-ma-ma1] remote-mep ccm-receive mep-id 1 enable
   ```
3. Configure the ETH-Test function.
   
   
   
   The receive end cannot detect the initiator's sending round. Therefore, you must clear statistics on the receive end before initiating an Eth-Test test. If the statistics are not cleared, disorder statistics appear.
   
   # Configure PE2.
   
   ```
   [*PE2-md-md1-ma-ma1] eth-test enable mep 2
   ```
   ```
   [*PE2-md-md1-ma-ma1] commit 
   ```
   ```
   [~PE2-md-md1-ma-ma1] reset y1731 statistic-type eth-test md md1 ma ma1 mep 2
   ```
   ```
   [~PE2-md-md1-ma-ma1] commit
   ```
   
   # Configure PE1.
   
   ```
   [*PE1-md-md1-ma-ma1] eth-test enable mep 1
   ```
   ```
   [*PE1-md-md1-ma-ma1] commit
   ```
   ```
   [~PE1-md-md1-ma-ma1] eth-test start mep 1 remote-mep 2 rate 10
   ```
   ```
   [~PE1-md-md1-ma-ma1] commit
   ```
4. Verify the configuration.
   
   
   
   After completing the configuration, run the [**display y1731 eth-test**](cmdqueryname=display+y1731+eth-test) command on PE1 to view test configurations.
   
   ```
   <PE1>display y1731 eth-test md md1 ma ma1 mep 1
   The total number of Eth-Test is : 1                        
   --------------------------------------------------
    MD Name            : md1
    MA Name            : ma1
    MEP ID             : 1
    Sending            : Yes
    Remote MEP ID      : 2
    Mac                : --
    Interval           : 10 ms 
    Timeout            : 30 s
    Pattern            : zero-no-crc
    8021p              : 3
    Packet Size        : 64 bytes
    Out of Service     : Disabled
    Lck Level          : --
    Send Count         : 0
   
   ```
   
   Run the **display y1731 statistic-type eth-test** command on PE2 to view test results.
   
   ```
   <PE2>display y1731 statistic-type eth-test md md1 ma ma1 mep 2
   SrcMAC                       RcvPackets            ErrBitPackets            ErrSeqPackets            ErrCrcPackets
   00e0-fc12-7890                  9208312            0                        0                        0
   ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #                                                                               
  sysname PE1                                                                      
  #                                                                               
  cfm enable                                                                      
  #                                                                             
  mpls lsr-id 2.2.2.2   
  #                                                          
  mpls                                                                            
  #                                                                               
  mpls l2vpn                                                                      
  #                                                                               
  mpls ldp                                                                        
  #            
  mpls ldp remote-peer 1.1.1.1                                                    
   remote-ip 1.1.1.1                                                              
  #
  interface gigabitEthernet0/1/1.1
   vlan-type dot1q 3
   mpls l2vc 1.1.1.1 201
  #
  interface gigabitEthernet0/1/2
   ip address 192.168.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack0
   ip address 2.2.2.2 255.255.255.0
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 192.168.1.0 0.0.0.255   
  #                                                                               
  cfm md md1 level 3                                                                      
   ma ma1                                                                         
    map mpls l2vc 201 tagged                                                      
    mep mep-id 1 interface GigabitEthernet0/1/1.1 inward                         
    mep ccm-send mep-id 1 enable                                                  
    remote-mep mep-id 2                                                           
    remote-mep ccm-receive mep-id 2 enable                                        
    eth-test enable mep 1
    eth-test start mep 1 remote-mep 2 rate 10                                                         
  #                                 
  ```
* PE2 configuration file
  
  ```
  #                                                                               
  sysname PE2                                                                      
  #                                                                               
  cfm enable                                                                      
  #                                                                             
  mpls lsr-id 1.1.1.1  
  #                                                           
  mpls                                                                            
  #                                                                               
  mpls l2vpn                                                                      
  #                                                                               
  mpls ldp                                                                        
  #                                                                               
  mpls ldp remote-peer 2.2.2.2                                                    
   remote-ip 2.2.2.2                                                              
  #
  interface gigabitEthernet0/1/1.1
   vlan-type dot1q 3
   mpls l2vc 2.2.2.2 201
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 192.168.1.1 255.255.255.0
   mpls
   mpls ldp
  #                                                                               
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.0
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 192.168.1.0 0.0.0.255
  cfm md md1 level 3                                                                      
   ma ma1                                                                         
    map mpls l2vc 201 tagged                                                      
    mep mep-id 2 interface GigabitEthernet0/1/1.1 inward                         
    mep ccm-send mep-id 2 enable                                                  
    remote-mep mep-id 1                                                           
    remote-mep ccm-receive mep-id 1 enable                                        
    eth-test enable mep 2
  #                                 
  ```