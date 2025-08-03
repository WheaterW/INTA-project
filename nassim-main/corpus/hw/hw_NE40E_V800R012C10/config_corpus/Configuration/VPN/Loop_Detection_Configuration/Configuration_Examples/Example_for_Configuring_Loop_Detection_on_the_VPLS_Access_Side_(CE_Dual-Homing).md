Example for Configuring Loop Detection on the VPLS Access Side (CE Dual-Homing)
===============================================================================

In a CE dual-homing scenario, a CE is dual-homed to PE1 and PE2 through a switch. Together, PE1, PE2, and the switch form a physical ring network. To enable the devices to promptly eliminate loops and prevent subsequent broadcast storms in this case, you can deploy loop detection on the AC interfaces of PE1 and PE2 and specify blocking priorities for the interfaces on the primary and backup links.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001738472312__fig7798133616113), CE1 is dual-homed to PE1 and PE2 through a switch, and CE2 is directly connected to PE3. CE1 and CE2 belong to the same VPLS network. PWs are established with LDP as the VPLS signaling protocol, and VPLS is configured for CE1 and CE2 to communicate. Loop detection needs to be configured on PE1 and PE2 to prevent broadcast storms caused by loops formed by PE1, PE2, and the switch. The link between the switch and PE1 is the primary link, and that between the switch and PE2 is the backup link, which is blocked. If the primary link fails and no loop is detected on the backup link within the configured period of 10s, the backup link takes over traffic.

