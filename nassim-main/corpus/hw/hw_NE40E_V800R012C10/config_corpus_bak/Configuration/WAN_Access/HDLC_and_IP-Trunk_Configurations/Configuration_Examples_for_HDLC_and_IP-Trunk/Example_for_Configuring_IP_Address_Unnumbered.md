Example for Configuring IP Address Unnumbered
=============================================

This section provides an example for configuring IP address unnumbered and describes how IP address unnumbered works in typical networking scenarios.

#### Networking Requirements

Device A and Device B are connected using HDLC-enabled POS interfaces.

POS 0/1/0 on Device A borrows the IP address of a loopback interface on Device A, and the mask of the IP address is 32 bits.

**Figure 1** Networking diagram for configuring IP address unnumbered![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 in this example is POS0/1/0.


  
![](images/fig_dc_vrp_hdlc_ip-trunk_cfg_002001.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure HDLC as a link layer protocol on the interface of each Router.
2. Configure the IP address to be borrowed, that is, the IP address of the loopback interface on Device A.
3. Configure IP address unnumbered for the POS interface on Device A.
4. On Device A, configure a static route to Device B.
5. Assign an IP address to the interface on Device B.

#### Data Preparation

To complete the configuration, you need the following data:

* IP address of the loopback interface on Device A
* IP address of the POS interface on Device B

![](../../../../public_sys-resources/note_3.0-en-us.png) 

These two IP addresses must be on the same network segment; otherwise, the link layer protocol cannot go Up.



#### Procedure

1. Configure Device A.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [*HUAWEI] sysname DeviceA
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceA] interface loopback 1
   ```
   ```
   [*DeviceA-LoopBack1] ip address 10.1.1.1 32
   ```
   ```
   [*DeviceA-LoopBack1] quit
   ```
   ```
   [*DeviceA] interface pos 0/1/0
   ```
   ```
   [*DeviceA-Pos0/1/0] link-protocol hdlc
   ```
   ```
   [*DeviceA-Pos0/1/0] ip address unnumbered interface loopback 1
   ```
   ```
   [*DeviceA-Pos0/1/0] undo shutdown
   ```
   ```
   [*DeviceA-Pos0/1/0] quit
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
   ```
   [~DeviceB] interface pos 0/1/0
   ```
   ```
   [~DeviceB-Pos0/1/0] link-protocol hdlc
   ```
   ```
   [*DeviceB-Pos0/1/0] ip address 10.1.1.2 24
   ```
   ```
   [*DeviceB-Pos0/1/0] undo shutdown
   ```
   ```
   [*DeviceB-Pos0/1/0] quit
   ```
3. Configure a static route on Device A.
   
   
   ```
   [*DeviceA] ip route-static 10.1.1.0 255.255.255.255 pos 0/1/0
   ```
   ```
   [*DeviceB-Pos0/1/0] commit
   ```
4. Verify the configuration.
   
   
   
   After the configuration is complete, Device A and Device B can ping each other.
   
   The following example uses the command output on Device A.
   
   ```
   [~DeviceA] ping 10.1.1.2
   ```
   ```
     PING 10.1.1.2: 56  data bytes, press CTRL_C to break
   ```
   ```
       Reply from 10.1.1.2: bytes=56 Sequence=1 ttl=255 time=31 ms
   ```
   ```
       Reply from 10.1.1.2: bytes=56 Sequence=2 ttl=255 time=63 ms
   ```
   ```
       Reply from 10.1.1.2: bytes=56 Sequence=3 ttl=255 time=63 ms
   ```
   ```
       Reply from 10.1.1.2: bytes=56 Sequence=4 ttl=255 time=63 ms
   ```
   ```
       Reply from 10.1.1.2: bytes=56 Sequence=5 ttl=255 time=63 ms
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
       round-trip min/avg/max = 31/56/63 ms
   ```
   
   Run the **display ip routing-table** command. The command output shows that routing information is correct.
   
   The following example uses the command output on Device A.
   
   ```
   [~DeviceA] display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : Public
            Destinations : 2        Routes : 2         
   
   Destination/Mask   Proto   Pre  Cost        Flags NextHop         Interface
   
        10.1.1.0/24   Static  60   0             D   0.0.0.0         Pos0/1/0     
        10.1.1.1/32   Direct  0    0             D   127.0.0.1       LoopBack1     
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
   ip route-static 10.1.1.0 255.255.255.0 Pos0/1/0
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
   ip address unnumbered interface LoopBack1
  ```
  ```
  #
  ```
  ```
  interface LoopBack1
  ```
  ```
   ip address 10.1.1.1 255.255.255.255
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
  interface Pos0/1/0
  ```
  ```
   link-protocol hdlc
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
  return
  ```