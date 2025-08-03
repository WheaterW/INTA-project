Example for Configuring STAMP
=============================

This section provides an example for configuring STAMP in a basic IPv4 static route scenario.

#### Networking Requirements

DeviceA, DeviceB, and DeviceC are three devices on the network shown in [Figure 1](#EN-US_TASK_0000001389132440__fig_dc_vrp_twamp_cfg_001001). It is required that link quality be monitored through simple configurations. By deploying STAMP on DeviceA and DeviceC, you can configure each of them to function as both the Session-Sender and Session-Reflector to collect packet loss and delay statistics.

**Figure 1** Configuring STAMP![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent GE0/1/0 and GE0/2/0, respectively.


  
![](figure/en-us_image_0000001389191068.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IP address and a routing protocol for each involved interface so that all devices can communicate at the network layer.
2. Configure STAMP on DeviceA and DeviceC.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of interfaces on DeviceA: 10.3.3.3 and 10.1.1.1
* IP addresses of interfaces on DeviceB: 10.1.1.2 and 10.2.2.1
* IP addresses of interfaces on DeviceC: 10.4.4.4 and 10.2.2.2

#### Procedure

1. Configure DeviceA, DeviceB, and DeviceC to be reachable at the network layer. For configuration details, see the configuration files.
2. Configure STAMP on DeviceA.
   
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] nqa stamp
   ```
   ```
   [*DeviceA-stamp] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-Gigabitethernet0/1/0] ip address 10.1.1.1 24
   ```
   ```
   [*DeviceA-Gigabitethernet0/1/0] stamp ipv4 enable nexthop-ip 10.2.2.2
   ```
   ```
   [*DeviceA-Gigabitethernet0/1/0] quit
   ```
   ```
   [*DeviceA] commit
   ```
3. Configure STAMP on DeviceB.
   
   
   ```
   <DeviceC> system-view
   ```
   ```
   [~DeviceC] nqa stamp
   ```
   ```
   [*DeviceC-stamp] quit
   ```
   ```
   [*DeviceC] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceC-Gigabitethernet0/1/0] ip address 10.2.2.2 24
   ```
   ```
   [*DeviceC-Gigabitethernet0/1/0] stamp ipv4 enable nexthop-ip 10.1.1.1
   ```
   ```
   [*DeviceC-Gigabitethernet0/1/0] quit
   ```
   ```
   [*DeviceC] commit
   ```
4. Verify the configuration.
   
   
   
   # Check real-time STAMP session statistics on DeviceA.
   
   ```
   [~DeviceA] display stamp ipv4 test-session interface gigabitethernet 0/1/0
   ```
   ```
   Session ID                       : 2147483647
   Session Type                     : dynamic
   State                            : active
   Type                             : continual
   Sender IP                        : 10.1.1.1
   Sender Port                      : 50862
   Reflector IP                     : 10.2.2.2
   Reflector Port                   : 862
   Mode                             : unauthenticated
   DSCP                             : 0
   VPN Instance                     : -
   Interface                        : Gigabitethernet0/1/0
   Last Start Time                  : 2022-10-29 07:18:51
   Last Stop Time                   : never
   Period Time(in millisecond)      : 1000
   Time Out(in second)              : 5
   ```
   
   # Check two-way delay statistics of STAMP sessions on DeviceA.
   
   ```
   [~DeviceA] display stamp ipv4 statistic-type twoway-delay interface gigabitethernet 0/1/0
   ```
   ```
   Latest two-way delay statistics(usec):
   --------------------------------------------------------------------------------
        Index      Delay(Avg)  Jitter(Avg)    Tx-Jitter(Avg)   Rx-Jitter(Avg) 
   --------------------------------------------------------------------------------
            1             629          227                56              580
            2             533          186                34              350
            3             936          611                57              564
            4             530           93                44              453
            5             634          127                56              469
            6             618          171                46              453
            7             532          106                34              341
            8             542          157                36              341
            9             784          489                46              350
           10             619          171                24              230
           11             547          142                45              453
           12             668          246                69              675
           13             626          241                47              469
           14             510          146                46              477
           15             858          448                35              350
           16             658          131                36              341
           17             628          213                24              350
   --------------------------------------------------------------------------------
   Average Delay    :        638    Average Jitter   :        230
   Maximum Delay    :       2596    Maximum Jitter   :       1864
   Minimum Delay    :        335    Minimum Jitter   :          5
   Average TxJitter :         43    Average RxJitter :        426
   Maximum TxJitter :        107    Maximum RxJitter :       1073
   Minimum TxJitter :          0    Minimum RxJitter :          0
   ```
   
   # Check two-way packet loss statistics of STAMP sessions on DeviceA.
   
   ```
   [~DeviceA] display stamp ipv4 statistic-type twoway-loss interface gigabitethernet 0/1/0
   ```
   ```
   Latest two-way loss statistics:
   --------------------------------------------------------------------------------
        Index      Loss count      Loss ratio      Error count      Error ratio
   --------------------------------------------------------------------------------
            1               0         0.0000%                0          0.0000%
            2               0         0.0000%                0          0.0000%
            3               0         0.0000%                0          0.0000%
            4               0         0.0000%                0          0.0000%
            5               0         0.0000%                0          0.0000%
            6               0         0.0000%                0          0.0000%
            7               0         0.0000%                0          0.0000%
            8               0         0.0000%                0          0.0000%
            9               0         0.0000%                0          0.0000%
           10               0         0.0000%                0          0.0000%
           11               0         0.0000%                0          0.0000%
           12               0         0.0000%                0          0.0000%
           13               0         0.0000%                0          0.0000%
           14               0         0.0000%                0          0.0000%
           15               0         0.0000%                0          0.0000%
           16               0         0.0000%                0          0.0000%
           17               0         0.0000%                0          0.0000%
           18               0         0.0000%                0          0.0000%
           19               0         0.0000%                0          0.0000%
           20               0         0.0000%                0          0.0000%
           21               0         0.0000%                0          0.0000%
   --------------------------------------------------------------------------------
   Average Loss Count   :          0    Average Loss Ratio   :   0.0000%
   Maximum Loss Count   :          0    Maximum Loss Ratio   :   0.0000%
   Minimum Loss Count   :          0    Minimum Loss Ratio   :   0.0000%
   Average RxError Count:          0    Average RxError Ratio:   0.0000%
   Maximum RxError Count:          0    Maximum RxError Ratio:   0.0000%
   Minimum RxError Count:          0    Minimum RxError Ratio:   0.0000%
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  #
  interface Gigabitethernet0/1/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   stamp ipv4 enable nexthop-ip 10.2.2.2
  #
  interface Gigabitethernet0/2/0
   undo shutdown
   ip address 10.3.3.3 255.255.255.0
  #
  ip route-static 0.0.0.0 0.0.0.0 10.1.1.2
  #
  nqa stamp
  #
  return
  ```
* DeviceB configuration file
  
  ```
  #
  sysname DeviceB
  #
  interface Gigabitethernet0/1/0
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
  #
  interface Gigabitethernet0/2/0
   undo shutdown
   ip address 10.2.2.1 255.255.255.0
  #
  ip route-static 10.3.3.0 255.255.255.0 10.1.1.1
  ip route-static 10.4.4.0 255.255.255.0 10.2.2.2
  #
  return
  ```
* DeviceC configuration file
  
  ```
  #
  sysname DeviceC
  #
  interface Gigabitethernet0/1/0
   undo shutdown
   ip address 10.2.2.2 255.255.255.0
   stamp ipv4 enable nexthop-ip 10.1.1.1
  #
  interface Gigabitethernet0/2/0
   undo shutdown
   ip address 10.4.4.4 255.255.255.0
  #
  ip route-static 0.0.0.0 0.0.0.0 10.2.2.1
  #
  nqa stamp
  #
  return
  ```