**Figure 1** Network diagram of configuring loop detection on the VPLS access side (CE dual-homing)![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, interface3, interface4, interface5, and subinterface1.1 represent GE0/1/0, GE0/2/0, GE0/3/0, GE0/1/1, GE0/1/2, and GE0/1/0.1, respectively.


  
![](figure/en-us_image_0000001785392445.png)
#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a routing protocol on the backbone network for communication between devices.
2. Establish a remote LDP session between PEs.
3. Enable MPLS L2VPN on PEs.
4. Create VSIs, set the signaling protocol to LDP, and bind AC interfaces to VSIs on PEs.
5. Configure loop detection on the AC interfaces of PEs.

#### Data Preparation

To complete the configuration, you need the following data:

* VSI names and IDs
* Peer IP addresses and the tunnels used for setting up peer relationships
* Names of interfaces bound to VSIs
* Blocking priority and detection interval for unblocking an interface


#### Procedure

1. Configure IP addresses.
   
   
   
   Configure IP addresses for involved physical interfaces and loopback interfaces according to [Figure 1](#EN-US_TASK_0000001738472312__fig7798133616113).
   
   For detailed configurations, see [Configuration Files](#EN-US_TASK_0000001738472312__li18927104101117).
2. Configure an IGP on the MPLS backbone network. OSPF is used in this example.
   
   
   
   During OSPF configuration, the 32-bit loopback addresses of PEs and the P must be advertised.
   
   For detailed configurations, see [Configuration Files](#EN-US_TASK_0000001738472312__li18927104101117).
3. Configure basic MPLS functions and LDP.
   
   
   
   # Configure PE1.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE1
   ```
   ```
   [*PE1] mpls lsr-id 1.1.1.1
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
   [*PE1] interface GigabitEthernet 0/2/0
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] mpls ldp
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] quit
   ```
   
   
   
   # Configure PE2.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE2
   ```
   ```
   [*PE2] mpls lsr-id 2.2.2.2
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
   [*PE2] interface GigabitEthernet 0/2/0
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] mpls ldp
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] quit
   ```
   
   
   
   # Configure the P.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname P
   ```
   ```
   [*P] mpls lsr-id 3.3.3.3
   ```
   ```
   [*P] mpls
   ```
   ```
   [*P-mpls] quit
   ```
   ```
   [*P] mpls ldp
   ```
   ```
   [*P-mpls-ldp] quit
   ```
   ```
   [*P] interface GigabitEthernet 0/1/0
   ```
   ```
   [*P-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*P-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*P-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*P-GigabitEthernet0/1/0] quit
   ```
   ```
   [*P] interface GigabitEthernet 0/2/0
   ```
   ```
   [*P-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*P-GigabitEthernet0/2/0] mpls ldp
   ```
   ```
   [*P-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [*P-GigabitEthernet0/2/0] quit
   ```
   ```
   [*P] interface GigabitEthernet 0/3/0
   ```
   ```
   [*P-GigabitEthernet0/3/0] mpls
   ```
   ```
   [*P-GigabitEthernet0/3/0] mpls ldp
   ```
   ```
   [*P-GigabitEthernet0/3/0] undo shutdown
   ```
   ```
   [*P-GigabitEthernet0/3/0] quit
   ```
   
   
   
   # Configure PE3.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE3
   ```
   ```
   [*PE3] mpls lsr-id 4.4.4.4
   ```
   ```
   [*PE3] mpls
   ```
   ```
   [*PE3-mpls] quit
   ```
   ```
   [*PE3] mpls ldp
   ```
   ```
   [*PE3-mpls-ldp] quit
   ```
   ```
   [*PE3] interface GigabitEthernet 0/2/0
   ```
   ```
   [*PE3-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*PE3-GigabitEthernet0/2/0] mpls ldp
   ```
   ```
   [*PE3-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [*PE3-GigabitEthernet0/2/0] quit
   ```
4. Establish remote LDP sessions between PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] mpls ldp remote-peer pe2
   ```
   ```
   [*PE1-mpls-ldp-remote-pe2] remote-ip 2.2.2.2
   ```
   ```
   [*PE1-mpls-ldp-remote-pe2] quit
   ```
   ```
   [*PE1] mpls ldp remote-peer pe3
   ```
   ```
   [*PE1-mpls-ldp-remote-pe3] remote-ip 4.4.4.4
   ```
   ```
   [*PE1-mpls-ldp-remote-pe3] quit
   ```
   
   
   
   # Configure PE2.
   
   ```
   [~PE2] mpls ldp remote-peer pe1
   ```
   ```
   [*PE2-mpls-ldp-remote-pe1] remote-ip 1.1.1.1
   ```
   ```
   [*PE2-mpls-ldp-remote-pe1] quit
   ```
   ```
   [*PE2] mpls ldp remote-peer pe3
   ```
   ```
   [*PE2-mpls-ldp-remote-pe3] remote-ip 4.4.4.4
   ```
   ```
   [*PE2-mpls-ldp-remote-pe3] quit
   ```
   
   
   
   # Configure PE3.
   
   ```
   [~PE3] mpls ldp remote-peer pe1
   ```
   ```
   [*PE3-mpls-ldp-remote-pe1] remote-ip 1.1.1.1
   ```
   ```
   [*PE3-mpls-ldp-remote-pe1] quit
   ```
   ```
   [*PE3] mpls ldp remote-peer pe2
   ```
   ```
   [*PE3-mpls-ldp-remote-pe2] remote-ip 2.2.2.2
   ```
   ```
   [*PE3-mpls-ldp-remote-pe2] quit
   ```
5. Enable MPLS L2VPN on PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] mpls l2vpn
   ```
   ```
   [*PE1-l2vpn] quit
   ```
   
   
   
   # Configure PE2.
   
   ```
   [~PE2] mpls l2vpn
   ```
   ```
   [*PE2-l2vpn] quit
   ```
6. Create VSIs, set the signaling protocol to LDP, and bind AC interfaces to VSIs on PEs.
   
   
   
   # Configure PE1.
   
   
   
   ```
   [~PE1] vsi a2 static
   ```
   ```
   [*PE1-vsi-a2] pwsignal ldp
   ```
   ```
   [*PE1-vsi-a2-ldp] vsi-id 2
   ```
   ```
   [*PE1-vsi-a2-ldp] peer 2.2.2.2
   ```
   ```
   [*PE1-vsi-a2-ldp] peer 4.4.4.4
   ```
   ```
   [*PE1-vsi-a2-ldp] mac-withdraw enable
   ```
   ```
   [*PE1-vsi-a2-ldp] interface-status-change mac-withdraw enable
   ```
   ```
   [*PE1-vsi-a2-ldp] quit
   ```
   ```
   [*PE1-vsi-a2] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/1/0.1
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
   
   
   
   # Configure PE2.
   
   
   
   ```
   [~PE2] vsi a2 static
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
   [*PE2-vsi-a2-ldp] peer 4.4.4.4
   ```
   ```
   [*PE2-vsi-a2-ldp] mac-withdraw enable
   ```
   ```
   [*PE2-vsi-a2-ldp] interface-status-change mac-withdraw enable
   ```
   ```
   [*PE2-vsi-a2-ldp] quit
   ```
   ```
   [*PE2-vsi-a2] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/1/0.1
   ```
   ```
   [*PE2-GigabitEthernet0/1/0.1] shutdown
   ```
   ```
   [*PE2-GigabitEthernet0/1/0.1] vlan-type dot1q 10
   ```
   ```
   [*PE2-GigabitEthernet0/1/0.1] l2 binding vsi a2
   ```
   ```
   [*PE2-GigabitEthernet0/1/0.1] undo shutdown
   ```
   ```
   [*PE2-GigabitEthernet0/1/0.1] quit
   ```
   
   
   
   # Configure PE3.
   
   
   
   ```
   [~PE3] mpls l2vpn
   ```
   ```
   [*PE3-l2vpn] quit
   ```
   ```
   [*PE3] vsi a2 static
   ```
   ```
   [*PE3-vsi-a2] pwsignal ldp
   ```
   ```
   [*PE3-vsi-a2-ldp] vsi-id 2
   ```
   ```
   [*PE3-vsi-a2-ldp] peer 1.1.1.1
   ```
   ```
   [*PE3-vsi-a2-ldp] peer 2.2.2.2
   ```
   ```
   [*PE3-vsi-a2-ldp] mac-withdraw enable
   ```
   ```
   [*PE3-vsi-a2-ldp] interface-status-change mac-withdraw enable
   ```
   ```
   [*PE3-vsi-a2-ldp] quit
   ```
   ```
   [*PE3-vsi-a2] quit
   ```
   ```
   [*PE3] interface gigabitethernet 0/1/0.1
   ```
   ```
   [*PE3-GigabitEthernet0/1/0.1] shutdown
   ```
   ```
   [*PE3-GigabitEthernet0/1/0.1] vlan-type dot1q 10
   ```
   ```
   [*PE3-GigabitEthernet0/1/0.1] l2 binding vsi a2
   ```
   ```
   [*PE3-GigabitEthernet0/1/0.1] undo shutdown
   ```
   ```
   [*PE3-GigabitEthernet0/1/0.1] quit
   ```
   
   
   
   After the configuration is complete, check VSI connection information on a PE. The command output shows that two PWs have been successfully established.
   
   The following example uses the command output on PE1.
   ```
   [~PE1] display vsi name a2 verbose
   ***VSI Name               : a2
       Administrator VSI      : no
       Isolate Spoken         : disable
       VSI Index              : 0
       PW Signaling           : ldp
       Member Discovery Style : static
       PW MAC Learn Style     : unqualify
       Encapsulation Type     : vlan
       MTU                    : 1500
       Diffserv Mode          : uniform
       Service Class          : --
       Color                  : --
       DomainId               : 255
       Domain Name            :
       Create Time            : 1 days, 15 hours, 11 minutes, 4 seconds
       VSI State              : up
       VSI ID                 : 2
      *Peer Router ID         : 2.2.2.2
       VC Label               : 23552
       Peer Type              : dynamic
       Session                : up
       Tunnel ID              : 0x1002000,
      *Peer Router ID         : 4.4.4.4
       VC Label               : 23553
       Peer Type              : dynamic
       Session                : up
       Tunnel ID              : 0x1002002,
       Interface Name         : GigabitEthernet0/1/0.1
       State                  : up
       Last Up Time           : 2020/10/27 18:10:44
       Total Up Time          : 1 days, 16 hours, 53 minutes, 33 seconds
      **PW Information:
      *Peer Ip Address        : 2.2.2.2
       PW State               : up
       Local VC Label         : 23552
       Remote VC Label        : 23552
       PW Type                : label
       Tunnel ID              : 0x1002000
      *Peer Ip Address        : 4.4.4.4
       PW State               : up
       Local VC Label         : 23553
       Remote VC Label        : 23552
       PW Type                : label
       Tunnel ID              : 0x1002002
       FIB Link-ID            : 1
       PW Last Up Time        : 2020/10/28 10:03:35
       PW Total Up Time       : 0 days, 11 hours, 15 minutes, 38 seconds
   ```
7. Configure CEs to access the VPLS network.
   
   
   
   # Configure the switch.
   
   Create VLAN 10 on the switch and add GE0/1/0, GE0/1/1, and GE0/1/2 to VLAN 10.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname Switch
   ```
   ```
   [*Switch] vlan 10
   ```
   ```
   [*Switch-vlan10] quit
   ```
   ```
   [*Switch] interface gigabitethernet 0/1/0
   ```
   ```
   [*Switch-GigabitEthernet0/1/0] port trunk allow-pass vlan 10
   ```
   ```
   [*Switch-GigabitEthernet0/1/0] quit
   ```
   ```
   [*Switch] interface gigabitethernet 0/1/1
   ```
   ```
   [*Switch-GigabitEthernet0/1/1] port trunk allow-pass vlan 10
   ```
   ```
   [*Switch-GigabitEthernet0/1/1] quit
   ```
   ```
   [*Switch] interface gigabitethernet 0/1/2
   ```
   ```
   [*Switch-GigabitEthernet0/1/2] port trunk allow-pass vlan 10
   ```
   ```
   [*Switch-GigabitEthernet0/1/2] quit
   ```
   
   
   
   # Configure CE1.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname CE1
   ```
   ```
   [*CE1] interface gigabitethernet 0/1/0.1
   ```
   ```
   [*CE1-GigabitEthernet0/1/0.1] vlan-type dot1q 10
   ```
   ```
   [*CE1-GigabitEthernet0/1/0.1] ip address 192.168.1.1 24
   ```
   ```
   [*CE1-GigabitEthernet0/1/0.1] quit
   ```
   
   
   
   # Configure CE2.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname CE2
   ```
   ```
   [*CE2] interface gigabitethernet 0/1/0.1
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.1] vlan-type dot1q 10
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.1] ip address 192.168.1.2 24
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.1] quit
   ```
8. Configure loop detection on PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] loop-detection enable
   ```
   ```
   [*PE1] interface gigabitethernet0/1/0.1
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] loop-detect enable
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] loop-detect block 10
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] loop-detect priority 2
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] loop-detect trigger interface-down enable
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] quit
   ```
   
   
   
   # Configure PE2.
   
   ```
   [~PE2] loop-detection enable
   ```
   ```
   [*PE2] interface gigabitethernet0/1/0.1
   ```
   ```
   [*PE2-GigabitEthernet0/1/0.1] loop-detect enable
   ```
   ```
   [*PE2-GigabitEthernet0/1/0.1] loop-detect block 10
   ```
   ```
   [*PE2-GigabitEthernet0/1/0.1] loop-detect priority 1
   ```
   ```
   [*PE2-GigabitEthernet0/1/0.1] loop-detect trigger interface-down enable
   ```
   ```
   [*PE2-GigabitEthernet0/1/0.1] quit
   ```
9. Verify the configuration.
   
   
   
   After the configuration is complete, run the [**display loop-detect block all**](cmdqueryname=display+loop-detect+block+all) command on PE1 and PE2. The command output shows that GE0/1/0.1 on PE2 is already blocked.
   
   ```
   [~PE1] display loop-detect block all
   Info: There is no block interface in this router.
   ```
   ```
   [~PE2] display loop-detect block all
   Info: GigabitEthernet0/1/0.1 has been blocked.
   ```
   
   
   
   CE1 (192.168.1.1) can ping CE2 (192.168.1.2).
   
   ```
   [~CE1] ping 192.168.1.2
   PING 192.168.1.2: 56  data bytes, press CTRL_C to break
       Reply from 192.168.1.2: bytes=56 Sequence=1 ttl=255 time=90 ms
       Reply from 192.168.1.2: bytes=56 Sequence=2 ttl=255 time=77 ms
       Reply from 192.168.1.2: bytes=56 Sequence=3 ttl=255 time=34 ms
       Reply from 192.168.1.2: bytes=56 Sequence=4 ttl=255 time=46 ms
       Reply from 192.168.1.2: bytes=56 Sequence=5 ttl=255 time=94 ms
     --- 192.168.1.2 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 34/68/94 ms
   ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
   sysname PE1
  #
   mpls lsr-id 1.1.1.1
   mpls
  #
   mpls l2vpn
  #
  vsi a2 static 
   pwsignal ldp 
    vsi-id 2
    peer 2.2.2.2
    peer 4.4.4.4
    mac-withdraw enable
    interface-status-change mac-withdraw enable
  #
  mpls ldp
  #
  mpls ldp remote-peer pe2
   remote-ip 2.2.2.2
  #
  mpls ldp remote-peer pe3
   remote-ip 4.4.4.4
  #
  loop-detection enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
  #
  interface GigabitEthernet0/1/0.1
   vlan-type dot1q 10
   l2 binding vsi a2
   loop-detect enable
   loop-detect block 10
   loop-detect priority 2
   loop-detect trigger interface-down enable
  #
  interface GigabitEthernet0/2/0
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

