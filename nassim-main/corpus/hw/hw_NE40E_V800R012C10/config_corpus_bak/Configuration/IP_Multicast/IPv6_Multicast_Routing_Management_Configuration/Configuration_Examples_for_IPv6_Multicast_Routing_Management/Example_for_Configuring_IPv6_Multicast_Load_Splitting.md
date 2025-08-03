Example for Configuring IPv6 Multicast Load Splitting
=====================================================

On an IPv6 PIM-SM network stably running multicast services, configure a stable-preferred IPv6 load splitting policy to balance IPv6 traffic among equal-cost routes.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172367555__fig_dc_vrp_multicast_cfg_211101), there are three equal-cost routes between Host A and the multicast source. Host A needs to steadily receive multicast data from the multicast source. Configure a multicast load splitting policy to evenly distribute entries to equal-cost routes. In this manner, load balancing among the equal-cost routes is implemented.

**Figure 1** Configuring IPv6 multicast load splitting  
![](images/fig_dc_vrp_multicast_cfg_211101.png)  

| Device | Interface | IP Address |
| --- | --- | --- |
| Device A | GE 0/1/0 | 2001:db8:2001::2/64 |
| GigabitEthernet0/2/1 | 2001:db8:2002::1/64 |
| GigabitEthernet0/2/2 | 2001:db8:2003::1/64 |
| GigabitEthernet0/2/3 | 2001:db8:2004::1/64 |
| LoopBack0 | 2001:db8:2000::1/64 |
| DeviceB | GE 0/1/0 | 2001:db8:2002::2/64 |
| GigabitEthernet0/2/0 | 2001:db8:2005::1/64 |
| DeviceC | GE 0/1/0 | 2001:db8:2003::2/64 |
| GigabitEthernet0/2/0 | 2001:db8:2006::1/64 |
| DeviceD | GE 0/1/0 | 2001:db8:2004::2/64 |
| GigabitEthernet0/2/0 | 2001:db8:2007::1/64 |
| DeviceE | GE 0/1/1 | 2001:db8:2005::2/64 |
| GigabitEthernet0/1/2 | 2001:db8:2006::2/64 |
| GigabitEthernet0/1/3 | 2001:db8:2007::2/64 |
| GE 0/2/0 | 2001:db8:3001::1/64 |



#### Precautions

When configuring IPv6 multicast load splitting, note the following precautions:

* IPv6 PIM-SM must be enabled before Multicast Listener Discovery (MLD) is enabled.
* Five IPv6 load splitting policies are mutually exclusive. Configure one of them as needed.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IPv6 address for each Router interface.
2. Configure IS-IS IPv6 to implement communications among Routers and set the costs of the routes to be the same.
3. Enable IPv6 multicast routing on all Routers and IPv6 PIM-SM on each Router interface. Configure the Loopback interface on Device A as a Rendezvous Point (RP).
4. Configure stable-preferred IPv6 multicast load splitting on Device E to ensure the stability of IPv6 multicast services.
5. Because Host A requires to receive data from some multicast groups for a long period, configure the interface that connects Device E to Host A to statically join the multicast groups in batches.

#### Data Preparation

To complete the configuration, you need the following data:

* IPv6 address of the multicast source
* IPv6 address of each Router interface
* Addresses of the multicast groups that the interface connecting Device E to the host statically joins in batches

#### Procedure

1. Configure an IPv6 address for each Router interface. For configuration details, see Configuration Files in this section.
2. Configure IS-IS IPv6 to implement communications among Routers and set the costs of the routes to be the same. For configuration details, see Configuration Files in this section.
3. Enable IPv6 multicast routing on each Router and IPv6 PIM-SM on each Router interface.
   
   
   
   # Configure Device A. The configurations of Device B, Device C, Device D, and Device E are similar to the configuration of Device A. For configuration details, see Configuration Files in this section.
   
   ```
   [~DeviceA] multicast ipv6 routing-enable
   [*DeviceA] interface gigabitethernet 0/1/0
   [*DeviceA-GigabitEthernet0/1/0] pim ipv6 sm
   [*DeviceA-GigabitEthernet0/1/0] quit
   [*DeviceA] interface GigabitEthernet 0/2/1
   [*DeviceA-GigabitEthernet0/2/1] pim ipv6 sm
   [*DeviceA-GigabitEthernet0/2/1] quit
   [*DeviceA] interface GigabitEthernet 0/2/2
   [*DeviceA-GigabitEthernet0/2/2] pim ipv6 sm
   [*DeviceA-GigabitEthernet0/2/2] quit
   [*DeviceA] interface GigabitEthernet 0/2/3
   [*DeviceA-GigabitEthernet0/2/3] pim ipv6 sm
   [*DeviceA-GigabitEthernet0/2/3] quit
   [*DeviceA] interface loopback 0
   [*DeviceA-LoopBack0] pim ipv6 sm
   [*DeviceA-LoopBack0] commit
   [~DeviceA-LoopBack0] quit
   ```
