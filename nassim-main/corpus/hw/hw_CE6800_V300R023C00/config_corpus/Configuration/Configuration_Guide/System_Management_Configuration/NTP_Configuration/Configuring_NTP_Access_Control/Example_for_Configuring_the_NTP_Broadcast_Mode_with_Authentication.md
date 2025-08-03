Example for Configuring the NTP Broadcast Mode with Authentication
==================================================================

Example for Configuring the NTP Broadcast Mode with Authentication

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001563755705__fig_dc_vrp_ntp_cfg_002901):

* DeviceA and DeviceB are on the same network segment.
* DeviceA functions as an NTP broadcast server and sends NTP broadcast packets through Interface1. Its local clock is a stratum 3 NTP master clock.
* DeviceB listens for NTP broadcast messages through Interface1.
* NTP authentication needs to be enabled on DeviceA and DeviceB.

**Figure 1** Configuring the NTP broadcast mode with authentication![](public_sys-resources/note_3.0-en-us.png) 

In this example, Interface1 represents 100GE1/0/1.


  
![](figure/en-us_image_0000001512835866.png)

#### Precautions

Before configuring an authentication key on the client or server, ensure that the key already exists.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure DeviceA as an NTP broadcast server.
2. Configure DeviceB as an NTP broadcast client.
3. Configure DeviceA and DeviceB to participate in NTP authentication after passwords are encrypted using the HMAC-SHA256 algorithm.

#### Procedure

1. Assign an IP address to each device and ensure that the devices are routable.
2. Configure DeviceA as an NTP broadcast server.
   
   
   
   # Configure the local clock on DeviceA as a stratum 3 NTP master clock.
   
   ```
   <DeviceA> system-view
   [~DeviceA] ntp refclock-master 3
   [*DeviceA] commit
   ```
   
   # Specify a listening interface on DeviceA.
   
   ```
   [~DeviceA] ntp server source-interface 100ge 1/0/1 
   [*DeviceA] commit
   ```
   
   # Enable NTP authentication.
   
   ```
   [~DeviceA] ntp authentication enable
   [*DeviceA] ntp authentication-keyid 16 authentication-mode hmac-sha256 ********
   [*DeviceA] commit
   ```
   
   # Configure DeviceA as an NTP broadcast server that sends NTP broadcast packets from Interface1, and configure an authentication key with key ID being 16.
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] ntp broadcast-server authentication-keyid 16
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
   
   # Enable the NTP server function on DeviceA.
   
   ```
   [~DeviceA] undo ntp server disable
   [*DeviceA] commit
   ```
3. Configure DeviceB as an NTP broadcast client that resides on the same network segment as the NTP broadcast server.
   
   
   
   # Enable NTP authentication.
   
   ```
   <DeviceB> system-view
   [~DeviceB] ntp authentication enable
   [*DeviceB] ntp authentication-keyid 16 authentication-mode hmac-sha256 ********
   [*DeviceB] ntp trusted authentication-keyid 16
   [*DeviceB] commit
   ```
   
   # Configure DeviceB as an NTP broadcast client that listens for NTP broadcast packets on Interface1.
   
   ```
   [~DeviceB] interface 100ge 1/0/1
   [*DeviceB-100GE1/0/1] ntp broadcast-client
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] commit
   ```

#### Verifying the Configuration

# Check the NTP status of DeviceB. The command output shows that the clock status is **synchronized**, indicating that clock synchronization is complete. The stratum of DeviceB is 4, one stratum lower than DeviceA.

```
[~DeviceB] display ntp status
 clock status: synchronized
 clock stratum: 4
 reference clock ID: 10.0.1.31
 nominal frequency: 60.0002 Hz
 actual frequency: 60.0002 Hz
 clock precision: 2^18
 clock offset: 0.0000 ms
 root delay: 0.00 ms
 root dispersion: 0.42 ms
 peer dispersion: 0.00 ms
 reference time: 12:17:21.773 UTC Feb 7 2020(C7B7F851.C5EAF25B)
 synchronization state: clock synchronized
```

#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  ntp authentication-keyid 16 authentication-mode hmac-sha256 cipher %+%#>hD8))_H-XZVut2u3!_0lq3,+Ph=:OE}pX;T2M'9%+%#
  ntp refclock-master 3
  ntp authentication enable
  ntp server source-interface 100GE1/0/1
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.0.1.31 255.255.255.0
   ntp broadcast-server authentication-keyid 16
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  ntp authentication-keyid 16 authentication-mode hmac-sha256 cipher %+%#m:fVJfk*r&3x"1J`21^K`Y;LH;B+g(t2<ZX^}Q_~%+%#
  ntp trusted authentication-keyid 16
  ntp authentication enable
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.0.1.32 255.255.255.0
   ntp broadcast-client
  #
  return
  ```