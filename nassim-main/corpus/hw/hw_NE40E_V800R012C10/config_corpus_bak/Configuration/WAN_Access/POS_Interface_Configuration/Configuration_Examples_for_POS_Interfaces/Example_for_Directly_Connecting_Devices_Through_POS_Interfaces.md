Example for Directly Connecting Devices Through POS Interfaces
==============================================================

This example shows how to connect two devices through POS interfaces in typical networking.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172364032__fig_dc_ne_pos_cfg_001301), POS interfaces on DeviceA and DeviceB are directly connected using a pair of single-mode optical fibers for receiving and sending packets. PPP is the link layer protocol. It is required that the two devices can communicate with each other.

**Figure 1** Network diagram of directly connecting devices through POS interfaces![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface1 in this example represents POS 0/1/0.


  
![](images/fig_dc_ne_pos_cfg_001301.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure PPP as the link layer protocol.
2. Configure IP addresses.

#### Data Preparation

To complete the configuration, you need the following data:

* IP address of interface1 on DeviceA
* IP address of interface1 on DeviceB

#### Procedure

1. Configure DeviceA.
   
   
   
   # Configure POS 0/1/0. By default, the link layer protocol is PPP and the clock mode is master. In this step, the POS interface uses the default link layer protocol and clock mode.
   
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
   [~DeviceA] interface pos 0/1/0
   ```
   ```
   [*DeviceA-Pos0/1/0] ip address 10.1.1.1 30
   ```
   ```
   [*DeviceA-Pos0/1/0] quit
   ```
   ```
   [*DeviceA] commit
   ```
2. Configure DeviceB.
   
   
   
   # Configure POS 0/1/0 and set the clock mode to slave. By default, the link layer protocol is PPP. In this step, the POS interface uses the default link layer protocol.
   
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
   [DeviceB] interface pos 0/1/0
   ```
   ```
   [~DeviceB-Pos0/1/0] clock slave
   ```
   ```
   [*DeviceB-Pos0/1/0] ip address 10.1.1.2 30
   ```
   ```
   [*DeviceB-Pos0/1/0] quit
   ```
   ```
   [*DeviceB] commit
   ```
3. Verify the configuration.
   
   Run the **display interface pos** command to check the connectivity of the POS interface on DeviceA.
   ```
   [~DeviceA] display interface pos 0/1/0
   ```
   ```
   Pos0/1/0 current state : UP 
   Line protocol current state : UP 
   Last line protocol up time : 2010-07-13 16:47:08
   Description:
   Route Port,The Maximum Transmit Unit is 1600, Hold timer is 10(sec)
   Internet Address is 10.1.1.1/30
   Link layer protocol is PPP 
   LCP opened, IPCP opened, IP6CP opened, OSICP opened, MPLSCP opened
   PPP negotiated peer ip address is 10.1.1.10
   Current system time: 2010-07-13 17:29:44 
   The Vendor PN is FTLF1322P1BTR-HW
   The Vendor Name is FINISAR CORP.   
   Port BW: 622M, Transceiver max BW: 622M, Transceiver Mode: SingleMode
   WaveLength: 1310nm, Transmission Distance: 15km
   Rx Power:  7.66dBm,  Tx Power: -11.78dBm
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
           section layer:  B1 284236
           line    layer:  B2 1871  REI 4445
           path    layer:  B3 719417  REI 12417181
   Statistics last cleared:never
       Last 300 seconds input rate 304 bits/sec, 0 packets/sec
       Last 300 seconds output rate 320 bits/sec, 0 packets/sec
       Input: 5754803980 packets, 540947996544 bytes
       Input error: 0 shortpackets, 0 longpackets, 0 CRC, 0 lostpackets
       Output: 5676758063 packets, 533611565328 bytes
       Output error: 0 lostpackets
       Output error: 0 overrunpackets, 0 underrunpackets
   ```
   
   Run the [**ping**](cmdqueryname=ping) command to check the network connectivity.
   
   ```
   [~DeviceA] ping 10.1.1.2
   ```
   ```
     PING 10.1.1.2: 56  data bytes, press CTRL_C to break
   ```
   ```
       Reply from 10.1.1.2: bytes=56 Sequence=1 ttl=255 time=3 ms
   ```
   ```
       Reply from 10.1.1.2: bytes=56 Sequence=2 ttl=255 time=2 ms
   ```
   ```
       Reply from 10.1.1.2: bytes=56 Sequence=3 ttl=255 time=2 ms
   ```
   ```
       Reply from 10.1.1.2: bytes=56 Sequence=4 ttl=255 time=2 ms
   ```
   ```
       Reply from 10.1.1.2: bytes=56 Sequence=5 ttl=255 time=2 ms
   
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
   round-trip min/avg/max = 2/2/3 ms
   ```

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
  interface Pos0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   link-protocol ppp
  ```
  ```
   ip address 10.1.1.1 255.255.255.252
  ```
  ```
   clock master
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
  interface Pos0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   link-protocol ppp
  ```
  ```
   ip address 10.1.1.2 255.255.255.252
  ```
  ```
   clock slave
  ```
  ```
  #
  ```
  ```
  return
  ```