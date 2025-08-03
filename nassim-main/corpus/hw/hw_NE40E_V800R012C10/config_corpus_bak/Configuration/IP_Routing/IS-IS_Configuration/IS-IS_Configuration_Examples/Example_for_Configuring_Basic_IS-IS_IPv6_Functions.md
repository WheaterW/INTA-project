Example for Configuring Basic IS-IS IPv6 Functions
==================================================

This section describes how to configure basic IS-IS IPv6 functions, including enabling IPv6 globally, configuring an IPv6 address and enabling IPv6 for each interface, and configuring basic IS-IS functions and enabling IPv6.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172366108__fig_dc_vrp_isis_cfg_008901):

* Device A, Device B, Device C, and Device D belong to the same AS. It is required that IS-IS run on them to implement IPv6 interworking.
* Device A, Device B, and Device C belong to Area 10, and Device D belongs to Area 20.
* Device A and Device B are Level-1 devices; Device C is a Level-1-2 device; Device D is a Level-2 device.

**Figure 1** Configuring basic IS-IS IPv6 functions  
![](images/fig_dc_vrp_isis_cfg_008901.png)

| Device Name | Interface | IP Address |
| --- | --- | --- |
| Device A | GE 0/1/0 | 2001:db8:1::2/64 |
| Device B | GE 0/1/0 | 2001:db8:2::2/64 |
| Device C | GE 0/1/0 | 2001:db8:1::1/64 |
| GE0/2/0 | 2001:db8:2::1/64 |
| GE 0/3/0 | 2001:db8:3::1/64 |
| Device D | GE 0/1/0 | 2001:db8:3::2/64 |
| GE 0/2/0 | 2001:db8:4::1/64 |



#### Precautions

To improve security, you are advised to configure IS-IS authentication. For details, see "Configuring IS-IS Authentication." IS-IS interface authentication is used as an example. For details, see Example for Configuring Basic IS-IS Functions.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable the IPv6 forwarding capability on each Router, and configure an IPv6 address for each interface.
2. Enable IS-IS, configure the level, and specify the NET on each Router.

#### Data Preparation

To complete the configuration, you need the following data:

* IPv6 addresses of the interfaces on Device A, Device B, Device C, and Device D
* Areas of Device A, Device B, Device C, and Device D
* Levels of Device A, Device B, Device C, and Device D

#### Procedure

