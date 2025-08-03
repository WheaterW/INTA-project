Example for Configuring IS-IS Multi-Instance Processes
======================================================

This section provides an example for configuring IS-IS multi-instance processes.

#### Networking Requirements

On IS-IS networks, multiple IS-IS processes need to be used to isolate different access rings. To close the access rings, the IS-IS processes on all access rings need to be enabled. In this case, you need to enable different IGP processes on one interface. This reduces the interface number and configuration workload of the access rings.

As shown in [Figure 1](#EN-US_TASK_0172366097__fig_dc_vrp_isis_cfg_008001):

DeviceA, DeviceB, DeviceC, DeviceD run IS-IS to implement IP network connectivity and form an IS-IS access ring. In addition, DeviceA, DeviceB, DeviceE, and DeviceF run IS-IS to implement IP network connectivity and form another IS-IS access ring. IS-IS multi-instance processes are enabled on all Routers. Two IS-IS multi-instance processes are enabled on a specified interface of DeviceA and DeviceB, and one IS-IS multi-instance process is enabled on a specified interface of DeviceC, DeviceD, DeviceE, and DeviceF.

**Figure 1** Networking for configuring IS-IS multi-instance processes![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1, 2, and 3 stand for GE 0/1/0, GE 0/2/0, and GE 0/3/0, respectively.


  
![](images/fig_dc_vrp_isis_cfg_008001.png)

| Device Name | Interface | IP Address |
| --- | --- | --- |
| DeviceA | GE 0/1/0 | 10.1.1.2/24 |
| GE 0/2/0 | 192.168.4.4/24 |
| GE 0/3/0 | 192.168.5.5/24 |
| DeviceB | GE 0/1/0 | 10.1.1.1/24 |
| GE 0/2/0 | 192.168.0.1/24 |
| GE 0/3/0 | 192.168.1.1/24 |
| DeviceC | GE 0/1/0 | 192.168.3.1/24 |
| GE 0/2/0 | 192.168.4.2/24 |
| DeviceD | GE 0/1/0 | 192.168.3.2/24 |
| GE 0/2/0 | 192.168.1.2/24 |
| DeviceE | GE 0/1/0 | 192.168.2.4/24 |
| GE 0/2/0 | 192.168.5.4/24 |
| DeviceF | GE 0/1/0 | 192.168.2.5/24 |
| GE 0/2/0 | 192.168.0.3/24 |



#### Precautions

To improve security, you are advised to configure IS-IS authentication. For details, see "Configuring IS-IS Authentication." IS-IS interface authentication is used as an example. For details, see Example for Configuring Basic IS-IS Functions.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IS-IS multi-instance processes on the Router devices.
2. Enable two IS-IS multi-instance processes on an interface of DeviceA and DeviceB, and enable one IS-IS multi-instance process on an interface of DeviceC, DeviceD, DeviceE, and DeviceF.
3. Configure a cost for each IS-IS multi-instance process on the interface of DeviceA and DeviceB.
4. Check information about IS-IS interfaces.

#### Data Preparation

To complete the configuration, you need the following data:

* Area address of DeviceA, DeviceB, DeviceC, DeviceD, DeviceE, and DeviceF
* IS-IS multi-instance process IDs of DeviceA, DeviceB, DeviceC, DeviceD, DeviceE, and DeviceF

#### Procedure

1. Configure an IP address for each interface. For configuration details, see Configuration Files.
2. Configure IS-IS multi-instance processes.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] isis 1
   ```
   ```
   [*DeviceA-isis-1] network-entity 00.1111.1111.1111.00
   ```
   ```
   [*DeviceA-isis-1] multi-instance enable iid 2
   ```
   ```
   [*DeviceA-isis-1] commit
   ```
   ```
   [~DeviceA-isis-1] quit
   ```
   ```
   [~DeviceA] isis 2
   ```
   ```
   [*DeviceA-isis-2] network-entity 00.1111.1111.1112.00
   ```
   ```
   [*DeviceA-isis-2] multi-instance enable iid 3
   ```
   ```
   [*DeviceA-isis-2] commit
   ```
   ```
   [~DeviceA-isis-2] quit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] isis 1
   ```
   ```
   [*DeviceB-isis-1] network-entity 00.2222.2222.2222.00
   ```
   ```
   [*DeviceB-isis-1] multi-instance enable iid 2
   ```
   ```
   [*DeviceB-isis-1] commit
   ```
   ```
   [~DeviceB-isis-1] quit
   ```
   ```
   [~DeviceB] isis 2
   ```
   ```
   [*DeviceB-isis-2] network-entity 00.2222.2222.2223.00
   ```
   ```
   [*DeviceB-isis-2] multi-instance enable iid 3
   ```
   ```
   [*DeviceB-isis-2] commit
   ```
   ```
   [~DeviceB-isis-2] quit
   ```
   
   The configurations of DeviceC, DeviceD, DeviceE, and DeviceF are similar to the configuration of DeviceA. For configuration details, see Configuration Files.
3. Configure costs on DeviceA and DeviceB.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] isis enable 1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] isis enable 2
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] isis process-id 1 cost 5
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] isis process-id 2 cost 15
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] quit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] isis enable 1
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] isis enable 2
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] isis process-id 1 cost 5
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] isis process-id 2 cost 15
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] quit
   ```
   
   The configurations of DeviceC, DeviceD, DeviceE, and DeviceF are similar to the configuration of DeviceA. For configuration details, see Configuration Files.
