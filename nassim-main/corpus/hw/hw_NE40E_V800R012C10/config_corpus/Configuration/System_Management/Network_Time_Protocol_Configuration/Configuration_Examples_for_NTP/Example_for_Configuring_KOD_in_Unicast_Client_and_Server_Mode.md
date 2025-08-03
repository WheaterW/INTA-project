Example for Configuring KOD in Unicast Client/Server Mode
=========================================================

Example for Configuring KOD in Unicast Client/Server Mode

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001801088622__fig_dc_vrp_ntp_cfg_002701):

* DeviceA functions as a unicast NTP server. The clock on it functions as a stratum 2 NTP master clock.
* DeviceB functions as a unicast NTP client. Its clock needs to be synchronized with the clock on DeviceA.
* DeviceC and DeviceD function as NTP clients of DeviceB.
* NTP authentication needs to be enabled.
* Enable KOD on DeviceA so that DeviceA can perform access control when it receives a large number of access packets and cannot bear the load.

**Figure 1** Configuring KOD in unicast client/server mode  
![](figure/en-us_image_0000001801088666.png)
![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent GE0/1/0 and GE0/2/0, respectively.



#### Precautions

* Before configuring a key on the client and server, ensure that the key already exists.
* The authentication key must be reliable on both the client and server. Authentication must be enabled on the client.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure DeviceA as an NTP server and configure a master clock on it.
2. Configure DeviceB as an NTP client and synchronize its clock with the clock of DeviceA.
3. Configure DeviceC and DeviceD as NTP clients to synchronize their clocks with the clock of DeviceB.
4. Enable NTP authentication on all the Devices.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* You must enable NTP authentication on the client prior to specifying the IP address of the NTP server and the authentication key to be sent to the server. Otherwise, clock synchronization is implemented without NTP authentication.
* To implement authentication successfully, configure both the server and the client.


#### Data Preparation

To complete the configuration, you need the following data:

* IP address of the reference clock
* Stratum of the NTP master clock
* Authentication key and its ID. The HMAC-SHA256 algorithm is used to verify the key.
* Password

#### Procedure

1. Configure the IP addresses based on [Figure 1](#EN-US_TASK_0000001801088622__fig_dc_vrp_ntp_cfg_002701) so that DeviceA, DeviceB, DeviceC, and DeviceD are routable. For configuration details, see Configuration Files.
2. Configure an NTP master clock and listening interfaces on DeviceA and enable NTP authentication.
   
   
   
   # Set the local clock on DeviceA as a stratum 2 NTP master clock.
   
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
   [~DeviceA] ntp-service refclock-master 2
   ```
   
   # Specify a listening interface on DeviceA.
   
   ```
   [~DeviceA] ntp-service server source-interface gigabitethernet 0/1/0 
   ```
   
   # Enable NTP authentication, configure an authentication key, and declare the key to be reliable.
   
   ```
   [*DeviceA] ntp-service authentication enable
   ```
   ```
   [*DeviceA] ntp-service authentication-keyid 42 authentication-mode hmac-sha256 cipher Hello123
   ```
   ```
   [*DeviceA] ntp-service reliable authentication-keyid 42
   ```
   ```
   [*DeviceA] commit
   ```
   
   Note that authentication keys configured on the server and the client must be the same.
   
   # Configure an ACL rule.
   ```
   [~DeviceA] acl 2000
   ```
   ```
   [*DeviceA-acl4-basic-2000] rule 2000 permit source 10.1.1.11 0
   ```
   ```
   [*DeviceA-acl4-basic-2000] commit
   ```
   ```
   [~DeviceA-acl4-basic-2000] quit
   ```
   
   # Configure access control.
   
   ```
   [~DeviceA] ntp-service access limited 2000
   ```
   
   # Configure the minimum and average intervals for receiving NTP packets.
   
   ```
   [*DeviceA] ntp-service discard min-interval 4 avg-interval 4
   ```
   
   # Enable KOD.
   
   ```
   [*DeviceA] ntp-service kod-enable
   ```
   ```
   [*DeviceA] commit
   ```
3. Configure an NTP master clock and listening interfaces on DeviceB and enable NTP authentication.
   
   
   
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
4. On DeviceC, configure DeviceB to be its NTP server.
   
   
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
5. On DeviceD, configure DeviceB to be its NTP server.
   
   
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
6. Verify the configuration.
   
   
   
   After completing the configurations, check that the clock on DeviceB can be synchronized with the clock on DeviceA.
   
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
    synchronization state: spike (clock will be set in 1010 secs)
   ```
   
   After completing the configurations, check that the clock on DeviceC can be synchronized with the clock on DeviceB.
   
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
    synchronization state: spike (clock will be set in 1010 secs)
   ```
   
   View the NTP status on DeviceD. The command output shows that the clock state is **synchronized** and the stratum of the clock on DeviceD is 4, one stratum lower than that on DeviceB.
   
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
    synchronization state: spike (clock will be set in 1010 secs)
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
    synchronization state: spike (clock will be set in 1010 secs)
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
  ntp-service authentication enable
  ```
  ```
  ntp-service authentication-keyid 42 authentication-mode hmac-sha256 cipher %#%#JA!v6M22=Gg\{>U.lx%#)c%yY}0*"/`5mi><QS)L%#%#
  ```
  ```
  ntp-service reliable authentication-keyid 42
  ```
  ```
  ntp-service refclock-master 2
  ```
  ```
  acl 2000
  ```
  ```
   rule 2000 permit source 10.1.1.11 0
  ```
  ```
  ntp-service access limited 2000
  ```
  ```
  ntp-service discard min-interval 4 avg-interval 4
  ```
  ```
  ntp-service server source-interface gigabitethernet 0/1/0 
  ```
  ```
  ntp-service kod-enable
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
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.0.1.1 255.255.255.0
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
    network 10.0.1.0 0.0.0.255
  ```
  ```
    network 10.0.0.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  ntp-service authentication enable
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
  ntp-service server source-interface gigabitethernet 0/1/0 
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
  ntp-service authentication enable
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
   ip address 10.0.0.3 255.255.255.0
  ```
  ```
  #
  ```
  ```
  ntp-service authentication enable
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
  #
  ```
  ```
  return
  ```