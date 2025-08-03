Example for Configuring SRv6 TE Policy over GRE (IS-IS)
=======================================================

This section provides an example for configuring an SRv6 TE Policy over a GRE tunnel.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001111234020__fig_dc_vrp_srv6_cfg_all_001101), some of the devices among P1, P2, and P3 do not support IPv6. It is required that a bidirectional SRv6 TE Policy be deployed between PE1 and PE2. To meet the preceding requirement, you can establish a GRE tunnel between P1 and P3, and then deploy an SRv6 TE Policy over the GRE tunnel.

**Figure 1** SRv6 TE Policy over GRE networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](figure/en-us_image_0000001157354019.png "Click to enlarge")

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IP addresses for interfaces.
2. Configure OSPF on P1, P2, and P3, and establish a GRE tunnel between P1 and P3.
3. Enable IS-IS, configure an IS-IS level, and specify a network entity title on PE1, PE2, P1, and P3.
4. Configure IS-IS to advertise SRv6 locator routes and also configure static End.X SIDs on PE1, PE2, P1, and P3.
5. Deploy an SRv6 TE Policy between PE1 and PE2.

#### Precautions

During the configuration process, note the following:

* SRv6 TE Policy over GRE configuration in this example requires you to configure IPv6 interface addresses for the GRE tunnel and enable IS-IS. In addition, during End.X SID configuration, you can specify a GRE tunnel interface as the outbound interface.

#### Data Preparation

To complete the configuration, you need the following data:

* IP/IPv6 addresses on each device
* IS-IS process IDs, IS-IS levels, and network entity titles of PE1, PE2, P1, and P3

#### Procedure

