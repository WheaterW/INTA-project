Example for Configuring Global UCMP for IP Packet Forwarding
============================================================

This section provides an example for configuring global UCMP for IP packet forwarding.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172365029__fig_dc_ne_loadba_cfg_201001), two paths connect DeviceA and DeviceC.

* A physical link connects DeviceA's GE 0/2/0 and DeviceB's GE 0/2/0.
* DeviceA's GE 0/3/0 and GE 0/3/1 and DeviceB's GE 0/3/0 and GE 0/3/1 are added to Eth-Trunk1.

Eth-Trunk1 contains two GE interfaces, and therefore the bandwidth of Eth-Trunk1 is the sum of the bandwidth of the two member GE links. To load balance IP traffic, configure global UCMP between the two links from DeviceA to DeviceC.

**Figure 1** Configuring global UCMP  
![](images/fig_dc_ne_loadba_cfg_201001.png "Click to enlarge")

**Table 1** Device names, interface names, and IP addresses
| Device Name | Interface Name | IP Address |
| --- | --- | --- |
| DeviceA | GE0/1/0 | 10.1.1.1/24 |
| GE 0/2/0 | 10.30.1.1/24 |
| Eth-Trunk1 | 10.40.1.1/24 |
| DeviceB | GE 0/2/0 | 10.30.1.2/24 |
| Eth-Trunk1 | 10.40.1.2/24 |
| GE0/1/0 | 10.50.1.1/24 |
| DeviceC | GE 0/1/0 | 10.50.1.2/24 |
| GE 0/2/0 | 10.20.1.1/24 |

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, the bandwidths of GE 0/2/0, GE 0/3/0, and GE 0/1/0 on DeviceA and DeviceB are all 1 Gbit/s.



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure static routes on every Router.
2. Enable global UCMP on DeviceA, allowing the two paths between DeviceA and DeviceC to perform UCMP based on bandwidth ratios.

#### Data Preparation

To complete the configuration, you need the following data:

* Type and number of each interface
* IP address of each interface
* Eth-Trunk interface number

#### Procedure

