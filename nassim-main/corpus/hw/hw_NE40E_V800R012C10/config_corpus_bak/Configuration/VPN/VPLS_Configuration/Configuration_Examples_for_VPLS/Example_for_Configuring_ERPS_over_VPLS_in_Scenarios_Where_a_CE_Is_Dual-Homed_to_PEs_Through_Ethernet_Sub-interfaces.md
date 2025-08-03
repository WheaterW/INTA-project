Example for Configuring ERPS over VPLS in Scenarios Where a CE Is Dual-Homed to PEs Through Ethernet Sub-interfaces
===================================================================================================================

To configure ERPS over VPLS in scenarios where a CE is dual-homed to PEs through Ethernet sub-interfaces, enable ERPS on PE1, PE2, and the CE and configure ERPS to access the VPLS network in non-virtual channel (NVC) mode. Using Ethernet sub-interfaces to access the VPLS network must have the TC notification function enabled so that the VPLS network can have ARP and MAC address entries updated promptly after receiving TC packets. This function, however, does not need to be enabled when VLANIF interfaces are used for VPLS network access.

#### Networking Requirements

On the VPLS network shown in [Figure 1](#EN-US_TASK_0172370300__en-us_task_0172363490_fig_dc_vrp_erps_cfg_002201), a CE is dual-homed to PE1 and PE2. In this networking scenario, PE3 receives two copies of CE traffic from PE1 and PE2. To prevent this problem, enable ERPS on PE1, PE2, and the CE and configure the CE's GE 0/2/0 as an RPL owner port to block traffic sending from this port. In this way, the CE's traffic is directly sent to PE3 through PE2, thereby preventing any duplicate traffic or loop.

The ERPS ring shown in [Figure 1](#EN-US_TASK_0172370300__en-us_task_0172363490_fig_dc_vrp_erps_cfg_002201) is connected to a VPLS ring through Ethernet sub-interfaces.

**Figure 1** Configuring ERPS over VPLS in scenarios where a CE is dual-homed to PEs through Ethernet sub-interfaces![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/1/0, GE 0/2/0, and GE 0/3/0, respectively.


  
![](images/fig_dc_vrp_erps_cfg_002201.png)
![](../../../../public_sys-resources/note_3.0-en-us.png) 

* The configurations of ERPS over VPLS in CE single-homing scenarios are similar to those in CE dual-homing scenarios. This section uses CE dual-homing scenarios as an example.
* If an ERPS ring has revertive switching enabled and an AC interface recovers, it is not recommended that you use the [**clear**](cmdqueryname=clear) command to trigger revertive switching before the wait to restore (WTR) or wait to block (WTB) timer expires. If you do so and the VSI bound to the AC interface recovers later than the AC interface, traffic will be interrupted for a long time.

| Device | Interface | IP Address |
| --- | --- | --- |
| PE1 | GE 0/1/0 | -- |
| GE 0/2/0 | 10.1.1.1/24 |
| GE 0/3/0 | 10.3.1.1/24 |
| Loopback 1 | 1.1.1.1/32 |
| PE2 | GE 0/1/0 | -- |
| GE 0/2/0 | 10.2.1.1/24 |
| GE 0/3/0 | 10.3.1.2/24 |
| Loopback 1 | 2.2.2.2/32 |
| PE3 | GE 0/1/0 | 10.1.1.2/24 |
| GE 0/2/0 | 10.2.1.2/24 |
| Loopback 1 | 3.3.3.3/32 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IGP on the VPLS backbone network to allow the PEs to communicate.
2. Configure basic MPLS functions and establish LDP LSPs on the VPLS backbone network.
3. Establish a VPLS connection between every two PEs and bind each Ethernet sub-interface to a VSI.
4. Configure ERPS.
   
   * Enable ERPS on PE1, PE2, and the CE.
   * Configure an RPL owner port.

#### Data Preparation

To complete the configuration, you need the following data:

* Data needed for configuring OSPF: IP address of each interface, OSPF process ID, and OSPF domain ID
* MPLS LSR IDs (used as peer addresses)
* VSI names and VSI IDs
* Names of the Ethernet sub-interfaces bound to VSIs
* ERPS ring ID, control VLAN ID, and RPL owner port number

#### Procedure

1. Configure interface IP addresses and an IGP on the VPLS backbone network to allow PEs to communicate. This example uses OSPF as the IGP.
   
   
   
   When configuring OSPF, configure PE1, PE2, and PE3 to advertise their 32-bit IP addresses (used as LSR IDs) of loopback interfaces.
   
   For configuration details, see [Configuration Files](#EN-US_TASK_0172370300__en-us_task_0172363490_example_01) in this section.
2. Configure basic MPLS functions and establish dynamic LDP LSPs between every two PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] mpls lsr-id 1.1.1.1
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
   [*PE1] interface gigabitethernet 0/3/0
   ```
   ```
   [*PE1-GigabitEthernet0/3/0] mpls
   ```
   ```
   [*PE1-GigabitEthernet0/3/0] mpls ldp
   ```
   ```
   [*PE1-GigabitEthernet0/3/0] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] mpls lsr-id 2.2.2.2
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
   [*PE2] interface gigabitethernet 0/3/0
   ```
   ```
   [*PE2-GigabitEthernet0/3/0] mpls
   ```
   ```
   [*PE2-GigabitEthernet0/3/0] mpls ldp
   ```
   ```
   [*PE2-GigabitEthernet0/3/0] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] mpls lsr-id 3.3.3.3
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
   [*PE3] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE3-gigabitethernet0/1/0] mpls
   ```
   ```
   [*PE3-gigabitethernet0/1/0] mpls ldp
   ```
   ```
   [*PE3-gigabitethernet0/1/0] quit
   ```
   ```
   [*PE3] interface gigabitethernet 0/2/0
   ```
   ```
   [*PE3-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*PE3-GigabitEthernet0/2/0] mpls ldp
   ```
   ```
   [*PE3-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE3] commit
   ```
3. Enable MPLS L2VPN on each PE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] mpls l2vpn
   ```
   ```
   [*PE1-l2vpn] commit
   ```
   ```
   [~PE1-l2vpn] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] mpls l2vpn
   ```
   ```
   [*PE2-l2vpn] commit
   ```
   ```
   [~PE2-l2vpn] quit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] mpls l2vpn
   ```
   ```
   [*PE3-l2vpn] commit
   ```
   ```
   [~PE3-l2vpn] quit
   ```
