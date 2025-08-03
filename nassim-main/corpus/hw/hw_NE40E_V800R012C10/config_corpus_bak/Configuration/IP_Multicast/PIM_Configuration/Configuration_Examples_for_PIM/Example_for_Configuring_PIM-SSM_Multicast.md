Example for Configuring PIM-SSM Multicast
=========================================

This section provides an example for configuring basic Protocol Independent Multicast-Source-Specific Multicast (PIM-SSM) functions so that hosts can receive multicast data from specific multicast source.

#### Networking Requirements

On the ISP network shown in [Figure 1](#EN-US_TASK_0172366927__fig_dc_vrp_multicast_cfg_004101), multicast services are deployed. An IGP has been deployed on this network, and unicast traffic forwarding is normal. It is required that hosts on the network can join source-specific multicast groups.

**Figure 1** Configuring PIM-SSM multicast  
![](images/fig_dc_vrp_multicast_cfg_004101.png)

**Table 1** 
| Device | Interface | IP Address |
| --- | --- | --- |
| Device A | GE 0/1/0 | 192.168.2.1/24 |
| GigabitEthernet0/2/0 | 10.110.1.2/24 |
| DeviceB | GE 0/1/0 | 192.168.2.2/24 |
| GE 0/2/0 | 192.168.4.1/24 |
| Device C | GE 0/1/0 | 192.168.4.2/24 |
| GigabitEthernet0/2/0 | 10.110.2.1/24 |



#### Precautions

When configuring PIM-SSM multicast, note the following precautions:

* PIM-SM must be enabled before IGMP is enabled.
* You must set the same SSM group address range on all Routers.
* A Rendezvous Point (RP) must be configured on the PIM-SSM network.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IP address for each Router interface and configure a unicast routing protocol.
2. Enable multicast routing on all multicast Routers.
3. Enable PIM-SM on all Router interfaces.
4. Enable IGMP on interfaces that directly connect to hosts.
5. Set the same SSM group address range on all Routers.

#### Data Preparation

To complete the configuration, you need the following data:

* IP address of the multicast source
* SSM group address range

#### Procedure

1. Configure an IP address for each Router interface and a unicast routing protocol. For configuration details, see [Configuration Files](#EN-US_TASK_0172366927__example871923596214040) in this section.
2. Enable multicast routing on each Router and PIM-SM on each Router interface.
   
   
   
   # Configure Device A. Repeat this step for Device B and Device C. For configuration details, see [Configuration Files](#EN-US_TASK_0172366927__example871923596214040) in this section.
   
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
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] quit
   ```
3. Enable IGMP on Device interfaces that directly connect to hosts.
   
   
   
   # Enable IGMP on the interface connecting Device C to the host and set the IGMP version to 3.
   
   ```
   [~DeviceC] interface gigabitethernet 0/2/0
   ```
   ```
   [~DeviceC-GigabitEthernet0/2/0] igmp enable
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] igmp version 3
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] commit
   ```
   ```
   [~DeviceC-GigabitEthernet0/2/0] quit
   ```
4. Set the SSM group address range to 232.1.1.0/24 on all Devices.
   
   
   
   # Configure Router A. Repeat this step for Device B and Device C. For configuration details, see [Configuration Files](#EN-US_TASK_0172366927__example871923596214040) in this section.
   
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
5. Verify the configuration.
   
   
   
   # Have Host A receive the data sent from source 10.110.1.1/24 to group 232.1.1.1/24. Then, run the **display pim routing-table** command to view information about the PIM routing table on each Router. The following examples use the command outputs on Device A and Device B.
   
   ```
   <DeviceA> display pim routing-table
   ```
   ```
    VPN-Instance: public net
    Total 0 (*, G) entry; 1 (S, G) entry
   
    (10.110.1.1, 232.1.1.1)
        Protocol: pim-ssm, Flag: LOC
        UpTime: 00:02:13
        Upstream interface: GigabitEthernet0/2/0, Refresh time: 00:02:13
            Upstream neighbor: 10.110.1.1
            RPF prime neighbor: 10.110.1.1
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: GigabitEthernet0/1/0
                Protocol:  pim-ssm, UpTime: 00:02:13, Expires: 00:03:17
   
   ```
   ```
   <DeviceB> display pim routing-table
   ```
   ```
    VPN-Instance: public net
    Total 0 (*, G) entry; 1 (S, G) entry
   
    (10.110.1.1, 232.1.1.1)
        Protocol: pim-ssm, Flag:
        UpTime: 00:09:15
        Upstream interface: GigabitEthernet0/1/0, Refresh time: 00:09:15
            Upstream neighbor: 192.168.2.1
            RPF prime neighbor: 192.168.2.1
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: GigabitEthernet0/2/0
                Protocol:  pim-ssm, UpTime: 00:09:15, Expires: 00:03:13
   
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
   rule 5 permit source 232.1.1.0 0.0.0.255
  #
  isis 1
   network-entity 10.0000.0000.0001.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 192.168.2.1 255.255.255.0
   pim sm
   isis enable 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.110.1.2 255.255.255.0
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
   rule 5 permit source 232.1.1.0 0.0.0.255
  #
  isis 1
   network-entity 10.0000.0000.0002.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 192.168.2.2 255.255.255.0
   pim sm
   isis enable 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 192.168.4.1 255.255.255.0
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
   rule 5 permit source 232.1.1.0 0.0.0.255
  #
  isis 1
   network-entity 10.0000.0000.0003.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 192.168.4.2 255.255.255.0
   pim sm
   isis enable 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.110.2.1 255.255.255.0
   pim sm
   igmp enable
   igmp version 3
   isis enable 1
  #
  pim
   ssm-policy 2000
  #
  return
  
  ```