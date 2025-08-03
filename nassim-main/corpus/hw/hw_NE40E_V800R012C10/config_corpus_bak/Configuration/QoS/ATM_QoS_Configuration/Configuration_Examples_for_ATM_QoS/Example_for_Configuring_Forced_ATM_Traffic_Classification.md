Example for Configuring Forced ATM Traffic Classification
=========================================================

This section provides an example for configuring forced ATM traffic classification.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172371693__fig_dc_ne_qos_qos_cfg_01261001), when PE1 receives ATM cells from CE1, it transparently transmits the ATM cells over PW to PE2. PE2 then transmits the ATM cells over the ATM link.

L2VPN needs to be configured between PE1 and PE2 to implement forced traffic classification of the traffic flowing from CE1 to CE2.

**Figure 1** Networking diagram for forced ATM traffic classification![](../../../../public_sys-resources/note_3.0-en-us.png) 

interface1, interface2, and interface3 in this example represent ATM0/1/0, POS0/2/0, and POS0/1/0, respectively.


  
![](images/fig_dc_ne_qos_cfg_01261001.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IP addresses and PVC parameters for the interfaces.
2. Configure IGP on the P and PE devices in the MPLS network to achieve IP connectivity.
3. Configure basic MPLS functions on the P and PE devices.
4. Configure MPLS LDP on the P and PE devices.
5. Establish remote LDP sessions between the two PEs.
6. Enable MPLS L2VPN on the PE devices.
7. Configure transparent transmission of ATM cells on the PE devices.
8. Configure forced ATM traffic classification on the upstream interface ATM 3/0/0 of PE1.

#### Data Preparation

To complete the configuration, you need the following data:

* Data for configuring OSPF
* Name of the remote PE peer
* VC ID
* VPI/VCI value on the CE
* CoS and color of IP packets on the PVC for forced ATM traffic classification

#### Procedure

1. Configure ATM interfaces of the CEs.
   
   
   
   # Configure CE1.
   
   ```
   <CE1> system-view
   ```
   ```
   [~CE1] interface atm 0/1/0
   ```
   ```
   [~CE1-Atm0/1/0] undo shutdown
   ```
   ```
   [~CE1-Atm0/1/0] quit
   ```
   ```
   [~CE1] interface atm 0/1/0.1
   ```
   ```
   [~CE1-Atm0/1/0.1] ip address 192.168.160.1 24
   ```
   ```
   [*CE1-Atm0/1/0.1] pvc 1/100
   ```
   ```
   [*CE1-atm-pvc-Atm0/1/0.1-1/100] map ip 192.168.160.2
   ```
   ```
   [*CE1-atm-pvc-Atm0/1/0.1-1/100] commit
   ```
   ```
   [~CE1-atm-pvc-Atm0/1/0.1-1/100] return
   ```
   
   # Configure CE2.
   
   ```
   <CE2> system-view
   ```
   ```
   [~CE2] interface atm 0/1/0
   ```
   ```
   [~CE2-Atm0/1/0] undo shutdown
   ```
   ```
   [~CE2-Atm0/1/0] quit
   ```
   ```
   [~CE2] interface atm 0/1/0.1
   ```
   ```
   [~CE2-Atm0/1/0.1] ip address 192.168.160.2 24
   ```
   ```
   [*CE2-Atm0/1/0.1] pvc 1/100
   ```
   ```
   [*CE2-atm-pvc-Atm0/1/0.1-1/100] map ip 192.168.160.1
   ```
   ```
   [*CE2-atm-pvc-Atm0/1/0.1-1/100] commit
   ```
   ```
   [~CE2-atm-pvc-Atm0/1/0.1-1/100] return
   ```
2. Configure IGP on the MPLS network (In this example, OSPF is used).
   
   
   
   # Assign IP addresses for the interfaces on the PE1, PE2, and P devices (Details omitted).
   
   # Configure PE1.
   
   ```
   <PE1> system-view
   ```
   ```
   [~PE1] ospf 1 router-id 1.1.1.9
   ```
   ```
   [*PE1-ospf-1] area 0.0.0.0
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
   [*PE1-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~PE1-ospf-1] quit
   ```
   
   # Configure the P.
   
   ```
   <P> system-view
   ```
   ```
   [~P] ospf 1 router-id 2.2.2.9
   ```
   ```
   [*P-ospf-1] area 0.0.0.0
   ```
   ```
   [*P-ospf-1-area-0.0.0.0] network 2.2.2.9 0.0.0.0
   ```
   ```
   [*P-ospf-1-area-0.0.0.0] network 10.1.1.0 0.0.0.255
   ```
   ```
   [*P-ospf-1-area-0.0.0.0] network 10.1.2.0 0.0.0.255
   ```
   ```
   [*P-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [*P-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~P-ospf-1] quit
   ```
   
   # Configure PE2.
   
   ```
   <PE2> system-view
   ```
   ```
   [~PE2] ospf 1 router-id 3.3.3.9
   ```
   ```
   [*PE2-ospf-1] area 0.0.0.0
   ```
   ```
   [*PE2-ospf-1-area-0.0.0.0] network 3.3.3.9 0.0.0.0
   ```
   ```
   [*PE2-ospf-1-area-0.0.0.0] network 10.1.2.0 0.0.0.255
   ```
   ```
   [*PE2-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [*PE2-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~PE2-ospf-1] quit
   ```
3. Configure basic MPLS functions and LDP on the MPLS network.
   
   
   
   # Configure PE1.
   
   ```
   <PE1> system-view
   ```
   ```
   [~PE1] mpls lsr-id 1.1.1.9
   ```
   ```
   [*PE1] mpls
   ```
   ```
   [*PE1-mpls] lsp-trigger all
   ```
   ```
   [*PE1-mpls] commit
   ```
   ```
   [~PE1-mpls] quit
   ```
   ```
   [~PE1] mpls ldp
   ```
   ```
   [*PE1] commit
   ```
   ```
   [~PE1-mpls-ldp] quit
   ```
   ```
   [~PE1] interface pos 0/2/0
   ```
   ```
   [~PE1-Pos0/2/0] undo shutdown
   ```
   ```
   [~PE1-Pos0/2/0] mpls
   ```
   ```
   [*PE1-Pos0/2/0] mpls ldp
   ```
   ```
   [*PE1-Pos0/2/0] commit
   ```
   ```
   [~PE1-Pos0/2/0] return
   ```
   
   # Configure the P.
   
   ```
   <P> system-view
   ```
   ```
   [~P] mpls lsr-id 2.2.2.9
   ```
   ```
   [*P] mpls
   ```
   ```
   [*P-mpls] lsp-trigger all
   ```
   ```
   [*P-mpls] quit
   ```
   ```
   [*P] mpls ldp
   ```
   ```
   [*P-mpls-ldp] commit
   ```
   ```
   [~P-mpls-ldp] quit
   ```
   ```
   [~P] interface pos 0/2/0
   ```
   ```
   [~P-Pos0/2/0] undo shutdown
   ```
   ```
   [~P-Pos0/2/0] mpls
   ```
   ```
   [*P-Pos0/2/0] mpls ldp
   ```
   ```
   [*P-Pos0/2/0] commit
   ```
   ```
   [~P-Pos0/2/0] quit
   ```
   ```
   [~P] interface pos 0/1/0
   ```
   ```
   [~P-Pos0/1/0] undo shutdown
   ```
   ```
   [~P-Pos0/1/0] mpls
   ```
   ```
   [*P-Pos0/1/0] mpls ldp
   ```
   ```
   [*P-Pos0/1/0] commit
   ```
   ```
   [~P-Pos0/1/0] quit
   ```
   
   # Configure PE2.
   
   ```
   <PE2> system-view
   ```
   ```
   [~PE2] mpls lsr-id 3.3.3.9
   ```
   ```
   [*PE2] mpls
   ```
   ```
   [*PE2-mpls] lsp-trigger all
   ```
   ```
   [*PE2-mpls] quit
   ```
   ```
   [*PE2] mpls ldp
   ```
   ```
   [*PE2] commit
   ```
   ```
   [~PE2-mpls-ldp] quit
   ```
   ```
   [~PE2] interface pos 0/2/0
   ```
   ```
   [~PE2-Pos0/2/0] undo shutdown
   ```
   ```
   [~PE2-Pos0/2/0] mpls
   ```
   ```
   [*PE2-Pos0/2/0] mpls ldp
   ```
   ```
   [*PE2-Pos0/2/0] commit
   ```
   ```
   [~PE2-Pos0/2/0] quit
   ```
4. Establish remote LDP sessions between the two PEs.
   
   
   
   # Configure PE1.
   
   ```
   <PE1> system-view
   ```
   ```
   [~PE1] mpls ldp remote-peer 1
   ```
   ```
   [*PE1-mpls-ldp-remote-1] remote-ip 3.3.3.9
   ```
   ```
   [*PE1-mpls-ldp-remote-1] commit
   ```
   ```
   [~PE1-mpls-ldp-remote-1] return
   ```
   
   # Configure PE2.
   
   ```
   <PE2> system-view
   ```
   ```
   [~PE2] mpls ldp remote-peer 1
   ```
   ```
   [*PE2-mpls-ldp-remote-1] remote-ip 1.1.1.9
   ```
   ```
   [*PE2-mpls-ldp-remote-1] commit
   ```
   ```
   [~PE2-mpls-ldp-remote-1] return
   ```
5. On PEs, enable MPLS L2VPN and configure 1-to-1 VCC ATM transmission.
   
   
   
   # Configure PE1.
   
   ```
   <PE1> system-view
   ```
   ```
   [~PE1] mpls l2vpn
   ```
   ```
   [~PE1-l2vpn] quit
   ```
   ```
   [~PE1] interface atm 0/1/0
   ```
   ```
   [~PE1-Atm0/1/0] undo shutdown
   ```
   ```
   [~PE1-Atm0/1/0] quit
   ```
   ```
   [~PE1] interface atm 0/1/0.1 p2p
   ```
   ```
   [~PE1-Atm0/1/0.1] atm cell transfer
   ```
   ```
   [~PE1-Atm0/1/0.1] pvc 1/100
   ```
   ```
   [~PE1-atm-pvc-Atm0/1/0.1-1/100] quit
   ```
   ```
   [~PE1-Atm0/1/0.1] mpls l2vc 3.3.3.9 101
   ```
   ```
   [*PE1-Atm0/1/0.1] commit
   ```
   ```
   [~PE1-Atm0/1/0.1] return
   ```
   
   # Configure PE2.
   
   ```
   <PE2> system-view
   ```
   ```
   [~PE2] mpls l2vpn
   ```
   ```
   [~PE2-l2vpn] quit
   ```
   ```
   [~PE2] interface atm 0/1/0
   ```
   ```
   [~PE2-Atm0/1/0] undo shutdown
   ```
   ```
   [~PE2-Atm0/1/0] quit
   ```
   ```
   [~PE2] interface atm 0/1/0.1 p2p
   ```
   ```
   [~PE2-Atm0/1/0.1] atm cell transfer
   ```
   ```
   [~PE2-Atm0/1/0.1] pvc 1/100
   ```
   ```
   [~PE2-atm-pvc-Atm0/1/0.1-1/100] quit
   ```
   ```
   [~PE2-Atm0/1/0.1] mpls l2vc 1.1.1.9 101
   ```
   ```
   [*PE2-Atm0/1/0.1] commit
   ```
   ```
   [~PE2-Atm0/1/0.1] return
   ```
6. Configure forced ATM traffic classification on PE1.
   
   
   ```
   <PE1> system-view
   ```
   ```
   [~PE1] interface atm 0/1/0
   ```
   ```
   [~PE1-Atm0/1/0] undo shutdown
   ```
   ```
   [~PE1-Atm0/1/0] quit
   ```
   ```
   [~PE1] interface atm 0/1/0.1
   ```
   ```
   [~PE1-Atm0/1/0.1] traffic queue af4 green
   ```
   ```
   [~PE1-Atm0/1/0.1] commit
   ```
   ```
   [~PE1-Atm0/1/0.1] quit
   ```
   ```
   [~PE1] interface pos 0/2/0
   ```
   ```
   [~PE1-pos0/2/0] undo shutdown
   ```
   ```
   [~PE1-pos0/2/0] trust upstream default
   ```
   ```
   [*PE1-pos0/2/0] commit
   ```
   ```
   [~PE1-pos0/2/0] return
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Because network traffic is bi-directional, on PE2, you also need to configure ATM simple traffic classification for the reverse traffic. The configuration is similar to that on PE1 and is not mentioned in this example.

#### Configuration Files

* Configuration file of CE1
  
  ```
  #
  ```
  ```
   sysname CE1
  ```
  ```
  #
  ```
  ```
  interface Atm0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
  #
  ```
  ```
  interface Atm0/1/0.1
  ```
  ```
   pvc 1/100
  ```
  ```
   map ip 192.168.160.2
  ```
  ```
   ip address 192.168.160.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  return
  ```
* Configuration file of CE2
  
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
  interface Atm0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
  #
  ```
  ```
  interface Atm0/1/0.1
  ```
  ```
    pvc 1/100
  ```
  ```
   map ip 192.168.160.1
  ```
  ```
   ip address 192.168.160.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  return
  ```
* Configuration file of PE1
  
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
  mpls lsr-id 1.1.1.9
  ```
  ```
   mpls
  ```
  ```
    lsp-trigger all
  ```
  ```
   mpls l2vpn
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
  mpls ldp remote-peer 1
  ```
  ```
   remote-ip 3.3.3.9
  ```
  ```
  #
  ```
  ```
  interface Atm0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
  #
  ```
  ```
  interface Atm0/1/0.1
  ```
  ```
   traffic queue af4 green
  ```
  ```
   atm cell transfer
  ```
  ```
   pvc 1/100
  ```
  ```
   mpls l2vc 3.3.3.9 101 no-control-word
  ```
  ```
  #
  ```
  ```
  interface Pos0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.1.1 255.255.255.0
  ```
  ```
   trust upstream default
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
  ospf 1 router-id 1.1.1.9
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 1.1.1.9 0.0.0.0
  ```
  ```
    network 10.1.1.0 0.0.0.255
  ```
  ```
    network 192.168.160.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  return
  ```
* Configuration file of P
  
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
   mpls lsr-id 2.2.2.9
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
  interface Pos0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   link-protocol ppp
  ```
  ```
   ip address 10.1.1.2 255.255.255.0
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
  interface Pos0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   link-protocol ppp
  ```
  ```
   ip address 10.1.2.1 255.255.255.0
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
  ospf 1 router-id 2.2.2.9
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 2.2.2.9 0.0.0.0
  ```
  ```
    network 10.1.1.0 0.0.0.255
  ```
  ```
    network 10.1.2.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  return
  ```
* Configuration file of PE2
  
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
  mpls lsr-id 3.3.3.9
  ```
  ```
   mpls
  ```
  ```
    lsp-trigger all
  ```
  ```
   mpls l2vpn
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
  mpls ldp remote-peer 1
  ```
  ```
   remote-ip 1.1.1.9
  ```
  ```
  #
  ```
  ```
  interface Atm0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
  #
  ```
  ```
  interface Atm0/1/0.1
  ```
  ```
   traffic queue af4 green
  ```
  ```
   atm cell transfer
  ```
  ```
   pvc 1/100
  ```
  ```
   mpls l2vc 1.1.1.9 101 no-control-word
  ```
  ```
  #
  ```
  ```
  interface Pos0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.2.2 255.255.255.0
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
  ospf 1 router-id 3.3.3.9
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 3.3.3.9 0.0.0.0
  ```
  ```
    network 10.1.2.0 0.0.0.255
  ```
  ```
    network 192.168.160.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  return
  ```