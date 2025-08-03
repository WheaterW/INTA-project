Example for Configuring Basic IGMP Functions
============================================

This section provides an example for configuring basic IGMP functions.

#### Networking Requirements

On the ISP network shown in [Figure 1](#EN-US_TASK_0172366768__fig_dc_vrp_multicast_cfg_206801), multicast services are deployed. An IGP has been deployed on the network, and unicast is running properly. Hosts on the network are required to receive VOD information in multicast mode. HostA and HostB are required to steadily receive popular programs from the multicast group 225.1.1.1.

**Figure 1** Configuring basic IGMP functions![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface1, interface2, interface3, and interface4 in this example represent GigabitEthernet0/1/0, GigabitEthernet0/2/0, GigabitEthernet0/2/2, and GigabitEthernet0/2/3, respectively.


  
![](images/fig_dc_vrp_multicast_cfg_206801.png)

| Device | Interface | IP Address |
| --- | --- | --- |
| DeviceA | GigabitEthernet0/2/0 | 192.168.1.1/24 |
| GigabitEthernet0/1/0 | 10.110.1.1/24 |
| DeviceB | GigabitEthernet0/2/0 | 192.168.2.1/24 |
| GigabitEthernet0/1/0 | 10.110.2.1/24 |
| DeviceC | GigabitEthernet0/2/0 | 192.168.3.1/24 |
| GigabitEthernet0/1/0 | 10.110.2.2/24 |
| DeviceD | GigabitEthernet0/1/0 | 192.168.4.1/24 |
| GigabitEthernet0/2/0 | 192.168.1.2/24 |
| GigabitEthernet0/2/2 | 192.168.2.2/24 |
| GigabitEthernet0/2/3 | 192.168.3.2/24 |



#### Precautions

During configuration, note the following precautions:

* Both IGMP and PIM-SM must be enabled on the interfaces directly connected to hosts.
* Interfaces connected to the same user network segment must run the same IGMP version.

#### Configuration Roadmap

1. Configure an IP address for each Router interface and configure a unicast routing protocol.
2. Enable multicast routing on all multicast Routers.
3. Enable PIM-SM on Router interfaces.
4. Enable IGMP on interfaces that connect to hosts.
5. Configure GE 0/1/0 on Device A to statically join IGMP group 225.1.1.1.

#### Data Preparation

To complete the configuration, you need the following data:

* IGMPv2 runs on Routers and hosts
* Address of the IGMP group that the interface statically joins

#### Procedure

1. Configure an IP address for each Router interface and a unicast routing protocol. For configuration details, see Configuration Files in this section.
2. Enable multicast routing on each Router and PIM-SM on each Router interface.
   
   
   
   # Configure Device D.
   
   ```
   [~DeviceD] multicast routing-enable
   ```
   ```
   [*DeviceD] interface GigabitEthernet 0/1/0
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] pim sm
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceD] interface GigabitEthernet 0/2/0
   ```
   ```
   [*DeviceD-GigabitEthernet0/2/0] pim sm
   ```
   ```
   [*DeviceD-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceD] interface GigabitEthernet 0/2/2
   ```
   ```
   [*DeviceD-GigabitEthernet0/2/2] pim sm
   ```
   ```
   [*DeviceD-GigabitEthernet0/2/2] quit
   ```
   ```
   [*DeviceD] interface GigabitEthernet 0/2/3
   ```
   ```
   [*DeviceD-GigabitEthernet0/2/3] pim sm
   ```
   ```
   [*DeviceD-GigabitEthernet0/2/3] commit
   ```
   ```
   [~DeviceD-GigabitEthernet0/2/3] quit
   ```
   
   Repeat this step for Device A, Device B, and Device C. For configuration details, see Configuration Files in this section.
3. Configure a Rendezvous Point (RP).
   
   
   
   # Configure BSR RP on Device D.
   
   ```
   [~DeviceD] pim
   ```
   ```
   [*DeviceD-pim] c-bsr GigabitEthernet 0/1/0
   ```
   ```
   [*DeviceD-pim] c-rp GigabitEthernet 0/1/0
   ```
   ```
   [*DeviceD-pim] commit
   ```
   ```
   [~DeviceD-pim] quit
   ```
4. Enable IGMP on interfaces that connect to hosts.
   
   
   
   # Configure Device A.
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] igmp enable
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] quit
   ```
   
   Repeat this step for Device B and Device C. For configuration details, see Configuration Files in this section.
5. Configure GE 0/1/0 on Device A to statically join IGMP group 225.1.1.1.
   
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] igmp static-group 225.1.1.1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] quit
   ```
