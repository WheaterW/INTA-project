Example for Configuring EVPN VPWS over SRv6 TE Policy (Manual Configuration)
============================================================================

This section provides an example for configuring an SRv6 TE Policy to carry EVPN VPWSs.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001200879069__en-us_task_0185640031_fig1367823242219), PE1, the P, and PE2 are in the same AS and need to run IS-IS to implement IPv6 network connectivity. In addition, a bidirectional SRv6 TE Policy needs to be deployed between PE1 and PE2 to carry EVPN VPWSs.

**Figure 1** EVPN VPWS over SRv6 TE Policy networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](figure/en-us_image_0185646682.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable IPv6 forwarding and configure an IPv6 address for each interface on PE1, the P, and PE2.
2. Enable IS-IS, configure an IS-IS level, and specify a network entity title (NET) on PE1, the P, and PE2.
3. Configure EVPN VPWS and EVPL instances on each PE and bind the EVPL instance to an access-side sub-interface.
4. Establish a BGP EVPN peer relationship between PEs.
5. Configure SRv6 SIDs and enable IS-IS SRv6 on PE1, the P, and PE2. In addition, configure PE1 and PE2 to advertise VPN routes carrying SIDs.
6. Configure an SRv6 TE Policy on PE1 and PE2.
7. Configure a tunnel policy on PE1 and PE2 to import VPN traffic.

#### Data Preparation

To complete the configuration, you need the following data:

* IPv6 address of each interface on PE1, the P, and PE2
* IS-IS process ID of PE1, the P, and PE2
* IS-IS level of PE1, the P, and PE2
* EVPN instance name: evrf1
* RD and RT of the EVPN instance

#### Procedure

1. Enable IPv6 forwarding and configure an IPv6 address for each interface.
   
   
   
   # Configure PE1. The configurations of the P and PE2 are similar to the configuration of PE1. For detailed configurations, see Configuration Files.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname PE1
   [*HUAWEI] commit
   [~PE1] interface gigabitethernet 0/1/0
   [~PE1-GigabitEthernet0/1/0] ipv6 enable
   [*PE1-GigabitEthernet0/1/0] ipv6 address 2001:DB8:10::1 64
   [*PE1-GigabitEthernet0/1/0] quit
   [*PE1] interface LoopBack 1
   [*PE1-LoopBack1] ip address 1.1.1.1 32
   [*PE1-LoopBack1] ipv6 enable
   [*PE1-LoopBack1] ipv6 address 2001:DB8:1::1 128
   [*PE1-LoopBack1] quit
   [*PE1] commit
   ```
   
   Configure an IPv4 address for the loopback interface because the EVPN source address needs to be an IPv4 address.
2. Configure IS-IS.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] isis 1
   ```
   ```
   [*PE1-isis-1] is-level level-1
   ```
   ```
   [*PE1-isis-1] cost-style wide
   ```
   ```
   [*PE1-isis-1] network-entity 10.0000.0000.0001.00
   ```
   ```
   [*PE1-isis-1] ipv6 enable topology ipv6
   ```
   ```
   [*PE1-isis-1] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] isis ipv6 enable 1
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE1] interface loopback1
   ```
   ```
   [*PE1-LoopBack1] isis ipv6 enable 1
   ```
   ```
   [*PE1-LoopBack1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure the P.
   
   ```
   [~P] isis 1 
   ```
   ```
   [*P-isis-1] is-level level-1
   ```
   ```
   [*P-isis-1] cost-style wide
   ```
   ```
   [*P-isis-1] network-entity 10.0000.0000.0002.00
   ```
   ```
   [*P-isis-1] ipv6 enable topology ipv6
   ```
   ```
   [*P-isis-1] quit
   ```
   ```
   [*P] interface gigabitethernet 0/1/0
   ```
   ```
   [*P-GigabitEthernet0/1/0] isis ipv6 enable 1
   ```
   ```
   [*P-GigabitEthernet0/1/0] quit
   ```
   ```
   [*P] interface gigabitethernet 0/2/0
   ```
   ```
   [*P-GigabitEthernet0/2/0] isis ipv6 enable 1
   ```
   ```
   [*P-GigabitEthernet0/2/0] quit
   ```
   ```
   [*P] interface loopback1
   ```
   ```
   [*P-LoopBack1] isis ipv6 enable 1
   ```
   ```
   [*P-LoopBack1] quit
   ```
   ```
   [*P] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] isis 1
   ```
   ```
   [*PE2-isis-1] is-level level-1
   ```
   ```
   [*PE2-isis-1] cost-style wide
   ```
   ```
   [*PE2-isis-1] network-entity 10.0000.0000.0003.00
   ```
   ```
   [*PE2-isis-1] ipv6 enable topology ipv6
   ```
   ```
   [*PE2-isis-1] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] isis ipv6 enable 1
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE2] interface loopback1
   ```
   ```
   [*PE2-LoopBack1] isis ipv6 enable 1
   ```
   ```
   [*PE2-LoopBack1] quit
   ```
   ```
   [*PE2] commit
   ```
   
   
   
   After the configuration is complete, perform the following operations to check whether IS-IS is successfully configured:
   
   # Display IS-IS neighbor information. The following example uses the command output on PE1.
   
   ```
   [~PE1] display isis peer
   ```
   ```
                             Peer information for ISIS(1)
                            
     System Id     Interface         Circuit Id        State HoldTime Type     PRI
   --------------------------------------------------------------------------------
   0000.0000.0002* GE0/1/0           0000.0000.0002.01  Up   8s       L1       64 
   
   Total Peer(s): 1
   ```
3. Configure EVPN VPWS and EVPL instances on each PE and bind the EVPL instance to an access-side sub-interface. In addition, configure a VLAN on each CE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] evpn source-address 1.1.1.1
   ```
   ```
   [*PE1] evpn vpn-instance evrf1 vpws
   ```
   ```
   [*PE1-vpws-evpn-instance-evrf1] route-distinguisher 100:1
   ```
   ```
   [*PE1-vpws-evpn-instance-evrf1] vpn-target 1:1
   ```
   ```
   [*PE1-vpws-evpn-instance-evrf1] quit
   ```
   ```
   [*PE1] evpl instance 1
   ```
   ```
   [*PE1-evpl1] evpn binding vpn-instance evrf1
   ```
   ```
   [*PE1-evpl1] local-service-id 100 remote-service-id 200
   ```
   ```
   [*PE1-evpl1] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/2/0.1 mode l2
   ```
   ```
   [*PE1-GigabitEthernet 0/2/0.1] encapsulation dot1q vid 1
   ```
   ```
   [*PE1-GigabitEthernet 0/2/0.1] evpl instance 1
   ```
   ```
   [*PE1-GigabitEthernet 0/2/0.1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] evpn source-address 3.3.3.3
   ```
   ```
   [*PE2] evpn vpn-instance evrf1 vpws
   ```
   ```
   [*PE2-vpws-evpn-instance-evrf1] route-distinguisher 200:1
   ```
   ```
   [*PE2-vpws-evpn-instance-evrf1] vpn-target 1:1
   ```
   ```
   [*PE2-vpws-evpn-instance-evrf1] quit
   ```
   ```
   [*PE2] evpl instance 1
   ```
   ```
   [*PE2-evpl1] evpn binding vpn-instance evrf1
   ```
   ```
   [*PE2-evpl1] local-service-id 200 remote-service-id 100
   ```
   ```
   [*PE2-evpl1] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/2/0.1 mode l2
   ```
   ```
   [*PE2-GigabitEthernet 0/2/0.1] encapsulation dot1q vid 1
   ```
   ```
   [*PE2-GigabitEthernet 0/2/0.1] evpl instance 1
   ```
   ```
   [*PE2-GigabitEthernet 0/2/0.1] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure CE1.
   
   ```
   <CE1> system-view
   [~CE1] vlan 1 
   [*CE1-vlan1] quit           
   [*CE1] interface gigabitethernet 0/1/0
   [*CE1-GigabitEthernet0/1/0] portswitch
   [*CE1-GigabitEthernet0/1/0] undo shutdown
   [*CE1-GigabitEthernet0/1/0] port link-type trunk
   [*CE1-GigabitEthernet0/1/0] port trunk allow-pass vlan 1
   [*CE1-GigabitEthernet0/1/0] commit
   [~CE1-GigabitEthernet0/1/0] quit
   ```
   
   # Configure CE2.
   
   ```
   <CE2> system-view
   [~CE2] vlan 1
   [*CE2-vlan1] quit           
   [*CE2] interface gigabitethernet 0/1/0
   [*CE2-GigabitEthernet0/1/0] portswitch
   [*CE2-GigabitEthernet0/1/0] undo shutdown
   [*CE2-GigabitEthernet0/1/0] port link-type trunk
   [*CE2-GigabitEthernet0/1/0] port trunk allow-pass vlan 1
   [*CE2-GigabitEthernet0/1/0] commit
   [~CE2-GigabitEthernet0/1/0] quit
   ```
4. Establish a BGP EVPN peer relationship between PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [*PE1-bgp] router-id 1.1.1.1
   ```
   ```
   [*PE1-bgp] peer 2001:DB8:3::3 as-number 100
   ```
   ```
   [*PE1-bgp] peer 2001:DB8:3::3 connect-interface loopback 1
   ```
   ```
   [*PE1-bgp] l2vpn-family evpn
   ```
   ```
   [*PE1-bgp-af-evpn] peer 2001:DB8:3::3 enable
   ```
   ```
   [*PE1-bgp-af-evpn] quit
   ```
   ```
   [*PE1-bgp] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 100
   ```
   ```
   [*PE2-bgp] router-id 3.3.3.3
   ```
   ```
   [*PE2-bgp] peer 2001:DB8:1::1 as-number 100
   ```
   ```
   [*PE2-bgp] peer 2001:DB8:1::1 connect-interface loopback 1
   ```
   ```
   [*PE2-bgp] l2vpn-family evpn
   ```
   ```
   [*PE2-bgp-af-evpn] peer 2001:DB8:1::1 enable
   ```
   ```
   [*PE2-bgp-af-evpn] quit
   ```
   ```
   [*PE2-bgp] quit
   ```
   ```
   [*PE2] commit
   ```
   
   After the configuration is complete, run the **display bgp evpn peer** command on the PEs and check whether BGP EVPN peer relationships have been established between the PEs. If the **Established** state is displayed in the command output, the BGP EVPN peer relationships have been established successfully.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display bgp evpn peer
   
    BGP local router ID : 1.1.1.1
    Local AS number : 100
    Total number of peers : 1                 Peers in established state : 1
   
     Peer                             V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     2001:DB8:3::3                    4         100       40       40     0 00:30:41 Established        2
   ```
5. Configure SRv6 SIDs, and configure the PEs to carry SIDs in VPN routes.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] segment-routing ipv6
   ```
   ```
   [*PE1-segment-routing-ipv6] encapsulation source-address 2001:DB8:1::1
   ```
   ```
   [*PE1-segment-routing-ipv6] locator PE1 ipv6-prefix 2001:DB8:100:: 64 static 32
   ```
   ```
   [*PE1-segment-routing-ipv6-locator] opcode ::10 end psp
   ```
   ```
   [*PE1-segment-routing-ipv6-locator] quit
   ```
   ```
   [*PE1-segment-routing-ipv6] quit
   ```
   ```
   [*PE1] bgp 100
   ```
   ```
   [*PE1-bgp] l2vpn-family evpn
   ```
   ```
   [*PE1-bgp-af-evpn] peer 2001:DB8:3::3 advertise encap-type srv6
   ```
   ```
   [*PE1-bgp-af-evpn] quit
   ```
   ```
   [*PE1-bgp] quit
   ```
   ```
   [*PE1] evpl instance 1
   ```
   ```
   [*PE1-evpl1] segment-routing ipv6 locator PE1
   ```
   ```
   [*PE1-evpl1] quit
   ```
   ```
   [*PE1] evpn vpn-instance evrf1 vpws
   ```
   ```
   [*PE1-vpws-evpn-instance-evrf1] segment-routing ipv6 traffic-engineer best-effort
   ```
   ```
   [*PE1-vpws-evpn-instance-evrf1] quit
   ```
   ```
   [*PE1] commit
   ```
   ```
   [~PE1] isis 1
   ```
   ```
   [~PE1-isis-1] segment-routing ipv6 locator PE1 auto-sid-disable
   ```
   ```
   [*PE1-isis-1] commit
   ```
   ```
   [~PE1-isis-1] quit
   ```
   
   # Configure the P.
   
   ```
   [~P] segment-routing ipv6
   ```
   ```
   [*P-segment-routing-ipv6] encapsulation source-address 2001:DB8:2::2
   ```
   ```
   [*P-segment-routing-ipv6] locator P ipv6-prefix 2001:DB8:120:: 64 static 32
   ```
   ```
   [*P-segment-routing-ipv6-locator] opcode ::20 end psp
   ```
   ```
   [*P-segment-routing-ipv6-locator] quit
   ```
   ```
   [*P-segment-routing-ipv6] quit
   ```
   ```
   [~P] isis 1
   ```
   ```
   [~P-isis-1] segment-routing ipv6 locator P auto-sid-disable
   ```
   ```
   [*P-isis-1] commit
   ```
   ```
   [~P-isis-1] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] segment-routing ipv6
   ```
   ```
   [*PE2-segment-routing-ipv6] encapsulation source-address 2001:DB8:3::3
   ```
   ```
   [*PE2-segment-routing-ipv6] locator PE2 ipv6-prefix 2001:DB8:130:: 64 static 32
   ```
   ```
   [*PE2-segment-routing-ipv6-locator] opcode ::30 end psp
   ```
   ```
   [*PE2-segment-routing-ipv6-locator] quit
   ```
   ```
   [*PE2-segment-routing-ipv6] quit
   ```
   ```
   [*PE2] bgp 100
   ```
   ```
   [*PE2-bgp] l2vpn-family evpn
   ```
   ```
   [*PE2-bgp-af-evpn] peer 2001:DB8:1::1 advertise encap-type srv6
   ```
   ```
   [*PE2-bgp-af-evpn] quit
   ```
   ```
   [*PE2-bgp] quit
   ```
   ```
   [*PE2] evpl instance 1
   ```
   ```
   [*PE2-evpl1] segment-routing ipv6 locator PE2
   ```
   ```
   [*PE2-evpl1] quit
   ```
   ```
   [*PE2] evpn vpn-instance evrf1 vpws
   ```
   ```
   [*PE2-vpws-evpn-instance-evrf1] segment-routing ipv6 traffic-engineer best-effort
   ```
   ```
   [*PE2-vpws-evpn-instance-evrf1] quit
   ```
   ```
   [*PE2] commit
   ```
   ```
   [~PE2] isis 1
   ```
   ```
   [~PE2-isis-1] segment-routing ipv6 locator PE2 auto-sid-disable
   ```
   ```
   [*PE2-isis-1] commit
   ```
   ```
   [~PE2-isis-1] quit
   ```
   
   Run the [**display segment-routing ipv6 local-sid**](cmdqueryname=display+segment-routing+ipv6+local-sid) **end** **forwarding** command to check information about the SRv6 local SID table.
   
   ```
   [~PE1] display segment-routing ipv6 local-sid end forwarding
                       My Local-SID End Forwarding Table
                       ---------------------------------
   
   SID         : 2001:DB8:100::10/128                         FuncType    : End
   Flavor      : PSP                                          SidCompress : NO
   LocatorName : PE1                                          LocatorID   : 1
   ProtocolType: STATIC                                       ProcessID   : --
   UpdateTime  : 2021-08-30 01:46:05.713
   
   Total SID(s): 1
   ```
   ```
   [~PE2] display segment-routing ipv6 local-sid end forwarding
                       My Local-SID End Forwarding Table
                       ---------------------------------
   
   SID         : 2001:DB8:130::30/128                         FuncType    : End
   Flavor      : PSP                                          SidCompress : NO
   LocatorName : PE2                                          LocatorID   : 1
   ProtocolType: STATIC                                       ProcessID   : --
   UpdateTime  : 2021-08-30 01:47:26.426
   
   Total SID(s): 1
   ```
   ```
   [~P] display segment-routing ipv6 local-sid end forwarding
                       My Local-SID End Forwarding Table
                       ---------------------------------
   
   SID         : 2001:DB8:120::20/128                         FuncType    : End
   Flavor      : PSP                                          SidCompress : NO
   LocatorName : P                                            LocatorID   : 1
   ProtocolType: STATIC                                       ProcessID   : --
   UpdateTime  : 2021-08-30 01:49:44.292
   
   Total SID(s): 1
   ```
