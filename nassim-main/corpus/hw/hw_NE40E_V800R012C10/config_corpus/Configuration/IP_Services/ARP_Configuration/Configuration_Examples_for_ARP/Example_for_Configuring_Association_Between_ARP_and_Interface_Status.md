Example for Configuring Association Between ARP and Interface Status
====================================================================

This section describes how to configure association between ARP and interface status.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172364529__fig_dc_vrp_cfg_00214301), DeviceA and DeviceB are connected over a switch. If the link between DeviceA and the switch works properly, the link between DeviceB and the switch becomes faulty. If both the physical status and protocol status of interface 1 on DeviceA are up, DeviceA does not get aware of the link fault between DeviceB and the switch. Instead, DeviceA still sends packets to DeviceB over the switch. The packets, however, are discarded by the switch. Then, association between ARP and interface status is enabled on DeviceA to detect the status of interface 1 on DeviceB. In this manner, DeviceA rapidly adjusts the status of interface 1 based on the status of the link between DeviceB and the switch.

**Figure 1** Configuring association between ARP and interface status![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 in this example represents GigabitEthernet 0/1/1.


  
![](images/fig_dc_vrp_arp_cfg_203604.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IP address for the interface.
2. Enable association between ARP and interface status.

#### Data Preparation

To complete the configuration, you need the following data:

* Interface IP addresses
* Destination IP address of the ARP probe messages sent by the interface

#### Procedure

1. Configure an IP address for the interface.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceA
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceA] interface gigabitethernet 0/1/1
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] ip address 10.1.1.1 255.255.255.0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] quit
   ```
   
   # Configure DeviceB.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceB
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceB] interface gigabitethernet 0/1/1
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/1] ip address 10.1.1.2 255.255.255.0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/1] quit
   ```
   
   # Run the **ping** command on DeviceA and ensure that GigabitEthernet 0/1/1 on DeviceB is reachable.
   
   ```
   [~DeviceA] ping 10.1.1.2
   ```
   ```
     PING 10.1.1.2: 56  data bytes, press CTRL_C to break
       Reply from 10.1.1.2: bytes=56 Sequence=1 ttl=255 time=62 ms
       Reply from 10.1.1.2: bytes=56 Sequence=2 ttl=255 time=1 ms
       Reply from 10.1.1.2: bytes=56 Sequence=3 ttl=255 time=1 ms
       Reply from 10.1.1.2: bytes=56 Sequence=4 ttl=255 time=2 ms
       Reply from 10.1.1.2: bytes=56 Sequence=5 ttl=255 time=2 ms
   
     --- 10.1.1.2 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 1/13/62 ms
   ```
   
   # Run the **display interface** command on both DeviceA and DeviceB to view the status of GigabitEthernet 0/1/1 and check that both the physical status and protocol status of the interface are Up.
   
   ```
   [~DeviceA] display interface gigabitethernet 0/1/1
   ```
   ```
   GigabitEthernet0/1/1 current state : UP (ifindex: 9)
   Line protocol current state : UP 
   Last line protocol up time : 2018-01-24 11:03:06
   Link quality grade : GOOD
   Description: 
   Route Port,The Maximum Transmit Unit is 1500 
   Internet Address is 10.1.1.1/24
   IP Sending Frames' Format is PKTFMT_ETHNT_2, Hardware address is 00e0-fc21-0302
   Loopback:none, LAN full-duplex mode, Pause Flowcontrol: Receive Enable and Send Enable
   Last physical up time   : 2018-01-24 09:00:21
   Last physical down time : 2018-01-24 08:58:14
   Current system time: 2018-01-24 11:22:58
   Statistics last cleared:never
       Last 300 seconds input rate: 0 bits/sec, 0 packets/sec
       Last 300 seconds output rate: 0 bits/sec, 0 packets/sec
       Input peak rate 0 bits/sec, Record time: -
       Output peak rate 0 bits/sec, Record time: -
       Input: 0 bytes, 1254 packets
       Output: 0 bytes, 1261 packets
       Input: 
         Unicast: 10 packets, Multicast: 46 packets
         Broadcast: 1198 packets, JumboOctets: 0 packets
         CRC: 0 packets, Symbol: 0 packets
         Overrun: 0 packets, InRangeLength: 0 packets
         LongPacket: 0 packets, Jabber: 0 packets, Alignment: 0 packets
         Fragment: 0 packets, Undersized Frame: 0 packets
         RxPause: 0 packets
       Output:
         Unicast: 11 packets, Multicast: 46 packets
         Broadcast: 1204 packets, JumboOctets: 0 packets
         Lost: 0 packets, Overflow: 0 packets, Underrun: 0 packets
         System: 0 packets, Overruns: 0 packets
         TxPause: 0 packets
       Last 300 seconds input utility rate:  0.00%
       Last 300 seconds output utility rate: 0.00%
   ```
   ```
   [~DeviceB] display interface gigabitethernet 0/1/1
   ```
   ```
   GigabitEthernet0/1/1 current state : UP (ifindex: 9)
   Line protocol current state : UP 
   Last line protocol up time : 2018-01-24 11:03:28
   Link quality grade : GOOD
   Description: 
   Route Port,The Maximum Transmit Unit is 1500 
   Internet Address is 10.1.1.2/24
   IP Sending Frames' Format is PKTFMT_ETHNT_2, Hardware address is 00e0-fc41-0302
   Loopback:none, LAN full-duplex mode, Pause Flowcontrol: Receive Enable and Send Enable
   Last physical up time   : 2018-01-24 09:00:22
   Last physical down time : 2018-01-24 09:00:21
   Current system time: 2018-01-24 11:23:25
   Statistics last cleared:never
       Last 300 seconds input rate: 0 bits/sec, 0 packets/sec
       Last 300 seconds output rate: 0 bits/sec, 0 packets/sec
       Input peak rate 0 bits/sec, Record time: -
       Output peak rate 0 bits/sec, Record time: -
       Input: 0 bytes, 1262 packets
       Output: 0 bytes, 1255 packets
       Input: 
         Unicast: 11 packets, Multicast: 47 packets
         Broadcast: 1204 packets, JumboOctets: 0 packets
         CRC: 0 packets, Symbol: 0 packets
         Overrun: 0 packets, InRangeLength: 0 packets
         LongPacket: 0 packets, Jabber: 0 packets, Alignment: 0 packets
         Fragment: 0 packets, Undersized Frame: 0 packets
         RxPause: 0 packets
       Output:
         Unicast: 10 packets, Multicast: 47 packets
         Broadcast: 1198 packets, JumboOctets: 0 packets
         Lost: 0 packets, Overflow: 0 packets, Underrun: 0 packets
         System: 0 packets, Overruns: 0 packets
         TxPause: 0 packets
       Last 300 seconds input utility rate:  0.00%
       Last 300 seconds output utility rate: 0.00%
   ```
