Example for Configuring Inter-AS VPN Option B with a P Between ASBRs
====================================================================

An LSP is set up between ASBRs through LDP + IGP to traverse MPLS networks that do not support VPN. A P is deployed between the ASBRs.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172369506__fig_dc_vrp_mpls-l3vpn-v4_cfg_011501), CE1 and CE2 belong to the same VPN. CE1 connects to PE1 in AS 100, and CE2 connects to PE2 in AS 200. The MPLS network between ASBRs does not support VPN. In other words, there must be a P between the ASBRs. It is required that an LSP be set up between the ASBRs in different ASs to implement inter-AS VPN Option B.

**Figure 1** Inter-AS VPN Option B networking with a P between ASBRs![](../../../../public_sys-resources/note_3.0-en-us.png) 

interface1 and interface2 in this example represent GE0/1/0 and GE0/2/0, respectively.


  
![](images/fig_dc_vrp_mpls-l3vpn-v4_cfg_011501.png)

#### Precautions

When configuring inter-AS VPN Option B with a P between ASBRs, note the following:

* ASBRs do not need to have VPN instances or filter received VPNv4 routes based on VPN targets.
* IGP + LDP needs to be deployed between ASBRs.
* The MP-EBGP connection between ASBRs involves multiple hops.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IGP on the backbone network for IP connectivity between the ASBR and PE in the same AS, and set up an MPLS LDP LSP between the ASBR and PE in the same AS.
2. Set up EBGP peer relationships between PEs and CEs and MP-IBGP peer relationships between PEs and ASBRs.
3. Configure VPN instances on the PEs rather than ASBRs.
4. Set up an EBGP peer relationship and an MPLS LDP LSP between ASBRs.

#### Data Preparation

To complete the configuration, you need the following data:

* MPLS LSR IDs of the PEs and ASBRs: 10.31.1.9, 10.32.2.9, 10.33.3.9, 10.34.4.9, and 10.35.5.9
* Name (vpn1), RD (100:1/200:1), and export and import VPN targets (1:1) of the VPN instance on each PE

#### Procedure

1. On the MPLS backbone networks in AS 100 and AS 200, configure IGP for IP connectivity between the PE and ASBR on each network.
   
   
   
   In this example, OSPF is used as an IGP. For configuration details, see the configuration files.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The 32-bit IP address of the loopback interface that functions as the LSR ID needs to be advertised using OSPF.
   
   After the configuration is complete, run the **display ospf peer** command on the ASBR and PE in each AS. The command output shows that the OSPF neighbor relationship is in the **Full** state, which indicates that the OSPF neighbor relationship has been established between the ASBR and PE in the same AS.
   
   The ASBR and PE in the same AS can learn and successfully ping the address of each other's loopback interface.
2. Configure basic MPLS capabilities and MPLS LDP on the MPLS backbone networks in AS 100 and AS 200 to establish LDP LSPs.
   
   
   
   For configuration details, see the configuration files.
3. Configure the basic BGP/MPLS IP VPN functions on PE1 and PE2.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   PE1's import and export VPN targets must match PE2's export and import VPN targets, respectively.
   
   For configuration details, see the configuration files.
