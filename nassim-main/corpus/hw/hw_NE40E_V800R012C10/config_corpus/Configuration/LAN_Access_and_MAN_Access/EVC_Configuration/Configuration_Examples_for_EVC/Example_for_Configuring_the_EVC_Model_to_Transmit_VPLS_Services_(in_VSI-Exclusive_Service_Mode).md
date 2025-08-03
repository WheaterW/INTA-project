Example for Configuring the EVC Model to Transmit VPLS Services (in VSI-Exclusive Service Mode)
===============================================================================================

This section provides an example for configuring the EVC model to transmit virtual private LAN service (VPLS) services. In this example, the EVC model allows end users to communicate using single-tagged packets through a VPLS network.

#### Networking Requirements

On a VPLS network, the packet encapsulation mode on an attachment circuit (AC) is determined by the user access mode, which can be Ethernet or VLAN. When being transmitted over the public network, packets encapsulated in the Ethernet mode cannot carry any VLAN tags, whereas packets encapsulated in the VLAN mode must carry VLAN tags.

In [Figure 1](#EN-US_TASK_0172363406__fig_dc_vrp_evc_cfg_002001), VPN1 services need access the VPLS network using Ethernet. To enable users in VPN1 to communicate with each other, the pop traffic behavior needs to be specified on the PEs so that the PEs remove tags from packets before forwarding them to the VPLS network.

**Figure 1** Configuring the EVC model to carry VPLS services![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 2, subinterface1.1, and subinterface1.2 in this example represent GE0/1/2, GE0/1/1.1, and GE0/1/1.2, respectively.


  
![](images/fig_dc_vrp_evc_cfg_002001.png)

#### Precautions

The VPLS network transmits services over pseudowires (PWs). PWs support packets encapsulated using a VSI. VSI encapsulation types are as follows:

* Ethernet: Untagged packets are transmitted on PWs.
* VLAN: Tagged packets are transmitted on PWs.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure Layer 2 forwarding on each CE.
   
   1. Create a VLAN on each CE and add the CE's downstream interface to the corresponding VLAN.
   2. Configure Layer 2 forwarding on the interface connecting each CE to the network so that a CE sends single-tagged packets to a PE.
2. Configure VPLS on each PE.
   
   1. Configure a routing protocol on PEs to implement network connectivity.
   2. Configure basic MPLS functions and MPLS LDP on PEs and establish MPLS LSPs.
   3. Enable MPLS L2VPN and global L2VPN on each PE.
   4. Create a VSI and configure Label Distribution Protocol (LDP) signaling on each PE, set VSI IDs used in PW signaling negotiation.
3. Configure the EVC model on each PE:
   1. Configure a bridge domain to forward services.
   2. Create an EVC Layer 2 sub-interface, add it to the bridge domain, and specify traffic encapsulation types and behaviors on the EVC Layer 2 sub-interface.
   3. Bind a bridge domain to a VSI so that an EVC model transmits VPLS services.

#### Data Preparation

To complete the configuration, you need the following data:

* User VLAN IDs
* Number of interfaces that connect CEs to users and connect CEs to PEs
* Number and IP addresses of interfaces connecting PEs
* VSI ID on PEs (that must have the same VSI ID), MPLS LSR IDs, VSI name, and names of interfaces bound to a VSI
* Bridge domain ID, traffic encapsulation types, and traffic behaviors


#### Procedure

1. Configure Layer 2 forwarding on each CE.
   
   
   
   # Configure CE1.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname CE1
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~CE1] vlan 10
   ```
   ```
   [*CE1-vlan10] quit
   ```
   ```
   [*CE1] interface gigabitethernet 0/1/1
   ```
   ```
   [*CE1-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*CE1-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*CE1-GigabitEthernet0/1/1] port link-type access
   ```
   ```
   [*CE1-GigabitEthernet0/1/1] port default vlan 10
   ```
   ```
   [*CE1-GigabitEthernet0/1/1] quit
   ```
   ```
   [*CE1] interface gigabitethernet 0/1/2
   ```
   ```
   [*CE1-GigabitEthernet0/1/2] undo shutdown
   ```
   ```
   [*CE1-GigabitEthernet0/1/2] portswitch
   ```
   ```
   [*CE1-GigabitEthernet0/1/2] port link-type trunk
   ```
   ```
   [*CE1-GigabitEthernet0/1/2] port trunk allow-pass vlan 10
   ```
   ```
   [*CE1-GigabitEthernet0/1/2] commit
   ```
   ```
   [~CE1-GigabitEthernet0/1/2] quit
   ```
   
   # Configure CE2.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname CE2
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~CE2] vlan 10
   ```
   ```
   [*CE2-vlan10] quit
   ```
   ```
   [*CE2] interface gigabitethernet 0/1/1
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] port link-type access
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] port default vlan 10
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] quit
   ```
   ```
   [*CE2] interface gigabitethernet 0/1/2
   ```
   ```
   [*CE2-GigabitEthernet0/1/2] undo shutdown
   ```
   ```
   [*CE2-GigabitEthernet0/1/2] portswitch
   ```
   ```
   [*CE2-GigabitEthernet0/1/2] port link-type trunk
   ```
   ```
   [*CE2-GigabitEthernet0/1/2] port trunk allow-pass vlan 10
   ```
   ```
   [*CE2-GigabitEthernet0/1/2] commit
   ```
   ```
   [~CE2-GigabitEthernet0/1/2] quit
   ```
2. Configure VPLS.
   
   
   1. Configure OSPF on each PE.
      
      Assign an IP address to each PE interface. After OSPF is enabled, the 32-bit loopback address of each PE must be advertised.
      
      # Configure PE1.
      
      ```
      <HUAWEI> system-view
      ```
      ```
      [~HUAWEI] sysname PE1
      ```
      ```
      [*HUAWEI] commit
      ```
      ```
      [~PE1] interface loopback 1
      ```
      ```
      [*PE1-LoopBack1] ip address 1.1.1.9 32
      ```
      ```
      [*PE1-LoopBack1] quit
      ```
      ```
      [*PE1] interface gigabitethernet 0/1/2
      ```
      ```
      [*PE1-GigabitEthernet0/1/2] undo shutdown
      ```
      ```
      [*PE1-GigabitEthernet0/1/2] ip address 10.1.1.1 24
      ```
      ```
      [*PE1-GigabitEthernet0/1/2] quit
      ```
      ```
      [*PE1] ospf
      ```
      ```
      [*PE1-ospf-1] area 0
      ```
      ```
      [*PE1-ospf-1-area-0.0.0.0] network 1.1.1.9 0.0.0.0
      ```
      ```
      [*PE1-ospf-1-area-0.0.0.0] network 10.1.1.0 0.0.0.255
      ```
      ```
      [*PE1-ospf-1-area-0.0.0.0] quit
      ```
      ```
      [*PE1-ospf-1] quit
      ```
      ```
      [*PE1] commit
      ```
      
      # Configure PE2.
      
      ```
      <HUAWEI> system-view
      ```
      ```
      [~HUAWEI] sysname PE2
      ```
      ```
      [*HUAWEI] commit
      ```
      ```
      [~PE2] interface loopback 1
      ```
      ```
      [*PE2-LoopBack1] ip address 2.2.2.9 32
      ```
      ```
      [*PE2-LoopBack1] quit
      ```
      ```
      [*PE2] interface gigabitethernet 0/1/2
      ```
      ```
      [*PE2-GigabitEthernet0/1/2] undo shutdown
      ```
      ```
      [*PE2-GigabitEthernet0/1/2] ip address 10.1.1.2 24
      ```
      ```
      [*PE2-GigabitEthernet0/1/2] quit
      ```
      ```
      [*PE2] ospf
      ```
      ```
      [*PE2-ospf-1] area 0
      ```
      ```
      [*PE2-ospf-1-area-0.0.0.0] network 2.2.2.9 0.0.0.0
      ```
      ```
      [*PE2-ospf-1-area-0.0.0.0] network 10.1.1.0 0.0.0.255
      ```
      ```
      [*PE2-ospf-1-area-0.0.0.0] quit
      ```
      ```
      [*PE2-ospf-1] quit
      ```
      ```
      [*PE2] commit
      ```
      
      After the configuration is complete, PE1 and PE2 have learned the routes destined for Loopback1 interface of each other, and PE1 and PE2 can successfully ping each other.
      
      The following example uses the command output on PE1.
      
      ```
      [~PE1] display ip routing-table
      ```
      ```
      Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
      ------------------------------------------------------------------------------
      Routing Table : _public_
               Destinations : 9        Routes : 9
      
      Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface
      
              1.1.1.9/32  Direct  0    0             D  127.0.0.1       LoopBack1
              2.2.2.9/32  OSPF    10   1             D  10.1.1.2        GigabitEthernet0/1/2
             10.1.1.0/24  Direct  0    0             D  10.1.1.1        GigabitEthernet0/1/2
             10.1.1.1/32  Direct  0    0             D  127.0.0.1       GigabitEthernet0/1/2
           10.1.1.255/32  Direct  0    0             D  127.0.0.1       GigabitEthernet0/1/2
            127.0.0.0/8   Direct  0    0             D  127.0.0.1       InLoopBack0
            127.0.0.1/32  Direct  0    0             D  127.0.0.1       InLoopBack0
      127.255.255.255/32  Direct  0    0             D  127.0.0.1       InLoopBack0
      255.255.255.255/32  Direct  0    0             D  127.0.0.1       InLoopBack0
      ```
   2. Configure basic MPLS functions and LDP.
      
      # Configure PE1.
      
      ```
      [~PE1] mpls lsr-id 1.1.1.9
      ```
      ```
      [*PE1] mpls
      ```
      ```
      [*PE1-mpls] quit
      ```
      ```
      [*PE1] mpls ldp
      ```
      ```
      [*PE1-mpls-ldp] quit
      ```
      ```
      [*PE1] interface gigabitethernet 0/1/2
      ```
      ```
      [*PE1-GigabitEthernet0/1/2] mpls
      ```
      ```
      [*PE1-GigabitEthernet0/1/2] mpls ldp
      ```
      ```
      [*PE1-GigabitEthernet0/1/2] quit
      ```
      ```
      [*PE1] commit
      ```
      
      # Configure PE2.
      
      ```
      [~PE2] mpls lsr-id 2.2.2.9
      ```
      ```
      [*PE2] mpls
      ```
      ```
      [*PE2-mpls] quit
      ```
      ```
      [*PE2] mpls ldp
      ```
      ```
      [*PE2-mpls-ldp] quit
      ```
      ```
      [*PE2] interface gigabitethernet 0/1/2
      ```
      ```
      [*PE2-GigabitEthernet0/1/2] mpls
      ```
      ```
      [*PE2-GigabitEthernet0/1/2] mpls ldp
      ```
      ```
      [*PE2-GigabitEthernet0/1/2] quit
      ```
      ```
      [*PE2] commit
      ```
      
      After completing the preceding configuration, run the **display mpls ldp session** command on each PE. The command output shows that the LDP session is in the **Operational** state, indicating that the LDP session between PE1 and PE2 has been established.
      
      ```
      [~PE1] display mpls ldp session
      ```
      ```
       LDP Session(s) in Public Network
       Codes: LAM(Label Advertisement Mode), SsnAge Unit(DDDD:HH:MM)
       An asterisk (*) before a session means the session is being deleted.
      --------------------------------------------------------------------------
       PeerID             Status      LAM  SsnRole  SsnAge       KASent/Rcv
      --------------------------------------------------------------------------
       2.2.2.9:0          Operational DU   Passive  0000:00:00   1/1
      --------------------------------------------------------------------------
      TOTAL: 1 Session(s) Found.
      ```
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      If the PEs are indirectly connected, run the **mpls ldp remote-peer** and **remote-ip** commands to create a remote LDP session between the PEs.
   3. Enable MPLS L2VPN.
      
      # Configure PE1.
      
      ```
      [~PE1] mpls l2vpn
      ```
      ```
      [*PE1-l2vpn] quit
      ```
      ```
      [*PE1] commit
      ```
      
      # Configure PE2.
      
      ```
      [~PE2] mpls l2vpn
      ```
      ```
      [*PE2-l2vpn] quit
      ```
      ```
      [*PE2] commit
      ```
   4. Create a VSI and configure LDP signaling.
      
      # Configure PE1.
      
      ```
      [~PE1] vsi ldp1 bd-mode
      ```
      ```
      [*PE1-vsi-ldp1] encapsulation ethernet
      ```
      ```
      [*PE1-vsi-ldp1] pwsignal ldp
      ```
      ```
      [*PE1-vsi-ldp1-ldp] vsi-id 2
      ```
      ```
      [*PE1-vsi-ldp1-ldp] peer 2.2.2.9
      ```
      ```
      [*PE1-vsi-ldp1-ldp] quit
      ```
      ```
      [*PE1-vsi-ldp1] quit
      ```
      ```
      [*PE1] commit
      ```
      
      # Configure PE2.
      
      ```
      [~PE2] vsi ldp1 bd-mode
      ```
      ```
      [*PE2-vsi-ldp1] encapsulation ethernet
      ```
      ```
      [*PE2-vsi-ldp1] pwsignal ldp
      ```
      ```
      [*PE2-vsi-ldp1-ldp] vsi-id 2
      ```
      ```
      [*PE2-vsi-ldp1-ldp] peer 1.1.1.9
      ```
      ```
      [*PE2-vsi-ldp1-ldp] quit
      ```
      ```
      [*PE2-vsi-ldp1] quit
      ```
      ```
      [*PE2] commit
      ```
3. Establish the EVC model.
   
   
   1. Configure a bridge domain on each PE.
      
      # Configure PE1.
      
      ```
      [~PE1] bridge-domain 10
      ```
      ```
      [*PE1-bd10] quit
      ```
      
      # Configure PE2.
      
      ```
      [~PE2] bridge-domain 10
      ```
      ```
      [*PE2-bd10] quit
      ```
   2. Create an EVC Layer 2 sub-interface, add it to the bridge domain, and specify traffic encapsulation types and behaviors on the EVC Layer 2 sub-interface.
      
      # Configure PE1.
      
      ```
      [*PE1] interface gigabitethernet 0/1/1
      ```
      ```
      [*PE1-GigabitEthernet0/1/1] undo shutdown
      ```
      ```
      [*PE1-GigabitEthernet0/1/1] quit
      ```
      ```
      [*PE1] interface gigabitethernet 0/1/1.1 mode l2
      ```
      ```
      [*PE1-GigabitEthernet0/1/1.1] encapsulation dot1q vid 10
      ```
      ```
      [*PE1-GigabitEthernet0/1/1.1] rewrite pop single
      ```
      ```
      [*PE1-GigabitEthernet0/1/1.1] bridge-domain 10
      ```
      ```
      [*PE1-GigabitEthernet0/1/1.1] commit
      ```
      ```
      [~PE1-GigabitEthernet0/1/1] quit
      ```
      
      # Configure PE2.
      
      ```
      [~PE2] interface gigabitethernet 0/1/1
      ```
      ```
      [*PE2-GigabitEthernet0/1/1] undo shutdown
      ```
      ```
      [*PE2-GigabitEthernet0/1/1] quit
      ```
      ```
      [*PE2] interface gigabitethernet 0/1/1.1 mode l2
      ```
      ```
      [*PE2-GigabitEthernet0/1/1.1] encapsulation dot1q vid 10
      ```
      ```
      [*PE2-GigabitEthernet0/1/1.1] rewrite pop single
      ```
      ```
      [*PE2-GigabitEthernet0/1/1.1] bridge-domain 10
      ```
      ```
      [*PE2-GigabitEthernet0/1/1.1] commit
      ```
      ```
      [~PE2-GigabitEthernet0/1/1] quit
      ```
   3. Bind the bridge domain to the VSI.
      
      # Configure PE1.
      
      ```
      [~PE1] bridge-domain 10
      ```
      ```
      [*PE1-bd10] l2 binding vsi ldp1
      ```
      ```
      [*PE1-bd10] commit
      ```
      ```
      [~PE1] quit
      ```
      
      # Configure PE2.
      
      ```
      [~PE2] bridge-domain 10
      ```
      ```
      [*PE2-bd10] l2 binding vsi ldp1
      ```
      ```
      [*PE2-bd10] commit
      ```
      ```
      [~PE2] quit
      ```
4. Verify the configuration.
   
   
   
   After completing the configuration, run the [**display bridge-domain**](cmdqueryname=display+bridge-domain) command. The command output shows the BD to which an EVC Layer 2 sub-interface belongs and the BD status. The following example uses the command output on PE1.
   
   ```
   [~PE1] display bridge-domain
   ```
   ```
   The total number of bridge-domains is : 1
   --------------------------------------------------------------------------------
   MAC_LRN: MAC learning;         STAT: Statistics;         SPLIT: Split-horizon;
   BC: Broadcast;                 MC: Unknown multicast;    UC: Unknown unicast;
   *down: Administratively down;  FWD: Forward;             DSD: Discard;
   --------------------------------------------------------------------------------
   
   BDID  State MAC-LRN STAT    BC  MC  UC  SPLIT   Description
   --------------------------------------------------------------------------------
   10    up    enable  disable FWD FWD FWD disable
   ```
   
   Run the [**display ethernet uni information**](cmdqueryname=display+ethernet+uni+information) command. The command output shows the traffic encapsulation type and behavior configured on an EVC Layer 2 sub-interface. The following example uses the command output on PE2.
   
   ```
   [~PE2] display ethernet uni information
   ```
   ```
     GigabitEthernet0/1/1.1
       Total encapsulation number: 1
         encapsulation dot1q vid 10
       Rewrite pop single
       Bridge-domain 10
   ```
   
   Run the **display vsi name ldp1 verbose** command. The command output shows that a PW for a VSI named **ldp1** has been established between PE1 and PE2, and the VSI status is **Up**. The following example uses the command output on PE1.
   
   ```
   [~PE1] display vsi name ldp1 verbose
   ```
   ```
   ***VSI Name               : ldp1
       Administrator VSI      : no
       Isolate Spoken         : disable
       VSI Index              : 2
       PW Signaling           : ldp
       Member Discovery Style : --
       Bridge-domain Mode     : enable
       PW MAC Learn Style     : qualify
       Encapsulation Type     : ethernet
       MTU                    : 1500
       Ignore AcState         : disable
       P2P VSI                : disable
       Create Time            : 0 days, 0 hours, 1 minutes, 56 seconds
       VSI State              : up
       Resource Status        : --
   
       VSI ID                 : 2
      *Peer Router ID         : 2.2.2.9
       primary or secondary   : primary
       ignore-standby-state   : no
       VC Label               : 32830
       Peer Type              : dynamic
       Session                : up
       Tunnel ID              : 0x0000000001004c4b42
       Broadcast Tunnel ID    : --
       Broad BackupTunnel ID  : --
       CKey                   : 33
       NKey                   : 1409286261
       Stp Enable             : 0
       PwIndex                : 33
       Control Word           : disable
   
       Access bridge-domain   : bridge-domain 10
   
     **PW Information:
   
      *Peer Ip Address        : 2.2.2.9
       PW State               : up
       Local VC Label         : 32830
       Remote VC Label        : 32831
       Remote Control Word    : disable
       PW Type                : label
       Tunnel ID              : 0x0000000001004c4b42
       Broadcast Tunnel ID    : --
       Broad BackupTunnel ID  : --
       Ckey                   : 33
       Nkey                   : 1409286261
       Main PW Token          : 0x0
       Slave PW Token         : 0x0
       Tnl Type               : ldp
       OutInterface           : GE0/1/2
       Backup OutInterface    : --
       Stp Enable             : 0
       Mac Flapping           : 0
       PW Last Up Time        : 1976/12/04 00:05:59
       PW Total Up Time       : 0 days, 0 hours, 0 minutes, 17 seconds
   ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  mpls lsr-id 1.1.1.9
  #
  mpls
  #
  mpls l2vpn
  #
  vsi ldp1 bd-mode
   pwsignal ldp
    vsi-id 2
    peer 2.2.2.9
   encapsulation ethernet
  #
  bridge-domain 10
   l2 binding vsi ldp1
  #
  mpls ldp
  #
  interface loopback 1
   ip address 1.1.1.9 255.255.255.255
  #
  interface GigabitEthernet0/1/1
   undo shutdown
  #
  interface GigabitEthernet0/1/1.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
   bridge-domain 10
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.9 0.0.0.0
    network 10.1.1.0 0.0.0.255
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  mpls lsr-id 2.2.2.9
  #
  mpls
  #
  mpls l2vpn
  #
  vsi ldp1 bd-mode
   pwsignal ldp
    vsi-id 2
    peer 1.1.1.9
   encapsulation ethernet
  #
  bridge-domain 10
   l2 binding vsi ldp1
  #
  mpls ldp
  #
  interface loopback 1
   ip address 2.2.2.9 255.255.255.255
  #
  interface GigabitEthernet0/1/1
   undo shutdown
  #
  interface GigabitEthernet0/1/1.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
   bridge-domain 10
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.9 0.0.0.0
    network 10.1.1.0 0.0.0.255
  #
  return
  ```
* CE1 configuration file
  
  ```
  #
  sysname CE1
  #
  vlan 10
  #
  interface GigabitEthernet0/1/1
   portswitch
   undo shutdown
   port link-type access
   port default vlan 10
  #
  interface GigabitEthernet0/1/2
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
  vlan 10
  #
  interface GigabitEthernet0/1/1
   portswitch
   undo shutdown
   port link-type access
   port default vlan 10
  #
  interface GigabitEthernet0/1/2
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 10
  #
  return
  ```