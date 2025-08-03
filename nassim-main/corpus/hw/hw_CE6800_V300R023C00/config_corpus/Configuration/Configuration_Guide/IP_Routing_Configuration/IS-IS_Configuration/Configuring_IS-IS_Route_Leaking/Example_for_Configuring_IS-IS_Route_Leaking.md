Example for Configuring IS-IS Route Leaking
===========================================

Example for Configuring IS-IS Route Leaking

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001355819296__fig_dc_cfg_isisv4_008001), IS-IS is configured on the six routers. DeviceA and DeviceB function as Level-1 routers. DeviceC and DeviceD function as Level-1â2 routers and belong to area 10. DeviceE and DeviceF function as Level-2 routers and belong to area 20. The cost of GE 1/0/0 on DeviceC is 40, and other interfaces use the default cost 10. It is required that routing information in the Level-2 area be leaked to the Level-1 area so that the route from DeviceA to DeviceF is selected as the optimal route.

**Figure 1** Configuring IS-IS route leaking![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.


  
![](figure/en-us_image_0000001355979256.png)

#### Configuration Precautions

To improve security, you are advised to configure IS-IS authentication. For details, see Configuring IS-IS Authentication. IS-IS interface authentication is used as an example. For details, see Example for Configuring Basic IS-IS Functions.


#### Configuration Roadmap

The configuration roadmap is as follows:

* Assign an IP address to each interface and configure IS-IS on each device to implement network interworking.
* Configure DeviceA and DeviceB as Level-1 devices, and configure DeviceC and DeviceD as Level-1â2 devices in area 10. Configure DeviceE and DeviceF as Level-2 devices in area 20.
* Set the cost of GE 1/0/0 on DeviceC to 40, and retain the default cost 10 on other interfaces.
* Configure route leaking from the Level-2 area to the Level-1 area so that the route from DeviceA to DeviceF is selected as the optimal route.


#### Procedure

1. Configure IPv4 addresses for interfaces on each routing device.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ip address 192.168.1.1 24
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB, DeviceC, DeviceD, DeviceE, and DeviceF are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
2. Configure basic IS-IS functions on each device.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] isis 10
   [*DeviceA-isis-10] is-level level-1
   [*DeviceA-isis-10] network-entity 10.0000.0000.0001.00
   [*DeviceA-isis-10] quit
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] isis enable 10
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] isis 10
   [*DeviceB-isis-10] is-level level-1
   [*DeviceB-isis-10] network-entity 10.0000.0000.0002.00
   [*DeviceB-isis-10] quit
   [*DeviceB] interface 100ge 1/0/1
   [*DeviceB-100GE1/0/1] isis enable 10
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] isis 10
   [*DeviceC-isis-10] network-entity 10.0000.0000.0003.00
   [*DeviceC-isis-10] quit
   [*DeviceC] interface 100ge 1/0/1
   [*DeviceC-100GE1/0/1] isis enable 10
   [*DeviceC-100GE1/0/1] isis cost 40 level-2
   [*DeviceC-100GE1/0/1] quit
   [*DeviceC] commit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] isis 10
   [*DeviceD-isis-10] network-entity 10.0000.0000.0004.00
   [*DeviceD-isis-10] quit
   [*DeviceD] interface 100ge 1/0/1
   [*DeviceD-100GE1/0/1] isis enable 10
   [*DeviceD-100GE1/0/1] quit
   [*DeviceD] commit
   ```
   
   # Configure DeviceE.
   
   ```
   [~DeviceE] isis 10
   [*DeviceE-isis-10] is-level level-2
   [*DeviceE-isis-10] network-entity 20.0000.0000.0005.00
   [*DeviceE-isis-10] quit
   [*DeviceE] interface 100ge 1/0/1
   [*DeviceE-100GE1/0/1] isis enable 10
   [*DeviceE-100GE1/0/1] quit
   [*DeviceE] commit
   ```
   
   # Configure DeviceF.
   
   ```
   [~DeviceF] isis 10
   [*DeviceF-isis-10] is-level level-2
   [*DeviceF-isis-10] network-entity 20.0000.0000.0006.00
   [*DeviceF-isis-10] quit
   [*DeviceF] interface 100ge 1/0/1
   [*DeviceF-100GE1/0/1] isis enable 10
   [*DeviceF-100GE1/0/1] quit
   [*DeviceF] commit
   ```
   
   The configurations of 100GE1/0/2 and 100GE1/0/3 are the same as the configuration of 100GE1/0/1. For detailed configurations, see Configuration Scripts.
3. Configure route leaking on DeviceD.
   
   
   ```
   [~DeviceD] isis 10
   [*DeviceD-isis-10] import-route isis level-2 into level-1
   [*DeviceD-isis-10] quit
   ```

#### Verifying the Configuration

# Before configuring route leaking on DeviceD, run the **tracert 192.168.6.2** command on DeviceA. The command output shows that the link from DeviceA to DeviceF is DeviceA -> DeviceC -> DeviceE -> DeviceF. The cost of the entire link is 60 (10 + 40 + 10 = 60).

# After configuring route leaking on DeviceD, run the **tracert 192.168.6.2** command on DeviceA. The command output shows that the link from DeviceA to DeviceF is DeviceA -> DeviceB -> DeviceD -> DeviceE -> DeviceF. The cost of the entire link is 40 (10 + 10 + 10 + 10 = 40). The route from DeviceA to DeviceF is selected as the optimal route after route leaking is configured.


#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  isis 10
   is-level level-1
   network-entity 10.0000.0000.0001.00
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.1.1 255.255.255.0
   isis enable 10
  #  
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.2.1 255.255.255.0
   isis enable 10
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  isis 10
   is-level level-1
   network-entity 10.0000.0000.0002.00
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.1.2 255.255.255.0
   isis enable 10
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.3.1 255.255.255.0
   isis enable 10
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  isis 10
   network-entity 10.0000.0000.0003.00
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.4.1 255.255.255.0
   isis enable 10
   isis cost 40 level-2
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.2.2 255.255.255.0
   isis enable 10
  #
  return
  ```
* DeviceD
  
  ```
  #
  sysname DeviceD
  #
  isis 10
   network-entity 10.0000.0000.0004.00
   import-route isis level-2 into level-1
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.3.2 255.255.255.0
   isis enable 10
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.5.1 255.255.255.0
   isis enable 10
  #
  return
  ```
* DeviceE
  
  ```
  #
  sysname DeviceE
  #
  isis 10
   is-level level-2
   network-entity 20.0000.0000.0005.00
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.4.2 255.255.255.0
   isis enable 10
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.5.2 255.255.255.0
   isis enable 10
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 192.168.6.1 255.255.255.0
   isis enable 10
  #
  return
  ```
* DeviceF
  
  ```
  #
  sysname DeviceF
  #
  isis 10
   is-level level-2
   network-entity 20.0000.0000.0006.00
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.6.2 255.255.255.0
   isis enable 10
  #
  return
  ```