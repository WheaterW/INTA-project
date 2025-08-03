Example for Configuring the NTP Multicast Mode
==============================================

Example for Configuring the NTP Multicast Mode

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001563875341__fig_dc_vrp_ntp_cfg_003001):

* DeviceA and DeviceB are on the same network segment.
* DeviceA functions as the NTP multicast server and sends NTP multicast packets through Interface1. Its local clock is a stratum 2 NTP master clock.
* DeviceB listens for NTP multicast messages through Interface1.

**Figure 1** Configuring the NTP multicast mode![](public_sys-resources/note_3.0-en-us.png) 

In this example, Interface1 represents 100GE1/0/1.


  
![](figure/en-us_image_0000001512676270.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure DeviceA as an NTP multicast server.
2. Configure DeviceB as an NTP multicast client.

#### Procedure

1. Assign an IP address to each device and ensure that the devices are routable.
2. Configure an NTP multicast server.
   
   
   
   # Configure the local clock on DeviceA as a stratum 2 NTP master clock.
   
   ```
   <DeviceA> system-view
   [~DeviceA] ntp refclock-master 2
   [*DeviceA] commit
   ```
   
   # Specify a listening interface on DeviceA.
   
   ```
   [~DeviceA] ntp server source-interface 100ge 1/0/1 
   [*DeviceA] commit
   ```
   
   # Configure DeviceA as an NTP multicast server that sends NTP multicast packets from Interface1.
   
   ```
   [~DeviceA] interface 100ge 1/0/1 
   [~DeviceA-100GE1/0/1] ntp multicast-server
   [*DeviceA] quit
   [*DeviceA] commit
   ```
   
   # Enable the NTP server function on DeviceA.
   
   ```
   [~DeviceA] undo ntp server disable
   [*DeviceA] commit
   ```
3. Configure DeviceB as an NTP multicast client that resides on the same network segment as the NTP multicast server.
   
   
   
   # Configure DeviceB as an NTP multicast client that listens for NTP multicast packets on Interface1.
   
   ```
   <DeviceB> system-view
   [~DeviceB] interface 100ge 1/0/1 
   [~DeviceB-100GE1/0/1] ntp multicast-client
   [*DeviceB] quit
   [*DeviceB] commit
   ```

#### Verifying the Configuration

# Check the NTP status of DeviceB. The command output shows that the clock status is **synchronized**, indicating that clock synchronization is complete. The stratum of DeviceB is 3, one stratum lower than DeviceA.

```
[~DeviceB] display ntp status
 clock status: synchronized
 clock stratum: 3
 reference clock ID: 10.0.1.31
 nominal frequency: 60.0002 Hz
 actual frequency: 60.0002 Hz
 clock precision: 2^18
 clock offset: 0.66 ms
 root delay: 24.47 ms
 root dispersion: 208.39 ms
 peer dispersion: 9.63 ms
 reference time: 17:03:32.022 UTC Feb 25 2020(C61734FD.800303C0)
 synchronization state: clock synchronized
```

#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  ntp refclock-master 2
  ntp server source-interface 100GE1/0/1
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.0.1.31 255.255.255.0
   ntp multicast-server
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.0.1.32 255.255.255.0
   ntp multicast-client
  #
  return
  ```