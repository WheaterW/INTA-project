Example for Configuring IS-IS DIS Election
==========================================

This section describes how to configure the IS-IS DIS election, including configuring basic IS-IS functions and configuring the DIS priority on each device.

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0172366088__fig_dc_vrp_isis_cfg_008201):

* Device A, Device B, Device C, and Device D run IS-IS for IP interworking.
* Device A, Device B, Device C, and Device D belong to area 10, and the network type is broadcast (Ethernet in this case).
* Device A and Device B are Level-1-2 devices; Device C is a Level-1 device; Device D is a Level-2 device.
* The DIS priority of the interface on Device A is 100.
* It is required to change the DIS priority so that Device A functions as a Level-1-2 DIS.

**Figure 1** Configuring IS-IS DIS election  
![](images/fig_dc_vrp_isis_cfg_008201.png)

| Device Name | Interface | IP Address |
| --- | --- | --- |
| Device A | GE0/1/0 | 10.1.1.1/24 |
| Device B | GE0/1/0 | 10.1.1.2/24 |
| Device C | GE0/1/0 | 10.1.1.3/24 |
| Device D | GE0/1/0 | 10.1.1.4/24 |



#### Precautions

To improve security, you are advised to configure IS-IS authentication. For details, see "Configuring IS-IS Authentication." IS-IS interface authentication is used as an example. For details, see Example for Configuring Basic IS-IS Functions.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable IS-IS and specify the NET on each Router for interworking.
2. View information about the IS-IS interface on each Router with the default priority.
3. Configure the DIS priority of the interface on each Router.

#### Data Preparation

To complete the configuration, you need the following data:

* Area addresses of the four Routers
* Levels of the four Routers
* DIS priority of the interface on Device A

#### Procedure