1. Configure IP/IPv6 addresses for interfaces.
   
   
   
   # Configure PE1.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname PE1
   [*HUAWEI] commit
   [~PE1] interface gigabitethernet 0/1/0
   [~PE1-GigabitEthernet0/1/0] ipv6 enable
   [*PE1-GigabitEthernet0/1/0] ipv6 address 2001:DB8:1::2 96
   [*PE1-GigabitEthernet0/1/0] quit
   [*PE1] interface LoopBack 1
   [*PE1-LoopBack1] ipv6 enable
   [*PE1-LoopBack1] ipv6 address 2001:DB8:111::1 128
   [*PE1-LoopBack1] quit
   [*PE1] commit
   ```
   
   
   
   # Configure P1.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname P1
   [*HUAWEI] commit
   [~P1] interface gigabitethernet 0/1/0
   [~P1-GigabitEthernet0/1/0] ip address 172.16.1.1 24
   [*P1-GigabitEthernet0/1/0] quit
   [*P1] interface gigabitethernet 0/2/0
   [*P1-GigabitEthernet0/2/0] ipv6 enable
   [*P1-GigabitEthernet0/2/0] ipv6 address 2001:DB8:1::1 96
   [*P1-GigabitEthernet0/2/0] quit
   [*P1] interface LoopBack 1
   [*P1-LoopBack1] ip address 2.2.2.9 32
   [*P1-LoopBack1] ipv6 enable
   [*P1-LoopBack1] ipv6 address 2001:DB8:222::2 128
   [*P1-LoopBack1] quit
   [*P1] commit
   ```
   
   
   
   # Configure P2.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname P2
   [*HUAWEI] commit
   [~P2] interface gigabitethernet 0/1/0
   [~P2-GigabitEthernet0/1/0] ip address 172.16.1.2 24
   [*P2-GigabitEthernet0/1/0] quit
   [*P2] interface gigabitethernet 0/2/0
   [*P2-GigabitEthernet0/2/0] ip address 172.16.2.1 24
   [*P2-GigabitEthernet0/2/0] quit
   [*P2] commit
   ```
   
   
   
   # Configure P3.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname P3
   [*HUAWEI] commit
   [~P3] interface gigabitethernet 0/1/0
   [~P3-GigabitEthernet0/1/0] ip address 172.16.2.2 24
   [*P3-GigabitEthernet0/1/0] quit
   [*P3] interface gigabitethernet 0/2/0
   [*P3-GigabitEthernet0/2/0] ipv6 enable
   [*P3-GigabitEthernet0/2/0] ipv6 address 2001:DB8:3::1 96
   [*P3-GigabitEthernet0/2/0] quit
   [*P3] interface LoopBack 1
   [*P3-LoopBack1] ip address 3.3.3.9 32
   [*P3-LoopBack1] ipv6 enable
   [*P3-LoopBack1] ipv6 address 2001:DB8:333::3 128
   [*P3-LoopBack1] quit
   [*P3] commit
   ```
   
   
   
   # Configure PE2.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname PE2
   [*HUAWEI] commit
   [~PE2] interface gigabitethernet 0/1/0
   [~PE2-GigabitEthernet0/1/0] ipv6 enable
   [*PE2-GigabitEthernet0/1/0] ipv6 address 2001:DB8:3::2 96
   [*PE2-GigabitEthernet0/1/0] quit
   [*PE2] interface LoopBack 1
   [*PE2-LoopBack1] ipv6 enable
   [*PE2-LoopBack1] ipv6 address 2001:DB8:444::4 128
   [*PE2-LoopBack1] quit
   [*PE2] commit
   ```
2. Establish a GRE tunnel between P1 and P3.
   
   
   
   # Configure P1.
   
   ```
   [~P1] ospf 1
   [*P1-ospf-1] area 0.0.0.0
   [*P1-ospf-1-area-0.0.0.0] network 2.2.2.9 0.0.0.0
   [*P1-ospf-1-area-0.0.0.0] network 172.16.1.0 0.0.0.255 
   [*P1-ospf-1-area-0.0.0.0] quit
   [*P1-ospf-1] quit
   [*P1] interface LoopBack1 
   [*P1-LoopBack1] binding tunnel gre
   [*P1-LoopBack1] ospf enable 1 area 0.0.0.0 
   [*P1-LoopBack1] quit
   [*P1] interface Tunnel10 
   [*P1-Tunnel10] tunnel-protocol gre        
   [*P1-Tunnel10] source 2.2.2.9 
   [*P1-Tunnel10] destination 3.3.3.9
   [*P1-Tunnel10] ipv6 enable
   [*P1-Tunnel10] ipv6 address 2001:DB8:2::1 96
   [*P1-Tunnel10] quit
   [*P1] commit
   ```
   
   
   
   # Configure P2.
   
   ```
   [~P2] ospf 1
   [*P2-ospf-1] area 0.0.0.0
   [*P2-ospf-1-area-0.0.0.0] network 172.16.1.0 0.0.0.255 
   [*P2-ospf-1-area-0.0.0.0] network 172.16.2.0 0.0.0.255
   [*P2-ospf-1-area-0.0.0.0] quit
   [*P2-ospf-1] quit
   [*P2] commit
   ```
   
   
   
   # Configure P3.
   
   ```
   [~P3] ospf 1
   [*P3-ospf-1] area 0.0.0.0
   [*P3-ospf-1-area-0.0.0.0] network 3.3.3.9 0.0.0.0
   [*P3-ospf-1-area-0.0.0.0] network 172.16.2.0 0.0.0.255 
   [*P3-ospf-1-area-0.0.0.0] quit
   [*P3-ospf-1] quit
   [*P3] interface LoopBack1 
   [*P3-LoopBack1] binding tunnel gre
   [*P3-LoopBack1] ospf enable 1 area 0.0.0.0 
   [*P3-LoopBack1] quit
   [*P3] interface Tunnel10 
   [*P3-Tunnel10] tunnel-protocol gre        
   [*P3-Tunnel10] source 3.3.3.9 
   [*P3-Tunnel10] destination 2.2.2.9
   [*P3-Tunnel10] ipv6 enable
   [*P3-Tunnel10] ipv6 address 2001:DB8:2::2 96
   [*P3-Tunnel10] quit
   [*P3] commit
   ```
   
   After the configuration is complete, run the **display interface tunnel** command. The command output shows that the tunnel interface state is up. The following example uses the command output on P1.
   
   ```
   [~P1] display interface tunnel 10
   Tunnel10 current state : UP (ifindex: 30)               
   Line protocol current state : DOWN                      
   Description:                                            
   Route Port,The Maximum Transmit Unit is 1500            
   Internet protocol processing : disabled                 
   Encapsulation is TUNNEL, loopback not set               
   Tunnel source 2.2.2.9 (LoopBack1), destination 3.3.3.9  
   Tunnel protocol/transport GRE/IP, key disabled          
   keepalive disabled                                      
   Checksumming of packets disabled                        
   Current system time: 2021-05-13 09:25:47                
       300 seconds input rate 0 bits/sec, 0 packets/sec    
       300 seconds output rate 0 bits/sec, 0 packets/sec   
       0 seconds input rate 0 bits/sec, 0 packets/sec      
       0 seconds output rate 0 bits/sec, 0 packets/sec     
       19403 packets input,  2369471 bytes                 
       0 input error                                       
       19494 packets output,  2552122 bytes                
       0 output error                                      
       Input:                                              
         Unicast: 2277 packets, Multicast: 0 packets       
       Output:                                             
         Unicast: 19494 packets, Multicast: 0 packets 
       Input bandwidth utilization  :    0%                
       Output bandwidth utilization :    0% 
   ```
   
   Run the **display tunnel****-info all** command to check all tunnel information. The following example uses the command output on P1.
   
   ```
   [~P1] display tunnel-info all
   Tunnel ID            Type                Destination                             Status
   ----------------------------------------------------------------------------------------
   0x00000000050000001e gre                 3.3.3.9                                 UP
   ```
3. Configure IS-IS.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] isis 1
   [*PE1-isis-1] is-level level-2
   [*PE1-isis-1] cost-style wide
   [*PE1-isis-1] network-entity 00.0005.0000.0000.0001.00
   [*PE1-isis-1] traffic-eng level-2
   [*PE1-isis-1] ipv6 enable topology ipv6
   [*PE1-isis-1] quit
   [*PE1] interface gigabitethernet 0/1/0
   [*PE1-GigabitEthernet0/1/0] isis ipv6 enable 1
   [*PE1-GigabitEthernet0/1/0] quit
   [*PE1] interface loopback1
   [*PE1-LoopBack1] isis ipv6 enable 1
   [*PE1-LoopBack1] commit
   [~PE1-LoopBack1] quit
   ```
   
   # Configure P1.
   
   ```
   [~P1] isis 1 
   [*P1-isis-1] is-level level-2
   [*P1-isis-1] cost-style wide
   [*P1-isis-1] network-entity 00.0005.0000.0000.0002.00
   [*P1-isis-1] traffic-eng level-2
   [*P1-isis-1] ipv6 enable topology ipv6
   [*P1-isis-1] quit
   [*P1] interface Tunnel10 
   [*P1-Tunnel10] isis ipv6 enable 1 
   [*P1-Tunnel10] quit 
   [*P1] interface gigabitethernet 0/2/0
   [*P1-GigabitEthernet0/2/0] isis ipv6 enable 1
   [*P1-GigabitEthernet0/2/0] quit
   [*P1] interface loopback1
   [*P1-LoopBack1] isis ipv6 enable 1
   [*P1-LoopBack1] commit
   [~P1-LoopBack1] quit
   ```
   
   # Configure P3.
   
   ```
   [~P3] isis 1 
   [*P3-isis-1] is-level level-2
   [*P3-isis-1] cost-style wide
   [*P3-isis-1] network-entity 00.0005.0000.0000.0003.00
   [*P3-isis-1] traffic-eng level-2
   [*P3-isis-1] ipv6 enable topology ipv6
   [*P3-isis-1] quit
   [*P3] interface Tunnel10 
   [*P3-Tunnel10] isis ipv6 enable 1 
   [*P3-Tunnel10] quit 
   [*P3] interface gigabitethernet 0/2/0
   [*P3-GigabitEthernet0/2/0] isis ipv6 enable 1
   [*P3-GigabitEthernet0/2/0] quit
   [*P3] interface loopback1
   [*P3-LoopBack1] isis ipv6 enable 1
   [*P3-LoopBack1] commit
   [~P3-LoopBack1] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] isis 1
   [*PE2-isis-1] is-level level-2
   [*PE2-isis-1] cost-style wide
   [*PE2-isis-1] network-entity 00.0005.0000.0000.0004.00
   [*PE2-isis-1] traffic-eng level-2
   [*PE2-isis-1] ipv6 enable topology ipv6
   [*PE2-isis-1] quit
   [*PE2] interface gigabitethernet 0/1/0
   [*PE2-GigabitEthernet0/1/0] isis ipv6 enable 1
   [*PE2-GigabitEthernet0/1/0] quit
   [*PE2] interface loopback1
   [*PE2-LoopBack1] isis ipv6 enable 1
   [*PE2-LoopBack1] commit
   [~PE2-LoopBack1] quit
   ```
   
   
   
   After the configuration is complete, perform the following operations to check whether IS-IS is successfully configured.
   
   # Display IS-IS neighbor information. PE1 is used as an example.
   
   ```
   [~PE1] display isis peer
   
                             Peer information for ISIS(1) 
   
     System Id     Interface          Circuit Id        State HoldTime Type     PRI 
   --------------------------------------------------------------------------------   
   0000.0000.0002* GE0/1/0            0000.0000.0001.01  Up   22s      L2       64   
   
   Total Peer(s): 1
   ```
   
   # Display IS-IS routing information. PE1 is used as an example.
   
   ```
   [~PE1] display isis route
                            Route information for ISIS(1)                         
                            -----------------------------                         
   
                           ISIS(1) Level-2 Forwarding Table                       
                           --------------------------------                       
   
    IPV6 Dest.         ExitInterface      NextHop                    Cost     Flags   
   -------------------------------------------------------------------------------- 
   2001:DB8:1::/96     GE0/1/0            Direct                     10       D/-/L/- 
   2001:DB8:2::/96     GE0/1/0            FE80::3AB0:9EFF:FE11:300   20       A/-/-/- 
   2001:DB8:3::/96     GE0/1/0            FE80::3AB0:9EFF:FE11:300   30       A/-/-/- 
   2001:DB8:10::/64    NULL0              -                          0        A/-/L/- 
   2001:DB8:20::/64    GE0/1/0            FE80::3AB0:9EFF:FE11:300   10       A/-/-/- 
   2001:DB8:30::/64    GE0/1/0            FE80::3AB0:9EFF:FE11:300   20       A/-/-/-  
   2001:DB8:40::/64    GE0/1/0            FE80::3AB0:9EFF:FE11:300   30       A/-/-/-  
   2001:DB8:111::1/128 Loop1              Direct                     0        D/-/L/-   
   2001:DB8:222::2/128 GE0/1/0            FE80::3AB0:9EFF:FE11:300   10       A/-/-/-   
   2001:DB8:333::3/128 GE0/1/0            FE80::3AB0:9EFF:FE11:300   20       A/-/-/-   
   2001:DB8:444::4/128 GE0/1/0            FE80::3AB0:9EFF:FE11:300   30       A/-/-/-  
        Flags: D-Direct, A-Added to URT, L-Advertised in LSPs, S-IGP Shortcut,    
               U-Up/Down Bit Set, LP-Local Prefix-Sid                             
        Protect Type: L-Link Protect, N-Node Protect
   ```