1. Enable IPv6, and configure an IPv6 address for each interface. Use the command output on Device A as an example. The configurations of the other three Routers are the same as that of Device A. For configuration details, see [Configuration Files](#EN-US_TASK_0172366108__section_dc_vrp_isis_cfg_008905) in this section.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface gigabitethernet 0/1/0
   [~DeviceA-GigabitEthernet0/1/0] ipv6 enable
   [*DeviceA-GigabitEthernet0/1/0] ipv6 address 2001:db8:1::2 64
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
2. Configure IS-IS.
   
   
   
   # Configure Device A.
   
   ```
   [~DeviceA] isis 1
   ```
   ```
   [*DeviceA-isis-1] is-level level-1
   ```
   ```
   [*DeviceA-isis-1] network-entity 10.0000.0000.0001.00
   ```
   ```
   [*DeviceA-isis-1] ipv6 enable topology ipv6
   ```
   ```
   [*DeviceA-isis-1] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] isis ipv6 enable 1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] quit
   ```
   
   # Configure Device B.
   
   ```
   [~DeviceB] isis 1 
   ```
   ```
   [*DeviceB-isis-1] is-level level-1
   ```
   ```
   [*DeviceB-isis-1] network-entity 10.0000.0000.0002.00
   ```
   ```
   [*DeviceB-isis-1] ipv6 enable topology ipv6
   ```
   ```
   [*DeviceB-isis-1] quit
   ```
   ```
   [*DeviceB] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] isis ipv6 enable 1
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] quit
   ```
   
   # Configure Device C.
   
   ```
   [~DeviceC] isis 1
   ```
   ```
   [*DeviceC-isis-1] network-entity 10.0000.0000.0003.00
   ```
   ```
   [*DeviceC-isis-1] ipv6 enable topology ipv6
   ```
   ```
   [*DeviceC-isis-1] quit
   ```
   ```
   [*DeviceC] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] isis ipv6 enable 1
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceC] interface gigabitethernet 0/2/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] isis ipv6 enable 1
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceC] interface gigabitethernet 0/3/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/3/0] isis ipv6 enable 1
   ```
   ```
   [*DeviceC-GigabitEthernet0/3/0] isis circuit-level level-1-2
   ```
   ```
   [*DeviceC-GigabitEthernet0/3/0] commit
   ```
   ```
   [~DeviceC-GigabitEthernet0/3/0] quit
   ```
   
   # Configure Device D.
   
   ```
   [~DeviceD] isis 1 
   ```
   ```
   [*DeviceD-isis-1] is-level level-2
   ```
   ```
   [*DeviceD-isis-1] network-entity 20.0000.0000.0004.00
   ```
   ```
   [*DeviceD-isis-1] ipv6 enable topology ipv6
   ```
   ```
   [*DeviceD-isis-1] quit
   ```
   ```
   [*DeviceD] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] isis ipv6 enable 1
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceD] interface gigabitethernet 0/2/0
   ```
   ```
   [*DeviceD-GigabitEthernet0/2/0] isis ipv6 enable 1
   ```
   ```
   [*DeviceD-GigabitEthernet0/2/0] commit
   ```
   ```
   [~DeviceD-GigabitEthernet0/2/0] quit
   ```
3. Verify the configuration.
   
   
   
   # Display the IS-IS routing table of Device A. The command output shows that Device A has the routes to each network segment of the Level-1 area.
   
   ```
   [~DeviceA] display isis route
   
                            Route information for ISIS(1)
                            -----------------------------
   
                           ISIS(1) Level-1 Forwarding Table
                           --------------------------------
   
   IPV6 Dest.         ExitInterface                 NextHop                  Cost         Flags
   ----------------------------------------------------------------------------------------------
    ::/0              GigabitEthernet0/1/0          FE80::A83E:0:3ED2:1      10           A/-/-/-
    2001:db8:1::/64   GigabitEthernet0/1/0          Direct                   10           D/L/-/-
    2001:db8:2::/64   GigabitEthernet0/1/0          FE80::A83E:0:3ED2:1      20           A/-/-/-
   
        Flags: D-Direct, A-Added to URT, L-Advertised in LSPs, S-IGP Shortcut,
                                    U-Up/Down Bit Set, LP-Local Prefix-Sid
        Protect Type: L-Link Protect, N-Node Protect
   ```
   
   # Display detailed information about IS-IS neighbors on Device C.
   
   ```
   [~DeviceC] display isis peer verbose
                          Peer Verbose information for ISIS(1)                            
     System Id        Interface              Circuit Id              State  HoldTime   Type    PRI 
   -----------------------------------------------------------------------------------------------
   0000.0000.0001*    GigabitEthernet0/1/0   0000.0000.0003.01        Up     24s        L1     64
     MT IDs supported     : 2(UP) 
     Local MT IDs         : 2
     Area Address(es)     : 10
     Peer IPv6 Address(es): FE80::996B:0:9419:1
     Peer IPv6 GlbAddr(es): 2001:db8:1::2
     Uptime               : 00h00m15s
     Peer Up Time         : 2020-06-08 01:41:57
     Adj Protocol         : IPV6
     Restart Capable      : YES
     Suppressed Adj       : NO 
     Peer System ID       : 0000.0000.0001
     BFD Incr-Cost State  : MT0 : NO / MT2 : NO
     MT IDs BFD Required  : 0(IPv4:FALSE IPv6:FALSE) 2(IPv6:FALSE)
     Reverse Cost State   : -- 
   
   0000.0000.0002*    GigabitEthernet0/2/0    0000.0000.0003.02       Up    28s      L1       64
     MT IDs supported     : 2(UP)
     Local MT IDs         : 2
     Area Address(es)     : 10
     Peer IPv6 Address(es): FE80::DC40:0:47A9:1
     Peer IPv6 GlbAddr(es): 2001:db8:2::2/64
     Uptime               : 00h00m15s
     Peer Up Time         : 2020-06-08 01:41:57
     Adj Protocol         : IPV6
     Restart Capable      : YES
     Suppressed Adj       : NO 
     Peer System ID       : 0000.0000.0002
     BFD Incr-Cost State  : MT0 : NO / MT2 : NO
     MT IDs BFD Required  : 0(IPv4:FALSE IPv6:FALSE) 2(IPv6:FALSE)
     Reverse Cost State   : -- 
   
   0000.0000.0004*    GigabitEthernet0/3/0    0000.0000.0003.03      Up     24s     L2       --
     MT IDs supported     : 2(UP)
     Local MT IDs         : 2
     Area Address(es)     : 20
     Peer IPv6 Address(es): FE80::F81D:0:1E24:2
     Peer IPv6 GlbAddr(es): 2001:db8:3::2
     Uptime               : 00h00m15s
     Peer Up Time         : 2020-06-08 01:41:57
     Adj Protocol         : IPV6
     Restart Capable      : YES
     Suppressed Adj       : NO 
     Peer System ID       : 0000.0000.0004
     BFD Incr-Cost State  : MT0 : NO / MT2 : NO
     MT IDs BFD Required  : 0(IPv4:FALSE IPv6:FALSE) 2(IPv6:FALSE)
     Reverse Cost State   : -- 
   
   Total Peer (s): 3
   ```
   
   # Display detailed information about the IS-IS LSDB of Device C.
   
   ```
   [~DeviceC] display isis lsdb verbose
                           Database information for ISIS(1)
                           --------------------------------
   
                             Level-1 Link State Database                                                                               
   
   LSPID                  Seq Num    Checksum   HoldTime       Length   ATT/P/OL                                                       
   -----------------------------------------------------------------------------                                                       
   0000.0000.0001.00-00   0x0000004a 0x226f     796            91       0/0/0                                                          
    SOURCE       0000.0000.0001.00                                                                                                     
    NLPID        IPV6                                                                                                                  
    AREA ADDR    10                                                                                                                    
    INTF ADDR V6 2001:DB8:1::2                                                                                                         
    Topology     Standard, IPV6                                                                                                        
   +MT NBR ID    0000.0000.0003.01  COST: 10            MT: 2 (IPV6)                                                                   
    IPV6         2001:DB8:1::/64                  COST: 10         MT: 2 
    
   0000.0000.0002.00-00   0x00000066 0x5f12     1030           91       0/0/0                                                          
    SOURCE       0000.0000.0002.00                                                                                                     
    NLPID        IPV6                                                                                                                  
    AREA ADDR    10                                                                                                                    
    INTF ADDR V6 2001:DB8:2::2                                                                                                         
    Topology     Standard, IPV6                                                                                                        
   +MT NBR ID    0000.0000.0003.02  COST: 10            MT: 2 (IPV6)                                                                   
    IPV6         2001:DB8:2::/64                  COST: 10         MT: 2 
   
   0000.0000.0003.00-00*  0x00000077 0x9a36     370            148      0/0/0                                                          
    SOURCE       0000.0000.0003.00                                                                                                     
    NLPID        IPV6                                                                                                                  
    AREA ADDR    10                                                                                                                    
    INTF ADDR V6 2001:DB8:1::1                                                                                                         
    INTF ADDR V6 2001:DB8:2::1                                                                                                         
    INTF ADDR V6 2001:DB8:3::1                                                                                                         
    Topology     Standard, IPV6(ATT)                                                                                                   
   +MT NBR ID    0000.0000.0003.01  COST: 10            MT: 2 (IPV6)                                                                   
   +MT NBR ID    0000.0000.0003.02  COST: 10            MT: 2 (IPV6)                                                                   
    IPV6         2001:DB8:1::/64                  COST: 10         MT: 2                                                               
    IPV6         2001:DB8:2::/64                  COST: 10         MT: 2                                                               
   
   0000.0000.0003.01-00*  0x00000061 0xf372     368            55       0/0/0                                                          
    SOURCE       0000.0000.0003.01                                                                                                     
    NLPID        IPV6                                                                                                                  
    NBR  ID      0000.0000.0003.00  COST: 0                                                                                            
    NBR  ID      0000.0000.0001.00  COST: 0                                                                                            
   
   0000.0000.0003.02-00*  0x00000060 0x0b5a     367            55       0/0/0                                                          
    SOURCE       0000.0000.0003.02                                                                                                     
    NLPID        IPV6                                                                                                                  
    NBR  ID      0000.0000.0003.00  COST: 0                                                                                            
    NBR  ID      0000.0000.0002.00  COST: 0                                                                                            
   
   Total LSP(s): 5                                                                                                                     
       *(In TLV)-Leaking Route, *(By LSPID)-Self LSP, +-Self LSP(Extended),                                                            
              ATT-Attached, P-Partition, OL-Overload  
   		
   		
                      Level-2 Link State Database
   
   LSPID                  Seq Num    Checksum   HoldTime       Length   ATT/P/OL                                                       
   -----------------------------------------------------------------------------                                                       
   0000.0000.0003.00-00*  0x00000071 0xf3f8     367            151      0/0/0                                                          
    SOURCE       0000.0000.0003.00                                                                                                     
    NLPID        IPV6                                                                                                                  
    AREA ADDR    10                                                                                                                    
    INTF ADDR V6 2001:DB8:1::1                                                                                                         
    INTF ADDR V6 2001:DB8:2::1                                                                                                         
    INTF ADDR V6 2001:DB8:3::1                                                                                                         
    Topology     Standard, IPV6                                                                                                        
   +MT NBR ID    0000.0000.0003.03  COST: 10            MT: 2 (IPV6)                                                                   
    IPV6         2001:DB8:1::/64                  COST: 10         MT: 2                                                               
    IPV6         2001:DB8:2::/64                  COST: 10         MT: 2                                                               
    IPV6         2001:DB8:3::/64                  COST: 10         MT: 2                                                               
   
   0000.0000.0003.03-00*  0x00000066 0x302c     365            55       0/0/0                                                          
    SOURCE       0000.0000.0003.03                                                                                                     
    NLPID        IPV6                                                                                                                  
    NBR  ID      0000.0000.0003.00  COST: 0                                                                                            
    NBR  ID      0000.0000.0004.00  COST: 0                                                                                            
   
   0000.0000.0004.00-00   0x0000006e 0x50c2     488            121      0/0/0                                                          
    SOURCE       0000.0000.0004.00                                                                                                     
    NLPID        IPV6                                                                                                                  
    AREA ADDR    20                                                                                                                    
    INTF ADDR V6 2001:DB8:3::2                                                                                                         
    INTF ADDR V6 2001:DB8:4::1                                                                                                         
    Topology     Standard, IPV6                                                                                                        
   +MT NBR ID    0000.0000.0003.03  COST: 10            MT: 2 (IPV6)                                                                   
    IPV6         2001:DB8:3::/64                  COST: 10         MT: 2                                                               
    IPV6         2001:DB8:4::/64                  COST: 10         MT: 2                                                                                                                                                                                                 
   Total LSP(s): 3                                                                                                                     
       *(In TLV)-Leaking Route, *(By LSPID)-Self LSP, +-Self LSP(Extended),                                                            
              ATT-Attached, P-Partition, OL-Overload  
   ```

#### Configuration Files

* Device A configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceA
  ```
  ```
  #
  ```
  ```
  isis 1
  ```
  ```
   is-level level-1
  ```
  ```
   ipv6 enable topology ipv6
  ```
  ```
   network-entity 10.0000.0000.0001.00
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
   ipv6 enable
  ```
  ```
   ipv6 address 2001:db8:1::2/64
  ```
  ```
   isis ipv6 enable 1
  ```
  ```
  #
  ```
  ```
  return
  ```
* Device B configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceB
  ```
  ```
  #
  ```
  ```
  isis 1
  ```
  ```
   is-level level-1
  ```
  ```
   ipv6 enable topology ipv6
  ```
  ```
   network-entity 10.0000.0000.0002.00
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
   ipv6 enable
  ```
  ```
   ipv6 address 2001:db8:2::2/64
  ```
  ```
   isis ipv6 enable 1
  ```
  ```
  #
  ```
  ```
  return
  ```
* Device C configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceC
  ```
  ```
  #
  ```
  ```
  isis 1
  ```
  ```
   ipv6 enable topology ipv6
  ```
  ```
   network-entity 10.0000.0000.0003.00
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
   ipv6 enable
  ```
  ```
   ipv6 address 2001:db8:1::1/64
  ```
  ```
   isis ipv6 enable 1
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
   ipv6 enable
  ```
  ```
   ipv6 address 2001:db8:2::1/64
  ```
  ```
   isis ipv6 enable 1
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/3/0
  ```
  ```
   undo shutdown
  ```
  ```
   ipv6 enable
  ```
  ```
   ipv6 address 2001:db8:3::1/64
  ```
  ```
   isis ipv6 enable 1
  ```
  ```
   isis circuit-level level-1-2
  ```
  ```
  #
  ```
  ```
  return
  ```
* Device D configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceD
  ```
  ```
  #
  ```
  ```
  isis 1
  ```
  ```
   is-level level-2
  ```
  ```
   ipv6 enable topology ipv6
  ```
  ```
   network-entity 20.0000.0000.0004.00
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
   ipv6 enable
  ```
  ```
   ipv6 address 2001:db8:3::2/64
  ```
  ```
   isis ipv6 enable 1
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   ipv6 enable
  ```
  ```
   ipv6 address 2001:db8:4::1/64
  ```
  ```
   isis ipv6 enable 1
  ```
  ```
  #
  ```
  ```
  return
  ```