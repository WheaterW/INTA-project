Example for Configuring VPLS over SR-MPLS TE
============================================

The public network tunnel to which LDP VPLS recurses can be an SR-MPLS TE tunnel.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172368878__en-us_task_0172370251_fig_dc_vrp_vpls_cfg_508001), CE1 and CE2 belong to the same VPLS network and access the MPLS backbone network through PE1 and PE2, respectively. OSPF is used as the IGP on the MPLS backbone network.

LDP VPLS needs to be configured, and an SR-MPLS TE tunnel needs to be established between PE1 and PE2 to carry the VPLS service.

**Figure 1** Configuring LDP VPLS to recurse to an SR-MPLS TE tunnel![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, subinterface1.1, and subinterface2.1 represent GE0/1/0, GE0/2/0, GE0/1/0.1, and GE0/2/0.1, respectively.


  
![](images/fig_dc_vrp_vpls_cfg_508001.png)  


#### Configuration Precautions

During the configuration, note the following:

* PEs belonging to the same VPLS network must have the same VSI ID.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a routing protocol on the PEs and P of the backbone network for connectivity between these devices and enable MPLS on them.
2. Set up an SR-MPLS TE tunnel and configure the related tunnel policy. For details about how to establish an SR-MPLS TE tunnel, see the *NE40E Configuration Guide - Segment Routing*.
3. Enable MPLS L2VPN on PEs.
4. Create VSIs, set the signaling protocol to LDP, and bind AC interfaces to VSIs on PEs.
5. Configure the VSI to use an SR-MPLS TE tunnel.

#### Data Preparation

To complete the configuration, you need the following data:

* OSPF area where SR-MPLS TE is enabled
* VSI names and IDs
* Peer IP addresses and tunnel policies
* Interfaces bound to VSIs

#### Procedure

1. Configure IP addresses for involved interfaces on the backbone network.
   
   
   
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
   [*PE1] interface gigabitethernet0/1/0
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] ip address 10.10.1.1 24
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure the P.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname P
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~P] interface loopback 1
   ```
   ```
   [*P-LoopBack1] ip address 2.2.2.9 32
   ```
   ```
   [*P-LoopBack1] quit
   ```
   ```
   [*P] interface gigabitethernet0/1/0
   ```
   ```
   [*P-GigabitEthernet0/1/0] ip address 10.10.1.2 24
   ```
   ```
   [*P-GigabitEthernet0/1/0] quit
   ```
   ```
   [*P] interface gigabitethernet0/2/0
   ```
   ```
   [*P-GigabitEthernet0/2/0] ip address 10.20.1.1 24
   ```
   ```
   [*P-GigabitEthernet0/2/0] quit
   ```
   ```
   [*P] commit
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
   [*PE2-LoopBack1] ip address 3.3.3.9 32
   ```
   ```
   [*PE2-LoopBack1] quit
   ```
   ```
   [*PE2] interface gigabitethernet0/1/0
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] ip address 10.20.1.2 24
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE2] commit
   ```
2. Enable MPLS and MPLS TE.
   
   
   
   Enable MPLS and MPLS TE in the system view of each node along the tunnel.
   
   # Configure PE1.
   
   ```
   [~PE1] mpls lsr-id 1.1.1.9
   ```
   ```
   [*PE1] mpls
   ```
   ```
   [*PE1-mpls] mpls te
   ```
   ```
   [*PE1-mpls] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure the P.
   
   ```
   [~P] mpls lsr-id 2.2.2.9
   ```
   ```
   [*P] mpls
   ```
   ```
   [*P-mpls] mpls te
   ```
   ```
   [*P-mpls] quit
   ```
   ```
   [*P] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] mpls lsr-id 3.3.3.9
   ```
   ```
   [*PE2] mpls
   ```
   ```
   [*PE2-mpls] mpls te
   ```
   ```
   [*PE2-mpls] quit
   ```
   ```
   [*PE2] commit
   ```
