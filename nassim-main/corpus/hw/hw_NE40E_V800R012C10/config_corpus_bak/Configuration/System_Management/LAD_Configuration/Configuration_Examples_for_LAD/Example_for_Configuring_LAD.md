Example for Configuring LAD
===========================

This section provides an example for configuring Link Automatic Discovery (LAD) so that the NMS can obtain detailed network topology, helping network administrators monitor and manage network devices.

#### Networking Requirements

Large-scale networks demand increased NMS capabilities, with increasing device types and complex configurations. LAD flexibly discovers neighbors at the data link layer and provides Layer 2 device information for the NMS.

On the network shown in [Figure 1](#EN-US_TASK_0172360337__fig_dc_vrp_lad_cfg_000801), DeviceA and DeviceB have reachable links, and DeviceA has a reachable route to the NMS. However, the NMS can only analyze the Layer 3 network topology, not Layer 2 network topology or configuration conflicts. To allow the NMS to obtain the Layer 2 configurations of DeviceA and DeviceB, or detect configuration conflicts between DeviceA and DeviceB and identify the cause for network failures, configure LAD on both DeviceA and DeviceB.

**Figure 1** LAD networking  
![](images/fig_dc_vrp_lad_cfg_000801.png)
![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, Interface1 represents GE0/1/1.

Then enable DeviceA to send LAD Link Detect packets to DeviceB. After DeviceA receives Link Reply packets from DeviceB, DeviceA obtains DeviceB's information. The NMS can exchange NETCONF packets with DeviceA to obtain the network topology between DeviceA and DeviceB.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IP addresses and routing protocols for DeviceA and DeviceB to implement network layer connectivity.
2. Enable LAD on the specified interfaces of DeviceA and DeviceB.
3. Enable DeviceA to send LAD Link Detect packets to DeviceB.

#### Data Preparation

To complete the configuration, you need the following data:

* Types and numbers of the interfaces connecting DeviceA and DeviceB
* IP addresses of GE0/1/1 on DeviceA and DeviceB


#### Procedure

1. Assign an IP address to each interface.
   
   
   
   Configure IP addresses for GE0/1/1 on DeviceA and DeviceB. For configuration details, see [Configuration Files](#EN-US_TASK_0172360337__section_05).
2. Configure Open Shortest Path First (OSPF).
   
   
   
   Configure OSPF on DeviceA and DeviceB so that they are reachable at the network layer. For configuration details, see [Configuration Files](#EN-US_TASK_0172360337__section_05).
3. Enable LAD on the specified interfaces of DeviceA and DeviceB.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceA
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceA] link-detect enable
   [*DeviceA] commit
   ```
   ```
   [~DeviceA] interface gigabitethernet0/1/1
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] link-detect enable
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] quit
   ```
   ```
   [~DeviceA] quit
   ```
   
   
   
   # Configure DeviceB.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceB
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceB] link-detect enable
   [*DeviceB] commit
   ```
   ```
   [~DeviceB] interface gigabitethernet0/1/1
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/1] link-detect enable
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] commit
   ```
4. Enable DeviceA to send LAD packets to DeviceB.
   
   
   ```
   <DeviceA> link detect interface gigabitethernet 0/1/1
   ```
   ```
   <DeviceA> commit
   ```
5. Verify the configuration.
   
   
   
   # Display neighbor information on DeviceA.
   
   ```
   <DeviceA> display link neighbor all
   ```
   ```
   GigabitEthernet0/1/1 has neighbors:
    TxNeId   TxInterface              TxVlanOrVc12  TxVc4Id  ---  RxNeId   RxInterface               RxVlanOrVc12  RxVc4Id
    0x6      GigabitEthernet0/1/1     0             0        ---  0x10001  GigabitEthernet0/1/1      0             0
   Total records of slot 1: 1
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.10.10.1 255.255.255.0
   link-detect enable
  #
  ospf 1
   area 0.0.0.0
    network 10.10.10.0 0.0.0.255
  #
  return
  ```
* DeviceB configuration file
  
  ```
  #
  sysname DeviceB
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.10.10.2 255.255.255.0
   link-detect enable
  #
  ospf 1
   area 0.0.0.0
    network 10.10.10.0 0.0.0.255
  #
  return
  ```