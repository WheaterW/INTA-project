Example for Configuring a Device to Obtain Packet Headers Sent to its CPU
=========================================================================

This section provides an example for configuring a device to obtain packet headers sent to its central processing unit (CPU).

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172372303__fig_dc_vrp_capture-packet_cfg_0007), PC1 accesses the Internet over Device A and Device B. Device B has high CPU usage. To find out the reason why Device B has high CPU usage, configure Device B to obtain packet headers sent to its CPU.

**Figure 1** Configuring Device B to obtain packet headers sent to its CPU![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/1/0, GE 0/1/1, and GE 0/1/2, respectively.


  
![](images/dc_vrp_capture-packet_cfg_0007.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

* Configure the function of obtaining packet headers sent to Device B's CPU.

#### Data Preparation

To complete the configuration, you need the following data:

* Interface IP addresses
* Packet header obtaining timeout time and number of obtained packet headers


#### Procedure

1. Configure interface IP addresses and routing protocol. The configuration details are not provided.
2. Configure Device B to obtain packet headers sent to its CPU.
   
   
   ```
   <DeviceB> capture-packet local-host all interface gigabitethernet 0/1/2 packet-len 60 packet-num 1000 time-out 3600
   ```
3. View the configuration and the packet header obtaining file.
   
   
   
   # View the configuration.
   
   ```
   <DeviceB> display capture-packet config-state
   ```
   ```
   Capture-Packet Index 1
   Type        : local-host
   SysID       : all
   Interface   : GigabitEthernet0/1/2
   File Name   : cfcard:/capture_host_all_GigabitEthernet3.0.2_2012-05-03-10-51-29.cap
   Time-out    : 3600 seconds
   Packet-num  : 1000
   Packet-len  : 60
   BufferOnly  : disabled
   ```
   
   
   
   # View the packet header obtaining file.
   
   ```
   <DeviceB> display capture-packet file cfcard:/capture_host_all_GigabitEthernet3.0.2_2012-05-03-10-51-29.cap
   ```
   ```
   a1 b2 c3 d4 00 02 00 04 00 00 00 00 00 00 00 00
   00 00 ff ff 00 00 00 09 4d 10 36 db 00 0a d5 81
   00 00 00 0c 00 00 00 0c ff 03 c0 21 09 9d 00 08
   8a 8c bc c3 4d 10 36 db 00 0a d6 ae
   ```

#### Configuration Files

* Device A configuration file
  
  ```
  #
  sysname DeviceA
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
* Device B configuration file
  
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
  capture-packet local-host all interface gigabitethernet 0/1/2 packet-len 60 packet-num 1000 time-out 3600
  #
  return
  ```