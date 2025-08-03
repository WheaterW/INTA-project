Example for Configuring an NQA PWE3 Ping Test to check PW Connectivity on a VPWS Network
========================================================================================

This section provides an example for configuring an NQA PWE3 ping test to check PW connectivity on a virtual private wire service (VPWS) network.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172373144__fig_dc_vrp_nqa_cfg_004201), CE-A and CE-B run PPP to access U-PE1 and U-PE2, respectively. U-PE1 and U-PE2 are connected over an MPLS backbone network. A dynamic multi-segment PW between U-PE1 and U-PE2 is established over a label switched path (LSP), with an S-PE functioning as a switching node.

The PWE3 ping function can be configured to check the connectivity of the multi-segment PW between U-PE1 and U-PE2.

**Figure 1** VPWS networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

* In this example, interfaces 1 and 2 represent GE0/1/0 and GE0/2/0, respectively.

  
![](images/fig_dc_vrp_nqa_cfg_004201.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IGP on the backbone network for communication between Routers on the network.
2. Enable basic MPLS functions over the backbone network and set up LSPs. Establish a remote MPLS Label Distribution Protocol (LDP) peer relationship between U-PE1 and S-PE, and between U-PE2 and S-PE.
3. Set up an MPLS Layer 2 virtual circuit (L2VC) connection between U-PEs.
4. Set up a switched PW on the switching node S-PE.
5. Configure a PWE3 ping test instance for the multi-segment PW on U-PE1.

#### Data Preparation

To complete the configuration, you need the following data:

* Different L2VC IDs of U-PE1 and U-PE2
* MPLS LSR IDs of U-PE1, S-PE, and U-PE2
* IP address of the remote peer
* Encapsulation type of the switched PW
* Name of the PW template configured on each U-PE and template parameters

#### Procedure

1. Configure a dynamic multi-segment PW.
   
   
   
   Configure a dynamic multi-segment PW on the MPLS backbone network.
   
   For details, see "VPWS Configuration" in *HUAWEI NE40E-M2 seriesNE40E Configuration Guide > VPN*.
2. Configure a PWE3 ping test instance for the multi-segment PW.
   
   
   
   # Configure U-PE1.
   
   ```
   [*U-PE1] nqa test-instance test pwe3ping
   ```
   ```
   [*U-PE1-nqa-test-pwe3ping] test-type pwe3ping
   ```
   ```
   [*U-PE1-nqa-test-pwe3ping] local-pw-id 100
   ```
   ```
   [*U-PE1-nqa-test-pwe3ping] local-pw-type ppp
   ```
   ```
   [*U-PE1-nqa-test-pwe3ping] label-type control-word
   ```
   ```
   [*U-PE1-nqa-test-pwe3ping] remote-pw-id 200
   ```
   ```
   [*U-PE1-nqa-test-pwe3ping] commit
   ```
3. Start the test instance.
   
   
   ```
   [*U-PE1-nqa-test-pwe3ping] start now
   ```
4. Verify the test result.
   
   
   
   Run the **display nqa results** command on the PE. The command output shows that the test is successful.
   
   ```
   [*U-PE1-nqa-test-pwe3ping] display nqa results
   ```
   ```
   NQA entry(lh, 11) :testflag is inactive ,testtype is pwe3ping
     1 . Test 1 result   The test is finished 
      SendProbe:3                            ResponseProbe:3                       
      Completion:success                     RTD OverThresholds number:0           
      OWD OverThresholds SD number:0         OWD OverThresholds DS number:0        
      Min/Max/Avg/Sum RTT:3/5/4/11           RTT Square Sum:43                     
      NumOfRTT:3                             Drop operation number:0               
      Operation sequence errors number:0     RTT Status errors number:0            
      System busy operation number:0         Operation timeout number:0            
      Min Positive SD:0                      Min Positive DS:1                     
      Max Positive SD:0                      Max Positive DS:1                     
      Positive SD Number:0                   Positive DS Number:1                  
      Positive SD Sum:0                      Positive DS Sum:1                     
      Positive SD Square Sum:0               Positive DS Square Sum:1              
      Min Negative SD:1                      Min Negative DS:1                     
      Max Negative SD:2                      Max Negative DS:1                     
      Negative SD Number:2                   Negative DS Number:1                  
      Negative SD Sum:3                      Negative DS Sum:1                     
      Negative SD Square Sum:5               Negative DS Square Sum:1              
      Min Delay SD:0                         Min Delay DS:0                        
      Max Delay SD:0                         Max Delay DS:0                        
      Delay SD Square Sum:0                  Delay DS Square Sum:0                 
      Packet Loss SD:0                       Packet Loss DS:0                      
      Packet Loss Unknown:0                  Average of Jitter:1                   
      Average of Jitter SD:1                 Average of Jitter DS:1                
      Jitter out value:0.1015625             Jitter in value:0.0611979             
      NumberOfOWD:0                          Packet Loss Ratio:0 %                 
      OWD SD Sum:0                           OWD DS Sum:0                          
      ICPIF value:0                          MOS-CQ value:0                        
      Attempts number:1                      Disconnect operation number:0         
      Connection fail number:0               Destination ip address:10.4.1.2        
      Last Good Probe Time: 2016-11-15 20:33:43.8
   ```

#### Configuration Files

* CE-A configuration file
  
  ```
  #
  ```
  ```
   sysname CE-A
  ```
  ```
  #
  ```
  ```
   interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.10.1.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
   return
  ```
* U-PE1 configuration file
  
  ```
  #
  ```
  ```
   sysname U-PE1
  ```
  ```
  #
  ```
  ```
   mpls lsr-id 1.1.1.9
  ```
  ```
   mpls
  ```
  ```
  #
  ```
  ```
   mpls l2vpn
  ```
  ```
  #
  ```
  ```
   mpls ldp
  ```
  ```
  #
  ```
  ```
   mpls ldp remote-peer 3.3.3.9
  ```
  ```
   remote-ip 3.3.3.9  
  ```
  ```
  #
  ```
  ```
   pw-template wwt
  ```
  ```
   peer-address 3.3.3.9
  ```
  ```
   control-word
  ```
  ```
  #
  ```
  ```
   interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   mpls l2vc 3.3.3.9 pw-template wwt 100   
  ```
  ```
  #
  ```
  ```
   interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.1.1 255.255.255.0
  ```
  ```
   mpls
  ```
  ```
   mpls ldp
  ```
  ```
  #
  ```
  ```
   interface LoopBack0
  ```
  ```
   ip address 1.1.1.9 255.255.255.255
  ```
  ```
  #
  ```
  ```
   nqa test-instance test pwe3ping
  ```
  ```
   test-type pwe3ping
  ```
  ```
   local-pw-id 100
  ```
  ```
   local-pw-type ppp
  ```
  ```
   remote-pw-id 200
  ```
  ```
  #
  ```
  ```
   ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
   network 10.1.1.0 0.0.0.255
  ```
  ```
   network 1.1.1.9 0.0.0.0
  ```
  ```
  #
  ```
  ```
   return
  ```
* P1 configuration file
  
  ```
  #
  ```
  ```
   sysname P1
  ```
  ```
  #
  ```
  ```
   mpls lsr-id 2.2.2.9
  ```
  ```
   mpls
  ```
  ```
  #
  ```
  ```
   mpls ldp
  ```
  ```
  #
  ```
  ```
   interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.1.2 255.255.255.0
  ```
  ```
   mpls
  ```
  ```
   mpls ldp
  ```
  ```
  #
  ```
  ```
   interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.2.1.1 255.255.255.0
  ```
  ```
   mpls
  ```
  ```
   mpls ldp
  ```
  ```
  #
  ```
  ```
   interface LoopBack0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 2.2.2.9 255.255.255.255
  ```
  ```
  #
  ```
  ```
   ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
   network 2.2.2.9 0.0.0.0
  ```
  ```
   network 10.1.1.0 0.0.0.255
  ```
  ```
   network 10.2.1.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
   return
  ```
* S-PE configuration file
  
  ```
  #
  ```
  ```
   sysname S-PE
  ```
  ```
  #
  ```
  ```
   mpls lsr-id 3.3.3.9
  ```
  ```
   mpls
  ```
  ```
  #
  ```
  ```
   mpls l2vpn
  ```
  ```
  #
  ```
  ```
   mpls switch-l2vc 5.5.5.9 200 between 1.1.1.9 100 encapsulation ethernet
  ```
  ```
  #
  ```
  ```
   mpls ldp
  ```
  ```
  #
  ```
  ```
   mpls ldp remote-peer 1.1.1.9
  ```
  ```
   remote-ip 1.1.1.9
  ```
  ```
  #
  ```
  ```
   mpls ldp remote-peer 5.5.5.9
  ```
  ```
   remote-ip 5.5.5.9
  ```
  ```
  #
  ```
  ```
   interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.2.1.2 255.255.255.0
  ```
  ```
   mpls
  ```
  ```
   mpls ldp
  ```
  ```
  #
  ```
  ```
   interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.3.1.1 255.255.255.0
  ```
  ```
   mpls
  ```
  ```
   mpls ldp
  ```
  ```
  #
  ```
  ```
   interface LoopBack0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 3.3.3.9 255.255.255.255
  ```
  ```
  #
  ```
  ```
   ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
   network 3.3.3.9 0.0.0.0
  ```
  ```
   network 10.2.1.0 0.0.0.255
  ```
  ```
   network 10.3.1.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
   return
  ```
* P2 configuration file
  
  ```
  #
  ```
  ```
   sysname P2
  ```
  ```
  #
  ```
  ```
   mpls lsr-id 4.4.4.9
  ```
  ```
   mpls
  ```
  ```
  #
  ```
  ```
   mpls ldp
  ```
  ```
  #
  ```
  ```
   interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.3.1.2 255.255.255.0
  ```
  ```
   mpls
  ```
  ```
   mpls ldp
  ```
  ```
  #
  ```
  ```
   interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.4.1.1 255.255.255.0
  ```
  ```
   mpls
  ```
  ```
   mpls ldp
  ```
  ```
  #
  ```
  ```
   interface LoopBack0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 4.4.4.9 255.255.255.255
  ```
  ```
  #
  ```
  ```
   ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
   network 4.4.4.9 0.0.0.0
  ```
  ```
   network 10.3.1.0 0.0.0.255
  ```
  ```
   network 10.4.1.0 0.0.0.255
  ```
  ```
  #
  ```
* U-PE2 configuration file
  
  ```
  #
  ```
  ```
   sysname U-PE2
  ```
  ```
  #
  ```
  ```
   mpls lsr-id 5.5.5.9
  ```
  ```
   mpls
  ```
  ```
  #
  ```
  ```
   mpls l2vpn
  ```
  ```
  #
  ```
  ```
   mpls ldp
  ```
  ```
  #
  ```
  ```
   mpls ldp remote-peer 3.3.3.9
  ```
  ```
   remote-ip 3.3.3.9
  ```
  ```
  #
  ```
  ```
   interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.4.1.2 255.255.255.0
  ```
  ```
   mpls
  ```
  ```
   mpls ldp
  ```
  ```
  #
  ```
  ```
   pw-template wwt
   peer-address 3.3.3.9
   control-word
  #
   interface GigabitEthernet0/2/0
   undo shutdown
   mpls l2vc 3.3.3.9 pw-template wwt 200   
  ```
  ```
  #
  ```
  ```
   interface LoopBack0
  ```
  ```
   ip address 5.5.5.9 255.255.255.255
  ```
  ```
  #
  ```
  ```
   ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
   network 5.5.5.9 0.0.0.0
  ```
  ```
   network 10.4.1.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
   return
  ```
* CE-B configuration file
  
  ```
  #
  ```
  ```
   sysname CE-B
  ```
  ```
  #
  ```
  ```
   interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.10.1.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
   return
  ```