4. Configure VPLS.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] vsi s1 static
   ```
   ```
   [*PE1-vsi-s1] pwsignal ldp
   ```
   ```
   [*PE1-vsi-s1-ldp] vsi-id 10
   ```
   ```
   [*PE1-vsi-s1-ldp] peer 2.2.2.2
   ```
   ```
   [*PE1-vsi-s1-ldp] peer 3.3.3.3
   ```
   ```
   [*PE1-vsi-s1-ldp] quit
   ```
   ```
   [*PE1-vsi-s1] quit
   ```
   ```
   [*PE1] commit
   ```
   ```
   [~PE1] vlan 10
   ```
   ```
   [*PE1-vlan10] quit
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
   [*PE1-GigabitEthernet0/1/0.1] l2 binding vsi s1
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
   [~PE2] vsi s1 static
   ```
   ```
   [*PE2-vsi-s1] pwsignal ldp
   ```
   ```
   [*PE2-vsi-s1-ldp] vsi-id 10
   ```
   ```
   [*PE2-vsi-s1-ldp] peer 1.1.1.1
   ```
   ```
   [*PE2-vsi-s1-ldp] peer 3.3.3.3
   ```
   ```
   [*PE2-vsi-s1-ldp] quit
   ```
   ```
   [*PE2-vsi-s1] quit
   ```
   ```
   [*PE2] commit
   ```
   ```
   [~PE2] vlan 10
   ```
   ```
   [*PE2-vlan10] quit
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
   [*PE2-GigabitEthernet0/1/0.1] l2 binding vsi s1
   ```
   ```
   [*PE2-GigabitEthernet0/1/0.1] undo shutdown
   ```
   ```
   [*PE2-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] vsi s1 static
   ```
   ```
   [*PE3-vsi-s1] pwsignal ldp
   ```
   ```
   [*PE3-vsi-s1-ldp] vsi-id 10
   ```
   ```
   [*PE3-vsi-s1-ldp] peer 1.1.1.1
   ```
   ```
   [*PE3-vsi-s1-ldp] peer 2.2.2.2
   ```
   ```
   [*PE3-vsi-s1-ldp] quit
   ```
   ```
   [*PE3-vsi-s1] quit
   ```
   ```
   [*PE3] commit
   ```
5. Configure ERPS on PE1, PE2, and the CE.
   
   
   
   # Configure PE1. The specified service VLAN ID and instance ID must be mapped to trigger ERPS and VPLS association.
   
   ```
   [~PE1] stp region-configuration
   [*PE1-mst-region] instance 0 vlan 10 100
   [*PE1-mst-region] commit
   [~PE1-mst-region] quit
   [~PE1] erps ring 1
   ```
   ```
   [*PE1-erps-ring1] control-vlan 100
   ```
   ```
   [*PE1-erps-ring1] protected-instance 0
   ```
   ```
   [*PE1-erps-ring1] version v2
   ```
   ```
   [*PE1-erps-ring1] sub-ring
   ```
   ```
   [*PE1-erps-ring1] quit
   ```
   ```
   [*PE1] commit
   ```
   ```
   [~PE1] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE1-gigabitethernet0/1/0] undo shutdown
   ```
   ```
   [*PE1-gigabitethernet0/1/0] portswitch
   ```
   ```
   [*PE1-gigabitethernet0/1/0] port link-type trunk
   ```
   ```
   [*PE1-gigabitethernet0/1/0] port trunk allow-pass vlan 100
   ```
   ```
   [*PE1-gigabitethernet0/1/0] stp disable
   ```
   ```
   [*PE1-gigabitethernet0/1/0] erps ring 1
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] erps vpls-subinterface enable
   ```
   ```
   [*PE1-gigabitethernet0/1/0] commit
   ```
   ```
   [~PE1-gigabitethernet0/1/0] quit
   ```
   
   # Configure PE2. The specified service VLAN ID and instance ID must be mapped to trigger ERPS and VPLS association.
   
   ```
   [~PE2] stp region-configuration
   [*PE2-mst-region] instance 0 vlan 10 100
   [*PE2-mst-region] commit
   [~PE2-mst-region] quit
   [~PE2] erps ring 1
   ```
   ```
   [*PE2-erps-ring1] control-vlan 100
   ```
   ```
   [*PE2-erps-ring1] protected-instance 0
   ```
   ```
   [*PE2-erps-ring1] version v2
   ```
   ```
   [*PE2-erps-ring1] sub-ring
   ```
   ```
   [*PE2-erps-ring1] quit
   ```
   ```
   [*PE2] commit
   ```
   ```
   [~PE2] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE2-gigabitethernet0/1/0] undo shutdown
   ```
   ```
   [*PE2-gigabitethernet0/1/0] portswitch
   ```
   ```
   [*PE2-gigabitethernet0/1/0] port link-type trunk
   ```
   ```
   [*PE2-gigabitethernet0/1/0] port trunk allow-pass vlan 100
   ```
   ```
   [*PE2-gigabitethernet0/1/0] stp disable
   ```
   ```
   [*PE2-gigabitethernet0/1/0] erps ring 1
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] erps vpls-subinterface enable
   ```
   ```
   [*PE2-gigabitethernet0/1/0] commit
   ```
   ```
   [~PE2-gigabitethernet0/1/0] quit
   ```
   
   # Configure the CE.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname CE
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~CE] stp region-configuration
   [*CE-mst-region] instance 0 vlan 10 100
   [*CE-mst-region] commit
   [~CE-mst-region] quit
   [~CE] erps ring 1
   ```
   ```
   [*CE-erps-ring1] control-vlan 100
   ```
   ```
   [*CE-erps-ring1] protected-instance 0
   ```
   ```
   [*CE-erps-ring1] version v2
   ```
   ```
   [*CE-erps-ring1] sub-ring
   ```
   ```
   [*CE-erps-ring1] quit
   ```
   ```
   [*CE] commit
   ```
   ```
   [~CE] interface gigabitethernet 0/1/0
   ```
   ```
   [*CE-gigabitethernet0/1/0] undo shutdown
   ```
   ```
   [*CE-gigabitethernet0/1/0] portswitch
   ```
   ```
   [*CE-gigabitethernet0/1/0] port link-type trunk
   ```
   ```
   [*CE-gigabitethernet0/1/0] port trunk allow-pass vlan 10
   ```
   ```
   [*CE-gigabitethernet0/1/0] stp disable
   ```
   ```
   [*CE-gigabitethernet0/1/0] erps ring 1
   ```
   ```
   [*CE-gigabitethernet0/1/0] commit
   ```
   ```
   [~CE-gigabitethernet0/1/0] quit
   ```
   ```
   [~CE] interface gigabitethernet 0/2/0
   ```
   ```
   [*CE-gigabitethernet0/2/0] portswitch
   ```
   ```
   [*CE-gigabitethernet0/2/0] port link-type trunk
   ```
   ```
   [*CE-gigabitethernet0/2/0] port trunk allow-pass vlan 10
   ```
   ```
   [*CE-gigabitethernet0/2/0] stp disable
   ```
   ```
   [*CE-gigabitethernet0/2/0] erps ring 1 rpl owner
   ```
   ```
   [*CE-gigabitethernet0/2/0] commit
   ```
   ```
   [~CE-gigabitethernet0/2/0] quit
   ```
