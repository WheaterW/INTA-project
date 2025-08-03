Example for Configuring the Manycast Mode
=========================================

Example_for_Configuring_the_Manycast_Mode

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0000001801088650__fig_dc_vrp_cfg_01081001):

* DeviceC and DeviceD are in the same subnet; DeviceA is in another subnet; DeviceF connects with the two subnets.
* DeviceC functions as an NTP manycast server and its local clock is a master clock with the stratum 2. Manycast packets are sent out from GE0/1/0.
* DeviceD and DeviceA are manycast clients and send packets on their respective GE0/1/0.

**Figure 1** Configuring the NTP manycast mode  
![](figure/en-us_image_0000001801088686.png)
![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent GE0/1/0 and GE0/2/0, respectively.



#### Precautions

Ensure manycast client is reachable to the manycast server before synchronization. This can be checked using [**ping**](cmdqueryname=ping) command on the console interface.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure DeviceC as an NTP manycast server.
2. Configure DeviceA and DeviceD as NTP manycast clients.
3. Enable multicast for DeviceF.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of DeviceA, DeviceC, DeviceD, and DeviceF and unicast routing protocol
* Stratum of the NTP master clock

#### Procedure

1. Configure an IP address for each Router.
   
   
   
   Configure IP addresses based on [Figure 1](#EN-US_TASK_0000001801088650__fig_dc_vrp_cfg_01081001). The detailed procedures are not mentioned here.
2. Configure an NTP manycast server.
   
   
   
   # Set the local clock on DeviceC as an NTP master clock with stratum 2.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceC
   ```
   ```
   [*HUAWEI] commit 
   ```
   ```
   [~DeviceC] undo ntp-service server disable 
   ```
   ```
   [~DeviceC] ntp-service refclock-master 2
   ```
   
   # Specify a listening interface on DeviceC.
   
   ```
   [~DeviceC] ntp-service server source-interface gigabitethernet 0/1/0 
   ```
   
   # Configure DeviceC as an NTP manycast server. NTP manycast server sends NTP manycast packets after receiving manycast client packets.
   
   ```
   [*DeviceC] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] ntp-service manycast-server
   ```
   ```
   [*DeviceC] commit
   ```
3. Configure DeviceD.
   
   
   
   # Configure DeviceD to be an NTP manycast client. DeviceD sends NTP manycast packets to manycast server on GE0/1/0.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceD
   ```
   ```
   [*HUAWEI] commit 
   ```
   ```
   [~DeviceD] undo ntp-service server disable
   ```
   ```
   [~DeviceD] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceD-GigabitEthernet0/1/0] ntp-service manycast-client
   ```
   ```
   [*DeviceD] commit
   ```
4. Configure DeviceA.
   
   
   
   # Configure DeviceA to be an NTP manycast client. DeviceA sends NTP manycast packets to manycast server on GE0/1/0.
   
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
   [~DeviceA] undo ntp-service server disable
   ```
   ```
   [~DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] ntp-service manycast-client
   ```
   ```
   [*DeviceA] commit
   ```
5. Enable multicast for DeviceF.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceF
   ```
   ```
   [*HUAWEI] commit 
   ```
   ```
   [~DeviceF] undo ntp-service server disable
   ```
   ```
   [~DeviceF] multicast routing-enable
   ```
   ```
   [*DeviceF] commit
   ```
   ```
   [~DeviceF] interface gigabitethernet 0/2/0
   ```
   ```
   [~DeviceF-GigabitEthernet0/2/0] pim sm
   ```
   ```
   [*DeviceF-GigabitEthernet0/2/0] igmp enable
   ```
   ```
   [*DeviceF-GigabitEthernet0/2/0] igmp static-group 224.0.1.1
   ```
   ```
   [*DeviceF-GigabitEthernet0/2/0] commit
   ```
   ```
   [~DeviceF-GigabitEthernet0/2/0] quit
   ```
   ```
   [~DeviceF] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceF-GigabitEthernet0/1/0] pim sm
   ```
   ```
   [*DeviceF-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceF-GigabitEthernet0/1/0] quit
   ```
6. Verify the configuration.
   
   
   
   After the configurations are complete, the clock on DeviceA and DeviceD can be synchronized to the clock on DeviceC.
   
   Check the NTP status on DeviceD and you can find that the clock status is "synchronized". That is, clock synchronization completes. The stratum of the clock on DeviceD is 3, one stratum lower than that on DeviceC.
   
   ```
   [~DeviceD] display ntp-service status
   ```
   ```
    clock status: synchronized
   ```
   ```
    clock stratum: 3
   ```
   ```
    reference clock ID: 10.0.1.31
   ```
   ```
    nominal frequency: 60.0002 Hz
   ```
   ```
    actual frequency: 60.0002 Hz
   ```
   ```
    clock precision: 2^18
   ```
   ```
    clock offset: 0.66 ms
   ```
   ```
    root delay: 24.47 ms
   ```
   ```
    root dispersion: 208.39 ms
   ```
   ```
    peer dispersion: 9.63 ms
   ```
   ```
    reference time: 17:03:32.022 UTC Apr 25 2005(C61734FD.800303C0)
   ```
   ```
    autokey crypto flags: 0x80021
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
  undo ntp-service server disable
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.1.11 255.255.255.0
  ```
  ```
   ntp-service manycast-client
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
  undo ntp-service server disable
  ```
  ```
  ntp-service refclock-master 2
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
   ip address 10.0.1.31 255.255.255.0
  ```
  ```
   ntp-service manycast-server
  ```
  ```
  ntp-service server source-interface gigabitethernet 0/1/0 
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
  undo ntp-service server disable
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.0.1.32 255.255.255.0
  ```
  ```
   ntp-service manycast-client
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
  undo ntp-service server disable
  multicast routing-enable
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
   ip address 10.0.1.2 255.255.255.0
  ```
  ```
   pim sm
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
   ip address 10.1.1.2 255.255.255.0
  ```
  ```
   pim sm
  ```
  ```
   igmp static-group 224.0.1.1
  ```
  ```
  #
  ```
  ```
  Return
  ```