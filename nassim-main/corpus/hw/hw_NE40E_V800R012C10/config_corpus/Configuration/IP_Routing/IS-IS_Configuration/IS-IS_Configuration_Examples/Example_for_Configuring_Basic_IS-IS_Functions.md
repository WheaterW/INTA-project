Example for Configuring Basic IS-IS Functions
=============================================

This section describes how to configure basic IS-IS functions, including specifying the NET, configuring the IS-IS level, and enabling IS-IS on each device.

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0172366085__fig_dc_vrp_isis_cfg_007901):

* Device A, Device B, Device C, and Device D run IS-IS for IP interworking.
* Device A, Device B, and Device C belong to Area 10, and Device D belongs to Area 20.
* Device A and Device B are Level-1 devices; Device C is a Level-1-2 device; Device D is a Level-2 device.

**Figure 1** Configuring basic IS-IS functions  
![](images/fig_dc_vrp_isis_cfg_007901.png)

| Device Name | Interface | IP Address |
| --- | --- | --- |
| Device A | GE0/1/0 | 10.1.1.2/24 |
| Device B | GE0/1/0 | 10.1.2.2/24 |
| Device C | GE0/1/0 | 10.1.1.1/24 |
| GE0/2/0 | 10.1.2.1/24 |
| GE0/3/0 | 192.168.0.1/24 |
| Device D | GE0/1/0 | 192.168.0.2/24 |
| GE0/2/0 | 172.16.1.1/16 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable IS-IS, configure the level, and specify the NET on each Router.
2. Configure Device A and Device C to authenticate Hello packets in a specified mode and with the specified password.
3. View the IS-IS LSDB and the routing table of each Router.

#### Data Preparation

To complete the configuration, you need the following data:

* Area addresses of Device A, Device B, Device C, and Device D
* Levels of Device A, Device B, Device C, and Device D

#### Procedure

