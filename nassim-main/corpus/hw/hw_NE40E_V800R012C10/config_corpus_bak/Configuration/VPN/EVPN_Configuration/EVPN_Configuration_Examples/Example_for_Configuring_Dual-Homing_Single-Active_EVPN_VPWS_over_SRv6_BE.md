Example for Configuring Dual-Homing Single-Active EVPN VPWS over SRv6 BE
========================================================================

This section provides an example for configuring SRv6 BE to carry EVPN VPWSs. In the example, a redundancy mode needs to be configured on a per Ethernet segment identifier (ESI) basis.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001155020362__en-us_task_0227779374_fig_dc_vrp_srv6_cfg_all_002201), CE2 is dual-homed to PE2 and PE3. It is required that PE2 and PE3 operate in master/backup mode to transmit traffic from CE1 to CE2.

To meet this requirement, configure the single-active redundancy mode on a per ESI basis for PE2 and PE3.

**Figure 1** EVPN VPWS over SRv6 BE networking (CE dual-homing in single-active mode)![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/1/0, GE 0/2/0, and GE 0/3/0, respectively.


  
![](figure/en-us_image_0227779375.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable IPv6 forwarding and configure an IPv6 address for each PE interface.
2. Enable IS-IS, configure an IS-IS level, and specify a network entity on each PE.
3. Configure EVPN VPWS and EVPL instances on each PE.
4. Establish BGP EVPN peer relationships among the PEs.
5. Configure SRv6 BE on the PEs.
6. Bind the EVPL instance on each PE to an access-side sub-interface.
7. Configure a redundancy mode on a per ESI basis on PE2 and PE3.
8. Configure CE access to the PEs.

#### Data Preparation

To complete the configuration, you need the following data:

* EVPN instance name: evrf1
* RD and RT of the EVPN instance
* Locator names for PE1, PE2, and PE3: PE1, PE2, and PE3, respectively; dynamically generated operation code (opcode)

#### Procedure

1. Enable IPv6 forwarding and configure an IPv6 address for each interface.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname PE1
   [*HUAWEI] commit
   [~PE1] interface gigabitethernet 0/1/0
   [~PE1-GigabitEthernet0/1/0] ipv6 enable
   [*PE1-GigabitEthernet0/1/0] ipv6 address 2001:DB8:10::1 64
   [*PE1-GigabitEthernet0/1/0] quit
   [*PE1] interface gigabitethernet 0/2/0
   [*PE1-GigabitEthernet0/2/0] ipv6 enable
   [*PE1-GigabitEthernet0/2/0] ipv6 address 2001:DB8:20::1 64
   [*PE1-GigabitEthernet0/2/0] quit
   [*PE1] interface LoopBack 1
   [*PE1-LoopBack1] ip address 1.1.1.1 32
   [*PE1-LoopBack1] ipv6 enable
   [*PE1-LoopBack1] ipv6 address 2001:DB8:1::1 128
   [*PE1-LoopBack1] quit
   [*PE1] commit
   ```
   
   Configure an IPv4 address for the loopback interface because the EVPN source address needs to be an IPv4 address. The preceding example uses the configuration of PE1. The configurations of other devices are similar to the configuration of PE1. For configuration details, see [Configuration Files](dc_vrp_srv6_cfg_all_0234.html#EN-US_TASK_0227779374__section_dc_vrp_srv6_cfg_all_002205) in this section.
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
   [*PE1] interface gigabitethernet 0/2/0
   [*PE1-GigabitEthernet0/2/0] isis ipv6 enable 1
   [*PE1-GigabitEthernet0/2/0] quit
   [*PE1] interface loopback1
   [*PE1-LoopBack1] isis ipv6 enable 1
   [*PE1-LoopBack1] commit
   [~PE1-LoopBack1] quit
   ```
   
   
   
   # Configure PE2.
   
   ```
   [~PE2] isis 1
   [*PE2-isis-1] is-level level-1
   [*PE2-isis-1] cost-style wide
   [*PE2-isis-1] network-entity 10.0000.0000.0002.00
   [*PE2-isis-1] ipv6 enable topology ipv6
   [*PE2-isis-1] quit
   [*PE2] interface gigabitethernet 0/1/0
   [*PE2-GigabitEthernet0/1/0] isis ipv6 enable 1
   [*PE2-GigabitEthernet0/1/0] quit
   [*PE2] interface gigabitethernet 0/2/0
   [*PE2-GigabitEthernet0/2/0] isis ipv6 enable 1
   [*PE2-GigabitEthernet0/2/0] quit
   [*PE2] interface loopback1
   [*PE2-LoopBack1] isis ipv6 enable 1
   [*PE2-LoopBack1] commit
   [~PE2-LoopBack1] quit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] isis 1
   [*PE3-isis-1] is-level level-1
   [*PE3-isis-1] cost-style wide
   [*PE3-isis-1] network-entity 10.0000.0000.0003.00
   [*PE3-isis-1] ipv6 enable topology ipv6
   [*PE3-isis-1] quit
   [*PE3] interface gigabitethernet 0/1/0
   [*PE3-GigabitEthernet0/1/0] isis ipv6 enable 1
   [*PE3-GigabitEthernet0/1/0] quit
   [*PE3] interface gigabitethernet 0/2/0
   [*PE3-GigabitEthernet0/2/0] isis ipv6 enable 1
   [*PE3-GigabitEthernet0/2/0] quit
   [*PE3] interface loopback1
   [*PE3-LoopBack1] isis ipv6 enable 1
   [*PE3-LoopBack1] commit
   [~PE3-LoopBack1] quit
   ```
   
   After the configuration is complete, run the **display isis peer** and **display isis route** commands to check whether IS-IS has been configured successfully. The following example uses the command output on PE1.
   
   ```
   [~PE1] display isis peer
                             Peer information for ISIS(1)  
   
     System Id     Interface          Circuit Id        State HoldTime Type     PRI
   --------------------------------------------------------------------------------
   0000.0000.0003* GE0/2/0            0000.0000.0003.02  Up   8s       L1       64 
   0000.0000.0002* GE0/1/0            0000.0000.0002.02  Up   6s       L1       64 
   
   Total Peer(s): 2 
   ```
3. Configure EVPN VPWS and EVPL instances on each PE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] evpn source-address 1.1.1.1
   [*PE1] evpn vpn-instance evrf1 vpws
   [*PE1-vpws-evpn-instance-evrf1] route-distinguisher 100:1
   [*PE1-vpws-evpn-instance-evrf1] vpn-target 1:1
   [*PE1-vpws-evpn-instance-evrf1] quit
   [*PE1] evpl instance 1
   [*PE1-evpl1] evpn binding vpn-instance evrf1
   [*PE1-evpl1] local-service-id 100 remote-service-id 200
   [*PE1-evpl1] quit
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] evpn source-address 2.2.2.2
   [*PE2] evpn vpn-instance evrf1 vpws
   [*PE2-vpws-evpn-instance-evrf1] route-distinguisher 200:1
   [*PE2-vpws-evpn-instance-evrf1] vpn-target 1:1
   [*PE2-vpws-evpn-instance-evrf1] quit
   [*PE2] evpl instance 1
   [*PE2-evpl1] evpn binding vpn-instance evrf1
   [*PE2-evpl1] local-service-id 200 remote-service-id 100
   [*PE2-evpl1] quit
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] evpn source-address 3.3.3.3
   [*PE3] evpn vpn-instance evrf1 vpws
   [*PE3-vpws-evpn-instance-evrf1] route-distinguisher 300:1
   [*PE3-vpws-evpn-instance-evrf1] vpn-target 1:1
   [*PE3-vpws-evpn-instance-evrf1] quit
   [*PE3] evpl instance 1
   [*PE3-evpl1] evpn binding vpn-instance evrf1
   [*PE3-evpl1] local-service-id 200 remote-service-id 100
   [*PE3-evpl1] quit
   [*PE3] commit
   ```
4. Establish BGP EVPN peer relationships among the PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   [*PE1-bgp] router-id 1.1.1.1
   [*PE1-bgp] peer 2001:DB8:3::3 as-number 100
   [*PE1-bgp] peer 2001:DB8:3::3 connect-interface loopback 1
   [*PE1-bgp] peer 2001:DB8:2::2 as-number 100
   [*PE1-bgp] peer 2001:DB8:2::2 connect-interface loopback 1
   [*PE1-bgp] l2vpn-family evpn
   [*PE1-bgp-af-evpn] peer 2001:DB8:3::3 enable
   [*PE1-bgp-af-evpn] peer 2001:DB8:3::3 advertise encap-type srv6
   [*PE1-bgp-af-evpn] peer 2001:DB8:2::2 enable
   [*PE1-bgp-af-evpn] peer 2001:DB8:2::2 advertise encap-type srv6
   [*PE1-bgp-af-evpn] quit
   [*PE1-bgp] quit
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 100
   [*PE2-bgp] router-id 2.2.2.2
   [*PE2-bgp] peer 2001:DB8:1::1 as-number 100
   [*PE2-bgp] peer 2001:DB8:1::1 connect-interface loopback 1
   [*PE2-bgp] peer 2001:DB8:3::3 as-number 100
   [*PE2-bgp] peer 2001:DB8:3::3 connect-interface loopback 1
   [*PE2-bgp] l2vpn-family evpn
   [*PE2-bgp-af-evpn] peer 2001:DB8:1::1 enable
   [*PE2-bgp-af-evpn] peer 2001:DB8:1::1 advertise encap-type srv6
   [*PE2-bgp-af-evpn] peer 2001:DB8:3::3 enable
   [*PE2-bgp-af-evpn] peer 2001:DB8:3::3 advertise encap-type srv6
   [*PE2-bgp-af-evpn] quit
   [*PE2-bgp] quit
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] bgp 100
   [*PE3-bgp] router-id 3.3.3.3
   [*PE3-bgp] peer 2001:DB8:1::1 as-number 100
   [*PE3-bgp] peer 2001:DB8:1::1 connect-interface loopback 1
   [*PE3-bgp] peer 2001:DB8:2::2 as-number 100
   [*PE3-bgp] peer 2001:DB8:2::2 connect-interface loopback 1
   [*PE3-bgp] l2vpn-family evpn
   [*PE3-bgp-af-evpn] peer 2001:DB8:1::1 enable
   [*PE3-bgp-af-evpn] peer 2001:DB8:1::1 advertise encap-type srv6
   [*PE3-bgp-af-evpn] peer 2001:DB8:2::2 enable
   [*PE3-bgp-af-evpn] peer 2001:DB8:2::2 advertise encap-type srv6
   [*PE3-bgp-af-evpn] quit
   [*PE3-bgp] quit
   [*PE3] commit
   ```
   
   After the configuration is complete, run the **display bgp evpn peer** command on the PEs to check whether the BGP EVPN peer relationships have been established. If the **Established** state is displayed in the command output, the BGP EVPN peer relationships have been established successfully.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display bgp evpn peer  
   
    BGP local router ID : 1.1.1.1                          
    Local AS number : 100                                  
    Total number of peers : 2                 Peers in established state : 2       
   
     Peer                             V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv                              
     2001:DB8:2::2                    4         100      113      111     0 01:32:39 Established        2                              
     2001:DB8:3::3                    4         100      125      122     0 01:43:29 Established        2 
   ```
5. Configure SRv6 BE on the PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] segment-routing ipv6
   [*PE1-segment-routing-ipv6] encapsulation source-address 2001:DB8:1::1
   [*PE1-segment-routing-ipv6] locator PE1 ipv6-prefix 2001:DB8:11:: 64 static 32
   [*PE1-segment-routing-ipv6-locator] quit
   [*PE1-segment-routing-ipv6] quit
   [*PE1] isis 1
   [*PE1-isis-1] segment-routing ipv6 locator PE1
   [*PE1-isis-1] quit
   [*PE1] evpl instance 1
   [*PE1-evpl1] segment-routing ipv6 locator PE1
   [*PE1-evpl1] quit
   [*PE1] evpn vpn-instance evrf1 vpws
   [*PE1-vpws-evpn-instance-evrf1] segment-routing ipv6 best-effort
   [*PE1-vpws-evpn-instance-evrf1] quit
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] segment-routing ipv6
   [*PE2-segment-routing-ipv6] encapsulation source-address 2001:DB8:2::2
   [*PE2-segment-routing-ipv6] locator PE2 ipv6-prefix 2001:DB8:21:: 64 static 32
   [*PE2-segment-routing-ipv6-locator] quit
   [*PE2-segment-routing-ipv6] quit
   [*PE2] isis 1
   [*PE2-isis-1] segment-routing ipv6 locator PE2
   [*PE2-isis-1] quit
   [*PE2] evpl instance 1
   [*PE2-evpl1] segment-routing ipv6 locator PE2
   [*PE2-evpl1] quit
   [*PE2] evpn vpn-instance evrf1 vpws
   [*PE2-vpws-evpn-instance-evrf1] segment-routing ipv6 best-effort
   [*PE2-vpws-evpn-instance-evrf1] quit
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] segment-routing ipv6
   [*PE3-segment-routing-ipv6] encapsulation source-address 2001:DB8:3::3
   [*PE3-segment-routing-ipv6] locator PE3 ipv6-prefix 2001:DB8:31:: 64 static 32
   [*PE3-segment-routing-ipv6-locator] quit
   [*PE3-segment-routing-ipv6] quit
   [*PE3] isis 1
   [*PE3-isis-1] segment-routing ipv6 locator PE3
   [*PE3-isis-1] quit
   [*PE3] evpl instance 1
   [*PE3-evpl1] segment-routing ipv6 locator PE3
   [*PE3-evpl1] quit
   [*PE3] evpn vpn-instance evrf1 vpws
   [*PE3-vpws-evpn-instance-evrf1] segment-routing ipv6 best-effort
   [*PE3-vpws-evpn-instance-evrf1] quit
   [*PE3] commit
   ```
   
   After the configuration is complete, run the **display segment-routing ipv6 local-sid** **end-dx2** **forwarding** command on the PEs to check SRv6 BE local SID tables. The following example uses the command output on PE1.
   
   ```
   [~PE1] display segment-routing ipv6 local-sid end-dx2 forwarding
                      My Local-SID End.DX2 Forwarding Table
                       -------------------------------------                       
   
   SID        : 2001:DB8:11::1:0:20/128                      FuncType : End.DX2    
   EVPL ID    : 1                                          
   LocatorName: PE1                                          LocatorID: 1          
   Flavor     : NO-FLAVOR                                    SidCompress : NO
   UpdateTime : 2023-05-10 01:46:05.713
   
   Total SID(s): 1  
   ```
