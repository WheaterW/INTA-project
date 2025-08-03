Example for Configuring NTP Authentication in Client/Server Mode
================================================================

You must enable NTP authentication for the NTP client, and then specify the IP address of the NTP server and the authentication key to be sent to the NTP server. Otherwise, if NTP authentication fails, then no synchronization will take place. To implement authentication successfully, configure both the server and the client.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001847727701__fig_dc_vrp_ntp_cfg_002701):

* DeviceA functions as a unicast NTP server. The clock on it functions as a stratum 2 NTP master clock.
* DeviceB functions as a unicast NTP client. The client synchronizes clock with DeviceA.
* DeviceC and DeviceD function as NTP clients of DeviceB.
* Enable NTP authentication on all the Routers.

**Figure 1** Configuring the client/server mode  
![](figure/en-us_image_0000001801088666.png)
![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent GE0/1/0 and GE0/2/0, respectively.



#### Precautions

* You must enable NTP authentication for the NTP client, and then specify the IP address of the NTP server and the authentication key to be sent to the NTP server. Otherwise, clock synchronization is implemented without NTP authentication.
* Configure the same authentication key on the NTP server and NTP client and declare the authentication key on the client as reliable. Otherwise, the NTP authentication fails.
* Configure both the server and the client to implement authentication successfully.
* Enable NTP authentication on all the Routers.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure DeviceA as an NTP server and configure a master clock on it.
2. Configure DeviceB as an NTP client and synchronize its clock with the clock of DeviceA.
3. Configure DeviceC and DeviceD as NTP clients to synchronize their clocks with the clock of DeviceB.
4. Enable NTP authentication on all the Routers.

#### Data Preparation

To complete the configuration, you need the following data:

* IP address of the reference clock
* Stratum of the NTP master clock
* Key ID and key. The HMAC-SHA256 algorithm is used to verify the key.

#### Procedure

1. Configure available routes among the devices. For configuration details, see [Configuration Files](#EN-US_TASK_0000001847727701__example71152866214019) in this section.
2. Configure the IP addresses based on [Figure 1](#EN-US_TASK_0000001847727701__fig_dc_vrp_ntp_cfg_002701) so that DeviceA, DeviceB, DeviceC, and DeviceD are routable. For configuration details, see Configuration Files.
3. Configure an NTP master clock and listening interface on DeviceA and enable NTP authentication.
   
   
   
   # On DeviceA, set its local clock as an NTP master clock with stratum 2.
   
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
   [~DeviceA] ntp-service refclock-master 2
   ```
   
   # Specify a listening interface on DeviceA.
   
   ```
   [~DeviceA] ntp-service server source-interface gigabitethernet 0/1/0 
   ```
   
   # On DeviceA, enable NTP authentication. Configure the authentication key and declare the key to be reliable.
   
   ```
   [*DeviceA] ntp-service authentication enable
   ```
   ```
   [*DeviceA] ntp-service authentication-keyid 42 authentication-mode hmac-sha256 cipher Hello123
   ```
   ```
   [*DeviceA] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Authentication keys configured on the server and the client must be the same.
4. Configure an NTP master clock and listening interface on DeviceB and enable NTP authentication.
   
   
   
   # On DeviceB, enable NTP authentication. Configure the authentication key and declare the key to be reliable.
   
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
   [~DeviceB] undo ntp-service server disable
   ```
   ```
   [~DeviceB] ntp-service authentication enable
   ```
   ```
   [*DeviceB] ntp-service authentication-keyid 42 authentication-mode hmac-sha256 cipher Hello123
   ```
   ```
   [*DeviceB] ntp-service reliable authentication-keyid 42
   ```
   
   # Specify a listening interface on DeviceB.
   
   ```
   [*DeviceB] ntp-service server source-interface gigabitethernet 0/1/0 
   ```
   
   # Specify DeviceA to be the NTP server of DeviceB and use the authentication key.
   
   ```
   [*DeviceB] ntp-service unicast-server 2.2.2.2 authentication-keyid 42
   ```
   ```
   [*DeviceB] commit
   ```
5. Configure DeviceC as an NTP client and enable NTP authentication.
   
   
   
   # On DeviceC, configure DeviceB to be its NTP server.
   
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
   [~DeviceC] undo ntp-service disable
   ```
   ```
   [~DeviceC] ntp-service authentication enable
   ```
   ```
   [*DeviceC] ntp-service authentication-keyid 42 authentication-mode hmac-sha256 cipher Hello123
   ```
   ```
   [*DeviceC] ntp-service reliable authentication-keyid 42
   ```
   ```
   [*DeviceC] ntp-service unicast-server 10.0.0.1 authentication-keyid 42
   ```
   ```
   [*DeviceC] commit
   ```
6. Configure DeviceD as an NTP client and enable NTP authentication.
   
   
   
   # On DeviceD, configure DeviceB to be its NTP server.
   
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
   [~DeviceD] undo ntp-service disable
   ```
   ```
   [~DeviceD] ntp-service authentication enable
   ```
   ```
   [*DeviceD] ntp-service authentication-keyid 42 authentication-mode hmac-sha256 cipher Hello123
   ```
   ```
   [*DeviceD] ntp-service reliable authentication-keyid 42
   ```
   ```
   [*DeviceD] ntp-service unicast-server 10.0.0.1 authentication-keyid 42
   ```
   ```
   [*DeviceD] commit
   ```
7. Verify the configuration.
   
   
   
   After the configurations are complete, the clock on DeviceB can be synchronized with the clock on DeviceA.
   
   Check the NTP status on DeviceB. You can find that the clock status is **synchronized**. The stratum of the clock is 3, one stratum lower than that on DeviceA.
   
   ```
   [~DeviceB] display ntp-service status
   ```
   ```
    clock status: synchronized
   ```
   ```
    clock stratum: 3
   ```
   ```
    reference clock ID: 2.2.2.2
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
    clock offset: 3.8128 ms
   ```
   ```
    root delay: 31.26 ms
   ```
   ```
    root dispersion: 74.20 ms
   ```
   ```
    peer dispersion: 34.30 ms
   ```
   ```
    reference time: 11:55:56.833 UTC Mar 2 2006(C7B15BCC.D5604189)
   ```
   ```
    synchronization state: clock synchronized
   ```
   
   After the configurations are complete, the clock on DeviceC can be synchronized with the clock on DeviceB.
   
   Check the NTP status on DeviceC. You can find that the clock status is **synchronized**. The stratum of the clock is 4, one stratum lower than that on DeviceB.
   
   ```
   [~DeviceC] display ntp-service status
   ```
   ```
    clock status: synchronized
   ```
   ```
    clock stratum: 4
   ```
   ```
    reference clock ID: 10.0.0.1
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
    clock offset: 3.8128 ms
   ```
   ```
    root delay: 31.26 ms
   ```
   ```
    root dispersion: 74.20 ms
   ```
   ```
    peer dispersion: 34.30 ms
   ```
   ```
    reference time: 11:55:56.833 UTC Mar 2 2006(C7B15BCC.D5604189)
   ```
   ```
    synchronization state: clock synchronized
   ```
   
   Check the NTP status on DeviceD. You can find that the clock status is **synchronized**. The stratum of the clock is 4, one stratum lower than that on DeviceB.
   
   ```
   [~DeviceD] display ntp-service status
   ```
   ```
    clock status: synchronized
   ```
   ```
    clock stratum: 4
   ```
   ```
    reference clock ID: 10.0.0.1
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
    clock offset: 3.8128 ms
   ```
   ```
    root delay: 31.26 ms
   ```
   ```
    root dispersion: 74.20 ms
   ```
   ```
    peer dispersion: 34.30 ms
   ```
   ```
    reference time: 11:55:56.833 UTC Mar 2 2006(C7B15BCC.D5604189)
   ```
   ```
    synchronization state: clock synchronized
   ```
   
   Check the NTP status on DeviceA.
   
   ```
   [~DeviceA] display ntp-service status
   ```
   ```
    clock status: synchronized
   ```
   ```
    clock stratum: 2
   ```
   ```
    reference clock ID: LOCAL(0)
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
    clock offset: 0.0000 ms
   ```
   ```
    root delay: 0.00 ms
   ```
   ```
    root dispersion: 26.50 ms
   ```
   ```
    peer dispersion: 10.00 ms
   ```
   ```
    reference time: 12:01:48.377 UTC Mar 2 2006(C7B15D2C.60A15981)
   ```
   ```
    synchronization state: clock synchronized
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
  ```
  ```
  undo ntp-service server disable
  ```
  ```
  ntp-service authentication-keyid 42 authentication-mode hmac-sha256 cipher %#%#JA!v6M22=Gg\{>U.lx%#)c%yY}0*"/`5mi><QS)L%#%#
  ```
  ```
  ntp-service refclock-master 2
  ```
  ```
  ntp-service authentication enable
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
   ip address 2.2.2.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 2.2.2.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceB configuration file
  
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
  undo ntp-service server disable
  ```
  ```
  ntp-service authentication-keyid 42 authentication-mode hmac-sha256 cipher %#%#>hD8))_H-XZVut2u3!_0lq3,+Ph=:OE}pX;T2M'9%#%#
  ```
  ```
  ntp-service reliable authentication-keyid 42
  ```
  ```
  ntp-service unicast-server 2.2.2.2 authentication-keyid 42
  ```
  ```
  ntp-service authentication enable
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
   ip address 10.0.0.1 255.255.255.0
  ```
  ```
  interface GigabitEthernet0/2/0
   undo shutdown
  ```
  ```
   ip address 10.1.1.11 255.255.255.0
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 10.1.1.0 0.0.0.255
  ```
  ```
    network 10.0.0.0 0.0.0.255
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
  ntp-service authentication-keyid 42 authentication-mode hmac-sha256 cipher %#%#m:fVJfk*r&3x"1J`21^K`Y;LH;B+g(t2<ZX^}Q_~%#%#
  ```
  ```
  ntp-service reliable authentication-keyid 42
  ```
  ```
  ntp-service unicast-server 10.0.0.1 authentication-keyid 42
  ```
  ```
  ntp-service authentication enable
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
   ip address 10.0.0.2 255.255.255.0
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
  ntp-service authentication-keyid 42 authentication-mode hmac-sha256 cipher %#%#$\`_6BKWy1]kdR@=c;O@UX!)Vor5iYi|zIYEG_v5%#%#
  ```
  ```
  ntp-service reliable authentication-keyid 42
  ```
  ```
  ntp-service unicast-server 10.0.0.1 authentication-keyid 42
  ```
  ```
  ntp-service authentication enable
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
   ip address 10.0.0.3 255.255.255.0
  ```
  ```
  #
  ```
  ```
  return
  ```