1. Configure an IP address for each interface. 
   
   
   
   Configure an IP address for each [Figure 1](#EN-US_TASK_0172366085__fig_dc_vrp_isis_cfg_007901) interface. For detailed configurations, see Configuration Files.
2. Configure basic IS-IS functions.
   
   
   
   # Configure Device A.
   
   ```
   [~DeviceA] isis 1
   ```
   ```
   [*DeviceA-isis-1] is-level level-1
   ```
   ```
   [*DeviceA-isis-1] network-entity 10.0000.0000.0001.00
   ```
   ```
   [*DeviceA-isis-1] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] isis enable 1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] isis circuit-type p2p
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
   [*DeviceB-isis-1] is-level level-1
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
   [*DeviceB-GigabitEthernet0/1/0] isis enable 1
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] isis circuit-type p2p
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] quit
   ```
   
   # Configure Device C.
   
   ```
   [~DeviceC] isis 1
   ```
   ```
   [*DeviceC-isis-1] is-level level-1-2
   ```
   ```
   [*DeviceC-isis-1] network-entity 10.0000.0000.0003.00
   ```
   ```
   [*DeviceC-isis-1] quit
   ```
   ```
   [*DeviceC] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] isis enable 1
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] isis circuit-type p2p
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceC] interface gigabitethernet 0/2/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] isis enable 1
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] isis circuit-type p2p
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceC] interface gigabitethernet 0/3/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/3/0] isis enable 1
   ```
   ```
   [*DeviceC-GigabitEthernet0/3/0] isis circuit-type p2p
   ```
   ```
   [*DeviceC-GigabitEthernet0/3/0] commit
   ```
   ```
   [~DeviceC-GigabitEthernet0/3/0] quit
   ```
   
   # Configure Device D.
   
   ```
   [~DeviceD] isis 1
   ```
   ```
   [*DeviceD-isis-1] is-level level-2
   ```
   ```
   [*DeviceD-isis-1] network-entity 20.0000.0000.0004.00
   ```
   ```
   [*DeviceD-isis-1] quit
   ```
   ```
   [*DeviceD] interface gigabitethernet 0/2/0
   ```
   ```
   [*DeviceD-GigabitEthernet0/2/0] isis enable 1
   ```
   ```
   [*DeviceD-GigabitEthernet0/2/0] isis circuit-type p2p
   ```
   ```
   [*DeviceD-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceD] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] isis enable 1
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] isis circuit-type p2p
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceD-GigabitEthernet0/1/0] quit
   ```
3. Configure the authentication mode and password used by Device A and Device C to authenticate Hello packets.
   
   
   
   # Configure Device A.
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] isis authentication-mode hmac-sha256 key-id 1 cipher YsHsjx_202206
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] quit
   ```
   
   # Configure Device C.
   
   ```
   [~DeviceC] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceC-GigabitEthernet0/1/0] isis authentication-mode hmac-sha256 key-id 1 cipher YsHsjx_202206
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceC-GigabitEthernet0/1/0] quit
   ```
4. Verify the configuration.
   
   
   
   # Display the IS-IS LSDB of each Router.
   
   ```
   [~DeviceA] display isis lsdb
   ```
   ```
   Database information for ISIS(1)
   --------------------------------
                             Level-1 Link State Database
   LSPID                 Seq Num      Checksum      HoldTime      Length  ATT/P/OL
   -------------------------------------------------------------------------------
   0000.0000.0001.00-00* 0x00000006   0xbf7d        649           68      0/0/0
   0000.0000.0002.00-00  0x00000003   0xef4d        545           68      0/0/0
   0000.0000.0003.00-00  0x00000008   0x3340        582           111     0/1/0
   Total LSP(s): 3 
   *(In TLV)-Leaking Route, *(By LSPID)-Self LSP, +-Self LSP(Extended),
              ATT-Attached, P-Partition, OL-Overload 
   ```
   ```
   [~DeviceB] display isis lsdb
   ```
   ```
                           Database information for ISIS(1)
                           --------------------------------
                             Level-1 Link State Database
   LSPID                 Seq Num      Checksum      HoldTime      Length  ATT/P/OL
   -------------------------------------------------------------------------------
   0000.0000.0001.00-00  0x00000006   0xbf7d        642           68      0/0/0
   0000.0000.0002.00-00* 0x00000003   0xef4d        538           68      0/0/0
   0000.0000.0003.00-00  0x00000008   0x3340        574           111     0/1/0
   Total LSP(s): 3 
   *(In TLV)-Leaking Route, *(By LSPID)-Self LSP, +-Self LSP(Extended),
              ATT-Attached, P-Partition, OL-Overload
   ```
   ```
   [~DeviceC] display isis lsdb
   ```
   ```
                           Database information for ISIS(1)
                           --------------------------------
                             Level-1 Link State Database
   LSPID                 Seq Num      Checksum      HoldTime      Length  ATT/P/OL
   -------------------------------------------------------------------------------
   0000.0000.0001.00-00  0x00000006   0xbf7d        638           68      0/0/0
   0000.0000.0002.00-00  0x00000003   0xef4d        533           68      0/0/0
   0000.0000.0003.00-00* 0x00000008   0x3340        569           111     0/1/0
   Total LSP(s): 3 
   *(In TLV)-Leaking Route, *(By LSPID)-Self LSP, +-Self LSP(Extended),
              ATT-Attached, P-Partition, OL-Overload
                             Level-2 Link State Database
   LSPID                 Seq Num      Checksum      HoldTime      Length  ATT/P/OL
   -------------------------------------------------------------------------------
   0000.0000.0003.00-00* 0x00000008   0x55bb        650           100     0/0/0
   0000.0000.0004.00-00  0x00000005   0x651         629           84      0/0/0
   Total LSP(s): 2 
   *(In TLV)-Leaking Route, *(By LSPID)-Self LSP, +-Self LSP(Extended),
              ATT-Attached, P-Partition, OL-Overload 
   ```
   ```
   [~DeviceD] display isis lsdb
   ```
   ```
                           Database information for ISIS(1)
                           --------------------------------
                             Level-2 Link State Database
   LSPID                 Seq Num      Checksum      HoldTime      Length  ATT/P/OL
   -------------------------------------------------------------------------------
   0000.0000.0003.00-00  0x00000008   0x55bb        644           100     0/0/0
   0000.0000.0004.00-00* 0x00000005   0x651         624           84      0/0/0
   Total LSP(s): 2 
   *(In TLV)-Leaking Route, *(By LSPID)-Self LSP, +-Self LSP(Extended),
              ATT-Attached, P-Partition, OL-Overload
   ```
   
   # Display the IS-IS routing table of each Router. In the routing table of a Level-1 device, there must be a default route with a Level-1-2 device as the next hop. A Level-2 device must have all Level-1 and Level-2 routes.
   
   ```
   [~DeviceA] display isis route
   ```
   ```
                            Route information for ISIS(1)
                            -----------------------------
   
                           ISIS(1) Level-1 Forwarding Table
                           --------------------------------
    IPV4 Destination   IntCost   ExtCost ExitInterface   NextHop         Flags
   -----------------------------------------------------------------------------
    10.1.1.0/24        10        NULL    GE0/1/0         Direct          D/-/L/-
    10.1.2.0/24        20        NULL    GE0/1/0         10.1.1.1        A/-/-/-
    192.168.0.0/24     20        NULL    GE0/1/0         10.1.1.1        A/-/-/-
    0.0.0.0/0          10        NULL    GE0/1/0         10.1.1.1        A/-/-/-
       Flags: D-Direct, A-Added to URT, L-Advertised in LSPs, S-IGP Shortcut,
                                    U-Up/Down Bit Set, LP-Local Prefix-Sid
       Protect Type: L-Link Protect, N-Node Protect
   ```
   ```
   [~DeviceC] display isis route
   ```
   ```
                            Route information for ISIS(1)
                            -----------------------------
   
                           ISIS(1) Level-1 Forwarding Table
                           --------------------------------
    IPV4 Destination   IntCost   ExtCost ExitInterface   NextHop         Flags
   -----------------------------------------------------------------------------
    10.1.1.0/24        10        NULL    GE0/1/0         Direct          D/-/L/-
    10.1.2.0/24        10        NULL    GE0/2/0         Direct          D/-/L/-
    192.168.0.0/24     10        NULL    GE0/3/0         Direct          D/-/L/-
       Flags: D-Direct, A-Added to URT, L-Advertised in LSPs, S-IGP Shortcut,
                                    U-Up/Down Bit Set, LP-Local Prefix-Sid
       Protect Type: L-Link Protect, N-Node Protect
   
                           ISIS(1) Level-2 Forwarding Table
                           --------------------------------
    IPV4 Destination   IntCost   ExtCost ExitInterface   NextHop         Flags
   -----------------------------------------------------------------------------
    10.1.1.0/24        10        NULL    GE0/1/0         Direct          D/-/L/-
    10.1.2.0/24        10        NULL    GE0/2/0         Direct          D/-/L/-
    192.168.0.0/24     10        NULL    GE0/3/0         Direct          D/-/L/-
    172.16.0.0/16      20        NULL    GE0/3/0         192.168.0.2     A/-/-/-
       Flags: D-Direct, A-Added to URT, L-Advertised in LSPs, S-IGP Shortcut,
                                    U-Up/Down Bit Set, LP-Local Prefix-Sid
       Protect Type: L-Link Protect, N-Node Protect
   ```
   ```
   [~DeviceD] display isis route
   ```
   ```
                            Route information for ISIS(1)
                            -----------------------------
   
                           ISIS(1) Level-2 Forwarding Table
                           --------------------------------
    IPV4 Destination   IntCost   ExtCost ExitInterface   NextHop          Flags
   ------------------------------------------------------------------------------
    192.168.0.0/24     10        NULL    GE0/3/0         Direct           D/-/L/-
    10.1.1.0/24        20        NULL    GE0/3/0         192.168.0.1      A/-/-/-
    10.1.2.0/24        20        NULL    GE0/3/0         192.168.0.1      A/-/-/-
    172.16.0.0/16      10        NULL    GE0/2/0         Direct           D/-/L/-
       Flags: D-Direct, A-Added to URT, L-Advertised in LSPs, S-IGP Shortcut,
                                    U-Up/Down Bit Set, LP-Local Prefix-Sid
       Protect Type: L-Link Protect, N-Node Protect
   ```

#### Configuration Files

* Device A configuration file
  
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
  isis 1
  ```
  ```
   is-level level-1
  ```
  ```
   network-entity 10.0000.0000.0001.00
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
   ip address 10.1.1.2 255.255.255.0
  ```
  ```
   isis enable 1
  ```
  ```
   isis circuit-type p2p
  ```
  ```
   isis authentication-mode hmac-sha256 key-id 1 cipher %^%#c;\wJ4Qi8I1FMGM}KmIK9rha/.D.!$"~0(Ep66z~%^%#
  ```
  ```
  #
  ```
  ```
  return
  ```
