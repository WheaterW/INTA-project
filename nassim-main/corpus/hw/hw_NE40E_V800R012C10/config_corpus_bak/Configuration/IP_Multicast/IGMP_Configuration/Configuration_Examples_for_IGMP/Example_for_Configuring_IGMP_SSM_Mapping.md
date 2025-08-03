Example for Configuring IGMP SSM Mapping
========================================

If hosts' IGMP version can be upgraded to IGMPv1 or IGMPv2, not to IGMPv3, configure Source-Specific Multicast (SSM) mapping to implement version compatibility between a multicast device (running a higher IGMP version) and user hosts (running lower IGMP versions) and enable the multicast device to provide SSM services for the user hosts. The user hosts can then receive multicast data from a specified source.

#### Networking Requirements

On the multicast network shown in [Figure 1](#EN-US_TASK_0172366771__fig_dc_vrp_multicast_cfg_206901), PIM-SM is run and the SSM mode is configured. IGMPv3 is run on the interface connecting the Router to the receiver and IGMPv2 is run on the receiver. The IGMP version on the receiver is unable to be upgraded to IGMPv3.

The SSM group address range is set to 232.1.1.0/24, and Sources 1, 2, and 3 all send multicast data to multicast groups in this range. The receiver requires multicast data only from Sources 1 and 3. To meet this requirement, configure IGMP SSM mapping.

**Figure 1** Configuring IGMP SSM mapping![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1, 2, and 3 in this example represent GigabitEthernet0/1/0, GigabitEthernet0/2/0, and GigabitEthernet0/3/0, respectively.


  
![](images/fig_dc_vrp_multicast_cfg_206901.png)

| Device | Interface | IP Address |
| --- | --- | --- |
| DeviceA | GE0/1/0 | 10.10.1.2/24 |
| GE0/2/0 | 192.168.1.1/24 |
| GE0/3/0 | 192.168.4.2/24 |
| DeviceB | GE0/1/0 | 10.10.2.2/24 |
| GE0/2/0 | 192.168.1.2/24 |
| GE0/3/0 | 192.168.2.1/24 |
| DeviceC | GE0/1/0 | 10.10.3.2/24 |
| GE0/2/0 | 192.168.3.1/24 |
| GE0/3/0 | 192.168.2.2/24 |
| DeviceD | GE0/1/0 | 10.10.4.2/24 |
| GE0/2/0 | 192.168.3.2/24 |
| GE0/3/0 | 192.168.4.1/24 |



#### Precautions

During configuration, note the following precautions:

* PIM-SM and IGMP need to be enabled in succession on the interfaces connecting to the hosts.
* The ranges of SSM group addresses configured on all Routers in a PIM-SM domain must be the same.
* The basic IGMP function must be configured before IGMP SSM mapping is configured. For detailed configuration information, see the [Example for Configuring Basic IGMP Functions](dc_vrp_multicast_cfg_2068.html).
* To make SSM source-group address mapping entries take effect, you must enable SSM mapping first.

#### Configuration Roadmap

1. Assign IP addresses to Router interfaces and configure a unicast routing protocol.
2. Enable multicast routing on all Routers that provide multicast services.
3. Enable PIM-SM on all interfaces of Routers that provide multicast services.
4. Enable IGMP and SSM mapping on interfaces connected to hosts.
5. Configure the SSM group address range on all Routers in the PIM-SM domain.
6. Configure static SSM mapping rules on Routers connected to hosts.

#### Data Preparation

To complete the configuration, you need the following data:

* SSM group address range
* IP addresses of Sources 1 and 3

#### Procedure

1. Configure an IP address for each Router interface and a unicast routing protocol. For configuration details, see Configuration Files in this section.
2. Enable the multicast function on each Router, and enable PIM-SM on Router interfaces.
   
   
   
   # Configure Device D. The configurations of Device A, Device B, and Device C are similar to the configuration of Device D. For configuration details, see Configuration Files in this section.
   
   ```
   [~DeviceD] multicast routing-enable
   ```
   ```
   [*DeviceD] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] pim sm
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceD] interface gigabitethernet 0/2/0
   ```
   ```
   [*DeviceD-GigabitEthernet0/2/0] pim sm
   ```
   ```
   [*DeviceD-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceD] interface gigabitethernet 0/3/0
   ```
   ```
   [*DeviceD-GigabitEthernet0/3/0] pim sm
   ```
   ```
   [*DeviceD-GigabitEthernet0/3/0] commit
   ```
   ```
   [~DeviceD-GigabitEthernet0/3/0] quit
   ```
3. Enable IGMP and SSM mapping on interfaces connected to hosts.
   
   
   
   # Enable IGMP and SSM mapping on GE 0/1/0 of Device D.
   
   ```
   [~DeviceD] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceD-GigabitEthernet0/1/0] igmp enable
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] igmp version 3
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] igmp ssm-mapping enable
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceD-GigabitEthernet0/1/0] quit
   ```
4. Set the SSM group address range.
   
   
   
   Set the SSM group address range to 232.1.1.0/24 on all Routers in the PIM-SM domain. The configurations of Device B, Device C, and Device D are similar to the configuration of Device A. For configuration details, see Configuration Files in this section.
   
   ```
   [~DeviceA] acl number 2000
   ```
   ```
   [*DeviceA-acl4-basic-2000] rule permit source 232.1.1.0 0.0.0.255
   ```
   ```
   [*DeviceA-acl4-basic-2000] quit
   ```
   ```
   [*DeviceA] pim
   ```
   ```
   [*DeviceA-pim] ssm-policy 2000
   ```
   ```
   [*DeviceA-pim] commit
   ```
   ```
   [~DeviceA-pim] quit
   ```
5. Configure SSM mapping rules on the Router connected to the receiver.
   
   
   
   # On Device D, map the multicast groups in the range of 232.1.1.0/24 to Sources 1 and 3.
   
   ```
   [~DeviceD] igmp
   ```
   ```
   [*DeviceD-igmp] ssm-mapping 232.1.1.0 24 10.10.1.1
   ```
   ```
   [*DeviceD-igmp] ssm-mapping 232.1.1.0 24 10.10.3.1
   ```
   ```
   [*DeviceD-igmp] commit
   ```
   ```
   [~DeviceD-igmp] quit
   ```
6. Verify the configuration.
   
   
   
   # View information about SSM mapping rules on Device D.
   
   ```
   <DeviceD> display igmp ssm-mapping group
   ```
   ```
   IGMP SSM-Mapping conversion table of VPN-Instance: public net
   ```
   ```
    Total 2 entries    2 entries matched
   ```
   ```
    00001. (10.10.1.1, 232.1.1.0)
   ```
   ```
    00002. (10.10.3.1, 232.1.1.0)
   ```
   ```
    Total 2 entries matched
   ```
   
   # Run the **display igmp group ssm-mapping** command to view source-group information on Routers. The command output on DeviceD is as follows:
   
   ```
   <DeviceD> display igmp group ssm-mapping
   ```
   ```
   IGMP SSM mapping Interface group report information of VPN-Instance: public net
   ```
   ```
    GigabitEthernet0/1/0 (10.10.4.2):
   ```
   ```
     Total 1 IGMP SSM-Mapping Group reported
   ```
   ```
      Group Address   Last Reporter   Uptime      Expires
   ```
   ```
      232.1.1.1       10.10.4.1     00:01:44    00:00:26
   ```
   ```
   <DeviceD> display igmp group ssm-mapping verbose
   ```
   ```
   Interface group report information of VPN-Instance: public net 
   ```
   ```
    Limited entry of this VPN-Instance: - 
   ```
   ```
    GigabitEthernet0/1/0 (10.10.4.2):
   ```
   ```
     Total entry on this interface: 1
   ```
   ```
     Limited entry on this interface: - 
   ```
   ```
     Total 1 IGMP SSM-Mapping Group reported
   ```
   ```
      Group: 232.1.1.1
   ```
   ```
        Uptime: 00:01:52
   ```
   ```
        Expires: 00:00:18
   ```
   ```
        Last reporter: 10.10.4.1
   ```
   ```
        Last-member-query-counter: 0
   ```
   ```
        Last-member-query-timer-expiry: off
   ```
   ```
        Group mode: exclude
   ```
   ```
        Version1-host-present-timer-expiry: off
   ```
   ```
        Version2-host-present-timer-expiry: 00:00:17
   ```
   
   # Run the **display pim routing-table** command to view information about the PIM-SM routing table. The command output on DeviceD is as follows:
   
   ```
   <DeviceD> display pim routing-table
   ```
   ```
   VPN-Instance: public net
   ```
   ```
    Total 0 (*, G) entry; 2 (S, G) entries
   ```
   ```
    (10.10.1.1, 232.1.1.1)
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
            Upstream neighbor: 192.168.4.2
   ```
   ```
            RPF prime neighbor: 192.168.4.2
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
                Protocol: ssm-map, UpTime: 00:11:25, Expires:-
   ```
   ```
    (10.10.3.1, 232.1.1.1)
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
            Upstream neighbor: 192.168.3.1
   ```
   ```
            RPF prime neighbor: 192.168.3.1
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
                Protocol: ssm-map, UpTime: 00:11:25, Expires:-
   ```

#### Configuration Files

* Device A configuration file
  
  ```
  #
  sysname DeviceA
  #
  multicast routing-enable
  #
  acl number 2000
   rule permit source 232.1.1.0 0.0.0.255
  #
  isis 1
   network-entity 10.0000.0000.0001.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.10.1.2 255.255.255.0
   pim sm
   isis enable 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 192.168.1.1 255.255.255.0
   pim sm
   isis enable 1
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 192.168.4.2 255.255.255.0
   pim sm
   isis enable 1
  #
  pim
   ssm-policy 2000
  #
  return
  ```
* Device B configuration file
  
  ```
  #
  sysname DeviceB
  #
  multicast routing-enable
  #
  acl number 2000
   rule permit source 232.1.1.0 0.0.0.255
  #
  isis 1
   network-entity 10.0000.0000.0002.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.10.2.2 255.255.255.0
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
   ip address 192.168.2.1 255.255.255.0
   pim sm
   isis enable 1
  #
  pim
   ssm-policy 2000
  #
  return
  ```
* Device C configuration file
  
  ```
  #
  sysname DeviceC
  #
  multicast routing-enable
  #
  acl number 2000
   rule permit source 232.1.1.0 0.0.0.255
  #
  isis 1
   network-entity 10.0000.0000.0003.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.10.3.2 255.255.255.0
   pim sm
   isis enable 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 192.168.3.1 255.255.255.0
   pim sm
   isis enable 1
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 192.168.2.2 255.255.255.0
   pim sm
   isis enable 1
  #
  pim
   ssm-policy 2000
  #
  return
  ```
* Device D configuration file
  
  ```
  #
  sysname DeviceD
  #
  multicast routing-enable
  #
  acl number 2000
   rule permit source 232.1.1.0 0.0.0.255
  #
  isis 1
   network-entity 10.0000.0000.0004.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.10.4.2 255.255.255.0
   isis enable 1
   pim sm
   igmp enable
   igmp version 3
   igmp ssm-mapping enable
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   
   pim sm
   isis enable 1
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 192.168.4.1 255.255.255.0
   pim sm
   isis enable 1
  #
  igmp
   ssm-mapping 232.1.1.0 255.255.255.0 10.10.1.1
   ssm-mapping 232.1.1.0 255.255.255.0 10.10.3.1
  #
  pim
   ssm-policy 2000
  #
  return
  ```