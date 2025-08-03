Example for Configuring an LDP Inbound Policy
=============================================

This section provides an example for configuring an LDP inbound policy. The configuration procedure involves enabling MPLS and MPLS LDP globally.

#### Networking Requirements

MPLS LDP services are deployed on the network shown in [Figure 1](#EN-US_TASK_0172368569__fig_dc_vrp_ldp-p2p_cfg_204801). LSRD is a low-performance DSLAM for user access. By default, LSRD receives Label Mapping messages from all peers and uses the routing information in these messages to establish a large number of LSPs. As a result, memory on LSRD is overused and LSRD is overburdened. Configure an LDP inbound policy to allow LSRD to receive only Label Mapping messages destined for LSRC. This ensures that LSRD establishes LSPs only to LSRC, reducing resource consumption.

**Figure 1** Configuring an LDP inbound policy![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/1/0, GE 0/1/1, and GE 0/1/2, respectively.


  
![](images/fig_dc_vrp_ldp-p2p_cfg_204801.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IP address to each interface, including the loopback interface on each node.
2. Configure OSPF to advertise the route to the network segment of each interface and to advertise the host route to each LSR ID.
3. Enable MPLS and MPLS LDP on each node and interfaces.
4. Configure an LDP inbound policy.

#### Data Preparation

To complete the configuration, you need the following data:

* IP address of each interface on each LSR (as shown in [Figure 1](#EN-US_TASK_0172368569__fig_dc_vrp_ldp-p2p_cfg_204801)), OSPF process ID, and area ID
* LSR ID of each node

#### Procedure

1. Assign an IP address to each interface and configure an IGP.
   
   
   
   Assign an IP address and mask to each interface (as shown in [Figure 1](#EN-US_TASK_0172368569__fig_dc_vrp_ldp-p2p_cfg_204801)), including the loopback interfaces. Configure OSPF to advertise the route to the network segment to which each interface is connected and the host route to each LSR ID.
2. Enable MPLS and MPLS LDP globally and on the interfaces of each node.
   
   
   
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
   [*LSRA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*LSRA] commit
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
   [*LSRB] interface gigabitethernet 0/1/1
   ```
   ```
   [*LSRB-GigabitEthernet0/1/1] mpls
   ```
   ```
   [*LSRB-GigabitEthernet0/1/1] mpls ldp
   ```
   ```
   [*LSRB-GigabitEthernet0/1/1] quit
   ```
   ```
   [*LSRB] interface gigabitethernet 0/1/2
   ```
   ```
   [*LSRB-GigabitEthernet0/1/2] mpls
   ```
   ```
   [*LSRB-GigabitEthernet0/1/2] mpls ldp
   ```
   ```
   [*LSRB-GigabitEthernet0/1/2] quit
   ```
   ```
   [*LSRB] commit
   ```
   
   # Configure LSRC.
   
   ```
   [~LSRC] mpls lsr-id 3.3.3.3
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
   [*LSRC-mpls-ldp] quit
   ```
   ```
   [*LSRC] interface gigabitethernet 0/1/0
   ```
   ```
   [*LSRC-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*LSRC-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*LSRC-GigabitEthernet0/1/0] quit
   ```
   ```
   [*LSRC] commit
   ```
   
   # Configure LSRD.
   
   ```
   [~LSRD] mpls lsr-id 4.4.4.4
   ```
   ```
   [*LSRD] mpls
   ```
   ```
   [*LSRD-mpls] quit
   ```
   ```
   [*LSRD] mpls ldp
   ```
   ```
   [*LSRD-mpls-ldp] quit
   ```
   ```
   [*LSRD] interface gigabitethernet 0/1/0
   ```
   ```
   [*LSRD-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*LSRD-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*LSRD-GigabitEthernet0/1/0] quit
   ```
   ```
   [*LSRD] commit
   ```
   
   # After completing the preceding configuration, run the [**display mpls lsp**](cmdqueryname=display+mpls+lsp) command on LSRD to check information about established LSPs.
   
   ```
   [~LSRD] display mpls lsp
   ```
   ```
   Flag after Out IF: (I) - RLFA Iterated LSP, (I*) - Normal and RLFA Iterated LSP 
   Flag after LDP FRR: (L) - Logic FRR LSP
   -------------------------------------------------------------------------------
                    LSP Information: LDP LSP
   -------------------------------------------------------------------------------
   FEC                In/Out Label    In/Out IF                      Vrf Name
   1.1.1.1/32         NULL/32829      -/GE0/1/0                     
   1.1.1.1/32         32828/32829     -/GE0/1/0                     
   2.2.2.2/32         NULL/3          -/GE0/1/0                     
   2.2.2.2/32         32829/3         -/GE0/1/0                     
   3.3.3.3/32         NULL/32830      -/GE0/1/0                     
   3.3.3.3/32         32830/32830     -/GE0/1/0                     
   4.4.4.4/32         3/NULL          -/-  
   ```
   
   The command output shows that LSPs to LSRA, LSRB, and LSRC have been established on LSRD.
3. Configure an LDP inbound policy.
   
   
   
   # Configure an IP prefix list on LSRD to permit only the routes to LSRC.
   
   ```
   [~LSRD] ip ip-prefix prefix1 permit 3.3.3.3 32
   ```
   ```
   [*LSRD] commit
   ```
   
   # Configure an inbound policy on LSRD to allow LSRD to receive Label Mapping messages for the routes only to LSRC.
   
   ```
   [~LSRD] mpls ldp
   ```
   ```
   [*LSRD-mpls-ldp] ipv4-family
   ```
   ```
   [*LSRD-mpls-ldp-ipv4] inbound peer 2.2.2.2 fec ip-prefix prefix1
   ```
   ```
   [*LSRD-mpls-ldp-ipv4] quit
   ```
   ```
   [*LSRD-mpls-ldp] quit
   ```
   ```
   [*LSRD] commit
   ```
4. Verify the configuration.
   
   
   
   After completing the preceding configuration, run the [**display mpls lsp**](cmdqueryname=display+mpls+lsp) command on LSRD. The command output shows that only an LSP to LSRC is established.
   
   ```
   [~LSRD] display mpls lsp
   ```
   ```
   Flag after Out IF: (I) - RLFA Iterated LSP, (I*) - Normal and RLFA Iterated LSP 
   Flag after LDP FRR: (L) - Logic FRR LSP
   -------------------------------------------------------------------------------
                    LSP Information: LDP LSP
   -------------------------------------------------------------------------------
   FEC                In/Out Label    In/Out IF                      Vrf Name
   3.3.3.3/32         NULL/32830      -/GE0/1/0                     
   3.3.3.3/32         32830/32830     -/GE0/1/0                     
   4.4.4.4/32         3/NULL          -/-  
   ```

#### Configuration Files

* LSRA configuration file
  
  ```
  #
  sysname LSRA
  #
  mpls lsr-id 1.1.1.1
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 10.1.1.0 0.0.0.255
  #
  return
  ```
* LSRB configuration file
  
  ```
  #
  sysname LSRB
  #
  mpls lsr-id 2.2.2.2
   mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.2.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.1.3.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.1.2.0 0.0.0.255
    network 10.1.3.0 0.0.0.255
  #
  return
  ```
* LSRC configuration file
  
  ```
  #
  sysname LSRC
  #
  mpls lsr-id 3.3.3.3
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.2.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
  #
  ospf 1
   area 0.0.0.0
    network 3.3.3.3 0.0.0.0
    network 10.1.2.0 0.0.0.255
  #
  return
  ```
* LSRD configuration file
  
  ```
  #
  sysname LSRD
  #
  mpls lsr-id 4.4.4.4
  mpls
  #
  mpls ldp
   ipv4-family
    inbound peer 2.2.2.2 fec ip-prefix prefix1
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.3.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 4.4.4.4 255.255.255.255
  #
  ospf 1
   area 0.0.0.0
    network 4.4.4.4 0.0.0.0
    network 10.1.3.0 0.0.0.255
  #
  ip ip-prefix prefix1 index 10 permit 3.3.3.3 32
  #
  return
  ```