4. Configure IS-IS to advertise SRv6 locator routes and also configure static End.X SIDs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] segment-routing ipv6
   [*PE1-segment-routing-ipv6] encapsulation source-address 2001:DB8:111::1
   [*PE1-segment-routing-ipv6] locator as1 ipv6-prefix 2001:DB8:10:: 64 static 32
   [*PE1-segment-routing-ipv6-locator] opcode ::100 end-x interface GigabitEthernet0/1/0 nexthop 2001:DB8:1::1 psp 
   [*PE1-segment-routing-ipv6-locator] quit
   [*PE1-segment-routing-ipv6] quit
   [*PE1] isis 1
   [*PE1-isis-1] ipv6 enable topology ipv6 
   [*PE1-isis-1] segment-routing ipv6 locator as1 auto-sid-disable
   [*PE1-isis-1] commit
   [~PE1-isis-1] quit
   ```
   
   # Configure P1.
   
   ```
   [~P1] segment-routing ipv6
   [*P1-segment-routing-ipv6] encapsulation source-address 2001:DB8:222::2
   [*P1-segment-routing-ipv6] locator as1 ipv6-prefix 2001:DB8:20:: 64 static 32
   [*P1-segment-routing-ipv6-locator] opcode ::100 end-x interface Tunnel10 nexthop 2001:DB8:2::2 psp  
   [*P1-segment-routing-ipv6-locator] opcode ::200 end-x interface GigabitEthernet0/2/0 nexthop 2001:DB8:1::2 psp 
   [*P1-segment-routing-ipv6-locator] quit
   [*P1-segment-routing-ipv6] quit
   [*P1] isis 1
   [*P1-isis-1] ipv6 enable topology ipv6 
   [*P1-isis-1] segment-routing ipv6 locator as1 auto-sid-disable
   [*P1-isis-1] commit
   [~P1-isis-1] quit
   ```
   
   # Configure P3.
   
   ```
   [~P3] segment-routing ipv6
   [*P3-segment-routing-ipv6] encapsulation source-address 2001:DB8:333::3
   [*P3-segment-routing-ipv6] locator as1 ipv6-prefix 2001:DB8:30:: 64 static 32
   [*P3-segment-routing-ipv6-locator] opcode ::100 end-x interface GigabitEthernet0/2/0 nexthop 2001:DB8:3::2 psp  
   [*P3-segment-routing-ipv6-locator] opcode ::200 end-x interface Tunnel10 nexthop 2001:DB8:2::1 psp 
   [*P3-segment-routing-ipv6-locator] quit
   [*P3-segment-routing-ipv6] quit
   [*P3] isis 1
   [*P3-isis-1] ipv6 enable topology ipv6 
   [*P3-isis-1] segment-routing ipv6 locator as1 auto-sid-disable
   [*P3-isis-1] commit
   [~P3-isis-1] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] segment-routing ipv6
   [*PE2-segment-routing-ipv6] encapsulation source-address 2001:DB8:444::4
   [*PE2-segment-routing-ipv6] locator as1 ipv6-prefix 2001:DB8:40:: 64 static 32
   [*PE2-segment-routing-ipv6-locator] opcode ::200 end-x interface GigabitEthernet0/1/0 nexthop 2001:DB8:3::1 psp
   [*PE2-segment-routing-ipv6-locator] quit
   [*PE2-segment-routing-ipv6] quit
   [*PE2] isis 1
   [*PE2-isis-1] ipv6 enable topology ipv6 
   [*PE2-isis-1] segment-routing ipv6 locator as1 auto-sid-disable
   [*PE2-isis-1] commit
   [~PE2-isis-1] quit
   ```
   
   Run the [**display segment-routing ipv6 local-sid**](cmdqueryname=display+segment-routing+ipv6+local-sid) **end-x** **forwarding** command to check information about the SRv6 local SID table. The following example uses the command output on PE1.
   
   ```
   [~PE1] display segment-routing ipv6 local-sid end-x forwarding
   
                               My Local-SID End.X Forwarding Table          
                               -----------------------------------
   
   SID         : 2001:DB8:10::100/128                                             FuncType    : End.X
   Flavor      : PSP                                                              SidCompress : NO
   LocatorName : as1                                                              LocatorID   : 1     
   ProtocolType: STATIC                                                           ProcessID   : --    
   UpdateTime  : 2021-05-13 04:26:13.408                                          NextHopCount: 1 
   NextHop     :                              Interface :                         ExitIndex:          
   2001:DB8:1::1                              GigabitEthernet0/1/0                0x00000007 
   TeFrrFlags  : --                                                               DelayTimerRemain: - 
   
   Total SID(s): 1
   ```
5. Configure an SRv6 TE Policy.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] segment-routing ipv6 
   [~PE1-segment-routing-ipv6] segment-list list1 
   [*PE1-segment-routing-ipv6-segment-list-list1] index 5 sid ipv6 2001:DB8:10::100
   [*PE1-segment-routing-ipv6-segment-list-list1] index 10 sid ipv6 2001:DB8:20::100
   [*PE1-segment-routing-ipv6-segment-list-list1] index 15 sid ipv6 2001:DB8:30::100 
   [*PE1-segment-routing-ipv6-segment-list-list1] commit
   [~PE1-segment-routing-ipv6-segment-list-list1] quit
   [~PE1-segment-routing-ipv6] srv6-te-policy locator as1 
   [*PE1-segment-routing-ipv6] srv6-te policy policy1 endpoint 2001:DB8:444::4 color 101
   [*PE1-segment-routing-ipv6-policy-policy1] binding-sid 2001:DB8:10::1000
   [*PE1-segment-routing-ipv6-policy-policy1] candidate-path preference 100
   [*PE1-segment-routing-ipv6-policy-policy1-path] segment-list list1 
   [*PE1-segment-routing-ipv6-policy-policy1-path] commit
   [~PE1-segment-routing-ipv6-policy-policy1-path] quit
   [~PE1-segment-routing-ipv6-policy-policy1] quit
   [~PE1-segment-routing-ipv6] quit
   ```
   
   
   
   # Configure PE2.
   
   ```
   [~PE2] segment-routing ipv6 
   [~PE2-segment-routing-ipv6] segment-list list1 
   [*PE2-segment-routing-ipv6-segment-list-list1] index 5 sid ipv6 2001:DB8:40::200          
   [*PE2-segment-routing-ipv6-segment-list-list1] index 10 sid ipv6 2001:DB8:30::200         
   [*PE2-segment-routing-ipv6-segment-list-list1] index 15 sid ipv6 2001:DB8:20::200 
   [*PE2-segment-routing-ipv6-segment-list-list1] commit
   [~PE2-segment-routing-ipv6-segment-list-list1] quit
   [~PE2-segment-routing-ipv6] srv6-te-policy locator as1 
   [*PE2-segment-routing-ipv6] srv6-te policy policy1 endpoint 2001:DB8:111::1 color 101
   [*PE2-segment-routing-ipv6-policy-policy1] binding-sid 2001:DB8:40::1000
   [*PE2-segment-routing-ipv6-policy-policy1] candidate-path preference 100
   [*PE2-segment-routing-ipv6-policy-policy1-path] segment-list list1 
   [*PE2-segment-routing-ipv6-policy-policy1-path] commit
   [~PE2-segment-routing-ipv6-policy-policy1-path] quit
   [~PE2-segment-routing-ipv6-policy-policy1] quit
   [~PE2-segment-routing-ipv6] quit
   ```
   
   After the configuration is complete, run the [**display srv6-te policy**](cmdqueryname=display+srv6-te+policy) command to check SRv6 TE Policy information.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display srv6-te policy 
   PolicyName : policy1                                    
   Color                   : 101                            Endpoint             : 2001:DB8:444::4  
   TunnelId                : 1                              
   TunnelType              : SRv6-TE Policy                 DelayTimerRemain     : -          
   Policy State            : Up                             State Change Time    : 2021-05-13 04:26:18  
   Admin State             : Up                             Traffic Statistics   : Disable              
   Backup Hot-Standby      : Disable                        BFD                  : Disable              
   Interface Index         : -                              Interface Name       : -                    
   Interface State         : -                              Encapsulation Mode   : Insert
   Binding SID             : 2001:DB8:10::1000(Insert, Preferred)
   Candidate-path Count    : 1                             
   
    Candidate-path Preference : 100
    Path State             : Active                         Path Type            : Primary              
    Protocol-Origin        : Configuration(30)              Originator           : 0, 0.0.0.0           
    Discriminator          : 100                            Binding SID          : 2001:DB8:10::1000    
    GroupId                : 1                              Policy Name          : policy1
    Template ID            : 0                              Path Verification    : Disable              
    DelayTimerRemain       : -                              Network Slice ID     : - 
    Segment-List Count     : 1                             
     Segment-List          : list1                         
      Segment-List ID      : 1                              XcIndex              : 1                    
      List State           : Up                             DelayTimerRemain     : -
      Verification State   : -                              SuppressTimeRemain   : -                    
      PMTU                 : 9600                           Active PMTU          : 9600                 
      Weight               : 1                              BFD State            : -   
      Loop Detection State : Up                             BFD Delay Remain     : -                  
      Network Slice ID     : -    
      Binding SID          : -
      Reverse Binding ID   : -
      SID :                 
            2001:DB8:10::100                               
            2001:DB8:20::100                               
            2001:DB8:30::100  
   ```
6. Verify the configuration.
   
   
   
   # Configure an End.OP SID on PE1.
   
   ```
   [~PE1] segment-routing ipv6
   [~PE1-segment-routing-ipv6] locator as1
   [~PE1-segment-routing-ipv6-locator] opcode ::1111 end-op 
   [*PE1-segment-routing-ipv6-locator] quit
   [*PE1-segment-routing-ipv6] quit
   [*PE1] commit
   ```
   
   # Configure an End.OP SID on PE2.
   
   ```
   [~PE2] segment-routing ipv6
   [~PE2-segment-routing-ipv6] locator as1
   [~PE2-segment-routing-ipv6-locator] opcode ::4444 end-op 
   [*PE2-segment-routing-ipv6-locator] quit
   [*PE2-segment-routing-ipv6] quit
   [*PE2] commit
   ```
   
   Run the [**ping srv6-te policy**](cmdqueryname=ping+srv6-te+policy) command on PE1 to check the SRv6 TE Policy connectivity. For example:
   
   ```
   [~PE1] ping srv6-te policy policy-name policy1 end-op 2001:DB8:40::4444                                                
     PING srv6-te policy : 100  data bytes, press CTRL_C to break                        
     srv6-te policy's segment list:                        
     Preference: 100; Path Type: primary; Protocol-Origin: local; Originator: 0, 0.0.0.0; Discriminator: 100; Segment-List ID: 1; Xcindex: 1; end-op: 2001:DB8:40::4444 
       Reply from 2001:DB8:40::4444                        
       bytes=100 Sequence=1 time=3 ms                      
       Reply from 2001:DB8:40::4444                        
       bytes=100 Sequence=2 time=3 ms                      
       Reply from 2001:DB8:40::4444                        
       bytes=100 Sequence=3 time=3 ms                      
       Reply from 2001:DB8:40::4444                        
       bytes=100 Sequence=4 time=3 ms                      
       Reply from 2001:DB8:40::4444                        
       bytes=100 Sequence=5 time=4 ms                      
   
     --- srv6-te policy ping statistics ---                
       5 packet(s) transmitted                             
       5 packet(s) received                                
       0.00% packet loss                                   
       round-trip min/avg/max = 3/3/4 ms 
   ```
   
   Run the [**ping srv6-te policy**](cmdqueryname=ping+srv6-te+policy) command on PE2 to check the SRv6 TE Policy connectivity. For example:
   
   ```
   [~PE2] ping srv6-te policy policy-name policy1 end-op 2001:DB8:10::1111                                                
     PING srv6-te policy : 100  data bytes, press CTRL_C to break                                                                      
     srv6-te policy's segment list:                        
     Preference: 100; Path Type: primary; Protocol-Origin: local; Originator: 0, 0.0.0.0; Discriminator: 100; Segment-List ID: 1; Xcindex: 1; end-op: 2001:DB8:10::1111    
       Reply from 2001:DB8:10::1111                        
       bytes=100 Sequence=1 time=4 ms                      
       Reply from 2001:DB8:10::1111                        
       bytes=100 Sequence=2 time=3 ms                      
       Reply from 2001:DB8:10::1111                        
       bytes=100 Sequence=3 time=4 ms                      
       Reply from 2001:DB8:10::1111                        
       bytes=100 Sequence=4 time=3 ms                      
       Reply from 2001:DB8:10::1111                        
       bytes=100 Sequence=5 time=3 ms                      
   
     --- srv6-te policy ping statistics ---                
       5 packet(s) transmitted                             
       5 packet(s) received                                
       0.00% packet loss                                   
       round-trip min/avg/max = 3/3/4 ms 
   ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  segment-routing ipv6                                    
   encapsulation source-address 2001:DB8:111::1           
   locator as1 ipv6-prefix 2001:DB8:10:: 64 static 32     
    opcode ::100 end-x interface GigabitEthernet0/1/0 nexthop 2001:DB8:1::1 psp 
    opcode ::1111 end-op                                  
   srv6-te-policy locator as1                             
   segment-list list1                                     
    index 5 sid ipv6 2001:DB8:10::100                     
    index 10 sid ipv6 2001:DB8:20::100                    
    index 15 sid ipv6 2001:DB8:30::100                    
   srv6-te policy policy1 endpoint 2001:DB8:444::4 color 101             
    binding-sid 2001:DB8:10::1000                         
    candidate-path preference 100                         
     segment-list list1                                   
  #                                                       
  isis 1                                                  
   is-level level-2                                       
   cost-style wide                                        
   network-entity 00.0005.0000.0000.0001.00               
   traffic-eng level-2 
   #                                                      
   ipv6 enable topology ipv6                              
   segment-routing ipv6 locator as1 auto-sid-disable      
   #                                                      
  #                                                       
  interface GigabitEthernet0/1/0                                 
   undo shutdown                                          
   ipv6 enable                                            
   ipv6 address 2001:DB8:1::2/96                          
   isis ipv6 enable 1 
  #                                                       
  interface LoopBack1                                     
   ipv6 enable                                            
   ipv6 address 2001:DB8:111::1/128                       
   isis ipv6 enable 1  
  #                                                       
  return 
  ```
* P1 configuration file
  
  ```
  #
  sysname P1   
  segment-routing ipv6                                    
   encapsulation source-address 2001:DB8:222::2           
   locator as1 ipv6-prefix 2001:DB8:20:: 64 static 32     
    opcode ::100 end-x interface Tunnel10 nexthop 2001:DB8:2::2 psp      
    opcode ::200 end-x interface GigabitEthernet0/2/0 nexthop 2001:DB8:1::2 psp 
  #                                                       
  isis 1                                                  
   is-level level-2                                       
   cost-style wide                                        
   network-entity 00.0005.0000.0000.0002.00               
   traffic-eng level-2                                    
   #                                                      
   ipv6 enable topology ipv6                              
   segment-routing ipv6 locator as1 auto-sid-disable      
   #                                                      
  #                                                       
  interface GigabitEthernet0/1/0   
   undo shutdown                                          
   ip address 172.16.1.1 255.255.255.0
  #                                                       
  interface GigabitEthernet0/2/0  
   undo shutdown                                          
   ipv6 enable                                            
   ipv6 address 2001:DB8:1::1/96                          
   isis ipv6 enable 1     
  #                                                       
  interface LoopBack1                                     
   ipv6 enable                                            
   ip address 2.2.2.9 255.255.255.255                     
   ipv6 address 2001:DB8:222::2/128
   ospf enable 1 area 0.0.0.0                     
   isis ipv6 enable 1                                     
   binding tunnel gre  
  #                                                       
  interface Tunnel10                                      
   ipv6 enable                   
   ipv6 address 2001:DB8:2::1/96                          
   tunnel-protocol gre                                    
   source 2.2.2.9                                         
   destination 3.3.3.9                                    
   isis ipv6 enable 1  
  #
  ospf 1                                                  
   opaque-capability enable                               
   area 0.0.0.0                                           
    network 2.2.2.9 0.0.0.0                               
    network 172.16.1.0 0.0.0.255                          
  #    
  return
  ```
* P2 configuration file
  ```
  #
  sysname P2
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 172.16.1.2 255.255.255.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 172.16.2.1 255.255.255.0
  #
  ospf 1
   opaque-capability enable 
   area 0.0.0.0
    network 172.16.1.0 0.0.0.255
    network 172.16.2.0 0.0.0.255
  ```
* P3 configuration file
  
  ```
  #
  sysname P3 
  #
  segment-routing ipv6                                    
   encapsulation source-address 2001:DB8:333::3           
   locator as1 ipv6-prefix 2001:DB8:30:: 64 static 32     
    opcode ::100 end-x interface GigabitEthernet0/2/0 nexthop 2001:DB8:3::2 psp 
    opcode ::200 end-x interface Tunnel10 nexthop 2001:DB8:2::1 psp      
  #                                                       
  isis 1                                                  
   is-level level-2                                       
   cost-style wide                                        
   network-entity 00.0005.0000.0000.0003.00               
   traffic-eng level-2                                    
   #                                                      
   ipv6 enable topology ipv6                              
   segment-routing ipv6 locator as1 auto-sid-disable      
   #                                                      
  #                                                       
  interface GigabitEthernet0/1/0                                 
   undo shutdown                                          
   ip address 172.16.2.2 255.255.255.0   
  #                                                       
  interface GigabitEthernet0/2/0                                 
   undo shutdown                                          
   ipv6 enable                                            
   ipv6 address 2001:DB8:3::1/96                          
   isis ipv6 enable 1 
  #                                                       
  interface LoopBack1                                     
   ipv6 enable                                            
   ip address 3.3.3.9 255.255.255.255                     
   ipv6 address 2001:DB8:333::3/128
   ospf enable 1 area 0.0.0.0                      
   isis ipv6 enable 1                                     
   binding tunnel gre  
  #                                                       
  interface Tunnel10                                      
   ipv6 enable                                                               
   ipv6 address 2001:DB8:2::2/96                          
   tunnel-protocol gre                                    
   source 3.3.3.9                                         
   destination 2.2.2.9                                    
   isis ipv6 enable 1  
  #                                                       
  ospf 1                                                  
   opaque-capability enable                               
   area 0.0.0.0                                           
    network 3.3.3.9 0.0.0.0                               
    network 172.16.2.0 0.0.0.255  
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  segment-routing ipv6                                    
   encapsulation source-address 2001:DB8:444::4           
   locator as1 ipv6-prefix 2001:DB8:40:: 64 static 32     
    opcode ::200 end-x interface GigabitEthernet0/1/0 nexthop 2001:DB8:3::1 psp 
    opcode ::4444 end-op                                  
   srv6-te-policy locator as1                             
   segment-list list1                                     
    index 5 sid ipv6 2001:DB8:40::200                     
    index 10 sid ipv6 2001:DB8:30::200                    
    index 15 sid ipv6 2001:DB8:20::200                    
   srv6-te policy policy1 endpoint 2001:DB8:111::1 color 101             
    binding-sid 2001:DB8:40::1000                         
    candidate-path preference 100                         
     segment-list list1                                   
  #                                                       
  isis 1                                                  
   is-level level-2                                       
   cost-style wide                                        
   network-entity 00.0005.0000.0000.0004.00               
   traffic-eng level-2                                    
   #                                                      
   ipv6 enable topology ipv6 
   segment-routing ipv6 locator as1 auto-sid-disable      
   #                                                      
  #                                                       
  interface GigabitEthernet0/1/0                                 
   undo shutdown                                          
   ipv6 enable                                            
   ipv6 address 2001:DB8:3::2/96                          
   isis ipv6 enable 1  
  #                                                       
  interface LoopBack1                                     
   ipv6 enable                                            
   ipv6 address 2001:DB8:444::4/128                       
   isis ipv6 enable 1   
  #
  return
  ```