4. Establish an MPLS LDP LSP and an MP-EBGP peer relationship between ASBRs.
   
   
   
   Configure IGP between the ASBRs. This example uses OSPF as IGP.
   
   # Configure ASBR1.
   
   ```
   <ASBR1> system-view
   ```
   ```
   [~ASBR1] interface gigabitethernet 0/2/0
   ```
   ```
   [~ASBR1-GigabitEthernet0/2/0] ip address 192.168.1.1 24
   ```
   ```
   [*ASBR1-GigabitEthernet0/2/0] commit
   ```
   ```
   [~ASBR1-GigabitEthernet0/2/0] quit
   ```
   ```
   [~ASBR1] ospf 2
   ```
   ```
   [*ASBR1-ospf-2] area 0
   ```
   ```
   [*ASBR1-ospf-2-area-0.0.0.0] network 10.32.2.10 0.0.0.0
   ```
   ```
   [*ASBR1-ospf-2-area-0.0.0.0] network 192.168.1.0 0.0.0.255
   ```
   ```
   [*ASBR1-ospf-2-area-0.0.0.0] quit
   ```
   ```
   [*ASBR1-ospf-2] commit
   ```
   ```
   [~ASBR1-ospf-2] quit
   ```
   ```
   [~ASBR1] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The process ID of the OSPF protocol running between ASBRs must be different from the process ID of the OSPF protocol running in each AS.
   
   The configurations of ASBR2 and the P are similar to the configuration of ASBR1. For configuration details, see the configuration files.
   
   # Set up an MPLS LDP LSP between ASBRs.
   
   ```
   <ASBR1> system-view
   ```
   ```
   [~ASBR1] mpls lsr-id 10.32.2.9
   ```
   ```
   [*ASBR1] mpls
   ```
   ```
   [*ASBR1-mpls] quit
   ```
   ```
   [*ASBR1] mpls ldp
   ```
   ```
   [*ASBR1-mpls-ldp] quit
   ```
   ```
   [*ASBR1] interface gigabitethernet0/2/0
   ```
   ```
   [*ASBR1-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*ASBR1-GigabitEthernet0/2/0] mpls ldp
   ```
   ```
   [*ASBR1-GigabitEthernet0/2/0] commit
   ```
   ```
   [~ASBR1-GigabitEthernet0/2/0] quit
   ```
   
   The configurations of ASBR2 and the P are similar to the configuration of ASBR1. For configuration details, see the configuration files.
   
   After the configuration is complete, run the **display mpls ldp lsp** command on ASBRs. The command output shows that an MPLS LDP LSP has been established between ASBRs.
   
   ```
   <ASBR1>display mpls ldp lsp
   ```
   ```
    LDP LSP Information
    -------------------------------------------------------------------------------
    Flag after Out IF: (I) - RLFA Iterated LSP, (I*) - Normal and RLFA Iterated LSP
    -------------------------------------------------------------------------------
    DestAddress/Mask   In/OutLabel    UpstreamPeer    NextHop          OutInterface
    -------------------------------------------------------------------------------
    10.31.1.9/32       NULL/3         -               172.16.1.2       GigabitEthernet0/1/0
    10.31.1.9/32       48060/3        10.31.1.9       172.16.1.2       GigabitEthernet0/1/0
    10.31.1.9/32       48060/3        10.35.5.9       172.16.1.2       GigabitEthernet0/1/0
    10.32.2.9/32       3/NULL         10.31.1.9       127.0.0.1        Loop1
    10.32.2.9/32       3/NULL         10.35.5.9       127.0.0.1        Loop1
   *10.32.2.9/32       Liberal/48061                  DS/10.31.1.9
   *10.32.2.9/32       Liberal/48077                  DS/10.35.5.9
    10.32.2.10/32      3/NULL         10.31.1.9       127.0.0.1        Loop2
    10.32.2.10/32      3/NULL         10.35.5.9       127.0.0.1        Loop2
   *10.32.2.10/32      Liberal/48076                  DS/10.35.5.9
    10.33.3.9/32       NULL/48079     -               192.168.1.2      GigabitEthernet0/2/0
    10.33.3.9/32       48080/48079    10.31.1.9       192.168.1.2      GigabitEthernet0/2/0
    10.33.3.9/32       48080/48079    10.35.5.9       192.168.1.2      GigabitEthernet0/2/0
    10.33.3.10/32      NULL/48078     -               192.168.1.2      GigabitEthernet0/2/0
    10.33.3.10/32      48079/48078    10.31.1.9       192.168.1.2      GigabitEthernet0/2/0
    10.33.3.10/32      48079/48078    10.35.5.9       192.168.1.2      GigabitEthernet0/2/0
    10.35.5.9/32       NULL/3         -               192.168.1.2      GigabitEthernet0/2/0
    10.35.5.9/32       48078/3        10.31.1.9       192.168.1.2      GigabitEthernet0/2/0
    10.35.5.9/32       48078/3        10.35.5.9       192.168.1.2      GigabitEthernet0/2/0
    -------------------------------------------------------------------------------
    TOTAL: 5 Normal LSP(s) Found.
    TOTAL: 1 Liberal LSP(s) Found.
    TOTAL: 0 Frr LSP(s) Found.
    An asterisk (*) before an LSP means the LSP is not established
    An asterisk (*) before a Label means the USCB or DSCB is stale
    An asterisk (*) before an UpstreamPeer means the session is stale
    An asterisk (*) before a DS means the session is stale
    An asterisk (*) before a NextHop means the LSP is FRR LSP
   ```
   
   # Configure ASBR1 to establish an MP-EBGP peer with ASBR2, and disable ASBR1 from filtering received VPNv4 routes based on VPN targets.
   
   ```
   [~ASBR1] bgp 100
   ```
   ```
   [*ASBR1-bgp] peer 10.33.3.10 as-number 200
   ```
   ```
   [*ASBR1-bgp] peer 10.33.3.10 connect-interface loopback2
   ```
   ```
   [*ASBR1-bgp] peer 10.33.3.10 ebgp-max-hop 3
   ```
   ```
   [*ASBR1-bgp] ipv4-family vpnv4
   ```
   ```
   [*ASBR1-bgp-af-vpnv4] peer 10.33.3.10 enable
   ```
   ```
   [*ASBR1-bgp-af-vpnv4] undo policy vpn-target
   ```
   ```
   [*ASBR1-bgp-af-vpnv4] commit
   ```
   ```
   [~ASBR1-bgp-af-vpnv4] quit
   ```
   ```
   [~ASBR1-bgp] quit
   ```
5. Verify the configuration.
   
   
   
   After the configuration is complete, CE1 and CE2 can learn routes to interfaces on each other and ping each other successfully.
   
   The following example uses the command output on CE1.
   
   ```
   <CE1> display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ```
   ```
   ------------------------------------------------------------------------------
   ```
   ```
   Routing Table: _public_
   ```
   ```
            Destinations : 8        Routes : 8
   ```
   ```
   Destination/Mask    Proto  Pre  Cost     Flags NextHop         Interface
   ```
   ```
          10.1.1.0/24  Direct 0    0             D  10.1.1.1        GigabitEthernet0/1/0
   ```
   ```
          10.1.1.1/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/1/0
   ```
   ```
        10.1.1.255/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/1/0
   ```
   ```
      10.22.22.22/32  EBGP   255  0             D  10.1.1.2        GigabitEthernet0/1/0
   ```
   ```
         127.0.0.0/8   Direct 0    0             D  127.0.0.1       InLoopBack0
   ```
   ```
         127.0.0.1/32  Direct 0    0             D  127.0.0.1       InLoopBack0
   ```
   ```
   127.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
   ```
   ```
   255.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
   ```
   ```
   <CE1> ping -a 10.11.11.11 10.22.22.22
   ```
   ```
     PING 10.22.22.22: 56  data bytes, press CTRL_C to break
   ```
   ```
       Reply from 10.22.22.22: bytes=56 Sequence=1 ttl=252 time=120 ms
   ```
   ```
       Reply from 10.22.22.22: bytes=56 Sequence=2 ttl=252 time=73 ms
   ```
   ```
       Reply from 10.22.22.22: bytes=56 Sequence=3 ttl=252 time=111 ms
   ```
   ```
       Reply from 10.22.22.22: bytes=56 Sequence=4 ttl=252 time=86 ms
   ```
   ```
       Reply from 10.22.22.22: bytes=56 Sequence=5 ttl=252 time=110 ms
   ```
   ```
     --- 22.22.22.22 ping statistics ---
   ```
   ```
       5 packet(s) transmitted
   ```
   ```
       5 packet(s) received
   ```
   ```
       0.00% packet loss
   ```
   ```
       round-trip min/avg/max = 73/100/120 ms 
   ```
   
   Run the **display bgp vpnv4 all routing-table** command on either ASBR to view information about VPNv4 routes.
   
   The following example uses the command output on ASBR1.
   
   ```
   <ASBR1> display bgp vpnv4 all routing-table
   ```
   ```
    BGP Local router ID is 10.32.2.9
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
   
   
    Total number of routes from all PE: 2
    Route Distinguisher: 100:1
   
   
         Network            NextHop        MED        LocPrf    PrefVal Path/Ogn
   
    *>i  10.11.11.11/32   10.31.1.9       0          100        0      65001i
    Route Distinguisher: 200:1
   
   
         Network            NextHop        MED        LocPrf    PrefVal Path/Ogn
   
    *>   10.22.22.22/24   10.33.3.10                           0      200 65002i
   ```

#### Configuration Files

* CE1 configuration file
  
  ```
  #
  sysname CE1
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
  #
  interface Loopback 1
   ip address 10.11.11.11 255.255.255.255
  #
  bgp 65001
   peer 10.1.1.2 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    network 10.11.11.11 255.255.255.255
    peer 10.1.1.2 enable
  return
  ```
* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 1:1 export-extcommunity
    vpn-target 1:1 import-extcommunity
  #
  mpls lsr-id 10.31.1.9
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 172.16.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip binding vpn-instance vpn1
   ip address 10.1.1.2 255.255.255.0
  #
  interface LoopBack1
   ip address 10.31.1.9 255.255.255.255
  #
  bgp 100
   peer 10.32.2.9 as-number 100
   peer 10.32.2.9 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 10.32.2.9 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 10.32.2.9 enable
  #
   ipv4-family vpn-instance vpn1
    peer 10.1.1.1 as-number 65001
  #
  ospf 1
   area 0.0.0.0
    network 10.31.1.9 0.0.0.0
    network 172.16.1.0 0.0.0.255
  #
  return
  ```
