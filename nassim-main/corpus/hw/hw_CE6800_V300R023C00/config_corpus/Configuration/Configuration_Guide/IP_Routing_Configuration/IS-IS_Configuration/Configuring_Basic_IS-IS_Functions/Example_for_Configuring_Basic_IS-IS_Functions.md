Example for Configuring Basic IS-IS Functions
=============================================

Example for Configuring Basic IS-IS Functions

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001130784136__fig347228173312), DeviceA, DeviceB, DeviceC, and DeviceD run IS-IS to implement IP network connectivity.

* Devices A, B, and C belong to area 10, and DeviceD belongs to area 20.
* DeviceA and DeviceB are Level-1 devices; DeviceC is a Level-1-2 device; DeviceD is a Level-2 device.

**Figure 1** Network diagram of basic IS-IS functions![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001130624394.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IPv4 addresses for interfaces on each routing device.
2. Enable IS-IS, configure a level, and set a NET for each routing device.
3. Configure the authentication mode and password for DeviceA and DeviceC to authenticate Hello packets.

#### Procedure

1. Configure IPv4 addresses for interfaces on each routing device.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ip address 10.1.1.2 255.255.255.0
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB, DeviceC, and DeviceD are similar to the configuration of DeviceA. For detailed configurations, see configuration scripts.
2. Enable IS-IS, configure a level, and set a NET for each routing device.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] isis 1
   [*DeviceA-isis-1] is-level level-1
   [*DeviceA-isis-1] network-entity 10.0000.0000.0001.00
   [*DeviceA-isis-1] quit
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] isis enable 1
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] isis 1
   [*DeviceB-isis-1] is-level level-1
   [*DeviceB-isis-1] network-entity 10.0000.0000.0002.00
   [*DeviceB-isis-1] quit
   [*DeviceB] interface 100ge 1/0/1
   [*DeviceB-100GE1/0/1] isis enable 1
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] isis 1
   [*DeviceC-isis-1] is-level level-1-2
   [*DeviceC-isis-1] network-entity 10.0000.0000.0003.00
   [*DeviceC-isis-1] quit
   [*DeviceC] interface 100ge 1/0/1
   [*DeviceC-100GE1/0/1] isis enable 1
   [*DeviceC-100GE1/0/1] quit
   [*DeviceC] interface 100ge 1/0/2
   [*DeviceC-100GE1/0/2] isis enable 1
   [*DeviceC-100GE1/0/2] quit
   [*DeviceC] interface 100ge 1/0/3
   [*DeviceC-100GE1/0/3] isis enable 1
   [*DeviceC-100GE1/0/3] quit
   [*DeviceC] commit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] isis 1
   [*DeviceD-isis-1] is-level level-2
   [*DeviceD-isis-1] network-entity 20.0000.0000.0004.00
   [*DeviceD-isis-1] quit
   [*DeviceD] interface 100ge 1/0/2
   [*DeviceD-100GE1/0/2] isis enable 1
   [*DeviceD-100GE1/0/2] quit
   [*DeviceD] interface 100ge 1/0/1
   [*DeviceD-100GE1/0/1] isis enable 1
   [*DeviceD-100GE1/0/1] quit
   [*DeviceD] commit
   ```
3. Configure the authentication mode and password for DeviceA and DeviceC to authenticate Hello packets.
   
   
   
   # Configure DeviceA.
   
   ```
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] isis authentication-mode hmac-sha256 key-id 1 cipher YsHsjx_202206
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [*DeviceC] interface 100ge 1/0/1
   [*DeviceC-100GE1/0/1] isis authentication-mode hmac-sha256 key-id 1 cipher YsHsjx_202206
   [*DeviceC-100GE1/0/1] quit
   [*DeviceC] commit
   ```

#### Verifying the Configuration

# Check IS-IS routing information on DeviceA.

```
[~DeviceA] display isis route

Route Information for ISIS(1)
--------------------------------------------------------------------------------

Flags: D-Direct, A-Added to URT, L-Advertised in LSPs, S-IGP Shortcut,
                        U-Up/Down Bit Set

ISIS(1) Level-1 Forwarding Table
--------------------------------------------------------------------------------