1. Configure an IPv4 address for each interface. For configuration details, see [Configuration Files](#EN-US_TASK_0172366088__section_dc_vrp_isis_cfg_008205) in this section.
2. Display the MAC address of the GE interface on each Router. When the DIS priority of each interface is the same, the Router whose interface has the largest MAC address is elected as the DIS.
   
   
   
   # Display the MAC address of GigabitEthernet 0/1/0 on Device A.
   
   ```
   [~DeviceA] display arp interface gigabitethernet 0/1/0
   ```
   ```
   ARP timeout:1200s
   IP ADDRESS      MAC ADDRESS     EXPIRE(M) TYPE        INTERFACE   VPN-INSTANCE
                                             VLAN/CEVLAN PVC
   ------------------------------------------------------------------------------
   10.1.1.1        00e0-fc10-afec            I -         GE0/1/0
   ------------------------------------------------------------------------------
   Total:1         Dynamic:0       Static:0    Interface:1    Remote:0
   Redirect:0
   ```
   
   # Display the MAC address of GigabitEthernet 0/1/0 on Device B.
   
   ```
   [~DeviceB] display arp interface gigabitethernet 0/1/0
   ```
   ```
   ARP timeout:1200s
   IP ADDRESS      MAC ADDRESS     EXPIRE(M) TYPE        INTERFACE   VPN-INSTANCE
                                             VLAN/CEVLAN PVC
   ------------------------------------------------------------------------------
   10.1.1.2        00e0-fccd-acdf            I -         GE0/1/0
   ------------------------------------------------------------------------------
   Total:1         Dynamic:0       Static:0    Interface:1    Remote:0
   Redirect:0
   ```
   
   # Display the MAC address of GigabitEthernet 0/1/0 on Device C.
   
   ```
   [~DeviceC] display arp interface gigabitethernet 0/1/0
   ```
   ```
   ARP timeout:1200s
   IP ADDRESS      MAC ADDRESS     EXPIRE(M) TYPE        INTERFACE   VPN-INSTANCE
                                             VLAN/CEVLAN PVC
   ------------------------------------------------------------------------------
   10.1.1.3        00e0-fc50-25fe            I -         GE0/1/0
   ------------------------------------------------------------------------------
   Total:1         Dynamic:0       Static:0    Interface:1    Remote:0
   Redirect:0
   ```
   
   # Display the MAC address of GigabitEthernet 0/1/0 on Device D.
   
   ```
   [~DeviceD] display arp interface gigabitethernet 0/1/0
   ```
   ```
   ARP timeout:1200s
   IP ADDRESS      MAC ADDRESS     EXPIRE(M) TYPE        INTERFACE   VPN-INSTANCE
                                             VLAN/CEVLAN PVC
   ------------------------------------------------------------------------------
   10.1.1.4        00e0-fcf0-23ed            I -         GE0/1/0
   ------------------------------------------------------------------------------
   Total:1         Dynamic:0       Static:0    Interface:1    Remote:0
   Redirect:0
   ```
3. Enable IS-IS.
   
   
   
   # Configure Device A.
   
   ```
   [~DeviceA] isis 1
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
   [*DeviceB-GigabitEthernet0/1/0] isis enable 1
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
   [*DeviceC-isis-1] network-entity 10.0000.0000.0003.00
   ```
   ```
   [*DeviceC-isis-1] is-level level-1
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
   [*DeviceC-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceC-GigabitEthernet0/1/0] quit
   ```
   
   # Configure Device D.
   
   ```
   [~DeviceD] isis 1
   ```
   ```
   [*DeviceD-isis-1] network-entity 10.0000.0000.0004.00
   ```
   ```
   [*DeviceD-isis-1] is-level level-2
   ```
   ```
   [*DeviceD-isis-1] quit
   ```
   ```
   [*DeviceD] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] isis enable 1
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceD-GigabitEthernet0/1/0] quit
   ```
   
   # Display information about IS-IS neighbors of Device A.
   
   ```
   [~DeviceA] display isis peer
   ```
   ```
                             Peer information for ISIS(1)
   
     System Id     Interface          Circuit Id        State HoldTime Type     PRI
   --------------------------------------------------------------------------------
   0000.0000.0002  GE0/1/0            0000.0000.0002.01  Up   30s      L1(L1L2) 64 
   0000.0000.0003  GE0/1/0            0000.0000.0002.01  Up   30s      L1       64 
   0000.0000.0002  GE0/1/0            0000.0000.0004.01  Up   30s      L2(L1L2) 64 
   0000.0000.0004  GE0/1/0            0000.0000.0004.01  Up   30s      L2       64 
   
   Total Peer(s): 4
   ```
   
   # Display information about the IS-IS interface on Device A.
   
   ```
   [~DeviceA] display isis interface
   ```
   ```
                          Interface information for ISIS(1)
                          ---------------------------------
    Interface         Id      IPV4.State          IPV6.State      MTU  Type  DIS
    GE0/1/0           001        Up           Mtu:Dn/Lnk:Dn/IP:Dn 1497 L1/L2 No/No
   ```
   
   # Display information about the IS-IS interface on Device B.
   
   ```
   [~DeviceB] display isis interface
   ```
   ```
                          Interface information for ISIS(1)
                          ---------------------------------
    Interface         Id      IPV4.State          IPV6.State      MTU  Type  DIS
    GE0/1/0           001        Up           Mtu:Dn/Lnk:Dn/IP:Dn 1497 L1/L2 Yes/No
   ```
   
   # Display information about the IS-IS interface on Device D.
   
   ```
   [~DeviceD] display isis interface
   ```
   ```
                          Interface information for ISIS(1)
                          ---------------------------------
    Interface         Id      IPV4.State          IPV6.State      MTU  Type  DIS
    GE0/1/0           001        Up           Mtu:Dn/Lnk:Dn/IP:Dn 1497 L1/L2 No/Yes
   ```
   
   As shown in the preceding interface information, when the default DIS priority is used, the interface on Device B has the largest MAC address among the interfaces on Level-1 devices. Therefore, Device B is elected as the Level-1 DIS. The interface on Device D has the largest MAC address among the interfaces on Level-2 devices. Therefore, Device D is elected as the Level-2 DIS. Level-1 and Level-2 pseudo nodes are 0000.0000.0002.01 and 0000.0000.0004.01, respectively.
4. Configure the DIS priority on Device A.
   
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] isis dis-priority 100
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   
   # Display information about IS-IS neighbors of Device A.
   
   ```
   [~DeviceA] display isis peer
   ```
   ```
                             Peer information for ISIS(1)
   
     System Id     Interface          Circuit Id        State HoldTime Type     PRI
   --------------------------------------------------------------------------------
   0000.0000.0002  GE0/1/0            0000.0000.0001.01  Up   27s      L1(L1L2) 64 
   0000.0000.0003  GE0/1/0            0000.0000.0001.01  Up   27s      L1       64 
   0000.0000.0002  GE0/1/0            0000.0000.0001.01  Up   27s      L2(L1L2) 64 
   0000.0000.0004  GE0/1/0            0000.0000.0001.01  Up   27s      L2       64 
   
   Total Peer(s): 4
   ```