4. Verify the configuration.
   
   
   
   # View information about the specified IS-IS interface on DeviceA. The command output shows that more than one multi-instance IS-IS process can be enabled on the interface.
   
   ```
   [~DeviceA] display isis interface gigabitethernet 0/1/0
   ```
   ```
                       Interface information for ISIS(1)
                       ---------------------------------
    Interface    Id      IPV4.State          IPV6.State       MTU  Type  DIS  
    GE0/1/0     001         Up          Mtu:Dn/Lnk:Dn/IP:Dn  1497 L1/L2 No/No
    
                       Interface information for ISIS(2)
                       ---------------------------------
    Interface    Id      IPV4.State          IPV6.State        MTU  Type  DIS  
    GE0/1/0     001         Up          Mtu:Dn/Lnk:Dn/IP:Dn  1497 L1/L2 No/No
   ```

#### Configuration Files

* DeviceA configuration file
  
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
   network-entity 00.1111.1111.1111.00
  ```
  ```
   multi-instance enable iid 2
  ```
  ```
  isis 2
  ```
  ```
   network-entity 00.1111.1111.1112.00
  ```
  ```
   multi-instance enable iid 3
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
   isis process-id 1 cost 5
  ```
  ```
   isis enable 2
  ```
  ```
   isis process-id 2 cost 15
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
   ip address 192.168.4.4 255.255.255.0
  ```
  ```
   isis enable 2
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
   ip address 192.168.5.5 255.255.255.0
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
* DeviceB configuration file
  
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
   network-entity 00.2222.2222.2222.00
  ```
  ```
   multi-instance enable iid 2
  ```
  ```
  isis 2
  ```
  ```
   network-entity 00.2222.2222.2223.00
  ```
  ```
   multi-instance enable iid 3
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
   isis process-id 1 cost 5
  ```
  ```
   isis enable 2
  ```
  ```
   isis process-id 2 cost 15
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
   ip address 192.168.0.1 255.255.255.0
  ```
  ```
   isis enable 1
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
   ip address 192.168.1.1 255.255.255.0
  ```
  ```
   isis enable 2
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceC configuration file
  
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
  isis 2
  ```
  ```
   network-entity 00.3333.3333.3333.00
  ```
  ```
   multi-instance enable iid 3
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
   ip address 192.168.3.1 255.255.255.0
  ```
  ```
   isis enable 2
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
   ip address 192.168.4.2 255.255.255.0
  ```
  ```
   isis enable 2
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceD configuration file
  
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
  isis 2
  ```
  ```
   network-entity 00.4444.4444.4444.00
  ```
  ```
   multi-instance enable iid 3
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
   ip address 192.168.3.2 255.255.255.0
  ```
  ```
   isis enable 2
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
   ip address 192.168.1.2 255.255.255.0
  ```
  ```
   isis enable 2
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceE configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceE
  ```
  ```
  #
  ```
  ```
  isis 1
  ```
  ```
   network-entity 00.5555.5555.5555.00
  ```
  ```
   multi-instance enable iid 2
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
   ip address 192.168.2.4 255.255.255.0
  ```
  ```
   isis enable 1
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
   ip address 192.168.5.4 255.255.255.0
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
* DeviceF configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceF
  ```
  ```
  #
  ```
  ```
  isis 1
  ```
  ```
   network-entity 00.6666.6666.6666.00
  ```
  ```
   multi-instance enable iid 2
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
   ip address 192.168.2.5 255.255.255.0
  ```
  ```
   isis enable 1
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
   ip address 192.168.0.3 255.255.255.0
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