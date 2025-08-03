Example for Deploying NetStream on a BGP/MPLS IP VPN Network
============================================================

This section provides an example for configuring NetStream on a BGP/MPLS IP VPN network to monitor VPN service traffic.

#### Networking Requirements

As Layer 3 virtual private network (L3VPN) services develop, carriers place increasingly higher requirements on VPN traffic statistics collection. After conventional IP networks carry voice and video services, it has become commonplace for carriers and their customers to sign Service Level Agreements (SLAs). Deploying NetStream on a BGP/MPLS IP VPN network allows users to analyze LSP traffic between PEs and adjust the network to better meet service requirements.

On the IPv4 BGP/MPLS IP VPN network shown in [Figure 1](#EN-US_TASK_0172373031__fig_dc_vrp_ns_cfg_003501):

* Packets with specified application labels are sampled on PE2 and sent to the NetStream Collector (NSC) and NetStream Data Analyzer (NDA).
* Statistics collection of incoming and outgoing packets with specified application labels is enabled on the P. Packets with specified application labels sent by the CE are sampled and sent to the NSC and NDA.
* Traffic statistics are analyzed on the NSC and NDA to obtain users' traffic volume between PEs.

**Figure 1** Networking diagram of the BGP/MPLS IP VPN![](../../../../public_sys-resources/note_3.0-en-us.png) 

* In this example, interfaces 1 through 3 represent GE0/1/0, GE0/2/0, and GE0/3/0, respectively.

  
![](images/fig_dc_vrp_ns_cfg_003501.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IP address to each involved interface.
2. Configure the BGP/MPLS IP VPN.
3. Enable NetStream to sample packets with specified application labels on PE2.
4. Enable NetStream to collect statistics about incoming and outgoing packets with specified labels on the P.

#### Data Preparation

To complete the configuration, you need the following data:

* Version for outputting NetStream packets and sampling interval
* Destination address, destination port number, and source address of the output NetStream flows
* ID of the slot in which the NetStream service processing board resides (In this example, the NetStream service processing board is in slot 3.)

#### Procedure

1. Assign an IP address to each involved interface.
   
   
   
   Assign an IP address and a mask to each interface (including loopback interfaces) according to [Figure 1](#EN-US_TASK_0172373031__fig_dc_vrp_ns_cfg_003501). The configuration details are not provided here.
2. Configure the BGP/MPLS IP VPN.
   
   
   
   For configuration details, see "BGP/MPLS IP VPN Configuration" in *NE40E Configuration > VPN*.
3. Enable NetStream to sample packets with specified application labels on PE2.
   
   # Configure the board on PE2 to process NetStream services in distributed mode.
   ```
   [*PE2] slot 3
   [*PE2-slot-3] ip netstream sampler to slot self
   [*PE2-slot-3] quit
   ```
   
   # Configure PE2 to send information about L3VPN application labels to the NSC.
   ```
   [*PE2] ip netstream export template option application-label
   ```
   
   # Set the version for outputting NetStream flows to V9, and specify the source and destination addresses and destination port number for the output flows.
   
   ```
   [*PE2] ip netstream export version 9
   [*PE2] ip netstream export host 192.168.2.2 9000
   [*PE2] ip netstream export source 192.168.2.1
   ```
4. Enable NetStream to collect statistics about incoming and outgoing packets with specified labels on the P.
   
   # Configure the board on the P to process NetStream services in distributed mode.
   ```
   [*P] slot 3
   [*P-slot-3] ip netstream sampler to slot self
   [*P-slot-3] quit 
   ```
   
   # Collect statistics about incoming and outgoing packets on GigabitEthernet 0/1/0 of the P.
   ```
   [*P] interface GigabitEthernet 0/1/0
   [*P-GigabitEthernet0/1/0] ip netstream inbound
   [*P-GigabitEthernet0/1/0] ip netstream outbound
   [*P-GigabitEthernet0/1/0] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   NetStream enabled on a main interface cannot collect traffic statistics about its sub-interface.
   
   
   
   # Configure NetStream to sample both inner IP packets and labels of MPLS packets.
   ```
   [*P] ip netstream mpls-aware label-and-ip
   ```
   
   # Set the version for outputting NetStream flows to V9, and specify the source and destination addresses and destination port number for the output flows.
   
   ```
   [*P] ip netstream export version 9
   [*P] ip netstream export host 172.16.2.2 9001
   [*P] ip netstream export source 172.16.2.1
   ```
   
   # Enable NetStream sampling and configure the fixed packet sampling mode.
   
   ```
   [*P] ip netstream sampler fix-packets 10000 inbound
   [*P] ip netstream sampler fix-packets 10000 outbound
   [*P] commit
   ```
5. Verify the configuration.
   
   
   
   # Run the [**display ip netstream cache origin slot**](cmdqueryname=display+ip+netstream+cache+origin+slot) **3** command on the P after completing the configuration. The command output shows IP and MPLS related information about VPN packets cached in the NetStream flow buffer.
   
   ```
   [~P] display ip netstream cache origin slot 3
   
   
    DstIf                         
    SrcIf                           
    DstP                          Msk          Pro            Tos 
    SrcP                          Msk          Flags          Ttl
    Packets                                                   Bytes
    NextHop                                                   Direction
    DstIP                                                     DstAs
    SrcIP                                                     SrcAs
    BGP: BGP NextHop                                          TopLabelType
    Label1                        Exp1         Bottom1
    Label2                        Exp2         Bottom2
    Label3                        Exp3         Bottom3
    TopLabelIpAddress                          VlanId         VniId
    CreateFlowTime                LastRefreshTime             VPN(direct)
    FlowLabel                     Rdvalue
    ForwardStatus
     --------------------------------------------------------------------------
   
    GigabitEthernet0/2/0                                                          
    GigabitEthernet0/1/0                                            
    0                             24            253            0
    0                             24            0              60
    3                                                          384       
    172.16.3.1                                                 in
    10.2.1.5                                                   0         
    10.4.1.5                                                   0         
    0.0.0.0                                                    UNKNOWN             
    0                             0            0         
    0                             0            0         
    0                             0            0         
    0.0.0.0                                    0               0        
    2018-05-09 11:38:07           2018-05-09 11:40:30          --
    --                            -:-
    66(Forwarded Not Fragmented)
   ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  ```
  ```
  sysname PE1
  ```
  ```
  #
  ```
  ```
  ip vpn-instance vpna
  ```
  ```
   route-distinguisher 100:1
  ```
  ```
   apply-label per-instance
  ```
  ```
   vpn-target 100:1 export-extcommunity
  ```
  ```
   vpn-target 100:1 import-extcommunity
  ```
  ```
  #
  ```
  ```
   mpls lsr-id 1.1.1.9
  ```
  ```
  #
  ```
  ```
  mpls
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   ip binding vpn-instance vpna
  ```
  ```
   ip address 10.2.1.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/3/0
  ```
  ```
    ip address 172.16.1.1 255.255.255.0
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
  interface LoopBack1
  ```
  ```
   ip address 1.1.1.9 255.255.255.255
  ```
  ```
  #
  ```
  ```
  bgp 100
  ```
  ```
   peer 3.3.3.9 as-number 100
  ```
  ```
   peer 3.3.3.9 connect-interface LoopBack1
  ```
  ```
   #
  ```
  ```
   ipv4-family unicast
  ```
  ```
    peer 3.3.3.9 enable
  ```
  ```
   #
  ```
  ```
   ipv4-family vpnv4
  ```
  ```
    policy vpn-target
  ```
  ```
    peer 3.3.3.9 enable
  ```
  ```
  #
  ```
  ```
   ipv4-family vpn-instance vpna
  ```
  ```
    import-route direct
  ```
  ```
    peer 10.1.1.1 as-number 65440
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
    network 1.1.1.9 0.0.0.0
  ```
  ```
    network 172.16.1.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  return
  ```
* P configuration file
  
  ```
  #
  ```
  ```
  slot 3
  ```
  ```
   ip netstream sampler to slot self
  ```
  ```
  #
  ```
  ```
  sysname P
  ```
  ```
  #
  ```
  ```
   ip netstream mpls-aware label-and-ip
  ```
  ```
   ip netstream export version 9
  ```
  ```
   ip netstream sampler fix-packets 10000 inbound
  ```
  ```
   ip netstream sampler fix-packets 10000 outbound 
  ```
  ```
   ip netstream export source 172.16.2.1
  ```
  ```
   ip netstream export host 172.16.2.2 9001
  ```
  ```
  #
  ```
  ```
  mpls lsr-id 2.2.2.9
  ```
  ```
  #
  ```
  ```
  mpls
  ```
  ```
   lsp-trigger all
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
   ip address 172.16.1.2 255.255.255.0
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
   ip address 172.16.3.1 255.255.255.0
  ```
  ```
   ip netstream inbound
  ```
  ```
   ip netstream outbound
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
  interface GigabitEthernet0/3/0
  ```
  ```
   ip address 172.16.2.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface LoopBack1
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
    network 172.16.1.0 0.0.0.255
  ```
  ```
    network 172.17.1.0 0.0.0.255
  ```
  ```
    network 2.2.2.9 0.0.0.0
  ```
  ```
  #
  ```
  ```
  return
  ```
* PE2 configuration file
  
  ```
  #
  ```
  ```
  slot 3
  ```
  ```
   ip netstream sampler to slot self
  ```
  ```
  #
  ```
  ```
  sysname PE2
  ```
  ```
  # 
  ```
  ```
   ip netstream export version 9
  ```
  ```
   ip netstream export source 192.168.2.1
  ```
  ```
   ip netstream export host 192.168.2.2 9000
  ```
  ```
   ip netstream export template option application-label
  ```
  ```
  #
  ```
  ```
  ip vpn-instance vpna
  ```
  ```
   route-distinguisher 200:1
  ```
  ```
   apply-label per-instance
  ```
  ```
   vpn-target 100:1 export-extcommunity
  ```
  ```
   vpn-target 100:1 import-extcommunity
  ```
  ```
  #
  ```
  ```
  mpls lsr-id 3.3.3.9
  ```
  ```
  #
  ```
  ```
  mpls
  ```
  ```
   lsp-trigger all
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
   ip binding vpn-instance vpna
  ```
  ```
   ip address 10.3.1.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/3/0
  ```
  ```
   ip address 172.16.3.2 255.255.255.0
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
  interface LoopBack1
  ```
  ```
   ip address 3.3.3.9 255.255.255.255
  ```
  ```
  #
  ```
  ```
  bgp 100
  ```
  ```
   peer 1.1.1.9 as-number 100
  ```
  ```
   peer 1.1.1.9 connect-interface LoopBack1
  ```
  ```
   #
  ```
  ```
   ipv4-family unicast
  ```
  ```
    peer 1.1.1.9 enable
  ```
  ```
   #
  ```
  ```
   ipv4-family vpnv4
  ```
  ```
    policy vpn-target
  ```
  ```
    peer 1.1.1.9 enable
  ```
  ```
   #
  ```
  ```
   ipv4-family vpn-instance vpna
  ```
  ```
    import-route direct
  ```
  ```
    peer 10.4.1.1 as-number 65440
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
    network 172.17.1.0 0.0.0.255
  ```
  ```
    network 3.3.3.9 0.0.0.0
  ```
  ```
  #
  ```
  ```
  return
  ```
* CE2 configuration file
  
  ```
  #
  ```
  ```
  sysname CE2
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   ip address 10.2.1.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  bgp 65420
  ```
  ```
   peer 10.2.1.2 as-number 100
  ```
  ```
   #
  ```
  ```
   ipv4-family unicast
  ```
  ```
    import-route direct
  ```
  ```
    peer 10.2.1.2 enable
  ```
  ```
  #
  ```
  ```
  return
  ```
* CE4 configuration file
  
  ```
  #
  ```
  ```
  sysname CE4
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   ip address 10.4.1.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  bgp 65440
  ```
  ```
   peer 10.4.1.2 as-number 100
  ```
  ```
   #
  ```
  ```
   ipv4-family unicast
  ```
  ```
    import-route direct
  ```
  ```
    peer 10.4.1.2 enable
  ```
  ```
  #
  ```
  ```
  return
  ```