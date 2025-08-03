Example for Configuring Primary and Secondary IP Addresses for an Interface
===========================================================================

This section provides an example for configuring a primary IP address and a secondary IP address for an interface.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172364939__fig_dc_vrp_ipv4_cfg_002501), GE 0/1/1 of the device connects to a LAN in which computers belong to one of the two network segments: 172.16.1.0/24 and 172.16.2.0/24. It is required that the device can communicate with the two network segments. At the same time, the hosts of the two network segments can communicate with each other.

**Figure 1** Configuring primary and secondary IP addresses for an interface![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 in this example represents GE 0/1/1.


  
![](images/fig_dc_vrp_ipv4_cfg_002501.png)

#### Precautions

None


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Analyze the addresses of the network segments to which the interface connects.
2. Configure a primary IP address for the interface and then one or more secondary IP addresses for the interface.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The primary and secondary IP addresses of an interface can have overlapped network segments but cannot be the same. The secondary IP addresses of an interface must belong to different network segments.



#### Data Preparation

To complete the configuration, you need the following data:

* Primary IP address and subnet mask of the interface
* Secondary IP address and subnet mask of the interface

#### Procedure

1. Configure the device.
   
   
   
   # Configure primary and secondary IP addresses for GE 0/1/1.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] interface gigabitethernet 0/1/1
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/1] ip address 172.16.1.1 255.255.255.0
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/1] ip address 172.16.2.1 255.255.255.0 sub
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/1] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/1] quit
   ```
2. Verify the configuration.
   
   
   
   # Ping the hosts on the network segment 172.16.1.0 from Device. The ping operation is successful.
   
   ```
   [~HUAWEI] ping 172.16.1.2
   ```
   ```
     PING 172.16.1.2: 56  data bytes, press CTRL_C to break
   ```
   ```
       Reply from 172.16.1.2: bytes=56 Sequence=1 ttl=255 time=614 ms
   ```
   ```
       Reply from 172.16.1.2: bytes=56 Sequence=2 ttl=255 time=16 ms
   ```
   ```
       Reply from 172.16.1.2: bytes=56 Sequence=3 ttl=255 time=2 ms
   ```
   ```
       Reply from 172.16.1.2: bytes=56 Sequence=4 ttl=255 time=3 ms
   ```
   ```
       Reply from 172.16.1.2: bytes=56 Sequence=5 ttl=255 time=2 ms
   ```
   ```
     --- 172.16.1.2 ping statistics ---
   ```
   ```
       5 packet(s) transmitted
   ```
   ```
       5 packet(s) received
   ```
   ```
       0.00% packet loss
   ```
   ```
       round-trip min/avg/max = 25/26/27 ms
   ```
   
   # Ping the hosts on the network segment 172.16.2.0 from Device. The ping operation is successful.
   
   ```
   [~HUAWEI] ping 172.16.2.2
   ```
   ```
     PING 172.16.2.2: 56  data bytes, press CTRL_C to break
   ```
   ```
       Reply from 172.16.2.2: bytes=56 Sequence=1 ttl=255 time=13 ms
   ```
   ```
       Reply from 172.16.2.2: bytes=56 Sequence=2 ttl=255 time=2 ms
   ```
   ```
       Reply from 172.16.2.2: bytes=56 Sequence=3 ttl=255 time=2 ms
   ```
   ```
       Reply from 172.16.2.2: bytes=56 Sequence=4 ttl=255 time=2 ms
   ```
   ```
       Reply from 172.16.2.2: bytes=56 Sequence=5 ttl=255 time=2 ms
   ```
   ```
     --- 172.16.2.2 ping statistics ---
   ```
   ```
       5 packet(s) transmitted
   ```
   ```
       5 packet(s) received
   ```
   ```
       0.00% packet loss
   ```
   ```
       round-trip min/avg/max = 25/25/26 ms
   ```
   
   # The hosts on the two network segments cannot ping each other.

#### Configuration Files

* Device configuration file
  
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 172.16.1.1 255.255.255.0
  ```
  ```
   ip address 172.16.2.1 255.255.255.0 sub
  ```
  ```
  #
  ```
  ```
  return
  ```