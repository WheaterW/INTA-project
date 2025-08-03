Example for Configuring IS-IS DIS Election
==========================================

Example for Configuring IS-IS DIS Election

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001405986073__fig_dc_cfg_isisv4_004901), four devices on the broadcast network communicate using IS-IS. DeviceA and DeviceB are Level-1-2 devices, DeviceC is a Level-1 device, and DeviceD is a Level-2 device. DeviceA with high performance needs to be elected as a Level-2 DIS.

**Figure 1** Configuring IS-IS DIS election![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 represents 100GE1/0/1.


  
![](figure/en-us_image_0000001355947870.png)

#### Precautions

To improve security, you are advised to configure IS-IS authentication. For details, see Configuring IS-IS Authentication. IS-IS interface authentication is used as an example. For details, see Example for Configuring Basic IS-IS Functions.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IS-IS to implement network interworking.
2. Set the DIS priority of DeviceA to 100 so that DeviceA can be elected as a Level-2 DIS.

#### Procedure

1. Configure IPv4 addresses for interfaces on each routing device.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ip address 10.1.1.1 24
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB, DeviceC, and DeviceD are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
2. Check the MAC address of each GE interface on each router.
   
   
   
   # Check the MAC address of 100GE1/0/1 on DeviceA.
   
   ```
   [~DeviceA] display arp interface 100ge 1/0/1
   IP ADDRESS      MAC ADDRESS  EXPIRE(M) TYPE        INTERFACE      VPN-INSTANCE
                                          VLAN/CEVLAN PVC
   -------------------------------------------------------------------------
   10.1.1.1        00e0-fc10-afec         I -         100GE1/0/1
   -------------------------------------------------------------------------
   Total:1        Dynamic:0       Static:0    Interface:1  
   ```
   
   # Check the MAC address of 100GE1/0/1 on DeviceB.
   
   ```
   [~DeviceA] display arp interface 100ge 1/0/1
   IP ADDRESS      MAC ADDRESS  EXPIRE(M) TYPE        INTERFACE      VPN-INSTANCE
                                          VLAN/CEVLAN PVC
   -------------------------------------------------------------------------
   10.1.1.2        00e0-fccd-acdf         I -         100GE1/0/1
   -------------------------------------------------------------------------
   Total:1        Dynamic:0       Static:0    Interface:1  
   ```
   
   # Check the MAC address of 100GE1/0/1 on DeviceC.
   
   ```
   [~DeviceA] display arp interface 100ge 1/0/1
   IP ADDRESS      MAC ADDRESS  EXPIRE(M) TYPE        INTERFACE      VPN-INSTANCE
                                          VLAN/CEVLAN PVC
   -------------------------------------------------------------------------
   10.1.1.3        00e0-fc50-25fe        I -         100GE1/0/1
   -------------------------------------------------------------------------
   Total:1        Dynamic:0       Static:0    Interface:1  
   ```
   
   # Check the MAC address of 100GE1/0/1 on DeviceD.
   
   ```
   [~DeviceA] display arp interface 100ge 1/0/1
   IP ADDRESS      MAC ADDRESS  EXPIRE(M) TYPE        INTERFACE      VPN-INSTANCE
                                          VLAN/CEVLAN PVC
   -------------------------------------------------------------------------
   10.1.1.4        00e0-fcfd-305c         I -         100GE1/0/1
   -------------------------------------------------------------------------
   Total:1        Dynamic:0       Static:0    Interface:1  
   ```
3. Enable IS-IS, configure a level, and set a NET for each device.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] isis 1
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
   [*DeviceC-isis-1] is-level level-1
   [*DeviceC-isis-1] network-entity 10.0000.0000.0003.00
   [*DeviceC-isis-1] quit
   [*DeviceC] interface 100ge 1/0/1
   [*DeviceC-100GE1/0/1] isis enable 1
   [*DeviceC-100GE1/0/1] quit
   [*DeviceC] commit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] isis 1
   [*DeviceD-isis-1] is-level level-2
   [*DeviceD-isis-1] network-entity 10.0000.0000.0004.00
   [*DeviceD-isis-1] quit
   [*DeviceD] interface 100ge 1/0/1
   [*DeviceD-100GE1/0/1] isis enable 1
   [*DeviceD-100GE1/0/1] quit
   [*DeviceD] commit
   ```
   
   # Check information about IS-IS neighbors on DeviceA.
   
   ```
   [~DeviceA] display isis peer
   Peer information for ISIS(1)
   --------------------------------------------------------------------------------
   System Id      Interface         Circuit Id        State  HoldTime Type     PRI
   --------------------------------------------------------------------------------
   0000.0000.0002 100GE1/0/1           0000.0000.0002.01  Up    9s       L1(L1L2) 64
   0000.0000.0003 100GE1/0/1           0000.0000.0002.01  Up    27s      L1       64
   0000.0000.0002 100GE1/0/1           0000.0000.0004.01  Up    28s      L2(L1L2) 64
   0000.0000.0004 100GE1/0/1           0000.0000.0004.01  Up    8s       L2       64
   
   Total Peer(s): 4
   ```
   
   # Check information about IS-IS interfaces on DeviceA.
   
   ```
   [~DeviceA] display isis interface
   Interface information for ISIS(1)
   ---------------------------------------------------------------------------
    Interface       Id      IPV4.State          IPV6.State      MTU  Type  DIS
    100GE1/0/1         001         Up                 Down         1497 L1/L2 No/No
   ```
   
   # Check information about IS-IS interfaces on DeviceB.
   
   ```
   [~DeviceB] display isis interface
   Interface information for ISIS(1)
   ---------------------------------------------------------------------------
    Interface       Id      IPV4.State          IPV6.State      MTU  Type  DIS
    100GE1/0/1         001         Up                 Down         1497 L1/L2 No/No
   ```
   
   # Check information about IS-IS interfaces on DeviceD.
   
   ```
   [~DeviceD] display isis interface
   Interface information for ISIS(1)
   ---------------------------------------------------------------------------
    Interface       Id      IPV4.State          IPV6.State      MTU  Type  DIS
    100GE1/0/1         001         Up                 Down         1497 L2 No/Yes
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   As shown in the interface information, when the default DIS priority is used, the MAC address of the interface on DeviceB is the largest among Level-1 routers. Therefore, DeviceB functions as the Level-1 DIS. Among the Level-2 routers, the MAC address of the interface on DeviceD is the largest. Therefore, DeviceD functions as the Level-2 DIS. Level-1 and Level-2 pseudo nodes are 0000.0000.0002.01 and 0000.0000.0004.01, respectively.
4. Set a DIS priority for DeviceA.
   
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] isis dis-priority 100
   ```
   
   # Check information about the IS-IS neighbors of DeviceA.
   
   ```
   [~DeviceA] display isis peer
   Peer information for ISIS(1)
   -------------------------------------------------------------------------------
   System Id      Interface         Circuit Id        State  HoldTime Type     PRI
   -----------------------------------------------------------------------------
   0000.0000.0002 100GE1/0/1           0000.0000.0001.01  Up    21s      L1(L1L2) 64
   0000.0000.0003 100GE1/0/1           0000.0000.0001.01  Up    27s      L1       64
   0000.0000.0002 100GE1/0/1           0000.0000.0001.01  Up    28s      L2(L1L2) 64
   0000.0000.0004 100GE1/0/1           0000.0000.0001.01  Up    30s      L2       64
   
   Total Peer(s): 4
   ```

#### Verifying the Configuration

# Check information about IS-IS interfaces on DeviceA.

```
[~DeviceA] display isis interface
Interface information for ISIS(1)
------------------------------------------------------------------------------
 Interface       Id      IPV4.State          IPV6.State      MTU  Type  DIS
 100GE1/0/1       001         Up                 Down         1497 L1/L2 Yes/Yes