2. Simulate an interface fault.
   
   
   
   # Run the **shutdown** command on GigabitEthernet 0/1/1 of DeviceB.
   
   ```
   [~DeviceB] interface gigabitethernet 0/1/1
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/1] shutdown
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/1] quit
   ```
   
   # Run the **display interface** command on DeviceA to view the status of GigabitEthernet 0/1/1 and check that both the physical status and protocol status of the interface are Up.
   
   ```
   [~DeviceA] display interface gigabitethernet 0/1/1
   ```
   ```
   GigabitEthernet0/1/1 current state : UP (ifindex: 9)
   Line protocol current state : UP 
   Last line protocol up time : 2018-01-24 11:03:06
   Link quality grade : GOOD
   Description: 
   Route Port,The Maximum Transmit Unit is 1500 
   Internet Address is 10.1.1.1/24
   IP Sending Frames' Format is PKTFMT_ETHNT_2, Hardware address is 00e0-fc21-0302
   Loopback:none, LAN full-duplex mode, Pause Flowcontrol: Receive Enable and Send Enable
   Last physical up time   : 2018-01-24 09:00:21
   Last physical down time : 2018-01-24 08:58:14
   Current system time: 2018-01-24 11:25:18
   Statistics last cleared:never
       Last 300 seconds input rate: 0 bits/sec, 0 packets/sec
       Last 300 seconds output rate: 0 bits/sec, 0 packets/sec
       Input peak rate 0 bits/sec, Record time: -
       Output peak rate 0 bits/sec, Record time: -
       Input: 0 bytes, 1254 packets
       Output: 0 bytes, 1261 packets
       Input: 
         Unicast: 10 packets, Multicast: 46 packets
         Broadcast: 1198 packets, JumboOctets: 0 packets
         CRC: 0 packets, Symbol: 0 packets
         Overrun: 0 packets, InRangeLength: 0 packets
         LongPacket: 0 packets, Jabber: 0 packets, Alignment: 0 packets
         Fragment: 0 packets, Undersized Frame: 0 packets
         RxPause: 0 packets
       Output:
         Unicast: 11 packets, Multicast: 46 packets
         Broadcast: 1204 packets, JumboOctets: 0 packets
         Lost: 0 packets, Overflow: 0 packets, Underrun: 0 packets
         System: 0 packets, Overruns: 0 packets
         TxPause: 0 packets
       Last 300 seconds input utility rate:  0.00%
       Last 300 seconds output utility rate: 0.00%
   ```
   
   # Run the **ping** command on DeviceA and ensure that GigabitEthernet 0/1/1 on DeviceB is reachable.
   
   ```
   [~DeviceA] ping 10.1.1.2
   ```
   ```
     PING 10.1.1.2: 56  data bytes, press CTRL_C to break
       Request time out
       Request time out
       Request time out
       Request time out
       Request time out
   
     --- 10.1.1.2 ping statistics ---
       5 packet(s) transmitted
       0 packet(s) received
       100.00% packet loss
   ```