3. Configure OSPF TE on the backbone network.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] ospf 1
   ```
   ```
   [*PE1-ospf-1] opaque-capability enable
   ```
   ```
   [*PE1-ospf-1] area 0.0.0.0
   ```
   ```
   [*PE1-ospf-1-area-0.0.0.0] network 1.1.1.9 0.0.0.0
   ```
   ```
   [*PE1-ospf-1-area-0.0.0.0] network 10.10.1.0 0.0.0.255
   ```
   ```
   [*PE1-ospf-1-area-0.0.0.0] mpls-te enable
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
   
   # Configure the P.
   
   ```
   [~P] ospf 1
   ```
   ```
   [*P-ospf-1] opaque-capability enable
   ```
   ```
   [*P-ospf-1] area 0.0.0.0
   ```
   ```
   [*P-ospf-1-area-0.0.0.0] network 2.2.2.9 0.0.0.0
   ```
   ```
   [*P-ospf-1-area-0.0.0.0] network 10.10.1.0 0.0.0.255
   ```
   ```
   [*P-ospf-1-area-0.0.0.0] network 10.20.1.0 0.0.0.255
   ```
   ```
   [*P-ospf-1-area-0.0.0.0] mpls-te enable
   ```
   ```
   [*P-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [*P-ospf-1] quit
   ```
   ```
   [*P] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] ospf 1
   ```
   ```
   [*PE2-ospf-1] opaque-capability enable
   ```
   ```
   [*PE2-ospf-1] area 0.0.0.0
   ```
   ```
   [*PE2-ospf-1-area-0.0.0.0] network 3.3.3.9 0.0.0.0
   ```
   ```
   [*PE2-ospf-1-area-0.0.0.0] network 10.20.1.0 0.0.0.255
   ```
   ```
   [*PE2-ospf-1-area-0.0.0.0] mpls-te enable
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
4. Configure SR on the backbone network.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] segment-routing
   ```
   ```
   [*PE1-segment-routing] quit
   ```
   ```
   [*PE1] ospf 1
   ```
   ```
   [*PE1-ospf-1] segment-routing mpls
   ```
   ```
   [*PE1-ospf-1] segment-routing global-block 16000 47999
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The SRGB range varies according to the device. The range specified in this example is for reference only.
   
   ```
   [*PE1-ospf-1] quit
   ```
   ```
   [*PE1] interface loopback 1
   ```
   ```
   [*PE1-LoopBack1] ospf prefix-sid absolute 16100
   ```
   ```
   [*PE1-LoopBack1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure the P.
   
   ```
   [~P] segment-routing
   ```
   ```
   [*P-segment-routing] quit
   ```
   ```
   [*P] ospf 1
   ```
   ```
   [*P-ospf-1] segment-routing mpls
   ```
   ```
   [*P-ospf-1] segment-routing global-block 16000 47999
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The SRGB range varies according to the device. The range specified in this example is for reference only.
   
   ```
   [*P-ospf-1] quit
   ```
   ```
   [*P] interface loopback 1
   ```
   ```
   [*P-LoopBack1] ospf prefix-sid absolute 16300
   ```
   ```
   [*P-LoopBack1] quit
   ```
   ```
   [*P] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] segment-routing
   ```
   ```
   [*PE2-segment-routing] quit
   ```
   ```
   [*PE2] ospf 1
   ```
   ```
   [*PE2-ospf-1] segment-routing mpls
   ```
   ```
   [*PE2-ospf-1] segment-routing global-block 16000 47999
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The SRGB range varies according to the device. The range specified in this example is for reference only.
   
   ```
   [*PE2-ospf-1] quit
   ```
   ```
   [*PE2] interface loopback 1
   ```
   ```
   [*PE2-LoopBack1] ospf prefix-sid absolute 16200
   ```
   ```
   [*PE2-LoopBack1] quit
   ```
   ```
   [*PE2] commit
   ```
