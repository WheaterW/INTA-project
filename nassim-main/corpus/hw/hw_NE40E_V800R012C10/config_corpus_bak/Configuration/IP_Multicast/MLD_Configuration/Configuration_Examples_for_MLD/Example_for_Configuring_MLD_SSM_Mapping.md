Example for Configuring MLD SSM Mapping
=======================================

If a host's MLD version is MLDv1 and cannot be upgraded to MLDv2, configure Source-Specific Multicast (SSM) mapping on the IPv6 multicast network to implement version compatibility between a multicast device (running a later MLD version) and user hosts (running an earlier MLD version) and enable the multicast device to provide SSM services for the user hosts. The user hosts can then receive IPv6 multicast data from a specified source.

#### Networking Requirements

On the IPv6 multicast network shown in [Figure 1](#EN-US_TASK_0172367450__fig_dc_vrp_multicast_cfg_209501), PIM-SM is run and the SSM mode is configured. MLDv2 is run on the interface connecting the Router to the receiver and MLDv1 is run on the receiver. The MLD version on the receiver is unable to be upgraded to MLDv2.

The SSM group address range is set to FF31::/32, and Sources 1, 2, and 3 all send IPv6 multicast data to multicast groups in this range. The receiver requires IPv6 multicast data only from Sources 1 and 3. To meet this requirement, configure MLD SSM mapping.

**Figure 1** Configuring MLD SSM mapping![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/1/0, GE 0/2/0, and GE0/3/0, respectively.


  
![](images/fig_dc_vrp_multicast_cfg_209501.png)

| Device | Interface | IP Address |
| --- | --- | --- |
| Device A | GE0/1/0 | 2001:db8:5::2/64 |
| GE0/2/0 | 2001:db8:1::1/64 |
| GE0/3/0 | 2001:db8:3::1/64 |
| DeviceB | GE0/1/0 | 2001:db8:6::2/64 |
| GE0/2/0 | 2001:db8:1::2/64 |
| GE0/3/0 | 2001:db8:2::1/64 |
| DeviceC | GE0/1/0 | 2001:db8:7::2/64 |
| GE0/2/0 | 2001:db8:4::1/64 |
| GE0/3/0 | 2001:db8:2::2/64 |
| DeviceD | GE0/1/0 | 2001:db8:8::2/64 |
| GE0/2/0 | 2001:db8:4::2/64 |
| GE0/3/0 | 2001:db8:3::2/64 |



#### Precautions

When configuring MLD SSM mapping, note the following precautions:

* IPv6 PIM-SM must be enabled before MLD is enabled.
* The SSM group address ranges set on all Routers in the IPv6 PIM-SM domain must be identical.
* To make SSM source-group address mapping entries take effect, you must enable SSM mapping first.

#### Configuration Roadmap

Configure SSM mapping on the Router connected to hosts so that the multicast device running a later version can provide the SSM service for hosts running an earlier version.

1. Configure an IPv6 address for each Router interface and configure a unicast routing protocol.
2. Enable IPv6 multicast routing on all Routers.
3. Enable IPv6 PIM-SM on all Router interfaces.
4. Enable MLD and SSM mapping on interfaces connecting Routers to receivers.
5. Set the SSM group address range on all Routers in the IPv6 PIM-SM domain.
6. Configure SSM mapping rules on Routers connected to receivers.

#### Data Preparation

To complete the configuration, you need the following data:

* SSM group address range
* IPv6 addresses of Sources 1 and 3

#### Procedure

1. Configure an IPv6 address for each Router interface and a unicast routing protocol. For configuration details, see Configuration Files in this section.
2. Enable IPv6 multicast routing on each Router and IPv6 PIM-SM on each Router interface.
   
   
   
   # Configure Device D. The configurations of Device A, Device B, and Device C are similar to the configuration of Device D. For configuration details, see Configuration Files in this section.
   
   ```
   [~DeviceD] multicast ipv6 routing-enable
   ```
   ```
   [*DeviceD] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] pim ipv6 sm
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceD] interface gigabitethernet 0/2/0
   ```
   ```
   [*DeviceD-GigabitEthernet0/2/0] pim ipv6 sm
   ```
   ```
   [*DeviceD-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceD] interface gigabitethernet 0/3/0
   ```
   ```
   [*DeviceD-GigabitEthernet0/3/0] pim ipv6 sm
   ```
   ```
   [*DeviceD-GigabitEthernet0/3/0] commit
   ```
   ```
   [~DeviceD-GigabitEthernet0/3/0] quit
   ```
3. Enable MLD and SSM mapping on the interface connecting the Router to the receiver.
   
   
   
   # Enable MLD and SSM mapping on GE 0/1/0 of Device D.
   
   ```
   [~DeviceD] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceD-GigabitEthernet0/1/0] mld enable
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] mld version 2
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] mld ssm-mapping enable
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceD-GigabitEthernet0/1/0] quit
   ```
4. Set an SSM group address range.
   
   
   
   # Set the SSM group address range to FF31::/32 on all Routers. The configurations of Device B, Device C, and Device D are similar to the configuration of Device A. For configuration details, see [Configuration Files](#EN-US_TASK_0172367450__example10277366214043) in this section.
   
   ```
   [~DeviceA] acl ipv6 number 2000
   ```
   ```
   [*DeviceA-acl6-basic-2000] rule permit source ff31::/32
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
5. Configure SSM mapping rules on the Router connected to the receiver.
   
   
   
   # On Device D, map the multicast groups in the range of FF31::/32 to Sources 1 and 3.
   
   ```
   [~DeviceD] mld
   ```
   ```
   [*DeviceD-mld] ssm-mapping ff31:: 32 2001:db8:5::1
   ```
   ```
   [*DeviceD-mld] ssm-mapping ff31:: 32 2001:db8:7::1
   ```
   ```
   [*DeviceD-mld] commit
   ```
   ```
   [~DeviceD-mld] quit
   ```
6. Verify the configuration.
   
   
   
   # View information about SSM mapping rules on Device D.
   
   ```
   <DeviceD> display mld ssm-mapping group
   MLD SSM-Mapping conversion table of VPN-Instance: public net
    Total 2 entries, 2 entries matched
   
    00001. (2001:DB8:5::1, FF31::)
   
    00002. (2001:DB8:7::1, FF31::)
   ```
   
   The command output shows that the receiver joins group FF31::1. # Run the **display mld group ssm-mapping** command to view source-group information on Router D. The command output is as follows:
   
   ```
   <DeviceD> display mld group ssm-mapping
   ```
   ```
   MLD SSM mapping Interface group report information of VPN-Instance: public net
   ```
   ```
    GigabitEthernet0/1/0 (2001:DB8:8::2):
   ```
   ```
     Total 1 MLD SSM-Mapping Group reported
   ```
   ```
      Group Address   Last Reporter   Uptime      Expires
   ```
   ```
      FF31::1         2001:DB8:8::1   00:01:44    00:00:26
   ```
   ```
   <DeviceD> display mld group ssm-mapping verbose
   ```
   ```
   Total entry on this router: 1
   Interface group report information of VPN-Instance: public net
    GigabitEthernet0/1/0(FE80::DD:84):
     Total entry on this interface: 1
     Total 1 MLD SSM-Mapping Group reported
      Group: FF31::1
        Uptime: 00:00:13
        Expires: 00:04:07
        Last reporter: FE80::10
        Last-listener-query-counter: 0
        Last-listener-query-timer-expiry: off
        Group mode: exclude
        Version1-host-present-timer-expiry: 00:04:07
   ```
   
   # Run the **display pim ipv6 routing-table** command to view information about the IPv6 PIM-SM routing table on Device D. The command output is as follows:
   
   ```
   <DeviceD> display pim ipv6 routing-table
   ```
   ```
   VPN-Instance: public net
   ```
   ```
    Total 0 (*, G) entry; 2 (S, G) entries
   ```
   ```
    (2001:DB8:5::1, FF31::1)
   ```
   ```
        Protocol: pim-ssm, Flag:SG_RCVR
   ```
   ```
        UpTime: 00:11:25
   ```
   ```
        Upstream interface: GigabitEthernet0/3/0, Refresh time: 00:11:25
   ```
   ```
            Upstream neighbor: 2001:DB8:3::1
   ```
   ```
            RPF prime neighbor: 2001:DB8:3::1
   ```
   ```
        Downstream interface(s) information:
   ```
   ```
        Total number of downstreams: 1
   ```
   ```
            1: GigabitEthernet0/1/0
   ```
   ```
                Protocol: mld, UpTime: 00:11:25, Expires:-
   ```
   ```
    (2001:DB8:7::1, FF31::1)
   ```
   ```
        Protocol: pim-ssm, Flag:SG_RCVR
   ```
   ```
        UpTime: 00:11:25
   ```
   ```
        Upstream interface: GigabitEthernet0/2/0, Refresh time: 00:11:25
   ```
   ```
            Upstream neighbor: 2001:DB8:4::1
   ```
   ```
            RPF prime neighbor: 2001:DB8:4::1
   ```
   ```
        Downstream interface(s) information:
   ```
   ```
        Total number of downstreams: 1
   ```
   ```
            1: GigabitEthernet0/1/0
   ```
   ```
                Protocol: mld, UpTime: 00:11:25, Expires:-
   ```

#### Configuration Files

* Device A configuration file
  
  ```
  #
  sysname DeviceA
  #
  multicast ipv6 routing-enable
  #
  acl ipv6 number 2000
   rule permit source ff31::/32
  #
  isis 1
   ipv6 enable topology ipv6
   network-entity 10.0000.0000.0001.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:5::2/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:1::1/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:3::1/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  pim-ipv6
  ssm-policy 2000
  #
  return
  ```
* Device B configuration file
  
  ```
  #
  sysname DeviceB
  #
  multicast ipv6 routing-enable
  #
  acl ipv6 number 2000
   rule permit source ff31::/32
  #
  isis 1
   ipv6 enable topology ipv6
   network-entity 10.0000.0000.0002.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:6::2/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:1::2
   pim ipv6 sm
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:2::1/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  pim-ipv6
   ssm-policy 2000
  #
  return
  ```
* Device C configuration file
  
  ```
  #
  sysname DeviceC
  #
  multicast ipv6 routing-enable
  #
  acl ipv6 number 2000
   rule permit source ff31::/32
  #
  isis 1
   ipv6 enable topology ipv6
   network-entity 10.0000.0000.0003.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:7::2/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:4::1/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:2::2/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  pim-ipv6
   ssm-policy 2000
  #
  return
  ```
* Device D configuration file
  
  ```
  #
  sysname DeviceD
  #
  multicast ipv6 routing-enable
  #
  acl ipv6 number 2000
   rule permit source ff31::/32
  #
  isis 1
   ipv6 enable topology ipv6
   network-entity 10.0000.0000.0004.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:8::2/64
   pim ipv6 sm
   mld enable
   mld version 2
   mld ssm-mapping enable
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:4::2/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:3::2/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  mld
   ssm-mapping ff31:: 32 2001:DB8:5::1
   ssm-mapping ff31:: 32 2001:DB8:7::1
  #
  pim-ipv6
   ssm-policy 2000
  #
  return
  ```