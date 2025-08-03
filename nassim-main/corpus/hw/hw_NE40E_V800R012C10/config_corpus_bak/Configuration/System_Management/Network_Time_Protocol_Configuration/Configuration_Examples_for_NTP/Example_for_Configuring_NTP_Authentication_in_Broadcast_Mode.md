Example for Configuring NTP Authentication in Broadcast Mode
============================================================

On a LAN, the device with high clock precision functions as the NTP server, and other devices are synchronized to the clock of the NTP server. In the broadcast mode, you do not need to specify a server for the client, and the client listens to packets sent from the broadcast server in real time.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001800928874__fig_dc_vrp_ntp_cfg_002901):

* DeviceC and DeviceD are on the same network segment.
* DeviceC functions as an NTP broadcast server, and its clock is a stratum 3 NTP master clock. Broadcast packets are sent from GE0/1/0.
* DeviceD listens to broadcast messages on GE0/1/0.
* NTP authentication needs to be enabled on DeviceC and DeviceD.

**Figure 1** Configuring NTP authentication in broadcast mode  
![](figure/en-us_image_0000001847727717.png)
![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 represents GE0/1/0.



#### Precautions

Before configuring a key on the client and server, ensure that the key already exists.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure DeviceC as an NTP broadcast server.
2. Configure DeviceD as an NTP broadcast client.
3. Configure NTP authentication on DeviceC and DeviceD.

#### Data Preparation

To complete the configuration, you need the following data:

* Interface IP addresses of Routers
* Stratum of the NTP master clock
* Authentication key and key ID. The HMAC-SHA256 algorithm is used to verify the key.

#### Procedure

1. Configure an IP address for each Router.
   
   
   
   Configure IP addresses based on [Figure 1](#EN-US_TASK_0000001800928874__fig_dc_vrp_ntp_cfg_002901). For configuration details, see Configuration Files.
2. Configure an NTP broadcast server and enable NTP authentication on it.
   
   
   
   # Set the local clock on DeviceC as a stratum 3 NTP master clock.
   
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
   [~DeviceC] ntp-service refclock-master 3
   ```
   
   # Specify a listening interface on DeviceC.
   
   ```
   [*DeviceC] ntp-service server source-interface gigabitethernet 0/1/0 
   ```
   
   # Enable NTP authentication.
   
   ```
   [*DeviceC] ntp-service authentication enable
   ```
   ```
   [*DeviceC] ntp-service authentication-keyid 16 authentication-mode hmac-sha256 cipher Hello123
   ```
   ```
   [*DeviceC] ntp-service reliable authentication-keyid 16
   ```
   
   # Configure DeviceC to be an NTP broadcast server. Broadcast packets are encrypted by using the authentication key ID 16 and then sent from GE0/1/0.
   
   ```
   [*DeviceC] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] ntp-service broadcast-server authentication-keyid 16
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceC-GigabitEthernet0/1/0] quit
   ```
3. Configure DeviceD as an NTP broadcast client which is on the same network segment as that of the NTP server.
   
   
   
   # Enable NTP authentication.
   
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
   [*DeviceD] ntp-service authentication-keyid 16 authentication-mode hmac-sha256 cipher Hello123
   ```
   ```
   [*DeviceD] ntp-service reliable authentication-keyid 16
   ```
   
   # Configure DeviceD as an NTP broadcast client. DeviceD listens to the broadcast packets on GE0/1/0.
   
   ```
   [*DeviceD] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] ntp-service broadcast-client
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceD-GigabitEthernet0/1/0] quit
   ```
   
   After the configurations are complete, the clock on DeviceD can be synchronized with the clock on DeviceC.
4. Verify the configuration.
   
   
   
   After completing the configurations, check that DeviceD can synchronize its clock with DeviceC.
   
   Check the NTP status on DeviceD. You can find that the clock status is **synchronized**. The stratum of the clock is 4, one stratum lower than that on DeviceC.
   
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
    clock offset: 0.0000 ms
   ```
   ```
    root delay: 0.00 ms
   ```
   ```
    root dispersion: 0.42 ms
   ```
   ```
    peer dispersion: 0.00 ms
   ```
   ```
    reference time: 12:17:21.773 UTC Mar 7 2006(C7B7F851.C5EAF25B)
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
  ntp-service authentication-keyid 16 authentication-mode hmac-sha256 cipher %#%#>hD8))_H-XZVut2u3!_0lq3,+Ph=:OE}pX;T2M'9%#%#
  ```
  ```
  ntp-service reliable authentication-keyid 16
  ```
  ```
  ntp-service refclock-master 3
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
   ip address 10.0.1.31 255.255.255.0
  ```
  ```
   ntp-service broadcast-server authentication-keyid 16
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
  ntp-service authentication-keyid 16 authentication-mode hmac-sha256 cipher %#%#m:fVJfk*r&3x"1J`21^K`Y;LH;B+g(t2<ZX^}Q_~%#%#
  ```
  ```
  ntp-service reliable authentication-keyid 16
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
   ip address 10.0.1.32 255.255.255.0
  ```
  ```
   ntp-service broadcast-client
  ```
  ```
  #
  ```
  ```
  Return
  ```