6. Bind the EVPL instance on each PE to an access-side sub-interface.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] interface gigabitethernet 0/3/0.1 mode l2
   [*PE1-GigabitEthernet0/3/0.1] encapsulation dot1q vid 10
   [*PE1-GigabitEthernet0/3/0.1] evpl instance 1
   [*PE1-GigabitEthernet0/3/0.1] quit
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] lacp e-trunk system-id 00e0-fc00-0000
   [*PE2] lacp e-trunk priority 10
   [*PE2] e-trunk 1
   [*PE2-e-trunk-1] priority 10
   [*PE2-e-trunk-1] peer-ipv6 2001:DB8:3::3 source-ipv6 2001:DB8:2::2
   [*PE2-e-trunk-1] security-key cipher YsHsjx_202206
   [*PE2-e-trunk-1] quit
   [*PE2] interface eth-trunk 10
   [*PE2-Eth-Trunk10] mode lacp-static
   [*PE2-Eth-Trunk10] e-trunk 1
   [*PE2-Eth-Trunk10] quit
   [*PE2] interface eth-trunk 10.1 mode l2
   [*PE2-Eth-Trunk10.1] encapsulation dot1q vid 10
   [*PE2-Eth-Trunk10.1] evpl instance 1
   [*PE2-Eth-Trunk10.1] quit
   [*PE2] interface gigabitethernet 0/3/0
   [*PE2-GigabitEthernet0/3/0] eth-trunk 10
   [*PE2-GigabitEthernet0/3/0] quit
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] lacp e-trunk system-id 00e0-fc00-0000
   [*PE3] lacp e-trunk priority 10
   [*PE3] e-trunk 1
   [*PE3-e-trunk-1] priority 20
   [*PE3-e-trunk-1] peer-ipv6 2001:DB8:2::2 source-ipv6 2001:DB8:3::3
   [*PE3-e-trunk-1] security-key cipher YsHsjx_202206
   [*PE3-e-trunk-1] quit
   [*PE3] interface eth-trunk 10
   [*PE3-Eth-Trunk10] mode lacp-static
   [*PE3-Eth-Trunk10] e-trunk 1
   [*PE3-Eth-Trunk10] quit
   [*PE3] interface eth-trunk 10.1 mode l2
   [*PE3-Eth-Trunk10.1] encapsulation dot1q vid 10
   [*PE3-Eth-Trunk10.1] evpl instance 1
   [*PE3-Eth-Trunk10.1] quit
   [*PE3] interface gigabitethernet 0/3/0
   [*PE3-GigabitEthernet0/3/0] eth-trunk 10
   [*PE3-GigabitEthernet0/3/0] quit
   [*PE3] commit
   ```
7. Configure a redundancy mode on a per ESI basis on PE2 and PE3.
   
   
   
   # Configure PE2.
   
   ```
   [~PE2] evpn
   [*PE2-evpn] esi 0001.0002.0003.0004.0005
   [*PE2-evpn-esi-0001.0002.0003.0004.0005] evpn redundancy-mode single-active
   [*PE2-evpn-esi-0001.0002.0003.0004.0005] quit
   [*PE2-evpn] quit
   [*PE2] interface Eth-Trunk 10
   [*PE2-Eth-Trunk10] esi 0001.0002.0003.0004.0005
   [*PE2-Eth-Trunk10] quit
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] evpn
   [*PE3-evpn] esi 0001.0002.0003.0004.0005
   [*PE3-evpn-esi-0001.0002.0003.0004.0005] evpn redundancy-mode single-active
   [*PE3-evpn-esi-0001.0002.0003.0004.0005] quit
   [*PE3-evpn] quit
   [*PE3] interface Eth-Trunk 10
   [*PE3-Eth-Trunk10] esi 0001.0002.0003.0004.0005
   [*PE3-Eth-Trunk10] quit
   [*PE3] commit
   ```
8. Configure FRR on the PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] evpn vpn-instance evrf1 vpws
   ```
   ```
   [*PE1-vpws-evpn-instance-evrf1] remote frr enable
   ```
   ```
   [*PE1-vpws-evpn-instance-evrf1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] evpn vpn-instance evrf1 vpws
   ```
   ```
   [*PE2-vpws-evpn-instance-evrf1] local-remote frr enable
   ```
   ```
   [*PE2-vpws-evpn-instance-evrf1] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] evpn vpn-instance evrf1 vpws
   ```
   ```
   [*PE3-vpws-evpn-instance-evrf1] local-remote frr enable
   ```
   ```
   [*PE3-vpws-evpn-instance-evrf1] quit
   ```
   ```
   [*PE3] commit
   ```
