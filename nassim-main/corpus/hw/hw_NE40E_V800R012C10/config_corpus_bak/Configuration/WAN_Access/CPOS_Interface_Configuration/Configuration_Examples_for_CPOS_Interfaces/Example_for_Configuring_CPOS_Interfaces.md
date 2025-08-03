Example for Configuring CPOS Interfaces
=======================================

Example_for_Configuring_CPOS_Interfaces

#### Networking Requirements

CPOS interfaces are used to improve the convergence capability of low-speed access for Routers. STM-1 CPOS interfaces are often used to converge multiple E1 interfaces.

At present, some governmental agencies and enterprises use low-end and mid-range devices to access the transmission network through E1 leased lines. Users requiring bandwidth between E1 and E3, such as the date center, lease several E1 interfaces simultaneously. Bandwidth of these users converges on one or multiple CPOS interfaces through the transmission network. CPOS interfaces are then connected to DeviceA that identifies each low-end device through timeslots.

In application, there may be more than one level of transmission networks between CPOS interfaces and low-end devices. Other transmission devices are needed to relay communication between low-end devices and transmission networks.

**Figure 1** Networking diagram of using STM-1 CPOS interface  
![](images/fig_dc_vrp_cpos_cfg_001001.png "Click to enlarge")

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create the channel.
2. Create the channel-set.
3. Bundle the channel into the channel-set.

#### Data Preparation

To complete the configuration, you need the following data:

* Channel number and timeslot number of each E1 channel
* Number of the channel-set of each interface

#### Procedure

1. Configure DeviceA.
   
   
   
   # Create a channel on the CPOS interface.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceA
   ```
   ```
   [*DeviceA] controller cpos 0/3/0
   ```
   ```
   [*DeviceA-Cpos0/3/0] e1 1 channel-set 1 timeslot-list 1-10
   ```
   ```
   [*DeviceA-Cpos0/3/0] e1 2 channel-set 2 timeslot-list 11-15
   ```
   ```
   [*DeviceA-Cpos0/3/0] e1 3 channel-set 3 timeslot-list 16-20
   ```
   ```
   [*DeviceA-Cpos0/3/0] e1 4 channel-set 4 timeslot-list 21-31
   ```
   ```
   [*DeviceA-Cpos0/3/0] undo shutdown
   ```
   ```
   [*DeviceA-Cpos0/3/0] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Create a channel-set and configure the endpoint authenticator.
   
   ```
   [~DeviceA] interface mp-group 0/3/1
   ```
   ```
   [*DeviceA-Mp-group0/3/1] discriminator
   ```
   ```
   [*DeviceA-Mp-group0/3/1] undo shutdown
   ```
   ```
   [*DeviceA-Mp-group0/3/1] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Bundle the channel into the channel-set.
   
   ```
   [~DeviceA] interface Serial 0/3/0/1:1
   ```
   ```
   [~DeviceA-Serial0/3/0/1:1] link-protocol ppp
   ```
   ```
   [*DeviceA-Serial0/3/0/1:1] ppp mp mp-group 0/3/1
   ```
   ```
   [*DeviceA-Serial0/3/0/1:1] quit
   ```
   ```
   [*DeviceA] interface Serial 0/3/0/2:2
   ```
   ```
   [*DeviceA-Serial0/3/0/2:2] link-protocol ppp
   ```
   ```
   [*DeviceA-Serial0/3/0/2:2] ppp mp mp-group 0/3/1
   ```
   ```
   [*DeviceA-Serial0/3/0/2:2] quit
   ```
   ```
   [*DeviceA] interface Serial 0/3/0/3:3
   ```
   ```
   [*DeviceA-Serial0/3/0/3:3] link-protocol ppp
   ```
   ```
   [*DeviceA-Serial0/3/0/3:3] ppp mp mp-group 0/3/1
   ```
   ```
   [*DeviceA-Serial0/3/0/3:3] quit
   ```
   ```
   [*DeviceA] interface Serial 0/3/0/4:4
   ```
   ```
   [*DeviceA-Serial0/3/0/4:4] link-protocol ppp
   ```
   ```
   [*DeviceA-Serial0/3/0/4:4] ppp mp mp-group 0/3/1
   ```
   ```
   [*DeviceA-Serial0/3/0/4:4] quit
   ```
   ```
   [*DeviceA] commit
   ```
2. Configure DeviceB.
   
   
   
   # Create the channel on the E1 interface.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceB
   ```
   ```
   [*DeviceB] controller E1 0/2/9
   ```
   ```
   [*DeviceB-E10/2/9] channel-set 0 timeslot-list 1-31
   ```
   ```
   [*DeviceB-E10/2/9]  undo shutdown
   ```
   ```
   [*DeviceB-E10/2/9] quit
   ```
   ```
   [*DeviceB] commit
   ```
   
   # Create a channel-set.
   
   ```
   [~DeviceB] interface mp-group 0/2/10
   ```
   ```
   [*DeviceB-Mp-group0/2/10] discriminator
   ```
   ```
   [*DeviceB-Mp-group0/2/10] undo shutdown
   ```
   ```
   [*DeviceB-Mp-group0/2/10] quit
   ```
   ```
   [*DeviceB] commit
   ```
   
   # Bundle the channel into the channel-set.
   
   ```
   [~DeviceB] interface Serial0/2/9:0
   ```
   ```
   [~DeviceB-Serial0/2/9:0] link-protocol ppp
   ```
   ```
   [*DeviceB-Serial0/2/9:0] ppp mp mp-group 0/2/10
   ```
   ```
   [*DeviceB] commit
   ```

#### Configuration Files

* Configuration file of DeviceA
  
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
  controller Cpos0/3/0
  ```
  ```
   e1 1 channel-set 1 timeslot-list 1-10
  ```
  ```
   e1 2 channel-set 2 timeslot-list 11-15
  ```
  ```
   e1 3 channel-set 3 timeslot-list 16-20
  ```
  ```
   e1 4 channel-set 4 timeslot-list 21-31
  ```
  ```
   undo shutdown
  ```
  ```
  #
  ```
  ```
  interface Serial0/3/0/1:1
  ```
  ```
   link-protocol ppp
  ```
  ```
   ppp mp Mp-group 0/3/1
  ```
  ```
  #
  ```
  ```
  interface Serial0/3/0/2:2
  ```
  ```
   link-protocol ppp
  ```
  ```
   ppp mp Mp-group 0/3/1
  ```
  ```
  #
  ```
  ```
  interface Serial0/3/0/3:3
  ```
  ```
   link-protocol ppp
  ```
  ```
   ppp mp Mp-group 0/3/1
  ```
  ```
  #
  ```
  ```
  interface Serial0/3/0/4:4
  ```
  ```
   link-protocol ppp
  ```
  ```
   ppp mp Mp-group 0/3/1
  ```
  ```
  #
  ```
  ```
  interface Mp-group0/3/1
  ```
  ```
   discriminator
  ```
  ```
  #
  ```
  ```
  return
  ```
* Configuration file of DeviceB
  
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
  controller E1 0/2/9
  ```
  ```
   channel-set 0 timeslot-list 1-31
  ```
  ```
   undo shutdown
  ```
  ```
  #
  ```
  ```
  interface Mp-group 0/2/10
  ```
  ```
   discriminator
  ```
  ```
  #
  ```
  ```
  interface Serial0/2/9:0
  ```
  ```
   link-protocol ppp
  ```
  ```
   ppp mp Mp-group 0/2/10
  ```
  ```
  #
  ```
  ```
  return
  ```