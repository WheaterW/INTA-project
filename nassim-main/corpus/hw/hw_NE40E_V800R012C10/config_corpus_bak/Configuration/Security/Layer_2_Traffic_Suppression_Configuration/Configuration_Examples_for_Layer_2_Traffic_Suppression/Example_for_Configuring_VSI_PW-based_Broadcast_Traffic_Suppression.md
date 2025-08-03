Example for Configuring VSI PW-based Broadcast Traffic Suppression
==================================================================

This section provides an example for configuring VSI PW-based broadcast traffic suppression in order to properly allocate user bandwidth and improve network performance.

#### Networking Requirements

In addition to user traffic management and bandwidth allocation, an Ethernet requires broadcast, multicast, and unknown unicast traffic to be suppressed to ensure the secure transmission of unicast traffic and properly utilize bandwidth resources. If these types of traffic are not suppressed, forwarding a large volume of such traffic consumes numerous bandwidth resources, reducing network performance and even causing a communication interruption.

On the network shown in [Figure 1](#EN-US_TASK_0172372586__fig_dc_ne_traff-supress_cfg_501101), CE1 and CE2 belong to the same LDP VPLS network and can communicate with each other. If you configure broadcast traffic suppression on an interface, the broadcast traffic of all PWs created on the interface is suppressed. In this case, you can configure broadcast traffic suppression for only the PW in a specified VSI. This makes traffic suppression more convenient and flexible.

**Figure 1** Networking diagram for configuring VSI PW-based broadcast traffic suppression![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, subinterface1.1, and subinterface2.1 represent GE0/1/0, GE0/2/0, GE0/1/0.1, and 0/2/0.1, respectively.


  
![](images/fig_dc_ne_traff-supress_cfg_501101.png)  

| Device Name | Interface Number | Interface IP Address | Interface MAC Address |
| --- | --- | --- | --- |
| CE1 | GE0/1/0.1 | 10.1.1.1/24 | - |
| PE1 | Loopback1 | 1.1.1.1/32 | - |
| PE1 | GE0/2/0 | 172.16.1.1/24 | - |
| P | Loopback1 | 2.2.2.2/32 | - |
| P | GE0/1/0 | 172.16.1.2/24 | - |
| P | GE0/2/0 | 192.168.1.1/24 | - |
| PE2 | Loopback1 | 3.3.3.3/32 | - |
| PE2 | GE0/1/0 | 192.168.1.2/24 | - |
| CE2 | GE0/2/0.1 | 10.1.1.2/24 | - |




#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a routing protocol on the backbone network to implement interworking.
2. Establish a remote LDP session between the PEs.
3. Establish a tunnel for data transmission between the PEs.
4. Enable MPLS L2VPN on the PEs.
5. Create a VSI on each PE, specify LDP as the signaling protocol, and bind an AC interface to the VSI.
6. Configure VSI PW-based broadcast traffic suppression.

#### Data Preparation

To complete the configuration, you need the following data:

* VSI names and IDs
* Peer IP address and tunnel policy used for establishing the peer relationship
* Interfaces to be bound to the VSIs
* Committed information rate (CIR) for broadcast traffic

#### Procedure

1. Configure an IGP.
   
   
   
   OSPF is used in this example. The configuration details are not provided here.
   
   After the configuration is complete, run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) command on PE1, the P, and PE2. The command output shows that the devices have learned routes from their peers.
   
   Configure addresses for interfaces on PE1, the P, and PE2, as shown in [Figure 1](#EN-US_TASK_0172372586__fig_dc_ne_traff-supress_cfg_501101). During OSPF configuration, enable the devices to advertise their 32-bit loopback addresses (LSR-IDs).
2. Configure basic MPLS functions and LDP.
   
   
   
   The configuration details are not provided here.
   
   After the configuration is complete, run the [**display mpls ldp session**](cmdqueryname=display+mpls+ldp+session) command on PE1, the P, and PE2. The command output shows that the status of the peer relationship between PE1 and the P and the status of the peer relationship between PE2 and the P are both **Operational**. This means that the peer relationships have been established. To check information about LSP establishment, run the [**display mpls lsp**](cmdqueryname=display+mpls+lsp) command.
3. Establish a remote LDP session between the PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] mpls ldp remote-peer 3.3.3.3
   ```
   ```
   [*PE1-mpls-ldp-remote-3.3.3.3] remote-ip 3.3.3.3
   ```
   ```
   [*PE1-mpls-ldp-remote-3.3.3.3] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] mpls ldp remote-peer 1.1.1.1
   ```
   ```
   [*PE2-mpls-ldp-remote-1.1.1.1] remote-ip 1.1.1.1
   ```
   ```
   [*PE2-mpls-ldp-remote-1.1.1.1] quit
   ```
   ```
   [*PE2] commit
   ```
   
   After the configuration is complete, run the [**display mpls ldp session**](cmdqueryname=display+mpls+ldp+session) command on PE1 or PE2. The command output shows that the status of the peer relationship between PE1 and PE2 is **Operational**. This means that the remote peer relationship has been established.
4. Enable MPLS L2VPN on the PEs.
   
   
   
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
5. Configure a VSI on each PE and configure VSI PW-based traffic suppression.
   
   
   
   # Configure VSI PW-based broadcast, multicast, and unknown unicast traffic suppression on PE1.
   
   ```
   [~PE1] vsi a2 static
   ```
   ```
   [*PE1-vsi-a2] suppression inbound enable   
   ```
   ```
   [*PE1-vsi-a2] pwsignal ldp
   ```
   ```
   [*PE1-vsi-a2-ldp] vsi-id 2
   ```
   ```
   [*PE1-vsi-a2-ldp] peer 3.3.3.3
   ```
   ```
   [*PE1-vsi-a2-ldp] peer 3.3.3.3 pw 1
   ```
   ```
   [*PE1-vsi-a2-ldp-pw-1] broadcast-suppression cir 1000
   ```
   ```
   [*PE1-vsi-a2-ldp-pw-1] multicast-suppression cir 1000
   ```
   ```
   [*PE1-vsi-a2-ldp-pw-1] unknown-unicast-suppression cir 1000
   ```
   ```
   [*PE1-vsi-a2-ldp-pw-1] quit
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
   
   # Configure VSI PW-based broadcast, multicast, and unknown unicast traffic suppression on PE2.
   
   ```
   [~PE2] vsi a2 static
   ```
   ```
   [*PE2-vsi-a2] suppression inbound enable   
   ```
   ```
   [*PE2-vsi-a2] pwsignal ldp
   ```
   ```
   [*PE2-vsi-a2-ldp] vsi-id 2
   ```
   ```
   [*PE2-vsi-a2-ldp] peer 1.1.1.1
   ```
   ```
   [*PE2-vsi-a2-ldp] peer 1.1.1.1 pw 1
   ```
   ```
   [*PE2-vsi-a2-ldp-pw-1] broadcast-suppression cir 1000
   ```
   ```
   [*PE2-vsi-a2-ldp-pw-1] multicast-suppression cir 1000
   ```
   ```
   [*PE2-vsi-a2-ldp-pw-1] unknown-unicast-suppression cir 1000
   ```
   ```
   [*PE2-vsi-a2-ldp-pw-1] quit
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
6. Bind interfaces to the VSIs on the PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] interface gigabitethernet0/1/0.1
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] shutdown
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] vlan-type dot1q 10
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] l2 binding vsi a2
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] undo shutdown
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] interface gigabitethernet0/2/0.1
   ```
   ```
   [*PE2-GigabitEthernet0/2/0.1] shutdown
   ```
   ```
   [*PE2-GigabitEthernet0/2/0.1] vlan-type dot1q 10
   ```
   ```
   [*PE2-GigabitEthernet0/2/0.1] l2 binding vsi a2
   ```
   ```
   [*PE2-GigabitEthernet0/2/0.1] undo shutdown
   ```
   ```
   [*PE2-GigabitEthernet0/2/0.1] quit
   ```
   ```
   [*PE2] commit
   ```
