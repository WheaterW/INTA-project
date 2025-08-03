Example for Configuring PIM-SM Security
=======================================

This section provides an example for configuring filtering policies, including setting a valid source address range and a valid Candidate-Rendezvous Point (C-RP) address range, to prevent malicious packet attacks on a PIM-SM network.

#### Networking Requirements

Multicast services need to be deployed on the network shown in [Figure 1](#EN-US_TASK_0172366921__fig15213210537). An IGP has been deployed on this network, and unicast traffic forwarding is normal. It is required that filtering policies be configured on each Router to improve the security of the multicast network and ensure that users can receive secure and reliable multicast data.

**Figure 1** Configuring PIM-SM security  
![](figure/en-us_image_0258925647.png)

| Device | Interface | IP Address |
| --- | --- | --- |
| DeviceA | GE 0/1/0 | 192.168.9.1/24 |
| GigabitEthernet0/3/0 | 192.168.1.1/24 |
| GigabitEthernet0/2/0 | 10.110.1.1/24 |
| DeviceB | GE 0/1/0 | 192.168.2.1/24 |
| GigabitEthernet0/2/0 | 10.110.2.1/24 |
| DeviceC | GE 0/2/0 | 192.168.3.1/24 |
| GigabitEthernet0/1/0 | 10.110.2.2/24 |
| DeviceD | GE 0/1/0 | 192.168.4.2/24 |
| GigabitEthernet0/2/0 | 192.168.1.2/24 |
| GigabitEthernet0/3/0 | 10.110.5.1/24 |
| DeviceE | GE 0/1/0 | 192.168.3.2/24 |
| GigabitEthernet0/2/0 | 192.168.2.2/24 |
| GigabitEthernet0/3/0 | 192.168.9.2/24 |
| GigabitEthernet0/1/1 | 192.168.4.1/24 |



#### Precautions

When configuring PIM security, note the following precautions:

* PIM-SM must be enabled before IGMP is enabled.
* The multicast group range that each C-RP serves and the valid C-RP address range can be set only on Candidate-BootStrap Routers (C-BSRs).
* Source address-based and BSR address-based filtering policies need to be configured on all Routers.
* Policies for filtering Register messages need to be configured on all C-RPs.
* Policies for filtering Join/Prune messages are generally configured on the last-hop Routers.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IP address for each involved interface and a unicast routing protocol on each Router.
2. Enable multicast routing on all multicast Routers.
3. Enable PIM-SM on all Router interfaces.
4. Enable IGMP on interfaces connected to hosts.
5. Configure C-BSRs and C-RPs if a BSR RP needs to be used.
6. Set the range of multicast groups that each C-RP serves on the C-BSR.
7. Create a policy for filtering Register messages on the C-RP to prevent the attacks of Register messages carrying invalid multicast source information.
8. Create source address-based filtering policies on all Routers to deny all multicast packets from attack sources.
9. Create BSR address-based filtering policies on all Routers to prevent BSR spoofing.

#### Data Preparation

To complete the configuration, you need the following data:

* Multicast group address
* IP address of the multicast source
* ACL rules for defining filtering policies

#### Procedure

1. Configure an IP address for each involved interface and a unicast routing protocol on each Router. For configuration details, see [Configuration Files](#EN-US_TASK_0172366921__example467012675214040) in this section.
2. Enable multicast routing on each Router and PIM-SM on each Router interface.
   
   
   
   # Configure DeviceA. Repeat this step for DeviceB, DeviceC, DeviceD, and DeviceE. For configuration details, see [Configuration Files](#EN-US_TASK_0172366921__example467012675214040) in this section.
   
   ```
   [~DeviceA] multicast routing-enable
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/2/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] pim sm
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceA] interface gigabitEthernet 0/1/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] pim sm
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceA] interface gigabitEthernet 0/3/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/3/0] pim sm
   ```
   ```
   [*DeviceA-GigabitEthernet0/3/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/3/0] quit
   ```
3. Enable IGMP on interfaces that directly connect to hosts.
   
   
   
   # Configure DeviceA. Repeat this step for DeviceB and DeviceC. For configuration details, see [Configuration Files](#EN-US_TASK_0172366921__example467012675214040) in this section.
   
   ```
   [~DeviceA] interface gigabitethernet 0/2/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0] igmp enable
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] igmp version 3
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0] quit
   ```
4. Configure C-BSRs and C-RPs.
   
   
   
   # Configure a C-BSR and a C-RP on DeviceE.
   
   ```
   [~DeviceE] pim
   ```
   ```
   [*DeviceE-pim] c-bsr gigabitEthernet 0/2/0
   ```
   ```
   [*DeviceE-pim] c-rp gigabitEthernet 0/2/0
   ```
   ```
   [*DeviceE-pim] commit
   ```
   ```
   [~DeviceE-pim] quit
   ```
5. Set the range of multicast groups that each C-RP serves and the valid C-RP address range on the C-BSR.
   
   
   
   # Configure DeviceE.
   
   ```
   [~DeviceE] acl number 3000
   ```
   ```
   [*DeviceE-acl4-advance-3000] rule permit ip source 192.168.2.2 0 destination 224.0.0.0 15.255.255.255
   ```
   ```
   [*DeviceE-acl4-advance-3000] quit
   ```
   ```
   [*DeviceE] pim
   ```
   ```
   [*DeviceE-pim] crp-policy 3000
   ```
   ```
   [*DeviceE-pim] commit
   ```
   ```
   [~DeviceE-pim] quit
   ```
6. Create a policy for filtering Register messages on the C-RP.
   
   
   
   # Configure DeviceE.
   
   ```
   [~DeviceE] acl number 3001
   ```
   ```
   [*DeviceE-acl4-advance-3001] rule permit ip source 10.110.5.0 0.0.0.255 destination 225.1.1.0 0.0.0.255
   ```
   ```
   [*DeviceE-acl4-advance-3001] quit
   ```
   ```
   [*DeviceE] pim
   ```
   ```
   [*DeviceE-pim] register-policy 3001
   ```
   ```
   [*DeviceE-pim] commit
   ```
   ```
   [~DeviceE-pim] quit
   ```
7. Configure source address-based and BSR address-based filtering policies on all the Routers.
   
   
   
   # Configure DeviceE. Repeat this step for DeviceA, DeviceB, DeviceC, and DeviceD. For configuration details, see [Configuration Files](#EN-US_TASK_0172366921__example467012675214040) in this section.
   
   ```
   [~DeviceE] acl number 2000
   ```
   ```
   [*DeviceE-acl4-basic-2000] rule permit source 10.110.5.0 0.0.0.255
   ```
   ```
   [*DeviceE-acl4-basic-2000] quit
   ```
   ```
   [*DeviceE] acl number 2001
   ```
   ```
   [*DeviceE-acl4-basic-2001] rule permit source 192.168.2.0 0.0.0.255
   ```
   ```
   [*DeviceE-acl4-basic-2001] quit
   ```
   ```
   [*DeviceE] pim
   ```
   ```
   [*DeviceE-pim] source-policy 2000
   ```
   ```
   [*DeviceE-pim] bsr-policy 2001
   ```
   ```
   [*DeviceE-pim] commit
   ```
   ```
   [~DeviceE-pim] quit
   ```
8. Verify the configuration.
   
   
   
   # Run the **display pim bsr-info** command to view information about the BSR on the Router. The BSR address matches the filtering rule. The following examples use the command outputs on DeviceD and DeviceE.
   
   ```
   <DeviceD> display pim bsr-info
   ```
   ```
    VPN-Instance: public net
    Elected AdminScope BSR Count: 0
    Elected BSR Address: 192.168.2.2
        Priority: 0
        Hash mask length: 30
        State: Accept Preferred
        Scope: Not scoped
        Uptime: 21:56:56
        Expires: 00:02:01
        C-RP Count: 1
   ```
   ```
   <DeviceE> display pim bsr-info
   ```
   ```
    VPN-Instance: public net
    Elected AdminScope BSR Count: 0
    Elected BSR Address: 192.168.2.2
        Priority: 0
        Hash mask length: 30
        State: Elected
        Scope: Not scoped
        Uptime: 21:57:15
        Next BSR message scheduled at: 00:00:14
        C-RP Count: 1
    Candidate AdminScope BSR Count: 0
    Candidate BSR Address: 192.168.2.2
        Priority: 0
        Hash mask length: 30
        State: Elected
        Scope: Not scoped
        Wait to be BSR: 0
   ```
   
   # Run the **display pim rp-info** command to view information about the RPs on the Routers. The RP address matches the filtering rule. The following examples use the command outputs on DeviceD and DeviceE.
   
   ```
   <DeviceD> display pim rp-info
   ```
   ```
    VPN-Instance: public net
    PIM-SM BSR RP Number:1
    Group/MaskLen: 224.0.0.0/4
        RP: 192.168.2.2
        Priority: 0
        Uptime: 01:27:21
        Expires: 00:02:11
   ```
   ```
   <DeviceE> display pim rp-info
   ```
   ```
    VPN-Instance: public net
    PIM-SM BSR RP Number:1
    Group/MaskLen: 224.0.0.0/4
        RP: 192.168.2.2 (local)
        Priority: 0
        Uptime: 01:29:10
        Expires: 00:02:20
   ```
   
   # Have hosts receive multicast data from a valid multicast source. Have multicast source 10.110.5.100 send multicast data, have Host A receive the data for multicast group 225.1.1.1/24, and have Host B receive the data for group 225.1.1.2/24. Run the **display pim routing-table** command to view information about the PIM routing table on each Router. The following examples use the command outputs on DeviceD and DeviceE.
   
   ```
   <DeviceD> display pim routing-table
   ```
   ```
    VPN-Instance: public net
    Total 0 (*, G) entry; 2 (S, G) entries
   
    (10.110.5.100, 225.1.1.1)
        RP: 192.168.2.2
        Protocol: pim-sm, Flag: SPT ACT
        UpTime: 00:57:20
        Upstream interface: GigabitEthernet0/3/0, Refresh time: 00:57:20
            Upstream neighbor: 10.110.5.100
            RPF prime neighbor: 10.110.5.100
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: GigabitEthernet0/2/0
                Protocol:  pim-sm, UpTime: 00:57:20, Expires: 00:03:02
   
    (10.110.5.100, 225.1.1.2)
        RP: 192.168.2.2
        Protocol: pim-sm, Flag: SPT ACT
        UpTime: 01:56:45
        Upstream interface: GigabitEthernet0/3/0, Refresh time: 01:56:45
            Upstream neighbor: 10.110.5.100
            RPF prime neighbor: 10.110.5.100
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: GigabitEthernet0/1/0
                Protocol:  pim-sm, UpTime: 01:56:45, Expires: 00:02:43
   
   ```
   ```
   <DeviceE> display pim routing-table
   ```
   ```
    VPN-Instance: public net
    Total 2 (*, G) entries; 1 (S, G) entry
   
    (*, 225.1.1.1)
        RP: 192.168.2.2 (local)
        Protocol: pim-sm, Flag: WC
        UpTime: 00:21:40
        Upstream interface: register, Refresh time: 00:21:40
            Upstream neighbor: 192.168.4.2
            RPF prime neighbor: 192.168.4.2
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: GigabitEthernet0/3/0
                Protocol:  pim-sm, UpTime: 00:21:40, Expires: 00:02:43
   
    (*, 225.1.1.2)
        RP: 192.168.2.2 (local)
        Protocol: pim-sm, Flag: WC
        UpTime: 00:21:40
        Upstream interface: register, Refresh time: 00:21:40
            Upstream neighbor: 192.168.4.2
            RPF prime neighbor: 192.168.4.2
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: GigabitEthernet0/1/0
                Protocol:  pim-sm, UpTime: 00:21:40, Expires: 00:02:43
   
    (10.110.5.100, 225.1.1.2)
        RP: 192.168.2.2
        Protocol: pim-sm, Flag: SPT ACT
        UpTime: 01:56:45
        Upstream interface: GigabitEthernet0/3/0, Refresh time: 01:56:45
            Upstream neighbor: 192.168.4.2
            RPF prime neighbor: 192.168.4.2
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: GigabitEthernet0/1/0
                Protocol:  pim-sm, UpTime: 01:56:45, Expires: 00:02:43
   
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  #
  multicast routing-enable
  #
  acl number 2000
   rule 5 permit source 10.110.5.0 0.0.0.255
  #
  acl number 2001
   rule 5 permit source 192.168.2.0 0.0.0.255
  #
  isis 1
   network-entity 10.0000.0000.0001.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 192.168.9.1 255.255.255.0
   pim sm
   isis enable 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.110.1.1 255.255.255.0
   pim sm
   igmp enable
   igmp version 3
   isis enable 1
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 192.168.1.1 255.255.255.0
   pim sm
   isis enable 1
  #
  pim
   bsr-policy 2001
   source-policy 2000
  #
  return
  
  ```
* DeviceB configuration file
  
  ```
  #
  sysname DeviceB
  #
  multicast routing-enable
  #
  acl number 2000
   rule 5 permit source 10.110.5.0 0.0.0.255
  #
  acl number 2001
   rule 5 permit source 192.168.2.0 0.0.0.255
  #
  isis 1
   network-entity 10.0000.0000.0002.00
  #
  interface GigabitEthernet0/1/0
   ip address 192.168.2.1 255.255.255.0
   isis enable 1
   pim sm
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.110.2.1 255.255.255.0
   isis enable 1
   pim sm
   igmp enable
   igmp version 3
  #
  pim
   bsr-policy 2001
   source-policy 2000
  #
  return
  
  ```
* DeviceC configuration file
  
  ```
  #
  sysname DeviceC
  #
  multicast routing-enable
  #
  acl number 2000
   rule 5 permit source 10.110.5.0 0.0.0.255
  #
  acl number 2001
   rule 5 permit source 192.168.2.0 0.0.0.255
  #
  isis 1
   network-entity 10.0000.0000.0003.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.110.2.2 255.255.255.0
   isis enable 1
   pim sm
   igmp enable
   igmp version 3
  #
  interface GigabitEthernet0/2/0
   ip address 192.168.3.1 255.255.255.0
   pim sm
   isis enable 1
  #
  pim
   bsr-policy 2001
   source-policy 2000
  #
  return
  
  ```
* DeviceD configuration file
  
  ```
  #
  sysname DeviceD
  #
  multicast routing-enable
  #
  acl number 2000
   rule 5 permit source 10.110.5.0 0.0.0.255
  #
  acl number 2001
   rule 5 permit source 192.168.2.0 0.0.0.255
  #
  isis 1
   network-entity 10.0000.0000.0004.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 192.168.4.2 255.255.255.0
   pim sm
   isis enable 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 192.168.1.2 255.255.255.0
   pim sm
   isis enable 1
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 10.110.5.1 255.255.255.0
   pim sm
   isis enable 1
  #
  pim
   bsr-policy 2001
   source-policy 2000
  #
  return
  ```
* DeviceE configuration file
  
  ```
  #
  sysname DeviceE
  #
  multicast routing-enable
  #
  acl number 2000
   rule 5 permit source 10.110.5.0 0.0.0.255
  #
  acl number 2001
   rule 5 permit source 192.168.2.0 0.0.0.255
  #
  acl number 3000
   rule 5 permit ip source 192.168.2.2 0 destination 224.0.0.0 15.255.255.255
  #
  acl number 3001
   rule 5 permit ip source 10.110.5.0 0.0.0.255 destination 225.1.1.0 0.0.0.255
  #
  isis 1
   network-entity 10.0000.0000.0005.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 192.168.3.2 255.255.255.0
   pim sm
   isis enable 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 192.168.2.2 255.255.255.0
   pim sm
   isis enable 1
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 192.168.9.2 255.255.255.0
   pim sm
   isis enable 1
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 192.168.4.1 255.255.255.0
   pim sm
   isis enable 1
  #
  pim
   bsr-policy 2001
   register-policy 3001
   source-policy 2000
   c-bsr GigabitEthernet0/2/0
   crp-policy 3000
   c-rp GigabitEthernet0/2/0
  #
  return
  ```