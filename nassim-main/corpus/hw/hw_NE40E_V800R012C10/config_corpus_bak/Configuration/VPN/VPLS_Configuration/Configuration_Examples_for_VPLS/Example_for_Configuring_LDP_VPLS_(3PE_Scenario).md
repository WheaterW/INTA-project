Example for Configuring LDP VPLS (3PE Scenario)
===============================================

LDP VPLS applies to scenarios where PEs can use LDP as the VPLS signaling protocol. To fully mesh PEs on a VPLS network using PWs, set up LDP sessions between all the PEs.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000002042693058__fig_dc_vrp_vpls_cfg_503001), LDP VPLS is configured on PE1, PE2, and PE3, which function as PEs. CE1, CE2, and CE3 connect to PE1, PE2, and PE3, respectively. CE1, CE2, and CE3 belong to the same VPLS network.

**Figure 1** Network diagram of configuring LDP VPLS![](../../../../public_sys-resources/note_3.0-en-us.png) 

* In this example, subinterface1.1, interface2, and interface3 represent GE0/1/0.1, GE0/2/0, and GE0/3/0, respectively.

  
![](figure/en-us_image_0000002042879156.png)

#### Precautions

During the configuration, note the following:

* PEs belonging to the same L2VPN must have the same VSI ID.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a routing protocol on the backbone network for communication between devices.
2. Set up LDP sessions between PEs.
3. Enable MPLS L2VPN on PEs.
4. Create VSIs, set the signaling protocol to LDP, and bind AC interfaces to VSIs on PEs.

#### Data Preparation

To complete the configuration, you need the following data:

* VSI names and IDs
* Peer IP addresses and tunnel policies used for setting up peer relationships
* Interfaces bound to VSIs

#### Procedure

