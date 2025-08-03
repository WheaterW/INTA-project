Example for Configuring the NTP Client/Server Mode with Authentication
======================================================================

Example for Configuring the NTP Client/Server Mode with Authentication

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001564115461__fig_dc_vrp_ntp_cfg_002701):

* DeviceA functions as an NTP server, and its local clock functions as a stratum 2 NTP master clock.
* DeviceB functions as an NTP client to synchronize its clock to DeviceA.
* DeviceC and DeviceD function as NTP clients and use DeviceB as their respective NTP server.
* NTP authentication needs to be enabled on all devices.

**Figure 1** Configuring the NTP client/server mode with authentication![](public_sys-resources/note_3.0-en-us.png) 

In this example, Interface1 and Interface2 represent 100GE1/0/1 and 100GE1/0/2, respectively.


  
![](figure/en-us_image_0000001513035438.png)

#### Precautions

* Before specifying the NTP server address and the authentication key to be sent to the NTP server, you must enable NTP authentication on an NTP client. Otherwise, clock synchronization is directly implemented without NTP authentication.
* The authentication keys on the NTP client and server must be the same and the authentication key must be declared. Otherwise, NTP authentication will fail.
* Enable NTP authentication on both the server and client.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure DeviceA as an NTP server to provide the master clock.
2. Configure DeviceB as an NTP client to synchronize its clock to DeviceA.
3. Configure DeviceC and DeviceD as NTP clients to synchronize their clocks to DeviceB.
4. Configure DeviceA, DeviceB, DeviceC, and DeviceD to participate in NTP authentication after passwords are encrypted using the HMAC-SHA256 algorithm.

#### Procedure

1. Assign an IP address to each device and ensure that the devices are routable.
2. On DeviceA, configure the NTP master clock, specify a listening interface, and enable NTP authentication.
   
   
   
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
   
   # Enable NTP authentication on DeviceA and configure an authentication key.
   
   ```
   [~DeviceA] ntp authentication enable
   [*DeviceA] ntp authentication-keyid 42 authentication-mode hmac-sha256 ********
   [*DeviceA] commit
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The authentication keys configured on the server and the client must be the same.
   
   
   # Enable the NTP server function on DeviceA.
   
   ```
   [~DeviceA] undo ntp server disable
   [*DeviceA] commit
   ```
3. On DeviceB, enable NTP authentication, specify a listening interface, and specify an NTP server.
   
   
   
   # Enable NTP authentication on DeviceB, configure an authentication key, and declare the authentication key as reliable.
   
   ```
   <DeviceB> system-view
   [~DeviceB] ntp authentication enable
   [*DeviceB] ntp authentication-keyid 42 authentication-mode hmac-sha256 ********
   [*DeviceB] ntp trusted authentication-keyid 42
   [*DeviceB] commit
   ```
   
   # Specify a listening interface on DeviceB.
   
   ```
   [~DeviceB] ntp server source-interface 100ge 1/0/1
   [*DeviceB] commit
   ```
   
   # Specify DeviceA as the NTP server of DeviceB, and configure DeviceB to use the configured authentication key.
   
   ```
   [~DeviceB] ntp unicast-server 2.2.2.2 authentication-keyid 42
   [*DeviceB] commit
   ```
   
   # Enable the NTP server function on DeviceB.
   
   ```
   [~DeviceB] undo ntp server disable
   [*DeviceB] commit
   ```
4. On DeviceC, enable NTP authentication and specify its NTP server.
   
   
   ```
   <DeviceC> system-view
   [~DeviceC] ntp authentication enable
   [*DeviceC] ntp authentication-keyid 42 authentication-mode hmac-sha256 ********
   [*DeviceC] ntp trusted authentication-keyid 42
   [*DeviceC] ntp unicast-server 10.0.0.1 authentication-keyid 42
   [*DeviceC] commit
   ```
5. On DeviceD, enable NTP authentication and specify its NTP server.
   
   
   ```
   <DeviceD> system-view
   [~DeviceD] ntp authentication enable
   [*DeviceD] ntp authentication-keyid 42 authentication-mode hmac-sha256 ********
   [*DeviceD] ntp trusted authentication-keyid 42
   [*DeviceD] ntp unicast-server 10.0.0.1 authentication-keyid 42
   [*DeviceD] commit
   ```

#### Verifying the Configuration

# Check the NTP status of DeviceB. The command output shows that the clock status is **synchronized**, indicating that clock synchronization is complete. The stratum of DeviceB is 3, one stratum lower than DeviceA.

```
[~DeviceB] display ntp status
 clock status: synchronized
 clock stratum: 3
 reference clock ID: 2.2.2.2
 nominal frequency: 60.0002 Hz
 actual frequency: 60.0002 Hz
 clock precision: 2^18
 clock offset: 3.8128 ms
 root delay: 31.26 ms
 root dispersion: 74.20 ms
 peer dispersion: 34.30 ms
 reference time: 11:55:56.833 UTC Feb 2 2020(C7B15BCC.D5604189)
 synchronization state: clock synchronized
