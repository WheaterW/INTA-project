Example for Configuring the NTP Peer Mode
=========================================

Example for Configuring the NTP Peer Mode

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001564115429__fig_dc_vrp_ntp_cfg_002801), three devices are in the LAN.

* DeviceA sets its local clock as a stratum 2 NTP master clock.
* DeviceB sets DeviceA as its NTP server. That is, DeviceB functions as an NTP client.
* DeviceC sets DeviceB as its symmetric passive peer. That is, DeviceC functions as the symmetric active peer.

**Figure 1** Configuring the NTP peer mode![](public_sys-resources/note_3.0-en-us.png) 

In this example, Interface1 represents 100GE1/0/1.


  
![](figure/en-us_image_0000001563755729.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure DeviceA as the local master clock so that DeviceB sends request packets to DeviceA for clock synchronization.
2. Configure DeviceC and DeviceB as peers so that DeviceC sends request packets to DeviceB for clock synchronization.

#### Procedure

1. Assign an IP address to each device and ensure that the devices are routable.
2. Configure the NTP client/server mode.
   
   
   
   # Configure DeviceA to use its local clock as a stratum 2 NTP reference clock.
   
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
   
   # Enable the NTP server function on DeviceA.
   
   ```
   [~DeviceA] undo ntp server disable
   [*DeviceA] commit
   ```
   
   # On DeviceB, configure DeviceA as the NTP server.
   
   ```
   <DeviceB> system-view
   [~DeviceB] ntp unicast-server 10.0.1.31
   [*DeviceB] commit
   ```
   
   # Specify a listening interface on DeviceB.
   
   ```
   [~DeviceB] ntp server source-interface 100ge 1/0/1 
   [*DeviceB] commit
   ```
3. Configure the NTP peer mode.
   
   
   
   # On DeviceC, specify DeviceB as the symmetric passive peer.
   
   ```
   <DeviceC> system-view
   [~DeviceC] ntp unicast-peer 10.0.1.32
   [*DeviceC] commit
   ```

#### Verifying the Configuration

# Check the NTP status of DeviceB. The command output shows that the clock status is **synchronized**, indicating that clock synchronization is complete. The stratum of DeviceB is 3, one stratum lower than DeviceA.

```
[~DeviceB] display ntp status
 clock status: synchronized
 clock stratum: 3
 reference clock ID: 10.0.1.31
 nominal frequency: 64.0029 Hz
 actual frequency: 64.0029 Hz
 clock precision: 2^7
 clock offset: 0.0000 ms
 root delay: 62.50 ms
 root dispersion: 0.20 ms
 peer dispersion: 7.81 ms
 reference time: 06:52:33.465 UTC Feb 7 2020(C7B7AC31.773E89A8)
 synchronization state: clock synchronized
```

# Check the NTP status of DeviceC. The command output shows that the clock status is **synchronized**, indicating that clock synchronization is complete. The stratum of DeviceC is 4, one stratum lower than DeviceB.

```
[~DeviceC] display ntp status
 clock status: synchronized
 clock stratum: 4
 reference clock ID: 10.0.1.32
 nominal frequency: 64.0029 Hz
 actual frequency: 64.0029 Hz
 clock precision: 2^7
 clock offset: 0.0000 ms
 root delay: 124.98 ms
 root dispersion: 0.15 ms
 peer dispersion: 10.96 ms
 reference time: 06:55:50.784 UTC Feb 7 2020(C7B7ACF6.C8D002E2)
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
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  ntp server source-interface 100GE1/0/1
  ntp unicast-server 10.0.1.31
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.0.1.32 255.255.255.0
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  ntp unicast-peer 10.0.1.32
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.0.1.33 255.255.255.0
  #
  return
  ```