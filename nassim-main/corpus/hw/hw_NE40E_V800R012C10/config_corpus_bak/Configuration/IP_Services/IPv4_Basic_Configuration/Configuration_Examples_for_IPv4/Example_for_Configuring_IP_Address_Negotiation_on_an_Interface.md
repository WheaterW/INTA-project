Example for Configuring IP Address Negotiation on an Interface
==============================================================

This section provides an example for configuring IP address negotiation on an interface so that the interface can obtain an IP address.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172364942__fig_dc_vrp_ipv4_cfg_002601), DeviceA functions as a PPP server, and DeviceB functions as a PPP client. To allow DeviceA to assign an IP address to POS 0/1/0 on DeviceB through PPP negotiation, configure IP address negotiation on POS 0/1/0.

**Figure 1** Configuring IP address negotiation on an interface![](../../../../public_sys-resources/note_3.0-en-us.png) 

interface1 in this example represents POS 0/1/0.


  
![](figure/en-us_image_0000001526329336.png)

#### Precautions

None


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IP address for the local interface.
2. Assign an IP address to the interface on the client.
3. Configure the client to obtain an IP address through negotiation.

#### Data Preparation

To complete the configuration, you need the following data:

* IP address and subnet mask of the local interface
* The IP address to be assigned to the client

#### Procedure

1. Configure DeviceA.
   
   
   
   # Configure an IP address for POS 0/1/0.
   
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
   [~DeviceA] interface pos0/1/0
   ```
   ```
   [~DeviceA-Pos0/1/0] link-protocol ppp
   ```
   ```
   [*DeviceA-Pos0/1/0] ip address 192.168.1.1 255.255.255.0
   ```
   
   # Assign an IP address to the interface on the client.
   
   ```
   [*DeviceA-Pos0/1/0] remote address 192.168.1.2
   ```
   ```
   [*DeviceA-Pos0/1/0] shutdown
   ```
   ```
   [*DeviceA-Pos0/1/0] commit
   ```
   ```
   [~DeviceA-Pos0/1/0] undo shutdown
   ```
   ```
   [*DeviceA-Pos0/1/0] commit
   ```
   ```
   [~DeviceA-Pos0/1/0] quit
   ```
2. Configure DeviceB.
   
   
   
   # Configure the interface to obtain an IP address through negotiation.
   
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
   [~DeviceB] interface pos0/1/0
   ```
   ```
   [~DeviceB-Pos0/1/0] link-protocol ppp
   ```
   ```
   [*DeviceB-Pos0/1/0] ip address ppp-negotiate
   ```
   ```
   [*DeviceB-Pos0/1/0] undo shutdown
   ```
   ```
   [*DeviceB-Pos0/1/0] commit
   ```
   ```
   [~DeviceB-Pos0/1/0] quit
   ```
3. Verify the configuration.
   
   
   
   # Ping POS 0/1/0 on DeviceA from DeviceB. The ping operation is successful.
   
   ```
   [~DeviceB] ping 192.168.1.1
   ```
   ```
     PING 192.168.1.1: 56  data bytes, press CTRL_C to break
   ```
   ```
       Reply from 192.168.1.1: bytes=56 Sequence=1 ttl=255 time=156 ms
   ```
   ```
       Reply from 192.168.1.1: bytes=56 Sequence=2 ttl=255 time=63 ms
   ```
   ```
       Reply from 192.168.1.1: bytes=56 Sequence=3 ttl=255 time=62 ms
   ```
   ```
       Reply from 192.168.1.1: bytes=56 Sequence=4 ttl=255 time=63 ms
   ```
   ```
       Reply from 192.168.1.1: bytes=56 Sequence=5 ttl=255 time=63 ms
   ```
   ```
     --- 192.168.1.1 ping statistics ---
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
   round-trip min/avg/max = 62/81/156 ms  
   ```
   
   # Display the status of POS 0/1/0 on DeviceB.
   
   ```
   [~DeviceB] display interface pos0/1/0
   ```
   ```
   Pos0/1/0 current state : UP
   Line protocol current state : UP
   Last line protocol up time : 2007-12-07, 17:12:39 
   Route Port,The Maximum Transmit Unit is 4470, Hold timer is 10(sec)
   Internet Address is negotiated, 192.168.1.2/32
   Link layer protocol is PPP
   LCP opened, IPCP opened
   The Vendor PN is FTRJ1321P1BTL
   Port BW: 2.5G, Transceiver max BW: 2.5G, Transceiver Mode: SingleMode
   WaveLength: 1310nm, Transmission Distance: 5km
   Rx Power: -2.81dBm, Tx Power: -1.91dBm
    Physical layer is Packet Over SDH
   Scramble enabled, clock master, CRC-32, loopback: none
   Flag J0 "NetEngine       "
   Flag J1 "NetEngine       "
   Flag C2 22(0x16)
       SDH alarm:
           section layer:  none
           line    layer:  none
           path    layer:  none
       SDH error:
           section layer:  B1 61575
           line    layer:  B2 12002824  REI 16835916
           path    layer:  B3 65535
   Statistics last cleared:never
       Last 300 seconds input rate 16 bits/sec, 0 packets/sec
       Last 300 seconds output rate 40 bits/sec, 0 packets/sec
       Input: 3510 packets, 57372 bytes
       Input error: 0 shortpacket, 0 longpacket, 4 CRC, 0 lostpacket
       Output: 7270 packets, 344198 bytes
       Output error: 0 lostpackets
       Output error: 0 overrunpackets, 0 underrunpackets          
   ```
   
   The command output shows "Internet Address is negotiated, 192.168.1.2/32", meaning that IP address negotiation is successful.

#### Configuration Files

* DeviceA configuration file
  
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
  interface pos0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   link-protocol ppp
  ```
  ```
   ip address 192.168.1.1 255.255.255.0
  ```
  ```
   remote address 192.168.1.2
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceB configuration file
  
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
  interface pos0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   link-protocol ppp
  ```
  ```
   ip address ppp-negotiate
  ```
  ```
  #
  ```
  ```
  return
  ```