Example for Configuring CPOS Interface Interconnection
======================================================

This section provides an example on how to interconnect devices through CPOS interfaces and how to configure MP-group interfaces for link bundling.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172364100__fig_dc_vrp_cpos_cfg_001001), Device A and Device B need to communicate with each other through CPOS interfaces, and MP-group interfaces need to be configured for link bundling.

**Figure 1** Configuring CPOS interface interconnection![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent CPOS 0/3/0 and CPOS 0/2/9, respectively.


  
![](images/fig_dc_ne_cpos_cfg_001001.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a working mode for CPOS interfaces and channelize them into synchronous serial interfaces.
2. Configure MP-group interfaces and add the synchronous serial interfaces to the MP-group interfaces.

#### Data Preparation

To complete the configuration, you need the following data:

* Channel number and timeslot number of each E1 channel
* IP addresses of MP-group interfaces

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The interface to be added to an MP-group interface must have the same slot number and card number as the MP-group interface.

The timeslot channels of the serial interfaces on Device A must be the same as those on Device B.



#### Procedure

1. Configure a working mode for CPOS interfaces and channelize them into synchronous serial interfaces.
   
   
   
   # Create synchronous serial interfaces on the CPOS interface of Device A.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] controller cpos 0/3/0
   [~DeviceA-Cpos0/3/0] e1 1 channel-set 1 timeslot-list 1-15
   [*DeviceA-Cpos0/3/0] e1 2 channel-set 1 timeslot-list 16-31
   [*DeviceA-Cpos0/3/0] undo shutdown
   [*DeviceA-Cpos0/3/0] commit
   [~DeviceA-Cpos0/3/0] quit
   ```
   
   # Create synchronous serial interfaces on the CPOS interface of Device B.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] controller cpos 0/2/9
   [~DeviceB-Cpos0/2/9] e1 1 channel-set 1 timeslot-list 1-15
   [*DeviceB-Cpos0/2/9] e1 2 channel-set 1 timeslot-list 16-31
   [*DeviceB-Cpos0/2/9] undo shutdown
   [*DeviceB-Cpos0/2/9] commit
   [~DeviceB-Cpos0/2/9] quit
   ```
2. Configure MP-group interfaces and add the synchronous serial interfaces to the MP-group interfaces.
   
   
   
   # Create an MP-group interface on Device A.
   
   ```
   [~DeviceA] interface mp-group 0/3/1
   [*DeviceA-Mp-group0/3/1] ip address 10.1.1.1 255.255.255.0
   [*DeviceA-Mp-group0/3/1] undo shutdown
   [*DeviceA-Mp-group0/3/1] commit
   [~DeviceA-Mp-group0/3/1] quit
   ```
   
   # Add the synchronous serial interfaces to the MP-group interface on Device A.
   
   ```
   [~DeviceA] interface serial 0/3/0/1:1
   [~DeviceA-Serial0/3/0/1:1] link-protocol ppp
   [*DeviceA-Serial0/3/0/1:1] ppp mp mp-group 0/3/1
   [*DeviceA-Serial0/3/0/1:1] commit
   [~DeviceA-Serial0/3/0/1:1] quit
   [~DeviceA] interface serial 0/3/0/2:1
   [~DeviceA-Serial0/3/0/2:1] link-protocol ppp
   [*DeviceA-Serial0/3/0/2:1] ppp mp mp-group 0/3/1
   [*DeviceA-Serial0/3/0/2:1] commit
   [~DeviceA-Serial0/3/0/2:1] quit
   ```
   
   # Create an MP-group interface on Device B.
   
   ```
   [~DeviceB] interface mp-group 0/2/10
   [*DeviceB-Mp-group0/2/10] ip address 10.1.1.2 255.255.255.0
   [*DeviceB-Mp-group0/2/10] undo shutdown
   [*DeviceB-Mp-group0/2/10] commit
   [~DeviceB-Mp-group0/2/10] quit
   ```
   
   # Add the synchronous serial interfaces to the MP-group interface on Device B.
   
   ```
   [~DeviceB] interface serial 0/2/9/1:1
   [~DeviceB-Serial0/2/9/1:1] link-protocol ppp
   [*DeviceB-Serial0/2/9/1:1] ppp mp mp-group 0/2/10
   [*DeviceB-Serial0/2/9/1:1] commit
   [~DeviceB-Serial0/2/9/1:1] quit
   [~DeviceB] interface serial 0/2/9/2:1
   [~DeviceB-Serial0/2/9/2:1] link-protocol ppp
   [*DeviceB-Serial0/2/9/2:1] ppp mp mp-group 0/2/10
   [*DeviceB-Serial0/2/9/2:1] commit
   [~DeviceB-Serial0/2/9/2:1] quit
   ```
3. Verify the configuration.
   
   
   
   # On Device A, ping the IP address of the MP-group interface on Device B. The command output shows that the ping is successful.
   
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
  controller Cpos0/3/0
   e1 1 channel-set 1 timeslot-list 1-15
   e1 2 channel-set 1 timeslot-list 16-31
   undo shutdown
  #
  interface Mp-group0/3/1
   ip address 10.1.1.1 255.255.255.0
  #
  interface Serial0/3/0/1:1
   link-protocol ppp
   ppp mp Mp-group0/3/1
  #
  interface Serial0/3/0/2:1
   link-protocol ppp
   ppp mp Mp-group0/3/1
  #
  return
  ```
* Device B configuration file
  
  ```
  #
  sysname DeviceB
  #
  controller Cpos0/2/9
   e1 1 channel-set 1 timeslot-list 1-15
   e1 2 channel-set 1 timeslot-list 16-31
   undo shutdown
  #
  interface Mp-group0/2/10
   ip address 10.1.1.2 255.255.255.0
  #
  interface Serial0/2/9/1:1
   link-protocol ppp
   ppp mp Mp-group0/2/10
  #
  interface Serial0/2/9/2:1
   link-protocol ppp
   ppp mp Mp-group0/2/10
  #
  return
  ```