7. Configure the CEs.
   
   
   
   # Configure CE1.
   
   ```
   <HUAWEI> sysname CE1
   ```
   ```
   <HUAWEI> commit
   ```
   ```
   [~CE1] interface gigabitethernet0/1/0.1
   ```
   ```
   [*CE1-GigabitEthernet0/1/0.1] shutdown
   ```
   ```
   [*CE1-GigabitEthernet0/1/0.1] vlan-type dot1q 10
   ```
   ```
   [*CE1-GigabitEthernet0/1/0.1] ip address 10.1.1.1 255.255.255.0
   ```
   ```
   [*CE1-GigabitEthernet0/1/0.1] undo shutdown
   ```
   ```
   [*CE1-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*CE1] commit
   ```
   
   # Configure CE2.
   
   ```
   <HUAWEI> sysname CE2
   ```
   ```
   <HUAWEI> commit
   ```
   ```
   [~CE2] interface gigabitethernet0/1/0.1
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.1] shutdown
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.1] vlan-type dot1q 10
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.1] ip address 10.1.1.2 255.255.255.0
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.1] undo shutdown
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*CE1] commit
   ```
8. Verify the configuration.
   
   
   
   After the configuration is complete, run the **display vsi name a2 verbose** command on PE1. The command output shows that a PW to PE2 has been established for the VSI **a2** and the VSI state is **up**.
   
   ```
   [PE1] display vsi name a2 verbose
   ```
   ```
    ***VSI Name               : a2
   ```
   ```
       Administrator VSI      : no
   ```
   ```
       Isolate Spoken         : disable
   ```
   ```
       VSI Index              : 0
   ```
   ```
       PW Signaling           : ldp
   ```
   ```
       Member Discovery Style : static
   ```
   ```
       PW MAC Learn Style     : unqualify
   ```
   ```
       Encapsulation Type     : vlan
   ```
   ```
       MTU                    : 1500
   ```
   ```
       Diffserv Mode          : uniform
   ```
   ```
       Service Class          : --
   ```
   ```
       Color                  : --
   ```
   ```
       DomainId               : 255
   ```
   ```
       Domain Name            :
   ```
   ```
       Ignore AcState         : disable
   ```
   ```
       Multicast Fast Switch  : disable
   ```
   ```
       Create Time            : 0 days, 3 hours, 30 minutes, 31 seconds
   ```
   ```
       VSI State              : up
   ```
   ```
       VSI ID                 : 2
   ```
   ```
      *Peer Router ID         : 3.3.3.3
   ```
   ```
       primary or secondary   : primary
   ```
   ```
       ignore-standby-state   : no
   ```
   ```
       VC Label               : 18
   ```
   ```
       Peer Type              : dynamic
   ```
   ```
       Session                : up
   ```
   ```
       Tunnel ID              : 0x0000000001004c4b82
   ```
   ```
       Broadcast Tunnel ID    : --
   ```
   ```
       Broad BackupTunnel ID  : --
   ```
   ```
       CKey                   : 6
   ```
   ```
       NKey                   : 5
   ```
   ```
       StpEnable              : 0 
   ```
   ```
       PwIndex                : 0
   ```
   ```
       Interface Name         : GigabitEthernet0/1/0.1
   ```
   ```
       State                  : up
   ```
   ```
       Last Up Time           : 2012/10/10 10:14:46
   ```
   ```
       Total Up Time          : 0 days, 0 hours, 1 minutes, 2 seconds
   ```
   ```
      **PW Information:
   ```
   ```
      *Peer Ip Address        : 3.3.3.3
   ```
   ```
       PW State               : up
   ```
   ```
       Local VC Label         : 18
   ```
   ```
       Remote VC Label        : 18
   ```
   ```
       PW Type                : label
   ```
   ```
       Tunnel ID              : 0x0000000001004c4b82
   ```
   ```
       Broadcast Tunnel ID    : --
   ```
   ```
       Broad BackupTunnel ID  : --
   ```
   ```
       Ckey                   : 1
   ```
   ```
       Nkey                   : 1610612838
   ```
   ```
       Main PW Token          : 0x0
   ```
   ```
       Slave PW Token         : 0x0 
   ```
   ```
       Tnl Type               : LdP
   ```
   ```
       OutInterface           : LDP LSP
   ```
   ```
       Backup OutInterface    :
   ```
   ```
       Stp Enable             : 0
   ```
   ```
       PW Last Up Time        : 2012-10-10 10:15:59
   ```
   ```
       PW Total Up Time       : 0 days, 0 hours, 1 minutes, 3 seconds
   ```
   
   # Check that CE1 (10.1.1.1) can ping CE2 (10.1.1.2).
   
   ```
   [CE1] ping 10.1.1.2
   ```
   ```
     PING 10.1.1.2: 56  data bytes, press CTRL_C to break
   ```
   ```
       Reply from 10.1.1.2: bytes=56 Sequence=1 ttl=255 time=90 ms
   ```
   ```
       Reply from 10.1.1.2: bytes=56 Sequence=2 ttl=255 time=77 ms
   ```
   ```
       Reply from 10.1.1.2: bytes=56 Sequence=3 ttl=255 time=34 ms
   ```
   ```
       Reply from 10.1.1.2: bytes=56 Sequence=4 ttl=255 time=46 ms
   ```
   ```
       Reply from 10.1.1.2: bytes=56 Sequence=5 ttl=255 time=94 ms
   ```
   ```
     --- 10.1.1.2 ping statistics ---
   ```
   ```
       5 packet(s) transmitted
   ```
   ```
       5 packet(s) received
   ```
   ```
       0.00% packet loss
   ```
   ```
       round-trip min/avg/max = 34/68/94 ms 
   ```

