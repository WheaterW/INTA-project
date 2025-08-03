Example for Configuring a Device to Obtain Forwarded Packet Headers
===================================================================

This section provides an example for configuring a device to obtain forwarded packet headers.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172372306__fig_dc_vrp_capture-packet_cfg_0008), PC1 accesses the Internet through DeviceA and DeviceB. If PC1 encounters mosaic in video display, DeviceB may have reported error data. In this case, you need to obtain the original packet headers for fault locating. To achieve this, configure the inbound interface GE0/1/0 on DeviceA to obtain the headers of packets forwarded from DeviceB.

**Figure 1** Configuring a device to obtain forwarded packet headers![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent GE0/1/0, GE0/1/1, and GE0/1/2, respectively.


  
![](figure/en-us_image_0000001963187789.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an ACL rule.
2. Configure the function of obtaining forwarded packet headers.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of interfaces
* ACL number
* Timeout period for obtaining packet headers, maximum number of packet headers that can be obtained, and name of the file saving obtained packet headers


#### Procedure

1. Configure interface IP addresses and routing protocols.
2. Configure an ACL rule.
   
   
   ```
   <DeviceA> system-view
   ```
   ```
   [DeviceA] acl number 2001
   ```
   ```
   [DeviceA-acl4-basic-2001] rule permit source 10.1.1.1 0
   ```
   ```
   [DeviceA-acl4-basic-2001] commit
   ```
   ```
   [DeviceA-acl4-basic-2001] quit
   ```
   ```
   [DeviceA] quit
   ```
3. Configure the function of obtaining forwarded packet headers.
   
   
   ```
   <DeviceA> capture-packet forwarding interface gigabitethernet 0/1/0 inbound acl 2001 time-out 3600 packet-len 62 packet-num 900
   ```
4. View the file saving obtained packet headers.
   
   
   
   # View the packet header obtaining configuration.
   
   ```
   <DeviceA> display capture-packet config-state
   ```
   ```
   Capture-Packet Index 1
   Type        : forwarding
   Interface   : GigabitEthernet
   Direction   : inbound
   ACL         : 2001
   File Name   : cfcard:/capture_fwd_GigabitEthernet3.0.0_2012-05-03-14-25-42.cap
   Time-out    : 3600 seconds
   Packet-num  : 900
   Packet-len  : 62
   BufferOnly  : disabled 
   ```
   
   
   
   # View the file saving obtained packet headers.
   
   ```
   <DeviceA> display capture-packet file cfcard:/capture_fwd_GigabitEthernet3.0.0_2012-05-03-14-25-42.cap
   ```
   ```
   a1 b2 c3 d4 00 02 00 04 00 00 00 00 00 00 00 00
   00 00 ff ff 00 00 00 09 4d 10 36 db 00 0a d5 81
   00 00 00 0c 00 00 00 0c ff 03 c0 21 09 9d 00 08
   8a 8c bc c3 4d 10 36 db 00 0a d6 ae
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  #
  acl number 2001
   rule 5 permit source 10.1.1.1 0
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.2.1 255.255.255.0
  #
  ospf 1
   area 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.1.2.0 0.0.0.255
  #
  return
  ```
* DeviceB configuration file
  
  ```
  #
  sysname DeviceB
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.1.5.1 255.255.255.0
  #
  ospf 1
   area 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.1.5.0 0.0.0.255
  #
  return
  ```