```

# Check the NTP status of DeviceC. The command output shows that the clock status is **synchronized**, indicating that clock synchronization is complete. The stratum of DeviceC is 4, one stratum lower than DeviceB.

```
[~DeviceC] display ntp status
 clock status: synchronized
 clock stratum: 4
 reference clock ID: 10.0.0.1
 nominal frequency: 60.0002 Hz
 actual frequency: 60.0002 Hz
 clock precision: 2^18
 clock offset: 3.8128 ms
 root delay: 31.26 ms
 root dispersion: 74.20 ms
 peer dispersion: 34.30 ms
 reference time: 11:55:56.833 UTC Feb 2 2020(C7B15BCC.D5604189)
 synchronization state: clock synchronized
```

# Check the NTP status of DeviceD. The command output shows that the clock status is **synchronized**, indicating that clock synchronization is complete. The stratum of DeviceD is 4, one stratum lower than DeviceB.

```
[~DeviceD] display ntp status
 clock status: synchronized
 clock stratum: 4
 reference clock ID: 10.0.0.1
 nominal frequency: 60.0002 Hz
 actual frequency: 60.0002 Hz
 clock precision: 2^18
 clock offset: 3.8128 ms
 root delay: 31.26 ms
 root dispersion: 74.20 ms
 peer dispersion: 34.30 ms
 reference time: 11:55:56.833 UTC Feb 2 2020(C7B15BCC.D5604189)
 synchronization state: clock synchronized
```

# Check the NTP status of DeviceA.

```
[~DeviceA] display ntp status
 clock status: synchronized
 clock stratum: 2
 reference clock ID: LOCAL(0)
 nominal frequency: 60.0002 Hz
 actual frequency: 60.0002 Hz
 clock precision: 2^18
 clock offset: 0.0000 ms
 root delay: 0.00 ms
 root dispersion: 26.50 ms
 peer dispersion: 10.00 ms
 reference time: 12:01:48.377 UTC Feb 2 2020(C7B15D2C.60A15981)
 synchronization state: clock synchronized
```

#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  ntp authentication-keyid 42 authentication-mode hmac-sha256 cipher %+%#JA!v6M22=Gg\{>U.lx%#)c%yY}0*"/`5mi><QS)L%+%#
  ntp refclock-master 2
  ntp authentication enable
  ntp server source-interface 100GE1/0/1
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 2.2.2.2 255.255.255.0
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  ntp authentication-keyid 42 authentication-mode hmac-sha256 cipher %+%#>hD8))_H-XZVut2u3!_0lq3,+Ph=:OE}pX;T2M'9%+%#
  ntp trusted authentication-keyid 42
  ntp unicast-server 2.2.2.2 authentication-keyid 42
  ntp authentication enable
  ntp server source-interface 100GE1/0/1
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.0.0.1 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.1.11 255.255.255.0
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  ntp authentication-keyid 42 authentication-mode hmac-sha256 cipher %+%#m:fVJfk*r&3x"1J`21^K`Y;LH;B+g(t2<ZX^}Q_~%+%#
  ntp trusted authentication-keyid 42
  ntp unicast-server 10.0.0.1 authentication-keyid 42
  ntp authentication enable
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.0.0.2 255.255.255.0
  #
  return
  ```
* DeviceD
  
  ```
  #
  sysname DeviceD
  #
  ntp authentication-keyid 42 authentication-mode hmac-sha256 cipher %+%#$\`_6BKWy1]kdR@=c;O@UX!)Vor5iYi|zIYEG_v5%+%#
  ntp trusted authentication-keyid 42
  ntp unicast-server 10.0.0.1 authentication-keyid 42
  ntp authentication enable
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.0.0.3 255.255.255.0
  #
  return
  ```