* ASBR1 configuration file
  
  ```
  #
  sysname ASBR1
  #
  mpls lsr-id 10.32.2.9
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 172.16.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 192.168.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 10.32.2.9 255.255.255.255
  #
  interface LoopBack2
   ip address 10.32.2.10 255.255.255.255
  #
  bgp 100
   peer 10.31.1.9 as-number 100
   peer 10.31.1.9 connect-interface LoopBack1
   peer 10.33.3.10 as-number 200
   peer 10.33.3.10 connect-interface LoopBack2
   peer 10.33.3.10 ebgp-max-hop 3
   #
   ipv4-family unicast
    undo synchronization
    peer 10.33.3.10 enable
    peer 10.31.1.9 enable
   #
   ipv4-family vpnv4
    undo policy vpn-target
    peer 10.31.1.9 enable
    peer 10.33.3.10 enable
  #
  ospf 1
   area 0.0.0.0
    network 10.32.2.9 0.0.0.0
    network 172.16.1.0 0.0.0.255
  #
  ospf 2
   import-route direct
   area 0.0.0.0
    network 10.32.2.10 0.0.0.0
    network 192.168.1.0 0.0.0.255
  #
  return
  ```
* P configuration file
  
  ```
  #
  sysname P
  #
  mpls lsr-id 10.35.5.9
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 192.168.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 192.168.2.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 10.35.5.9 255.255.255.255
  #
  ospf 1
   area 0.0.0.0
    network 10.35.5.9 0.0.0.0
    network 192.168.1.0 0.0.0.255
    network 192.168.2.0 0.0.0.255
  #
  return
  ```