3. Enable association between ARP and interface status on DeviceA.
   
   
   
   # Enable the interface on DeviceA to send ARP probe messages.
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/1
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] arp status-detect 10.1.1.2
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] quit
   ```
4. Verify the configuration.
   
   
   
   # After the detection period elapses, the physical status of GigabitEthernet 0/1/1 of DeviceA becomes Up and the protocol status becomes Down.
   
   ```
   [~DeviceA] display interface gigabitethernet 0/1/1
   ```
   ```
   GigabitEthernet0/1/1 current state : UP (ifindex: 9)
   Line protocol current state : DOWN 
   Link quality grade : GOOD
   Description: 
   Route Port,The Maximum Transmit Unit is 1500 
   Internet Address is 10.1.1.1/24
   IP Sending Frames' Format is PKTFMT_ETHNT_2, Hardware address is 00e0-fc21-0302
   Loopback:none, LAN full-duplex mode, Pause Flowcontrol: Receive Enable and Send Enable
   Last physical up time   : 2018-01-24 12:03:24
   Last physical down time : 2018-01-24 11:40:45
   Current system time: 2018-01-24 12:06:25
   Statistics last cleared:never
       Last 300 seconds input rate: 0 bits/sec, 0 packets/sec
       Last 300 seconds output rate: 0 bits/sec, 0 packets/sec
       Input peak rate 0 bits/sec, Record time: -
       Output peak rate 0 bits/sec, Record time: -
       Input: 0 bytes, 1354 packets
       Output: 0 bytes, 1370 packets
       Input: 
         Unicast: 64 packets, Multicast: 91 packets
         Broadcast: 1199 packets, JumboOctets: 0 packets
         CRC: 0 packets, Symbol: 0 packets
         Overrun: 0 packets, InRangeLength: 0 packets
         LongPacket: 0 packets, Jabber: 0 packets, Alignment: 0 packets
         Fragment: 0 packets, Undersized Frame: 0 packets
         RxPause: 0 packets
       Output:
         Unicast: 12 packets, Multicast: 90 packets
         Broadcast: 1268 packets, JumboOctets: 0 packets
         Lost: 0 packets, Overflow: 0 packets, Underrun: 0 packets
         System: 0 packets, Overruns: 0 packets
         TxPause: 0 packets
       Last 300 seconds input utility rate:  0.00%
       Last 300 seconds output utility rate: 0.00%
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  #
  interface GigabitEthernet0/1/1
   undo shutdown  
   ip address 10.1.1.1 255.255.255.0
   arp status-detect 10.1.1.2
  #
  return
  ```
* DeviceB configuration file
  
  ```
  #
  sysname DeviceB
  #
  interface GigabitEthernet0/1/1
   undo shutdown  
   ip address 10.1.1.2 255.255.255.0
  #
  return
  ```