5. Configure an explicit path.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] explicit-path path2pe2
   ```
   ```
   [*PE1-explicit-path-path2pe2] next sid label 16300 type prefix
   ```
   ```
   [*PE1-explicit-path-path2pe2] next sid label 16200 type prefix
   ```
   ```
   [*PE1-explicit-path-path2pe2] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] explicit-path path2pe1
   ```
   ```
   [*PE2-explicit-path-path2pe1] next sid label 16300 type prefix
   ```
   ```
   [*PE2-explicit-path-path2pe1] next sid label 16100 type prefix
   ```
   ```
   [*PE2-explicit-path-path2pe1] quit
   ```
   ```
   [*PE2] commit
   ```
6. Configure a tunnel interface on each device.
   
   
   
   # Create tunnel interfaces on PEs and specify MPLS TE as the tunnel protocol and SR as the signaling protocol.
   
   # Configure PE1.
   
   ```
   [~PE1] interface Tunnel 10
   ```
   ```
   [*PE1-Tunnel10] ip address unnumbered interface loopback1
   ```
   ```
   [*PE1-Tunnel10] tunnel-protocol mpls te
   ```
   ```
   [*PE1-Tunnel10] destination 3.3.3.9
   ```
   ```
   [*PE1-Tunnel10] mpls te signal-protocol segment-routing
   ```
   ```
   [*PE1-Tunnel10] mpls te tunnel-id 100
   ```
   ```
   [*PE1-Tunnel10] mpls te path explicit-path path2pe2
   ```
   ```
   [*PE1-Tunnel10] mpls te reserved-for-binding
   ```
   ```
   [*PE1-Tunnel10] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] interface Tunnel 10
   ```
   ```
   [*PE2-Tunnel10] ip address unnumbered interface loopback1
   ```
   ```
   [*PE2-Tunnel10] tunnel-protocol mpls te
   ```
   ```
   [*PE2-Tunnel10] destination 1.1.1.9
   ```
   ```
   [*PE2-Tunnel10] mpls te signal-protocol segment-routing
   ```
   ```
   [*PE2-Tunnel10] mpls te tunnel-id 100
   ```
   ```
   [*PE2-Tunnel10] mpls te path explicit-path path2pe1
   ```
   ```
   [*PE2-Tunnel10] mpls te reserved-for-binding
   ```
   ```
   [*PE2-Tunnel10] quit
   ```
   ```
   [*PE2] commit
   ```
   
   Run the **display tunnel-info all** command in the system view. The command output shows that the TE tunnel whose destination address is the MPLS LSR ID of the peer PE exists. The following example uses the command output on PE1.
   
   ```
   [~PE1] display tunnel-info all
   ```
   ```
   Tunnel ID                     Type                Destination         Status
   -----------------------------------------------------------------------------
   0x000000000300000001          sr-te               3.3.3.9             UP
   ```
7. Configure remote LDP sessions.
   
   
   
   Set up a remote peer session between PE1 and PE2.
   
   # Configure PE1.
   
   ```
   [~PE1] mpls ldp
   ```
   ```
   [*PE1-mpls-ldp] quit
   ```
   ```
   [*PE1] mpls ldp remote-peer 3.3.3.9
   ```
   ```
   [*PE1-mpls-ldp-remote-3.3.3.9] remote-ip 3.3.3.9
   ```
   ```
   [*PE1-mpls-ldp-remote-3.3.3.9] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] mpls ldp
   ```
   ```
   [*PE2-mpls-ldp] quit
   ```
   ```
   [*PE2] mpls ldp remote-peer 1.1.1.9
   ```
   ```
   [*PE2-mpls-ldp-remote-1.1.1.9] remote-ip 1.1.1.9
   ```
   ```
   [*PE2-mpls-ldp-remote-1.1.1.9] quit
   ```
   ```
   [*PE2] commit
   ```
8. Configure a tunnel policy.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] tunnel-policy policy1
   ```
   ```
   [*PE1-tunnel-policy-policy1] tunnel binding destination 3.3.3.9 te Tunnel10
   ```
   ```
   [*PE1-tunnel-policy-policy1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] tunnel-policy policy1
   ```
   ```
   [*PE2-tunnel-policy-policy1] tunnel binding destination 1.1.1.9 te Tunnel10
   ```
   ```
   [*PE2-tunnel-policy-policy1] quit
   ```
   ```
   [*PE2] commit
   ```
