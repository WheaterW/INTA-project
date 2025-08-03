Example for Establishing LSPs Through LDP
=========================================

This section provides an example for establishing LSPs using LDP. The configuration procedure involves establishing a local LDP session and modifying the policy for triggering the establishment of an LSP on each LSR.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172368565__fig_dc_vrp_ldp-p2p_cfg_004101), LSRA, LSRB, and LSRC all function as core devices or edge devices on a backbone network. On this network, after local LDP sessions are set up between LSRA and LSRB, and between LSRB and LSRC, each pair of LSRs can distribute labels to each other and establish LDP LSPs. MPLS services can be transmitted along the LSPs.

**Figure 1** Configuring a policy for triggering LDP LSP establishment![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE0/1/0 and GE0/2/0, respectively.


  
![](figure/en-us_image_0278892277.png)

#### Configuration Notes

During the configuration, note the following:

* Each LSR must have route entries that exactly match FECs for the LSPs to be established.
* By default, the triggering policy is **host**, allowing a device to use host IP routes with 32-bit addresses to trigger LDP LSP establishment.
* If the triggering policy is **all**, all IGP routes are used to trigger LDP LSP establishment. The device does not use public network BGP routes to trigger LDP LSP establishment.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure local LDP sessions.
2. Change the policy for triggering LDP LSP establishment on each LSR.

#### Data Preparation

To complete the configuration, you need the following data:

* IP address of each interface on each LSR (as shown in [Figure 1](#EN-US_TASK_0172368565__fig_dc_vrp_ldp-p2p_cfg_004101)), OSPF process ID, and area ID
* Policy for triggering LDP LSP establishment

#### Procedure

1. Configure an LDP LSP.
   
   
   
   After you complete the task described in [Example for Configuring Local LDP Sessions](dc_vrp_ldp-p2p_cfg_0039.html), each LSR uses the default LDP LSP triggering policy. That is, each LSR uses host IP routes with 32-bit addresses to trigger LDP LSP establishment.
   
   # Run the [**display mpls ldp lsp**](cmdqueryname=display+mpls+ldp+lsp) command on each LSR. The command output shows the LSR has successfully established LDP LSPs for all host routes.
   
   The following example uses the command output on LSRA.
   
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
    1.1.1.9/32         3/NULL         2.2.2.9         127.0.0.1        LoopBack1
   *1.1.1.9/32         Liberal/3                      DS/2.2.2.9
    2.2.2.9/32         NULL/3         -               10.1.1.2         GE0/1/0
    2.2.2.9/32         1024/3         2.2.2.9         10.1.1.2         GE0/1/0
    3.3.3.9/32         NULL/1025      -               10.1.1.2         GE0/1/0
    3.3.3.9/32         1025/1025      3.3.3.9         10.1.1.2         GE0/1/0     
    ------------------------------------------------------------------------------
    TOTAL: 5 Normal LSP(s) Found.
    TOTAL: 1 Liberal LSP(s) Found.
    TOTAL: 0 Frr LSP(s) Found.
    An asterisk (*) before an LSP means the LSP is not established
    An asterisk (*) before a Label means the USCB or DSCB is stale
    An asterisk (*) before an UpstreamPeer means the session is stale
    An asterisk (*) before a DS means the session is stale
    An asterisk (*) before a NextHop means the LSP is FRR LSP
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The default triggering policy is recommended, as this allows a device to use host IP routes with 32-bit addresses to trigger LDP LSP establishment. You can also perform the following steps to change the policy for triggering LDP LSP establishment as required.
2. Change the policy for triggering the establishment of LDP LSPs.
   
   
   
   Change the policy for triggering LDP LSP establishment to **all** on each LSR so that the LSR uses all static routes and IGP routes in the routing table to trigger LDP LSP establishment.
   
   # Configure LSRA.
   
   ```
   [~LSRA] mpls
   ```
   ```
   [~LSRA-mpls] lsp-trigger all
   ```
   ```
   [*LSRA-mpls] commit
   ```
   ```
   [~LSRA-mpls] quit
   ```
   
   # Configure LSRB.
   
   ```
   [~LSRB] mpls
   ```
   ```
   [~LSRB-mpls] lsp-trigger all
   ```
   ```
   [*LSRB-mpls] commit
   ```
   ```
   [~LSRB-mpls] quit
   ```
   
   # Configure LSRC.
   
   ```
   [~LSRC] mpls
   ```
   ```
   [~LSRC-mpls] lsp-trigger all
   ```
   ```
   [*LSRC-mpls] commit
   ```
   ```
   [~LSRC-mpls] quit
   ```
3. Verify the configuration.
   
   
   
   # After completing the configuration, run the [**display mpls ldp lsp**](cmdqueryname=display+mpls+ldp+lsp) command on each node to check information about LDP LSPs. The following example uses the command output on LSRA.
   
   ```
   [~LSRA] display mpls ldp lsp
   ```
   ```
    LDP LSP Information
    -------------------------------------------------------------------------------
    Flag after Out IF: (I) - RLFA Iterated LSP, (I*) - Normal and RLFA Iterated LSP
    -------------------------------------------------------------------------------
    DestAddress/Mask   In/OutLabel   UpstreamPeer    NextHop     OutInterface
    -------------------------------------------------------------------------------
    1.1.1.9/32         3/NULL        2.2.2.9         127.0.0.1   LoopBack1    
   *1.1.1.9/32         Liberal/3                     DS/2.2.2.9
    2.2.2.9/32         NULL/3        -               10.1.1.2    GE0/1/0    
    2.2.2.9/32         1024/3        2.2.2.9         10.1.1.2    GE0/1/0    
    3.3.3.9/32         NULL/1025     -               10.1.1.2    GE0/1/0    
    3.3.3.9/32         1025/1025     2.2.2.9         10.1.1.2    GE0/1/0    
    10.1.1.0/30        3/NULL        2.2.2.9         10.1.1.1    GE0/1/0    
   *10.1.1.0/30        Liberal/3                     DS/2.2.2.9
    10.2.1.0/30        NULL/3        -               10.1.1.2    GE0/1/0    
    10.2.1.0/30        1026/3        2.2.2.9         10.1.1.2    GE0/1/0    
    -------------------------------------------------------------------------------
    TOTAL: 8 Normal LSP(s) Found.
    TOTAL: 2 Liberal LSP(s) Found.
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
  ```
  ```
  sysname LSRA
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
   ip address 10.1.1.1 255.255.255.252
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
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 1.1.1.9 0.0.0.0
  ```
  ```
    network 10.1.1.0 0.0.0.3
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
   ip address 10.1.1.2 255.255.255.252
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
   ip address 10.2.1.1 255.255.255.252
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
    network 2.2.2.9 0.0.0.0
  ```
  ```
    network 10.1.1.0 0.0.0.3
  ```
  ```
    network 10.2.1.0 0.0.0.3
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
   ip address 10.2.1.2 255.255.255.252
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
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 3.3.3.9 0.0.0.0
  ```
  ```
    network 10.2.1.0 0.0.0.3
  ```
  ```
  #
  ```
  ```
  return
  ```