```
![](public_sys-resources/note_3.0-en-us.png) 

The preceding information shows that DeviceA becomes a Level-1-2 DIS immediately after the DIS priority of the IS-IS interface is changed and that the pseudonode is 0000.0000.0001.01.

# Check information about IS-IS neighbors and interfaces on DeviceB.

```
[~DeviceB] display isis peer
Peer information for ISIS(1)
-------------------------------------------------------------------------------
  System Id    Interface          Circuit Id       State  HoldTime Type     PRI
-------------------------------------------------------------------------------
0000.0000.0001 100GE1/0/1          0000.0000.0001.01 Up    7s       L1(L1L2) 100
0000.0000.0003 100GE1/0/1          0000.0000.0001.01 Up    25s      L1       64
0000.0000.0001 100GE1/0/1          0000.0000.0001.01 Up    7s       L2(L1L2) 100
0000.0000.0004 100GE1/0/1          0000.0000.0001.01 Up    25s      L2       64

Total Peer(s): 4

 [~RouterB] display isis interface
Interface information for ISIS(1)
----------------------------------------------------------------------------
 Interface       Id      IPV4.State          IPV6.State      MTU  Type  DIS
 100GE1/0/1       001         Up                 Down         1497 L1/L2 No/No

```

# Check information about IS-IS neighbors and interfaces on DeviceD.

```
[~DeviceD] display isis peer
Peer information for ISIS(1)
-------------------------------------------------------------------------------
System Id      Interface          Circuit Id       State  HoldTime Type     PRI
-------------------------------------------------------------------------------
0000.0000.0001 100GE1/0/1          0000.0000.0001.01 Up    9s       L2       100
0000.0000.0002 100GE1/0/1          0000.0000.0001.01 Up    28s      L2       64

Total Peer(s): 2

[~RouterD] display isis interface
Interface information for ISIS(1)
---------------------------------------------------------------------------
 Interface       Id      IPV4.State          IPV6.State      MTU  Type  DIS
 100GE1/0/1       001         Up                 Down         1497 L1/L2 No/No

```

#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  isis 1
   network-entity 10.0000.0000.0001.00
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.1 255.255.255.0
   isis enable 1
   isis dis-priority 100
  #  
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  isis 1
   network-entity 10.0000.0000.0002.00
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.2 255.255.255.0
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
   is-level level-1
   network-entity 10.0000.0000.0003.00
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.3 255.255.255.0
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
   network-entity 10.0000.0000.0004.00
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.4 255.255.255.0
   isis enable 1
  #
  return
  ```