6. Configure an SRv6 TE Policy.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] segment-routing ipv6 
   [*PE1-segment-routing-ipv6] segment-list list1 
   [*PE1-segment-routing-ipv6-segment-list-list1] index 5 sid ipv6 2001:DB8:120::20
   [*PE1-segment-routing-ipv6-segment-list-list1] index 10 sid ipv6 2001:DB8:130::30
   [*PE1-segment-routing-ipv6-segment-list-list1] commit
   [~PE1-segment-routing-ipv6-segment-list-list1] quit
   [~PE1-segment-routing-ipv6] srv6-te-policy locator PE1 
   [*PE1-segment-routing-ipv6] srv6-te policy policy1 endpoint 2001:DB8:3::3 color 101
   [*PE1-segment-routing-ipv6-policy-policy1] binding-sid 2001:DB8:100::450
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
   [*PE2-segment-routing-ipv6] segment-list list1 
   [*PE2-segment-routing-ipv6-segment-list-list1] index 5 sid ipv6 2001:DB8:120::20
   [*PE2-segment-routing-ipv6-segment-list-list1] index 10 sid ipv6 2001:DB8:100::10
   [*PE2-segment-routing-ipv6-segment-list-list1] commit
   [~PE2-segment-routing-ipv6-segment-list-list1] quit
   [~PE2-segment-routing-ipv6] srv6-te-policy locator PE2 
   [*PE2-segment-routing-ipv6] srv6-te policy policy1 endpoint 2001:DB8:1::1 color 101
   [*PE2-segment-routing-ipv6-policy-policy1] binding-sid 2001:DB8:130::350
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
   Color                   : 101                            Endpoint             : 2001:DB8:3::3
   TunnelId                : 1                              
   TunnelType              : SRv6-TE Policy                 DelayTimerRemain     : -            
   Policy State            : Up                             State Change Time    : 2020-03-03 02:32:11
   Admin State             : Up                             Traffic Statistics   : Disable  
   Backup Hot-Standby      : Disable                        BFD                  : Disable	
   Interface Index         : -                              Interface Name       : - 
   Interface State         : -                              Encapsulation Mode   : Insert
   Binding SID             : 2001:DB8:100::450(Insert, Preferred)
   Candidate-path Count    : 1 
   
    Candidate-path Preference : 100
    Path State             : Active                         Path Type            : Primary
    Protocol-Origin        : Configuration(30)              Originator           : 0, 0.0.0.0
    Discriminator          : 100                            Binding SID          : 2001:DB8:100::450
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
            2001:DB8:120::20
            2001:DB8:130::30
   ```
7. Configure a tunnel policy to import VPN traffic.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] route-policy p1 permit node 10
   [*PE1-route-policy] apply extcommunity color 0:101
   [*PE1-route-policy] quit
   [*PE1] bgp 100
   [*PE1-bgp] l2vpn-family evpn
   [*PE1-bgp-af-evpn] peer 2001:DB8:3::3 route-policy p1 import 
   [*PE1-bgp-af-evpn] quit
   [*PE1-bgp] quit
   [*PE1] tunnel-policy p1
   [*PE1-tunnel-policy-p1] tunnel select-seq ipv6 srv6-te-policy load-balance-number 1
   [*PE1-tunnel-policy-p1] quit
   [*PE1] evpn vpn-instance evrf1 vpws
   [*PE1-vpws-evpn-instance-evrf] tnl-policy p1
   [*PE1-vpws-evpn-instance-evrf] commit
   [~PE1-vpws-evpn-instance-evrf] quit
   ```
   
   
   
   # Configure PE2.
   
   ```
   [~PE2] route-policy p1 permit node 10
   [*PE2-route-policy] apply extcommunity color 0:101
   [*PE2-route-policy] quit
   [*PE2] bgp 100
   [*PE2-bgp] l2vpn-family evpn
   [*PE2-bgp-af-evpn] peer 2001:DB8:1::1 route-policy p1 import 
   [*PE2-bgp-af-evpn] quit
   [*PE2-bgp] quit
   [*PE2] tunnel-policy p1
   [*PE2-tunnel-policy-p1] tunnel select-seq ipv6 srv6-te-policy load-balance-number 1
   [*PE2-tunnel-policy-p1] quit
   [*PE2] evpn vpn-instance evrf1 vpws
   [*PE2-vpws-evpn-instance-evrf] tnl-policy p1
   [*PE2-vpws-evpn-instance-evrf] commit
   [~PE2-vpws-evpn-instance-evrf] quit
   ```