* Device B configuration file
  
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
  isis 1
  ```
  ```
   is-level level-1
  ```
  ```
  network-entity 10.0000.0000.0002.00
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
   ip address 10.1.2.2 255.255.255.0
  ```
  ```
   isis enable 1
  ```
  ```
   isis circuit-type p2p
  ```
  ```
  #
  ```
  ```
  return
  ```
* Device C configuration file
  
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
  isis 1
  ```
  ```
   is-level level-1-2
  ```
  ```
   network-entity 10.0000.0000.0003.00
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
  ip address 10.1.1.1 255.255.255.0
  ```
  ```
   isis enable 1
  ```
  ```
   isis circuit-type p2p
  ```
  ```
   isis authentication-mode hmac-sha256 key-id 1 cipher %^%#c;\wJ4Qi8I1FMGM}KmIK9rha/.D.!$"~0(Ep66z~%^%#
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
   ip address 10.1.2.1 255.255.255.0
  ```
  ```
   isis enable 1
  ```
  ```
   isis circuit-type p2p
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
   ip address 192.168.0.1 255.255.255.0
  ```
  ```
   isis enable 1
  ```
  ```
   isis circuit-type p2p
  ```
  ```
  #
  ```
  ```
  return
  ```
* Device D configuration file
  
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
  isis 1
  ```
  ```
   is-level level-2
  ```
  ```
   network-entity 20.0000.0000.0004.00
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
   ip address 192.168.0.2 255.255.255.0
  ```
  ```
   isis enable 1
  ```
  ```
   isis circuit-type p2p
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
   ip address 172.16.1.1 255.255.0.0
  ```
  ```
   isis enable 1
  ```
  ```
   isis circuit-type p2p
  ```
  ```
  #
  ```
  ```
  return
  ```