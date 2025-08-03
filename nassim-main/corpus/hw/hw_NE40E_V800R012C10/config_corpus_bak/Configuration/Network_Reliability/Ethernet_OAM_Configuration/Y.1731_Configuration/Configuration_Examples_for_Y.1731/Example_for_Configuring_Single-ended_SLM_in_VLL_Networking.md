Example for Configuring Single-ended SLM in VLL Networking
==========================================================

This section provides an example for configuring single-ended synthetic loss measurement (SLM) in virtual leased line (VLL) networking.

#### Networking Requirements

As networks rapidly develop and applications diversify, various value-added services, such as Internet Protocol television (IPTV), video conferencing, and Voice over Internet Protocol (VoIP), are more widely used than ever before. Therefore, performance monitoring is especially important for service transport.

On the point-to-point network shown in [Figure 1](#EN-US_TASK_0172362158__fig_dc_vrp_y1731_cfg_007301), a carrier wants to collect accurate performance statistics about LM on the link between PE1 and PE2. To monitor network performance in real time, the carrier can configure single-ended SLM on the VLL network. This configuration allows the carrier to immediately adjust the network in case of voice quality deterioration.

**Figure 1** Single-ended SLM in VLL networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent GE 0/1/1 and GE 0/1/2, respectively.


  
![](images/fig_dc_vrp_y1731_cfg_007301.png)

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
   
   
   1. Configure a VLL connection.
      
      Configure a VLL connection between PE1 and PE2. For configuration details, see "VLL Configuration" in *Configuration Guide - VPN* or configuration files in this section.
      
      After the preceding configuration is complete, run the [**display mpls l2vc**](cmdqueryname=display+mpls+l2vc) command on each PE to view VC and attachment circuit (AC) information. The following example uses the command output on PE1.
      
      ```
      [~PE1] display mpls l2vc                                           
      Total LDP VC : 1     1 up       0 down                                     
                                                                                      
       *client interface       : Eth-Trunk2.1 is up                                   
        Administrator PW       : no                                                   
        session state          : up                                                   
        AC status              : up                                                   
        VC state               : up                                                   
        Label state            : 0                                                    
        Token state            : 0                                                    
        VC ID                  : 10001                                                
        VC type                : VLAN                                                 
        destination            : 10.1.1.25                                             
        local VC label         : 16           remote VC label      : 16               
        control word           : disable                                              
        remote control word    : disable                                              
        forwarding entry       : exist                                                
        local group ID         : 0                                                    
        remote group ID        : 0                                                    
        local AC OAM State     : up                                                   
        local PSN OAM State    : up                                                   
        local forwarding state : forwarding                                           
        local status code      : 0x0                                                  
        remote AC OAM state    : up                                                   
        remote PSN OAM state   : up                                                   
        remote forwarding state: forwarding                                           
        remote status code     : 0x0                                                  
        ignore standby state   : no                                                   
        BFD for PW             : unavailable                                          
        VCCV State             : up                                                   
        manual fault           : not set                                              
        active state           : active                                               
        OAM Protocol           : --                                                   
        OAM Status             : --                                                   
        OAM Fault Type         : --                                                   
        PW APS ID              : 0                                                    
        PW APS Status          : --                                                   
        TTL Value              : 1                                                    
        link state             : up                                                   
        local VC MTU           : 1500         remote VC MTU        : 1500             
        local VCCV             : alert ttl lsp-ping bfd                               
        remote VCCV            : alert ttl lsp-ping bfd                               
        tunnel policy name     : --                                                   
        PW template name       : --                                                   
        primary or secondary   : primary                                              
        load balance type      : flow                                                 
        Access-port            : false                                                
        Switchover Flag        : false                                                
        VC tunnel/token info   : 1 tunnels/tokens                                     
          NO.0  TNL type       : lsp   , TNL ID : 0x203                               
          Backup TNL type      : lsp   , TNL ID : 0x0                                 
        create time            : 2 days, 21 hours, 33 minutes, 37 seconds             
        up time                : 0 days, 4 hours, 20 minutes, 19 seconds              
        last change time       : 0 days, 4 hours, 20 minutes, 19 seconds              
        VC last up time        : 2013/04/15 10:04:26                                  
        VC total up time       : 2 days, 21 hours, 25 minutes, 20 seconds             
        CKey                   : 6                                                    
        NKey                   : 3                                                    
        PW redundancy mode     : frr                                                  
        AdminPw interface      : --                                                   
        AdminPw link state     : --                                                   
        Forward state          : send inactive, receive inactive 
        Diffserv Mode          : uniform                                              
        Service Class          : --                                                   
        Color                  : --                                                   
        DomainId               : --                                                   
        Domain Name            : --                                                   
                                                                                      
      
      ```
   2. Configure basic Ethernet connectivity fault management (CFM) functions and set the maintenance association end point (MEP) type to inward.
      
      Configure basic Ethernet CFM functions on each PE. Specify the Ethernet CFM protocol as IEEE Standard 802.1ag-2007. Create an MD named **md1** and an MA named **ma1**, and bind the MA to the VLL.
      
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
      [*PE1-md-md1-ma-ma1] map mpls l2vc 2 tagged
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
      [*PE1-md-md1-ma-ma1] test-id 1 mep 1 remote-mep 2
      ```
      ```
      [*PE1-md-md1-ma-ma1] commit
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
      [*PE2-md-md1-ma-ma1] map mpls l2vc 2 tagged
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
      [*PE2-md-md1-ma-ma1] test-id 1 mep 2 remote-mep 1
      ```
      ```
      [*PE2-md-md1-ma-ma1] commit
      ```
   3. Enable PE2 to receive SLM packets.
      
      # Configure PE2.
      
      ```
      [~PE2-md-md1-ma-ma1] loss-measure single-ended-synthetic receive test-id 1 time-out 300
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
      [~PE1-md-md1-ma-ma1] loss-measure single-ended-synthetic send test-id 1 interval 1000 sending-count 10 time-out 2
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
      [~PE1]display  y1731  statistic-type single-synthetic-loss test-id 1
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
      [*PE2-md-md-ma-ma1] commit
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
      [*PE2-md-md-ma-ma1] commit
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
   mpls l2vc 10.1.1.25 10001                                                       
  #                                                                               
  interface GigabitEthernet0/1/1                                                  
   undo shutdown                                                                  
   eth-trunk 2                                                                    
  #                                                                          
  interface GigabitEthernet0/1/2                                                  
   undo shutdown                                                                  
   ip address 192.168.1.3 255.255.255.0                                           
   mpls                                                                           
   mpls ldp                                                                                                                                                #                                          
  interface LoopBack0                                                             
   ip address 10.1.1.24 255.255.255.255                                            
  #                                                             
  ospf 1                                                                          
   opaque-capability enable                                                       
   area 0.0.0.1                                                                   
    network 10.1.1.1 0.0.0.0                                                       
    network 10.1.1.24 0.0.0.0                                                      
    network 2.2.2.2 0.0.0.0                                                      
    network 10.1.1.0 0.0.0.255                                                                                                    
    network 192.168.1.0 0.0.0.255                                                 
    network 192.168.2.0 0.0.0.255                                                 
  #                                                                    
  cfm md md1                      
   ma ma1
    map mpls l2vc 2 tagged                                                    
    mep mep-id 1 interface Eth-Trunk2.1 inward                                    
    mep ccm-send mep-id 1 enable                                                  
    remote-mep mep-id 2
    remote-mep ccm-receive mep-id 2 enable                                     
    test-id 1 mep 1 remote-mep 2
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
   mpls l2vc 10.1.1.24 10001                                                       
  #                                                                               
  interface GigabitEthernet0/1/1                                                  
   undo shutdown                                                                  
   eth-trunk 2                                                                                                                       #                                                           
  interface GigabitEthernet0/1/2                                                  
   undo shutdown                                                                  
   ip address 192.168.1.4 255.255.255.0                                           
   mpls                                                                           
   mpls ldp                                                                                                                                             #                                                                         
  interface NULL0                                                                 
  #                                                                               
  interface LoopBack0                                                             
   ip address 10.1.1.25 255.255.255.255                                            
  #                                                                       
  ospf 1                                                                          
   opaque-capability enable                                                       
   area 0.0.0.1                                                                   
    network 10.1.1.25 0.0.0.0                                                      
    network 2.2.2.2 0.0.0.0                                                       
    network 10.1.1.0 0.0.0.255                                                    
    network 10.1.1.1 0.0.0.255                                                                                                    
    network 192.168.1.0 0.0.0.255                                                 
    network 192.168.2.0 0.0.0.255                                                 
  #                                               
  cfm md md1   
   ma ma1
    map mpls l2vc 2 tagged                                                    
    mep mep-id 2 interface Eth-Trunk2.1 inward                                 
    mep ccm-send mep-id 2 enable                                               
    remote-mep mep-id 1                                                          
    remote-mep ccm-receive mep-id 1 enable                                        
    test-id 1 mep 2 remote-mep 1                                               
    loss-measure single-ended-synthetic receive test-id 1 time-out 300 
  #                                                                               
  return 
  ```