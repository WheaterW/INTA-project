Example for Configuring IPv6 PIM-SM Intra-domain Multicast
==========================================================

This section provides an example for configuring basic PIM-SM functions for an IPv6 PIM-SM domain.

#### Networking Requirements

On the ISP network shown in [Figure 1](#EN-US_TASK_0172367522__fig_dc_vrp_multicast_cfg_203701), multicast services are deployed. An Interior Gateway Protocol (IGP) has been deployed on the network, IPv6 unicast is running properly, and the network has been connected to the Internet. It is required that hosts receive VoD information in multicast mode.

**Figure 1** Configuring IPv6 PIM-SM intra-domain multicast![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1, 2, 3, and 4 in this example represent GE 0/1/0, GE 0/2/0, GE 0/3/0, and GE 0/1/1, respectively.


  
![](images/fig_dc_vrp_multicast_cfg_203701.png)

#### Precautions

When configuring IPv6 PIM-SM intra-domain multicast, note the following precautions:

* IPv6 PIM-SM must be enabled before Multicast Listener Discovery (MLD) is enabled.
* To use a static Rendezvous Point (RP), configure the same RP address on all Routers.
* Use the Protocol Independent Multicast - Source-specific Multicast (PIM-SSM) service when the users need to receive data from a specified multicast source. Ensure that all Routers share the same SSM group address range.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IPv6 address for each Router interface and an IPv6 unicast routing protocol.
2. Enable IPv6 multicast routing on all Routers.
3. Enable IPv6 PIM-SM on all Router interfaces.
4. Enable MLD on interfaces that directly connect Routers to hosts.
5. Configure an RP. An RP is a rendezvous point tree (RPT)'s root node on a PIM-SM network. Setting an RP on the Router that has more multicast flows is recommended.
6. (Optional) Set a BootStrap router (BSR) boundary on interfaces connected to the Internet. Bootstrap messages cannot pass through the BSR boundary. Therefore, the BSR serves only this PIM-SM domain. This improves multicast controllability.
7. (Optional) Configure the same SSM group address range on each Router. This enables the multicast Routers in the PIM-SM domain to provide services only for multicast groups with addresses being in the SSM group address range.

#### Data Preparation

To complete the configuration, you need the following data:

* Multicast group address
* Multicast source address
* SSM group address range

#### Procedure

1. Configure an IPv6 address for each Router interface and an IPv6 unicast routing protocol. For configuration details, see Configuration Files in this section.
2. Enable IPv6 multicast routing on each Router and enable IPv6 PIM-SM on each interface on the Routers.
   
   
   
   # Configure DeviceA. The configurations of DeviceB, DeviceC, and DeviceD are similar to the configuration of DeviceA. For configuration details, see Configuration Files in this section.
   
   ```
   [~DeviceA] multicast ipv6 routing-enable
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] pim ipv6 sm
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceA] interface GigabitEthernet 0/2/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] pim ipv6 sm
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceA] interface GigabitEthernet 0/3/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/3/0] pim ipv6 sm
   ```
   ```
   [*DeviceA-GigabitEthernet0/3/0] quit
   ```
   ```
   [*DeviceA] interface GigabitEthernet 0/1/1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] pim ipv6 sm
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] quit
   ```
   
   # Run the **display pim ipv6 interface** command to check IPv6 PIM interfaces on each Router. The following example uses the command output on DeviceB.
   
   ```
   <DeviceB> display pim ipv6 interface
    VPN-Instance: public net
    Interface           State NbrCnt HelloInt   DR-Pri     DR-Address
    GE0/1/0             up    1      30         1          FE80::A01:10E:1 (local)
    GE0/2/0             up    0      30         1          FE80::200:AFF:FE01:10E (local)
    GE0/3/0             up    1      30         1          FE80::9D62:0:FDC5:2
   ```
3. Enable MLD on the interfaces connected to hosts. 
   
   
   
   # The configuration of DeviceC is similar to the configuration of DeviceB. For configuration details, see Configuration Files in this section.
   
   ```
   [~DeviceB] interface gigabitethernet 0/2/0
   ```
   ```
   [~DeviceB-GigabitEthernet0/2/0] mld enable
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/2/0] quit
   ```
4. Configure RPs.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   You can configure both a static RP and a BSR RP, or only one of them. When both a static RP and a BSR RP are configured, the BSR RP is used by default. To use the static RP, specify **preferred** in the **static-rp** *rp-address* command.
   
   The following shows how to configure a BSR RP
   
   # Configure a BSR RP. Perform the following configurations on one or several Routers in the PIM-SM domain. For example, on DeviceD, set the range of groups severed by the RP and addresses of C-BSRs and C-RPs.
   
   ```
   [~DeviceD] acl ipv6 number 2001
   ```
   ```
   [*DeviceD-acl6-basic-2001] rule permit source ff3e::1 64
   ```
   ```
   [*DeviceD-acl6-basic-2001] quit
   ```
   ```
   [*DeviceD] pim-ipv6
   ```
   ```
   [*DeviceD-pim6] c-rp 2001:db8:3::2 group-policy 2001
   ```
   
   # Configure a C-BSR on DeviceD.
   
   ```
   [*DeviceD-pim6] c-bsr 2001:db8:3::2
   ```
   ```
   [*DeviceD-pim6] commit
   ```
   ```
   [~DeviceD-pim6] quit
   ```
   
   # Run the **display pim ipv6 bsr-info** command to check BSR information on each Router. The following examples use the command outputs on DeviceB and DeviceD (C-BSR information is also displayed on DeviceD).
   
   ```
   <DeviceB> display pim ipv6 bsr-info
   ```
   ```
   VPN-Instance: public net
   ```
   ```
    Elected AdminScope BSR Count: 0
   ```
   ```
    Elected BSR Address: 2001:DB8:3::2
   ```
   ```
        Priority: 0
   ```
   ```
        Hash mask length: 126
   ```
   ```
        State: Accept Preferred
   ```
   ```
        Uptime: 00:04:22
   ```
   ```
        Expires: 00:01:46
   ```
   ```
        C-RP Count: 1
   ```
   ```
   <DeviceD> display pim ipv6 bsr-info
   ```
   ```
   VPN-Instance: public net
   ```
   ```
    Elected AdminScope BSR Count: 0
   ```
   ```
    Elected BSR Address: 2001:DB8:3::2
   ```
   ```
        Priority: 0
   ```
   ```
        Hash mask length: 126
   ```
   ```
        State: Elected
   ```
   ```
        Uptime: 00:01:10
   ```
   ```
        Next BSR message scheduled at: 00:00:48
   ```
   ```
        C-RP Count: 1
   ```
   ```
    Candidate AdminScope BSR Count: 0
   ```
   ```
    Candidate BSR Address: 2001:DB8:3::2
   ```
   ```
        Priority: 0
   ```
   ```
        Hash mask length: 126
   ```
   ```
        State: Elected
   ```
   ```
        Wait to be BSR: 0
   ```
   
   # Run the **display pim ipv6 rp-info** command to check RP information on each Router. The following example uses the command output on Device B.
   
   ```
   <DeviceB> display pim ipv6 rp-info
   ```
   ```
   VPN-Instance: public net
   ```
   ```
    PIM-SM BSR RP information:
   ```
   ```
    Group/MaskLen: FF3E::1/64
   ```
   ```
        RP: 2001:DB8:3::2
   ```
   ```
        Priority: 192
   ```
   ```
        Uptime: 00:05:19
   ```
   ```
        Expires: 00:02:11
   ```
5. (Optional) Configure a BSR boundary on the interface that connects Device A to the Internet.
   
   
   ```
   [~DeviceA] interface GigabitEthernet 0/1/1
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] pim ipv6 bsr-boundary
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] quit
   ```
6. (Optional) Configure the SSM group address range.
   
   
   
   # Configure the SSM group address range to FF3E::1/64 on Device A.
   
   The configurations of Device B, Device C, and Device D are similar to the configuration of Device A. For configuration details, see Configuration Files in this section.
   
   ```
   [~DeviceA] acl ipv6 2000
   ```
   ```
   [*DeviceA-acl6-basic-2000] rule permit source FF3E::1 64
   ```
   ```
   [*DeviceA-acl6-basic-2000] quit
   ```
   ```
   [*DeviceA] pim-ipv6
   ```
   ```
   [*DeviceA-pim6] ssm-policy 2000
   ```
   ```
   [*DeviceA-pim6] commit
   ```
   ```
   [~DeviceA-pim6] quit
   ```
7. Verify the configuration.
   
   
   
   # Have the multicast source S (2001:db8:5::5) send multicast packets to multicast group FF3E::1 (within the SSM group address range) and multicast group FF0E::1 (beyond the SSM group address range). Have Host A and Host C receive information of multicast group FF0E::1. Have Host B receive multicast information sent by S (2001:db8:5::5) to multicast group FF3E::1. Then, run the **display pim ipv6 routing-table** command to check the IPv6 PIM routing table on each Router.
   
   ```
   <DeviceA> display pim ipv6 routing-table
   ```
   ```
   VPN-Instance: public net
   ```
   ```
    Total 0 (*, G) entry; 2 (S, G) entries
   ```
   ```
    (2001:DB8:5::5, FF0E::1)
   ```
   ```
        RP: 2001:DB8:3::2
   ```
   ```
        Protocol: pim-sm, Flag: SPT LOC ACT
   ```
   ```
        UpTime: 00:02:15
   ```
   ```
        Upstream interface: GigabitEthernet0/1/0, Refresh time: 00:02:15
   ```
   ```
            Upstream neighbor: NULL
   ```
   ```
            RPF prime neighbor: NULL
   ```
   ```
        Downstream interface(s) information:
   ```
   ```
        Total number of downstreams: 3
   ```
   ```
            1: Register
   ```
   ```
                Protocol: pim-sm, UpTime: 00:02:15, Expires:  -
   ```
   ```
            2: GigabitEthernet0/2/0
   ```
   ```
                Protocol: pim-sm, UpTime: 00:02:15, Expires: 00:03:15
   ```
   ```
            3: GigabitEthernet0/3/0
   ```
   ```
                Protocol: pim-sm, UpTime: 00:02:15, Expires: 00:03:15
   ```
   ```
   (2001:DB8:5::5, FF3E::1)
   ```
   ```
        Protocol: pim-ssm, Flag: LOC SG_RCVR
   ```
   ```
        UpTime: 00:00:11
   ```
   ```
        Upstream interface: GigabitEthernet0/1/0, Refresh time: 00:00:11
   ```
   ```
            Upstream neighbor: NULL
   ```
   ```
            RPF prime neighbor: NULL
   ```
   ```
        Downstream interface(s) information:
   ```
   ```
        Total number of downstreams: 1
   ```
   ```
            1: GigabitEthernet0/2/0
   ```
   ```
                Protocol: pim-ssm, UpTime: 00:00:11, Expires: 00:03:19
   ```
   ```
   <DeviceB> display pim ipv6 routing-table
   ```
   ```
   VPN-Instance: public net
   ```
   ```
    Total 1 (*, G) entry; 2 (S, G) entries
   ```
   ```
    (*, FF0E::1)
   ```
   ```
        RP: 2001:DB8:3::2
   ```
   ```
        Protocol: pim-sm, Flag: WC
   ```
   ```
        UpTime: 00:14:44
   ```
   ```
        Upstream interface: GigabitEthernet0/3/0, Refresh time: 00:14:44
   ```
   ```
            Upstream neighbor: FE80::9D62:0:FDC5:2
   ```
   ```
            RPF prime neighbor: FE80::9D62:0:FDC5:2
   ```
   ```
        Downstream interface(s) information:
   ```
   ```
        Total number of downstreams: 1
   ```
   ```
            1: GigabitEthernet0/2/0
   ```
   ```
                Protocol: mld, UpTime: 00:14:44, Expires: -
   ```
   ```
   (2001:DB8:5::5, FF0E::1)
   ```
   ```
        RP: 2001:DB8:3::2
   ```
   ```
        Protocol: pim-sm, Flag: SPT ACT
   ```
   ```
        UpTime: 00:02:42
   ```
   ```
        Upstream interface: GigabitEthernet0/1/0, Refresh time: 00:02:42
   ```
   ```
            Upstream neighbor: FE80::A01:10C:1
   ```
   ```
            RPF prime neighbor: FE80::A01:10C:1
   ```
   ```
        Downstream interface(s) information:
   ```
   ```
        Total number of downstreams: 1
   ```
   ```
            1: GigabitEthernet0/2/0
   ```
   ```
                Protocol: pim-sm, UpTime: 00:14:44, Expires: -
   ```
   ```
   (2001:DB8:5::5, FF3E::1)
   ```
   ```
        Protocol: pim-ssm, Flag: SG_RCVR
   ```
   ```
        UpTime: 00:08:02
   ```
   ```
        Upstream interface: GigabitEthernet0/1/0, Refresh time: 00:08:02
   ```
   ```
            Upstream neighbor: FE80::A01:10C:1
   ```
   ```
            RPF prime neighbor: FE80::A01:10C:1
   ```
   ```
        Downstream interface(s) information:
   ```
   ```
        Total number of downstreams: 1
   ```
   ```
            1: GigabitEthernet0/2/0
   ```
   ```
                Protocol: pim-ssm, UpTime: 00:08:02, Expires: -
   ```
   ```
   <DeviceC> display pim ipv6 routing-table
   ```
   ```
   VPN-Instance: public net
   ```
   ```
    Total 1 (*, G) entry; 1 (S, G) entry
   ```
   ```
    (*, FF0E::1)
   ```
   ```
        RP: 2001:DB8:3::2
   ```
   ```
        Protocol: pim-sm, Flag: WC
   ```
   ```
        UpTime: 00:14:44
   ```
   ```
        Upstream interface: GigabitEthernet0/1/0, Refresh time: 00:14:44
   ```
   ```
            Upstream neighbor: FE80::7493:FE25:1
   ```
   ```
            RPF prime neighbor: FE80::7493:FE25:1
   ```
   ```
        Downstream interface(s) information:
   ```
   ```
        Total number of downstreams: 1
   ```
   ```
            1: GigabitEthernet0/2/0
   ```
   ```
                Protocol: mld, UpTime: 00:14:43, Expires: -
   ```
   ```
   (2001:DB8:5::5, FF0E::1)
   ```
   ```
        RP: 2001:DB8:3::2
   ```
   ```
        Protocol: pim-sm, Flag: SPT ACT
   ```
   ```
        UpTime: 00:02:42
   ```
   ```
         Upstream interface: GigabitEthernet0/1/0, Refresh time: 00:02:42
   ```
   ```
            Upstream neighbor: FE80::7493:FE25:1
   ```
   ```
            RPF prime neighbor: FE80::7493:FE25:1
   ```
   ```
        Downstream interface(s) information:
   ```
   ```
        Total number of downstreams: 1
   ```
   ```
            1: GigabitEthernet0/2/0
   ```
   ```
                Protocol: pim-sm, UpTime: 00:02:14, Expires: -
   ```
   ```
   <DeviceD> display pim ipv6 routing-table
   ```
   ```
   VPN-Instance: public net
   ```
   ```
    Total 1 (*, G) entry; 1 (S, G) entry
   ```
   ```
    (*, FF0E::1)
   ```
   ```
        RP: 2001:DB8:3::2 (local)
   ```
   ```
        Protocol: pim-sm, Flag: WC
   ```
   ```
        UpTime: 00:16:56
   ```
   ```
        Upstream interface: Register, Refresh time: 00:16:56
   ```
   ```
            Upstream neighbor: NULL
   ```
   ```
            RPF prime neighbor: NULL
   ```
   ```
        Downstream interface(s) information:
   ```
   ```
        Total number of downstreams: 2
   ```
   ```
            1: GigabitEthernet0/2/0
   ```
   ```
                Protocol: pim-sm, UpTime: 00:16:56, Expires: 00:02:34
   ```
   ```
            2: GigabitEthernet0/3/0
   ```
   ```
                Protocol: pim-sm, UpTime: 00:07:56, Expires: 00:02:35
   ```
   ```
    (2001:DB8:5::5, FF0E::1)
   ```
   ```
        RP: 2001:DB8:3::2 (local)
   ```
   ```
        Protocol: pim-sm, Flag: SWT ACT
   ```
   ```
        UpTime: 00:02:54
   ```
   ```
        Upstream interface: GigabitEthernet0/1/0, Refresh time: 00:02:54
   ```
   ```
            Upstream neighbor: FE81::659:10C:3
   ```
   ```
            RPF prime neighbor: FE81::659:10C:3
   ```
   ```
        Downstream interface(s) information:
   ```
   ```
        Total number of downstreams: 1
   ```
   ```
               1: GigabitEthernet0/3/0
   ```
   ```
                Protocol: pim-sm, UpTime: 00:02:54, Expires: 00:02:36
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
  multicast ipv6 routing-enable
  ```
  ```
  #
  ```
  ```
  acl ipv6 number 2000
  ```
  ```
   rule 0 permit source FF3E::1/64
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
   ipv6 enable
  ```
  ```
   ipv6 address 2001:DB8:5::1/64
  ```
  ```
   pim ipv6 sm
  ```
  ```
   ospfv3 1 area 0.0.0.0
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
   ipv6 enable
  ```
  ```
   ipv6 address 2001:DB8:1::1/64
  ```
  ```
   pim ipv6 sm
  ```
  ```
   ospfv3 1 area 0.0.0.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/3/0
  ```
  ```
   undo shutdown
  ```
  ```
   ipv6 enable
  ```
  ```
   ipv6 address 2001:DB8:2::1/64
  ```
  ```
   pim ipv6 sm
  ```
  ```
   ospfv3 1 area 0.0.0.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   ipv6 enable
  ```
  ```
   ipv6 address 2001:DB8:6::1/64
  ```
  ```
   pim ipv6 bsr-boundary
  ```
  ```
   pim ipv6 sm
  ```
  ```
   ospfv3 1 area 0.0.0.0
  ```
  ```
  #
  ```
  ```
  ospfv3 1
  ```
  ```
   router-id 1.1.1.1
  ```
  ```
   area 0.0.0.0
  ```
  ```
  #
  ```
  ```
  pim-ipv6
  ```
  ```
   ssm-policy 2000
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
  sysname DeviceB
  ```
  ```
  #
  ```
  ```
  multicast ipv6 routing-enable
  ```
  ```
  #
  ```
  ```
  acl ipv6 number 2000
  ```
  ```
   rule 0 permit source FF3E::1/64
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
   ipv6 enable
  ```
  ```
   ipv6 address 2001:DB8:1::2/64
  ```
  ```
   pim ipv6 sm
  ```
  ```
   ospfv3 1 area 0.0.0.0
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
   ipv6 enable
  ```
  ```
   ipv6 address 2001:DB8:7::1/64
  ```
  ```
   pim ipv6 sm
  ```
  ```
   mld enable
  ```
  ```
   ospfv3 1 area 0.0.0.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/3/0
  ```
  ```
   undo shutdown
  ```
  ```
   ipv6 enable
  ```
  ```
   ipv6 address 2001:DB8:3::1/64
  ```
  ```
   pim ipv6 sm
  ```
  ```
   ospfv3 1 area 0.0.0.0
  ```
  ```
  #
  ```
  ```
  ospfv3 1
  ```
  ```
   router-id 2.2.2.2
  ```
  ```
   area 0.0.0.0
  ```
  ```
  #
  ```
  ```
  pim-ipv6
  ```
  ```
   ssm-policy 2000
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
  multicast ipv6 routing-enable
  ```
  ```
  #
  ```
  ```
  acl ipv6 number 2000
  ```
  ```
   rule 0 permit source FF3E::1/64
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
   ipv6 enable
  ```
  ```
   ipv6 address 2001:DB8:4::2/64
  ```
  ```
   pim ipv6 sm
  ```
  ```
   ospfv3 1 area 0.0.0.0
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
   ipv6 enable
  ```
  ```
   ipv6 address 2001:DB8:8::1/64
  ```
  ```
   pim ipv6 sm
  ```
  ```
   mld enable
  ```
  ```
   ospfv3 1 area 0.0.0.0
  ```
  ```
  #
  ```
  ```
  ospfv3 1
  ```
  ```
   router-id 3.3.3.3
  ```
  ```
   area 0.0.0.0
  ```
  ```
  #
  ```
  ```
  pim-ipv6
  ```
  ```
   ssm-policy 2000
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceD configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceD
  ```
  ```
  #
  ```
  ```
  multicast ipv6 routing-enable
  ```
  ```
  #
  ```
  ```
  acl ipv6 number 2000
  ```
  ```
   rule 0 permit source FF3E::1/64
  ```
  ```
  #
  ```
  ```
  acl ipv6 number 2001
  ```
  ```
   rule 0 permit source FF0E::1/64
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
   ipv6 enable
  ```
  ```
   ipv6 address 2001:DB8:2::2/64
  ```
  ```
   pim ipv6 sm
  ```
  ```
   ospfv3 1 area 0.0.0.0
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
   ipv6 enable
  ```
  ```
   ipv6 address 2001:DB8:3::2/64
  ```
  ```
   pim ipv6 sm
  ```
  ```
   ospfv3 1 area 0.0.0.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/3/0
  ```
  ```
   undo shutdown
  ```
  ```
   ipv6 enable
  ```
  ```
   ipv6 address 2001:DB8:4::1/64
  ```
  ```
   pim ipv6 sm
  ```
  ```
   ospfv3 1 area 0.0.0.0
  ```
  ```
  #
  ```
  ```
  ospfv3 1
  ```
  ```
   router-id 4.4.4.4
  ```
  ```
   area 0.0.0.0
  ```
  ```
  #
  ```
  ```
  pim-ipv6
  ```
  ```
   ssm-policy 2000
  ```
  ```
   c-bsr 2001:DB8:3::2
  ```
  ```
   c-rp 2001:DB8:3::2 group-policy 2001
  ```
  ```
  #
  ```
  ```
  return
  ```