1. Configure interface addresses and an IGP on PEs according to [Figure 1](#EN-US_TASK_0000002042693058__fig_dc_vrp_vpls_cfg_503001). OSPF is used in this example.
   
   
   
   When configuring OSPF, configure PE1, PE2, and PE3 to advertise their 32-bit loopback interface addresses (used as LSR IDs).
   
   For detailed configurations, see [Configuration Files](#EN-US_TASK_0000002042693058__li714417045214053).
   
   After the configuration is complete, run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) command on PE1, PE2, and PE3. The command output shows that they have learned routes from each other.
2. Configure basic MPLS functions and LDP.
   
   
   
   For detailed configurations, see [Configuration Files](#EN-US_TASK_0000002042693058__li714417045214053).
   
   After the configuration is complete, run the **display mpls ldp session** command on PE1, PE2, and PE3 to verify that peer relationships have been established between PEs (**Status** is **Operational** for each peer). Run the **display mpls lsp** command. The command output shows whether LSPs have been set up.
3. Enable MPLS L2VPN on PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] mpls l2vpn
   ```
   ```
   [*PE1-l2vpn] commit
   ```
   
   # Configure PE2.
   
   ```
   [*PE2] mpls l2vpn
   ```
   ```
   [*PE2-l2vpn] commit
   ```
   
   # Configure PE3.
   
   ```
   [*PE3] mpls l2vpn
   ```
   ```
   [*PE3-l2vpn] commit
   ```
4. Configure a VSI on each PE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] vsi a2
   ```
   ```
   [*PE1-vsi-a2] pwsignal ldp
   ```
   ```
   [*PE1-vsi-a2-ldp] vsi-id 2
   ```
   ```
   [*PE1-vsi-a2-ldp] peer 2.2.2.9
   ```
   ```
   [*PE1-vsi-a2-ldp] peer 3.3.3.9
   ```
   ```
   [*PE1-vsi-a2-ldp] quit
   ```
   ```
   [*PE1-vsi-a2] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] vsi a2
   ```
   ```
   [*PE2-vsi-a2] pwsignal ldp
   ```
   ```
   [*PE2-vsi-a2-ldp] vsi-id 2
   ```
   ```
   [*PE2-vsi-a2-ldp] peer 1.1.1.9
   ```
   ```
   [*PE2-vsi-a2-ldp] peer 3.3.3.9
   ```
   ```
   [*PE2-vsi-a2-ldp] quit
   ```
   ```
   [*PE2-vsi-a2] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] vsi a2
   ```
   ```
   [*PE3-vsi-a2] pwsignal ldp
   ```
   ```
   [*PE3-vsi-a2-ldp] vsi-id 2
   ```
   ```
   [*PE3-vsi-a2-ldp] peer 1.1.1.9
   ```
   ```
   [*PE3-vsi-a2-ldp] peer 2.2.2.9
   ```
   ```
   [*PE3-vsi-a2-ldp] quit
   ```
   ```
   [*PE3-vsi-a2] quit
   ```
   ```
   [*PE3] commit
   ```
5. Bind interfaces to VSIs on PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] interface gigabitethernet0/1/0.1
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] vlan-type dot1q 10
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] l2 binding vsi a2
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] interface gigabitethernet0/1/0.1
   ```
   ```
   [*PE2-GigabitEthernet0/1/0.1] vlan-type dot1q 10
   ```
   ```
   [*PE2-GigabitEthernet0/1/0.1] l2 binding vsi a2
   ```
   ```
   [*PE2-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE3] interface gigabitethernet0/1/0.1
   ```
   ```
   [*PE3-GigabitEthernet0/1/0.1] vlan-type dot1q 10
   ```
   ```
   [*PE3-GigabitEthernet0/1/0.1] l2 binding vsi a2
   ```
   ```
   [*PE3-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*PE3] commit
   ```
6. Configure CEs.
   
   
   
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
   [*CE1] interface gigabitethernet0/1/0.1
   ```
   ```
   [*CE1-GigabitEthernet0/1/0.1] vlan-type dot1q 10
   ```
   ```
   [*CE1-GigabitEthernet0/1/0.1] ip address 10.1.1.1 255.255.255.0
   ```
   ```
   [*CE1-GigabitEthernet0/1/0.1] quit
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
   [~CE2] interface gigabitethernet0/1/0.1
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.1] vlan-type dot1q 10
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.1] ip address 10.1.1.2 255.255.255.0
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*CE2] commit
   ```
   
   # Configure CE3.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname CE3
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~CE3] interface gigabitethernet0/1/0.1
   ```
   ```
   [*CE3-GigabitEthernet0/1/0.1] vlan-type dot1q 10
   ```
   ```
   [*CE3-GigabitEthernet0/1/0.1] ip address 10.1.1.3 255.255.255.0
   ```
   ```
   [*CE3-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*CE3] commit
   ```
7. Verify the configuration.
   
   
   
   After the configuration is complete, run the **[**display vsi**](cmdqueryname=display+vsi) name a2 verbose** command on PE1. The command output shows that a VSI named **a2** has established two PWs (one to PE2 and the other to PE3), and **VSI State** is **up**.
   
   ```
   [~PE1]display vsi name a2 verbose
   
    ***VSI Name               : a2
       Work Mode           : normal
       Administrator VSI      : no
       Isolate Spoken         : disable
       VSI Index              : 1
       PW Signaling           : ldp
       Member Discovery Style : --
       Bridge-domain Mode     : disable
       PW MAC Learn Style     : unqualify
       Encapsulation Type     : vlan
       MTU                    : 1500
       Diffserv Mode          : uniform
       Service Class          : --
       Color                  : --
       DomainId               : 255
       Domain Name            :
       Ignore AcState         : disable
       P2P VSI                : disable
       Multicast Fast Switch  : disable
       Create Time            : 0 days, 0 hours, 53 minutes, 11 seconds
       VSI State              : up
       Resource Status        : --
   
       VSI ID                 : 2
      *Peer Router ID         : 2.2.2.9
       Negotiation-vc-id      : 2
       Encapsulation Type     : vlan
       primary or secondary   : primary
       ignore-standby-state   : no
       VC Label               : 65583
       Peer Type              : dynamic
       Session                : up
       Tunnel ID              : 0x0000000001004c4b43
       Broadcast Tunnel ID    : --
       Broad BackupTunnel ID  : --
       CKey                   : 1
       NKey                   : 16777458
       Stp Enable             : 0
       PwIndex                : 1
       Control Word           : disable
       BFD for PW             : unavailable
      *Peer Router ID         : 3.3.3.9
       Negotiation-vc-id      : 2
       Encapsulation Type     : vlan
       primary or secondary   : primary
       ignore-standby-state   : no
       VC Label               : 65584
       Peer Type              : dynamic
       Session                : up
       Tunnel ID              : 0x0000000001004c4b44
       Broadcast Tunnel ID    : --
       Broad BackupTunnel ID  : --
       CKey                   : 2
       NKey                   : 16777459
       Stp Enable             : 0
       PwIndex                : 2
       Control Word           : disable
       BFD for PW             : unavailable
   
       Interface Name         : GigabitEthernet0/1/0.1
       State                  : up
       Ac Block State         : unblocked
       Access Port            : false
       Last Up Time           : 2024/10/11 07:26:34
       Total Up Time          : 0 days, 0 hours, 20 minutes, 57 seconds
   
     **PW Information:
   
      *Peer Ip Address        : 2.2.2.9
       PW State               : up
       Local VC Label         : 65583
       Remote VC Label        : 48093
       Remote Control Word    : disable
       PW Type                : label
       Local  VCCV            : alert lsp-ping bfd
       Remote VCCV            : alert lsp-ping bfd
       Tunnel ID              : 0x0000000001004c4b43
       Broadcast Tunnel ID    : --
       Broad BackupTunnel ID  : --
       Ckey                   : 1
       Nkey                   : 16777458
       Main PW Token          : 0x0
       Slave PW Token         : 0x0
       Tnl Type               : ldp
       OutInterface           : GigabitEthernet0/3/0
       Backup OutInterface    : --
       Stp Enable             : 0
       Mac Flapping           : 0
       Monitor Group Name     : --
       PW Last Up Time        : 2024/10/11 07:30:02
       PW Total Up Time       : 0 days, 0 hours, 17 minutes, 29 seconds
      *Peer Ip Address        : 3.3.3.9
       PW State               : up
       Local VC Label         : 65584
       Remote VC Label        : 48091
       Remote Control Word    : disable
       PW Type                : label
       Local  VCCV            : alert lsp-ping bfd
       Remote VCCV            : alert lsp-ping bfd
       Tunnel ID              : 0x0000000001004c4b44
       Broadcast Tunnel ID    : --
       Broad BackupTunnel ID  : --
       Ckey                   : 2
       Nkey                   : 16777459
       Main PW Token          : 0x0
       Slave PW Token         : 0x0
       Tnl Type               : ldp
       OutInterface           : GigabitEthernet0/2/0
       Backup OutInterface    : --
       Stp Enable             : 0
       Mac Flapping           : 0
       Monitor Group Name     : --
       PW Last Up Time        : 2024/10/11 07:33:08
       PW Total Up Time       : 0 days, 0 hours, 14 minutes, 23 seconds
   ```
   
   # Configure CE1 (10.1.1.1) to ping CE2 (10.1.1.2). The ping is successful.
   
   ```
   <CE1> ping 10.1.1.2
     PING 10.1.1.2: 56  data bytes, press CTRL_C to break
       Reply from 10.1.1.2: bytes=56 Sequence=1 ttl=255 time=90 ms
       Reply from 10.1.1.2: bytes=56 Sequence=2 ttl=255 time=77 ms
       Reply from 10.1.1.2: bytes=56 Sequence=3 ttl=255 time=34 ms
       Reply from 10.1.1.2: bytes=56 Sequence=4 ttl=255 time=46 ms
       Reply from 10.1.1.2: bytes=56 Sequence=5 ttl=255 time=94 ms
     --- 10.1.1.2 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 34/68/94 ms 
   ```
   
   # Configure CE1 (10.1.1.1) to ping CE3 (10.1.1.3). The ping is successful.
   
   ```
   <CE1> ping 10.1.1.3
     PING 10.1.1.3: 56  data bytes, press CTRL_C to break
       Reply from 10.1.1.3: bytes=56 Sequence=1 ttl=255 time=90 ms
       Reply from 10.1.1.3: bytes=56 Sequence=2 ttl=255 time=77 ms
       Reply from 10.1.1.3: bytes=56 Sequence=3 ttl=255 time=34 ms
       Reply from 10.1.1.3: bytes=56 Sequence=4 ttl=255 time=46 ms
       Reply from 10.1.1.3: bytes=56 Sequence=5 ttl=255 time=94 ms
     --- 10.1.1.3 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 34/68/94 ms 
   ```

#### Configuration Files

* CE1 configuration file
  
  ```
  #
  sysname CE1
  #
  interface GigabitEthernet0/1/0.1
   undo shutdown
   vlan-type dot1q 10
   ip address 10.1.1.1 255.255.255.0
  #
  return
  ```
* CE2 configuration file
  
  ```
  #
  sysname CE2
  #
  interface GigabitEthernet0/1/0.1
   undo shutdown
   vlan-type dot1q 10
   ip address 10.1.1.2 255.255.255.0
  #
  return
  ```
* CE3 configuration file
  ```
  #
  sysname CE3
  #
  interface GigabitEthernet0/1/0.1
   undo shutdown
   vlan-type dot1q 10
   ip address 10.1.1.3 255.255.255.0
  #
  return
  ```
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
  vsi a2
   pwsignal ldp 
    vsi-id 2
    peer 2.2.2.9    
    peer 3.3.3.9
  # 
  mpls ldp
  #
  interface GigabitEthernet0/1/0.1
   undo shutdown
   vlan-type dot1q 10
   l2 binding vsi a2
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 172.16.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 172.16.2.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 1.1.1.9 255.255.255.255
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.9 0.0.0.0
    network 172.16.1.0 0.0.0.255
    network 172.16.2.0 0.0.0.255
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
  vsi a2
   pwsignal ldp  
    vsi-id 2     
    peer 1.1.1.9 
    peer 3.3.3.9 
  # 
  mpls ldp
  #
  interface GigabitEthernet0/1/0.1
   undo shutdown
   vlan-type dot1q 10
   l2 binding vsi a2
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 172.17.3.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 172.16.2.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 2.2.2.9 255.255.255.255
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.9 0.0.0.0
    network 172.16.2.0 0.0.0.255
    network 172.17.3.0 0.0.0.255
  #
  return
  ```
* PE3 configuration file
  
  ```
  #
  sysname PE3
  #
  mpls lsr-id 3.3.3.9
  #
  mpls
  #
  mpls l2vpn
  #
  vsi a2
   pwsignal ldp  
    vsi-id 2     
    peer 1.1.1.9 
    peer 2.2.2.9 
  # 
  mpls ldp
  #
  interface GigabitEthernet0/1/0.1
   undo shutdown
   vlan-type dot1q 10
   l2 binding vsi a2
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 172.16.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 172.17.3.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 3.3.3.9 255.255.255.255
  #
  ospf 1
   area 0.0.0.0
    network 3.3.3.9 0.0.0.0
    network 172.16.1.0 0.0.0.255
    network 172.17.3.0 0.0.0.255
  #
  return
  ```