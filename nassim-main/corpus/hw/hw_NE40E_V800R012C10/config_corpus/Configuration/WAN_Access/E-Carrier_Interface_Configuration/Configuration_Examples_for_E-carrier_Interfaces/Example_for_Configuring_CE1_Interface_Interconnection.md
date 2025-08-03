Example for Configuring CE1 Interface Interconnection
=====================================================

This section provides an example for interconnecting devices through CE1 interfaces.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172364058__fig_dc_vrp_mp_cfg_000701), Device A and Device B need to communicate with each other through CE1 interfaces.

**Figure 1** CE1 interface interconnection![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent CE1 0/1/0 and CE1 0/2/0, respectively.


  
![](images/fig_dc_ne_ce1_cfg_000701.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create synchronous serial interfaces.
2. Create MP-group interfaces.
3. Bundle the synchronous serial interfaces into the MP-group interfaces.
4. Restart all the interfaces to make the configuration take effect.


#### Data Preparation

To complete the configuration, you need the following data:

* CE1 interface number of Device A
* CE1 interface number of Device B
* MP-group interface number of Device A
* MP-group interface number of Device B

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The timeslot channels of the serial interfaces on Device A must be the same as those on Device B.



#### Procedure

1. Create synchronous serial interfaces.
   
   
   
   # Configure the CE1 interface on Device A as a synchronous serial interface.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] controller e1 0/1/0
   [~DeviceA-E1 0/1/0] channel-set 1 timeslot-list 1-15
   [*DeviceA-E1 0/1/0] commit
   [~DeviceA-E1 0/1/0] quit
   ```
   
   # Configure the CE1 interface on Device B as a synchronous serial interface.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] controller e1 0/2/0
   [~DeviceB-E1 0/2/0] channel-set 1 timeslot-list 1-15
   [*DeviceB-E1 0/2/0] commit
   [~DeviceB-E1 0/2/0] quit
   ```
2. Create MP-group interfaces.
   
   
   
   # Create an MP-group interface on Device A.
   
   ```
   [~DeviceA] interface mp-group 0/1/1
   [*DeviceA-Mp-group0/1/1] discriminator
   [*DeviceA-Mp-group0/1/1] ip address 10.1.1.1 255.255.255.0
   [*DeviceA-Mp-group0/1/1] undo shutdown
   [*DeviceA-Mp-group0/1/1] quit
   [*DeviceA] commit
   ```
   
   # Create an MP-group interface on Device B.
   
   ```
   [~DeviceA] interface mp-group 0/2/1
   [*DeviceA-Mp-group0/2/1] discriminator
   [*DeviceA-Mp-group0/2/1] ip address 10.1.1.2 255.255.255.0
   [*DeviceA-Mp-group0/2/1] undo shutdown
   [*DeviceA-Mpgroup0/2/1] quit
   [*DeviceA] commit
   ```
3. Bundle the synchronous serial interfaces into the MP-group interfaces.
   
   
   
   # Bundle the synchronous serial interface into the MP-group interface on Device A.
   
   ```
   [~DeviceA] interface serial 0/1/0:1
   [~DeviceA-Serial0/1/0:1] link-protocol ppp
   [*DeviceA-Serial0/1/0:1] ppp mp mp-group 0/1/1
   [*DeviceA-Serial0/1/0:1] ip address 10.1.1.1 255.255.255.0
   [~DeviceA-Serial0/1/0:1] quit
   [*DeviceA] commit
   ```
   
   
   
   # Bundle the synchronous serial interface into the MP-group interface on Device B.
   
   ```
   [~DeviceB] interface serial 0/2/0:1
   [~DeviceB-Serial0/2/0:1] link-protocol ppp
   [*DeviceB-Serial0/2/0:1] ppp mp mp-group 0/2/1
   [*DeviceB-Serial0/2/0:1] ip address 10.1.1.2 255.255.255.0
   [~DeviceB-Serial0/2/0:1] quit
   [*DeviceB] commit
   ```
4. Restart all the interfaces to make the configuration take effect.
   
   
   
   # Restart the synchronous serial interface on Device A.
   
   ```
   [~DeviceA] interface serial 0/1/0:1
   [~DeviceA-Serial0/1/0:1] undo shutdown
   [*DeviceA-Serial0/1/0:1] commit
   [~DeviceA-Serial0/1/0:1] quit
   ```
   
   
   
   # Restart the synchronous serial interface on Device B.
   
   ```
   [~DeviceB] interface serial 0/2/0:1
   [~DeviceB-Serial0/2/0:1] undo shutdown
   [*DeviceB-Serial0/2/0:1] commit
   [~DeviceB-Serial0/2/0:1] quit
   ```
5. Verify the configuration.
   
   
   
   # On Device A, ping the IP address of the synchronous serial interface on Device B. The command output shows that the ping is successful.
   
   ```
   [~DeviceA] ping 10.1.1.2
   ```
   ```
   PING 10.1.1.2: 56  data bytes, press CTRL_C to break
       Reply from 10.1.1.2: bytes=56 Sequence=1 ttl=255 time=29 ms
       Reply from 10.1.1.2: bytes=56 Sequence=2 ttl=255 time=31 ms
       Reply from 10.1.1.2: bytes=56 Sequence=3 ttl=255 time=29 ms
       Reply from 10.1.1.2: bytes=56 Sequence=4 ttl=255 time=30 ms
       Reply from 10.1.1.2: bytes=56 Sequence=5 ttl=255 time=30 ms
     --- 10.1.1.2 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 29/29/31 ms
   ```

#### Configuration Files

* Device A configuration file
  
  ```
  #
  sysname DeviceA
  #
  controller E1 0/1/0
   channel-set 1 timeslot-list 1-15
  #
  interface Serial0/1/0:1
   link-protocol ppp
   ppp mp mp-group 0/1/1
   undo shutdown
  #
  interface mp-group 0/1/1
   discriminator
   ip address 10.1.1.1 255.255.255.0
  #
  return
  ```
* Device B configuration file
  
  ```
  #
  sysname DeviceB
  #
  controller E1 0/2/0
   channel-set 1 timeslot-list 1-15
  #
  interface Serial0/2/0:1
   link-protocol ppp
   ppp mp mp-group 0/2/1
   undo shutdown
  #
  interface mp-group 0/2/1
   discriminator
   ip address 10.1.1.2 255.255.255.0
  #
  return
  ```