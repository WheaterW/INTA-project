Example for Configuring VPLS-based CFM (Layer 3 Network Access Using a Layer 2 Network)
=======================================================================================

This section provides an example for configuring VPLS-based CFM for Layer 3 network access using a Layer 2 network.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172361971__fig_dc_vrp_cfm_cfg_00002301), virtual private LAN service (VPLS) is deployed on PE1 and PE2. PE3 and PE4, which work in active/standby mode, connect a Layer 2 network to a Layer 3 network. Configure VPLS-based CFM to detect faults on the following links:

* Link between the CE and PE3
* Link between the CE and PE4
* Link between PE3 and PE4

**Figure 1** VLAN-based CFM for Layer 3 network access using a Layer 2 network![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent GE 0/1/1, GE 0/1/2, and GE 0/1/3, respectively.


  
![](images/fig_dc_vrp_cfm_cfg_00002301.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a pseudo wire (PW) between PE2 and PE1 to transmit packets between them.
2. Configure basic CFM functions to monitor the link between the CE and PE3.
3. Configure basic CFM functions to monitor the link between the CE and PE4.
4. Configure basic CFM functions to monitor the link between PE3 and PE4.

#### Data Preparation

To complete the configuration, you need the following data:

* Maintenance domain (MD) name
* Maintenance association (MA) name

#### Procedure

1. Configure a VPLS connection.
   
   
   
   Configure a VPLS connection between PE1 and PE2. For configuration details, see "VPLS Configuration" in *HUAWEI NE40E-M2 seriesUniversal Service Router Configuration Guide - VPN* or Configuration Files in this section.
   
   Run the [**display vsi name**](cmdqueryname=display+vsi+name) *vsi-name* **verbose** command on PE1 to view information about the virtual switching instance (VSI) and PW.
   
   ```
   <PE1>display vsi name ldp1 verbose
    ***VSI Name               : ldp1                                               
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
       Create Time            : 3 days, 22 hours, 58 minutes, 0 seconds            
       VSI State              : up                                                 
       Resource Status        : Valid
   
       VSI ID                 : 1                                                  
      *Peer Router ID         : 2.2.2.224                                          
       primary or secondary   : primary                                            
       ignore-standby-state   : no                                                 
       VC Label               : 4096                                               
       Peer Type              : dynamic                                            
       Session                : up                                                 
       Tunnel ID              : 0x82004004                                         
       Broadcast Tunnel ID    : 0x82004004                                         
       Broad BackupTunnel ID  : 0x0                                                
       CKey                   : 6                                                  
       NKey                   : 5                                                  
       StpEnable              : 0                                                  
       PwIndex                : 0                                                  
       Control Word           : enable
                                                                                   
       Interface Name         : GigabitEthernet0/1/2.1                             
       State                  : up                                                 
       Access Port            : false                                              
       Last Up Time           : 2000/01/28 23:56:24                                
       Total Up Time          : 3 days, 22 hours, 56 minutes, 10 seconds           
                                                                                   
      **PW Information:                                                            
                                                                                   
      *Peer Ip Address        : 2.2.2.224                                          
       PW State               : up                                                 
       Local VC Label         : 4096                                               
       Remote VC Label        : 4096                                               
       Remote Control Word    : enable
       PW Type                : label                                              
       Tunnel ID              : 0x82004004                                         
       Broadcast Tunnel ID    : 0x82004004                                         
       Broad BackupTunnel ID  : 0x0                                                
       Ckey                   : 0x6                                                
       Nkey                   : 0x5                                                
       Main PW Token          : 0x82004004                                         
       Slave PW Token         : 0x0                                                
       Tnl Type               : LSP                                                
       OutInterface           : GigabitEthernet0/1/1                               
       Backup OutInterface    :                                                    
       Stp Enable             : 0                                                  
       Mac Flapping           : 0                                                  
       PW Last Up Time        : 2000/01/29 01:37:08                                
       PW Total Up Time       : 3 days, 22 hours, 48 minutes, 37 seconds      
   ```
   
   Run the [**display vsi name**](cmdqueryname=display+vsi+name) *vsi-name* **verbose** command on PE2 to view information about the VSI and PW.
   
   ```
   <PE2>display vsi name ldp1 verbose
    ***VSI Name               : ldp1                                               
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
       Create Time            : 3 days, 22 hours, 31 minutes, 11 seconds           
       VSI State              : up                                                 
       Resource Status        : Valid
                                                                                   
       VSI ID                 : 1                                                  
      *Peer Router ID         : 1.1.1.223                                          
       primary or secondary   : primary                                            
       ignore-standby-state   : no                                                 
       VC Label               : 4096                                               
       Peer Type              : dynamic                                            
       Session                : up                                                 
       Tunnel ID              : 0x81004001                                         
       Broadcast Tunnel ID    : 0x81004001                                         
       Broad BackupTunnel ID  : 0x0                                                
       CKey                   : 2                                                  
       NKey                   : 1                                                  
       StpEnable              : 0                                                  
       PwIndex                : 0                                                  
                                                                                   
       Interface Name         : GigabitEthernet0/1/2.1                             
       State                  : up                                                 
       Access Port            : false                                              
       Last Up Time           : 2000/01/01 01:01:21                                
       Total Up Time          : 3 days, 22 hours, 29 minutes, 36 seconds           
       Interface Name         : GigabitEthernet0/1/1.1                             
       State                  : up                                                 
       Access Port            : false                                              
       Last Up Time           : 2000/01/01 01:42:11                                
       Total Up Time          : 3 days, 21 hours, 48 minutes, 46 seconds           
                                                                                   
      **PW Information:                                                            
                                                                                   
      *Peer Ip Address        : 1.1.1.223                                          
       PW State               : up                                                 
       Local VC Label         : 4096                                               
       Remote VC Label        : 4096                                               
       PW Type                : label                                              
       Tunnel ID              : 0x81004001                                         
       Broadcast Tunnel ID    : 0x81004001                                         
       Broad BackupTunnel ID  : 0x0                                                
       Ckey                   : 0x2                                                
       Nkey                   : 0x1                                                
       Main PW Token          : 0x81004001                                         
       Slave PW Token         : 0x0                                                
       Tnl Type               : LSP                                                
       OutInterface           : GigabitEthernet0/1/3                               
       Backup OutInterface    :                                                    
       Stp Enable             : 0                                                  
       Mac Flapping           : 0                                                  
       PW Last Up Time        : 2000/01/01 02:11:03                                
       PW Total Up Time       : 3 days, 22 hours, 27 minutes, 35 seconds  
   ```
2. Configure basic CFM functions on the CE, PE3, and PE4.
   
   
   
   # Configure basic CFM functions on the CE.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname CE
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~CE] cfm enable
   ```
   ```
   [*CE] vlan 2
   ```
   ```
   [*CE-vlan2] quit
   ```
   ```
   [*CE] interface GigabitEthernet0/1/1
   ```
   ```
   [*CE-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*CE-GigabitEthernet0/1/1] port trunk allow-pass vlan 2
   ```
   ```
   [*CE-GigabitEthernet0/1/1] quit
   ```
   ```
   [*CE] cfm md md
   ```
   ```
   [*CE-md-md] ma ma
   ```
   ```
   [*CE-md-md-ma-ma] map vlan 2
   ```
   ```
   [*CE-md-md-ma-ma] mep mep-id 1 interface GigabitEthernet0/1/1 outward
   ```
   ```
   [*CE-md-md-ma-ma] mep ccm-send mep-id 1 enable
   ```
   ```
   [*CE-md-md-ma-ma] remote-mep mep-id 2
   ```
   ```
   [*CE-md-md-ma-ma] remote-mep ccm-receive mep-id 2 enable
   ```
   ```
   [*CE-md-md-ma-ma] remote-mep mep-id 3
   ```
   ```
   [*CE-md-md-ma-ma] remote-mep ccm-receive mep-id 3 enable
   ```
   ```
   [*CE-md-md-ma-ma] commit
   ```
   
   # Configure basic CFM functions on PE3.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE3
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~PE3] cfm enable
   ```
   ```
   [*PE3] interface GigabitEthernet 0/1/2.1
   ```
   ```
   [*PE3-GigabitEthernet0/1/2.1] vlan-type dot1q 2
   ```
   ```
   [*PE3-GigabitEthernet0/1/2.1] quit
   ```
   ```
   [*PE3] cfm md md
   ```
   ```
   [*PE3-md-md] ma ma
   ```
   ```
   [*PE3-md-md-ma-ma] mep mep-id 2 interface GigabitEthernet0/1/2.1 vlan 2 outward
   ```
   ```
   [*PE3-md-md-ma-ma] mep ccm-send mep-id 2 enable
   ```
   ```
   [*PE3-md-md-ma-ma] remote-mep mep-id 1
   ```
   ```
   [*PE3-md-md-ma-ma] remote-mep ccm-receive mep-id 1 enable
   ```
   ```
   [*PE3-md-md-ma-ma] remote-mep mep-id 3
   ```
   ```
   [*PE3-md-md-ma-ma] remote-mep ccm-receive mep-id 3 enable
   ```
   ```
   [*PE3] commit
   ```
   
   # Configure basic CFM functions on PE4.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE4
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~PE4] cfm enable
   ```
   ```
   [*PE4] interface GigabitEthernet 0/1/2.1
   ```
   ```
   [*PE4--GigabitEthernet0/1/2.1] vlan-type dot1q 2
   ```
   ```
   [*PE4--GigabitEthernet0/1/2.1] quit
   ```
   ```
   [*PE4] cfm md md
   ```
   ```
   [*PE4-md-md] ma ma
   ```
   ```
   [*PE4-md-md-ma-ma] mep mep-id 3 interface GigabitEthernet0/1/2.1 vlan 2 outward
   ```
   ```
   [*PE4-md-md-ma-ma] mep ccm-send mep-id 3 enable
   ```
   ```
   [*PE4-md-md-ma-ma] remote-mep mep-id 1
   ```
   ```
   [*PE4-md-md-ma-ma] remote-mep ccm-receive mep-id 1 enable
   ```
   ```
   [*PE4-md-md-ma-ma] remote-mep mep-id 2
   ```
   ```
   [*PE4-md-md-ma-ma] remote-mep ccm-receive mep-id 2 enable
   ```
   ```
   [*PE4] commit
   ```
3. Verify the configuration.
   
   
   
   Run the [**display cfm remote-mep**](cmdqueryname=display+cfm+remote-mep) command to view RMEP information. The following example uses the command output on the CE.
   
   ```
   [*CE]display cfm remote-mep                                             
   The total number of RMEPs is : 1
   The status of RMEPs : 1 up, 0 down, 0 disable
   --------------------------------------------------
    MD Name            : md
    Level              : 0
    MA Name            : ma
    RMEP ID            : 2
    VLAN ID            : 2 
    VSI Name           : ldp1
    L2VC ID            : --
    L2VPN Name         : --  CE ID              : --  CE Offset          : --
     L2TPV3 Tunnel Name            : --
    L2TPV3 Local Connection Name  : --
    MAC                : 00e0-fc12-7890
    CCM Receive        : enabled
    Trigger-If-Down    : enabled
    CFM Status         : up
    Alarm Status       : none
    Interface TLV      : --
    Port Status TLV    : --
   ```

#### Configuration Files

* CE configuration file
  
  ```
  #                                                                               
  sysname CE                                                               
  #                                                        
  vlan 2                                                 
  #                                                                               
  cfm version standard                                                            
  cfm enable                                                                      
  #                                                                    
  interface GigabitEthernet0/1/1                                                  
   portswitch
   undo shutdown                                                                  
   port trunk allow-pass vlan 2                                  
  #                                                                               
  cfm md md                                                                       
   ma ma                                                                          
    map vlan 2                                                                    
    mep mep-id 1 interface GigabitEthernet0/1/1 outward                           
    mep ccm-send mep-id 1 enable                                                  
    remote-mep mep-id 2                                                           
    remote-mep ccm-receive mep-id 2 enable                                        
    remote-mep mep-id 3                                                           
    remote-mep ccm-receive mep-id 3 enable                                        
  #                                                                               
  return 
  ```
* PE1 configuration file
  
  ```
  #                                                                               
  sysname PE1
  #                                                        
  cfm version standard                                                            
  cfm enable                                                                      
  #                                                             
  mpls lsr-id 1.1.1.223                                                           
  mpls                                                                            
  #                                                                               
  mpls l2vpn                                                                      
  #                                                                               
  vsi ldp1 static                                                                    
   pwsignal ldp                                                                   
    vsi-id 1                                                                      
    peer 2.2.2.224                                                                
  #                                                                               
  mpls ldp                                                                        
  #                                     
  interface GigabitEthernet0/1/1                                                  
   undo shutdown                                                                  
   ip address 192.168.1.1 255.255.255.0                                           
   mpls                                                                           
   mpls ldp                                                                       
  #                                                                               
  interface GigabitEthernet0/1/2.1                                                
   vlan-type dot1q 2                                                              
   l2 binding vsi ldp1
  #                                           
  interface LoopBack0                                                             
   ip address 1.1.1.223 255.255.255.0                                             
  #                                                         
  ospf 1                                                                          
   area 0.0.0.0                                                                   
    network 2.2.2.224 0.0.0.0                                                     
    network 192.168.1.0 0.0.0.255                                                 
    network 1.1.1.223 0.0.0.0                                                     
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
  mpls lsr-id 2.2.2.224                                                           
  mpls                                                                            
  #                                                                               
  mpls l2vpn                                                                      
  #                                                                               
  vsi ldp1 static                                                                    
   pwsignal ldp                                                                   
    vsi-id 1                                                                      
    peer 1.1.1.223                                                                
  #                                                                               
  mpls ldp                                                                        
  #                                     
  interface GigabitEthernet0/1/3                                                  
   undo shutdown                                                                  
   ip address 192.168.1.2 255.255.255.0                                           
   mpls                                                                           
   mpls ldp                                                                       
  #                                                                               
  interface GigabitEthernet0/1/2.1                                                
   vlan-type dot1q 2                                                              
   l2 binding vsi ldp1
  #                                           
  interface LoopBack0                                                             
   ip address 2.2.2.224 255.255.255.0                                             
  #                                                         
  ospf 1                                                                          
   area 0.0.0.0                                                                   
    network 2.2.2.224 0.0.0.0                                                     
    network 192.168.1.0 0.0.0.255                                                 
    network 1.1.1.223 0.0.0.0                                                     
  #                                             
  return
  ```
* PE3 configuration file
  
  ```
  #                                                                               
  sysname PE3                                                               
  #                                                             
  cfm version standard                                                            
  cfm enable                                                                      
  #                                       
  interface GigabitEthernet0/1/2.1                                                
   vlan-type dot1q 2                                                                    
  #                                         
  cfm md md                                                                       
   ma ma                                                                          
    mep mep-id 2 interface GigabitEthernet0/1/2.1 vlan 2 outward                  
    mep ccm-send mep-id 2 enable                                                  
    remote-mep mep-id 1                                                           
    remote-mep ccm-receive mep-id 1 enable
    remote-mep mep-id 3
    remote-mep ccm-receive mep-id 3 enable                                        
  #                                              
  return
  ```
* PE4 configuration file
  
  ```
  #                                                                               
  sysname PE4
  #                                                        
  cfm version standard                                                            
  cfm enable                                                                      
  #                                           
  interface GigabitEthernet0/1/2.1                                                
   vlan-type dot1q 2 
  #                            
  cfm md md                                                                       
   ma ma                                                                          
    mep mep-id 3 interface GigabitEthernet0/1/2.1 vlan 2 outward                  
    mep ccm-send mep-id 3 enable                                                  
    remote-mep mep-id 1                                                           
    remote-mep ccm-receive mep-id 1 enable
    remote-mep mep-id 2
    remote-mep ccm-receive mep-id 2 enable                                        
  #                                                                              
  return
  ```