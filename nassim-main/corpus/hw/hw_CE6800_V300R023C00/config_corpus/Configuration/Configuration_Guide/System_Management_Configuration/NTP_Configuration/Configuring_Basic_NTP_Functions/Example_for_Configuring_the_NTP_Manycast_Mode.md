Example for Configuring the NTP Manycast Mode
=============================================

Example for Configuring the NTP Manycast Mode

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001513155354__fig_dc_vrp_cfg_01081001):

* DeviceC and DeviceD are on the same network segment, and DeviceA is on a different network segment. DeviceB is connected to the two network segments.
* DeviceC is an NTP manycast server that sends manycast packets through Interface1. The local clock of DeviceC is a stratum 2 NTP master clock.
* DeviceD and DeviceA function as manycast clients and send packets through their respective Interface1.

**Figure 1** Configuring the NTP manycast mode![](public_sys-resources/note_3.0-en-us.png) 

In this example, Interface1 and Interface2 represent 100GE1/0/1 and 100GE1/0/2, respectively.


  
![](figure/en-us_image_0000001563755757.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure DeviceC as an NTP manycast server.
2. Configure DeviceA and DeviceD as NTP manycast clients.

#### Procedure

1. Assign an IP address to each device and ensure that the devices are routable.
2. Configure an NTP manycast server.
   
   
   
   # Configure the local clock on DeviceC as a stratum 2 NTP master clock.
   
   ```
   <DeviceC> system-view
   [*DeviceC] ntp refclock-master 2
   [*DeviceC] commit
   ```
   
   # Specify a listening interface on DeviceC.
   
   ```
   [~DeviceC] ntp server source-interface 100ge 1/0/1
   [*DeviceC] commit
   ```
   
   # Configure DeviceC as an NTP manycast server.
   
   ```
   [~DeviceC] interface 100ge 1/0/1
   [~DeviceC-100GE1/0/1] ntp manycast-server
   [*DeviceC] quit
   [*DeviceC] commit
   ```
   
   # Enable the NTP server function on DeviceC.
   
   ```
   [~DeviceC] undo ntp server disable
   [*DeviceC] commit
   ```
3. Configure DeviceD.
   
   
   
   # Configure DeviceD as an NTP manycast client. DeviceD sends NTP manycast packets to the NTP manycast server through Interface1.
   
   ```
   <DeviceD> system-view
   [*DeviceD] interface 100ge 1/0/1 
   [*DeviceD-100GE1/0/1] ntp manycast-client
   [*DeviceD] quit
   [*DeviceD] commit
   ```
4. Configure DeviceA.
   
   
   
   # Configure DeviceA as an NTP manycast client. DeviceA sends NTP manycast packets to the NTP manycast server through Interface1.
   
   ```
   <DeviceA> system-view
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] ntp manycast-client
   [*DeviceA] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Check the NTP clock status of the manycast client (DeviceD is used as an example). The command output shows that the clock status is **synchronized**, indicating that clock synchronization is complete. The stratum of DeviceD is 3, one stratum lower than DeviceC.

```
[~DeviceD] display ntp status
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
 autokey crypto flags: 0x80021
```

#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.11 255.255.255.0
   ntp manycast-client
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
   ip address 10.1.1.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.0.1.2 255.255.255.0
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.0.1.31 255.255.255.0
   ntp manycast-server
  #
   ntp server source-interface 100GE1/0/1
  #
  return
  ```
* DeviceD
  
  ```
  #
  sysname DeviceD
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.0.1.32 255.255.255.0
   ntp manycast-client
  #
  return
  ```