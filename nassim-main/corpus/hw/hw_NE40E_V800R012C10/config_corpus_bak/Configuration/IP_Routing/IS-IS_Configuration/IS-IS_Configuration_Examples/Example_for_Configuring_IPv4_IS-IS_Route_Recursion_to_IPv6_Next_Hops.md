Example for Configuring IPv4 IS-IS Route Recursion to IPv6 Next Hops
====================================================================

This section describes how to configure IS-IS route recursion to IPv6 next hops.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0000001307923501__fig_dc_vrp_isis_cfg_008401):

* Device A and Device B belong to the same AS, and an IS-IS neighbor relationship is established between the two devices.

**Figure 1** Networking diagram for configuring IS-IS route recursion to IPv6 next hops  
![](figure/en-us_image_0000001308163409.png)

| Device Name | Interface | IP Address |
| --- | --- | --- |
| DeviceA | GE0/1/0 | 2001:DB8:1::1/64 |
| DeviceB | Loopback0 | 2.2.2.2/32 |
| GE0/1/0 | 2001:DB8:1::2/64 |



#### Precautions

To improve security, you are advised to configure IS-IS authentication. For details, see "Configuring IS-IS Authentication." IS-IS interface authentication is used as an example. For details, see Example for Configuring Basic IS-IS Functions.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable IS-IS and specify NETs on Device A and Device B.
2. Configure IS-IS route recursion to IPv6 next hops on Device A, and then check the routing information.

#### Data Preparation

To complete the configuration, you need the following data:

* Area addresses of Device A and Device B

#### Procedure

1. Configure basic IS-IS functions.
   
   
   
   # Configure Device A.
   
   ```
   [~DeviceA] isis 1
   ```
   ```
   [*DeviceA-isis-1] network-entity 10.0000.0000.0001.00
   ```
   ```
   [*DeviceA-isis-1] ipv6 enable topology standard
   ```
   ```
   [*DeviceA-isis-1] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] ipv6 enable
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] ipv6 address 2001:DB8:1::1 64
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] isis enable 1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] isis ipv6 enable 1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] quit
   ```
   
   # Configure Device B.
   
   ```
   [~DeviceB] isis 1
   ```
   ```
   [*DeviceB-isis-1] network-entity 10.0000.0000.0002.00
   ```
   ```
   [*DeviceB-isis-1] quit
   ```
   ```
   [*DeviceB] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] ipv6 enable
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] ipv6 address 2001:DB8:1::2 64
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] isis enable 1
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] isis ipv6 enable 1
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceB] interface Loopback 0
   ```
   ```
   [*DeviceB-LoopBack0] isis enable 1
   ```
   ```
   [*DeviceB-LoopBack0] quit
   ```
   ```
   [*DeviceB] commit
   ```
2. Configure IS-IS route recursion to IPv6 next hops.
   
   
   
   # Configure Device A.
   
   ```
   [~DeviceA] isis 1
   [*DeviceA-isis-1] ipv4-prefix ipv6-nexthop enable
   [*DeviceA-isis-1] commit
   [~DeviceA-isis-1] quit
   ```
3. Check routing information.
   
   
   
   # Check the routing table of Device A. The command output shows that the IS-IS route recurses to an IPv6 next hop.
   
   ```
   [~DeviceA] display isis route ipv4
   
                            Route information for ISIS(1)
                            -----------------------------
   
                           ISIS(1) Level-1 Forwarding Table
                           --------------------------------
   
   IPV4 Destination   IntCost    ExtCost ExitInterface     NextHop         Flags
   -------------------------------------------------------------------------------
   2.2.2.2/32         10         NULL    GigabitEthernet0/1/0          FE80::3A05:28FF:FE21:300 A/-/L/-
        Flags: D-Direct, A-Added to URT, L-Advertised in LSPs, S-IGP Shortcut,
               U-Up/Down Bit Set, LP-Local Prefix-Sid
        Protect Type: L-Link Protect, N-Node Protect
   
   
                           ISIS(1) Level-2 Forwarding Table
                           --------------------------------
   
   IPV4 Destination   IntCost    ExtCost ExitInterface     NextHop         Flags
   -------------------------------------------------------------------------------
   2.2.2.2/32         10         NULL    -                 -               -/-/-/-
        Flags: D-Direct, A-Added to URT, L-Advertised in LSPs, S-IGP Shortcut,
               U-Up/Down Bit Set, LP-Local Prefix-Sid
        Protect Type: L-Link Protect, N-Node Protect
   ```

#### Configuration Files

* Device A configuration file
  
  ```
  #
  sysname DeviceA
  #
  isis 1
   network-entity 10.0000.0000.0001.00
   ipv4-prefix ipv6-nexthop enable
   #
   ipv6 enable topology standard
   #
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:1::1/64
   isis enable 1
   isis ipv6 enable 1
  #
  return
  ```
* Device B configuration file
  
  ```
  #
  sysname DeviceB
  #
  isis 1
   network-entity 10.0000.0000.0002.00
   #
   ipv6 enable topology standard
   #
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:1::2/64
   isis enable 1
   isis ipv6 enable 1
  #
  interface LoopBack0
   ip address 2.2.2.2 255.255.255.255
   isis enable 1
  #
  return
  ```