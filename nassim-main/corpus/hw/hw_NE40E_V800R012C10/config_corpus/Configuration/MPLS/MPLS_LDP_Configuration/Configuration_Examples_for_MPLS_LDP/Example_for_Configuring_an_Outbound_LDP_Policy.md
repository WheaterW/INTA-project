Example for Configuring an Outbound LDP Policy
==============================================

This section provides an example for configuring an outbound Label Distribution Protocol (LDP) policy that uses routes matching a specified IP prefix list to establish LDP label switched paths (LSPs).

#### Networking Requirements

An IP metro or bearer network uses L2VPN or L3VPN to transmit high speed Internet (HSI) or voice over IP (VoIP) services over end-to-end public network LDP LSPs. Generally, user-side DSLAMs have low performance, and are easily overloaded if a large number of LDP LSPs are established. To prevent this issue, configure an outbound LDP policy to minimize LDP LSPs to be established, reduce DSLAM memory consumption, and relieve the burden of the DSLAMs.

**Figure 1** Networking diagram for configuring an outbound LDP policy![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE0/1/1 and GE0/1/3, respectively.


  
![](figure/en-us_image_0279158611.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IP address to each interface, including the loopback interface on each node.
2. Configure OSPF to advertise the route to each network segment to which each interface is connected and advertise the host route to each LSR ID.
3. Enable MPLS and MPLS LDP globally on each node.
4. Configure an outbound LDP policy on LSRA to send the DSLAM the Label Mapping messages destined for LSRC only. This allows the DSLAM to establish an LSP to LSRC only, reducing memory usage.
5. Configure MPLS and MPLS LDP on each interface.

#### Data Preparation

To complete the configuration, you need the following data:

* IP address of each interface on each LSR (as shown in [Figure 1](#EN-US_TASK_0172368572__fig_dc_vrp_ldp-p2p_cfg_004801)), OSPF process ID (1), and area ID (0.0.0.0)
* LSR ID (loopback interface IP address as shown in [Figure 1](#EN-US_TASK_0172368572__fig_dc_vrp_ldp-p2p_cfg_004801)) of each node
* Name of an IP prefix list (prefix1) to be specified in an outbound LDP policy on LSRA

#### Procedure

1. Assign an IP address to each interface and configure an IGP.
   
   
   
   Assign an IP address and mask to each interface (as shown in [Figure 1](#EN-US_TASK_0172368572__fig_dc_vrp_ldp-p2p_cfg_004801)), including the loopback interfaces. Configure OSPF to advertise the route to the network segment to which each interface is connected and the host route to each LSR ID.
2. Enable MPLS and MPLS LDP globally on each node.
   
   
   
   # Configure LSRA.
   
   ```
   <LSRA> system-view 
   ```
   ```
   [~LSRA] mpls lsr-id 3.3.3.9
   ```
   ```
   [*LSRA] mpls
   ```
   ```
   [*LSRA-mpls] quit
   ```
   ```
   [*LSRA] mpls ldp
   ```
   ```
   [*LSRA-mpls-ldp] commit
   ```
   ```
   [~LSRA-mpls-ldp] quit
   ```
   
   # Configure LSRB.
   
   ```
   <LSRB> system-view 
   ```
   ```
   [~LSRB] mpls lsr-id 2.2.2.9
   ```
   ```
   [*LSRB] mpls
   ```
   ```
   [*LSRB-mpls] quit
   ```
   ```
   [*LSRB] mpls ldp
   ```
   ```
   [*LSRB-mpls-ldp] commit
   ```
   ```
   [~LSRB-mpls-ldp] quit
   ```
   
   # Configure LSRC.
   
   ```
   <LSRC> system-view 
   ```
   ```
   [~LSRC] mpls lsr-id 1.1.1.9
   ```
   ```
   [*LSRC] mpls
   ```
   ```
   [*LSRC-mpls] quit
   ```
   ```
   [*LSRC] mpls ldp
   ```
   ```
   [*LSRC-mpls-ldp] commit
   ```
   ```
   [~LSRC-mpls-ldp] quit
   ```
   
   # Configure the DSLAM.
   
   ```
   <DSLAM> system-view 
   ```
   ```
   [~DSLAM] mpls lsr-id 4.4.4.9
   ```
   ```
   [*DSLAM] mpls
   ```
   ```
   [*DSLAM-mpls] quit
   ```
   ```
   [*DSLAM] mpls ldp
   ```
   ```
   [*DSLAM-mpls-ldp] commit
   ```
   ```
   [~DSLAM-mpls-ldp] quit
   ```
3. Configure an outbound LDP policy.
   
   
   
   # Configure an IP prefix list on LSRA to permit only the routes to LSRC.
   
   ```
   [~LSRA] ip ip-prefix prefix1 permit 1.1.1.9 32
   ```
   
   # Configure an outbound policy on LSRA to send the DSLAM the Label Mapping messages destined for LSRC only.
   
   ```
   [*LSRA] mpls ldp
   ```
   ```
   [*LSRA-mpls-ldp] ipv4-family
   ```
   ```
   [*LSRA-mpls-ldp-ipv4] outbound peer 4.4.4.9 fec ip-prefix prefix1
   ```
   ```
   [*LSRA-mpls-ldp-ipv4] commit
   ```
   ```
   [~LSRA-mpls-ldp-ipv4] quit
   ```
   ```
   [~LSRA-mpls-ldp] quit
   ```
4. Enable MPLS and MPLS LDP on each interface.
   
   
   
   # Configure LSRA.
   
   ```
   <LSRA> system-view 
   ```
   ```
   [~LSRA] interface gigabitethernet0/1/1
   ```
   ```
   [~LSRA-GigabitEthernet0/1/1] mpls
   ```
   ```
   [*LSRA-GigabitEthernet0/1/1] mpls ldp
   ```
   ```
   [*LSRA-GigabitEthernet0/1/1] commit
   ```
   ```
   [~LSRA-GigabitEthernet0/1/1] quit
   ```
   ```
   [~LSRA] interface gigabitethernet0/1/3
   ```
   ```
   [~LSRA-GigabitEthernet0/1/3] mpls
   ```
   ```
   [*LSRA-GigabitEthernet0/1/3] mpls ldp
   ```
   ```
   [*LSRA-GigabitEthernet0/1/3] commit
   ```
   ```
   [~LSRA-GigabitEthernet0/1/3] quit
   ```
   
   # Configure LSRB.
   
   ```
   <LSRB> system-view 
   ```
   ```
   [~LSRB] interface gigabitethernet0/1/1
   ```
   ```
   [~LSRB-GigabitEthernet0/1/1] mpls
   ```
   ```
   [*LSRB-GigabitEthernet0/1/1] mpls ldp
   ```
   ```
   [*LSRB-GigabitEthernet0/1/1] quit
   ```
   ```
   [*LSRB] interface gigabitethernet0/1/3
   ```
   ```
   [*LSRB-GigabitEthernet0/1/3] mpls
   ```
   ```
   [*LSRB-GigabitEthernet0/1/3] mpls ldp
   ```
   ```
   [*LSRB-GigabitEthernet0/1/3] commit
   ```
   ```
   [~LSRB-GigabitEthernet0/1/3] quit
   ```
   
   # Configure LSRC.
   
   ```
   <LSRC> system-view 
   ```
   ```
   [~LSRC] interface gigabitethernet0/1/1
   ```
   ```
   [~LSRC-GigabitEthernet0/1/1] mpls
   ```
   ```
   [*LSRC-GigabitEthernet0/1/1] mpls ldp
   ```
   ```
   [*LSRC-GigabitEthernet0/1/1] commit
   ```
   ```
   [~LSRC-GigabitEthernet0/1/1] quit
   ```
   
   # Configure the DSLAM.
   
   ```
   <DSLAM> system-view 
   ```
   ```
   [~DSLAM] interface gigabitethernet0/1/1
   ```
   ```
   [~DSLAM-GigabitEthernet0/1/1] mpls
   ```
   ```
   [*DSLAM-GigabitEthernet0/1/1] mpls ldp
   ```
   ```
   [*DSLAM-GigabitEthernet0/1/1] commit
   ```
   ```
   [~DSLAM-GigabitEthernet0/1/1] quit
   ```
5. Verify the configuration.
   
   
   
   After completing the preceding configuration, run the **display mpls ldp lsp** command on the DSLAM. The command output shows that only an LSP to LSRC is established.
   
   ```
   [~DSLAM] display mpls ldp lsp
   ```
   ```
    LDP LSP Information
    -------------------------------------------------------------------------------
    Flag after Out IF: (I) - RLFA Iterated LSP, (I*) - Normal and RLFA Iterated LSP
    -------------------------------------------------------------------------------
    DestAddress/Mask   In/OutLabel    UpstreamPeer    NextHop         OutInterface
    -------------------------------------------------------------------------------
    1.1.1.9/32         NULL/1025      -               10.1.3.1        GE0/1/1
    1.1.1.9/32         1024/1025      3.3.3.9         10.1.3.1        GE0/1/1
    4.4.4.9/32         3/NULL         3.3.3.9         127.0.0.1       LoopBack0
    -------------------------------------------------------------------------------
    TOTAL: 3 Normal LSP(s) Found.
    TOTAL: 0 Liberal LSP(s) Found.
    TOTAL: 0 Frr LSP(s) Found.
    An asterisk (*) before an LSP means the LSP is not established
    An asterisk (*) before a Label means the USCB or DSCB is stale
    An asterisk (*) before an UpstreamPeer means the session is stale
    An asterisk (*) before a DS means the session is stale
    An asterisk (*) before a NextHop means the LSP is FRR LSP
   
   ```
   
   If no outbound LDP policy is configured on LSRA, the LDP LSPs established on the DSLAM are as follows:
   
   ```
    LDP LSP Information
    -------------------------------------------------------------------------------
    Flag after Out IF: (I) - RLFA Iterated LSP, (I*) - Normal and RLFA Iterated LSP
    -------------------------------------------------------------------------------
    DestAddress/Mask   In/OutLabel    UpstreamPeer    NextHop         OutInterface
    -------------------------------------------------------------------------------
    1.1.1.9/32         NULL/1025      -               10.1.3.1        GE0/1/1
    1.1.1.9/32         1024/1025      3.3.3.9         10.1.3.1        GE0/1/1
    2.2.2.9/32         NULL/1024      -               10.1.3.1        GE0/1/1
    2.2.2.9/32         1027/1024      3.3.3.9         10.1.3.1        GE0/1/1
    3.3.3.9/32         NULL/3         -               10.1.3.1        GE0/1/1
    3.3.3.9/32         1028/3         3.3.3.9         10.1.3.1        GE0/1/1
    4.4.4.9/32         3/NULL         3.3.3.9         127.0.0.1       LoopBack0
   *4.4.4.9/32         Liberal/1026                   DS/3.3.3.9
    -------------------------------------------------------------------------------
    TOTAL: 7 Normal LSP(s) Found.
    TOTAL: 1 Liberal LSP(s) Found.
    TOTAL: 0 Frr LSP(s) Found.
    An asterisk (*) before an LSP means the LSP is not established
    An asterisk (*) before a Label means the USCB or DSCB is stale
    An asterisk (*) before an UpstreamPeer means the session is stale
    An asterisk (*) before a DS means the session is stale
    An asterisk (*) before a NextHop means the LSP is FRR LSP
   
   ```

#### Configuration Files

* LSRA configuration file
  
  ```
  #
  sysname LSRA
  #
  mpls lsr-id 3.3.3.9
  #
  mpls
  #
  mpls ldp
   #
   ipv4-family
    outbound peer 4.4.4.9 fec ip-prefix prefix1
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.2.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   ip address 10.1.3.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack0
   ip address 3.3.3.9 255.255.255.255
  #
  ospf 1
   area 0.0.0.0
    network 3.3.3.9 0.0.0.0
    network 10.1.2.0 0.0.0.255
    network 10.1.3.0 0.0.0.255
  #
  ip ip-prefix prefix1 index 10 permit 1.1.1.9 32
  #
  return
  ```
* LSRB configuration file
  
  ```
  #
  sysname LSRB
  #
  mpls lsr-id 2.2.2.9
  #
  mpls
  #
  mpls ldp
   #
   ipv4-family
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.2.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack0
   ip address 2.2.2.9 255.255.255.255
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.9 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.1.2.0 0.0.0.255
  #
  return 
  ```
* LSRC configuration file
  
  ```
  #
  sysname LSRC
  #
  mpls lsr-id 1.1.1.9
  #
  mpls
  #
  mpls ldp
   #
   ipv4-family
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack0
   ip address 1.1.1.9 255.255.255.255
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.9 0.0.0.0
    network 10.1.1.0 0.0.0.255
  #
  return
  
  ```
* DSLAM configuration file
  
  ```
  #
  sysname DSLAM
  #
  mpls lsr-id 4.4.4.9
  #
  mpls
  #
  mpls ldp
   #
   ipv4-family
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.3.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack0
   ip address 4.4.4.9 255.255.255.255
  #
  ospf 1
   area 0.0.0.0
    network 4.4.4.9 0.0.0.0
    network 10.1.3.0 0.0.0.255
  #
  return
  ```