Example for Configuring NTP Peer Mode
=====================================

In NTP peer mode, both peers can be synchronized to the clock of each other.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001847727693__fig_dc_vrp_ntp_cfg_002801), three Routers are located in a LAN.

* Configure the clock on DeviceC as an NTP master clock with stratum 2.
* DeviceD takes DeviceC as its NTP server. That is, DeviceD functions as the client.
* DeviceE takes DeviceD as its symmetric passive peer. That is, DeviceE is the symmetric active peer.

**Figure 1** Configuring the NTP peer mode  
![](images/fig_dc_vrp_ntp_cfg_002801.png)
![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 represents GE0/1/0.



#### Precautions

Before configuring the NTP peer mode, ensure that the peer is reachable.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure the clock on DeviceC to be the NTP master clock. The clock on DeviceD must be synchronized to the clock on DeviceC.
2. Configure DeviceE and DeviceD as NTP peers so that DeviceE sends clock synchronization requests to DeviceD.
3. Finally, the clocks on DeviceC, DeviceD, and DeviceE can be synchronized.

#### Data Preparation

To complete the configuration, you need the following data:

* IP address of DeviceC
* IP address of DeviceD
* Stratum of the NTP master clock

#### Procedure

1. Configure IP addresses for DeviceC, DeviceD, and DeviceE.
   
   
   
   Configure an IP address for each interface based on [Figure 1](#EN-US_TASK_0000001847727693__fig_dc_vrp_ntp_cfg_002801). After configurations, the three Routers can **ping** through each other.
   
   For configuration details, see [Configuration Files](#EN-US_TASK_0000001847727693__example2091786840214019) in this section.
2. Configure the NTP server/client mode.
   
   
   
   # Configure the clock on DeviceC to be its own reference clock with the stratum being 2.
   
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
   [~DeviceC] ntp-service refclock-master 2
   ```
   
   # Specify a listening interface on DeviceC.
   
   ```
   [~DeviceC] ntp-service server source-interface gigabitethernet 0/1/0 
   ```
   ```
   [*DeviceC] commit
   ```
   
   # On DeviceD, configure DeviceC to be its NTP server.
   
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
   [~DeviceD] ntp-service unicast-server 10.0.1.31
   ```
   ```
   [*DeviceD] commit
   ```
   
   # Specify a listening interface on DeviceD.
   
   ```
   [~DeviceD] ntp-service server source-interface gigabitethernet 0/1/0 
   ```
   ```
   [*DeviceD] commit
   ```
   
   After configurations, the clock on DeviceD can be synchronized to the clock on DeviceC.
   
   Display the NTP status on DeviceD. The command output shows that the clock is synchronized. The stratum of the clock on DeviceD is 3, one stratum lower than that on DeviceC.
   
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
    nominal frequency: 64.0029 Hz
   ```
   ```
    actual frequency: 64.0029 Hz
   ```
   ```
    clock precision: 2^7
   ```
   ```
    clock offset: 0.0000 ms
   ```
   ```
    root delay: 62.50 ms
   ```
   ```
    root dispersion: 0.20 ms
   ```
   ```
    peer dispersion: 7.81 ms
   ```
   ```
    reference time: 06:52:33.465 UTC Mar 7 2006(C7B7AC31.773E89A8)
   ```
   ```
    synchronization state: clock synchronized
   ```
3. Configure the unicast NTP peer mode. 
   
   
   
   # On DeviceE, configure DeviceD to be the symmetric passive peer.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceE
   ```
   ```
   [*HUAWEI] commit 
   ```
   ```
   [~DeviceE] ntp-service unicast-peer 10.0.1.32
   ```
   ```
   [*DeviceE] commit
   ```
   
   Since no master clock is configured on DeviceE, the clock on DeviceE must be synchronized to the clock on DeviceD.
4. Verify the configuration.
   
   
   
   After the configurations are complete, check the NTP status of DeviceE. The command output shows that the NTP status is **synchronized** and the stratum of the clock on DeviceE is 4, one stratum lower than that on DeviceD.
   
   ```
   [~DeviceE] display ntp-service status
   ```
   ```
    clock status: synchronized
   ```
   ```
    clock stratum: 4
   ```
   ```
    reference clock ID: 10.0.1.32
   ```
   ```
    nominal frequency: 64.0029 Hz
   ```
   ```
    actual frequency: 64.0029 Hz
   ```
   ```
    clock precision: 2^7
   ```
   ```
    clock offset: 0.0000 ms
   ```
   ```
    root delay: 124.98 ms
   ```
   ```
    root dispersion: 0.15 ms
   ```
   ```
    peer dispersion: 10.96 ms
   ```
   ```
    reference time: 06:55:50.784 UTC Mar 7 2006(C7B7ACF6.C8D002E2)
   ```
   ```
    synchronization state: clock synchronized
   ```

#### Configuration Files

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
  ntp-service refclock-master 2
  ```
  ```
  ntp-service server source-interface gigabitethernet 0/1/0 
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
  ntp-service unicast-server 10.0.1.31
  ```
  ```
  ntp-service server source-interface gigabitethernet 0/1/0 
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
   ip address 10.0.1.32 255.255.255.0
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
  ntp-service unicast-peer 10.0.1.32
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
   ip address 10.0.1.33 255.255.255.0
  ```
  ```
  #
  ```
  ```
  return
  ```