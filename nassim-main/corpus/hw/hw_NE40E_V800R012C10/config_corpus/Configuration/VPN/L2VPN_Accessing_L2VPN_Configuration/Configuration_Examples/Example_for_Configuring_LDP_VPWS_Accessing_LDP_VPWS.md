Example for Configuring LDP VPWS Accessing LDP VPWS
===================================================

This section provides an example for configuring LDP VPWS accessing LDP VPWS through VE interfaces.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001153009292__fig_dc_vrp_l2-l3_cfg_501501), LDP VPWS is deployed between the UPE and NPE and between the NPE and PE. VE0/2/0 and VE0/2/1 are created on the NPE. VE0/2/0 functions as an L2VE interface to terminate VPWS, and VE0/2/1 functions as an L3VE interface to access VPWS.

**Figure 1** LDP VPWS accessing LDP VPWS![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 through 4 represent GE0/1/0, GE0/2/0, VE0/2/0, and VE0/2/1, respectively.


  
![](figure/en-us_image_0000001199088931.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create an L2VE interface and an L3VE interface on the NPE, and bind them to the same VE group.
2. Configure LDP VPWS, which involves the following steps:
   
   * Configure a routing protocol on the related devices (UPE, NPE, and PE) for them to communicate, and enable MPLS.
   * Establish LSPs to transmit service data. The default tunnel policy is used in this example.
   * Enable MPLS L2VPN and create a VC on the PE.

#### Procedure

1. Create two VE interfaces on the NPE, and bind them to the same VE group.
   
   
   
   # Create VE0/2/0 to terminate MPLS L2VPN.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname NPE
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~NPE] interface virtual-ethernet0/2/0
   ```
   ```
   [*NPE-Virtual-Ethernet0/2/0] ve-group 1 l2-terminate
   ```
   ```
   [*NPE-Virtual-Ethernet0/2/0] quit
   ```
   ```
   [*NPE] commit
   ```
   
   # Create VE0/2/1 for access to MPLS L2VPN.
   
   ```
   [~NPE] interface virtual-ethernet0/2/1
   ```
   ```
   [*NPE-Virtual-Ethernet0/2/1] ve-group 1 l3-access
   ```
   ```
   [*NPE-Virtual-Ethernet0/2/1] quit
   ```
   ```
   [*NPE] commit
   ```
   
   After the configuration is complete, run the **display virtual-ethernet ve-group** command on the NPE. The command output shows the binding between the VE interfaces and VE group.
   
   ```
   [~NPE] display virtual-ethernet ve-group
   ```
   ```
    Ve-groupID    TerminateVE                   AccessVE  
   ```
   ```
    1             Virtual-Ethernet0/2/0         Virtual-Ethernet0/2/1
   ```
   ```
   Total 1, 1 printed
   ```
2. Configure an IGP on the access network. OSPF is used in the example. The configuration details are not described here.
   
   
   
   Configure interface addresses on the UPE, NPE, and PE according to [Figure 1](#EN-US_TASK_0000001153009292__fig_dc_vrp_l2-l3_cfg_501501). When configuring OSPF, you need to configure the UPE, NPE, and PE to advertise the 32-bit addresses of loopback interfaces.
   
   For configuration details, see Configuration Files.
3. Configure basic MPLS functions and LDP on the access network.
   
   
   
   # Configure the UPE.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname UPE
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~UPE] mpls lsr-id 1.1.1.1
   ```
   ```
   [*UPE] mpls
   ```
   ```
   [*UPE-mpls] quit
   ```
   ```
   [*UPE] mpls ldp
   ```
   ```
   [*UPE-mpls-ldp] quit
   ```
   ```
   [*UPE] interface gigabitethernet 0/2/0
   ```
   ```
   [*UPE-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*UPE-GigabitEthernet0/2/0] mpls ldp
   ```
   ```
   [*UPE-GigabitEthernet0/2/0] quit
   ```
   ```
   [*UPE] commit
   ```
   
   # Configure the PE.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~PE] mpls lsr-id 3.3.3.3
   ```
   ```
   [*PE] mpls
   ```
   ```
   [*PE-mpls] quit
   ```
   ```
   [*PE] mpls ldp
   ```
   ```
   [*PE-mpls-ldp] quit
   ```
   ```
   [*PE] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*PE-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*PE-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE] commit
   ```
   
   # Configure the NPE.
   
   ```
   [~NPE] mpls lsr-id 2.2.2.2
   ```
   ```
   [*NPE] mpls
   ```
   ```
   [*NPE-mpls] quit
   ```
   ```
   [*NPE] mpls ldp
   ```
   ```
   [*NPE-mpls-ldp] quit
   ```
   ```
   [*NPE] interface gigabitethernet 0/1/0
   ```
   ```
   [*NPE-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*NPE-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*NPE-GigabitEthernet0/1/0] quit
   ```
   ```
   [*NPE] interface gigabitethernet 0/2/0
   ```
   ```
   [*NPE-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*NPE-GigabitEthernet0/2/0] mpls ldp
   ```
   ```
   [*NPE-GigabitEthernet0/2/0] quit
   ```
   ```
   [*NPE] commit
   ```
4. Enable MPLS L2VPN on the UPE and NPE, and establish VCs.
   
   
   
   # Configure the UPE.
   
   ```
   [~UPE] mpls l2vpn
   ```
   ```
   [*UPE-l2vpn] quit
   ```
   ```
   [*UPE] interface gigabitethernet 0/1/0.1
   ```
   ```
   [*UPE-GigabitEthernet0/1/0.1] shutdown
   ```
   ```
   [*UPE-GigabitEthernet0/1/0.1] vlan-type dot1q 10
   ```
   ```
   [*UPE-GigabitEthernet0/1/0.1] mpls l2vc 2.2.2.2 101
   ```
   ```
   [*UPE-GigabitEthernet0/1/0.1] undo shutdown
   ```
   ```
   [*UPE-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*UPE] commit
   ```
   
   # Configure the NPE.
   
   ```
   [~NPE] mpls l2vpn
   ```
   ```
   [*NPE-l2vpn] quit
   ```
   ```
   [*NPE] interface virtual-ethernet0/2/0.1
   ```
   ```
   [*NPE-Virtual-Ethernet0/2/0.1] vlan-type dot1q 1
   ```
   ```
   [*NPE-Virtual-Ethernet0/2/0.1] mpls l2vc 1.1.1.1 101
   ```
   ```
   [*NPE-Virtual-Ethernet0/2/0.1] quit
   ```
   ```
   [*NPE] interface virtual-ethernet0/2/1.1
   ```
   ```
   [*NPE-Virtual-Ethernet0/2/1.1] vlan-type dot1q 1
   ```
   ```
   [*NPE-Virtual-Ethernet0/2/1.1] mpls l2vc 3.3.3.3 102
   ```
   ```
   [*NPE-Virtual-Ethernet0/2/1.1] quit
   ```
   ```
   [*NPE] commit
   ```
   
   
   
   # Configure the PE.
   
   ```
   [~PE] mpls l2vpn
   ```
   ```
   [*PE-l2vpn] quit
   ```
   ```
   [*PE] interface gigabitethernet 0/2/0.1
   ```
   ```
   [*PE-GigabitEthernet0/2/0.1] shutdown
   ```
   ```
   [*PE-GigabitEthernet0/2/0.1] vlan-type dot1q 20
   ```
   ```
   [*PE-GigabitEthernet0/2/0.1] mpls l2vc 2.2.2.2 102
   ```
   ```
   [*PE-GigabitEthernet0/2/0.1] undo shutdown
   ```
   ```
   [*PE-GigabitEthernet0/2/0.1] quit
   ```
   ```
   [*PE] commit
   ```
5. Verify the configuration.
   
   
   
   Check L2VPN connection information on the PE. You can find that an L2VC has been set up and is in the up state.
   
   The command output on the NPE is used as an example.
   
   ```
   [~NPE] display mpls l2vc
   ```
   ```
   Total ldp vc : 2     2 up       0 down
   ```
   ```
    *Client Interface          : Virtual-Ethernet0/2/0.1 is up
   ```
   ```
     Administrator PW          : no
   ```
   ```
     Session State             : up
   ```
   ```
     AC Status                 : up
   ```
   ```
     Ignore AC state           : disable
   ```
   ```
     VC State                  : up
   ```
   ```
     Label state               : 0
   ```
   ```
     Token state               : 0
   ```
   ```
     VC ID                     : 101
   ```
   ```
     VC Type                   : vlan
   ```
   ```
     Destination               : 1.1.1.1
   ```
   ```
     local VC label            : 140288       remote VC label      : 140292
   ```
   ```
     control word              : disable
   ```
   ```
     remote control word       : disable
   ```
   ```
     forwarding entry          : exist
   ```
   ```
     local group ID            : 0
   ```
   ```
     remote group ID           : 0
     local AC OAM State        : up
     local PSN OAM State       : up
     local forwarding state    : forwarding
     local status code         : 0x0
     remote AC OAM state       : up
     remote PSN OAM state      : up
     remote forwarding state   : forwarding
     remote status code        : 0x0
     ignore standby state      : no
     BFD for PW                : unavailable
     VCCV State                : up
   
   ```
   ```
     manual fault              : not set
   ```
   ```
     active state              : active
   ```
   ```
     OAM Protocol              : --
     OAM Status                : --
     OAM Fault Type            : --
     PW APS ID                 : --
     PW APS Status             : --
     TTL Value                 : 1
   ```
   ```
     link state                : up
   ```
   ```
     local VC MTU              : 1500         remote VC MTU        : 1500
   ```
   ```
     local VCCV                : alert ttl lsp-ping bfd
     remote VCCV               : alert ttl lsp-ping bfd
   
   ```
   ```
     tunnel policy name        : --
     PW template name          : --
     primary or secondary      : primary
     load balance type         : flow
     Access-port               : false
   
   ```
   ```
     Switchover Flag           : false
     VC tunnel info            : 1 tunnels
       NO.0  TNL type          : ldp   , TNL ID : 0x0000000001004c4e42
   
   ```
   ```
     create time               : 0 days, 0 hours, 30 minutes, 18 seconds
   ```
   ```
     up time                   : 0 days, 0 hours, 0 minutes, 0 seconds
   ```
   ```
     last change time          : 0 days, 0 hours, 30 minutes, 18 seconds
     VC last up time           : 2013/07/24 12:31:31
     VC total up time          : 0 days, 2 hours, 12 minutes, 51 seconds
   ```
   ```
     CKey                      : 11                                                   
     NKey                      : 10     
   ```
   ```
     PW redundancy mode        : frr
   ```
   ```
     AdminPw interface         : --
     AdminPw link state        : --
     Forward state             : send inactive, receive inactive 
     Diffserv Mode             : uniform
     Service Class             : --
     Color                     : --
     DomainId                  : --
     Domain Name               : --
   ```
   
   
   
   # CE1 and CE2 can ping each other.
   
   The following example uses CE1.
   
   ```
   [~CE1] ping 10.10.1.2
   ```
   ```
     PING 10.10.1.2: 56  data bytes, press CTRL_C to break
   ```
   ```
       Reply from 10.10.1.2: bytes=56 Sequence=1 ttl=255 time=31 ms
   ```
   ```
       Reply from 10.10.1.2: bytes=56 Sequence=2 ttl=255 time=10 ms
   ```
   ```
       Reply from 10.10.1.2: bytes=56 Sequence=3 ttl=255 time=5 ms
   ```
   ```
       Reply from 10.10.1.2: bytes=56 Sequence=4 ttl=255 time=2 ms
   ```
   ```
       Reply from 10.10.1.2: bytes=56 Sequence=5 ttl=255 time=28 ms
   ```
   ```
     --- 10.10.1.2 ping statistics ---
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
   round-trip min/avg/max = 2/15/31 ms
   ```

#### Configuration Files

* UPE configuration file
  
  ```
  #
  ```
  ```
   sysname UPE
  ```
  ```
  #
  ```
  ```
   mpls lsr-id 1.1.1.1
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
  #
  ```
  ```
  interface GigabitEthernet0/1/0.1
  ```
  ```
   vlan-type dot1q 10
  ```
  ```
   mpls l2vc 2.2.2.2 101
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
   ip address 10.2.1.1 255.255.255.0
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
    network 10.2.1.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  return
  ```
* PE configuration file
  
  ```
  #
  ```
  ```
   sysname PE
  ```
  ```
  #
  ```
  ```
   mpls lsr-id 3.3.3.3
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
   ip address 10.2.2.2 255.255.255.0
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
   vlan-type dot1q 20
  ```
  ```
   mpls l2vc 2.2.2.2 102
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
    network 10.2.2.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  return
  ```
* NPE configuration file
  
  ```
  #
  ```
  ```
   sysname NPE
  ```
  ```
  #
  ```
  ```
   mpls lsr-id 2.2.2.2
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
   ip address 10.2.2.1 255.255.255.0
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
   ip address 10.2.1.2 255.255.255.0
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
  interface Virtual-Ethernet0/2/0
  ```
  ```
   ve-group 1 l2-terminate
  ```
  ```
  #
  ```
  ```
  interface Virtual-Ethernet0/2/0.1
  ```
  ```
   vlan-type dot1q 1
  ```
  ```
   mpls l2vc 1.1.1.1 101
  ```
  ```
  #
  ```
  ```
  interface Virtual-Ethernet0/2/1
  ```
  ```
   ve-group 1 l3-access
  ```
  ```
  #
  ```
  ```
  interface Virtual-Ethernet0/2/1.1
  ```
  ```
   vlan-type dot1q 1
  ```
  ```
   mpls l2vc 3.3.3.3 102
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
    network 2.2.2.2 0.0.0.0
  ```
  ```
    network 10.2.1.0 0.0.0.255
  ```
  ```
    network 10.2.2.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  return
  ```
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
   vlan-type dot1q 10
  ```
  ```
   ip address 10.10.1.1 255.255.255.0
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
   vlan-type dot1q 20
  ```
  ```
   ip address 10.10.1.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  return
  ```