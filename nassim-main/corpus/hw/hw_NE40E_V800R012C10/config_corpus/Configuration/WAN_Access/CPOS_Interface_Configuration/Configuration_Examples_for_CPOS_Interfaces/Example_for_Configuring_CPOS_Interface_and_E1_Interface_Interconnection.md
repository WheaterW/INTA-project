Example for Configuring CPOS Interface and E1 Interface Interconnection
=======================================================================

This section provides an example on how to interconnect devices through CPOS interface and E1 interface, and how to configure MP-group interfaces for link bundling.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172364103__fig_dc_ne_cpos_cfg_001201), Device A and Device B need to communicate with each other through CPOS interface and E1 interfaces, and MP-group interfaces need to be configured for link bundling.

**Figure 1** Configuring CPOS interface and E1 Interface interconnection![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent CPOS 0/3/0, E1 0/2/0, and E1 0/2/1, respectively.


  
![](images/fig_dc_ne_cpos_cfg_001201.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a working mode for CPOS interfaces.
2. Configure MP-group interfaces and add the synchronous serial interfaces to the MP-group interfaces.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of MP-group interfaces

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The interface to be added to an MP-group interface must have the same slot number and card number as the MP-group interface.



#### Procedure

1. Configure a working mode for CPOS interfaces and create synchronous serial interfaces.
   
   
   
   # Create synchronous serial interfaces on the CPOS interface of Device A.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*DeviceA] controller cpos 0/3/0
   [*DeviceA-Cpos0/3/0] e1 1 unframed
   [*DeviceA-Cpos0/3/0] e1 2 unframed
   [*DeviceA-Cpos0/3/0] undo shutdown
   [*DeviceA-Cpos0/3/0] commit
   [~DeviceA-Cpos0/3/0] quit
   ```
   
   # # Create synchronous serial interfaces on the E1 interface of Device B.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*DeviceB] controller e1 0/2/0
   [*DeviceB-E10/2/0] using e1
   [*DeviceB-E10/2/0] undo shutdown
   [*DeviceB-E10/2/0] commit
   [~DeviceB-E10/2/0] quit
   [*DeviceB] controller e1 0/2/1
   [*DeviceB-E10/2/1] using e1
   [*DeviceB-E10/2/1] undo shutdown
   [*DeviceB-E10/2/1] commit
   [~DeviceB-E10/2/1] quit
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
   [~DeviceA] interface serial 0/3/0/1:0
   [~DeviceA-Serial0/3/0/1:0] link-protocol ppp
   [*DeviceA-Serial0/3/0/1:0] ppp mp mp-group 0/3/1
   [*DeviceA-Serial0/3/0/1:0] commit
   [~DeviceA-Serial0/3/0/1:0] quit
   [~DeviceA] interface serial 0/3/0/2:0
   [~DeviceA-Serial0/3/0/2:0] link-protocol ppp
   [*DeviceA-Serial0/3/0/2:0] ppp mp mp-group 0/3/1
   [*DeviceA-Serial0/3/0/2:0] commit
   [~DeviceA-Serial0/3/0/2:0] quit
   ```
   
   # Create an MP-group interface on Device B.
   
   ```
   [~DeviceB] interface mp-group 0/2/1
   [*DeviceB-Mp-group0/2/1] ip address 10.1.1.2 255.255.255.0
   [*DeviceB-Mp-group0/2/1] undo shutdown
   [*DeviceB-Mp-group0/2/1] commit
   [~DeviceB-Mp-group0/2/1] quit
   ```
   
   # Add the synchronous serial interfaces to the MP-group interface on Device B.
   
   ```
   [~DeviceB] interface serial 0/2/0:0
   [~DeviceB-Serial0/2/0:0] link-protocol ppp
   [*DeviceB-Serial0/2/0:0] ppp mp mp-group 0/2/1
   [*DeviceB-Serial0/2/0:0] commit
   [~DeviceB-Serial0/2/0:0] quit
   [~DeviceB] interface serial 0/2/1:0
   [~DeviceB-Serial0/2/1:0] link-protocol ppp
   [*DeviceB-Serial0/2/1:0] ppp mp mp-group 0/2/1
   [*DeviceB-Serial0/2/1:0] commit
   [~DeviceB-Serial0/2/1:0] quit
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
   e1 1 unframed
   e1 2 unframed
   undo shutdown
  #
  interface Mp-group0/3/1
   ip address 10.1.1.1 255.255.255.0
  #
  interface Serial0/3/0/1:0
   link-protocol ppp
   ppp mp Mp-group0/3/1
  #
  interface Serial0/3/0/2:0
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
  controller E1 0/2/0
   using e1
   undo shutdown
  #
  controller E1 0/2/1
   using e1
   undo shutdown
  #
  interface Mp-group0/2/1
   ip address 10.1.1.2 255.255.255.0
  #
  interface Serial0/2/0:0
   link-protocol ppp
   ppp mp Mp-group0/2/1
  #
  interface Serial0/2/1:0
   link-protocol ppp
   ppp mp Mp-group0/2/1
  #
  return
  ```