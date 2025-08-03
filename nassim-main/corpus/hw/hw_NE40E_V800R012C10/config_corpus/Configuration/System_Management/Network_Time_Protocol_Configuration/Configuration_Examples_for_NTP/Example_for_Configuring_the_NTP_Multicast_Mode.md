Example for Configuring the NTP Multicast Mode
==============================================

In a multicast domain, the device with high clock precision functions as the NTP server, and other devices are synchronized with the clock of the NTP server.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001847647785__fig_dc_vrp_ntp_cfg_003001):

* Device C and Device D are on the same network segment.
* Device C functions as an NTP multicast server and its clock is a stratum 2 NTP master clock. Multicast packets are sent out from GE 0/1/0.
* Device D listens to multicast messages on GE 0/1/0.

**Figure 1** Configuring the NTP multicast mode  
![](figure/en-us_image_0000001800928954.png)
![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 in this example represents GE 0/1/0.



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure Device C as an NTP multicast server.
2. Configure Device A and Device D as NTP multicast clients.

#### Data Preparation

To complete the configuration, you need the following data:

* Interface IP addresses of all Routers and a unicast routing protocol
* Stratum of the NTP master clock

#### Procedure

1. Configure an IP address for each Device.
   
   
   
   Configure IP addresses based on [Figure 1](#EN-US_TASK_0000001847647785__fig_dc_vrp_ntp_cfg_003001). The detailed procedures are not mentioned here.
2. Configure an NTP multicast server.
   
   
   
   # Set the local clock on Device C as a stratum 2 NTP master clock.
   
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
   
   # Specify a listening interface on Device C.
   
   ```
   [~DeviceC] ntp-service server source-interface gigabitethernet 0/1/0 
   ```
   
   # Configure Device C as an NTP multicast server. NTP multicast packets are sent from GE 0/1/0.
   
   ```
   [*DeviceC] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] ntp-service multicast-server
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] commit
   ```
3. Configure DeviceD as an NTP multicast client which is on the same network segment as that of the NTP server.
   
   
   
   # Configure Device D as an NTP multicast client. Device D listens to the NTP multicast packets on GE 0/1/0.
   
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
   [~DeviceD] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceD-GigabitEthernet0/1/0] ntp-service multicast-client
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] commit
   ```
4. Verify the configuration.
   
   
   
   After completing the configurations, check that Device D can synchronize its clock with Device C.
   
   Check the NTP status on Device D. You can find that the clock status is **synchronized**. The stratum of the clock on Device D is 3, one stratum lower than that on Device C.
   
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
    synchronization state: clock synchronized
   ```

#### Configuration Files

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
   ntp-service multicast-server
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
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.0.1.32 255.255.255.0
  ```
  ```
   ntp-service multicast-client
  ```
  ```
  #
  ```
  ```
  Return
  ```