9. Configure CE access to the PEs.
   
   
   
   # Configure CE1.
   
   ```
   <CE1> system-view
   [~CE1] vlan 10 
   [*CE1-vlan10] quit           
   [*CE1] interface gigabitethernet 0/1/0
   [*CE1-GigabitEthernet0/1/0] portswitch
   [*CE1-GigabitEthernet0/1/0] undo shutdown
   [*CE1-GigabitEthernet0/1/0] port link-type trunk
   [*CE1-GigabitEthernet0/1/0] port trunk allow-pass vlan 10
   [*CE1-GigabitEthernet0/1/0] commit
   [~CE1-GigabitEthernet0/1/0] quit
   ```
   
   # Configure CE2.
   
   ```
   <CE2> system-view
   [~CE2] vlan 10
   [*CE2-vlan10] quit 
   [*CE2] interface Eth-Trunk10
   [*CE2-Eth-Trunk10] portswitch
   [*CE2-Eth-Trunk10] mode lacp-static
   [*CE2-Eth-Trunk10] undo shutdown
   [*CE2-Eth-Trunk10] port link-type trunk
   [*CE2-Eth-Trunk10] port trunk allow-pass vlan 10
   [*CE2-Eth-Trunk10] quit
   [*CE2] interface gigabitethernet 0/1/0
   [*CE2-GigabitEthernet0/1/0] undo shutdown
   [*CE2-GigabitEthernet0/1/0] eth-trunk 10
   [*CE2-GigabitEthernet0/1/0] quit
   [*CE2] interface gigabitethernet 0/2/0
   [*CE2-GigabitEthernet0/2/0] undo shutdown
   [*CE2-GigabitEthernet0/2/0] eth-trunk 10
   [*CE2-GigabitEthernet0/2/0] quit
   [*CE2] commit
   ```
   
   
   
   After the configuration is complete, the corresponding Eth-Trunk should be up. Run the [**display eth-trunk**](cmdqueryname=display+eth-trunk) command on PE2 and PE3 to check the Eth-Trunk status.
   
   Command output on PE2:
   
   ```
   [~PE2] display eth-trunk 10                              
   Eth-Trunk10's state information is:                     
   WorkingMode: NORMAL          Hash arithmetic: According to flow                 
   Least Active-linknumber: 1   Max Bandwidth-affected-linknumber: 32              
   Operate status: up           Number Of Up Ports In Trunk: 1                     
   --------------------------------------------------------------------------------
   PortName                      Status      Weight        
   GigabitEthernet0/3/0          Up          1               
   ```
   
   Command output on PE3:
   
   ```
   [~PE3] display eth-trunk 10   
   Eth-Trunk10's state information is:                     
   WorkingMode: NORMAL          Hash arithmetic: According to flow                 
   Least Active-linknumber: 1   Max Bandwidth-affected-linknumber: 32              
   Operate status: down         Number Of Up Ports In Trunk: 0                     
   --------------------------------------------------------------------------------
   PortName                      Status      Weight        
   GigabitEthernet0/3/0          Down        1               
   ```
   
   According to the status of Eth-Trunk 10 shown in the preceding command output, PE2 and PE3 are in master and backup states, respectively. That is, only PE2 is active.