6. Verify the configuration.
   
   
   
   After the configurations are complete, run the **display vsi name s1 verbose** command on PE3. The command output shows that PE3 has established two PWs: one with PE1 (1.1.1.1), one with PE2 (2.2.2.2.).
   
   ```
   [~PE3] display vsi name s1 verbose
   ```
   ```
    ***VSI Name               : s1
       Work Mode              : normal
       Administrator VSI      : no
       Isolate Spoken         : disable
       VSI Index              : 2
       PW Signaling           : ldp
       Member Discovery Style : static
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
       Create Time            : 0 days, 1 hours, 19 minutes, 38 seconds
       VSI State              : up
       Resource Status        : Valid
   
       VSI ID                 : 10
      *Peer Router ID         : 1.1.1.1
       primary or secondary   : primary
       ignore-standby-state   : no
       VC Label               : 32891
       Peer Type              : dynamic
       Session                : up
       Tunnel ID              : 0x0000000001004c4b41 
       Broadcast Tunnel ID    : --
       Broad BackupTunnel ID  : -- 
       CKey                   : 2
       NKey                   : 1862271177
       Stp Enable             : 0
       PwIndex                : 1
       Control Word           : disable
      *Peer Router ID         : 2.2.2.2
       primary or secondary   : primary
       ignore-standby-state   : no
       VC Label               : 32892
       Peer Type              : dynamic
       Session                : up
       Tunnel ID              : 0x0000000001004c4b42 
       Broadcast Tunnel ID    : --
       Broad BackupTunnel ID  : -- 
       CKey                   : 2
       NKey                   : 1862271178
       Stp Enable             : 0
       PwIndex                : 2
       Control Word           : disable
    
     **PW Information:
   
      *Peer Ip Address        : 1.1.1.1
       PW State               : up
       Local VC Label         : 32891
       Remote VC Label        : 32890
       Remote Control Word    : disable
       PW Type                : label
       Tunnel ID              : 0x0000000001004c4b41 
       Broadcast Tunnel ID    : --
       Broad BackupTunnel ID  : --
       Ckey                   : 2
       Nkey                   : 1862271177
       Main PW Token          : 0x0
       Slave PW Token         : 0x0
       Tnl Type               : ldp
       OutInterface           : LDP LSP
       Backup OutInterface    : --
       Stp Enable             : 0
       Mac Flapping           : 0
       PW Last Up Time        : 2013/12/26 17:35:12
       PW Total Up Time       : 0 days, 1 hours, 19 minutes, 38 seconds  
      *Peer Ip Address        : 2.2.2.2
       PW State               : up
       Local VC Label         : 32892
       Remote VC Label        : 32893
       Remote Control Word    : disable
       PW Type                : label
       Tunnel ID              : 0x0000000001004c4b42 
       Broadcast Tunnel ID    : --
       Broad BackupTunnel ID  : --
       Ckey                   : 2
       Nkey                   : 1862271178
       Main PW Token          : 0x0
       Slave PW Token         : 0x0
       Tnl Type               : ldp
       OutInterface           : LDP LSP
       Backup OutInterface    : --
       Stp Enable             : 0
       Mac Flapping           : 0
       PW Last Up Time        : 2013/12/28 10:35:45
       PW Total Up Time       : 0 days, 1 hours, 19 minutes, 45 seconds
   ```
   
   Run the **display erps** command on the CE. The command output shows that the link between the CE and PE1 is blocked.
   
   ```
   [~CE] display erps
   ```
   ```
   D  : Discarding
   F  : Forwarding
   R  : RPL Owner
   N  : RPL Neighbour
   FS : Forced Switch
   MS : Manual Switch
   Total number of rings configured = 1
   Ring  Control  WTR Timer  Guard Timer  Port 1              Port 2
   ID    VLAN     (min)      (csec)
   --------------------------------------------------------------------------------
      1       100         5          200  (F)GE0/1/0          (D,R)GE0/2/0
   --------------------------------------------------------------------------------
   
   ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  vlan batch 10 100
  #
  stp region-configuration
   instance 0 vlan 10 100
  #
  erps ring 1
   control-vlan 100
   protected-instance 0
   version v2
   sub-ring
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
  #
  mpls l2vpn
  #
  vsi s1 static
   pwsignal ldp
    vsi-id 10
    peer 2.2.2.2
    peer 3.3.3.3
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 100 
   stp disable
   erps ring 1
   erps vpls-subinterface enable
  #
  interface GigabitEthernet0/1/0.1
   vlan-type dot1q 10
   l2 binding vsi s1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 10.3.1.1 255.255.255.0
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
    network 10.3.1.0 0.0.0.255
  #
  return
  
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  vlan batch 10 100
  #
  stp region-configuration
   instance 0 vlan 10 100
  #
  erps ring 1
   control-vlan 100
   protected-instance 0
   version v2
   sub-ring
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
  #
  mpls l2vpn
  #
  vsi s1 static
   pwsignal ldp
    vsi-id 10
    peer 1.1.1.1
    peer 3.3.3.3
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 100
   stp disable
   erps ring 1
   erps vpls-subinterface enable
  #
  interface GigabitEthernet0/1/0.1
   vlan-type dot1q 10
   l2 binding vsi s1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.2.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 10.3.1.2 255.255.255.0
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
    network 10.3.1.0 0.0.0.255
  #
  return
  
  ```
* PE3 configuration file
  
  ```
  #
  sysname PE3
  #
  mpls lsr-id 3.3.3.3
  #
  mpls
  #
  mpls l2vpn
  #
  vsi s1 static
   pwsignal ldp
    vsi-id 10
    peer 1.1.1.1
    peer 2.2.2.2
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
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
  #
  return
  
  ```
* CE configuration file
  
  ```
  #
  sysname CE
  #
  vlan batch 10 100
  #
  stp region-configuration
   instance 0 vlan 10 100
  #
  erps ring 1
   control-vlan 100
   protected-instance 0
   version v2
   sub-ring
  #
  interface GigabitEthernet0/1/0
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 10 100
   stp disable
   erps ring 1
  #
  interface GigabitEthernet0/2/0
   portswitch
   port link-type trunk
   port trunk allow-pass vlan 10 100
   stp disable
   erps ring 1 rpl owner
  #
  return
  
  ```