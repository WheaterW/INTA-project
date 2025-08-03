Example for Configuring Transit LSPs Through an IP Prefix List
==============================================================

This section provides an example for configuring transit LSPs. The configuration procedure involves establishing local LDP sessions and configuring an IP prefix list to filter routes on each transit LSR.

#### Networking Requirements

After MPLS LDP is enabled on each interface, LDP LSPs can be automatically established, including a great number of unnecessary transit LSPs, which wastes resources. On the network shown in [Figure 1](#EN-US_TASK_0172368566__fig_dc_vrp_ldp-p2p_cfg_004201), after a policy for triggering the establishment of transit LSPs is configured, LSRB only uses the routes to 4.4.4.4/32 to establish a transit LSP.

**Figure 1** Configuring a policy for triggering transit LSP establishment![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE0/1/0 and GE0/2/0, respectively.


  
![](figure/en-us_image_0279157581.png)

#### Configuration Notes

During the configuration, note the following:

By default, LDP establishes transit LSPs for all routes, without filtering them.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IP address to each interface and configure OSPF to advertise the route to the network segment to which each interface is connected and the host route to each LSR ID.
2. Configure an IP prefix list to limit the routes for which transit LSPs can be established.
3. Enable MPLS and MPLS LDP globally on each LSR and configure a policy of triggering LSP establishment.
4. Configure LSRB (transit node) to use the IP prefix list to limit the routes for which transit LSPs can be established.
5. Enable MPLS and MPLS LDP on each interface.

#### Data Preparation

To complete the configuration, you need the following data:

* IP address of each interface on each node (as shown in [Figure 1](#EN-US_TASK_0172368566__fig_dc_vrp_ldp-p2p_cfg_004201)), OSPF process ID, and area ID
* Policy for triggering LSP establishment
* IP prefix list name and the routes to be filtered on the transit node

#### Procedure

1. Assign an IP address to each interface and configure OSPF to advertise the route to the network segment to which each interface is connected and the host route to each LSR ID.
   
   
   
   # Assign an IP address to each interface (as shown in [Figure 1](#EN-US_TASK_0172368566__fig_dc_vrp_ldp-p2p_cfg_004201)), including the loopback interfaces. Configure OSPF to advertise the route to the network segment to which each interface is connected and the host route to each LSR ID.
2. Configure an IP prefix list on the transit node LSRB.
   
   
   
   # Configure an IP prefix list on LSRB to allow LSRB to establish a transit LSP only for the route 4.4.4.4/32 to LSRD.
   
   ```
   [~LSRB]ip ip-prefix FilterOnTransit permit 4.4.4.4 32
   ```
   ```
   [*LSRB]commit
   ```
3. Configure basic MPLS and MPLS LDP functions on each node and interface, and configure a policy for triggering LSP establishment.
   
   
   
   # Configure LSRA.
   
   ```
   [~LSRA] mpls lsr-id 1.1.1.1
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
   [*LSRA-mpls-ldp] quit
   ```
   ```
   [*LSRA] interface gigabitethernet 0/1/0
   ```
   ```
   [*LSRA-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*LSRA-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*LSRA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~LSRA-GigabitEthernet0/1/0] quit
   ```
   
   # Configure LSRB.
   
   ```
   [~LSRB] mpls lsr-id 2.2.2.2
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
   [*LSRB-mpls-ldp] propagate mapping for ip-prefix FilterOnTransit
   ```
   ```
   [*LSRB-mpls-ldp] quit
   ```
   ```
   [*LSRB] interface gigabitethernet 0/1/0
   ```
   ```
   [*LSRB-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*LSRB-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*LSRB-GigabitEthernet0/1/0] quit
   ```
   ```
   [*LSRB] interface gigabitethernet 0/2/0
   ```
   ```
   [*LSRB-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*LSRB-GigabitEthernet0/2/0] mpls ldp
   ```
   ```
   [*LSRB-GigabitEthernet0/2/0] commit
   ```
   ```
   [~LSRB-GigabitEthernet0/2/0] quit
   ```
   
   The configurations of LSRC and LSRD are similar to the configuration of LSRA.
4. Verify the configuration.
   
   
   
   Run the [**display mpls ldp lsp**](cmdqueryname=display+mpls+ldp+lsp) command to check LSP information.
   
   # Display LDP LSPs established on LSRA.
   
   ```
   [~LSRA] display mpls ldp lsp
   ```
   ```
    LDP LSP Information
    -------------------------------------------------------------------------------
    Flag after Out IF: (I) - RLFA Iterated LSP, (I*) - Normal and RLFA Iterated LSP
    -------------------------------------------------------------------------------
    DestAddress/Mask   In/OutLabel    UpstreamPeer    NextHop          OutInterface
    -------------------------------------------------------------------------------
    1.1.1.1/32         3/NULL         2.2.2.2         127.0.0.1        LoopBack1
    2.2.2.2/32         NULL/3         -               192.168.1.2      GE0/1/0
    2.2.2.2/32         1025/3         2.2.2.2         192.168.1.2      GE0/1/0
    4.4.4.4/32         NULL/1025      -               192.168.1.2      GE0/1/0
    4.4.4.4/32         1026/1026      4.4.4.4         192.168.1.2      GE0/1/0
    192.168.1.0/24     3/NULL         2.2.2.2         192.168.1.1      GE0/1/0
   *192.168.1.0/24     Liberal/26                     DS/2.2.2.2
    192.168.2.0/24     NULL/3         -               192.168.1.2      GE0/1/0
    192.168.2.0/24     1027/3         3.3.3.3         192.168.1.2      GE0/1/0
   --------------------------------------------------------------------------
    TOTAL: 8 Normal LSP(s) Found.
    TOTAL: 1 Liberal LSP(s) Found.
    TOTAL: 0 Frr LSP(s) Found.
    An asterisk (*) before an LSP means the LSP is not established
    An asterisk (*) before a Label means the USCB or DSCB is stale
    An asterisk (*) before an UpstreamPeer means the session is stale
    An asterisk (*) before a DS means the session is stale
    An asterisk (*) before a NextHop means the LSP is FRR LSP
   
   ```
   
   The command output on each node shows that the LDP LSP with LSRB as the transit node is established only for the route 4.4.4.4/32 and that other LDP LSPs not with LSRB as the transit node are established.

#### Configuration Files

* LSRA configuration file
  
  ```
  #
  ```
  ```
  sysname LSRA
  ```
  ```
  #
  ```
  ```
  mpls lsr-id 1.1.1.1
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
  mpls ldp
  ```
  ```
   #
   ipv4-family
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
   ip address 192.168.1.1 255.255.255.0
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
   ip address 1.1.1.1 255.255.255.255
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
    network 1.1.1.1 0.0.0.0
  ```
  ```
    network 192.168.1.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  return
  ```
* LSRB configuration file
  
  ```
  #
  ```
  ```
  sysname LSRB
  ```
  ```
  #
  ```
  ```
  mpls lsr-id 2.2.2.2
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
  mpls ldp
   #
   ipv4-family
    propagate mapping for ip-prefix FilterOnTransit
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
   ip address 192.168.1.2 255.255.255.0
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
   undo shutdown
  ```
  ```
   ip address 192.168.2.1 255.255.255.0
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
   ip address 2.2.2.2 255.255.255.255
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
    network 2.2.2.2 0.0.0.0
  ```
  ```
    network 192.168.1.0 0.0.0.255
  ```
  ```
    network 192.168.2.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  ip ip-prefix FilterOnTransit index 10 permit 4.4.4.4 32
  ```
  ```
  #
  ```
  ```
  return
  ```
* LSRC configuration file
  
  ```
  #
  ```
  ```
  sysname LSRC
  ```
  ```
  #
  ```
  ```
  mpls lsr-id 3.3.3.3
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
  mpls ldp
  ```
  ```
   #
   ipv4-family
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
   ip address 192.168.2.2 255.255.255.0
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
   undo shutdown
  ```
  ```
   ip address 192.168.3.1 255.255.255.0
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
   ip address 3.3.3.3 255.255.255.255
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
    network 3.3.3.3 0.0.0.0
  ```
  ```
    network 192.168.2.0 0.0.0.255
  ```
  ```
    network 192.168.3.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  return
  ```
* LSRD configuration file
  
  ```
  #
  ```
  ```
  sysname LSRD
  ```
  ```
  #
  ```
  ```
  mpls lsr-id 4.4.4.4
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
  mpls ldp
  ```
  ```
   #
   ipv4-family
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
   ip address 192.168.3.2 255.255.255.0
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
   ip address 4.4.4.4 255.255.255.255
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
    network 4.4.4.4 0.0.0.0
  ```
  ```
    network 192.168.3.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  Return
  ```