* ASBR2 configuration file
  
  ```
  #
  sysname ASBR2
  #
  mpls lsr-id 10.33.3.9
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.162.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 192.168.2.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 10.33.3.9 255.255.255.255
  #
  interface LoopBack2
   ip address 10.33.3.10 255.255.255.255
  #
  bgp 200
   peer 10.32.2.10 as-number 100
   peer 10.32.2.10 connect-interface LoopBack2
   peer 10.32.2.10 ebgp-max-hop 3
   peer 10.34.4.9 as-number 200
   peer 10.34.4.9 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 10.32.2.10 enable
    peer 10.34.4.9 enable
   #
   ipv4-family vpnv4
    undo policy vpn-target
    peer 10.34.4.9 enable
    peer 10.32.2.10 enable
  #
  ospf 1
   area 0.0.0.0
    network 10.33.3.9 0.0.0.0
    network 10.162.1.0 0.0.0.255
  #
  ospf 2
   import-route direct
   area 0.0.0.0
    network 10.33.3.10 0.0.0.0
    network 192.168.2.0 0.0.0.255
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 200:1
    apply-label per-instance
    vpn-target 1:1 export-extcommunity
    vpn-target 1:1 import-extcommunity
  #
  mpls lsr-id 10.34.4.9
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.162.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip binding vpn-instance vpn1
   ip address 10.2.1.2 255.255.255.0
  #
  interface LoopBack1
   ip address 10.34.4.9 255.255.255.255
  #
  bgp 200
   peer 10.33.3.9 as-number 200
   peer 10.33.3.9 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 10.33.3.9 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 10.33.3.9 enable
  #
   ipv4-family vpn-instance vpn1
    peer 10.2.1.1 as-number 65002
  #
  ospf 1
   area 0.0.0.0
    network 10.34.4.9 0.0.0.0
    network 10.162.1.0 0.0.0.255
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
   ip address 10.2.1.1 255.255.255.0
  #
  interface Loopback 1
   ip address 10.22.22.22 255.255.255.255
  #
  bgp 65002
   peer 10.2.1.2 as-number 200
   #
   ipv4-family unicast
    undo synchronization
    network 10.22.22.22 255.255.255.255
    peer 10.2.1.2 enable
  #
  return
  ```