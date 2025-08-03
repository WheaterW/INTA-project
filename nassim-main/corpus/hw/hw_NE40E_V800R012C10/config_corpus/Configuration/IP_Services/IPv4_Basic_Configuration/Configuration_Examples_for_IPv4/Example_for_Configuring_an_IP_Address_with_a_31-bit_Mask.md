Example for Configuring an IP Address with a 31-bit Mask
========================================================

This section provides an example for configuring an IP address with a 31-bit mask.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172364951__fig_dc_vrp_ipv4_cfg_002901), Device A and Device B are directly connected through a PPP link. To allow Device A and Device B to communicate, configure IP addresses with a 31-bit mask for the interfaces that connect Device A and Device B.

**Figure 1** Configuring an IP address with a 31-bit mask![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 in this example represents GE 0/1/0.


  
![](images/fig_dc_vrp_ipv4_cfg_002901.png)

#### Precautions

None


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IP address with a 31-bit mask for GE 0/1/0 on DeviceA.
2. Configure an IP address with a 31-bit mask for GE 0/1/0 on DeviceB.

#### Data Preparation

To complete the configuration, you need the following data:

* IP address and subnet mask of GE 0/1/0 on DeviceA
* IP address and subnet mask of GE 0/1/0 on DeviceB

#### Procedure

1. Configure an IP address for each interface.
   
   
   
   # Configure an IP address for GE 0/1/0 on DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface GigabitEthernet 0/1/0
   [~DeviceA-GigabitEthernet0/1/0] ip address 10.1.1.1 31
   [*DeviceA-GigabitEthernet0/1/0] undo shutdown
   [*DeviceA-GigabitEthernet0/1/0] commit
   [~DeviceA-GigabitEthernet0/1/0] quit
   ```
   
   # Configure an IP address for GE 0/1/0 on DeviceB.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] interface GigabitEthernet 0/1/0
   [~DeviceB-GigabitEthernet0/1/0] ip address 10.1.1.0 31
   [*DeviceB-GigabitEthernet0/1/0] undo shutdown
   [*DeviceB-GigabitEthernet0/1/0] commit
   [~DeviceB-GigabitEthernet0/1/0] quit
   ```
2. Verify the configuration.
   
   
   
   # After the configuration is complete, check the routing table on DeviceA. The command output shows that both the network address and the broadcast address of the network segment are used as host addresses.
   
   ```
   [~DeviceA] display ip routing-table
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table: Public
            Destinations : 5        Routes : 5
   Destination/Mask    Proto  Pre  Cost     Flags NextHop         Interface
          10.1.1.0/31  Direct 0    0           D  10.1.1.1           GigabitEthernet0/1/0
          10.1.1.0/32  Direct 0    0           D  10.1.1.0           GigabitEthernet0/1/0
          10.1.1.1/32  Direct 0    0           D  127.0.0.1          GigabitEthernet0/1/0
         127.0.0.0/8   Direct 0    0           D  127.0.0.1          InLoopBack0
         127.0.0.1/32  Direct 0    0           D  127.0.0.1          InLoopBack0
   ```
   
   # After the configuration is complete, check the routing table on DeviceB. In the routing table, you can view that both the network address and the broadcast address of the network segment are used as host addresses.
   
   ```
   [~DeviceB] display ip routing-table
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table: _public_
            Destinations : 5        Routes : 5
   
   Destination/Mask    Proto  Pre  Cost     Flags NextHop         Interface
   
          10.1.1.0/31  Direct 0    0           D  10.1.1.0           GigabitEthernet0/1/0
          10.1.1.0/32  Direct 0    0           D  127.0.0.1          GigabitEthernet0/1/0
          10.1.1.1/32  Direct 0    0           D  10.1.1.1           GigabitEthernet0/1/0
         127.0.0.0/8   Direct 0    0           D  127.0.0.1          InLoopBack0
         127.0.0.1/32  Direct 0    0           D  127.0.0.1          InLoopBack0   
   ```

#### Configuration Files

* DeviceA
  
  ```
  #
   sysname DeviceA
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.254
  #
  return
  ```
* DeviceB
  
  ```
  #
   sysname DeviceB
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.0 255.255.255.254
  #
  return
  ```