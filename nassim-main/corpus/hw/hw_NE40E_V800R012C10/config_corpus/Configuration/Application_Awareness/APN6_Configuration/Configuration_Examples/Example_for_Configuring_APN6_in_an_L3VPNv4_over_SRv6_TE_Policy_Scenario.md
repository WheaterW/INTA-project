Example for Configuring APN6 in an L3VPNv4 over SRv6 TE Policy Scenario
=======================================================================

This section provides an example for configuring APN6 in an L3VPNv4 over SRv6 TE Policy scenario.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001245610756__fig184238288365):

* PE1, P1, P2, and PE2 are in the same AS. They are required to run IS-IS to achieve IPv6 network connectivity.
* PE1, P1, P2, and PE2 are Level-1 devices in IS-IS process 1.

It is required that a bidirectional SRv6 TE flow group be deployed between PE1 and PE2 to carry L3VPNv4 services.

SRv6 TE flow groups are used to implement APN ID-based traffic steering. During route recursion, the headend associates a service route with a specific SRv6 TE flow group based on the next-hop address of the route. The services carry APN IDs during forwarding. Based on the SRv6 mapping policy configuration, the services are first associated with a specific color and then a specific SRv6 TE Policy in the SRv6 TE flow group, thereby implementing APN ID-based traffic steering.