5. Verify the configuration.
   
   
   
   # Display information about the IS-IS interface on Device A.
   
   ```
   [~DeviceA] display isis interface
   ```
   ```
                          Interface information for ISIS(1)
                          ---------------------------------
    Interface         Id      IPV4.State          IPV6.State      MTU  Type  DIS
    GE0/1/0           001        Up           Mtu:Dn/Lnk:Dn/IP:Dn 1497 L1/L2 Yes/Yes
   ```
   
   As shown in the preceding information, after the DIS priority of the IS-IS interface is changed, DeviceA immediately becomes a Level-1-2 DIS and the pseudonode is 0000.0000.0001.01.
   
   # Display information about IS-IS neighbors and the IS-IS interface on Device B.
   
   ```
   [~DeviceB] display isis peer
   ```
   ```
                             Peer information for ISIS(1)
   
     System Id     Interface          Circuit Id        State HoldTime Type     PRI
   --------------------------------------------------------------------------------
   0000.0000.0001  GE0/1/0            0000.0000.0001.01  Up   26s      L1(L1L2) 100 
   0000.0000.0003  GE0/1/0            0000.0000.0001.01  Up   26s      L1       64 
   0000.0000.0001  GE0/1/0            0000.0000.0001.01  Up   26s      L2(L1L2) 100 
   0000.0000.0004  GE0/1/0            0000.0000.0001.01  Up   26s      L2       64 
   
   Total Peer(s): 4
   ```
   ```
   [~DeviceB] display isis interface
   ```
   ```
                          Interface information for ISIS(1)
                          ---------------------------------
    Interface         Id      IPV4.State          IPV6.State      MTU  Type  DIS
    GE0/1/0           001        Up           Mtu:Dn/Lnk:Dn/IP:Dn 1497 L1/L2 No/No
   ```
   
   # Display information about IS-IS neighbors and the IS-IS interface on Device D.
   
   ```
   [~DeviceD] display isis peer
   ```
   ```
                             Peer information for ISIS(1)
   
     System Id     Interface          Circuit Id        State HoldTime Type     PRI
   --------------------------------------------------------------------------------
   0000.0000.0001  GE0/1/0            0000.0000.0001.01  Up   20s      L2       100 
   0000.0000.0002  GE0/1/0            0000.0000.0001.01  Up   20s      L2       64 
   
   Total Peer(s): 2
   ```
   ```
   [~DeviceD] display isis interface
   ```
   ```
                          Interface information for ISIS(1)
                          ---------------------------------
    Interface         Id      IPV4.State          IPV6.State      MTU  Type  DIS
    GE0/1/0           001        Up           Mtu:Dn/Lnk:Dn/IP:Dn 1497 L1/L2 No/No
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
   ip address 10.1.1.1 255.255.255.0
  ```
  ```
   isis enable 1
  ```
  ```
   isis dis-priority 100
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
   ip address 10.1.1.2 255.255.255.0
  ```
  ```
   isis enable 1
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
   is-level level-1
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
   ip address 10.1.1.3 255.255.255.0
  ```
  ```
   isis enable 1
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
   network-entity 10.0000.0000.0004.00
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
   ip address 10.1.1.4 255.255.255.0
  ```
  ```
   isis enable 1
  ```
  ```
  #
  ```
  ```
  return
  ```