6. Verify the configuration.
   
   
   
   # Run the **display igmp interface** command to view brief IGMP information on the Router interfaces. The following example uses IGMP information on GE 0/1/0 of Device B.
   
   ```
   <DeviceB> display igmp interface
   ```
   ```
   Interface information of VPN-Instance: public net
    GigabitEthernet0/1/0(10.110.2.1):
      IGMP is enabled   
      Current IGMP version is 2   
      IGMP state: up
      IGMP group policy: none
      IGMP limit: -
      Value of query interval for IGMP (negotiated): -
      Value of query interval for IGMP(in seconds): 60 s
      Value of other querier timeout for IGMP(in seconds): 0 s
      Value of maximum query response time for IGMP(in seconds): 10 s
      Querier for IGMP: 10.110.2.1 (this router)
      Total 1 IGMP Group reported
   ```
   
   The command output shows that Device B is a querier. This is because GE 0/1/0 of Device B has the lowest IP address among the interfaces connected to the user network segment.
   
   # Run the [**display pim routing-table**](cmdqueryname=display+pim+routing-table) command on Device A to check whether GE 0/1/0 has joined IGMP group 225.1.1.1. The command output shows that the (\*, 225.1.1.1) entry is generated, the downstream interface is GE 0/1/0, and the protocol type is **static**. The information indicates that GE 0/1/0 has joined IGMP group 225.1.1.1.
   
   ```
   <DeviceA> display pim routing-table
   ```
   ```
   VPN-Instance: public net
    Total 1 (*, G) entry; 0 (S, G) entry
    (*, 225.1.1.1)
        RP: 192.168.4.1
        Protocol: pim-sm, Flag: WC
        UpTime: 00:12:17
        Upstream interface: GigabitEthernet0/2/0, Refresh time: 00:12:17
            Upstream neighbor: 192.168.1.2
            RPF prime neighbor: 192.168.1.2
        Downstream interface(s) information:
        Total number of downstreams: 1
            1: GigabitEthernet0/1/0
                Protocol: static, UpTime: 00:12:17, Expires: -
   ```

#### Configuration Files

* Device A configuration file
  
  ```
  #
  sysname DeviceA
  #
  multicast routing-enable
  #
  isis 1
   network-entity 10.0000.0000.0001.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.110.1.1 255.255.255.0
   pim sm
   igmp enable
   igmp static-group 225.1.1.1
   isis enable 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 192.168.1.1 255.255.255.0
   pim sm
   isis enable 1
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
  isis 1
   network-entity 10.0000.0000.0002.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.110.2.1 255.255.255.0
   pim sm
   igmp enable
   isis enable 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 192.168.2.1 255.255.255.0
   pim sm
   isis enable 1
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
  isis 1
   network-entity 10.0000.0000.0003.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.110.2.2 255.255.255.0
   pim sm
   igmp enable
   isis enable 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 192.168.3.1 255.255.255.0
   pim sm
   isis enable 1
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
  isis 1
   network-entity 10.0000.0000.0004.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 192.168.4.1 255.255.255.0
   pim sm
   isis enable 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 192.168.1.2 255.255.255.0
   pim sm
   isis enable 1
  #
  interface GigabitEthernet0/2/2
   undo shutdown
   ip address 192.168.2.2 255.255.255.0
   pim sm
   isis enable 1
  #
  interface GigabitEthernet0/2/3
   undo shutdown
   ip address 192.168.3.2 255.255.255.0
   pim sm
   isis enable 1
  #
  pim
   c-bsr GigabitEthernet0/1/0
   c-rp GigabitEthernet0/1/0
  #
  return
  ```