* PE2 configuration file
  
  ```
  #
   sysname PE2
  #
   mpls lsr-id 2.2.2.2
   mpls
  #
   mpls l2vpn
  #
  vsi a2 static
   pwsignal ldp
    vsi-id 2
    peer 1.1.1.1
    peer 4.4.4.4
    mac-withdraw enable
    interface-status-change mac-withdraw enable
  #
  mpls ldp
  #
  mpls ldp remote-peer pe1
   remote-ip 1.1.1.1
  #
  mpls ldp remote-peer pe3
   remote-ip 4.4.4.4
  #
  loop-detection enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
  #
  interface GigabitEthernet0/1/0.1
   vlan-type dot1q 10
   l2 binding vsi a2
   loop-detect enable
   loop-detect block 10
   loop-detect priority 1
   loop-detect trigger interface-down enable
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.2.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 10.2.1.0 0.0.0.255
  #
  return
  ```

* P configuration file
  
  ```
  #
   sysname P
  #
   mpls lsr-id 3.3.3.3
   mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.3.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 10.2.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
  #
  ospf 1
   area 0.0.0.0
    network 3.3.3.3 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.2.1.0 0.0.0.255
    network 10.3.1.0 0.0.0.255
  #
  return
  ```

* PE3 configuration file
  
  ```
  #
   sysname PE3
  #
   mpls lsr-id 4.4.4.4
   mpls
  #
   mpls l2vpn
  #
  vsi a2 static
   pwsignal ldp
    vsi-id 2
    peer 1.1.1.1
    peer 2.2.2.2
    mac-withdraw enable
    interface-status-change mac-withdraw enable
  #
  mpls ldp
  #
  mpls ldp remote-peer pe1
   remote-ip 1.1.1.1
  #
  mpls ldp remote-peer pe2
   remote-ip 2.2.2.2
  #
  interface GigabitEthernet0/1/0
   undo shutdown
  #
  interface GigabitEthernet0/1/0.1
   vlan-type dot1q 10
   l2 binding vsi a2
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.3.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 4.4.4.4 255.255.255.255
  #
  ospf 1
   area 0.0.0.0
    network 4.4.4.4 0.0.0.0
    network 10.3.1.0 0.0.0.255
  #
  return
  ```

* CE1 configuration file
  
  ```
  #
   sysname CE1
  #
  interface GigabitEthernet0/1/0
   undo shutdown
  #
  interface GigabitEthernet0/1/0.1
   vlan-type dot1q 10
   ip address 192.168.1.1 255.255.255.0
  #
  return
  ```

* CE2 configuration file
  
  ```
  #
   sysname CE2
  #
  interface GigabitEthernet0/1/0
   undo shutdown
  #
  interface GigabitEthernet0/1/0.1
   vlan-type dot1q 10
   ip address 192.168.1.2 255.255.255.0
  #
  return
  ```

* Switch configuration file
  
  ```
  #
   sysname Switch
  #
   vlan batch 10
  #
  interface GigabitEthernet0/1/0
   port trunk allow-pass vlan 10
  #
  interface GigabitEthernet0/1/1
   port trunk allow-pass vlan 10
  #
  interface GigabitEthernet0/1/2
   port trunk allow-pass vlan 10
  #
  return
  ```