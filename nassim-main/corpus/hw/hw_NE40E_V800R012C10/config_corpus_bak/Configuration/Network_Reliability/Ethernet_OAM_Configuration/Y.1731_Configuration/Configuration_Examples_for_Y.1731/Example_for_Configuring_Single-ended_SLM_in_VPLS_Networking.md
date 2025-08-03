Example for Configuring Single-ended SLM in VPLS Networking
===========================================================

This section provides an example for configuring single-ended synthetic packet loss measurement (LM) in virtual private LAN service (VPLS) networking.

#### Networking Requirements

As networks rapidly develop and applications diversify, various value-added services, such as Internet Protocol television (IPTV), video conferencing, and Voice over Internet Protocol (VoIP), are more widely used than ever before. Therefore, performance monitoring is especially important for service transport.

On the point-to-multipoint network shown in [Figure 1](#EN-US_TASK_0172362167__fig_dc_vrp_y1731_cfg_007401), a carrier wants to collect accurate performance statistics about LM on the link between PE1 and PE2. To monitor network performance in real time, the carrier can configure single-ended SLM on the VPLS network. This configuration allows the carrier to immediately adjust the network in case of voice quality deterioration.

**Figure 1** Single-ended synthetic packet LM in VPLS networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent GE 0/1/1 and GE 0/1/2, respectively.


  
![](images/fig_dc_vrp_y1731_cfg_007401.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure single-ended on-demand SLM on a PW between provider edges (PEs).
2. Configure single-ended proactive SLM on a PW between PEs.


#### Data Preparation

To complete the configuration, you need the following data:

* Layer 2 virtual circuit (L2VC) ID
* Names of the maintenance domain (MD) and maintenance association (MA) in which CE1, PE1, and PE2 reside

#### Procedure

1. Configure single-ended on-demand SLM on a PW between PEs.
   
   
   1. Configure a VPLS connection.
      
      Configure a VPLS connection between PE1 and PE2. For configuration details, see "VPLS Configuration" in *Configuration Guide - VPN* or configuration files in this section.
      
      After the preceding configuration is complete, run the [**display vsi**](cmdqueryname=display+vsi) command on each PE to view VC and attachment circuit (AC) information. The following example uses the command output on PE1.
      
      ```
      [~PE1] display vsi name ethoam verbose                                           
                                                                                    
       ***VSI Name               : ethoam                                             
          Administrator VSI      : no                                                 
          Isolate Spoken         : disable                                            
          VSI Index              : 0                                                  
          PW Signaling           : ldp                                                
          Member Discovery Style : static                                             
          Bridge-domain Mode     : disable
          PW MAC Learn Style     : unqualify                                          
          Encapsulation Type     : vlan                                               
          MTU                    : 1500                                               
          Diffserv Mode          : uniform                                            
          Service Class          : --                                                 
          Color                  : --                                                 
          DomainId               : 255                                                
          Domain Name            :                                                    
          Ignore AcState         : disable                                            
          P2P VSI                : disable                                            
          Create Time            : 5 days, 19 hours, 40 minutes, 31 seconds           
          VSI State              : up                                                 
                                                                                      
          VSI ID                 : 80000                                              
         *Peer Router ID         : 10.1.1.24                                           
          primary or secondary   : primary                                            
          ignore-standby-state   : no                                                 
          VC Label               : 527                                                
          Peer Type              : dynamic                                            
          Session                : up                                                 
          Tunnel ID              : 0x25f                                              
          Broadcast Tunnel ID    : 0x25f                                              
          Broad BackupTunnel ID  : 0x0                                                
          CKey                   : 2                                                  
          NKey                   : 1                                                  
          Stp Enable             : 0                                                  
          PwIndex                : 0                                                  
          Control Word           : enable
                                                                                      
          Interface Name         : Eth-Trunk2.1                                       
          State                  : up                                                 
          Access Port            : false                                              
          Last Up Time           : 2013/04/15 17:37:09                                
          Total Up Time          : 0 days, 0 hours, 1 minutes, 37 seconds             
                                                                                      
        **PW Information:                                                             
                                                                                      
         *Peer Ip Address        : 10.1.1.24                                           
          PW State               : up                                                 
          Local VC Label         : 527                                                
          Remote VC Label        : 527                                                
          Remote Control Word    : enable
          PW Type                : label                                              
          Tunnel ID              : 0x25f                                              
          Broadcast Tunnel ID    : 0x25f                                              
          Broad BackupTunnel ID  : 0x0                                                
          Ckey                   : 0x2                                                
          Nkey                   : 0x1                                                
          Main PW Token          : 0x25f                                              
          Slave PW Token         : 0x0                                                
          Tnl Type               : LSP                                                
          OutInterface           : GigabitEthernet0/2/1                               
          Backup OutInterface    :                                                    
          Stp Enable             : 0                                                  
          PW Last Up Time        : 2013/04/15 17:37:28                                
          PW Total Up Time       : 0 days, 0 hours, 1 minutes, 18 seconds     
      
      ```
   2. Configure basic Ethernet connectivity fault management (CFM) functions and set the maintenance association end point (MEP) type to inward.
      
      Configure basic Ethernet CFM functions on each PE. Specify the Ethernet CFM protocol as IEEE Standard 802.1ag-2007. Create an MD named **md1** and an MA named **ma1**, and bind the MA to the VPLS.
      
      # Configure PE1.
      
      ```
      [~PE1] cfm enable
      ```
      ```
      [*PE1] cfm version standard
      ```
      ```
      [*PE1] cfm md md1
      ```
      ```
      [*PE1-md-md1] ma ma1
      ```
      ```
      [*PE1-md-md1-ma-ma1] map vsi ethoam
      ```
      ```
      [*PE1-md-md1-ma-ma1] mep mep-id 1 interface Eth-Trunk2.1 inward
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
      ```
      [*PE1-md-md1-ma-ma1] test-id 1 mep 1 remote-mep 2 peer 10.1.1.24
      ```
      
      # Configure PE2.
      
      ```
      [~PE2] cfm enable
      ```
      ```
      [*PE2] cfm version standard
      ```
      ```
      [*PE2] cfm md md1
      ```
      ```
      [*PE2-md-md1] ma ma1
      ```
      ```
      [*PE2-md-md1-ma-ma1] map vsi ethoam
      ```
      ```
      [*PE2-md-md1-ma-ma1] mep mep-id 2 interface Eth-Trunk2.1 inward
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
      ```
      [*PE2-md-md1-ma-ma1] test-id 1 mep 2 remote-mep 1 peer 10.1.1.25
      ```
   3. Enable PE2 to receive SLM packets.
      
      # Configure PE2.
      
      ```
      [*PE2-md-md1-ma-ma1] loss-measure single-ended-synthetic receive test-id 1 time-out 300
      ```
      ```
      [*PE2-md-md1-ma-ma1] commit
      ```
      ```
      [~PE2-md-md1-ma-ma1] quit
      ```
      ```
      [~PE2-md-md1] quit
      ```
   4. Enable PE1 to send SLM packets.
      
      # Configure PE1.
      
      ```
      [*PE1-md-md1-ma-ma1] loss-measure single-ended-synthetic send test-id 1 interval 1000 sending-count 10 time-out 2
      ```
      ```
      [*PE1-md-md1-ma-ma1] commit
      ```
      ```
      [~PE1-md-md1-ma-ma1] quit
      ```
      ```
      [~PE1-md-md1] quit
      ```
   5. Verify the configuration.
      
      Run the [**display y1731 statistic-type**](cmdqueryname=display+y1731+statistic-type) command on PE1 to view statistics about single-ended on-demand SLM.
      
      ```
      [~PE1]display y1731 statistic-type single-synthetic-loss test-id 1
      --------------------------------------------------------------------------------
      Index       L-send R-send L-recv Unack  L-loss R-loss L-loss-ratio R-loss-ratio 
      --------------------------------------------------------------------------------
      1016        10     10     10     0           0      0      0.0000%      0.0000% 
      --------------------------------------------------------------------------------
      Average Local-loss  :          0    Average Local-loss Ratio  :         0.0000% 
      Maximum Local-loss  :          0    Maximum Local-loss Ratio  :         0.0000% 
      Minimum Local-loss  :          0    Minimum Local-loss Ratio  :         0.0000% 
      Average Remote-loss :          0    Average Remote-loss Ratio :         0.0000% 
      Maximum Remote-loss :          0    Maximum Remote-loss Ratio :         0.0000% 
      Minimum Remote-loss :          0    Minimum Remote-loss Ratio :         0.0000% 
      
      ```
2. Configure single-ended proactive SLM on a PW between PEs.
   
   
   1. Enable PE2 to receive SLM packets.
      
      # Configure PE2.
      
      ```
      [~PE2] cfm md md1
      ```
      ```
      [~PE2-md-md1] ma ma1
      ```
      ```
      [~PE2-md-md-ma-ma1] loss-measure single-ended-synthetic receive test-id 1 time-out 300
      ```
      ```
      [*PE2-md-md1-ma-ma1] commit
      ```
      ```
      [~PE2-md-md1-ma-ma1] quit
      ```
      ```
      [~PE2-md-md1] quit
      ```
   2. Enable PE1 to send SLM packets.
      
      # Configure PE1.
      
      ```
      [~PE1] cfm md md1
      ```
      ```
      [~PE1-md-md1] ma ma1
      ```
      ```
      [~PE1-md-md1-ma-ma1] loss-measure single-ended-synthetic continual send test-id 1 interval 1000
      ```
      ```
      [*PE1-md-md1-ma-ma1] commit
      ```
      ```
      [~PE1-md-md1-ma-ma1] quit
      ```
      ```
      [~PE1-md-md1] quit
      ```
   3. Verify the configuration.
      
      Run the [**display y1731 statistic-type**](cmdqueryname=display+y1731+statistic-type) command on PE1 to view statistics about single-ended proactive SLM.
      
      ```
      [~PE1] display  y1731  statistic-type single-synthetic-loss test-id 1
      ```
      ```
      --------------------------------------------------------------------------------
      Index       L-send R-send L-recv Unack  L-loss R-loss L-loss-ratio R-loss-ratio 
      --------------------------------------------------------------------------------
      1016        10     10     10     0           0      0      0.0000%      0.0000% 
      1017        10     10     10     0           0      0      0.0000%      0.0000% 
      1018        10     10     10     0           0      0      0.0000%      0.0000% 
      1019        10     10     10     0           0      0      0.0000%      0.0000% 
      1020        10     10     10     0           0      0      0.0000%      0.0000% 
      1021        10     10     10     0           0      0      0.0000%      0.0000% 
      --------------------------------------------------------------------------------
      Average Local-loss  :          0    Average Local-loss Ratio  :         0.0000% 
      Maximum Local-loss  :          0    Maximum Local-loss Ratio  :         0.0000% 
      Minimum Local-loss  :          0    Minimum Local-loss Ratio  :         0.0000% 
      Average Remote-loss :          0    Average Remote-loss Ratio :         0.0000% 
      Maximum Remote-loss :          0    Maximum Remote-loss Ratio :         0.0000% 
      Minimum Remote-loss :          0    Minimum Remote-loss Ratio :         0.0000% 
      ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #                                                                               
  sysname PE1
  #                                                                               
  cfm version standard                                                            
  cfm enable                                                                      
  #                                                                              
  mpls lsr-id 10.1.1.25                                                            
  mpls                                                                            
  #                                                                               
  mpls l2vpn                                                                      
  #                                                                           
  mpls ldp                                                                        
  #                                                                              
  interface Eth-Trunk2                                                            
  #                                                                               
  interface Eth-Trunk2.1                                                          
   vlan-type dot1q 1                                                              
   l2 binding vsi ethoam                                                       
  #                                                                               
  interface GigabitEthernet0/1/1                                                  
   undo shutdown                                                                  
   eth-trunk 2                                                                                                                               #                                          
  interface GigabitEthernet0/1/2                                                  
   undo shutdown                                                                  
   ip address 192.168.1.3 255.255.255.0                                           
   mpls                                                                           
   mpls ldp                                                                       
  #                                          
  interface LoopBack0                                                             
   ip address 10.1.1.25 255.255.255.255                                            
  #                                                             
  ospf 1                                                                          
   opaque-capability enable                                                       
   area 0.0.0.1                                                                   
    network 1.1.1.1 0.0.0.0                                                       
    network 10.1.1.25 0.0.0.0                                                      
    network 2.2.2.2 0.0.0.0                                                      
    network 10.1.1.0 0.0.0.255                                                                                               
    network 192.168.1.0 0.0.0.255                                                 
    network 192.168.2.0 0.0.0.255                                                 
  #                                                                    
  cfm md md1                      
   ma ma1
    map vsi ethoam                                                    
    mep mep-id 1 interface Eth-Trunk2.1 inward                                    
    mep ccm-send mep-id 1 enable                                                  
    remote-mep mep-id 2
    remote-mep ccm-receive mep-id 2 enable                                     
    test-id 1 mep 1 remote-mep 2 peer 10.1.1.24
    loss-measure single-ended-synthetic continual send test-id 1 interval 1000    
  #                                                                               
  return  
  ```
* PE2 configuration file
  
  ```
  #                                                                               
  sysname PE2
  # 
  cfm version standard                                                           
  cfm enable                                                                      
  #                                                                               
  mpls lsr-id 10.1.1.24                                                            
  mpls                                                                            
  #                                                                               
  mpls l2vpn                                                                      
  #                                                                           
  mpls ldp                                                                        
  #                                                                               
  interface Eth-Trunk2                                                            
  #                                                                               
  interface Eth-Trunk2.1                                                          
   vlan-type dot1q 1                                                              
   l2 binding vsi ethoam                                                       
  #                                                                               
  interface GigabitEthernet0/1/1                                                  
   undo shutdown                                                                  
   eth-trunk 2                                                                    
  #                                                           
  interface GigabitEthernet0/1/2                                                  
   undo shutdown                                                                  
   ip address 192.168.1.4 255.255.255.0                                           
   mpls                                                                           
   mpls ldp                                                                       
  #                                                                                              
  interface NULL0                                                                 
  #                                                                               
  interface LoopBack0                                                             
   ip address 10.1.1.24 255.255.255.255                                            
  #                                                                       
  ospf 1                                                                          
   opaque-capability enable                                                       
   area 0.0.0.1                                                                   
    network 10.1.1.24 0.0.0.0                                                      
    network 2.2.2.2 0.0.0.0                                                       
    network 10.1.1.0 0.0.0.255                                                                                                  
    network 192.168.1.0 0.0.0.255                                                 
    network 192.168.2.0 0.0.0.255                                                 
  #                                               
  cfm md md1   
   ma ma1
    map vsi ethoam                                                    
    mep mep-id 2 interface Eth-Trunk2.1 inward                                 
    mep ccm-send mep-id 2 enable                                               
    remote-mep mep-id 1                                                          
    remote-mep ccm-receive mep-id 1 enable                                        
    test-id 1 mep 2 remote-mep 1 peer 10.1.1.25                                               
    loss-measure single-ended-synthetic receive test-id 1 time-out 300 
  #                                                                               
  return 
  ```