Example for Configuring IS-IS Multi-Instance Processes
======================================================

Example for Configuring IS-IS Multi-Instance Processes

#### Networking Requirements

On IS-IS networks, multiple IS-IS processes need to be used to isolate different access rings. To close the access rings, the IS-IS processes on all access rings need to be enabled. In this case, you need to enable different IGP processes on one interface. This reduces the interface count and configuration workload of the access rings.

As shown in [Figure 1](#EN-US_TASK_0000001412446569__fig_dc_vrp_isis_cfg_008001):

DeviceA, DeviceB, DeviceC, and DeviceD interwork through IS-IS and form an IS-IS access ring. DeviceA, DeviceB, DeviceE, and DeviceF also interwork through IS-IS and form another IS-IS access ring. The IS-IS multi-instance process function is enabled on each router. Two IS-IS multi-instance processes are enabled on specified interfaces of DeviceA and DeviceB. One IS-IS multi-instance process is enabled on specified interfaces of DeviceC, DeviceD, DeviceE, and DeviceF.

**Figure 1** Configuring IS-IS multi-instance processes![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.


  
![](figure/en-us_image_0000001362089212.png)

| Device Name | Interface | IP Address |
| --- | --- | --- |
| DeviceA | 100GE1/0/1 | 10.1.1.2/24 |
| 100GE1/0/2 | 192.168.4.4/24 |
| 100GE1/0/3 | 192.168.5.5/24 |
| DeviceB | 100GE1/0/1 | 10.1.1.1/24 |
| 100GE1/0/2 | 192.168.0.1/24 |
| 100GE1/0/3 | 192.168.1.1/24 |
| DeviceC | 100GE1/0/1 | 192.168.3.1/24 |
| 100GE1/0/2 | 192.168.4.2/24 |
| DeviceD | 100GE1/0/1 | 192.168.3.2/24 |
| 100GE1/0/2 | 192.168.1.2/24 |
| DeviceE | 100GE1/0/1 | 192.168.2.4/24 |
| 100GE1/0/2 | 192.168.5.4/24 |
| DeviceF | 100GE1/0/1 | 192.168.2.5/24 |
| 100GE1/0/2 | 192.168.0.3/24 |



#### Precautions

To improve security, you are advised to configure IS-IS authentication. For details, see Configuring IS-IS Authentication. IS-IS interface authentication is used as an example. For details, see Example for Configuring Basic IS-IS Functions.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable the IS-IS multi-instance process function on each router.
2. Enable two IS-IS multi-instance processes on specified interfaces of DeviceA and DeviceB. In addition, enable one IS-IS multi-instance process on specified interfaces of DeviceC, DeviceD, DeviceE, and DeviceF.
3. Configure a cost for each of the two multi-instance processes on the specified interfaces of DeviceA and DeviceB.
4. Check information about IS-IS interfaces.

#### Data Preparation

To complete the configuration, you need the following data:

* Area addresses of DeviceA, DeviceB, DeviceC, DeviceD, DeviceE, and DeviceF
* IS-IS multi-instance process IDs of DeviceA, DeviceB, DeviceC, DeviceD, DeviceE, and DeviceF

#### Procedure

1. Configure an IP address for each interface.
   
   
   
   Configure IP addresses for interfaces according to [Figure 1](#EN-US_TASK_0000001412446569__fig_dc_vrp_isis_cfg_008001). For detailed configurations, see Configuration Scripts.
2. Enable IS-IS, configure a level, and set a NET for each device.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] isis 1
   [*DeviceA-isis-1] network-entity 00.1111.1111.1111.00
   [*DeviceA-isis-1] multi-instance enable iid 2
   [*DeviceA-isis-1] quit
   [*DeviceA] isis 2
   [*DeviceA-isis-2] network-entity 00.1111.1111.1112.00
   [*DeviceA-isis-2] multi-instance enable iid 3
   [*DeviceA-isis-2] quit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] isis 1
   [*DeviceB-isis-1] network-entity 00.2222.2222.2222.00
   [*DeviceB-isis-1] multi-instance enable iid 2
   [*DeviceB-isis-1] quit
   [*DeviceB] isis 2
   [*DeviceB-isis-2] network-entity 00.2222.2222.2223.00
   [*DeviceB-isis-2] multi-instance enable iid 3
   [*DeviceB-isis-2] quit
   ```
   
   # Configure DeviceC, DeviceD, DeviceE, and DeviceF.
   
   The configuration procedure is the same as that of DeviceA. For detailed configurations, see Configuration Scripts.
3. Set link costs for interfaces on DeviceA and DeviceB.
   
   
   
   # Configure DeviceA.
   
   
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] isis enable 1
   [*DeviceA-100GE1/0/1] isis enable 2
   [*DeviceA-100GE1/0/1] isis process-id 1 cost 5
   [*DeviceA-100GE1/0/1] isis process-id 2 cost 15
   [*DeviceA-100GE1/0/1] commit
   [~DeviceA-100GE1/0/1] quit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] interface 100ge 1/0/1
   [*DeviceB-100GE1/0/1] isis enable 1
   [*DeviceB-100GE1/0/1] isis enable 2
   [*DeviceB-100GE1/0/1] isis process-id 1 cost 5
   [*DeviceB-100GE1/0/1] isis process-id 2 cost 15
   [*DeviceB-100GE1/0/1] commit
   [~DeviceB-100GE1/0/1] quit
   ```

#### Verifying the Configuration

# Check information about the specified IS-IS interface on DeviceA. The command output shows that multiple IS-IS multi-instance processes can be enabled on the same interface.

```
[~DeviceA] display isis interface 100GE1/0/1
Interface information for ISIS(1)
------------------------------------------------------------------------
Interface    Id      IPV4.State          IPV6.State       MTU  Type  DIS  
100GE1/0/1      001         Up          Mtu:Up/Lnk:Up/IP:Up  1497 L1/L2 No/No
 
Interface information for ISIS(2)
-------------------------------------------------------------------------
Interface    Id      IPV4.State          IPV6.State        MTU  Type  DIS  
100GE1/0/1      001        Up           Mtu:Up/Lnk:Dn/IP:Dn  1497 L1/L2 No/No
```

#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  isis 1
   network-entity 00.1111.1111.1111.00
   multi-instance enable iid 2
  isis 2
   network-entity 00.1111.1111.1112.00
   multi-instance enable iid 3
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.2 255.255.255.0
   isis enable 1
   isis process-id 1 cost 5
   isis enable 2
   isis process-id 2 cost 15
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.4.4 255.255.255.0
   isis enable 2
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 192.168.5.5 255.255.255.0
   isis enable 1
  #  
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  isis 1
   network-entity 00.2222.2222.2222.00
   multi-instance enable iid 2
  isis 2
   network-entity 00.2222.2222.2223.00
   multi-instance enable iid 3
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.1 255.255.255.0
   isis enable 1
   isis process-id 1 cost 5
   isis enable 2
   isis process-id 2 cost 15
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.0.1 255.255.255.0
   isis enable 1
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 192.168.1.1 255.255.255.0
   isis enable 2
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  isis 2
   network-entity 00.3333.3333.3333.00
   multi-instance enable iid 3
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.3.1 255.255.255.0
   isis enable 2
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.4.2 255.255.255.0
   isis enable 2
  #
  return
  ```
* DeviceD
  
  ```
  #
  sysname DeviceD
  #
  isis 2
   network-entity 00.4444.4444.4444.00
   multi-instance enable iid 3
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.3.2 255.255.255.0
   isis enable 2
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.1.2 255.255.255.0
   isis enable 2
  #
  return
  ```
* DeviceE
  
  ```
  #
  sysname DeviceE
  #
  isis 1
   network-entity 00.5555.5555.5555.00
   multi-instance enable iid 2
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.2.4 255.255.255.0
   isis enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.5.4 255.255.255.0
   isis enable 1
  #
  return
  ```
* DeviceF
  
  ```
  #
  sysname DeviceF
  #
  isis 1
   network-entity 00.6666.6666.6666.00
   multi-instance enable iid 2
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.2.5 255.255.255.0
   isis enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.0.3 255.255.255.0
   isis enable 1
  return
  ```