9. Enable MPLS L2VPN on PEs.
   
   
   
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
10. Create a VSI on each PE and configure a tunnel policy for the VSI.
    
    
    
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
    [*PE1-vsi-a2-ldp] peer 3.3.3.9 tnl-policy policy1
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
    [*PE2-vsi-a2-ldp] peer 1.1.1.9 tnl-policy policy1
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
11. Bind interfaces to VSIs on PEs.
    
    
    
    # Configure PE1.
    
    ```
    [~PE1] interface gigabitethernet0/2/0.1
    ```
    ```
    [*PE1-GigabitEthernet0/2/0.1] vlan-type dot1q 10
    ```
    ```
    [*PE1-GigabitEthernet0/2/0.1] l2 binding vsi a2
    ```
    ```
    [*PE1-GigabitEthernet0/2/0.1] quit
    ```
    ```
    [*PE1] commit
    ```
    
    # Configure PE2.
    
    ```
    [~PE2] interface gigabitethernet0/2/0.1
    ```
    ```
    [*PE2-GigabitEthernet0/2/0.1] vlan-type dot1q 10
    ```
    ```
    [*PE2-GigabitEthernet0/2/0.1] l2 binding vsi a2
    ```
    ```
    [*PE2-GigabitEthernet0/2/0.1] quit
    ```
    ```
    [*PE2] commit
    ```
    
    # Configure CE1.
    
    ```
    [~CE1] interface gigabitethernet0/1/0.1
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
12. Verify the configuration.
    
    
    
    After the configuration is complete, run the **display vsi name a2 verbose** command on PE1. The command output shows that a VSI named **a2** has established a PW to PE2 and **VSI State** is **up**.
    
    ```
    [~PE1] display vsi name a2 verbose
    ```
    ```
     ***VSI Name               : a2
        Work Mode              : normal
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
        Create Time            : 1 days, 8 hours, 46 minutes, 34 seconds
        VSI State              : up
        Resource Status        : --
    
        VSI ID                 : 2
       *Peer Router ID         : 3.3.3.9
        Negotiation-vc-id      : 2
        Encapsulation Type     : vlan
        primary or secondary   : primary
        ignore-standby-state   : no
        VC Label               : 18
        Peer Type              : dynamic
        Session                : up
        Tunnel ID              : 0x000000000300000001
        Broadcast Tunnel ID    : --
        Broad BackupTunnel ID  : --
        Tunnel Policy Name     : policy1
        CKey                   : 33
        NKey                   : 1610612843
        Stp Enable             : 0
        PwIndex                : 0
        Control Word           : disable
        BFD for PW             : unavailable
    
        Interface Name         : GigabitEthernet0/2/0.1
        State                  : up
        Ac Block State         : unblocked
        Access Port            : false
        Last Up Time           : 2012/09/10 10:14:46
        Total Up Time          : 1 days, 8 hours, 41 minutes, 37 seconds
    
      **PW Information:
    
       *Peer Ip Address        : 3.3.3.9
        PW State               : up
        Local VC Label         : 18
        Remote VC Label        : 18
        Remote Control Word    : disable
        PW Type                : label
        Local  VCCV            : alert lsp-ping bfd
        Remote VCCV            : alert lsp-ping bfd
        Tunnel ID              : 0x000000000300000001
        Broadcast Tunnel ID    : --
        Broad BackupTunnel ID  : --
        Ckey                   : 33
        Nkey                   : 1610612843
        Main PW Token          : 0x0
        Slave PW Token         : 0x0
        Tnl Type               : te
        OutInterface           : Tunnel10
        Backup OutInterface    : --
        Stp Enable             : 0
        Mac Flapping           : 0
        Monitor Group Name     : --
        PW Last Up Time        : 2012/09/11 09:19:12
        PW Total Up Time       : 1 days, 6 hours, 52 minutes, 3 seconds 
    ```
    
    Run the [**display vsi pw out-interface vsi a2**](cmdqueryname=display+vsi+pw+out-interface+vsi+a2) command on PE1. The command output shows that the outbound interface of the MPLS TE tunnel between 1.1.1.9 and 3.3.3.9 is Tunnel10.
    
    ```
    [~PE1] display vsi pw out-interface vsi a2
    ```
    ```
    Total: 1
    --------------------------------------------------------------------------------
    Vsi Name                        peer            vcid       interface
    --------------------------------------------------------------------------------
    a2                              3.3.3.9         2          Tunnel10
    ```
    
    CE1 and CE2 can ping each other.
    
    ```
    [~CE1] ping 10.1.1.2
    ```
    ```
      PING 10.1.1.2: 56  data bytes, press CTRL_C to break
    ```
    ```
        Reply from 10.1.1.2: bytes=56 Sequence=1 ttl=255 time=125 ms
    ```
    ```
        Reply from 10.1.1.2: bytes=56 Sequence=2 ttl=255 time=125 ms
    ```
    ```
        Reply from 10.1.1.2: bytes=56 Sequence=3 ttl=255 time=94 ms
    ```
    ```
        Reply from 10.1.1.2: bytes=56 Sequence=4 ttl=255 time=125 ms
    ```
    ```
        Reply from 10.1.1.2: bytes=56 Sequence=5 ttl=255 time=125 ms
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
        round-trip min/avg/max = 94/118/125 ms
    ```

#### Configuration Files

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
   ip address 10.1.1.1 255.255.255.0
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
   mpls te
  #
  mpls l2vpn
  #
  vsi a2
   pwsignal ldp
    vsi-id 2
    peer 3.3.3.9 tnl-policy policy1
  #
  explicit-path path2pe2
   next sid label 16300 type prefix index 1
   next sid label 16200 type prefix index 2
  #
  mpls ldp
   #
   ipv4-family
  #
  mpls ldp remote-peer 3.3.3.9
   remote-ip 3.3.3.9
  #
  segment-routing
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.10.1.1 255.255.255.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
  #
  interface GigabitEthernet0/2/0.1
   vlan-type dot1q 10
   l2 binding vsi a2
  #
  interface LoopBack1
   ip address 1.1.1.9 255.255.255.255
   ospf prefix-sid absolute 16100
  #
  interface Tunnel10
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 3.3.3.9
   mpls te signal-protocol segment-routing
   mpls te reserved-for-binding
   mpls te tunnel-id 100
   mpls te path explicit-path path2pe2
  #
  ospf 1
   opaque-capability enable
   segment-routing mpls
   segment-routing global-block 16000 47999
   area 0.0.0.0
    network 1.1.1.9 0.0.0.0
    network 10.10.1.0 0.0.0.255
    mpls-te enable
  #
  tunnel-policy policy1
   tunnel binding destination 3.3.3.9 te Tunnel10
  #
  return
  ```
