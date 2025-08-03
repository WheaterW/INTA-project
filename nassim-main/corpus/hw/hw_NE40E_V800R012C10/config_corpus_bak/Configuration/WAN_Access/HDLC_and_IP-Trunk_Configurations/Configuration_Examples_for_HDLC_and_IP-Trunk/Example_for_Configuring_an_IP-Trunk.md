Example for Configuring an IP-Trunk
===================================

Example_for_Configuring_an_IP-Trunk

#### Networking Requirements

An IP-Trunk link between Device A and Device B is established.

**Figure 1** Networking diagram for an IP-Trunk link![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example are POS 0/1/0 and POS 0/2/0, respectively.


  
![](images/fig_dc_vrp_hdlc_ip-trunk_cfg_002101.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Connect Device A to Device B using POS interfaces.
2. Create an IP-Trunk interface.
3. Add the POS interfaces to the IP-Trunk interface.

#### Data Preparation

To complete the configuration, you need the following data:

* IP address of the IP-Trunk interface on Device A
* IP address of the IP-Trunk interface on Device B

#### Procedure

1. Configure Device A.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceA
   ```
   ```
   [*HUAWEI] commit
   ```
   
   # Create IP-Trunk 1 on Device A and assign an IP address to it.
   
   ```
   [~DeviceA] interface ip-trunk 1
   ```
   ```
   [*DeviceA-Ip-Trunk1] ip address 10.1.1.1 255.255.255.0
   ```
   ```
   [*DeviceA-Ip-Trunk1] undo shutdown
   ```
   ```
   [*DeviceA-Ip-Trunk1] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Add POS 0/1/0 and POS 0/2/0 to IP-Trunk 1.
   
   ```
   [*DeviceA] interface pos 0/1/0
   ```
   ```
   [~DeviceA-Pos0/1/0] link-protocol hdlc
   ```
   ```
   [*DeviceA-Pos0/1/0] ip-trunk 1
   ```
   ```
   [*DeviceA-Pos0/1/0] undo shutdown
   ```
   ```
   [*DeviceA-Pos0/1/0] quit
   ```
   ```
   [*DeviceA] interface pos 0/2/0
   ```
   ```
   [~DeviceA-Pos0/2/0] link-protocol hdlc
   ```
   ```
   [*DeviceA-Pos0/2/0] ip-trunk 1
   ```
   ```
   [*DeviceA-Pos0/2/0] undo shutdown
   ```
   ```
   [*DeviceA-Pos0/2/0] quit
   ```
   ```
   [*DeviceA] commit
   ```
2. Configure Device B.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [*HUAWEI] sysname DeviceB
   ```
   ```
   [*HUAWEI] commit
   ```
   
   # Create IP-Trunk 1 on Device B and assign an IP address to it.
   
   ```
   [~DeviceB] interface ip-trunk 1
   ```
   ```
   [*DeviceB-Ip-Trunk1] ip address 10.1.1.2 255.255.255.0
   ```
   ```
   [*DeviceB-Ip-Trunk1] undo shutdown
   ```
   ```
   [*DeviceB-Ip-Trunk1] quit
   ```
   ```
   [*DeviceB-Ip-Trunk1] commit
   ```
   
   # Add POS 0/1/0 and POS 0/2/0 to IP-Trunk 1.
   
   ```
   [*DeviceB] interface pos 0/1/0
   ```
   ```
   [~DeviceB-Pos0/1/0] link-protocol hdlc
   ```
   ```
   [*DeviceB-Pos0/1/0] ip-trunk 1
   ```
   ```
   [*DeviceB-Pos0/1/0] undo shutdown
   ```
   ```
   [*DeviceB-Pos0/1/0] quit
   ```
   ```
   [*DeviceB] interface pos 0/2/0
   ```
   ```
   [~DeviceB-Pos0/2/0] link-protocol hdlc
   ```
   ```
   [*DeviceB-Pos0/2/0] ip-trunk 1
   ```
   ```
   [*DeviceB-Pos0/2/0] undo shutdown
   ```
   ```
   [*DeviceB-Pos0/2/0] quit
   ```
   ```
   [*DeviceB] commit
   ```
3. Verify the configuration.
   
   
   
   Run the **display interface ip-trunk** command on Device A or Device B. The command output shows that IP-Trunk 1 is Up.
   
   The following example uses the command output on Device A.
   
   ```
   [~DeviceA] display interface ip-trunk 1
   ```
   ```
   Ip-Trunk1 current state : UP (ifindex: 894)
   Line protocol current state : UP
   
   Link quality grade : GOOD
   Description:
   Route Port,Hash arithmetic : According to flow, Maximal BW: 155Mbps, Current BW:
    155Mbps, The Maximum Transmit Unit is 9600
   Internet Address is 10.1.1.1/24
   Link layer protocol is nonstandard HDLC
   Current system time: 2013-08-08 10:26:52
   Physical is IP_TRUNK
       Last 300 seconds input rate 35 bits/sec, 0 packets/sec
       Last 300 seconds output rate 3 bits/sec, 0 packets/sec
       Input: 17508 packets,805368 bytes
              0 errors,0 drops
       Output:1750 packets,80500 bytes
              0 errors,0 drops
       Last 300 seconds input utility rate:  0.01%
       Last 300 seconds output utility rate: 0.01%
   ---------------------------------------------------
   PortName            Status                Weight   
   ---------------------------------------------------
   Pos0/1/0         UP                    1        
   Pos0/2/0         UP                    1        
   ---------------------------------------------------
   The Number of Ports in Trunk : 1
   The Number of UP Ports in Trunk : 1            
   ```
   
   On Device A, view information about member interfaces of IP-Trunk 1.
   
   ```
   [~DeviceA] display trunkmembership ip-trunk 1
   ```
   ```
   Trunk ID: 1
   TYPE: pos
   Number Of Ports in Trunk = 1
   Number Of Up Ports in Trunk = 1
   operate status: up
   
   Interface Pos0/1/0, valid, operate up, weight 1
   Interface Pos0/2/0, valid, operate up, weight 1
   ```
   
   The IP-Trunk interfaces on Device A and Device B can ping each other.
   
   ```
   [~DeviceA] ping -a 10.1.1.1 10.1.1.2
   ```
   ```
     PING 10.1.1.2: 56  data bytes, press CTRL_C to break
   ```
   ```
       Reply from 10.1.1.2: bytes=56 Sequence=1 ttl=255 time=62 ms
   ```
   ```
       Reply from 10.1.1.2: bytes=56 Sequence=2 ttl=255 time=62 ms
   ```
   ```
       Reply from 10.1.1.2: bytes=56 Sequence=3 ttl=255 time=62 ms
   ```
   ```
       Reply from 10.1.1.2: bytes=56 Sequence=4 ttl=255 time=62 ms
   ```
   ```
       Reply from 10.1.1.2: bytes=56 Sequence=5 ttl=255 time=62 ms
   ```
   ```
     --- 10.1.1.2 ping statistics ---
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
       round-trip min/avg/max = 62/62/62 ms
   ```

#### Configuration Files

* Device A configuration file
  
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
  interface Ip-Trunk1
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.1.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface Pos0/1/0
  ```
  ```
   link-protocol hdlc
  ```
  ```
   undo shutdown
  ```
  ```
   ip-trunk 1
  ```
  ```
  #
  ```
  ```
  interface Pos0/2/0
  ```
  ```
   link-protocol hdlc
  ```
  ```
   undo shutdown
  ```
  ```
   ip-trunk 1
  ```
  ```
  #
  ```
  ```
  return
  ```
* Device B configuration file
  
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
  interface Ip-Trunk1
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.1.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface Pos0/1/0
  ```
  ```
   link-protocol hdlc
  ```
  ```
   undo shutdown
  ```
  ```
   ip-trunk 1
  ```
  ```
  #
  ```
  ```
  interface Pos0/2/0
  ```
  ```
   link-protocol hdlc
  ```
  ```
   undo shutdown
  ```
  ```
   ip-trunk 1
  ```
  ```
  #
  ```
  ```
  return
  ```