4. Configure an RP on Device A.
   
   
   
   # Configure Loopback 0 on Device A as an RP.
   
   ```
   [~DeviceA] pim-ipv6
   [*DeviceA-pim6] c-bsr 2001:db8:2000::1
   [*DeviceA-pim6] c-rp 2001:db8:2000::1
   [*DeviceA-pim6] commit
   [~DeviceA-pim6] quit
   ```
5. Configure stable-preferred IPv6 load splitting on Device E.
   
   
   ```
   [~DeviceE] multicast ipv6 load-splitting stable-preferred
   ```
   ```
   [*DeviceE] commit
   ```
6. Configure the interface connecting Device E to the host to statically join multicast groups in batches.
   
   
   
   # Configure GE 0/2/0 to statically join groups FF13::1 to FF13::3 in batches.
   
   ```
   [~DeviceE] interface gigabitethernet 0/2/0
   [~DeviceE-GigabitEthernet0/2/0] mld static-group ff13::1 inc-step-mask 128 number 3
   [*DeviceE-GigabitEthernet0/2/0] commit
   [~DeviceE-GigabitEthernet0/2/0] quit
   ```
7. Verify the configuration.
   
   
   
   # Have multicast source (2001:db8:2001::1/64) send multicast data to groups FF13::1 to FF13::3. Have Host A receive the multicast data from the multicast source. Then, view brief information about the IPv6 PIM routing table on Device E.
   
   ```
   <DeviceE> display pim ipv6 routing-table brief
    VPN-Instance: public net
    Total 3 (*, G) entries; 3 (S, G) entries
   
     00001.(*, FF13::1)
          Upstream interface:GigabitEthernet0/1/1
          Number of downstream:1
     00002.(2001:DB8:2001::1, FF13::1)
          Upstream interface:GigabitEthernet0/1/1
          Number of downstream:1
     00003.(*, FF13::2)
          Upstream interface:GigabitEthernet0/1/2
          Number of downstream:1
     00004.(2001:DB8:2001::1, FF13::2)
          Upstream interface:GigabitEthernet0/1/2
          Number of downstream:1
     00005.(*, FF13::3)
          Upstream interface:GigabitEthernet0/1/3
          Number of downstream:1
     00006.(2001:DB8:2001::1, FF13::3)
          Upstream interface:GigabitEthernet0/1/3
          Number of downstream:1
   ```
   
   (\*, G) and (S, G) entries are equally distributed to the three equal-cost routes, with the upstream interfaces being GE 0/1/1, GE 0/1/2, and GE 0/1/3 respectively.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The load splitting algorithm processes (\*, G) and (S, G) entries separately and the process rules are the same.

#### Configuration Files

* Device A configuration file
  
  ```
  #
  sysname DeviceA
  #
  multicast ipv6 routing-enable
  #
  isis 1
   ipv6 enable topology ipv6
   network-entity 10.0000.0000.0001.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:2001::2/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/2/1
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:2002::1/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/2/2
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:2003::1/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/2/3
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:2004::1/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  interface LoopBack0
   ipv6 enable
   ipv6 address 2001:DB8:2000::1/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  pim-ipv6
   c-bsr 2001:DB8:2000::1
   c-rp 2001:DB8:2000::1
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
  isis 1
   ipv6 enable topology ipv6
   network-entity 10.0000.0000.0002.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:2002::2/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:2005::1/64
   pim ipv6 sm
   isis ipv6 enable 1
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
  isis 1
   ipv6 enable topology ipv6
   network-entity 10.0000.0000.0003.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:2003::2/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:2006::1/64
   pim ipv6 sm
   isis ipv6 enable 1
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
  isis 1
   ipv6 enable topology ipv6
   network-entity 10.0000.0000.0004.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:2004::2/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:2007::1/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  return
  ```
* Device E configuration file
  
  ```
  #
  sysname DeviceE
  #
  multicast ipv6 routing-enable
  multicast ipv6 load-splitting stable-preferred
  #
  isis 1
   ipv6 enable topology ipv6
   network-entity 10.0000.0000.0005.00
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:2005::2/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:2006::2/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:2007::2/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:3001::1/64
   pim ipv6 sm
   mld static-group FF13::1 inc-step-mask 128 number 3
   isis ipv6 enable 1
  #
  return
  ```