**Figure 1** L3VPNv4 over SRv6 TE flow group networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/1/0, GE 0/2/0, and GE 0/3/0, respectively.


  
![](figure/en-us_image_0000001245451476.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable IPv6 forwarding and configure an IPv6 address for each interface on PE1, P1, P2, and PE2.
2. Enable IS-IS, configure an IS-IS level, and specify a network entity title on PE1, P1, P2, and PE2.
3. Configure VPN instances on PE1 and PE2.
4. Establish an EBGP peer relationship between each PE and its connected CE.
5. Establish an MP-IBGP peer relationship between the PEs.
6. Configure SRv6 SIDs and enable IS-IS SRv6 on PE1, P1, P2, and PE2. In addition, configure PE1 and PE2 to advertise VPN routes carrying SIDs.
7. Deploy an SRv6 TE Policy on PE1 and PE2.
8. Configure APN6 instances on PE1 and PE2.
9. Configure a service flow filtering policy on PE1 and PE2 to ensure that APN IDs are generated for permitted service flows based on the specified generation mode.
10. Configure an SRv6 mapping policy on PE1 and PE2.
11. Configure a tunnel policy on PE1 and PE2 to preferentially use the SRv6 TE flow group for VPN traffic import.

#### Data Preparation

To complete the configuration, you need the following data.

* IPv6 address of each interface on PE1, P1, P2, and PE2
* IS-IS process ID of PE1, P1, P2, and PE2
* IS-IS level of PE1, P1, P2, and PE2
* VPN instance names, RDs, and RTs on PE1 and PE2

#### Procedure

1. Enable IPv6 forwarding and configure an IPv6 address for each interface.
   
   
   
   # Configure PE1. The configurations of P1, P2, and PE2 are similar to the configuration of PE1. For detailed configurations, see the configuration files.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname PE1
   [*HUAWEI] commit
   [~PE1] interface gigabitethernet 0/1/0
   [~PE1-GigabitEthernet0/1/0] ipv6 enable
   [*PE1-GigabitEthernet0/1/0] ipv6 address 2001:DB8:11::1 96
   [*PE1-GigabitEthernet0/1/0] quit
   [*PE1] interface gigabitethernet 0/3/0
   [*PE1-GigabitEthernet0/3/0] ipv6 enable
   [*PE1-GigabitEthernet0/3/0] ipv6 address 2001:DB8:13::1 96
   [*PE1-GigabitEthernet0/3/0] quit
   [*PE1] interface LoopBack 1
   [*PE1-LoopBack1] ipv6 enable
   [*PE1-LoopBack1] ipv6 address 2001:DB8:1::1 128
   [*PE1-LoopBack1] quit
   [*PE1] commit
   ```
2. Configure IS-IS.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] isis 1
   [*PE1-isis-1] is-level level-1
   [*PE1-isis-1] cost-style wide
   [*PE1-isis-1] network-entity 10.0000.0000.0001.00
   [*PE1-isis-1] ipv6 enable topology ipv6
   [*PE1-isis-1] quit
   [*PE1] interface gigabitethernet 0/1/0
   [*PE1-GigabitEthernet0/1/0] isis ipv6 enable 1
   [*PE1-GigabitEthernet0/1/0] quit
   [*PE1] interface gigabitethernet 0/3/0
   [*PE1-GigabitEthernet0/3/0] isis ipv6 enable 1
   [*PE1-GigabitEthernet0/3/0] quit
   [*PE1] interface loopback1
   [*PE1-LoopBack1] isis ipv6 enable 1
   [*PE1-LoopBack1] commit
   [~PE1-LoopBack1] quit
   ```
   
   # Configure P1.
   
   ```
   [~P1] isis 1 
   [*P1-isis-1] is-level level-1
   [*P1-isis-1] cost-style wide
   [*P1-isis-1] network-entity 10.0000.0000.0002.00
   [*P1-isis-1] ipv6 enable topology ipv6
   [*P1-isis-1] quit
   [*P1] interface gigabitethernet 0/1/0
   [*P1-GigabitEthernet0/1/0] isis ipv6 enable 1
   [*P1-GigabitEthernet0/1/0] quit
   [*P1] interface gigabitethernet 0/2/0
   [*P1-GigabitEthernet0/2/0] isis ipv6 enable 1
   [*P1-GigabitEthernet0/2/0] quit
   [*P1] interface loopback1
   [*P1-LoopBack1] isis ipv6 enable 1
   [*P1-LoopBack1] commit
   [~P1-LoopBack1] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] isis 1
   [*PE2-isis-1] is-level level-1
   [*PE2-isis-1] cost-style wide
   [*PE2-isis-1] network-entity 10.0000.0000.0003.00
   [*PE2-isis-1] ipv6 enable topology ipv6
   [*PE2-isis-1] quit
   [*PE2] interface gigabitethernet 0/1/0
   [*PE2-GigabitEthernet0/1/0] isis ipv6 enable 1
   [*PE2-GigabitEthernet0/1/0] quit
   [*PE2] interface gigabitethernet 0/3/0
   [*PE2-GigabitEthernet0/3/0] isis ipv6 enable 1
   [*PE2-GigabitEthernet0/3/0] quit
   [*PE2] interface loopback1
   [*PE2-LoopBack1] isis ipv6 enable 1
   [*PE2-LoopBack1] commit
   [~PE2-LoopBack1] quit
   ```
   
   
   
   # Configure P2.
   
   ```
   [~P2] isis 1 
   [*P2-isis-1] is-level level-1
   [*P2-isis-1] cost-style wide
   [*P2-isis-1] network-entity 10.0000.0000.0004.00
   [*P2-isis-1] ipv6 enable topology ipv6
   [*P2-isis-1] quit
   [*P2] interface gigabitethernet 0/1/0
   [*P2-GigabitEthernet0/1/0] isis ipv6 enable 1
   [*P2-GigabitEthernet0/1/0] quit
   [*P2] interface gigabitethernet 0/2/0
   [*P2-GigabitEthernet0/2/0] isis ipv6 enable 1
   [*P2-GigabitEthernet0/2/0] quit
   [*P2] interface loopback1
   [*P2-LoopBack1] isis ipv6 enable 1
   [*P2-LoopBack1] commit
   [~P2-LoopBack1] quit
   ```
   
   After completing the configuration, check whether IS-IS is successfully configured.
   
   # Display IS-IS neighbor information. The following example uses the command output on PE1.
   
   ```
   [~PE1] display isis peer
   
                             Peer information for ISIS(1)
                            
     System Id     Interface          Circuit Id        State HoldTime Type     PRI
   -------------------------------------------------------------------------------- 
   0000.0000.0002* GE0/1/0            0000.0000.0003.01  Up   9s       L1       64 
   0000.0000.0004* GE0/3/0            0000.0000.0004.02  Up   7s       L1       64   
   
   Total Peer(s): 2
   ```
3. Create a VPN instance and enable the IPv4 address family on each PE. Then, bind each PE's interface connected to a CE to the corresponding VPN instance.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] ip vpn-instance vpna
   [*PE1-vpn-instance-vpna] ipv4-family
   [*PE1-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
   [*PE1-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
   [*PE1-vpn-instance-vpna-af-ipv4] quit
   [*PE1-vpn-instance-vpna] quit
   [*PE1] interface gigabitethernet 0/2/0
   [*PE1-GigabitEthernet0/2/0] ip binding vpn-instance vpna
   [*PE1-GigabitEthernet0/2/0] ip address 10.1.1.1 24
   [*PE1-GigabitEthernet0/2/0] quit
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] ip vpn-instance vpna
   [*PE2-vpn-instance-vpna] ipv4-family
   [*PE2-vpn-instance-vpna-af-ipv4] route-distinguisher 200:1
   [*PE2-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
   [*PE2-vpn-instance-vpna-af-ipv4] quit
   [*PE2-vpn-instance-vpna] quit
   [*PE2] interface gigabitethernet 0/2/0
   [*PE2-GigabitEthernet0/2/0] ip binding vpn-instance vpna
   [*PE2-GigabitEthernet0/2/0] ip address 10.2.1.1 24
   [*PE2-GigabitEthernet0/2/0] quit
   [*PE2] commit
   ```
   
   # Configure an IP address for each interface on the CEs, as shown in [Figure 1](#EN-US_TASK_0000001245610756__fig184238288365). For detailed configurations, see the configuration files.
   
   After completing the configuration, run the **display ip vpn-instance verbose** command on each PE to check the VPN instance configuration. Confirm that each PE can ping its connected CE.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If a PE has multiple interfaces bound to the same VPN instance, specify a source IP address using the **-a** *source-ip-address* parameter in the **ping -vpn-instance** *vpn-instance-name* **-a** *source-ip-address dest-ip-address* command to ping the CE that is connected to the remote PE. If the source IP address is not specified, the ping operation may fail.
4. Establish an EBGP peer relationship between each PE and its connected CE.
   
   
   
   # Configure CE1.
   
   ```
   [~CE1] interface loopback 1
   [*CE1-LoopBack1] ip address 11.11.11.11 32
   [*CE1-LoopBack1] quit
   [*CE1] bgp 65410
   [*CE1-bgp] peer 10.1.1.1 as-number 100
   [*CE1-bgp] network 11.11.11.11 32
   [*CE1-bgp] quit
   [*CE1] commit
   ```
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   [*PE1-bgp] router-id 1.1.1.1
   [*PE1-bgp] ipv4-family vpn-instance vpna
   [*PE1-bgp-vpna] peer 10.1.1.2 as-number 65410
   [*PE1-bgp-vpna] import-route direct
   [*PE1-bgp-vpna] commit
   [~PE1-bgp-vpna] quit
   [~PE1-bgp] quit
   ```
   
   # Configure CE2.
   
   ```
   [~CE2] interface loopback 1
   [*CE2-LoopBack1] ip address 22.22.22.22 32
   [*CE2-LoopBack1] quit
   [*CE2] bgp 65420
   [*CE2-bgp] peer 10.2.1.1 as-number 100
   [*CE2-bgp] network 22.22.22.22 32
   [*CE2-bgp] quit
   [*CE2] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 100
   [*PE2-bgp] router-id 2.2.2.2
   [*PE2-bgp] ipv4-family vpn-instance vpna
   [*PE2-bgp-vpna] peer 10.2.1.2 as-number 65420
   [*PE2-bgp-vpna] import-route direct
   [*PE2-bgp-vpna] commit
   [~PE2-bgp-vpna] quit
   [~PE2-bgp] quit
   ```
   
   After completing the configuration, run the **display bgp vpnv4 vpn-instance peer** command on each PE to check whether a BGP peer relationship has been established between the PE and its connected CE. If the **Established** state is displayed in the command output, the BGP peer relationship has been established successfully.
   
   The following example uses the command output on PE1 to show that a relationship has been established between PE1 and CE1.
   
   ```
   [~PE1] display bgp vpnv4 vpn-instance vpna peer
   
    BGP local router ID : 1.1.1.1                                                  
    Local AS number : 100      
   
    VPN-Instance vpna, Router ID 1.1.1.1:                                          
    Total number of peers : 1                 Peers in established state : 1       
   
     Peer                             V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv                              
     10.1.1.2                         4       65410       88       89     0 01:12:27 Established        1 
   ```
5. Establish an MP-IBGP peer relationship between the PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   [~PE1-bgp] peer 2001:DB8:3::3 as-number 100
   [*PE1-bgp] peer 2001:DB8:3::3 connect-interface loopback 1
   [*PE1-bgp] ipv4-family vpnv4
   [*PE1-bgp-af-vpnv4] peer 2001:DB8:3::3 enable
   [*PE1-bgp-af-vpnv4] commit
   [~PE1-bgp-af-vpnv4] quit
   [~PE1-bgp] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 100
   [~PE2-bgp] peer 2001:DB8:1::1 as-number 100
   [*PE2-bgp] peer 2001:DB8:1::1 connect-interface loopback 1
   [*PE2-bgp] ipv4-family vpnv4
   [*PE2-bgp-af-vpnv4] peer 2001:DB8:1::1 enable
   [*PE2-bgp-af-vpnv4] commit
   [~PE2-bgp-af-vpnv4] quit
   [~PE2-bgp] quit
   ```
   
   After completing the configuration, run the **display bgp vpnv4 all peer** command on the PEs to check whether a BGP peer relationship has been established between them. If the **Established** state is displayed in the command output, the BGP peer relationship has been established successfully.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display bgp vpnv4 all peer
   
    BGP local router ID : 1.1.1.1                                                  
    Local AS number : 100      
    Total number of peers : 2                 Peers in established state : 2       
   
     Peer                             V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv                              
     2001:DB8:3::3                    4         100       85       85     0 01:10:30 Established        2                              
   
     Peer of IPv4-family for vpn instance :                                        
   
     VPN-Instance vpna, Router ID 1.1.1.1:                                         
     Peer                             V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv                              
     10.1.1.2                         4       65410       88       89     0 01:12:58 Established        1 
   ```
6. Configure SRv6 SIDs and configure the PEs to advertise VPN routes carrying SIDs.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   An End.DT4 SID can be either dynamically allocated through BGP or manually configured. If a dynamically allocated SID and a manually configured SID both exist, the latter takes effect. If you want to run the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* command to enable dynamic End.DT4 SID allocation through BGP or the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* [**end-dt46**](cmdqueryname=end-dt46) command to enable dynamic End.DT46 SID allocation through BGP in the future, you do not need to run the **opcode** *func-opcode* **end-dt4** **vpn-instance** *vpn-instance-name* or **opcode** *func-opcode* **end-dt46** **vpn-instance** *vpn-instance-name* command to configure an opcode for static SIDs.
   
   In this example, SIDs are dynamically allocated through BGP.
   
   # Configure PE1.
   
   ```
   [~PE1] segment-routing ipv6
   [*PE1-segment-routing-ipv6] encapsulation source-address 2001:DB8:1::1
   [*PE1-segment-routing-ipv6] locator as1 ipv6-prefix 2001:DB8:100:: 64 static 32
   [*PE1-segment-routing-ipv6-locator] opcode ::100 end psp
   [*PE1-segment-routing-ipv6-locator] opcode ::200 end no-flavor
   [*PE1-segment-routing-ipv6-locator] quit
   [*PE1-segment-routing-ipv6] quit
   [*PE1] bgp 100
   [*PE1-bgp] ipv4-family vpnv4
   [*PE1-bgp-af-vpnv4] peer 2001:DB8:3::3 prefix-sid
   [*PE1-bgp-af-vpnv4] quit
   [*PE1-bgp] ipv4-family vpn-instance vpna
   [*PE1-bgp-vpna] segment-routing ipv6 traffic-engineer best-effort
   [*PE1-bgp-vpna] segment-routing ipv6 locator as1
   [*PE1-bgp-vpna] commit
   [~PE1-bgp-vpna] quit
   [~PE1-bgp] quit
   [~PE1] isis 1
   [~PE1-isis-1] segment-routing ipv6 locator as1 auto-sid-disable
   [*PE1-isis-1] commit
   [~PE1-isis-1] quit
   ```
   
   # Configure P1.
   
   ```
   [~P1] segment-routing ipv6
   [*P1-segment-routing-ipv6] encapsulation source-address 2001:DB8:2::2
   [*P1-segment-routing-ipv6] locator as1 ipv6-prefix 2001:DB8:200:: 64 static 32
   [*P1-segment-routing-ipv6-locator] opcode ::100 end psp
   [*P1-segment-routing-ipv6-locator] opcode ::200 end no-flavor
   [*P1-segment-routing-ipv6-locator] quit
   [*P1-segment-routing-ipv6] quit
   [*P1] isis 1
   [*P1-isis-1] segment-routing ipv6 locator as1 auto-sid-disable
   [*P1-isis-1] commit
   [~P1-isis-1] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] segment-routing ipv6
   [*PE2-segment-routing-ipv6] encapsulation source-address 2001:DB8:3::3
   [*PE2-segment-routing-ipv6] locator as1 ipv6-prefix 2001:DB8:300:: 64 static 32
   [*PE2-segment-routing-ipv6-locator] opcode ::100 end psp
   [*PE2-segment-routing-ipv6-locator] opcode ::200 end no-flavor
   [*PE2-segment-routing-ipv6-locator] quit
   [*PE2-segment-routing-ipv6] quit
   [*PE2] bgp 100
   [*PE2-bgp] ipv4-family vpnv4
   [*PE2-bgp-af-vpnv4] peer 2001:DB8:1::1 prefix-sid
   [*PE2-bgp-af-vpnv4] quit
   [*PE2-bgp] ipv4-family vpn-instance vpna
   [*PE2-bgp-vpna] segment-routing ipv6 traffic-engineer best-effort
   [*PE2-bgp-vpna] segment-routing ipv6 locator as1
   [*PE2-bgp-vpna] commit
   [~PE2-bgp-vpna] quit
   [~PE2-bgp] quit
   [~PE2] isis 1
   [~PE2-isis-1] segment-routing ipv6 locator as1 auto-sid-disable
   [*PE2-isis-1] commit
   [~PE2-isis-1] quit
   ```
   
   # Configure P2.
   
   ```
   [~P2] segment-routing ipv6
   [*P2-segment-routing-ipv6] encapsulation source-address 2001:DB8:4::4
   [*P2-segment-routing-ipv6] locator as1 ipv6-prefix 2001:DB8:400:: 64 static 32
   [*P2-segment-routing-ipv6-locator] opcode ::100 end psp
   [*P2-segment-routing-ipv6-locator] opcode ::200 end no-flavor
   [*P2-segment-routing-ipv6-locator] quit
   [*P2-segment-routing-ipv6] quit
   [*P2] isis 1
   [*P2-isis-1] segment-routing ipv6 locator as1 auto-sid-disable
   [*P2-isis-1] commit
   [~P2-isis-1] quit
   ```
   
   Run the [**display segment-routing ipv6 local-sid**](cmdqueryname=display+segment-routing+ipv6+local-sid) **end** **forwarding** command to check information about the SRv6 local SID table.
   
   ```
   [~PE1] display segment-routing ipv6 local-sid end forwarding
                       My Local-SID End Forwarding Table                        
                       ---------------------------------                        
   
   SID         : 2001:DB8:100::100/128                        FuncType    : End 
   Flavor      : PSP     
   LocatorName : as1                                          LocatorID   : 1   
   ProtocolType: STATIC                                       ProcessID   : --  
   UpdateTime  : 2021-05-05 09:24:18.785                                        
   
   SID         : 2001:DB8:100::200/128                        FuncType    : End 
   Flavor      : NO-FLAVOR                                                      
   LocatorName : as1                                          LocatorID   : 1   
   ProtocolType: STATIC                                       ProcessID   : --  
   UpdateTime  : 2021-05-05 09:24:18.785                                        
   
   Total SID(s): 2  
   ```
   ```
   [~P1] display segment-routing ipv6 local-sid end forwarding
                       My Local-SID End Forwarding Table                        
                       ---------------------------------                        
   
   SID         : 2001:DB8:200::100/128                        FuncType    : End 
   Flavor      : PSP     
   LocatorName : as1                                          LocatorID   : 1   
   ProtocolType: STATIC                                       ProcessID   : --  
   UpdateTime  : 2021-05-05 09:29:22.633                                        
   
   SID         : 2001:DB8:200::200/128                        FuncType    : End 
   Flavor      : NO-FLAVOR                                                      
   LocatorName : as1                                          LocatorID   : 1   
   ProtocolType: STATIC                                       ProcessID   : --  
   UpdateTime  : 2021-05-05 09:29:22.633                                        
   
   Total SID(s): 2
   ```
   ```
   [~PE2] display segment-routing ipv6 local-sid end forwarding
                       My Local-SID End Forwarding Table                        
                       ---------------------------------                        
   
   SID         : 2001:DB8:300::100/128                        FuncType    : End 
   Flavor      : PSP     
   LocatorName : as1                                          LocatorID   : 1   
   ProtocolType: STATIC                                       ProcessID   : --  
   UpdateTime  : 2021-05-05 09:36:31.017                                        
   
   SID         : 2001:DB8:300::200/128                        FuncType    : End 
   Flavor      : NO-FLAVOR                                                      
   LocatorName : as1                                          LocatorID   : 1   
   ProtocolType: STATIC                                       ProcessID   : --  
   UpdateTime  : 2021-05-05 09:36:31.017                                        
   
   Total SID(s): 2 
   ```
   ```
   [~P2] display segment-routing ipv6 local-sid end forwarding
                       My Local-SID End Forwarding Table                        
                       ---------------------------------                        
   
   SID         : 2001:DB8:400::100/128                        FuncType    : End 
   Flavor      : PSP     
   LocatorName : as1                                          LocatorID   : 1   
   ProtocolType: STATIC                                       ProcessID   : --  
   UpdateTime  : 2021-05-05 09:32:38.292                                        
   
   SID         : 2001:DB8:400::200/128                        FuncType    : End 
   Flavor      : NO-FLAVOR                                                      
   LocatorName : as1                                          LocatorID   : 1   
   ProtocolType: STATIC                                       ProcessID   : --  
   UpdateTime  : 2021-05-05 09:32:38.292                                        
   
   Total SID(s): 2
   ```
7. Configure an SRv6 TE Policy.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] segment-routing ipv6 
   [~PE1-segment-routing-ipv6] segment-list list1 
   [*PE1-segment-routing-ipv6-segment-list-list1] index 5 sid ipv6 2001:DB8:200::100
   [*PE1-segment-routing-ipv6-segment-list-list1] index 10 sid ipv6 2001:DB8:300::100
   [*PE1-segment-routing-ipv6-segment-list-list1] quit
   [*PE1-segment-routing-ipv6] segment-list list2 
   [*PE1-segment-routing-ipv6-segment-list-list2] index 5 sid ipv6 2001:DB8:400::100
   [*PE1-segment-routing-ipv6-segment-list-list2] index 10 sid ipv6 2001:DB8:300::100
   [*PE1-segment-routing-ipv6-segment-list-list2] quit
   [*PE1-segment-routing-ipv6] srv6-te-policy locator as1 
   [*PE1-segment-routing-ipv6] srv6-te policy policy1 endpoint 2001:DB8:3::3 color 10
   [*PE1-segment-routing-ipv6-policy-policy1] binding-sid 2001:DB8:100::900
   [*PE1-segment-routing-ipv6-policy-policy1] candidate-path preference 100
   [*PE1-segment-routing-ipv6-policy-policy1-path] segment-list list1 
   [*PE1-segment-routing-ipv6-policy-policy1-path] quit
   [*PE1-segment-routing-ipv6-policy-policy1] quit
   [*PE1-segment-routing-ipv6] srv6-te policy policy2 endpoint 2001:DB8:3::3 color 20
   [*PE1-segment-routing-ipv6-policy-policy2] binding-sid 2001:DB8:100::901
   [*PE1-segment-routing-ipv6-policy-policy2] candidate-path preference 100
   [*PE1-segment-routing-ipv6-policy-policy2-path] segment-list list2 
   [*PE1-segment-routing-ipv6-policy-policy2-path] commit
   [~PE1-segment-routing-ipv6-policy-policy2-path] quit
   [~PE1-segment-routing-ipv6-policy-policy2] quit
   [~PE1-segment-routing-ipv6] quit
   ```
   
   
   
   # Configure PE2.
   
   ```
   [~PE2] segment-routing ipv6 
   [~PE2-segment-routing-ipv6] segment-list list1 
   [*PE2-segment-routing-ipv6-segment-list-list1] index 5 sid ipv6 2001:DB8:200::100
   [*PE2-segment-routing-ipv6-segment-list-list1] index 10 sid ipv6 2001:DB8:100::100
   [*PE2-segment-routing-ipv6-segment-list-list1] quit
   [*PE2-segment-routing-ipv6] segment-list list2 
   [*PE2-segment-routing-ipv6-segment-list-list2] index 5 sid ipv6 2001:DB8:400::100
   [*PE2-segment-routing-ipv6-segment-list-list2] index 10 sid ipv6 2001:DB8:100::100
   [*PE2-segment-routing-ipv6-segment-list-list2] quit
   [*PE2-segment-routing-ipv6] srv6-te-policy locator as1 
   [*PE2-segment-routing-ipv6] srv6-te policy policy1 endpoint 2001:DB8:1::1 color 10
   [*PE2-segment-routing-ipv6-policy-policy1] binding-sid 2001:DB8:300::900
   [*PE2-segment-routing-ipv6-policy-policy1] candidate-path preference 100
   [*PE2-segment-routing-ipv6-policy-policy1-path] segment-list list1 
   [*PE2-segment-routing-ipv6-policy-policy1-path] quit
   [*PE2-segment-routing-ipv6-policy-policy1] quit
   [*PE2-segment-routing-ipv6] srv6-te policy policy2 endpoint 2001:DB8:1::1 color 20
   [*PE2-segment-routing-ipv6-policy-policy2] binding-sid 2001:DB8:300::901
   [*PE2-segment-routing-ipv6-policy-policy2] candidate-path preference 100
   [*PE2-segment-routing-ipv6-policy-policy2-path] segment-list list2 
   [*PE2-segment-routing-ipv6-policy-policy2-path] commit
   [~PE2-segment-routing-ipv6-policy-policy2-path] quit
   [~PE2-segment-routing-ipv6-policy-policy2] quit
   [~PE2-segment-routing-ipv6] quit
   ```
   
   After completing the configuration, run the **display srv6-te policy** command to check SRv6 TE Policy information.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display srv6-te policy 
   PolicyName : policy1  
   Color                   : 10                             Endpoint             : 2001:DB8:3::3                  
   TunnelId                : 1                                          
   TunnelType              : SRv6-TE Policy                 DelayTimerRemain     : -                                                   
   Policy State            : Up                             State Change Time    : 2021-05-05 09:24:24
   Admin State             : Up                             Traffic Statistics   : Disable  
   Backup Hot-Standby      : Disable                        BFD                  : Disable  
   Interface Index         : -                              Interface Name       : -        
   Interface State         : -                              Encapsulation Mode   : Insert
   Binding SID             : 2001:DB8:100::900(Insert, Preferred)
   Candidate-path Count    : 1       
   
    Candidate-path Preference : 100
    
    Path State             : Active                         Path Type            : Primary  
    Protocol-Origin        : Configuration(30)              Originator           : 0, 0.0.0.0                                          
    Discriminator          : 100                            Binding SID          : 2001:DB8:100::900  
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
            2001:DB8:200::100      
            2001:DB8:300::100      
   
   PolicyName : policy2  
   Color                   : 20                             Endpoint             : 2001:DB8:3::3     
   TunnelId                : 2                                
   TunnelType              : SRv6-TE Policy                 DelayTimerRemain     : -        
   Policy State            : Up                             State Change Time    : 2021-05-05 09:24:24
   Admin State             : Up                             Traffic Statistics   : Disable  
   Backup Hot-Standby      : Disable                        BFD                  : Disable  
   Interface Index         : -                              Interface Name       : -        
   Interface State         : -                              Encapsulation Mode   : Insert
   Binding SID             : 2001:DB8:100::901(Insert, Preferred)
   Candidate-path Count    : 1 
   
    Candidate-path Preference : 100
    Path State             : Active                         Path Type            : Primary  
    Protocol-Origin        : Configuration(30)              Originator           : 0, 0.0.0.0                    
    Discriminator          : 100                            Binding SID          : 2001:DB8:100::901  
    GroupId                : 2                              Policy Name          : policy2  
    Template ID            : 0                              Path Verification    : Disable  
    DelayTimerRemain       : -                              Network Slice ID     : -
    Segment-List Count     : 1       
     Segment-List          : list2   
      Segment-List ID      : 2                              XcIndex              : 2        
      List State           : Up                             DelayTimerRemain     : -        
      Verification State   : -                              SuppressTimeRemain   : -        
      PMTU                 : 9600                           Active PMTU          : 9600     
      Weight               : 1                              BFD State            : -        
      Loop Detection State : Up                             BFD Delay Remain     : - 
      Network Slice ID     : -  
      Binding SID          : -
      Reverse Binding ID   : -
      SID :              
            2001:DB8:400::100      
            2001:DB8:300::100  
   ```
8. Configure an APN6 instance.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] apn 
   [*PE1-apn] ipv6 
   [*PE1-apn-ipv6] apn-id template tmplt1 length 64 app-group 16 
   [*PE1-apn-ipv6-template-tmplt1] app-group index 1 app-group1 length 16 
   [*PE1-apn-ipv6-template-tmplt1] quit 
   [*PE1-apn-ipv6] apn-id instance APN6-instance1 
   [*PE1-apn-ipv6-instance-APN6-instance1] template tmplt1 
   [*PE1-apn-ipv6-instance-APN6-instance1] apn-field app-group1 1 
   [*PE1-apn-ipv6-instance-APN6-instance1] commit 
   [~PE1-apn-ipv6-instance-APN6-instance1] quit 
   [~PE1-apn-ipv6] quit 
   [~PE1-apn] quit
   ```
   
   
   
   # Configure PE2.
   
   ```
   [~PE2] apn 
   [*PE2-apn] ipv6 
   [*PE2-apn-ipv6] apn-id template tmplt1 length 64 app-group 16 
   [*PE2-apn-ipv6-template-tmplt1] app-group index 1 app-group1 length 16 
   [*PE2-apn-ipv6-template-tmplt1] quit 
   [*PE2-apn-ipv6] apn-id instance APN6-instance1 
   [*PE2-apn-ipv6-instance-APN6-instance1] template tmplt1 
   [*PE2-apn-ipv6-instance-APN6-instance1] apn-field app-group1 1 
   [*PE2-apn-ipv6-instance-APN6-instance1] commit 
   [~PE2-apn-ipv6-instance-APN6-instance1] quit 
   [~PE2-apn-ipv6] quit 
   [~PE2-apn] quit
   ```
9. Configure a service flow filtering policy to ensure that APN IDs are generated for permitted service flows based on the specified generation mode.
   
   # Configure PE1.
   ```
   [~PE1] acl number 3333
   [*PE1-acl-advance-3333] rule 5 permit ip source 11.11.11.11 0 destination 22.22.22.22 0
   [*PE1-acl-advance-3333] commit
   [~PE1-acl-advance-3333] quit
   [~PE1] traffic classifier c1
   [*PE1-classifier-c1] if-match acl 3333
   [*PE1-classifier-c1] commit
   [~PE1-classifier-c1] quit
   [~PE1] traffic behavior b1
   [*PE1-behavior-b1] remark apn-id-ipv6 instance APN6-instance1
   [*PE1-behavior-b1] commit
   [~PE1-behavior-b1] quit
   [~PE1] traffic policy p1
   [*PE1-trafficpolicy-p1] classifier c1 behavior b1
   [*PE1-trafficpolicy-p1] share-mode
   [*PE1-trafficpolicy-p1] statistics enable
   [*PE1-trafficpolicy-p1] quit
   [*PE1] interface GigabitEthernet 0/2/0
   [*PE1-GigabitEthernet0/2/0] traffic-policy p1 inbound
   [*PE1-GigabitEthernet0/2/0] commit
   [~PE1-GigabitEthernet0/2/0] quit
   ```
   
   
   # Configure PE2.
   ```
   [~PE2] acl number 3333
   [*PE2-acl-advance-3333] rule 5 permit ip source 22.22.22.22 0 destination 11.11.11.11 0
   [*PE2-acl-advance-3333] commit
   [~PE2-acl-advance-3333] quit
   [~PE2] traffic classifier c1
   [*PE2-classifier-c1] if-match acl 3333
   [*PE2-classifier-c1] commit
   [~PE2-classifier-c1] quit
   [~PE2] traffic behavior b1
   [*PE2-behavior-b1] remark apn-id-ipv6 instance APN6-instance1
   [*PE2-behavior-b1] commit
   [~PE2-behavior-b1] quit
   [~PE2] traffic policy p1
   [*PE2-trafficpolicy-p1] classifier c1 behavior b1
   [*PE2-trafficpolicy-p1] share-mode
   [*PE2-trafficpolicy-p1] statistics enable
   [*PE2-trafficpolicy-p1] quit
   [*PE2] interface GigabitEthernet 0/2/0
   [*PE2-GigabitEthernet0/2/0] traffic-policy p1 inbound
   [*PE2-GigabitEthernet0/2/0] commit
   [~PE2-GigabitEthernet0/2/0] quit
   ```
10. Configure an SRv6 mapping policy.
    
    
    
    After an SRv6 mapping policy is configured for a device, the device matches the associated service route against the SRv6 mapping policy that has the same color value as the route. If such a mapping policy is found, the device dynamically generates an SRv6 TE flow group that contains multiple SRv6 TE Policies with the same endpoint but different color values.
    
    In this example, traffic of APN6-instance1 is forwarded through policy1, and other traffic is forwarded through policy2 by default.
    
    # Configure PE1.
    
    ```
    [~PE1] segment-routing ipv6 
    [~PE1-segment-routing-ipv6] mapping-policy p1 color 101  
    [*PE1-segment-routing-ipv6-mapping-policy-p1] match-type apn-id-ipv6
    [*PE1-segment-routing-ipv6-mapping-policy-p1-apn-id-ipv6] index 10 instance APN6-instance1 match srv6-te-policy color 10 
    [*PE1-segment-routing-ipv6-mapping-policy-p1-apn-id-ipv6] default match srv6-te-policy color 20
    [*PE1-segment-routing-ipv6-mapping-policy-p1-apn-id-ipv6] quit
    [*PE1-segment-routing-ipv6-mapping-policy-p1] quit
    [*PE1-segment-routing-ipv6] commit
    [~PE1-segment-routing-ipv6] quit
    ```
    
    # Configure PE2.
    
    ```
    [~PE2] segment-routing ipv6 
    [~PE2-segment-routing-ipv6] mapping-policy p1 color 101  
    [*PE2-segment-routing-ipv6-mapping-policy-p1] match-type apn-id-ipv6
    [*PE2-segment-routing-ipv6-mapping-policy-p1-apn-id-ipv6] index 10 instance APN6-instance1 match srv6-te-policy color 10 
    [*PE2-segment-routing-ipv6-mapping-policy-p1-apn-id-ipv6] default match srv6-te-policy color 20
    [*PE2-segment-routing-ipv6-mapping-policy-p1-apn-id-ipv6] quit
    [*PE2-segment-routing-ipv6-mapping-policy-p1] quit
    [*PE2-segment-routing-ipv6] commit
    [~PE2-segment-routing-ipv6] quit
    ```
11. Configure a tunnel policy to import VPN traffic.
    
    
    
    # Configure PE1.
    
    ```
    [~PE1] route-policy p1 permit node 10
    [*PE1-route-policy] apply extcommunity color 0:101
    [*PE1-route-policy] quit
    [*PE1] bgp 100
    [*PE1-bgp] ipv4-family vpnv4
    [*PE1-bgp-af-vpnv4] peer 2001:DB8:3::3 route-policy p1 import 
    [*PE1-bgp-af-vpnv4] quit
    [*PE1-bgp] quit
    [*PE1] tunnel-policy p1
    [*PE1-tunnel-policy-p1] tunnel select-seq ipv6 srv6-te-flow-group load-balance-number 1
    [*PE1-tunnel-policy-p1] quit
    [*PE1] ip vpn-instance vpna
    [*PE1-vpn-instance-vpna] ipv4-family
    [*PE1-vpn-instance-vpna-af-ipv4] tnl-policy p1
    [*PE1-vpn-instance-vpna-af-ipv4] commit
    [~PE1-vpn-instance-vpna-af-ipv4] quit
    [~PE1-vpn-instance-vpna] quit
    ```
    
    
    
    # Configure PE2.
    
    ```
    [~PE2] route-policy p1 permit node 10
    [*PE2-route-policy] apply extcommunity color 0:101
    [*PE2-route-policy] quit
    [*PE2] bgp 100
    [*PE2-bgp] ipv4-family vpnv4
    [*PE2-bgp-af-vpnv4] peer 2001:DB8:1::1 route-policy p1 import 
    [*PE2-bgp-af-vpnv4] quit
    [*PE2-bgp] quit
    [*PE2] tunnel-policy p1
    [*PE2-tunnel-policy-p1] tunnel select-seq ipv6 srv6-te-flow-group load-balance-number 1
    [*PE2-tunnel-policy-p1] quit
    [*PE2] ip vpn-instance vpna
    [*PE2-vpn-instance-vpna] ipv4-family
    [*PE2-vpn-instance-vpna-af-ipv4] tnl-policy p1
    [*PE2-vpn-instance-vpna-af-ipv4] commit
    [~PE2-vpn-instance-vpna-af-ipv4] quit
    [~PE2-vpn-instance-vpna] quit
    ```
    
    After completing the configuration, run the **display srv6-te flow-group** command to check the status of the dynamically created SRv6 TE flow group.
    
    The following example uses the command output on PE1.
    
    ```
    [~PE1] display srv6-te flow-group                                             
    
                              SRv6-TE Flow Group Information                     
    ------------------------------------------------------------------------------------  
    Group Name          :          
    Color               : 101                           Endpoint            : 2001:DB8:3::3                                       
    Group Tunnel ID     : 3                             Group Tunnel Type   : SRv6-TE Flow Group
    Group Tunnel State  : Up                            State Change Time   : 2021-05-05 09:38:19 
    Interface Index     : -                             Interface Name      : -   
    Interface State     : -
    Delay Timer Remain  : -                             UP/ALL Num          : 2/2                    
    
     Index                : -
     APN ID IPv6 Instance : Default(Configure)
     Match Tunnel         : SRv6-TE Policy                State               : Up
     Color                : 20                            Tunnel Id           : 1
    
     Index                : 1
     APN ID IPv6 Instance : APN6-instance1
     Match Tunnel         : SRv6-TE Policy                State               : Up
     Color                : 10                            Tunnel Id           : 1
    
    ```
    
    After completing the configuration, run the **display ip routing-table vpn-instance vpna** command to check that the VPN route has successfully recursed to the SRv6 TE Policy.
    
    The following example uses the command output on PE1.
    
    ```
    [~PE1] display ip routing-table vpn-instance vpna 
    Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
    ------------------------------------------------------------------------------ 
    Routing Table : vpna                           
             Destinations : 8        Routes : 8  
    
    Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface    
    
           10.1.1.0/24  Direct  0    0             D   10.1.1.1        GigabitEthernet0/2/0  
           10.1.1.1/32  Direct  0    0             D   127.0.0.1       GigabitEthernet0/2/0        
         10.1.1.255/32  Direct  0    0             D   127.0.0.1       GigabitEthernet0/2/0       
           10.2.1.0/24  IBGP    255  0             RD  2001:DB8:3::3   SRv6-TE Flow Group         
        11.11.11.11/32  EBGP    255  0             RD  10.1.1.2        GigabitEthernet0/2/0         
        22.22.22.22/32  IBGP    255  0             RD  2001:DB8:3::3   SRv6-TE Flow Group  
          127.0.0.0/8   Direct  0    0             D   127.0.0.1       InLoopBack0                 
    255.255.255.255/32  Direct  0    0             D   127.0.0.1       InLoopBack0 
    ```
    ```
    [~PE1] display ip routing-table vpn-instance vpna 22.22.22.22 verbose 
     Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route                                              
    ------------------------------------------------------------------------------  
    Routing Table : vpna        
    Summary Count : 1           
    
    Destination: 22.22.22.22/32 
         Protocol: IBGP               Process ID: 0                                 
       Preference: 255                      Cost: 0                                 
          NextHop: 2001:DB8:3::3       Neighbour: 2001:DB8:3::3                              
            State: Active Adv Relied         Age: 01h04m44s                         
              Tag: 0                    Priority: low                               
            Label: 3                     QoSInfo: 0x0                               
       IndirectID: 0x10000DE            Instance:                                   
     RelayNextHop: ::                  Interface: SRv6-TE Flow Group              
         TunnelID: 0x000000003700002001    Flags: RD 
    ```
12. Verify the configuration.
    
    
    
    Check that the CEs belonging to the same VPN instance can ping each other. For example:
    
    ```
    [~CE1] ping -a 11.11.11.11 22.22.22.22
      PING 22.22.22.22: 56  data bytes, press CTRL_C to break                       
        Reply from 22.22.22.22: bytes=56 Sequence=1 ttl=253 time=85 ms              
        Reply from 22.22.22.22: bytes=56 Sequence=2 ttl=253 time=33 ms              
        Reply from 22.22.22.22: bytes=56 Sequence=3 ttl=253 time=32 ms              
        Reply from 22.22.22.22: bytes=56 Sequence=4 ttl=253 time=30 ms              
        Reply from 22.22.22.22: bytes=56 Sequence=5 ttl=253 time=24 ms              
    
      --- 22.22.22.22 ping statistics ---                                           
        5 packet(s) transmitted 
        5 packet(s) received    
        0.00% packet loss       
        round-trip min/avg/max = 24/40/85 ms 
    ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 100:1
    apply-label per-instance
    tnl-policy p1
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  #
  apn
   ipv6
    apn-id template tmplt1 length 64 app-group 16
     app-group index 1 app-group1 length 16
    apn-id instance APN6-instance1
     template tmplt1
     apn-field app-group1 1
  #
  acl number 3333
   rule 5 permit ip source 11.11.11.11 0 destination 22.22.22.22 0
  #
  traffic classifier c1
   if-match acl 3333
  #
  traffic behavior b1
   remark apn-id-ipv6 instance APN6-instance1
  #        
  traffic policy p1
   share-mode
   statistics enable
   classifier c1 behavior b1 precedence 1
  #               
  segment-routing ipv6
   encapsulation source-address 2001:DB8:1::1                                              
   locator as1 ipv6-prefix 2001:DB8:100:: 64 static 32                                     
    opcode ::100 end psp      
    opcode ::200 end no-flavor
   srv6-te-policy locator as1 
   segment-list list1         
    index 5 sid ipv6 2001:DB8:200::100  
    index 10 sid ipv6 2001:DB8:300::100 
   segment-list list2         
    index 5 sid ipv6 2001:DB8:400::100  
    index 10 sid ipv6 2001:DB8:300::100 
   srv6-te policy policy1 endpoint 2001:DB8:3::3 color 10                                  
    binding-sid 2001:DB8:100::900       
    candidate-path preference 100     
     segment-list list1       
   srv6-te policy policy2 endpoint 2001:DB8:3::3 color 20                                  
    binding-sid 2001:DB8:100::901       
    candidate-path preference 100 
     segment-list list2       
   mapping-policy p1 color 101     
    match-type apn-id-ipv6 
     index 10 instance APN6-instance1 match srv6-te-policy color 10
     default match srv6-te-policy color 20
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
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:11::1/96
   isis ipv6 enable 1
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip binding vpn-instance vpna
   ip address 10.1.1.1 255.255.255.0
   traffic-policy p1 inbound
  #               
  interface GigabitEthernet0/3/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:13::1/96
   isis ipv6 enable 1
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:1::1/128
   isis ipv6 enable 1
  #               
  bgp 100         
   router-id 1.1.1.1
   peer 2001:DB8:3::3 as-number 100
   peer 2001:DB8:3::3 connect-interface LoopBack1
   #              
   ipv4-family unicast
    undo synchronization
   #              
   ipv6-family unicast
    undo synchronization
   #              
   ipv4-family vpnv4
    policy vpn-target
    peer 2001:DB8:3::3 enable
    peer 2001:DB8:3::3 route-policy p1 import
    peer 2001:DB8:3::3 prefix-sid
   #              
   ipv4-family vpn-instance vpna
    import-route direct
    segment-routing ipv6 locator as1
    segment-routing ipv6 traffic-engineer best-effort
    peer 10.1.1.2 as-number 65410
  #               
  route-policy p1 permit node 10
   apply extcommunity color 0:101
  #               
  tunnel-policy p1
   tunnel select-seq ipv6 srv6-te-flow-group load-balance-number 1
  #               
  return 
  ```
* P1 configuration file
  
  ```
  #
  sysname P1        
  #               
  segment-routing ipv6
   encapsulation source-address 2001:DB8:2::2
   locator as1 ipv6-prefix 2001:DB8:200:: 64 static 32
    opcode ::100 end psp
    opcode ::200 end no-flavor
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
   ipv6 address 2001:DB8:11::2/96
   isis ipv6 enable 1 
  # 
  interface GigabitEthernet0/2/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:12::1/96
   isis ipv6 enable 1  
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:2::2/128
   isis ipv6 enable 1
  #               
  return 
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 200:1
    apply-label per-instance
    tnl-policy p1
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  #
  apn
   ipv6
    apn-id template tmplt1 length 64 app-group 16
     app-group index 1 app-group1 length 16
    apn-id instance APN6-instance1
     template tmplt1
     apn-field app-group1 1
  #
  acl number 3333
   rule 5 permit ip source 22.22.22.22 0 destination 11.11.11.11 0
  #
  traffic classifier c1
   if-match acl 3333
  #
  traffic behavior b1
   remark apn-id-ipv6 instance APN6-instance1
  #        
  traffic policy p1
   share-mode
   statistics enable
   classifier c1 behavior b1 precedence 1
  #               
  segment-routing ipv6
   encapsulation source-address 2001:DB8:3::3                                              
   locator as1 ipv6-prefix 2001:DB8:300:: 64 static 32                                     
    opcode ::100 end psp          
    opcode ::200 end no-flavor 
   srv6-te-policy locator as1 
   segment-list list1         
    index 5 sid ipv6 2001:DB8:200::100  
    index 10 sid ipv6 2001:DB8:100::100 
   segment-list list2         
    index 5 sid ipv6 2001:DB8:400::100  
    index 10 sid ipv6 2001:DB8:100::100 
   srv6-te policy policy1 endpoint 2001:DB8:1::1 color 10                                  
    binding-sid 2001:DB8:300::900       
    candidate-path preference 100     
     segment-list list1       
   srv6-te policy policy2 endpoint 2001:DB8:1::1 color 20                                  
    binding-sid 2001:DB8:300::901       
    candidate-path preference 100          
     segment-list list2       
   mapping-policy p1 color 101     
    match-type apn-id-ipv6 
     index 10 instance APN6-instance1 match srv6-te-policy color 10
     default match srv6-te-policy color 20
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0003.00
   #              
   ipv6 enable topology ipv6
   segment-routing ipv6 locator as1 auto-sid-disable  
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:12::2/96
   isis ipv6 enable 1
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip binding vpn-instance vpna
   ip address 10.2.1.1 255.255.255.0
   traffic-policy p1 inbound
  #               
  interface GigabitEthernet0/3/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:14::2/96
   isis ipv6 enable 1
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:3::3/128
   isis ipv6 enable 1
  #               
  bgp 100         
   router-id 2.2.2.2
   peer 2001:DB8:1::1 as-number 100
   peer 2001:DB8:1::1 connect-interface LoopBack1
   #              
   ipv4-family unicast
    undo synchronization
   #              
   ipv6-family unicast
    undo synchronization
   #              
   ipv4-family vpnv4
    policy vpn-target
    peer 2001:DB8:1::1 enable
    peer 2001:DB8:1::1 route-policy p1 import
    peer 2001:DB8:1::1 prefix-sid
   #              
   ipv4-family vpn-instance vpna
    import-route direct
    segment-routing ipv6 locator as1
    segment-routing ipv6 traffic-engineer best-effort
    peer 10.2.1.2 as-number 65420
  #               
  route-policy p1 permit node 10
   apply extcommunity color 0:101
  #               
  tunnel-policy p1
   tunnel select-seq ipv6 srv6-te-flow-group load-balance-number 1
  #               
  return
  ```
* P2 configuration file
  
  ```
  #
  sysname P2        
  #               
  segment-routing ipv6
   encapsulation source-address 2001:DB8:4::4
   locator as1 ipv6-prefix 2001:DB8:400:: 64 static 32
    opcode ::100 end psp
    opcode ::200 end no-flavor
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
   ipv6 address 2001:DB8:13::2/96
   isis ipv6 enable 1 
  # 
  interface GigabitEthernet0/2/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:14::1/96
   isis ipv6 enable 1  
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:4::4/128
   isis ipv6 enable 1
  #               
  return 
  ```
* CE1 configuration file
  
  ```
  #
  sysname CE1
  #
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.1.1.2 255.255.255.0
  #               
  interface LoopBack1
   ip address 11.11.11.11 255.255.255.255
  #               
  bgp 65410       
   peer 10.1.1.1 as-number 100
   #              
   ipv4-family unicast
    undo synchronization
    network 11.11.11.11 255.255.255.255
    peer 10.1.1.1 enable
  #               
  return 
  ```
* CE2 configuration file
  
  ```
  #
  sysname CE2
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.2.1.2 255.255.255.0
  #
  interface LoopBack1
   ip address 22.22.22.22 255.255.255.255
  #
  bgp 65420
   peer 10.2.1.1 as-number 100
  #
   ipv4-family unicast
    undo synchronization
    network 22.22.22.22 255.255.255.255
    peer 10.2.1.1 enable
  #
  return
  ```