Example for Configuring Local LDP Sessions
==========================================

This section provides an example for configuring local LDP sessions. The configuration procedure involves enabling MPLS and MPLS LDP on each LSR and interface.

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0172368561__fig_dc_vrp_ldp-p2p_cfg_003901), LSRA, LSRB, and LSRC function as core or edge devices on a backbone network. Configure local LDP sessions for MPLS LDP services. The LSRs can then exchange labels to establish LDP LSPs.

**Figure 1** Networking diagram of configuring local LDP sessions![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE0/1/0 and GE0/2/0, respectively.


  
![](figure/en-us_image_0278890083.png)

#### Configuration Notes

During the configuration, note the following:

* An LSR ID must be configured before you run other MPLS commands.
* LSR IDs can only be manually configured, and do not have default values.
* Using the IP address of a reachable loopback interface on an LSR as the LSR ID is recommended.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IP address to each interface and configure OSPF to advertise the route to the network segment to which each interface is connected and the host route to each LSR ID.
2. Enable MPLS and MPLS LDP globally on each LSR.
3. Enable MPLS on the interfaces of each LSR.
4. Enable MPLS LDP on the interfaces of both ends of each local LDP session.

#### Data Preparation

To complete the configuration, you need the following data:

* IP address of each interface on each LSR (as shown in [Figure 1](#EN-US_TASK_0172368561__fig_dc_vrp_ldp-p2p_cfg_003901)), OSPF process ID, and area ID
* LSR ID of each node

#### Procedure

1. Assign an IP address to each interface and configure OSPF to advertise the route to the network segment to which each interface is connected and the host route to each LSR ID.
   
   
   
   Assign an IP address to each interface (as shown in [Figure 1](#EN-US_TASK_0172368561__fig_dc_vrp_ldp-p2p_cfg_003901)), including the loopback interfaces. Configure OSPF to advertise the route to the network segment to which each interface is connected and the host route to each LSR ID.
2. Enable MPLS and MPLS LDP globally on each LSR.
   
   
   
   # Configure LSRA.
   
   ```
   <LSRA> system-view 
   ```
   ```
   [~LSRA] mpls lsr-id 1.1.1.9
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
   [~LSRC] mpls lsr-id 3.3.3.9
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
3. Enable MPLS and MPLS LDP on the interfaces of each LSR.
   
   
   
   # Configure LSRA.
   
   ```
   [~LSRA] interface gigabitethernet 0/1/0
   ```
   ```
   [~LSRA-GigabitEthernet0/1/0] mpls
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
   [~LSRB] interface gigabitethernet 0/1/0
   ```
   ```
   [~LSRB-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*LSRB-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*LSRB-GigabitEthernet0/1/0] commit
   ```
   ```
   [~LSRB-GigabitEthernet0/1/0] quit
   ```
   ```
   [~LSRB] interface gigabitethernet 0/2/0
   ```
   ```
   [~LSRB-GigabitEthernet0/2/0] mpls
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
   
   # Configure LSRC.
   
   ```
   [~LSRC] interface gigabitethernet 0/1/0
   ```
   ```
   [*LSRC-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*LSRC-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*LSRC-GigabitEthernet0/1/0] commit
   ```
   ```
   [~LSRC-GigabitEthernet0/1/0] quit
   ```
4. Verify the configuration.
   
   
   
   # After completing the configuration, run the **display mpls ldp session** command on each node. The command output shows that the status of the local LDP session between LSRA and LSRB, or between LSRB and LSRC is **Operational**.
   
   The following example uses the command output on LSRA.
   
   ```
   <LSRA> display mpls ldp session
   ```
   ```
    LDP Session(s) in Public Network
    Codes: LAM(Label Advertisement Mode), SsnAge Unit(DDDD:HH:MM)
    An asterisk (*) before a session means the session is being deleted.
   --------------------------------------------------------------------------
    PeerID             Status      LAM  SsnRole  SsnAge       KASent/Rcv
   --------------------------------------------------------------------------
   2.2.2.9:0           Operational DU   Passive  0000:00:22   91/91
   --------------------------------------------------------------------------
   TOTAL: 1 Session(s) Found.
   
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