IPV4 Destination      IntCost    ExtCost ExitInterface     NextHop         Flags
--------------------------------------------------------------------------------
0.0.0.0/0                  10       NULL  100GE1/0/1           10.1.1.1        A/-/-/-
10.1.1.0/24                10       NULL  100GE1/0/1           Direct          D/-/L/-
10.1.2.0/24                20       NULL  100GE1/0/1           10.1.1.  1      A/-/-/-
192.168.0.0/24             20       NULL  100GE1/0/1           10.1.1.1        A/-/-/-
```

DeviceA has a route to the network segment 10.1.2.0/24 of DeviceB and a default route. The next hop of the default route is DeviceC.

![](public_sys-resources/note_3.0-en-us.png) 

DeviceC is a Level-1-2 device and can reach more areas through area 20 than through area 10. In this case, DeviceC sets the ATT bit to 1 in the Level-1 LSP to be advertised in area 10. After receiving this Level-1 LSP, DeviceA generates a default route, with DeviceC as the next hop.

# Check IS-IS routing information on DeviceC.

```
[~DeviceC] display isis route

Route Information for ISIS(1)
--------------------------------------------------------------------------------

Flags: D-Direct, A-Added to URT, L-Advertised in LSPs, S-IGP Shortcut,
                     U-Up/Down Bit Set

ISIS(1) Level-1 Forwarding Table
--------------------------------------------------------------------------------

IPV4 Destination      IntCost    ExtCost ExitInterface     NextHop         Flags
--------------------------------------------------------------------------------
10.1.1.0/24                10       NULL 100GE1/0/1           Direct          D/-/L/-
10.1.2.0/24                10       NULL 100GE1/0/2           Direct          D/-/L/-
192.168.0.0/24             10       NULL 100GE1/0/3           Direct          D/-/L/-


ISIS(1) Level-2 Forwarding Table
--------------------------------------------------------------------------------

IPV4 Destination      IntCost    ExtCost ExitInterface     NextHop         Flags
--------------------------------------------------------------------------------
10.1.1.0/24                10       NULL  100GE1/0/1           Direct          D/-/L/-
10.1.2.0/24                10       NULL  100GE1/0/2           Direct          D/-/L/-
172.16.0.0/16              20       NULL  100GE1/0/3           192.168.0.2     A/-/-/-
192.168.0.0/24             10       NULL  100GE1/0/3          Direct          D/-/L/-

```

DeviceC has a route to the network segment 172.16.0.0/16.

# Check IS-IS routing information on DeviceD.

```
[~DeviceD] display isis route

Route Information for ISIS(1)
--------------------------------------------------------------------------------

Flags: D-Direct, A-Added to URT, L-Advertised in LSPs, S-IGP Shortcut,
                    U-Up/Down Bit Set

ISIS(1) Level-2 Forwarding Table
--------------------------------------------------------------------------------

IPV4 Destination      IntCost    ExtCost ExitInterface     NextHop         Flags
--------------------------------------------------------------------------------
10.1.1.0/24               20        NULL  100GE1/0/3           192.168.0.1     A/-/-/-
10.1.2.0/24               20        NULL  100GE1/0/3           192.168.0.1     A/-/-/-
172.16.0.0/16              10       NULL  100GE1/0/2           Direct          D/-/L/-
192.168.0.0/24             10       NULL  100GE1/0/3           Direct          D/-/L/-

```

DeviceD has routes to network segments 10.1.1.0/24 and 10.1.2.0/24.


#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  isis 1
   is-level level-1
   network-entity 10.0000.0000.0001.00
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.2 255.255.255.0
   isis enable 1
   isis authentication-mode hmac-sha256 key-id 1 cipher %^%#c;\wJ4Qi8I1FMGM}KmIK9rha/.D.!$"~0(Ep66z~%^%#
  #  
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  isis 1
   is-level level-1
   network-entity 10.0000.0000.0002.00
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.2.2 255.255.255.0
   isis enable 1
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  isis 1
   is-level level-1-2
   network-entity 10.0000.0000.0003.00
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.1 255.255.255.0
   isis enable 1
   isis authentication-mode hmac-sha256 key-id 1 cipher %^%#c;\wJ4Qi8I1FMGM}KmIK9rha/.D.!$"~0(Ep66z~%^%#
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.2.1 255.255.255.0
   isis enable 1
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 192.168.0.1 255.255.255.0
   isis enable 1
  #
  return
  ```
* DeviceD
  
  ```
  #
  sysname DeviceD
  #
  isis 1
   is-level level-2
   network-entity 20.0000.0000.0004.00
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.0.2 255.255.255.0
   isis enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 172.16.1.1 255.255.0.0
   isis enable 1
  #
  return
  ```