10. Verify the configuration.
    
    
    
    Run the **display bgp evpn all routing-table** command on each PE. The command output shows the EVPN routes sent from the peer end. The following example uses the command output on PE1.
    
    ```
    [~PE1] display bgp evpn all routing-table
    
     Local AS number : 100                                  
    
     BGP Local router ID is 1.1.1.1                         
     Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                   h - history,  i - internal, s - suppressed, S - Stale
                   Origin : i - IGP, e - EGP, ? - incomplete
    
    
     EVPN address family:                                   
     Number of A-D Routes: 5                                
     Route Distinguisher: 100:1                             
           Network(ESI/EthTagId)                                  NextHop           
     *>    0000.0000.0000.0000.0000:100                           127.0.0.1         
     Route Distinguisher: 200:1                             
           Network(ESI/EthTagId)                                  NextHop           
     *>i   0001.0002.0003.0004.0005:200                           2001:DB8:2::2     
     Route Distinguisher: 300:1                             
           Network(ESI/EthTagId)                                  NextHop           
     *>i   0001.0002.0003.0004.0005:200                           2001:DB8:3::3     
     Route Distinguisher: 2.2.2.2:0                         
           Network(ESI/EthTagId)                                  NextHop           
     *>i   0001.0002.0003.0004.0005:4294967295                    2001:DB8:2::2     
     Route Distinguisher: 3.3.3.3:0                         
           Network(ESI/EthTagId)                                  NextHop           
     *>i   0001.0002.0003.0004.0005:4294967295                    2001:DB8:3::3     
    
    
     EVPN-Instance evrf1:                                   
     Number of A-D Routes: 5                                
           Network(ESI/EthTagId)                                  NextHop           
     *>    0000.0000.0000.0000.0000:100                           127.0.0.1         
     *>i   0001.0002.0003.0004.0005:200                           2001:DB8:2::2     
     * i                                                          2001:DB8:3::3                                       
     *>i   0001.0002.0003.0004.0005:4294967295                    2001:DB8:2::2     
     * i                                                          2001:DB8:3::3 
    ```
    
    Run the **display bgp evpn all routing-table ad-route** command on PE1. The command output shows the A-D EVPN routes sent from the peer end.
    
    ```
    [~PE1] display bgp evpn all routing-table ad-route 0001.0002.0003.0004.0005:200 
    
     BGP local router ID : 1.1.1.1                          
     Local AS number : 100                                  
     Total routes of Route Distinguisher(200:1): 1          
     BGP routing table entry information of 0001.0002.0003.0004.0005:200:           
     Label information (Received/Applied): 3/NULL           
     From: 2001:DB8:2::2 (2.2.2.2)                          
     Route Duration: 0d00h18m33s                            
     Relay IP Nexthop: FE80::3AC2:67FF:FE31:307             
     Relay IP Out-Interface:GigabitEthernet0/1/0                   
     Relay Tunnel Out-Interface:                            
     Original nexthop: 2001:DB8:2::2                        
     Qos information : 0x0                                  
     Ext-Community: RT <1 : 1>, SoO <2.2.2.2 : 0>, EVPN L2 Attributes <MTU:1500 C:0 P:1 B:0>           
     Prefix-sid: 2001:DB8:21::1:0:3E, Endpoint Behavior: DX2(21)                        
     AS-path Nil, origin incomplete, localpref 100, pref-val 0, valid, internal, best, select, pre 255, IGP cost 10                     
     Route Type: 1 (Ethernet Auto-Discovery (A-D) route)    
     ESI: 0001.0002.0003.0004.0005, Ethernet Tag ID: 200    
     Not advertised to any peer yet                         
    
     Total routes of Route Distinguisher(300:1): 1          
     BGP routing table entry information of 0001.0002.0003.0004.0005:200: 
     Label information (Received/Applied): 3/NULL           
     From: 2001:DB8:3::3 (3.3.3.3)                          
     Route Duration: 0d00h01m06s                            
     Relay IP Nexthop: FE80::3AC2:67FF:FE41:305             
     Relay IP Out-Interface:GigabitEthernet0/2/0                   
     Relay Tunnel Out-Interface:                            
     Original nexthop: 2001:DB8:3::3                        
     Qos information : 0x0                                  
     Ext-Community: RT <1 : 1>, SoO <3.3.3.3 : 0>, EVPN L2 Attributes <MTU:1500 C:0 P:0 B:1>           
     Prefix-sid: 2001:DB8:31::1:0:3E, Endpoint Behavior: DX2(21)                        
     AS-path Nil, origin incomplete, localpref 100, pref-val 0, valid, internal, best, select, pre 255, IGP cost 10                     
     Route Type: 1 (Ethernet Auto-Discovery (A-D) route)    
     ESI: 0001.0002.0003.0004.0005, Ethernet Tag ID: 200    
     Not advertised to any peer yet                         
    
    
    
     EVPN-Instance evrf1:                                   
     Number of A-D Routes: 2                                
     BGP routing table entry information of 0001.0002.0003.0004.0005:200:           
     Route Distinguisher: 200:1                             
     Remote-Cross route 
     Label information (Received/Applied): 3/NULL           
     From: 2001:DB8:2::2 (2.2.2.2)                          
     Route Duration: 0d00h18m45s                            
     Relay IP Nexthop: FE80::3AC2:67FF:FE31:307             
     Relay IP Out-Interface:GigabitEthernet0/1/0                   
     Relay Tunnel Out-Interface:                            
     Original nexthop: 2001:DB8:2::2                        
     Qos information : 0x0                                  
     Ext-Community: RT <1 : 1>, SoO <2.2.2.2 : 0>, EVPN L2 Attributes <MTU:1500 C:0 P:1 B:0>           
     Prefix-sid: 2001:DB8:21::1:0:3E, Endpoint Behavior: DX2(21)                        
     AS-path Nil, origin incomplete, localpref 100, pref-val 0, valid, internal, best, select, pre 255, IGP cost 10                     
     Route Type: 1 (Ethernet Auto-Discovery (A-D) route)    
     ESI: 0001.0002.0003.0004.0005, Ethernet Tag ID: 200    
     Not advertised to any peer yet                         
    
     BGP routing table entry information of 0001.0002.0003.0004.0005:200:           
     Route Distinguisher: 300:1                             
     Remote-Cross route                                     
     Label information (Received/Applied): 3/NULL           
     From: 2001:DB8:3::3 (3.3.3.3)                          
     Route Duration: 0d00h01m19s                            
     Relay IP Nexthop: FE80::3AC2:67FF:FE41:305
     Relay IP Out-Interface:GigabitEthernet0/2/0                   
     Relay Tunnel Out-Interface:                            
     Original nexthop: 2001:DB8:3::3                        
     Qos information : 0x0                                  
     Ext-Community: RT <1 : 1>, SoO <3.3.3.3 : 0>, EVPN L2 Attributes <MTU:1500 C:0 P:0 B:1>           
     Prefix-sid: 2001:DB8:31::1:0:3E, Endpoint Behavior: DX2(21)                        
     AS-path Nil, origin incomplete, localpref 100, pref-val 0, valid, internal, pre 255, IGP cost 10, not preferred for L2 ext-community   
     Route Type: 1 (Ethernet Auto-Discovery (A-D) route)    
     ESI: 0001.0002.0003.0004.0005, Ethernet Tag ID: 200    
     Not advertised to any peer yet   
    ```
    
    According to the preceding command output, the EVPN instance evrf1 has one preferred route 0001.0002.0003.0004.0005:200 with the next hop being PE2. Although an active route with the next hop being PE3 exists, it is not the preferred route. This indicates that dual-homing single-active networking has been configured properly.

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  evpn vpn-instance evrf1 vpws
   route-distinguisher 100:1
   segment-routing ipv6 best-effort
   remote frr enable
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #
  evpl instance 1
   evpn binding vpn-instance evrf1
   local-service-id 100 remote-service-id 200
   segment-routing ipv6 locator PE1
  #               
  segment-routing ipv6
   encapsulation source-address 2001:db8:1::1
   locator PE1 ipv6-prefix 2001:DB8:11:: 64 static 32
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0001.00
   #              
   ipv6 enable topology ipv6
   segment-routing ipv6 locator PE1
   #              
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable    
   ipv6 address 2001:DB8:10::1/64
   isis ipv6 enable 1
  # 
  interface GigabitEthernet0/2/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:20::1/64
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/3/0
   undo shutdown
  #
  interface GigabitEthernet0/3/0.1 mode l2
   encapsulation dot1q vid 10
   evpl instance 1
  #
  interface LoopBack1
   ipv6 enable    
   ip address 1.1.1.1 255.255.255.255
   ipv6 address 2001:DB8:1::1/128
   isis ipv6 enable 1
  #               
  bgp 100         
   router-id 1.1.1.1
   peer 2001:DB8:2::2 as-number 100
   peer 2001:DB8:2::2 connect-interface LoopBack1
   peer 2001:DB8:3::3 as-number 100
   peer 2001:DB8:3::3 connect-interface LoopBack1
   #              
   ipv4-family unicast
    undo synchronization
   #              
   l2vpn-family evpn
    policy vpn-target
    peer 2001:DB8:2::2 enable
    peer 2001:DB8:2::2 advertise encap-type srv6
    peer 2001:DB8:3::3 enable
    peer 2001:DB8:3::3 advertise encap-type srv6
  #
  evpn source-address 1.1.1.1
  #
  return
  ```
* PE2 configuration file
  ```
  #
  sysname PE2
  #
  lacp e-trunk system-id 00e0-fc00-0000
  lacp e-trunk priority 10
  #
  evpn
   #  
   mac-duplication 
   #
   esi 0001.0002.0003.0004.0005
    evpn redundancy-mode single-active
  #
  evpn vpn-instance evrf1 vpws
   route-distinguisher 200:1
   segment-routing ipv6 best-effort
   local-remote frr enable
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #
  evpl instance 1
   evpn binding vpn-instance evrf1
   local-service-id 200 remote-service-id 100
   segment-routing ipv6 locator PE2
  #
  e-trunk 1
   priority 10
   peer-ipv6 2001:DB8:3::3 source-ipv6 2001:DB8:2::2
   security-key cipher %^%#VQE;E!Dl&Rr]if$F>}w9uk5C>y-4|MS$unQ!#Mb#%^%#
  #               
  segment-routing ipv6
   encapsulation source-address 2001:db8:2::2
   locator PE2 ipv6-prefix 2001:DB8:21:: 64 static 32
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0002.00
   #              
   ipv6 enable topology ipv6
   segment-routing ipv6 locator PE2 
   # 
  #
  interface Eth-Trunk10
   mode lacp-static
   e-trunk 1
   esi 0001.0002.0003.0004.0005
  #
  interface Eth-Trunk10.1 mode l2
   encapsulation dot1q vid 10
   evpl instance 1
  # 
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:10::2/64
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable    
   ipv6 address 2001:DB8:30::1/64
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   eth-trunk 10
  #
  interface LoopBack1
   ipv6 enable    
   ip address 2.2.2.2 255.255.255.255
   ipv6 address 2001:DB8:2::2/128
   isis ipv6 enable 1
  #               
  bgp 100         
   router-id 2.2.2.2
   peer 2001:DB8:1::1 as-number 100
   peer 2001:DB8:1::1 connect-interface LoopBack1
   peer 2001:DB8:3::3 as-number 100
   peer 2001:DB8:3::3 connect-interface LoopBack1
   #              
   ipv4-family unicast
    undo synchronization
   #              
   l2vpn-family evpn
    policy vpn-target
    peer 2001:DB8:1::1 enable
    peer 2001:DB8:1::1 advertise encap-type srv6
    peer 2001:DB8:3::3 enable
    peer 2001:DB8:3::3 advertise encap-type srv6
  #
  evpn source-address 2.2.2.2
  #
  return
  ```
* PE3 configuration file
  
  ```
  #
  sysname PE3
  #
  lacp e-trunk system-id 00e0-fc00-0000
  lacp e-trunk priority 10
  #
  evpn
   #  
   mac-duplication 
   #
   esi 0001.0002.0003.0004.0005
    evpn redundancy-mode single-active
  #
  evpn vpn-instance evrf1 vpws
   route-distinguisher 300:1
   segment-routing ipv6 best-effort
   local-remote frr enable
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #
  evpl instance 1
   evpn binding vpn-instance evrf1
   local-service-id 200 remote-service-id 100
   segment-routing ipv6 locator PE3
  #
  e-trunk 1
   priority 20
   peer-ipv6 2001:DB8:2::2 source-ipv6 2001:DB8:3::3
   security-key cipher %^%#!8C!"bAoc~O}UW2)%$HP4%.G9179.;&Yr[GmV.PN%^%#
  #               
  segment-routing ipv6
   encapsulation source-address 2001:db8:3::3
   locator PE3 ipv6-prefix 2001:DB8:31:: 64 static 32
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0003.00
   #              
   ipv6 enable topology ipv6
   segment-routing ipv6 locator PE3
   #              
  #
  interface Eth-Trunk10
   mode lacp-static
   e-trunk 1
   esi 0001.0002.0003.0004.0005
  #
  interface Eth-Trunk10.1 mode l2
   encapsulation dot1q vid 10
   evpl instance 1
  # 
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:20::2/64
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable    
   ipv6 address 2001:DB8:30::2/64
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   eth-trunk 10
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
   peer 2001:DB8:2::2 as-number 100
   peer 2001:DB8:2::2 connect-interface LoopBack1
   #              
   ipv4-family unicast
    undo synchronization
   #              
   l2vpn-family evpn
    policy vpn-target
    peer 2001:DB8:1::1 enable
    peer 2001:DB8:1::1 advertise encap-type srv6
    peer 2001:DB8:2::2 enable
    peer 2001:DB8:2::2 advertise encap-type srv6
  #
  evpn source-address 3.3.3.3
  #
  return
  ```
* CE1 configuration file
  ```
  #
  sysname CE1
  #
  vlan batch 10
  #
  interface GigabitEthernet0/1/0
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 10
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
  interface Eth-Trunk10
   mode lacp-static
   portswitch
   port link-type trunk
   port trunk allow-pass vlan 10
  #   
  interface GigabitEthernet0/1/0 
   undo shutdown
   eth-trunk 10
  #                    
  interface GigabitEthernet0/2/0 
   undo shutdown
   eth-trunk 10
  #
  return
  ```