* P configuration file
  
  ```
  #
  sysname P
  #
  mpls lsr-id 2.2.2.9
  #
  mpls
   mpls te
  #
  segment-routing
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.10.1.2 255.255.255.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.20.1.1 255.255.255.0
  #
  interface LoopBack1
   ip address 2.2.2.9 255.255.255.255
   ospf prefix-sid absolute 16300
  #
  ospf 1
   opaque-capability enable
   segment-routing mpls
   segment-routing global-block 16000 47999
   area 0.0.0.0
    network 2.2.2.9 0.0.0.0
    network 10.10.1.0 0.0.0.255
    network 10.20.1.0 0.0.0.255
    mpls-te enable
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  mpls lsr-id 3.3.3.9
  #
  mpls
   mpls te
  #
  mpls l2vpn
  #
  vsi a2
   pwsignal ldp
    vsi-id 2      
    peer 1.1.1.9 tnl-policy policy1 
  #
  explicit-path path2pe1
   next sid label 16300 type prefix index 1
   next sid label 16100 type prefix index 2
  #
  mpls ldp
   #
   ipv4-family
  #
  mpls ldp remote-peer 1.1.1.9
   remote-ip 1.1.1.9
  #
  segment-routing
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.20.1.2 255.255.255.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
  #
  interface GigabitEthernet0/2/0.1
   vlan-type dot1q 10
   l2 binding vsi a2
  #
  interface LoopBack1
   ip address 3.3.3.9 255.255.255.255
   ospf prefix-sid absolute 16200
  #
  interface Tunnel10
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 1.1.1.9
   mpls te signal-protocol segment-routing
   mpls te reserved-for-binding
   mpls te tunnel-id 100
   mpls te path explicit-path path2pe1
  #
  ospf 1
   opaque-capability enable
   segment-routing mpls
   segment-routing global-block 16000 47999
   area 0.0.0.0
    network 3.3.3.9 0.0.0.0
    network 10.20.1.0 0.0.0.255
    mpls-te enable
  #
  tunnel-policy policy1
   tunnel binding destination 1.1.1.9 te Tunnel10
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
   ip address 10.1.1.2 255.255.255.0
  #
  return
  ```