8. Verify the configuration.
   
   
   
   Run the **display bgp evpn evpl** command on each PE. The command output shows the EVPL status.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display bgp evpn evpl
   Total EVPLs: 1      1 Up     0 Down
   
   EVPL ID : 1
   State : up
   EVPL Down Causes : --
   Evpl Type : none
   Interface : GigabitEthernet0/2/0.1
   Interface Status : up
   Ignore AcState : disable
   Local MTU : 1500
   Local Control Word : false
   Local Redundancy Mode : all-active
   Local DF State : primary
   Local ESI : 0000.0000.0000.0000.0000
   Remote Redundancy Mode : all-active
   Remote Primary DF Number : 1
   Remote Backup DF Number : 0
   Remote None DF Number : 0
   Peer IP : 2001:DB8:3::3
    Origin Nexthop IP : 2001:DB8:3::3
    DF State : primary
    Eline Role : primary
    Remote MTU : 1500
    Remote Control Word : false
    Remote ESI : 0000.0000.0000.0000.0000
    Tunnel info : 1 tunnels
     NO.0   Tunnel Type : srv6te-policy, Tunnel ID : 0x000000003400000001
   Last Interface UP Timestamp : 2019-8-14 3:21:34:196
   Last Designated Primary Timestamp : 2019-8-14 3:23:45:839
   Last Designated Backup Timestamp : --
   Last EVPL UP Timestamp: --
   Last EVPL DOWN Timestamp: --
   ```
   
   Run the **display bgp evpn all routing-table** command on each PE. The command output shows the EVPN route sent from the peer end.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display bgp evpn all routing-table
   
    Local AS number : 100
   
    BGP Local router ID is 1.1.1.1
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
   
   
    EVPN address family:
    Number of A-D Routes: 2
    Route Distinguisher: 100:1
          Network(ESI/EthTagId)                                  NextHop
    *>    0000.0000.0000.0000.0000:100                           127.0.0.1                                    
    *>i   0000.0000.0000.0000.0000:200                           2001:DB8:3::3                                
   
   
    EVPN-Instance evrf1:
    Number of A-D Routes: 2
          Network(ESI/EthTagId)                                  NextHop
    *>    0000.0000.0000.0000.0000:100                           127.0.0.1                                    
    *>i   0000.0000.0000.0000.0000:200                           2001:DB8:3::3
   ```
   
   Run the **display bgp evpn all routing-table ad-route** command on PE1. The command output shows the A-D EVPN routes sent from the peer end.
   
   ```
   [~PE1] display bgp evpn all routing-table ad-route 0000.0000.0000.0000.0000:200 
   
    BGP local router ID : 1.1.1.1                  
    Local AS number : 100                          
    Total routes of Route Distinguisher(100:1): 1  
    BGP routing table entry information of 0000.0000.0000.0000.0000:200:           
    Label information (Received/Applied): 3/NULL   
    From: 2001:DB8:3::3 (3.3.3.3)                  
    Route Duration: 0d00h14m45s                    
    Relay IP Nexthop: FE80::3AC2:67FF:FE31:307     
    Relay IP Out-Interface:GigabitEthernet0/1/0           
    Relay Tunnel Out-Interface:                    
    Original nexthop: 2001:DB8:3::3                
    Qos information : 0x0                          
    Ext-Community: RT <1 : 1>, SoO <3.3.3.3 : 0>, Color <0 : 101>, EVPN L2 Attributes <MTU:1500 C:0 P:1 B:0>                                              
    Prefix-sid: 2001:DB8:130::1:0:5A, Endpoint Behavior: DX2(21)               
    AS-path Nil, origin incomplete, localpref 100, pref-val 0, valid, internal, best, select, pre 255, IGP cost 20                     
    Route Type: 1 (Ethernet Auto-Discovery (A-D) route)    
    ESI: 0000.0000.0000.0000.0000, Ethernet Tag ID: 200             
    Not advertised to any peer yet 
   
   
   
    EVPN-Instance evrf1:                           
    Number of A-D Routes: 1                        
    BGP routing table entry information of 0000.0000.0000.0000.0000:200:           
    Route Distinguisher: 100:1                     
    Remote-Cross route                             
    Label information (Received/Applied): 3/NULL   
    From: 2001:DB8:3::3 (3.3.3.3)                  
    Route Duration: 0d00h02m41s                    
    Relay Tunnel Out-Interface: policy1(srv6tepolicy)                    
    Original nexthop: 2001:DB8:3::3                
    Qos information : 0x0                          
    Ext-Community: RT <1 : 1>, SoO <3.3.3.3 : 0>, Color <0 : 101>, EVPN L2 Attributes <MTU:1500 C:0 P:1 B:0>                                              
    Prefix-sid: 2001:DB8:130::1:0:5A, Endpoint Behavior: DX2(21)               
    AS-path Nil, origin incomplete, localpref 100, pref-val 0, valid, internal, best, select, pre 255                                  
    Route Type: 1 (Ethernet Auto-Discovery (A-D) route)
    ESI: 0000.0000.0000.0000.0000, Ethernet Tag ID: 200      
    Not advertised to any peer yet
   ```