1. Assign an IP address to each physical interface and Eth-Trunk interface. For configuration details, see [Configuration Files](#EN-US_TASK_0172365029__example1280346556214034) in this section.
2. Configure static routes.
   
   
   
   # Configure DeviceA.
   
   ```
   [~RouterA] ip route-static 10.20.1.0 255.255.255.0 gigabitethernet0/2/0 10.30.1.2
   ```
   ```
   [*RouterA] ip route-static 10.20.1.0 255.255.255.0 eth-trunk1 10.40.1.2
   ```
   ```
   [*RouterA] ip route-static 10.50.1.0 255.255.255.0 gigabitethernet0/2/0 10.30.1.2
   ```
   ```
   [*RouterA] ip route-static 10.50.1.0 255.255.255.0 eth-trunk1 10.40.1.2
   ```
   ```
   [*RouterA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~RouterB] ip route-static 10.1.1.0 255.255.255.0 gigabitethernet0/2/0 10.30.1.1
   ```
   ```
   [*RouterB] ip route-static 10.1.1.0 255.255.255.0 eth-trunk1 10.40.1.1
   ```
   ```
   [*DeviceB] ip route-static 10.20.1.0 255.255.255.0 gigabitethernet0/1/0 10.50.1.2
   ```
   ```
   [*RouterB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] ip route-static 10.1.1.0 255.255.255.0 gigabitethernet0/1/0 10.50.1.1
   ```
   ```
   [*DeviceC] ip route-static 10.30.1.0 255.255.255.0 gigabitethernet0/1/0 10.50.1.1
   ```
   ```
   [*DeviceC] ip route-static 10.40.1.0 255.255.255.0 GigabitEthernet0/1/0 10.50.1.1
   ```
   ```
   [*RouterC] commit
   ```
3. Enable global UCMP on DeviceA.
   
   
   ```
   [~RouterA] load-balance unequal-cost enable
   ```
   ```
   [*RouterA] commit
   ```
4. Verify the configuration.
   
   
   
   # Ping DeviceA at 10.1.1.1 from DeviceC. The ping operation is successful. Run the **display interface brief** command to view the bandwidth usage of outbound interfaces. The command output shows that Eth-Trunk1's bandwidth usage is similar to GE 0/2/0's bandwidth usage, meaning that UCMP has been enabled and traffic is load-balanced among outbound interfaces based on the bandwidth ratio.
   
   ```
   [~RouterC] ping -c 100 -t 10 -m 10 10.1.1.1
   ```
   ```
   PING 10.1.1.1: 56  data bytes, press CTRL_C to break
       Reply from 10.1.1.1: bytes=56 Sequence=1 ttl=254 time=3 ms
       Reply from 10.1.1.1: bytes=56 Sequence=2 ttl=254 time=1 ms
       Reply from 10.1.1.1: bytes=56 Sequence=3 ttl=254 time=1 ms
   ...
    --- 10.1.1.1 ping statistics ---
       100 packet(s) transmitted
       99 packet(s) received
       1.00% packet loss
       round-trip min/avg/max = 1/1/6 ms
   ```
   ```
   [~RouterB] display interface brief
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
   Interface                   PHY   Protocol  InUti OutUti   inErrors  outErrors
   Eth-Trunk1                  up    up        0.01%  6.66%          0          0
     GigabitEthernet0/3/0     up    up        0.01%  6.66%          0          0
     GigabitEthernet0/3/1     up    up        0.01%  6.66%          0          0
   GigabitEthernet0/1/0        up    up           0%     0%          0          0
   GigabitEthernet0/2/0       up    up        0.01%  6.67%          0          0
   GigabitEthernet0/2/1        down  down         0%     0%          0          0
   GigabitEthernet0/2/3        down  down         0%     0%          0          0
   GigabitEthernet0/2/4        down  down         0%     0%          0          0
   GigabitEthernet0/2/5        down  down         0%     0%          0          0
   GigabitEthernet0/2/6        down  down         0%     0%          0          0
   GigabitEthernet0/2/7        down  down         0%     0%          0          0
   Ip-Trunk1                   down  down         0%     0%          0          0
   LoopBack0                   down  up(s)        0%     0%          0          0
   NULL0                       up    up           0%     0%          0          0
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
   sysname RouterA
  #
  load-balance unequal-cost enable
  #
  interface Eth-Trunk1
   ip address 10.40.1.1 255.255.255.0
   load-balance packet-all
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.30.1.1 255.255.255.0
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   eth-trunk 1
  #
  interface GigabitEthernet0/3/1
   undo shutdown
   eth-trunk 1
  #
   ip route-static 10.20.1.0 255.255.255.0 GigabitEthernet0/2/0 10.30.1.2
   ip route-static 10.20.1.0 255.255.255.0 Eth-Trunk1 10.40.1.2
   ip route-static 10.50.1.0 255.255.255.0 GigabitEthernet0/2/0 10.30.1.2
   ip route-static 10.50.1.0 255.255.255.0 Eth-Trunk1 10.40.1.2
  #
  return
  ```
* DeviceB configuration file
  
  ```
  #
   sysname RouterB
  #
  interface Eth-Trunk1
   ip address 10.40.1.2 255.255.255.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.30.1.2 255.255.255.0
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.50.1.1 255.255.255.0
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   eth-trunk 1
  #
  interface GigabitEthernet0/3/1
   undo shutdown
   eth-trunk 1
  #
   ip route-static 10.1.1.0 255.255.255.0 GigabitEthernet0/2/0 10.30.1.1
   ip route-static 10.1.1.0 255.255.255.0 Eth-Trunk1 10.40.1.1
   ip route-static 10.20.1.0 255.255.255.0 GigabitEthernet0/1/0  10.50.1.2
  #
  return
  
  ```
* DeviceC configuration file
  
  ```
  #
   sysname RouterC
  #
   ip route-static 10.1.1.0 255.255.255.0 GigabitEthernet0/1/0 10.50.1.1
   ip route-static 10.30.1.0 255.255.255.0 GigabitEthernet0/1/0 10.50.1.1
   ip route-static 10.40.1.0 255.255.255.0 GigabitEthernet0/1/0 10.50.1.1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.20.1.1 255.255.255.0
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.50.1.2 255.255.255.0
  #
  return
  
  ```