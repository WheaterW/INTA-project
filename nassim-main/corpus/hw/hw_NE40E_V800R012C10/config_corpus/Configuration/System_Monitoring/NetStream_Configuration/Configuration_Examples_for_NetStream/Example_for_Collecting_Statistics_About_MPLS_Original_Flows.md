Example for Collecting Statistics About MPLS Original Flows
===========================================================

This section provides an example for configuring NetStream to collect statistics about MPLS original flows with a specified label.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172373028__fig_dc_vrp_ns_cfg_003401), DeviceA, DeviceB, and DeviceC support MPLS and use OSPF as IGP on the MPLS backbone network.

Local Label Distribution Protocol (LDP) sessions are established between DeviceA and DeviceB and between DeviceB and DeviceC. A remote LDP session is established between DeviceA and DeviceC. NetStream is enabled on DeviceB to collect statistics about MPLS flows.

**Figure 1** Collecting statistics about MPLS original flows![](../../../../public_sys-resources/note_3.0-en-us.png) 

* In this example, interfaces 1 and 2 represent GE0/1/0 and GE0/2/0, respectively.

  
![](figure/en-us_image_0183113639.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an LDP session between every two Routers.
2. Specify the remote peer and its address on the two Routers that have established a remote LDP session.
3. Specify the destination address, destination port number, and source address of the output NetStream flows

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of interfaces on each Router as shown in [Figure 1](#EN-US_TASK_0172373028__fig_dc_vrp_ns_cfg_003401), OSPF process ID (1), and area (Area0)
* DeviceA's remote peer (DeviceC) with name Devicec and IP address 3.3.3.9
* DeviceC's remote peer (DeviceA) with name Devicea and IP address 1.1.1.9
* ID of the slot in which the NetStream service processing board resides (In this example, the NetStream service processing board is in slot 3.)

#### Procedure

1. Assign an IP address to each involved interface.
   
   
   
   # Assign an IP address and a mask to each interface (including loopback interfaces) according to [Figure 1](#EN-US_TASK_0172373028__fig_dc_vrp_ns_cfg_003401). The configuration details are not provided here.
2. Configure an LDP session between every two Routers.
   
   
   
   # Configure OSPF to advertise host routes to the specified label switching router (LSR) ID and of the network segments to which interfaces on the Router are connected. Enable basic MPLS functions and LDP on each Router and its interfaces.
   
   For configurations of the static MPLS TE tunnel, see "Basic MPLS Configurations" in *NE40E Configuration Guide > MPLS*.
3. Enable NetStream statistics collection on GigabitEthernet 0/1/0 of DeviceB.
   
   
   
   # Specify the distributed NetStream sampling mode on a board.
   
   ```
   [*DeviceB] slot 3
   ```
   ```
   [*DeviceB-slot-3] ip netstream sampler to slot self
   ```
   ```
   [*DeviceB-slot-3] quit
   ```
   
   # Configure NetStream to collect statistics about incoming and outgoing packets on GigabitEthernet 0/1/0 of DeviceB.
   
   ```
   [*DeviceB] interface GigabitEthernet 0/1/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] ip netstream inbound
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] ip netstream outbound
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   NetStream enabled on a main interface cannot collect traffic statistics about its sub-interface.
   
   # Configure NetStream to sample both inner IP packets and labels of MPLS packets.
   
   ```
   [*DeviceB] ip netstream mpls-aware label-and-ip
   ```
   
   # Specify the destination address, destination port number, and source address for the output flows.
   
   ```
   [*DeviceB] ip netstream export host 192.168.1.2 2100
   ```
   ```
   [*DeviceB] ip netstream export source 10.1.2.1
   ```
   
   # Enable NetStream sampling and configure the fixed packet sampling mode.
   
   ```
   [*DeviceB] ip netstream sampler fix-packets 10000 inbound
   ```
   ```
   [*DeviceB] ip netstream sampler fix-packets 10000 outbound
   ```
   ```
   [*DeviceB] commit
   ```
4. Verify the configuration.
   
   
   
   # Run the [**display ip netstream cache origin slot**](cmdqueryname=display+ip+netstream+cache+origin+slot) **3** command after completing the configuration. The command output shows information about the NetStream flow buffer and statistics about output packets.
   
   ```
   [~DeviceB] display ip netstream cache origin slot 3
   
   
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
    10.1.2.1                                                   in
    10.1.1.5                                                   0         
    192.168.1.4                                                0         
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

* DeviceA configuration file
  
  ```
  #
  ```
  ```
   sysname DeviceA
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
  ```
  ```
   mpls ldp remote-peer Devicec
  ```
  ```
   remote-ip 3.3.3.9
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
   ip address 10.1.1.1 255.255.255.0
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
    network 10.1.1.0 0.0.0.255
  ```
  ```
    network 1.1.1.9 0.0.0.0
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceB configuration file
  
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
   sysname DeviceB
  ```
  ```
  #
  ```
  ```
   ip netstream mpls-aware label-and-ip
  ```
  ```
  # 
  ```
  ```
  ip netstream sampler fix-packets 10000 inbound
  ```
  ```
  ip netstream sampler fix-packets 10000 outbound 
  ```
  ```
  ip netstream export host 192.168.1.2 2100
  ```
  ```
  ip netstream export source 10.1.2.1
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
   undo shutdown
  ```
  ```
   ip address 10.1.1.2 255.255.255.0
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
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
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
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 10.1.1.0 0.0.0.255
  ```
  ```
    network 10.1.2.0 0.0.0.255
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
* DeviceC configuration file
  
  ```
  #
  ```
  ```
   sysname DeviceC
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
   mpls ldp remote-peer DeviceA
  ```
  ```
   remote-ip 1.1.1.9
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
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 4.1.1.0 0.0.0.255
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