#### Configuration Files

* PE1 configuration file
  
  ```
  sysname PE1
  #               
  evpn vpn-instance evrf1 vpws
   route-distinguisher 100:1
   segment-routing ipv6 traffic-engineer best-effort
   tnl-policy p1  
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #               
  evpl instance 1
   evpn binding vpn-instance evrf1
   local-service-id 100 remote-service-id 200
   segment-routing ipv6 locator PE1
  #               
  segment-routing ipv6
   encapsulation source-address 2001:DB8:1::1
   locator PE1 ipv6-prefix 2001:DB8:100:: 64 static 32
    opcode ::10 end psp
   srv6-te-policy locator PE1
   segment-list list1
    index 5 sid ipv6 2001:DB8:120::20
    index 10 sid ipv6 2001:DB8:130::30
   srv6-te policy policy1 endpoint 2001:DB8:3::3 color 101
    binding-sid 2001:DB8:100::450
    candidate-path preference 100
     segment-list list1 
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0001.00
   #              
   ipv6 enable topology ipv6
   segment-routing ipv6 locator PE1 auto-sid-disable
   #              
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
  #               
  interface GigabitEthernet0/2/0.1 mode l2
   encapsulation dot1q vid 1
   evpl instance 1
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:10::1/64
   isis ipv6 enable 1
  #               
  interface LoopBack1
   ipv6 enable   
   ip address 1.1.1.1 255.255.255.255 
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
   l2vpn-family evpn
    policy vpn-target
    peer 2001:DB8:3::3 enable
    peer 2001:DB8:3::3 route-policy p1 import
    peer 2001:DB8:3::3 advertise encap-type srv6
  #               
  route-policy p1 permit node 10
   apply extcommunity color 0:101
  #               
  tunnel-policy p1
   tunnel select-seq ipv6 srv6-te-policy load-balance-number 1
  #
  evpn source-address 1.1.1.1
  #              
  return
  ```
