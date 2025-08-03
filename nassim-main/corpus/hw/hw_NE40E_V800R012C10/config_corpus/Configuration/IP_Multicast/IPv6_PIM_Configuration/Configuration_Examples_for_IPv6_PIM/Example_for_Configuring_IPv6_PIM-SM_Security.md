Example for Configuring IPv6 PIM-SM Security
============================================

To prevent packet attacks, you can configure filtering policies to improve IPv6 PIM network security, including configuring valid source address ranges and Candidate-Rendezvous Point (C-RP) address ranges.

#### Networking Requirements

On the ISP network shown in [Figure 1](#EN-US_TASK_0172367525__fig_dc_vrp_multicast_cfg_203901), IPv6 multicast services are deployed. An Interior Gateway Protocol (IGP) has been deployed on the network, and IPv6 unicast is running properly. It is required that filtering policies be configured on each Router to improve the security of the IPv6 multicast network and ensure that users can receive secure and reliable IPv6 multicast data.

**Figure 1** Configuring IPv6 PIM-SM security![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1, 2, 3, and 4 in this example represent GE 0/1/0, GE 0/2/0, GE 0/3/0, and GE 0/1/1, respectively.


  
![](images/fig_dc_vrp_multicast_cfg_203901.png)

#### Precautions

When configuring IPv6 PIM security, note the following precautions:

* IPv6 PIM-SM must be enabled before Multicast Listener Discovery (MLD) is enabled.
* The multicast group range that each C-RP serves and the valid C-RP address range can be set only on Candidate-BootStrap Routers (C-BSRs).
* Source address-based and BSR address-based filtering policies need to be configured on all Routers.
* Policies for filtering Register messages need to be configured on all C-RPs.
* Policies for filtering Join/Prune messages are generally configured on the last-hop Router.

#### Configuration Roadmap

Use PIM-SM to configure IPv6 multicast functions. To ensure the security of an IPv6 PIM network, you can configure filtering policies to limit the range of source addresses, BSR addresses, and RP addresses, filter Register messages, Join/Prune messages, and filter PIM neighbors.

1. Configure an IPv6 address for each Router interface and an IPv6 unicast routing protocol.
2. Enable IPv6 multicast routing on all Routers.
3. Enable IPv6 PIM-SM on all Router interfaces.
4. Enable MLD on interfaces that directly connect Routers to hosts.
5. Configure C-BSRs and C-RPs to elect an RP.
6. Set the range of multicast groups that each C-RP serves on the C-BSR.
7. Create a policy for filtering Register messages on the C-RP to prevent attacks of the Register messages carrying invalid multicast source information.
8. Create source address-based filtering policies on all Routers to deny all multicast packets from attack sources.
9. Create BSR address-based filtering policies on all Routers to prevent BSR spoofing.

#### Data Preparation

To complete the configuration, you need the following data:

* Multicast group address
* Multicast source address
* ACL rules for defining filtering policies

#### Procedure

1. Configure an IPv6 address for each Router interface and an IPv6 unicast routing protocol. For configuration details, see Configuration Files in this section.
2. Enable IPv6 multicast routing on all routers and IPv6 PIM-SM on each Router interface.
   
   
   
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
   [*DeviceA-GigabitEthernet0/3/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/3/0] quit
   ```
3. Enable MLD on the interfaces connected to hosts.
   
   
   
   # Configure DeviceB. The configuration of DeviceC is similar to the configuration of DeviceB. For configuration details, see Configuration Files in this section.
   
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
4. Configure C-BSRs and C-RPs.
   
   
   
   # Configure the locations of C-BSRs and C-RPs on Device D.
   
   ```
   [*DeviceD] pim-ipv6
   ```
   ```
   [*DeviceD-pim6] c-rp 2001:db8:3::2
   ```
   ```
   [*DeviceD-pim6] c-bsr 2001:db8:3::2
   ```
   ```
   [*DeviceD-pim6] commit
   ```
   ```
   [~DeviceD-pim6] quit
   ```
5. Configure the range of multicast groups that each C-RP serves and the range of valid C-RP addresses on the C-BSRs.
   
   
   
   # On DeviceD, configure the range of multicast groups served by each C-RP to ff00::/8 and the range of valid C-RP addresses to 2001:db8:3::2/128.
   
   ```
   [~DeviceD] acl ipv6 number 3000
   ```
   ```
   [*DeviceD-acl6-advance-3000] rule permit ipv6 source 2001:db8:3::2 128 destination ff00:: 8
   ```
   ```
   [*DeviceD-acl6-advance-3000] quit
   ```
   ```
   [*DeviceD] pim-ipv6
   ```
   ```
   [*DeviceD-pim6] crp-policy 3000
   ```
   ```
   [*DeviceD-pim6] commit
   ```
   ```
   [~DeviceD-pim6] quit
   ```
6. Configure a policy for filtering Register messages on all the C-RPs.
   
   
   
   # On DeviceD, configure a policy for filtering Register messages, allowing an RP to receive only Register messages sent by multicast sources in the range of 2001:db8:5::5/64 to multicast groups in the range of ff0e::1/64.
   
   ```
   [~DeviceD] acl ipv6 number 3001
   ```
   ```
   [*DeviceD-acl6-advance-3001] rule permit ipv6 source 2001:db8:5::5 64 destination ff0e::1 64
   ```
   ```
   [*DeviceD-acl6-advance-3001] quit
   ```
   ```
   [*DeviceD] pim-ipv6
   ```
   ```
   [*DeviceD-pim6] register-policy 3001
   ```
   ```
   [*DeviceD-pim6] commit
   ```
   ```
   [~DeviceD-pim6] quit
   ```
7. Configure source address-based and BSR address-based filtering policies on all the Routers.
   
   
   
   # Configure RouterA. The configurations of RouterB, RouterC, and RouterD are similar to the configuration of RouterA. For configuration details, see Configuration Files in this section.
   
   ```
   [~DeviceA] acl ipv6 number 2000
   ```
   ```
   [*DeviceA-acl6-basic-2000] rule permit source 2001:db8:5::5 64
   ```
   ```
   [*DeviceA-acl6-basic-2000] quit
   ```
   ```
   [*DeviceA] acl ipv6 number 2001
   ```
   ```
   [*DeviceA-acl6-basic-2001] rule permit source 2001:db8:3::2 64
   ```
   ```
   [*DeviceA-acl6-basic-2001] quit
   ```
   ```
   [*DeviceA] pim-ipv6
   ```
   ```
   [*DeviceA-pim6] source-policy 2000
   ```
   ```
   [*DeviceA-pim6] bsr-policy 2001
   ```
   ```
   [*DeviceA-pim6] commit
   ```
   ```
   [~DeviceA-pim6] quit
   ```
8. Verify the configuration.
   
   
   
   # Run the **display pim ipv6 bsr-info** command to check BSR information on each Router. You can see that the BSR address-based filtering policy takes effect. The following example uses the command output on DeviceB and DeviceD.
   
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
   
   # Run the **display pim ipv6 rp-info** command to check RP information on each Router. The following example uses the command output on DeviceB.
   
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
    Group/MaskLen: FF00::/8
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
   
   # Have the multicast source S (2001:db8:5::5) send multicast packets to multicast group FF15::1. The hosts can receive multicast data sent by the valid multicast source. Then, run the **display pim ipv6 routing-table** command to check the IPv6 PIM routing table on each Router.
   
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
    (2001:DB8:5::5, FF15::1)
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
   <DeviceB> display pim ipv6 routing-table
   ```
   ```
   VPN-Instance: public net
   ```
   ```
    Total 1 (*, G) entry; 2 (S, G) entries
   
   ```
   ```
    (*, FF15::1)
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
   (2001:DB8:5::5, FF15::1)
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
   <DeviceC> display pim ipv6 routing-table
   ```
   ```
   VPN-Instance: public net
   ```
   ```
    Total 1 (*, G) entry; 1 (S, G) entry
   
   ```
   ```
    (*, FF15::1)
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
   (2001:DB8:5::5, FF15::1)
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
    (2001:DB8:5::5, FF15::1)
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
   rule 5 permit source 2001:DB8:5::5 64
  ```
  ```
  #
  acl ipv6 number 2001
   rule 5 permit source 2001:DB8:3::2 64
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
   bsr-policy 2001
   source-policy 2000
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
   rule 5 permit source 2001:DB8:5::5 64
  ```
  ```
  #
  acl ipv6 number 2001
   rule 5 permit source 2001:DB8:3::2 64
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
   bsr-policy 2001
   source-policy 2000
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
   rule 5 permit source 2001:DB8:5::5 64
  ```
  ```
  #
  acl ipv6 number 2001
   rule 5 permit source 2001:DB8:3::2 64
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
   bsr-policy 2001
   source-policy 2000
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
   ipv6
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
   rule 5 permit source 2001:DB8:5::5 64
  ```
  ```
  #
  acl ipv6 number 2001
   rule 5 permit source 2001:DB8:3::2 64
  ```
  ```
  #
  acl ipv6 number 3000
   rule 5 permit ipv6 source 2001:DB8:3::2 128 destination ff00:: 8
  #
  acl ipv6 number 3001
   rule 5 permit ipv6 source 2001:DB8:5::5 64 destination ff0e::1 64
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
   ospfv3 1 area 0.0.0.0
  ```
  ```
   pim ipv6 sm
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
   ospfv3 1 area 0.0.0.0
  ```
  ```
   pim ipv6 sm
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
   ospfv3 1 area 0.0.0.0
  ```
  ```
   pim ipv6 sm
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
   bsr-policy 2001
   register-policy 3001
   source-policy 2000
   c-bsr 2001:DB8:3::2
   crp-policy 3000
   c-rp 2001:DB8:3::2
  ```
  ```
  #
  ```
  ```
  return
  ```