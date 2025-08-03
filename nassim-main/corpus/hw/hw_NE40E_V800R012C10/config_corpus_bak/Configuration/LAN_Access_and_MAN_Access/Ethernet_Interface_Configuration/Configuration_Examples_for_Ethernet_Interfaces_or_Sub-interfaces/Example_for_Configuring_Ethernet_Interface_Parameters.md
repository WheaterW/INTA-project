Example for Configuring Ethernet Interface Parameters
=====================================================

In this example, two interconnected Ethernet interfaces work at different rates, causing the link to go Down.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172362794__fig_dc_vrp_ethernet_cfg_001501), Ethernet electrical interfaces on Device A, Device B, and Device C are connected to the IP network 10.1.1.0/24, and an IP address is configured for each interface. Device A and Device B can ping each other but Device A and Device C cannot ping each other. It is found that the link between Device A and Device C is Down and the rate of GE 0/1/1 on Device A is 100 Mbit/s and the rate of GE 0/1/1 on Device B 10 Mbit/s.

**Figure 1** Networking for configuring Ethernet interface parameters![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 represents GE0/1/1.


  
![](figure/en-us_image_0000001690923210.png)

#### Precautions

* Rates of the Ethernet interfaces at the two ends of a link must be the same.
* After the rate of an interface is changed, you need to restart the interface to make the configuration take effect.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Change the rate of the Ethernet interface on Router C to be the same as the rate of the peer interface.
   
   If both Ethernet interfaces support auto-negotiation, configure the interfaces to work in the default auto-negotiation mode. In this mode, the interfaces automatically negotiate their rate and duplex mode.
2. Assign an IP address to each interface of the Router for communication at the network layer.

#### Data Preparation

To complete the configuration, you need the following data:

* All devices in this example support the auto-negotiation mode, and parameters of all the Ethernet interfaces adopt the default values.

#### Procedure

1. Configure Device A.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [HUAWEI] sysname DeviceA
   ```
   ```
   [HUAWEI] commit
   ```
   ```
   [~DeviceA] interface gigabitethernet 0/1/1
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] description DeviceA to Ethernet
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] speed auto
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] duplex auto
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] shutdown
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] ip address 10.1.1.1 255.255.255.0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] quit
   ```
2. Configure Device B.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [HUAWEI] sysname DeviceB
   ```
   ```
   [HUAWEI] commit
   ```
   ```
   [~DeviceB] interface gigabitethernet 0/1/1
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/1] description DeviceB to Ethernet
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/1] speed auto
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/1] duplex auto
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/1] shutdown
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/1] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/1] ip address 10.2.1.2 255.255.255.0
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/1] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/1] quit
   ```