#### Configuration Files

* CE1 configuration file
  
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
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0.1
  ```
  ```
   undo shutdown
  ```
  ```
   vlan-type dot1q 10
  ```
  ```
   ip address 10.1.1.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  return
  ```
* CE2 configuration file
  
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
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0.1
  ```
  ```
   undo shutdown
  ```
  ```
   vlan-type dot1q 10
  ```
  ```
   ip address 10.1.1.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  return
  ```
* PE1 configuration file
  
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
  mpls l2vpn
  ```
  ```
  #
  ```
  ```
  vsi a2 static 
  ```
  ```
   pwsignal ldp 
  ```
  ```
    vsi-id 2    
  ```
  ```
    peer 3.3.3.3
  ```
  ```
    peer 3.3.3.3 pw 1
  ```
  ```
    broadcast-suppression cir 1000
  ```
  ```
    multicast-suppression cir 1000
  ```
  ```
    unknown-unicast-suppression cir 1000
  ```
  ```
   suppression inbound enable   
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
   mpls ldp remote-peer 3.3.3.3
  ```
  ```
   remote-ip 3.3.3.3
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
  #
  ```
  ```
  interface GigabitEthernet0/1/0.1
  ```
  ```
   undo shutdown
  ```
  ```
   vlan-type dot1q 10
  ```
  ```
   l2 binding vsi a2
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
   ip address 172.16.1.1 255.255.255.0
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
    network 172.16.1.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  return
  ```
* P configuration file
  
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
   ip address 172.16.1.2 255.255.255.0
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
    network 172.16.1.0 0.0.0.255
  ```
  ```
    network 192.168.1.0 0.0.0.255
  ```
  ```
    network 2.2.2.2 0.0.0.0
  ```
  ```
  #
  ```
  ```
  return
  ```
* PE2 configuration file
  
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
   mpls l2vpn
  ```
  ```
  #
  ```
  ```
  vsi a2 static  
  ```
  ```
   pwsignal ldp  
  ```
  ```
    vsi-id 2     
  ```
  ```
    peer 1.1.1.1 
  ```
  ```
    peer 1.1.1.1 pw 1
  ```
  ```
    broadcast-suppression cir 1000
  ```
  ```
    multicast-suppression cir 1000
  ```
  ```
    unknown-unicast-suppression cir 1000
  ```
  ```
   suppression inbound enable   
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
   mpls ldp remote-peer 1.1.1.1
  ```
  ```
   remote-ip 1.1.1.1
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
  #
  ```
  ```
  interface GigabitEthernet0/2/0.1
  ```
  ```
   undo shutdown
  ```
  ```
   vlan-type dot1q 10
  ```
  ```
   l2 binding vsi a2
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
    network 192.168.1.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  return
  ```