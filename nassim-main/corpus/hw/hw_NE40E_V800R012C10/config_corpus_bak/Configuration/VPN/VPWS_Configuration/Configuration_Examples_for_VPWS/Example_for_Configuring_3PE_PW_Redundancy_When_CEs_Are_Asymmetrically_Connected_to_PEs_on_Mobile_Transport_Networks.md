Example for Configuring 3PE PW Redundancy When CEs Are Asymmetrically Connected to PEs on Mobile Transport Networks
===================================================================================================================

In PW redundancy scenarios in which CEs asymmetrically connect to PEs in 3PE mode, the E-Trunk determines the master/backup status of the PEs.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172369966__fig_dc_vrp_vpws_cfg_601701), CE1 and CE2 are users of the same enterprise, and PE1 through PE3 are public network devices. CE1 is single-homed to PE1, and CE2 is dual-homed to PE2 and PE3. To allow CE1 and CE2 to communicate and also ensure reliability, deploy PW redundancy between PE1, PE2, and PE3 to protect PWs. In addition, to rapidly detect public network link faults to implement fast PW switching, deploy BFD.

**Figure 1** Configuring 3PE PW redundancy when CEs are asymmetrically connected to PEs![](../../../../public_sys-resources/note_3.0-en-us.png) 

* In this example, interfaces 1 through 3 represent GE0/1/0, GE0/1/1, and GE0/1/2, respectively.


  
![](images/fig_dc_vrp_vpws_cfg_601701.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IP address and a routing protocol for each interface to ensure IP connectivity at the network layer. OSPF is used in this example.
2. Configure MPLS and public network tunnels.
3. Configure service PWs and mPWs, and bind the service PWs to the mPWs.
4. Configure BFD to detect mPW connectivity.
5. Configure an E-Trunk to determine the master/backup status of the PWs, and bind BFD to the E-Trunk.

#### Data Preparation

To complete the configuration, you need the following data:

* PEs' interface numbers, IP addresses and OSPF process IDs
* PE's LSR IDs
* E-Trunk's LACP system IDs and priorities
* L2VC's destination IP addresses, VC IDs, and VC types
* BFD session name and local and remote BFD session discriminators

#### Procedure

1. Configure an IP address and a routing protocol for each interface to ensure IP connectivity at the network layer.
   
   
   
   For detailed configurations, see [Configuration Files](#EN-US_TASK_0172369966__sec_dc_vrp_vpws_cfg_601701).
2. Configure basic MPLS functions. Configure a TE tunnel between PE1 and PE2 and between PE1 and PE3; configure an LDP LSP between PE2 and PE3.
   
   
   
   For detailed configurations, see [Configuration Files](#EN-US_TASK_0172369966__sec_dc_vrp_vpws_cfg_601701).
3. Configure PWE3.
   1. Configure a remote MPLS LDP session between PE1 and PE2 and between PE1 and PE3.
      
      
      
      For detailed configurations, see [Configuration Files](#EN-US_TASK_0172369966__sec_dc_vrp_vpws_cfg_601701).
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      PWE3 uses extended LDP signaling to distribute VPN labels. Because PE1 and PE2 and PE1 and PE3 are connected over TE tunnels without using MPLS LDP, you must globally enable MPLS LDP and establish remote LDP sessions.
      
      PE2 and PE3 are directly connected over an LDP LSP, and therefore do not need to establish a remote LDP session.
   2. Configure service PWs.
      
      
      
      # Configure PE1.
      
      ```
      <PE1> system-view
      ```
      ```
      [~PE1] mpls l2vpn
      ```
      ```
      [*PE1-l2vpn] quit
      ```
      ```
      [*PE1] interface gigabitethernet 0/1/0
      ```
      ```
      [*PE1-GigabitEthernet0/1/0] undo shutdown
      ```
      ```
      [*PE1-GigabitEthernet0/1/0] quit
      ```
      ```
      [*PE1] interface gigabitethernet 0/1/0.1
      ```
      ```
      [*PE1-GigabitEthernet0/1/0.1] vlan-type dot1q 10
      ```
      ```
      [*PE1-GigabitEthernet0/1/0.1] mpls l2vc 2.2.2.2 1 tunnel-policy policy
      ```
      ```
      [*PE1-GigabitEthernet0/1/0.1] mpls l2vc 3.3.3.3 2 tunnel-policy policy1 secondary
      ```
      ```
      [*PE1-GigabitEthernet0/1/0.1] mpls l2vpn redundancy independent
      ```
      ```
      [*PE1-GigabitEthernet0/1/0.1] quit
      ```
      ```
      [*PE1] commit
      ```
      
      # Configure PE2.
      
      ```
      <PE2> system-view
      ```
      ```
      [~PE2] mpls l2vpn
      ```
      ```
      [*PE2-l2vpn] quit
      ```
      ```
      [*PE2] interface eth-trunk 10
      ```
      ```
      [*PE2-Eth-Trunk10] quit
      ```
      ```
      [*PE2] interface eth-trunk 10.1
      ```
      ```
      [*PE2-Eth-Trunk10.1] vlan-type dot1q 10
      ```
      ```
      [*PE2-Eth-Trunk10.1] mpls l2vc 1.1.1.1 1 tunnel-policy policy1
      ```
      ```
      [*PE2-Eth-Trunk10.1] mpls l2vc 3.3.3.3 3 bypass
      ```
      ```
      [*PE2-Eth-Trunk10.1] quit
      ```
      ```
      [*PE2] commit
      ```
      
      # Configure PE3.
      
      ```
      <PE3> system-view
      ```
      ```
      [~PE3] mpls l2vpn
      ```
      ```
      [*PE3-l2vpn] quit
      ```
      ```
      [*PE3] interface eth-trunk 10
      ```
      ```
      [*PE3-Eth-Trunk10] quit
      ```
      ```
      [*PE3] interface eth-trunk 10.1
      ```
      ```
      [*PE3-Eth-Trunk10.1] vlan-type dot1q 10
      ```
      ```
      [*PE3-Eth-Trunk10.1] mpls l2vc 1.1.1.1 2 tunnel-policy policy1
      ```
      ```
      [*PE3-Eth-Trunk10.1] mpls l2vc 2.2.2.2 3 bypass
      ```
      ```
      [*PE3-Eth-Trunk10.1] quit
      ```
      ```
      [*PE3] commit
      ```
   3. Configure mPWs.
      
      
      
      # Configure PE1.
      
      ```
      [~PE1] interface loopback 1
      ```
      ```
      [~PE1-LoopBack1] mpls l2vc 2.2.2.2 4 tunnel-policy policy control-word admin
      ```
      ```
      [*PE1-LoopBack1] quit
      ```
      ```
      [*PE1] interface loopback 2
      ```
      ```
      [*PE1-LoopBack2] mpls l2vc 3.3.3.3 5 tunnel-policy policy1 control-word admin
      ```
      ```
      [*PE1-LoopBack2] quit
      ```
      ```
      [*PE1] commit
      ```
      
      # Configure PE2.
      
      ```
      [~PE2] interface loopback 1
      ```
      ```
      [~PE2-LoopBack1] mpls l2vc 1.1.1.1 4 tunnel-policy policy1 control-word admin
      ```
      ```
      [*PE2-LoopBack1] quit
      ```
      ```
      [*PE2] commit
      ```
      
      # Configure PE3.
      
      ```
      [~PE3] interface loopback 1
      ```
      ```
      [~PE3-LoopBack1] mpls l2vc 1.1.1.1 5 tunnel-policy policy1 control-word admin
      ```
      ```
      [*PE3-LoopBack1] quit
      ```
      ```
      [*PE3] commit
      ```
   4. Bind the service PWs to the mPWs.
      
      
      
      # Configure PE1.
      
      ```
      [~PE1] interface gigabitethernet 0/1/0.1
      ```
      ```
      [~PE1-GigabitEthernet0/1/0.1] mpls l2vc track admin-vc interface loopback 1
      ```
      ```
      [*PE1-GigabitEthernet0/1/0.1] mpls l2vc secondary track admin-vc interface loopback 2
      ```
      ```
      [*PE1-GigabitEthernet0/1/0.1] quit
      ```
      ```
      [*PE1] commit
      ```
      
      # Configure PE2.
      
      ```
      [~PE2] interface eth-trunk 10.1
      ```
      ```
      [~PE2-Eth-Trunk10.1] mpls l2vc track admin-vc interface loopback 1
      ```
      ```
      [*PE2-Eth-Trunk10.1] quit
      ```
      ```
      [*PE2] commit
      ```
      
      # Configure PE3.
      
      ```
      [~PE3] interface eth-trunk 10.1
      ```
      ```
      [~PE3-Eth-Trunk10.1] mpls l2vc track admin-vc interface loopback 1
      ```
      ```
      [*PE3-Eth-Trunk10.1] quit
      ```
      ```
      [*PE3] commit
      ```
4. Configure BFD to detect mPW connectivity.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bfd
   ```
   ```
   [*PE1-bfd] quit
   ```
   ```
   [*PE1] bfd pe1a bind pw interface loopback 1
   ```
   ```
   [*PE1-bfd-lsp-session-pe1a] discriminator local 1000
   ```
   ```
   [*PE1-bfd-lsp-session-pe1a] discriminator remote 1001
   ```
   ```
   [*PE1-bfd-lsp-session-pe1a] quit
   ```
   ```
   [*PE1] bfd pe1b bind pw interface loopback 2
   ```
   ```
   [*PE1-bfd-lsp-session-pe1b] discriminator local 2000
   ```
   ```
   [*PE1-bfd-lsp-session-pe1b] discriminator remote 2001
   ```
   ```
   [*PE1-bfd-lsp-session-pe1b] commit
   ```
   ```
   [*PE1-bfd-lsp-session-pe1b] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bfd
   ```
   ```
   [*PE2-bfd] quit
   ```
   ```
   [*PE2] bfd pe2 bind pw interface loopback 1
   ```
   ```
   [*PE2-bfd-lsp-session-pe2] discriminator local 1001
   ```
   ```
   [*PE2-bfd-lsp-session-pe2] discriminator remote 1000
   ```
   ```
   [*PE2-bfd-lsp-session-pe2] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] bfd
   ```
   ```
   [*PE3-bfd] quit
   ```
   ```
   [*PE3] bfd pe3 bind pw interface loopback 1
   ```
   ```
   [*PE3-bfd-lsp-session-pe3] discriminator local 2001
   ```
   ```
   [*PE3-bfd-lsp-session-pe3] discriminator remote 2000
   ```
   ```
   [*PE3-bfd-lsp-session-pe3] quit
   ```
   ```
   [*PE3] commit
   ```
5. Configure an E-Trunk to determine the master/backup status of the PWs.
   1. Configure Eth-Trunk interfaces.
      
      
      
      # Configure PE2.
      
      ```
      [~PE2] interface gigabitethernet 0/1/2
      ```
      ```
      [~PE2-GigabitEthernet0/1/2] undo shutdown
      ```
      ```
      [*PE2-GigabitEthernet0/1/2] quit
      ```
      ```
      [*PE2] interface eth-trunk 10
      ```
      ```
      [*PE2-Eth-Trunk10] mode lacp-static
      ```
      ```
      [*PE2-Eth-Trunk10] trunkport gigabitethernet 0/1/2
      ```
      ```
      [*PE2-Eth-Trunk10] quit
      ```
      ```
      [*PE2] commit
      ```
      
      # Configure PE3.
      
      ```
      [~PE3] interface gigabitethernet 0/1/2
      ```
      ```
      [~PE3-GigabitEthernet0/1/2] undo shutdown
      ```
      ```
      [*PE3-GigabitEthernet0/1/2] quit
      ```
      ```
      [*PE3] interface eth-trunk 10
      ```
      ```
      [*PE3-Eth-Trunk10] mode lacp-static
      ```
      ```
      [*PE3-Eth-Trunk10] trunkport gigabitethernet 0/1/2
      ```
      ```
      [*PE3-Eth-Trunk10] quit
      ```
      ```
      [*PE3] commit
      ```
      
      # Configure CE2.
      
      ```
      [~CE2] interface gigabitethernet 0/1/0
      ```
      ```
      [~CE2-GigabitEthernet0/1/0] undo shutdown
      ```
      ```
      [*CE2-GigabitEthernet0/1/0] quit
      ```
      ```
      [*CE2] interface gigabitethernet 0/1/1
      ```
      ```
      [*CE2-GigabitEthernet0/1/1] undo shutdown
      ```
      ```
      [*CE2-GigabitEthernet0/1/1] quit
      ```
      ```
      [*CE2] interface eth-trunk 10
      ```
      ```
      [*CE2-Eth-Trunk10] portswitch
      ```
      ```
      [*CE2-Eth-Trunk10] mode lacp-static
      ```
      ```
      [*CE2-Eth-Trunk10] port trunk allow-pass vlan 10
      ```
      ```
      [*CE2-Eth-Trunk10] trunkport gigabitethernet 0/1/0 to 0/1/1
      ```
      ```
      [*CE2-Eth-Trunk10] quit
      ```
      ```
      [*CE2] vlan 10
      ```
      ```
      [*CE2-vlan10] quit
      ```
      ```
      [*CE2] commit
      ```
   2. Configure an E-Trunk.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      For security purposes, you are advised not to use weak security algorithms in this feature. If you need to use such an algorithm, run the [**undo crypto weak-algorithm disable**](cmdqueryname=undo+crypto+weak-algorithm+disable) command to enable the weak security algorithm function.
      
      
      
      # Configure PE2.
      
      ```
      [~PE2] lacp e-trunk system-id 00e0-fc00-0000
      ```
      ```
      [*PE2] lacp e-trunk priority 100
      ```
      ```
      [*PE2] e-trunk 10
      ```
      ```
      [*PE2-e-trunk-10] security-key cipher YsHsjx_202206
      ```
      ```
      [*PE2-e-trunk-10] priority 10
      ```
      ```
      [*PE2-e-trunk-10] peer-address 3.3.3.3 source-address 2.2.2.2
      ```
      ```
      [*PE2-e-trunk-10] quit
      ```
      ```
      [*PE2] interface eth-trunk 10
      ```
      ```
      [*PE2-Eth-Trunk10] e-trunk 10
      ```
      ```
      [*PE2-Eth-Trunk10] quit
      ```
      ```
      [*PE2] commit
      ```
      
      # Configure PE3.
      
      ```
      [~PE3] lacp e-trunk system-id 00e0-fc00-0000
      ```
      ```
      [*PE3] lacp e-trunk priority 100
      ```
      ```
      [*PE3] e-trunk 10
      ```
      ```
      [*PE3-e-trunk-10] security-key cipher YsHsjx_202206
      ```
      ```
      [*PE3-e-trunk-10] priority 20
      ```
      ```
      [*PE3-e-trunk-10] peer-address 2.2.2.2 source-address 3.3.3.3
      ```
      ```
      [*PE3-e-trunk-10] quit
      ```
      ```
      [*PE3] interface eth-trunk 10
      ```
      ```
      [*PE3-Eth-Trunk10] e-trunk 10
      ```
      ```
      [*PE3-Eth-Trunk10] quit
      ```
      ```
      [*PE3] commit
      ```
   3. Bind BFD to the E-Trunk.
      
      
      
      # Configure PE2.
      
      ```
      [~PE2] bfd hello bind peer-ip 3.3.3.3 source-ip 2.2.2.2
      ```
      ```
      [*PE2-bfd-session-hello]  discriminator local 100
      ```
      ```
      [*PE2-bfd-session-hello] discriminator remote 101
      ```
      ```
      [*PE2-bfd-session-hello] quit
      ```
      ```
      [*PE2] e-trunk 10
      ```
      ```
      [*PE2-e-trunk-10] e-trunk track bfd-session session-name hello
      ```
      ```
      [*PE2-e-trunk-10] quit
      ```
      ```
      [*PE2] commit
      ```
      
      # Configure PE3.
      
      ```
      [~PE3] bfd hello bind peer-ip 2.2.2.2 source-ip 3.3.3.3
      ```
      ```
      [*PE3-bfd-session-hello] discriminator local 101
      ```
      ```
      [*PE3-bfd-session-hello] discriminator remote 100
      ```
      ```
      [*PE3-bfd-session-hello] quit
      ```
      ```
      [*PE3] e-trunk 10
      ```
      ```
      [*PE3-e-trunk-10] e-trunk track bfd-session session-name hello
      ```
      ```
      [*PE3-e-trunk-10] quit
      ```
      ```
      [*PE3] commit
      ```
6. Verify the configuration.
   1. Run the [**display bfd session all**](cmdqueryname=display+bfd+session+all) command on a PE to check whether the BFD session is Up. The following example uses the command output on PE1.
      
      
      ```
      [~PE1] display bfd session all
      ```
      ```
      (w): State in WTR 
      (*): State is invalid
      --------------------------------------------------------------------------------
      Local  Remote PeerIpAddr      State     Type      InterfaceName
      --------------------------------------------------------------------------------
      1000  1001   --.--.--.--     Up        S_PW(M)     LoopBack1
      2000  2001   --.--.--.--     Up        S_PW(M)     LoopBack2
      --------------------------------------------------------------------------------
           Total UP/DOWN Session Number : 2/0        
      ```
   2. Run the [**display e-trunk**](cmdqueryname=display+e-trunk) *trunk-id* command on PE2 and PE3 to check E-Trunk information. The following example uses the command output on PE2.
      
      
      ```
      [~PE2] display e-trunk 10
      ```
      ```
                                 The E-Trunk information
      E-Trunk-ID : 10                        Revert-Delay-Time (s) : 120
      Priority : 10                           System-ID : 00e0-fc00-1234
      Peer-IP : 3.3.3.3                       Source-IP : 2.2.2.2
      State : Master                          Causation : PRI
      Send-Period (100ms) : 10                Fail-Time (100ms) : 30
      Receive : 88                            Send : 122
      RecDrop : 0                             SndDrop : 0
      Peer-Priority : 20                      Peer-System-ID : 00e0-fc12-3456
      Peer-Fail-Time (100ms) : 30             BFD-Session : 100
      --------------------------------------------------------------------------------
                                  The Member information
      Type        ID  LocalPhyState   Work-Mode      State    Causation
      Eth-Trunk   10  Up              auto           Master   PEER_MEMBER_UP  
      ```
   3. Run the [**display mpls l2vc**](cmdqueryname=display+mpls+l2vc) command on a PE to check whether the **VC state** is **up**. The following example uses the command output on PE1.
      
      
      ```
      [~PE1] display mpls l2vc
      ```
      ```
       Total LDP VC : 4     4 up       0 down                                         
                                                                                      
       *client interface          : GigabitEthernet0/1/0.1 is up                           
        Administrator PW          : no                                                     
        session state             : up                                                     
        AC status                 : up                                                     
        VC state                  : up                                                     
        Label state               : 0                                                      
        Token state               : 0                                                      
        VC ID                     : 1                                                      
        VC type                   : VLAN                                                   
        destination               : 2.2.2.2                                                
        local VC label            : 1024         remote VC label      : 1025               
        control word              : disable                                                
        remote control word       : disable
        forwarding entry          : exist                                                  
        local group ID            : 0                                                      
        remote group ID           : 0
        local AC OAM State        : up
        local PSN OAM State       : up
        local forwarding state    : forwarding
        local status code         : 0x0
        remote AC OAM state       : up
        remote PSN OAM state      : up
        remote forwarding state   : forwarding
        remote status code        : 0x0
        ignore standby state      : no
        BFD for PW                : unavailable
        VCCV State                : up
        manual fault              : not set                                                
        active state              : active                                                 
        OAM Protocol              : --                                                     
        OAM Status                : --                                                     
        OAM Fault Type            : --                                                     
        PW APS ID                 : 0
        PW APS Status             : --
        TTL Value                 : 1                                                      
        link state                : up                                                     
        local VC MTU              : 1500         remote VC MTU        : 1500               
        local VCCV                : alert ttl lsp-ping bfd
        remote VCCV               : alert ttl lsp-ping bfd
        tunnel policy name        : policy                                                
        PW template name          : --                                                     
        primary or secondary      : primary                                                
        load balance type         : flow                                                   
        Access-port               : false                                                  
        Switchover Flag           : false
        VC tunnel info            : 1 tunnels
          NO.0  TNL type             : ldp   , TNL ID : 0x0000000001004c4e42
        create time               : 0 days, 0 hours, 27 minutes, 28 seconds                
        up time                   : 0 days, 0 hours, 24 minutes, 14 seconds                
        last change time          : 0 days, 0 hours, 24 minutes, 14 seconds                
        VC last up time           : 2014/09/20 14:00:58                                    
        VC total up time          : 0 days, 0 hours, 24 minutes, 14 seconds                
        CKey                      : 2                                                      
        NKey                      : 1                                                      
        PW redundancy mode        : independent
        AdminPw interface         : LoopBack1                                              
        AdminPw link state        : up                                                     
        Forward state             : send inactive, receive inactive 
        Diffserv Mode             : uniform                                                
        Service Class             : --                                                     
        Color                     : --                                                     
        DomainId                  : --                                                     
        Domain Name               : --                                                     
                                                                                      
       *client interface          : GigabitEthernet0/1/0.1 is up                           
        Administrator PW          : no                                                     
        session state             : up                                                     
        AC status                 : up                                                     
        VC state                  : up                                                     
        Label state               : 0                                                      
        Token state               : 0                                                      
        VC ID                     : 2                                                      
        VC type                   : VLAN                                                   
        destination               : 3.3.3.3                                                
        local VC label            : 1025         remote VC label      : 1025               
        control word              : disable                                                
        remote control word       : disable
        forwarding entry          : exist                                                  
        local group ID            : 0                                                      
        remote group ID           : 0
        local AC OAM State        : up
        local PSN OAM State       : up
        local forwarding state    : forwarding
        local status code         : 0x0
        remote AC OAM state        : up
        remote PSN OAM state      : up
        remote forwarding state   : forwarding
        remote status code        : 0x0
        ignore standby state      : no
        BFD for PW                : unavailable
        VCCV State                : up
        manual fault              : not set                                                
        active state              : inactive                                               
        OAM Protocol              : --                                                     
        OAM Status                : --                                                     
        OAM Fault Type            : --                                                     
        PW APS ID                 : 0
        PW APS Status             : --
        TTL Value                 : 1                                                      
        link state                : down                                                   
        local VC MTU              : 1500         remote VC MTU        : 1500               
        local VCCV                : alert ttl lsp-ping bfd
        remote VCCV               : alert ttl lsp-ping bfd
        tunnel policy name        : policy1                                                
        PW template name          : --                                                     
        primary or secondary      : secondary                                              
        load balance type         : flow                                                   
        Access-port               : false                                                  
        Switchover Flag           : false
        VC tunnel info            : 1 tunnels
          NO.0  TNL type          : ldp   , TNL ID : 0x0000000001004c4e43
        create time               : 0 days, 0 hours, 27 minutes, 15 seconds                
        up time                   : 0 days, 0 hours, 24 minutes, 23 seconds                
        last change time          : 0 days, 0 hours, 24 minutes, 23 seconds                
        VC last up time           : 2014/09/20 14:00:58                                    
        VC total up time          : 0 days, 0 hours, 24 minutes, 23 seconds                
        CKey                      : 4                                                      
        NKey                      : 3                                                      
        PW redundancy mode        : independent
        AdminPw interface         : LoopBack2                                              
        AdminPw link state        : up                                                     
        Forward state             : send inactive, receive inactive 
        Diffserv Mode             : uniform                                                
        Service Class             : --                                                     
        Color                     : --                                                     
        DomainId                  : --                                                     
        Domain Name               : --                                                     
                                                                                      
       *client interface          : LoopBack1 is up                                        
        Administrator PW          : yes                                                    
        session state             : up                                                     
        AC status                 : up                                                     
        VC state                  : up                                                     
        Label state               : 0                                                      
        Token state               : 0                                                      
        VC ID                     : 4                                                      
        VC type                   : IP-interworking                                        
        destination               : 2.2.2.2                                                
        local VC label            : 1026         remote VC label      : 1027               
        control word              : enable                                                 
        remote control word       : disable
        forwarding entry          : exist                                                  
        local group ID            : 0                                                      
        remote group ID           : 0
        local AC OAM State        : up
        local PSN OAM State       : up
        local forwarding state    : forwarding
        local status code         : 0x0
        remote AC OAM state       : up
        remote PSN OAM state      : up
        remote forwarding state   : forwarding
        remote status code        : 0x0
        ignore standby state      : no
        BFD for PW                : unavailable
        VCCV State                : up
        manual fault              : not set                                                
        active state              : active                                                 
        OAM Protocol              : --                                                     
        OAM Status                : --                                                     
        OAM Fault Type            : --                                                     
        PW APS ID                 : 0
        PW APS Status             : --
        TTL Value                 : 1                                                      
        link state                : up                                                     
        local VC MTU              : 1500         remote VC MTU        : 1500               
        local VCCV                : alert ttl lsp-ping bfd
        remote VCCV               : alert ttl lsp-ping bfd
        tunnel policy name        : policy                                                
        PW template name          : --                                                     
        primary or secondary      : primary                                                
        load balance type         : flow                                                   
        Switchover Flag           : false
        VC tunnel info            : 1 tunnels
          NO.0  TNL type          : ldp   , TNL ID : 0x0000000001004c4e44
        Access-port               : false                                                  
        create time               : 0 days, 0 hours, 23 minutes, 51 seconds                
        up time                   : 0 days, 0 hours, 22 minutes, 46 seconds                
        last change time          : 0 days, 0 hours, 22 minutes, 46 seconds                
        VC last up time           : 2014/09/20 14:02:43                                    
        VC total up time          : 0 days, 0 hours, 22 minutes, 46 seconds                
        CKey                      : 5                                                      
        NKey                      : 1                                                      
        PW redundancy mode        : independent
        Diffserv Mode             : uniform                                                
        Service Class             : --                                                     
        Color                     : --                                                     
        DomainId                  : --                                                     
        Domain Name               : --                                                     
                                                                                      
       *client interface          : LoopBack2 is up                                        
        Administrator PW          : yes                                                    
        session state             : up                                                     
        AC status                 : up                                                     
        VC state                  : up                                                     
        Label state               : 0                                                      
        Token state               : 0                                                      
        VC ID                     : 5                                                      
        VC type                   : IP-interworking                                        
        destination               : 3.3.3.3                                                
        local VC label            : 1027         remote VC label      : 1027               
        control word              : enable                                                 
        remote control word       : disable
       forwarding entry           : exist                                                  
        local group ID            : 0                                                      
        remote group ID           : 0
        local AC OAM State        : up
        local PSN OAM State       : up
        local forwarding state    : forwarding
        local status code         : 0x0
        remote AC OAM state       : up
        remote PSN OAM state      : up
        remote forwarding state   : forwarding
        remote status code        : 0x0
        ignore standby state      : no
        BFD for PW                : unavailable
        VCCV State                : up
        manual fault              : not set                                                
        active state              : active                                                 
        OAM Protocol              : --                                                     
        OAM Status                : --                                                     
        OAM Fault Type            : --                                                     
        PW APS ID                 : 0
        PW APS Status             : --
        TTL Value                 : 1                                                      
        link state                : up                                                     
        local VC MTU              : 1500         remote VC MTU        : 1500               
        local VCCV                : alert ttl lsp-ping bfd
        remote VCCV               : alert ttl lsp-ping bfd
        tunnel policy name        : policy                                                
        PW template name          : --                                                     
        primary or secondary      : primary                                                
        load balance type         : flow                                                   
        Access-port               : false                                                  
        Switchover Flag           : false
        VC tunnel info            : 1 tunnels
          NO.0  TNL type          : ldp   , TNL ID : 0x0000000001004c4e45
        create time               : 0 days, 0 hours, 23 minutes, 23 seconds                
        up time                   : 0 days, 0 hours, 21 minutes, 55 seconds                
        last change time          : 0 days, 0 hours, 21 minutes, 55 seconds                
        VC last up time           : 2014/09/20 14:03:41                                    
        VC total up time          : 0 days, 0 hours, 21 minutes, 55 seconds                
        CKey                      : 6                                                      
        NKey                      : 3                                                      
        PW redundancy mode        : independent
        Diffserv Mode             : uniform                                                
        Service Class             : --                                                     
        Color                     : --                                                     
        DomainId                  : --                                                     
        Domain Name               : --
      ```
   4. Configure CE1 to ping the VLANIF interface address of CE2.
      
      
      
      # Configure CE2.
      
      ```
      [~CE2] interface vlanif 10
      ```
      ```
      [*CE2-Vlanif10] ip address 10.1.1.2 24
      ```
      ```
      [*CE2-Vlanif10] quit
      ```
      ```
      [*CE2-Vlanif10] commit
      ```
      
      # Perform the ping operation.
      
      ```
      [~CE1] ping 10.1.1.2
      ```
      ```
      PING 10.1.1.2: 56  data bytes, press CTRL_C to break
          Reply from 10.1.1.2: bytes=56 Sequence=1 ttl=255 time=40 ms
          Reply from 10.1.1.2: bytes=56 Sequence=2 ttl=255 time=30 ms
          Reply from 10.1.1.2: bytes=56 Sequence=3 ttl=255 time=40 ms
          Reply from 10.1.1.2: bytes=56 Sequence=4 ttl=255 time=1 ms
          Reply from 10.1.1.2: bytes=56 Sequence=5 ttl=255 time=1 ms
      
        --- 10.1.1.2 ping statistics ---
          5 packet(s) transmitted
          5 packet(s) received
          0.00% packet loss
          round-trip min/avg/max = 1/22/40 ms  
      ```
   5. Simulate a fault and a fault recovery.
      
      
      
      Simulate a public network link fault between PE2 and PE1.
      
      # Disable GE 0/1/0 on PE2 to simulate a fault on the primary PW.![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      This step is used only to verify the configuration. Do not do this in practice.
      
      
      ```
      [~PE2] interface gigabitethernet 0/1/0
      ```
      ```
      [~PE2-GigabitEthernet0/1/0] shutdown
      ```
      ```
      [*PE2-GigabitEthernet0/1/0] commit
      ```
      
      Then run the **display mpls l2vc** command on PE1. The command output shows that the VC status of the mPW and service PW between PE1 and PE2 is **down** and the VC status of the mPW and service PW between PE1 and PE3 is **up**.
      
      ```
      [~PE1] display mpls l2vc
      ```
      ```
       Total LDP VC : 4     2 up       2 down                                         
                                                                                      
       *client interface          : GigabitEthernet0/1/0.1 is up                           
        Administrator PW          : no                                                     
        session state             : up                                                     
        AC status                 : up                                                     
        VC state                  : down                                                   
        Label state               : 0                                                      
        Token state               : 0                                                      
        VC ID                     : 1                                                      
        VC type                   : VLAN                                                   
        destination               : 2.2.2.2                                                
        local VC label            : 1024         remote VC label      : 1025               
        control word              : disable                                                
        remote control word       : disable
        forwarding entry          : not exist                                              
        local group ID            : 0                                                      
        remote group ID           : 0
        local AC OAM State        : up
        local PSN OAM State       : up
        local forwarding state    : forwarding
        local status code         : 0x0
        remote AC OAM state       : up
        remote PSN OAM state      : up
        remote forwarding state   : forwarding
        remote status code        : 0x0
        ignore standby state      : no
        BFD for PW                : unavailable
        VCCV State                : up
        manual fault              : not set                                                
        active state              : inactive                                               
        OAM Protocol              : --                                                     
        OAM Status                : --                                                     
        OAM Fault Type            : --                                                     
        PW APS ID                 : 0 
        PW APS Status             : --
        TTL Value                 : 1                                                      
        link state                : down                                                   
        local VC MTU              : 1500         remote VC MTU        : 1500               
        local VCCV                : alert ttl lsp-ping bfd
        remote VCCV               : alert ttl lsp-ping bfd
        tunnel policy name        : policy                                                
        PW template name          : --                                                     
        primary or secondary      : primary                                                
        load balance type         : flow                                                   
        Access-port               : false                                                  
        Switchover Flag           : false
        VC tunnel info            : 1 tunnels
          NO.0  TNL type          : ldp   , TNL ID : 0x0000000001004c4e42
        create time               : 0 days, 0 hours, 28 minutes, 50 seconds                
        up time                   : 0 days, 0 hours, 0 minutes, 0 seconds                  
        last change time          : 0 days, 0 hours, 0 minutes, 12 seconds                 
        VC last up time           : 2014/09/20 14:00:58                                    
        VC total up time          : 0 days, 0 hours, 25 minutes, 24 seconds                
        CKey                      : 2                                                      
        NKey                      : 1                                                      
        PW redundancy mode        : independent
        AdminPw interface         : LoopBack1                                              
        AdminPw link state        : down                                                   
        Forward state             : send inactive, receive inactive 
        Diffserv Mode             : uniform                                                
        Service Class             : --                                                     
        Color                     : --                                                     
        DomainId                  : --                                                     
        Domain Name               : --                                                     
                                                                                      
       *client interface          : GigabitEthernet0/1/0.1 is up                           
        Administrator PW          : no                                                     
        session state             : up                                                     
        AC status                 : up                                                     
        VC state                  : up                                                     
        Label state               : 0                                                      
        Token state               : 0                                                      
        VC ID                     : 2                                                      
        VC type                   : VLAN                                                   
        destination               : 3.3.3.3                                                
        local VC label            : 1025         remote VC label      : 1025               
        control word              : disable                                                
        remote control word       : disable
        forwarding entry          : exist                                                  
        local group ID            : 0                                                      
        remote group ID           : 0
        local AC OAM State        : up
        local PSN OAM State       : up
        local forwarding state    : forwarding
        local status code         : 0x0
        remote AC OAM state       : up
        remote PSN OAM state      : up
        remote forwarding state   : forwarding
        remote status code        : 0x0
        ignore standby state      : no
        BFD for PW                : unavailable
        VCCV State                : up
        manual fault              : not set                                                
        active state              : active                                                 
        OAM Protocol              : --                                                     
        OAM Status                : --                                                     
        OAM Fault Type            : --   
        PW APS ID                 : 0 
        PW APS Status             : --                                                     
        TTL Value                 : 1                                                      
        link state                : up                                                     
        local VC MTU              : 1500         remote VC MTU        : 1500               
        local VCCV                : alert ttl lsp-ping bfd
        remote VCCV               : alert ttl lsp-ping bfd
        tunnel policy name        : policy1                                                
        PW template name          : --                                                     
        primary or secondary      : secondary                                              
        load balance type         : flow                                                   
        Access-port               : false                                                  
       Switchover Flag            : false
        VC tunnel info            : 1 tunnels
          NO.0  TNL type          : ldp   , TNL ID : 0x0000000001004c4e43
        create time               : 0 days, 0 hours, 28 minutes, 37 seconds                
        up time                   : 0 days, 0 hours, 25 minutes, 45 seconds                
        last change time          : 0 days, 0 hours, 25 minutes, 45 seconds                
        VC last up time           : 2014/09/20 14:00:58                                    
        VC total up time          : 0 days, 0 hours, 25 minutes, 45 seconds                
        CKey                      : 4                                                      
        NKey                      : 3                                                      
        PW redundancy mode        : independent
        AdminPw interface         : LoopBack2                                              
        AdminPw link state        : up                                                     
        Forward state             : send inactive, receive inactive 
        Diffserv Mode             : uniform                                                
        Service Class             : --                                                     
        Color                     : --                                                     
        DomainId                  : --                                                     
        Domain Name               : --                                                     
                                                                                      
       *client interface          : LoopBack1 is up                                        
        Administrator PW          : yes                                                    
        session state             : up                                                     
        AC status                 : up                                                     
        VC state                  : down                                                   
        Label state               : 0                                                      
        Token state               : 0                                                      
        VC ID                     : 4                                                      
        VC type                   : IP-interworking                                        
        destination               : 2.2.2.2                                                
        local VC label            : 1026         remote VC label      : 1027               
        control word              : enable                                                 
        remote control word       : disable
        forwarding entry          : not exist                                              
        local group ID            : 0                                                      
        remote group ID           : 0
        local AC OAM State        : up
        local PSN OAM State       : up
        local forwarding state    : forwarding
        local status code         : 0x0
        remote AC OAM state       : up
        remote PSN OAM state      : up
        remote forwarding state   : forwarding
        remote status code        : 0x0
        ignore standby state      : no
        BFD for PW                : unavailable
        VCCV State                : up
        manual fault              : not set                                                
        active state              : inactive                                               
        OAM Protocol              : --                                                     
        OAM Status                : --                                                     
        OAM Fault Type            : --
        PW APS ID                 : 0 
        PW APS Status             : --                                             
        TTL Value                 : 1                                                      
        link state                : down                                                   
        local VC MTU              : 1500         remote VC MTU        : 1500               
        local VCCV                : alert ttl lsp-ping bfd
        remote VCCV               : alert ttl lsp-ping bfd
        tunnel policy name        : policy                                                
        PW template name          : --                                                     
        primary or secondary      : primary                                                
        load balance type         : flow                                                   
        Access-port               : false                                                  
        Switchover Flag           : false
        VC tunnel info            : 1 tunnels
          NO.0  TNL type          : ldp   , TNL ID : 0x0000000001004c4e44
        create time               : 0 days, 0 hours, 25 minutes, 15 seconds                
        up time                   : 0 days, 0 hours, 0 minutes, 0 seconds                  
        last change time          : 0 days, 0 hours, 0 minutes, 31 seconds                 
        VC last up time           : 2014/09/20 14:02:43                                    
        VC total up time          : 0 days, 0 hours, 23 minutes, 39 seconds                
        CKey                      : 5                                                      
        NKey                      : 1                                                      
        PW redundancy mode        : independent
        Diffserv Mode             : uniform                                                
        Service Class             : --                                                     
        Color                     : --                                                     
        DomainId                  : --                                                     
        Domain Name               : --                                                     
                                                                                      
       *client interface          : LoopBack2 is up                                        
        Administrator PW          : yes                                                    
        session state             : up                                                     
        AC status                 : up                                                     
        VC state                  : up                                                     
        Label state               : 0                                                      
        Token state               : 0                                                      
        VC ID                     : 5                                                      
        VC type                   : IP-interworking                                        
        destination               : 3.3.3.3                                                
        local VC label            : 1027         remote VC label      : 1027               
        control word              : enable                                                 
        remote control word       : disable
        forwarding entry          : exist                                                  
        local group ID            : 0                                                      
        remote group ID           : 0
        local AC OAM State        : up
        local PSN OAM State       : up
        local forwarding state    : forwarding
        local status code         : 0x0
        remote AC OAM state       : up
        remote PSN OAM state      : up
        remote forwarding state   : forwarding
        remote status code        : 0x0
        ignore standby state      : no
        BFD for PW                : unavailable
        VCCV State                : up
        manual fault              : not set                                                
        active state              : active                                                 
        OAM Protocol              : --                                                     
        OAM Status                : --                                                     
        OAM Fault Type            : --    
        PW APS ID                 : 0 
        PW APS Status             : --                                                  
        TTL Value                 : 1                                                      
        link state                : up                                                     
        local VC MTU              : 1500         remote VC MTU        : 1500               
        local VCCV                : alert ttl lsp-ping bfd
        remote VCCV               : alert ttl lsp-ping bfd
        tunnel policy name        : policy                                                
        PW template name          : --                                                     
        primary or secondary      : primary                                                
        load balance type         : flow                                                   
        Access-port               : false                                                  
        Switchover Flag           : false
        VC tunnel info            : 1 tunnels
          NO.0  TNL type          : ldp   , TNL ID : 0x0000000001004c4e45
        create time               : 0 days, 0 hours, 24 minutes, 50 seconds                
        up time                   : 0 days, 0 hours, 23 minutes, 22 seconds                
        last change time          : 0 days, 0 hours, 23 minutes, 22 seconds                
        VC last up time           : 2014/09/20 14:03:41                                    
        VC total up time          : 0 days, 0 hours, 23 minutes, 22 seconds                
        CKey                      : 6                                                      
        NKey                      : 3                                                      
        PW redundancy mode        : independent
        Diffserv Mode             : uniform                                                
        Service Class             : --                                                     
        Color                     : --                                                     
        DomainId                  : --                                                     
        Domain Name               : --
      ```
      
      # Enable GE 0/1/0 on PE2 to simulate a link fault recovery of the primary PW.
      
      ```
      [~PE2] interface gigabitethernet 0/1/0
      ```
      ```
      [~PE2-GigabitEthernet0/1/0] undo shutdown
      ```
      ```
      [*PE2-GigabitEthernet0/1/0] quit
      ```
      ```
      [*PE2] commit
      ```
      
      The link that bears the primary PW has restored, but it takes a period of time for the primary PW to be established. Therefore, traffic still travels along the secondary PW. After the primary PW is established, run the **display mpls l2vc** command on PE1. The command output shows that the VC status of the mPW and service PW between PE1 and PE2 has become **up**.
      
      ```
      [~PE1] display mpls l2vc
      ```
      ```
       Total LDP VC : 4     4 up       0 down                                         
                                                                                      
       *client interface          : GigabitEthernet0/1/0.1 is up                           
        Administrator PW          : no                                                     
        session state             : up                                                     
        AC status                 : up                                                     
        VC state                  : up                                                     
        Label state               : 0                                                      
        Token state               : 0                                                      
        VC ID                     : 1                                                      
        VC type                   : VLAN                                                   
        destination               : 2.2.2.2                                                
        local VC label            : 1024         remote VC label      : 1025               
        control word              : disable                                                
        remote control word       : disable
        forwarding entry          : exist                                                  
        local group ID            : 0                                                      
        remote group ID           : 0
        local AC OAM State        : up
        local PSN OAM State       : up
        local forwarding state    : forwarding
        local status code         : 0x0
        remote AC OAM state       : up
        remote PSN OAM state      : up
        remote forwarding state   : forwarding
        remote status code        : 0x0
        ignore standby state      : no
        BFD for PW                : unavailable
        VCCV State                : up
        manual fault              : not set                                                
        active state              : active                                                 
        OAM Protocol              : --                                                     
        OAM Status                : --                                                     
        OAM Fault Type            : --   
        PW APS ID                 : 0 
        PW APS Status             : --                                                    
        TTL Value                 : 1                                                      
        link state                : up                                                     
        local VC MTU              : 1500         remote VC MTU        : 1500               
        local VCCV                : alert ttl lsp-ping bfd
        remote VCCV               : alert ttl lsp-ping bfd
        tunnel policy name        : policy                                                
        PW template name          : --                                                     
        primary or secondary      : primary                                                
        load balance type         : flow                                                   
        Access-port               : false                                                  
        Switchover Flag           : false
        VC tunnel info            : 1 tunnels
          NO.0  TNL type          : ldp   , TNL ID : 0x0000000001004c4e42
        create time               : 0 days, 0 hours, 31 minutes, 46 seconds                
        up time                   : 0 days, 0 hours, 0 minutes, 19 seconds                 
        last change time          : 0 days, 0 hours, 0 minutes, 19 seconds                 
        VC last up time           : 2014/09/20 14:29:11                                    
        VC total up time          : 0 days, 0 hours, 25 minutes, 43 seconds                
        CKey                      : 2                                                      
        NKey                      : 1                                                      
        PW redundancy mode        : independent
        AdminPw interface         : LoopBack1                                              
        AdminPw link state        : up                                                     
        Forward state             : send inactive, receive inactive 
        Diffserv Mode             : uniform                                                
        Service Class             : --                                                     
        Color                     : --                                                     
        DomainId                  : --                                                     
        Domain Name               : --                                                     
                                                                                      
       *client interface          : GigabitEthernet0/1/0.1 is up                           
        Administrator PW          : no                                                     
        session state             : up                                                     
        AC status                 : up                                                     
        VC state                  : up                                                     
        Label state               : 0                                                      
        Token state               : 0                                                      
        VC ID                     : 2                                                      
        VC type                   : VLAN                                                   
        destination               : 3.3.3.3                                                
        local VC label            : 1025         remote VC label      : 1025               
        control word              : disable                                                
        remote control word       : disable
        forwarding entry          : exist                                                  
        local group ID            : 0                                                      
        remote group ID           : 0
        local AC OAM State        : up
        local PSN OAM State       : up
        local forwarding state    : forwarding
        local status code         : 0x0
        remote AC OAM state       : up
        remote PSN OAM state      : up
        remote forwarding state   : forwarding
        remote status code        : 0x0
        ignore standby state      : no
        BFD for PW                : unavailable
        VCCV State                : up
        manual fault              : not set                                                
        active state              : inactive                                               
        OAM Protocol              : --                                                     
        OAM Status                : --                                                     
        OAM Fault Type            : --  
        PW APS ID                 : 0 
        PW APS Status             : --                                                     
        TTL Value                 : 1                                                      
        link state                : down                                                   
        local VC MTU              : 1500         remote VC MTU        : 1500               
        local VCCV                : alert ttl lsp-ping bfd
        remote VCCV               : alert ttl lsp-ping bfd
        tunnel policy name        : policy1                                                
        PW template name          : --                                                     
        primary or secondary      : secondary                                              
        load balance type         : flow                                                   
        Access-port               : false                                                  
        Switchover Flag           : false
        VC tunnel info            : 1 tunnels
          NO.0  TNL type          : ldp   , TNL ID : 0x0000000001004c4e43
        create time               : 0 days, 0 hours, 31 minutes, 27 seconds                
        up time                   : 0 days, 0 hours, 28 minutes, 35 seconds                
        last change time          : 0 days, 0 hours, 28 minutes, 35 seconds                
        VC last up time           : 2014/09/20 14:00:58                                    
        VC total up time          : 0 days, 0 hours, 28 minutes, 35 seconds                
        CKey                      : 4                                                      
        NKey                      : 3                                                      
        PW redundancy mode        : independent
        AdminPw interface         : LoopBack2                                              
        AdminPw link state        : up                                                     
        Forward state             : send inactive, receive inactive 
        Diffserv Mode             : uniform                                                
        Service Class             : --                                                     
        Color                     : --                                                     
        DomainId                  : --                                                     
        Domain Name               : --                                                     
                                                                                      
       *client interface          : LoopBack1 is up                                        
        Administrator PW          : yes                                                    
        session state             : up                                                     
        AC status                 : up                                                     
        VC state                  : up                                                     
        Label state               : 0                                                      
        Token state               : 0                                                      
        VC ID                     : 4                                                      
        VC type                   : IP-interworking                                        
        destination               : 2.2.2.2                                                
        local VC label            : 1026         remote VC label      : 1027               
        control word              : enable                                                 
        remote control word       : disable
        forwarding entry          : exist                                                  
        local group ID            : 0                                                      
        remote group ID           : 0
        local AC OAM State        : up
        local PSN OAM State       : up
        local forwarding state    : forwarding
        local status code         : 0x0
        remote AC OAM state       : up
        remote PSN OAM state      : up
        remote forwarding state   : forwarding
        remote status code        : 0x0
        ignore standby state      : no
        BFD for PW                : unavailable
        VCCV State                : up
        manual fault              : not set                                                
        active state              : active                                                 
        OAM Protocol              : --                                                     
        OAM Status                : --                                                     
        OAM Fault Type            : --   
        PW APS ID                 : 0 
        PW APS Status             : --                                                    
        TTL Value                 : 1                                                      
        link state                : up                                                     
        local VC MTU              : 1500         remote VC MTU        : 1500               
        local VCCV                : alert ttl lsp-ping bfd
        remote VCCV               : alert ttl lsp-ping bfd
        tunnel policy name        : policy                                                
        PW template name          : --                                                     
        primary or secondary      : primary                                                
        load balance type         : flow                                                   
        Access-port               : false                                                  
        Switchover Flag           : false
        VC tunnel info            : 1 tunnels
          NO.0  TNL type          : ldp   , TNL ID : 0x0000000001004c4e44
        create time               : 0 days, 0 hours, 27 minutes, 56 seconds                
        up time                   : 0 days, 0 hours, 0 minutes, 23 seconds                 
        last change time          : 0 days, 0 hours, 0 minutes, 23 seconds                 
        VC last up time           : 2014/09/20 14:29:11                                    
        VC total up time          : 0 days, 0 hours, 24 minutes, 2 seconds                 
        CKey                      : 5                                                      
        NKey                      : 1                                                      
        PW redundancy mode        : independent
        Diffserv Mode             : uniform                                                
        Service Class             : --                                                     
        Color                     : --                                                     
        DomainId                  : --                                                     
        Domain Name               : --                                                     
                                                                                      
       *client interface          : LoopBack2 is up                                        
        Administrator PW          : yes                                                    
        session state             : up                                                     
        AC status                 : up                                                     
        VC state                  : up                                                     
        Label state               : 0                                                      
        Token state               : 0                                                      
        VC ID                     : 5                                                      
        VC type                   : IP-interworking                                        
        destination               : 3.3.3.3                                                
        local VC label            : 1027         remote VC label      : 1027               
        control word              : enable                                                 
        remote control word       : disable
        forwarding entry          : exist                                                  
        local group ID            : 0                                                      
        remote group ID           : 0
        local AC OAM State        : up
        local PSN OAM State       : up
        local forwarding state    : forwarding
        local status code         : 0x0
        remote AC OAM state       : up
        remote PSN OAM state      : up
        remote forwarding state   : forwarding
        remote status code        : 0x0
        ignore standby state      : no
        BFD for PW                : unavailable
        VCCV State                : up
        manual fault              : not set                                                
        active state              : active                                                 
        OAM Protocol              : --                                                     
        OAM Status                : --                                                     
        OAM Fault Type            : --                                                     
        PW APS ID                 : 0 
        PW APS Status             : --
        TTL Value                 : 1                                                      
        link state                : up                                                     
        local VC MTU              : 1500         remote VC MTU        : 1500               
        local VCCV                : alert ttl lsp-ping bfd
        remote VCCV               : alert ttl lsp-ping bfd
        tunnel policy name        : policy                                                
        PW template name          : --                                                     
        primary or secondary      : primary                                                
        load balance type         : flow                                                   
        Access-port               : false                                                  
        Switchover Flag           : false
        VC tunnel info            : 1 tunnels
          NO.0  TNL type          : ldp   , TNL ID : 0x0000000001004c4e45
        create time               : 0 days, 0 hours, 27 minutes, 25 seconds                
        up time                   : 0 days, 0 hours, 25 minutes, 57 seconds                
        last change time          : 0 days, 0 hours, 25 minutes, 57 seconds                
        VC last up time           : 2014/09/20 14:03:41                                    
        VC total up time          : 0 days, 0 hours, 25 minutes, 57 seconds                
        CKey                      : 6                                                      
        PW redundancy mode        : independent
        NKey                      : 3                                                      
        Diffserv Mode             : uniform                                                
        Service Class             : --                                                     
        Color                     : --                                                     
        DomainId                  : --                                                     
        Domain Name               : --
      ```

#### Configuration Files

* CE1 configuration file
  
  ```
  #
   sysname CE1
  #
  interface GigabitEthernet0/1/0
   undo shutdown
  #
  interface GigabitEthernet0/1/0.1
   vlan-type dot1q 10
   ip address 10.1.1.1 255.255.255.0
  #
  return                 
  ```
* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  bfd
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
   mpls te
   mpls rsvp-te
   mpls te cspf
  #
  mpls l2vpn
  #
  explicit-path tope2
   next hop 10.1.2.2
   next hop 2.2.2.2
  #
  explicit-path tope3
   next hop 10.1.3.2
   next hop 3.3.3.3
  #
  mpls ldp
  #
  mpls ldp remote-peer 2.2.2.2
   remote-ip 2.2.2.2
  #
  mpls ldp remote-peer 3.3.3.3
   remote-ip 3.3.3.3
  #
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.255
  #
  interface LoopBack1
   mpls l2vc 2.2.2.2 4 tunnel-policy policy control-word admin
  #
  interface LoopBack2
   mpls l2vc 3.3.3.3 5 tunnel-policy policy1 control-word admin
  #
  interface Tunnel11
   ip address unnumbered interface LoopBack0
   tunnel-protocol mpls te
   destination 2.2.2.2
   mpls te tunnel-id 100
   mpls te path explicit-path tope2
   mpls te reserved-for-binding
  #
  interface Tunnel12
   ip address unnumbered interface LoopBack0
   tunnel-protocol mpls te
   destination 3.3.3.3
   mpls te tunnel-id 200
   mpls te path explicit-path tope3
   mpls te reserved-for-binding
  #
  tunnel-policy policy
   tunnel binding destination 2.2.2.2 te Tunnel11
  #
  tunnel-policy policy1
   tunnel binding destination 3.3.3.3 te Tunnel12
  #
  interface GigabitEthernet0/1/0
   undo shutdown
  #
  interface GigabitEthernet0/1/0.1
   vlan-type dot1q 10
   mpls l2vc 2.2.2.2 1 tunnel-policy policy
   mpls l2vc track admin-vc interface LoopBack1
   mpls l2vc 3.3.3.3 2 tunnel-policy policy1 secondary
   mpls l2vc secondary track admin-vc interface LoopBack2
   mpls l2vpn redundancy independent
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.2.1 255.255.255.0
   mpls
   mpls te
   mpls rsvp-te
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.1.3.1 255.255.255.0
   mpls
   mpls te
   mpls rsvp-te
  #
  ospf 1
   opaque-capability enable
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 10.1.2.0 0.0.0.255
    network 10.1.3.0 0.0.0.255
    mpls-te enable
  #
  bfd pe1a bind pw interface LoopBack1
   discriminator local 1000
   discriminator remote 1001
  #
  bfd pe1b bind pw interface LoopBack2
   discriminator local 2000
   discriminator remote 2001
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  lacp e-trunk system-id 00e0-fc00-0000
  lacp e-trunk priority 100
  #
  e-trunk 10
  #
  bfd
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
   mpls te
   mpls rsvp-te
   mpls te cspf
  #
  mpls l2vpn
  #
  explicit-path tope1
   next hop 10.1.2.1
   next hop 1.1.1.1
  #
  mpls ldp
  #
  mpls ldp remote-peer 1.1.1.1
   remote-ip 1.1.1.1
  #
  interface LoopBack0
   ip address 2.2.2.2 255.255.255.255
  #
  interface LoopBack1
   mpls l2vc 1.1.1.1 4 tunnel-policy policy1 control-word admin
  #
  interface Tunnel10
   ip address unnumbered interface LoopBack0
   tunnel-protocol mpls te
   destination 1.1.1.1
   mpls te tunnel-id 100
   mpls te path explicit-path tope1
   mpls te reserved-for-binding
  #
  tunnel-policy policy1
   tunnel binding destination 1.1.1.1 te Tunnel10
  #
  bfd hello bind peer-ip 3.3.3.3 source-ip 2.2.2.2
   discriminator local 100
   discriminator remote 101
  #
  interface Eth-Trunk10
   mode lacp-static
   e-trunk 10
  #
  interface Eth-Trunk10.1
   vlan-type dot1q 10
   mpls l2vc 1.1.1.1 1 tunnel-policy policy1
   mpls l2vc track admin-vc interface LoopBack1
   mpls l2vc 3.3.3.3 3 bypass
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.2.2 255.255.255.0
   mpls
   mpls te
   mpls rsvp-te
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.4.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   eth-trunk 10
  #
  ospf 1
   opaque-capability enable
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 10.1.2.0 0.0.0.255
    network 10.1.4.0 0.0.0.255
    mpls-te enable
  #
  bfd pe2 bind pw interface LoopBack1
   discriminator local 1001
   discriminator remote 1000
  #
  e-trunk 10
   security-key cipher YsHsjx_202206
   priority 10
   peer-address 3.3.3.3 source-address 2.2.2.2
   e-trunk track bfd-session session-name hello
  #
  return 
  ```
* PE3 configuration file
  
  ```
  #
  sysname PE3
  #
  lacp e-trunk system-id 00e0-fc00-0000
  lacp e-trunk priority 100
  #
  e-trunk 10
  #
  bfd
  #
  mpls lsr-id 3.3.3.3
  #
  mpls
   mpls te
   mpls rsvp-te
   mpls te cspf
  #
  mpls l2vpn
  #
  explicit-path tope1
   next hop 10.1.3.1
   next hop 1.1.1.1
  #
  mpls ldp
  #
  mpls ldp remote-peer 1.1.1.1
   remote-ip 1.1.1.1
  #
  interface LoopBack0
   ip address 3.3.3.3 255.255.255.255
  #
  interface LoopBack1
   mpls l2vc 1.1.1.1 5 tunnel-policy policy1 control-word admin
  #
  interface Tunnel10
   ip address unnumbered interface LoopBack0
   tunnel-protocol mpls te
   destination 1.1.1.1
   mpls te tunnel-id 200
   mpls te path explicit-path tope1
   mpls te reserved-for-binding
  #
  tunnel-policy policy1
   tunnel binding destination 1.1.1.1 te Tunnel10
  #
  bfd hello bind peer-ip 2.2.2.2 source-ip 3.3.3.3
   discriminator local 101
   discriminator remote 100
  #
  interface Eth-Trunk10
   mode lacp-static
   e-trunk 10
  #
  interface Eth-Trunk10.1
   vlan-type dot1q 10
   mpls l2vc 1.1.1.1 2 tunnel-policy policy1
   mpls l2vc track admin-vc interface LoopBack1
   mpls l2vc 2.2.2.2 3 bypass
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.3.2 255.255.255.0
   mpls
   mpls te
   mpls rsvp-te
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.4.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   eth-trunk 10
  #
  ospf 1
   opaque-capability enable
   area 0.0.0.0
    network 3.3.3.3 0.0.0.0
    network 10.1.3.0 0.0.0.255
    network 10.1.4.0 0.0.0.255
    mpls-te enable
  #
  bfd pe3 bind pw interface LoopBack1
   discriminator local 2001
   discriminator remote 2000
  #
  e-trunk 10
   security-key cipher YsHsjx_202206
   priority 20
   peer-address 2.2.2.2 source-address 3.3.3.3
   e-trunk track bfd-session session-name hello
  #
  return
  ```
* CE2 configuration file
  
  ```
  #
  sysname CE2
  #
  vlan batch 10
  #
  interface Vlanif10
   ip address 10.1.1.2 255.255.255.0
  #
  interface Eth-Trunk10
   portswitch
   port trunk allow-pass vlan 10
   mode lacp-static
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   eth-trunk 10
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   eth-trunk 10
  #
  return
  ```