Example for Configuring MP Groups
=================================

When two devices connect to each other through E1 interfaces, these E1 interfaces can be added to MP groups to increase the available bandwidth. This section provides an example on how to configure MP groups.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172364199__fig_dc_vrp_mp_cfg_000701), Device A and Device B connect to each other through two pairs of E1 interfaces.

A single link sometimes cannot support data transmission when services are busy. To quickly, efficiently, and securely increase the available transmission bandwidth for data transmission, MP groups can be used.

**Figure 1** Adding E1 interfaces to MP groups![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, interface3, and interface4 represent E1 0/1/0, E1 0/1/1, E1 0/2/0, and E1 0/2/1respectively.


  
![](images/fig_dc_ne_mp_cfg_000701.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create MP-group interfaces.
2. Create synchronous serial interfaces and add the interfaces to the MP-group interfaces.
3. Restart all the interfaces to make the configuration take effect.


#### Data Preparation

To complete the configuration, you need the following data:

* IP address of the MP-group interface on Device A
* IP address of the MP-group interface on Device B
* E1 interface numbers of Device A
* E1 interface numbers of Device B

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The interface to be added to an MP-group interface must have the same slot number and card number as the MP-group interface.

The timeslot channels of the serial interfaces on Device A must be the same as those on Device B.



#### Procedure

1. Create MP-group interfaces.
   
   
   
   # Create an MP-group interface and configure an IP address for it on Device A.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface mp-group 0/1/1
   [*DeviceA-Mp-group0/1/1] ip address 10.1.1.1 255.255.255.0
   [*DeviceA-Mp-group0/1/1] shutdown
   [*DeviceA-Mp-group0/1/1] commit
   [~DeviceA-Mp-group0/1/1] quit
   ```
   
   
   
   # Create an MP-group interface and configure an IP address for it on Device B.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] interface mp-group 0/2/1
   [*DeviceB-Mp-group0/2/1] ip address 10.1.1.2 255.255.255.0
   [*DeviceB-Mp-group0/2/1] shutdown
   [*DeviceB-Mp-group0/2/1] commit
   [~DeviceB-Mp-group0/2/1] quit
   ```
2. Create synchronous serial interfaces and add the interfaces to the MP-group interfaces.
   
   
   
   # Configure E1 interfaces of Device A as synchronous serial interfaces and add them to the MP-group interface.
   
   ```
   [~DeviceA] controller e1 0/1/0
   [~DeviceA-E1 0/1/0] channel-set 1 timeslot-list 1-15
   [*DeviceA-E1 0/1/0] commit
   [~DeviceA-E1 0/1/0] quit
   [~DeviceA] controller e1 0/1/1
   [~DeviceA-E1 0/1/1] channel-set 1 timeslot-list 16-31
   [*DeviceA-E1 0/1/1] commit
   [~DeviceA-E1 0/1/1] quit
   [~DeviceA] interface serial 0/1/0:1
   [~DeviceA-Serial0/1/0:1] link-protocol ppp
   [*DeviceA-Serial0/1/0:1] ppp mp mp-group 0/1/1
   [*DeviceA-Serial0/1/0:1] commit
   [~DeviceA-Serial0/1/0:1] quit
   [~DeviceA] interface serial 0/1/1:1
   [~DeviceA-Serial0/1/1:1] link-protocol ppp
   [*DeviceA-Serial0/1/1:1] ppp mp mp-group 0/1/1
   [*DeviceA-Serial0/1/1:1] commit
   [~DeviceA-Serial0/1/1:1] quit
   ```
   
   
   
   # Configure E1 interfaces of Device B as synchronous serial interfaces and add them to the MP-group interface.
   
   ```
   [~DeviceB] controller e1 0/2/0
   [~DeviceB-E1 0/2/0] channel-set 1 timeslot-list 1-15
   [*DeviceB-E1 0/2/0] commit
   [~DeviceB-E1 0/2/0] quit
   [~DeviceB] controller e1 0/2/1
   [~DeviceB-E1 0/2/1] channel-set 1 timeslot-list 16-31
   [*DeviceB-E1 0/2/1] commit
   [~DeviceB-E1 0/2/1] quit
   [~DeviceB] interface serial 0/2/0:1
   [~DeviceB-Serial0/2/0:1] link-protocol ppp
   [*DeviceB-Serial0/2/0:1] ppp mp mp-group 0/2/1
   [*DeviceB-Serial0/2/0:1] commit
   [~DeviceB-Serial0/2/0:1] quit
   [~DeviceB] interface serial 0/2/1:1
   [~DeviceB-Serial0/2/1:1] link-protocol ppp
   [*DeviceB-Serial0/2/1:1] ppp mp mp-group 0/2/1
   [*DeviceB-Serial0/2/1:1] commit
   [~DeviceB-Serial0/2/1:1] quit
   ```
3. Restart all the interfaces to make the configuration take effect.
   
   
   
   # Restart the synchronous serial and MP-group interfaces on Device A.
   
   ```
   [~DeviceA] interface serial 0/1/0:1
   [~DeviceA-Serial0/1/0:1] undo shutdown
   [*DeviceA-Serial0/1/0:1] commit
   [~DeviceA-Serial0/1/0:1] quit
   [~DeviceA] interface serial 0/1/1:1
   [~DeviceA-Serial0/1/1:1] undo shutdown
   [*DeviceA-Serial0/1/1:1] commit
   [~DeviceA-Serial0/1/1:1] quit
   [~DeviceA] interface mp-group 0/1/1
   [~DeviceA-Mp-group0/1/1] undo shutdown
   [*DeviceA-Mp-group0/1/1] commit
   [~DeviceA-Mp-group0/1/1] quit
   ```
   
   
   
   # Restart the synchronous serial and MP-group interfaces on Device B.
   
   ```
   [~DeviceB] interface serial 0/2/0:1
   [~DeviceB-Serial0/2/0:1] undo shutdown
   [*DeviceB-Serial0/2/0:1] commit
   [~DeviceB-Serial0/2/0:1] quit
   [~DeviceB] interface serial 0/2/1:1
   [~DeviceB-Serial0/2/1:1] undo shutdown
   [*DeviceB-Serial0/2/1:1] commit
   [~DeviceB-Serial0/2/1:1] quit
   [~DeviceB] interface mp-group 0/2/1
   [~DeviceB-Mp-group0/2/1] undo shutdown
   [*DeviceB-Mp-group0/2/1] commit
   [~DeviceB-Mp-group0/2/1] quit
   ```
4. Verify the configuration.
   
   
   
   # On Device A, check information about the MP-group interface and statistics about the packets sent and received by the MP-group interface.
   
   ```
   [~DeviceA] display ppp mp interface mp-group 0/1/1
   ```
   ```
   Mp-group is Mp-group0/1/1
    ===========Sublinks status begin======
    Serial0/1/0:1 physical UP,protocol UP
    Serial0/1/1:1 physical UP,protocol UP
    ===========Sublinks status end========
    Bundle Multilink, 2 member, slot 1, Master link is Mp-group0/1/1
     0 lost fragments, 0 reordered, 0 unassigned, 0 interleaved,
    sequence 0/0 rcvd/sent
    The bundled son channels are:
         Serial0/1/0:1
         Serial0/1/1:1 
   ```
   
   # On Device B, check information about the MP-group interface and statistics about the packets sent and received by the MP-group interface.
   
   ```
   [~DeviceB] display ppp mp interface mp-group 0/2/1
   ```
   ```
   Mp-group is Mp-group0/2/1
    ===========Sublinks status begin======
    Serial0/2/0:1 physical UP,protocol UP
    Serial0/2/1:1 physical UP,protocol UP
    ===========Sublinks status end========
    Bundle Multilink, 2 member, slot 2, Master link is Mp-group0/2/1
     0 lost fragments, 0 reordered, 0 unassigned, 0 interleaved,
    sequence 0/0 rcvd/sent
    The bundled son channels are:
         Serial0/2/0:1
         Serial0/2/1:1 
   ```
   
   # On Device A, ping the IP address of MP-group 0/2/1 on Device B. The command output shows that the ping is successful.
   
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
   undo shutdown
   link-protocol ppp
   ppp mp Mp-group0/1/1
  #
  controller E1 0/1/1
   channel-set 1 timeslot-list 16-31
  #
  interface Serial0/1/1:1
   undo shutdown
   link-protocol ppp
   ppp mp Mp-group0/1/1  
  #
  interface Mp-group0/1/1
   undo shutdown
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
   undo shutdown
   link-protocol ppp
   ppp mp Mp-group0/2/1
  #
  controller E1 0/2/1
   channel-set 1 timeslot-list 16-31
  #
  interface Serial0/2/1:1
   undo shutdown
   link-protocol ppp
   ppp mp Mp-group0/2/1  
  #
  interface Mp-group0/2/1
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
  #
  return
  ```