3. Configure Device C.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [HUAWEI] sysname DeviceC
   ```
   ```
   [HUAWEI] commit
   ```
   ```
   [~DeviceC] interface gigabitethernet 0/1/1
   ```
   ```
   [~DeviceC-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [~DeviceC-GigabitEthernet0/1/1] description DeviceC to Ethernet
   ```
   ```
   [~DeviceC-GigabitEthernet0/1/1] speed auto
   ```
   ```
   [~DeviceC-GigabitEthernet0/1/1] duplex auto
   ```
   ```
   [~DeviceC-GigabitEthernet0/1/1] shutdown
   ```
   ```
   [~DeviceC-GigabitEthernet0/1/1] commit
   ```
   ```
   [~DeviceC-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [~DeviceC-GigabitEthernet0/1/1] ip address 10.3.1.3 255.255.255.0
   ```
   ```
   [~DeviceC-GigabitEthernet0/1/1] commit
   ```
   ```
   [~DeviceC-GigabitEthernet0/1/1] quit
   ```
4. Verify the configuration.
   
   
   
   After the configurations are complete, you can use the following methods to check whether the Ethernet interfaces work properly.
   
   * Run the **display interface brief** or **display interface gigabitethernet 0/1/1** command repeatedly on each Router.
     
     + Check whether statistics about error frames remain the same on the Routers. If the statistics remain the same, the Ethernet interfaces work properly.
     + Check whether the physical status and protocol status of each interface are Up.
       
       After the rate of GE 0/1/1 on Device C is changed, the link between Device C and Device A goes Up.
   * When traffic is light, use one Router to ping the Ethernet interface address on another Router, and then check whether all ping packets are replied.
     
     After the rate of GE 0/1/1 on Device C is changed, Device C and Device A can ping each other.
   
   Use the command output on Device A as an example.
   
   ```
   <DeviceA> display interface brief
   ```
   ```
   PHY: Physical
   *down: administratively down
   ^down: standby
   (l): loopback
   (s): spoofing
   (E): E-Trunk down
   (b): BFD down
   (B): Bit-error-detection down
   (e): ETHOAM down
   (d): Dampening Suppressed
   (p): port alarm down
   (ld): loop-detect trigger down
   (td): transceiver unmatch down
   (mf): mac-flapping blocked
   (c): CFM down
   (sd): STP instance discarding
   (D): DF backup down
   InUti/OutUti: input utility/output utility
   Interface                        PHY   Protocol  InUti OutUti   inErrors  outErrors
   GigabitEthernet0/1/1             up    up        0%    0%       0         0
   
   ```
   ```
   <DeviceA> display interface gigabitethernet 0/1/1
   ```
   ```
   GigabitEthernet0/1/1 current state : UP (ifindex: 6)
   Line protocol current state : UP
   Last line protocol up time :  2013-07-29 15:39:29
   Description:RouterA to Ethernet
   Route Port,The Maximum Transmit Unit is 9600
   Internet protocol processing : enabled
   IP Sending Frames' Format is PKTFMT_ETHNT_2, Hardware address is 00e0-fc12-3456
   Last physical up time   :  2013-07-29 15:39:23
   Last physical down time : 2013-07-29 15:38:41
   Current system time: 2013-07-30 09:15:33
   Statistics last cleared:never
         Last 300 seconds input rate: 23513 bits/sec, 2 packets/sec
         Last 300 seconds output rate: 64319 bits/sec, 3 packets/sec
         Input peak rate 26099 bits/sec, Record time: 2013-07-29 15:40:58
         Output peak rate 64809 bits/sec, Record time: 2013-07-30 03:59:41
         Input: 183126871 bytes, 182525 packets 
         Output: 509287017 bytes, 244628 packets
       Input:
         Unicast: 55 packets, Multicast: 160762 packets
         Broadcast: 21708 packets, JumboOctets: 31031 packets
         CRC: 0 packets, Symbol: 0 packets
         Overrun: 0 packets, InRangeLength: 0 packets
         LongPacket: 0 packets, Jabber: 0 packets, Alignment: 0 packets
         Fragment: 0 packets, Undersized Frame: 0 packets
         RxPause: 0 packets
       Output:
         Unicast: 53 packets, Multicast: 243990 packets
         Broadcast: 585 packets, JumboOctets: 0 packets
         Lost: 0 packets, Overflow: 0 packets, Underrun: 0 packets
         System: 0 packets, Overruns: 0 packets
         TxPause: 0 packets
       Last 300 seconds input utility rate:  0.01%
       Last 300 seconds output utility rate: 0.01%
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
  interface GigabitEthernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.1.1 255.255.255.0
  ```
  ```
   description DeviceA to Ethernet
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
  interface GigabitEthernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.2.1.2 255.255.255.0
  ```
  ```
   description DeviceB to Ethernet
  ```
  ```
  #
  ```
  ```
  return
  ```
* Device C configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceC
  ```
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
   ip address 10.3.1.3 255.255.255.0
  ```
  ```
   description DeviceC to Ethernet
  ```
  ```
  #
  ```
  ```
  return
  ```