* P configuration file
  
  ```
  sysname P
  #               
  segment-routing ipv6
   encapsulation source-address 2001:DB8:2::2
   locator P ipv6-prefix 2001:DB8:120:: 64 static 32
    opcode ::20 end psp
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0002.00
   #              
   ipv6 enable topology ipv6
   segment-routing ipv6 locator P auto-sid-disable
   #              
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:20::1/64
   isis ipv6 enable 1
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:10::2/64
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
  sysname PE2
  #               
  evpn vpn-instance evrf1 vpws
   route-distinguisher 200:1
   segment-routing ipv6 traffic-engineer best-effort
   tnl-policy p1  
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #               
  evpl instance 1
   evpn binding vpn-instance evrf1
   local-service-id 200 remote-service-id 100
   segment-routing ipv6 locator PE2
  #               
  segment-routing ipv6
   encapsulation source-address 2001:DB8:3::3
   locator PE2 ipv6-prefix 2001:DB8:130:: 64 static 32
    opcode ::30 end psp
   srv6-te-policy locator PE2
   segment-list list1
    index 5 sid ipv6 2001:DB8:120::20
    index 10 sid ipv6 2001:DB8:100::10
   srv6-te policy policy1 endpoint 2001:DB8:1::1 color 101
    binding-sid 2001:DB8:130::350
    candidate-path preference 100
     segment-list list1 
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0003.00
   #              
   ipv6 enable topology ipv6
   segment-routing ipv6 locator PE2 auto-sid-disable
   #              
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
  #               
  interface GigabitEthernet0/2/0.1 mode l2
   encapsulation dot1q vid 1
   evpl instance 1
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:20::2/64
   isis ipv6 enable 1
  #               
  interface LoopBack1
   ipv6 enable
   ip address 3.3.3.3 255.255.255.255    
   ipv6 address 2001:DB8:3::3/128
   isis ipv6 enable 1
  #               
  bgp 100         
   router-id 3.3.3.3
   peer 2001:DB8:1::1 as-number 100
   peer 2001:DB8:1::1 connect-interface LoopBack1
   #              
   ipv4-family unicast
    undo synchronization
   #              
   l2vpn-family evpn
    policy vpn-target
    peer 2001:DB8:1::1 enable
    peer 2001:DB8:1::1 route-policy p1 import
    peer 2001:DB8:1::1 advertise encap-type srv6
  #               
  route-policy p1 permit node 10
   apply extcommunity color 0:101
  #               
  tunnel-policy p1
   tunnel select-seq ipv6 srv6-te-policy load-balance-number 1
  #
  evpn source-address 3.3.3.3
  #               
  return
  ```
* CE1 configuration file
  
  ```
  sysname CE1
  #   
  vlan batch 1 
  #           
  interface GigabitEthernet0/1/0
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 1
  # 
  return 
  ```
* CE2 configuration file
  
  ```
  sysname CE2
  #   
  vlan batch 1 
  #               
  interface GigabitEthernet0/1/0
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 1
  #               
  return
  ```