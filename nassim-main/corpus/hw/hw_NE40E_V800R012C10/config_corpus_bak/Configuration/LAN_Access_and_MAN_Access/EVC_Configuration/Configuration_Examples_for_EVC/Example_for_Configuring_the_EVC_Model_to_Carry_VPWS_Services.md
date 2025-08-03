Example for Configuring the EVC Model to Carry VPWS Services
============================================================

This section provides an example for configuring the EVC model to carry VPWS services. In this example, the EVC model allows end users to communicate using single-tagged packets through a VPWS network.

#### Networking Requirements

In the traditional service model supported by the NE40E, common sub-interfaces (VLAN type), dot1q VLAN tag termination sub-interfaces, or QinQ VLAN tag termination sub-interfaces are created on the user-side interfaces of PEs to access the carrier network through VPWS. In actual networking, multiple access modes may be used between Layer 2 devices. EVC provides a unified Layer 2 service bearer model and configuration model. This implementation facilitates network planning and management, cutting down enterprise costs.

On the network shown in [Figure 1](#EN-US_TASK_0172363411__fig_dc_vrp_evc_cfg_002801), VPN1 services are sent to a VPWS network using the Ethernet technique. To enable users in VPN1 to communicate with each other, specify the pop traffic behavior on the PE so that the PE removes VLAN tags from packets before forwarding them to the VPWS network.

**Figure 1** Configuring the EVC model to carry VPWS services![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, subinterface1.1, and interface2 represent GE0/1/0, GE0/1/0.1, and GE0/2/0, respectively.


  
![](images/fig_dc_vrp_evc_cfg_002801.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure Layer 2 forwarding on each CE.
   
   1. Create a VLAN on each CE and add the CE's downstream interface to the corresponding VLAN.
   2. Configure Layer 2 forwarding on the interface connecting each CE to the network so that a CE sends single-tagged packets to a PE.
2. Configure VPWS on each PE.
   
   1. Configure a routing protocol on PEs to implement network connectivity.
   2. Configure basic MPLS functions and MPLS LDP on PEs and establish MPLS LSPs.
   3. Enable MPLS L2VPN on each PE and enable L2VPN globally.
   4. Configure LDP VPWS on each PE.
3. Configure the EVC model on each PE:
   1. Create an EVC Layer 2 sub-interface and specify the traffic encapsulation type and behavior on the Layer 2 sub-interface for service access.
   2. Configure VPWS on the EVC Layer 2 sub-interface.

#### Data Preparation

To complete the configuration, you need the following data:

* User VLAN ID
* Numbers of interfaces that connect CEs to the user side and connect CEs to PEs
* Number and IP addresses of interfaces connecting PEs
* MPLS LSR IDs of PEs
* Traffic encapsulation type and behavior


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
   [*CE1] interface gigabitethernet 0/1/0
   ```
   ```
   [*CE1-GigabitEthernet0/1/0] portswitch
   ```
   ```
   [*CE1-GigabitEthernet0/1/0] port link-type trunk
   ```
   ```
   [*CE1-GigabitEthernet0/1/0] port trunk allow-pass vlan 10 
   ```
   ```
   [*CE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*CE1] interface gigabitethernet 0/2/0
   ```
   ```
   [*CE1-GigabitEthernet0/2/0] portswitch
   ```
   ```
   [*CE1-GigabitEthernet0/2/0] port link-type trunk
   ```
   ```
   [*CE1-GigabitEthernet0/2/0] port trunk allow-pass vlan 10
   ```
   ```
   [*CE1-GigabitEthernet0/2/0] quit
   ```
   ```
   [*CE1] commit
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
   [*CE2] interface gigabitethernet 0/1/0
   ```
   ```
   [*CE2-GigabitEthernet0/1/0] portswitch
   ```
   ```
   [*CE2-GigabitEthernet0/1/0] port link-type trunk
   ```
   ```
   [*CE2-GigabitEthernet0/1/0] port trunk allow-pass vlan 10
   ```
   ```
   [*CE2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*CE2] interface gigabitethernet 0/2/0
   ```
   ```
   [*CE2-GigabitEthernet0/2/0] portswitch
   ```
   ```
   [*CE2-GigabitEthernet0/2/0] port link-type trunk
   ```
   ```
   [*CE2-GigabitEthernet0/2/0] port trunk allow-pass vlan 10
   ```
   ```
   [*CE2-GigabitEthernet0/2/0] quit
   ```
   ```
   [*CE2] commit
   ```
2. Establish the EVC model.
   
   
   1. Create an EVC Layer 2 sub-interface and specify the traffic encapsulation type and behavior on the Layer 2 sub-interface.
      
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
      [~PE1] interface gigabitethernet 0/1/0.1 mode l2
      ```
      ```
      [*PE1-GigabitEthernet0/1/0.1] encapsulation dot1q vid 10
      ```
      ```
      [*PE1-GigabitEthernet0/1/0.1] rewrite pop single
      ```
      ```
      [*PE1-GigabitEthernet0/1/0.1] quit
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
      [~PE2] interface gigabitethernet 0/1/0.1 mode l2
      ```
      ```
      [*PE2-GigabitEthernet0/1/0.1] encapsulation dot1q vid 10
      ```
      ```
      [*PE2-GigabitEthernet0/1/0.1] rewrite pop single
      ```
      ```
      [*PE2-GigabitEthernet0/1/0.1] quit
      ```
      ```
      [*PE2] commit
      ```
3. Configure LDP VPWS.
   
   
   1. Configure OSPF on each PE.
      
      Assign an IP address to each PE interface. After OSPF is enabled, the 32-bit loopback address of each PE must be advertised.
      
      # Configure PE1.
      
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
      [*PE1] interface gigabitethernet 0/2/0
      ```
      ```
      [*PE1-GigabitEthernet0/2/0] ip address 10.1.1.1 24
      ```
      ```
      [*PE1-GigabitEthernet0/2/0] quit
      ```
      ```
      [*PE1] ospf 1
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
      [~PE2] interface loopback 1
      ```
      ```
      [*PE2-LoopBack1] ip address 2.2.2.9 32
      ```
      ```
      [*PE2-LoopBack1] quit
      ```
      ```
      [*PE2] interface gigabitethernet 0/2/0
      ```
      ```
      [*PE2-GigabitEthernet0/2/0] ip address 10.1.1.2 24
      ```
      ```
      [*PE2-GigabitEthernet0/2/0] quit
      ```
      ```
      [*PE2] ospf 1
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
      
      After completing the configuration, run the **display ip routing-table** command on each PE. The command output shows that OSPF-capable PE1 and PE2 have discovered routes to each other's loopback 1 interface and the two PEs can ping each other.
      
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
              2.2.2.9/32  OSPF    10   1             D  10.1.1.2        GigabitEthernet0/2/0
             10.1.1.0/24  Direct  0    0             D  10.1.1.1        GigabitEthernet0/2/0
             10.1.1.1/32  Direct  0    0             D  127.0.0.1       GigabitEthernet0/2/0
           10.1.1.255/32  Direct  0    0             D  127.0.0.1       GigabitEthernet0/2/0
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
      [*PE1] interface gigabitethernet 0/2/0
      ```
      ```
      [*PE1-GigabitEthernet0/2/0] mpls
      ```
      ```
      [*PE1-GigabitEthernet0/2/0] mpls ldp
      ```
      ```
      [*PE1-GigabitEthernet0/2/0] quit
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
      [*PE2] interface gigabitethernet 0/2/0
      ```
      ```
      [*PE2-GigabitEthernet0/2/0] mpls
      ```
      ```
      [*PE2-GigabitEthernet0/2/0] mpls ldp
      ```
      ```
      [*PE2-GigabitEthernet0/2/0] quit
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
       2.2.2.9:0        Operational  DU   Passive  0000:00:00   1/1
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
   4. Configure LDP VPWS.
      
      # Configure PE1.
      
      ```
      [~PE1] interface gigabitethernet 0/1/0.1
      ```
      ```
      [*PE1-GigabitEthernet0/1/0.1] mpls l2vc 2.2.2.9 100 raw
      ```
      ```
      [*PE1-GigabitEthernet0/1/0.1] quit
      ```
      ```
      [*PE1] commit
      ```
      
      # Configure PE2.
      
      ```
      [~PE2] interface gigabitethernet 0/1/0.1
      ```
      ```
      [*PE2-GigabitEthernet0/1/0.1] mpls l2vc 1.1.1.9 100 raw
      ```
      ```
      [*PE2-GigabitEthernet0/1/0.1] quit
      ```
      ```
      [*PE2] commit
      ```
4. Verify the configuration.
   
   
   
   Run the [**display ethernet uni information**](cmdqueryname=display+ethernet+uni+information) command. The command output shows the traffic encapsulation type and behavior configured on an EVC Layer 2 sub-interface. The following example uses the command output on PE2.
   
   ```
   [~PE2] display ethernet uni information
   ```
   ```
     GigabitEthernet0/1/0.1
       Total encapsulation number: 1
         encapsulation dot1q vid 10
       Rewrite pop single
   ```
   
   Run the **display mpls l2vc brief** command. The command output shows that a VC has been established and is in the Up state. The following example uses the command output on PE1.
   
   ```
   [~PE1] display mpls l2vc brief
   ```
   ```
    Total LDP VC : 1     1 up       0 down
   
    *Client Interface  : GigabitEthernet0/1/1.1
     Administrator PW  : no
     AC status         : up
     VC state        : up
     Label state       : 0
     Token state       : 0
     VC ID             : 100
     VC Type           : Ethernet
     session state     : up
     Destination       : 2.2.2.9
     link state        : up
   ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  vlan batch 10
  #
  mpls lsr-id 1.1.1.9
  #
  mpls
  #
  mpls l2vpn
  #
  mpls ldp
  #
  interface loopback 1
   ip address 1.1.1.9 255.255.255.255
  #
  interface GigabitEthernet0/1/0
   undo shutdown
  #
  interface GigabitEthernet0/1/0.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
   mpls l2vc 2.2.2.9 100 raw
  #
  interface GigabitEthernet0/2/0
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
  mpls ldp
  #
  interface loopback 1
   ip address 2.2.2.9 255.255.255.255
  #
  
  interface GigabitEthernet0/1/0
   undo shutdown
  #
  interface GigabitEthernet0/1/0.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
   mpls l2vc 1.1.1.9 100 raw
  #
  interface GigabitEthernet0/2/0
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
  vlan batch 10
  #
  interface GigabitEthernet0/1/0
   portswitch
  undo shutdown
   port link-type trunk
  port trunk allow-pass vlan 10
  #
  interface GigabitEthernet0/2/0
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
  interface GigabitEthernet0/1/0
   portswitch
  undo shutdown
   port link-type trunk
  port trunk allow-pass vlan 10
  #
  interface GigabitEthernet0/2/0
   portswitch
  undo shutdown
   port link-type trunk
  port trunk allow-pass vlan 10
  #
  return
  ```