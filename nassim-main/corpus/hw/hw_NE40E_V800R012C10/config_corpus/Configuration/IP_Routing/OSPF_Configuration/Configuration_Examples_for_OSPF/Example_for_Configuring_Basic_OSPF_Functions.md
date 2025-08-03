Example for Configuring Basic OSPF Functions
============================================

This section describes how to configure basic OSPF functions, including enabling OSPF on each router and specifying network segments in different areas.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172365646__fig_dc_vrp_ospf_cfg_009401), all Routers run OSPF, and the entire AS is divided into three areas. DeviceA and DeviceB function as ABRs to forward interâarea routes.

After the configuration is complete, each Router should learn the routes to all network segments in the AS.

**Figure 1** Networking for configuring basic OSPF functions![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](images/fig_dc_vrp_ospf_cfg_009401.png)  


#### Precautions

When configuring basic OSPF functions, note the following rules:

* The backbone area is responsible for forwarding inter-area routes. In addition, the routing information between non-backbone areas must be forwarded through the backbone area. OSPF defines the following rules for the backbone area:
  
  + Connectivity must be available between non-backbone areas and the backbone area.
  + Connectivity must be available over the backbone area.
* The intervals at which Hello, Dead, and Poll packets are sent on the local interface must be the same as those on the remote interface. Otherwise, the OSPF neighbor relationship cannot be established.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable OSPF on each Router.
2. Specify network segments in different areas.
3. Configure ciphertext authentication for the OSPF area.

#### Data Preparation

To complete the configuration, you need the following data:

| Device Name | Router ID | Process ID | IP Address |
| --- | --- | --- | --- |
| Device A | 1.1.1.1 | 1 | Area 0: 192.168.0.0/24  Area 1: 192.168.1.0/24 |
| Device B | 2.2.2.2 | 1 | Area 0: 192.168.0.0/24  Area 2: 192.168.2.0/24 |
| Device C | 3.3.3.3 | 1 | Area 1: 192.168.1.0/24 and 172.16.1.0/24 |
| Device D | 4.4.4.4 | 1 | Area 2: 192.168.2.0/24 and 172.17.1.0/24 |
| Device E | 5.5.5.5 | 1 | Area 1: 172.16.1.0/24 |
| Device F | 6.6.6.6 | 1 | Area 2: 172.17.1.0/24 |



#### Procedure

1. Assign an IP address to each interface. For configuration details, see [Configuration Files](#EN-US_TASK_0172365646__section_dc_vrp_ospf_cfg_009406) in this section.
2. Configure basic OSPF functions.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] router id 1.1.1.1
   ```
   ```
   [*DeviceA] ospf 1
   ```
   ```
   [*DeviceA-ospf-1] area 0
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.0] network 192.168.0.0 0.0.0.255
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [*DeviceA-ospf-1] area 1
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.1] network 192.168.1.0 0.0.0.255
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.1] quit
   ```
   ```
   [*DeviceA-ospf-1] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] router id 2.2.2.2
   ```
   ```
   [*DeviceB] ospf 1
   ```
   ```
   [*DeviceB-ospf-1] area 0
   ```
   ```
   [*DeviceB-ospf-1-area-0.0.0.0] network 192.168.0.0 0.0.0.255
   ```
   ```
   [*DeviceB-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [*DeviceB-ospf-1] area 2
   ```
   ```
   [*DeviceB-ospf-1-area-0.0.0.2] network 192.168.2.0 0.0.0.255
   ```
   ```
   [*DeviceB-ospf-1-area-0.0.0.2] quit
   ```
   ```
   [*DeviceB-ospf-1] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] router id 3.3.3.3
   ```
   ```
   [*DeviceC] ospf 1
   ```
   ```
   [*DeviceC-ospf-1] area 1
   ```
   ```
   [*DeviceC-ospf-1-area-0.0.0.1] network 192.168.1.0 0.0.0.255
   ```
   ```
   [*DeviceC-ospf-1-area-0.0.0.1] network 172.16.1.0 0.0.0.255
   ```
   ```
   [*DeviceC-ospf-1-area-0.0.0.1] commit
   ```
   ```
   [~DeviceC-ospf-1-area-0.0.0.1] quit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] router id 4.4.4.4
   ```
   ```
   [*DeviceD] ospf 1
   ```
   ```
   [*DeviceD-ospf-1] area 2
   ```
   ```
   [*DeviceD-ospf-1-area-0.0.0.2] network 192.168.2.0 0.0.0.255
   ```
   ```
   [*DeviceD-ospf-1-area-0.0.0.2] network 172.17.1.0 0.0.0.255
   ```
   ```
   [*DeviceD-ospf-1-area-0.0.0.2] commit
   ```
   ```
   [~DeviceD-ospf-1-area-0.0.0.2] quit
   ```
   
   # Configure DeviceE.
   
   ```
   [~DeviceE] router id 5.5.5.5
   ```
   ```
   [~DeviceE] ospf 1
   ```
   ```
   [*DeviceE-ospf-1] area 1
   ```
   ```
   [*DeviceE-ospf-1-area-0.0.0.1] network 172.16.1.0 0.0.0.255
   ```
   ```
   [*DeviceE-ospf-1-area-0.0.0.1] commit
   ```
   ```
   [~DeviceE-ospf-1-area-0.0.0.1] quit
   ```
   
   # Configure DeviceF.
   
   ```
   [~DeviceF] router id 6.6.6.6
   ```
   ```
   [~DeviceF] ospf 1
   ```
   ```
   [*DeviceF-ospf-1] area 2
   ```
   ```
   [*DeviceF-ospf-1-area-0.0.0.2] network 172.17.1.0 0.0.0.255
   ```
   ```
   [*DeviceF-ospf-1-area-0.0.0.2] commit
   ```
   ```
   [~DeviceF-ospf-1-area-0.0.0.2] quit
   ```
3. Configure ciphertext authentication for the OSPF area.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] ospf 1
   ```
   ```
   [*DeviceA-ospf-1] area 0
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.0] authentication-mode hmac-sha256 1 cipher YsHsjx_202206
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [*DeviceA-ospf-1] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] ospf 1
   ```
   ```
   [*DeviceB-ospf-1] area 0
   ```
   ```
   [*DeviceB-ospf-1-area-0.0.0.0] authentication-mode hmac-sha256 1 cipher YsHsjx_202206
   ```
   ```
   [*DeviceB-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [*DeviceB-ospf-1] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Device B and Device A must be configured with the same password. Otherwise, the neighbor relationship cannot be established.
4. Verify the configuration.
   
   
   
   # Display the OSPF neighbors of DeviceA.
   
   ```
   [~DeviceA] display ospf peer
   ```
   ```
   (M) Indicates MADJ neighbor
              OSPF Process 1 with Router ID 1.1.1.1
                     Neighbors
   
    Area 0.0.0.0 interface 192.168.0.1(GigabitEthernet0/1/0)'s neighbors
    Router ID: 2.2.2.2      Address: 192.168.0.2
     State: Full  Mode:Nbr is  Master  Priority: 1
      DR: 192.168.0.2   BDR: 192.168.0.1   MTU: 0
      Dead timer due in 36  sec
      Retrans timer interval: 5
      Neighbor is up for 1h15m4s
      Neighbor up time : 2020-06-08 01:41:57
      Authentication Sequence: [ 0 ]
   
    Area 0.0.0.1 interface 192.168.1.1(GigabitEthernet0/2/0)'s neighbors
    Router ID: 3.3.3.3       Address: 192.168.1.2
     State: Full  Mode:Nbr is  Master  Priority: 1
      DR: 192.168.1.2   BDR: 192.168.1.1   MTU: 0
      Dead timer due in 39  sec
      Retrans timer interval: 5
      Neighbor is up for 1h15m4s
      Neighbor up time : 2020-06-08 01:41:57
      Authentication Sequence: [ 0 ]
   ```
   
   # Display the OSPF routes of DeviceA.
   
   ```
   [~DeviceA] display ospf routing
   ```
   ```
             OSPF Process 1 with Router ID 1.1.1.1
                      Routing Tables
   
    Routing for Network
    Destination        Cost       Type       NextHop         AdvRouter       Area
    172.16.1.0/24      2          Transit    192.168.1.2     3.3.3.3         0.0.0.1
    172.17.1.0/24      3          Inter-area 192.168.0.2     2.2.2.2         0.0.0.0
    192.168.2.0/24     2          Inter-area 192.168.0.2     2.2.2.2         0.0.0.0
   
    Total Nets: 3
    Intra Area: 1  Inter Area: 2  ASE: 0  NSSA: 0    
   ```
   
   # Display the LSDB of DeviceA.
   
   ```
   [~DeviceA] display ospf lsdb
   ```
   ```
             OSPF Process 1 with Router ID 1.1.1.1
                     Link State Database
   
                             Area: 0.0.0.0
    Type      LinkState ID    AdvRouter        Age  Len   Sequence       Metric
    Router    1.1.1.1         1.1.1.1           93  48    80000004            1
    Router    2.2.2.2         2.2.2.2           92  48    80000004            1
    Sum-Net   172.16.1.0      1.1.1.1         1287  28    80000002            2
    Sum-Net   192.168.1.0     1.1.1.1         1716  28    80000001            1
    Sum-Net   172.17.1.0      2.2.2.2         1336  28    80000001            2
    Sum-Net   192.168.2.0     2.2.2.2           87  28    80000002            1
   
                             Area: 0.0.0.1
    Type      LinkState ID    AdvRouter        Age  Len   Sequence       Metric
    Router    1.1.1.1         1.1.1.1         1420  48    80000002            1
    Router    3.3.3.3         3.3.3.3         1294  60    80000003            1
    Router    5.5.5.5         5.5.5.5         1296  36    80000002            1
    Network   172.16.1.1      3.3.3.3         1294  32    80000001            0
    Sum-Net   172.17.1.0      1.1.1.1         1325  28    80000001            3
    Sum-Net   192.168.0.0     1.1.1.1         1717  28    80000001            1
    Sum-Net   192.168.2.0     1.1.1.1         1717  28    80000001            2
   ```
   
   # Display the routing table on DeviceD and perform the ping operation to test the connectivity.
   
   ```
   [~DeviceD] display ospf routing
   ```
   ```
             OSPF Process 1 with Router ID 4.4.4.4
                      Routing Tables
   
    Routing for Network
    Destination        Cost       Type       NextHop         AdvRouter       Area
    172.16.1.0/24      4          Inter-area 192.168.2.1     2.2.2.2         0.0.0.2
    192.168.0.0/24     2          Inter-area 192.168.2.1     2.2.2.2         0.0.0.2
    192.168.1.0/24     3          Inter-area 192.168.2.1     2.2.2.2         0.0.0.2
   
    Total Nets: 3
    Intra Area: 0  Inter Area: 3  ASE: 0  NSSA: 0
   ```
   ```
   [~DeviceD] ping 172.16.1.1
   ```
   ```
     PING 172.16.1.1: 56  data bytes, press CTRL_C to break
       Reply from 172.16.1.1: bytes=56 Sequence=1 ttl=253 time=62 ms
       Reply from 172.16.1.1: bytes=56 Sequence=2 ttl=253 time=16 ms
       Reply from 172.16.1.1: bytes=56 Sequence=3 ttl=253 time=62 ms
       Reply from 172.16.1.1: bytes=56 Sequence=4 ttl=253 time=94 ms
       Reply from 172.16.1.1: bytes=56 Sequence=5 ttl=253 time=63 ms
   
     --- 172.16.1.1 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 16/59/94 ms
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
  router id 1.1.1.1
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.0.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.1.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 192.168.0.0 0.0.0.255
  ```
  ```
    authentication-mode hmac-sha256 1 cipher %^%#c;\wJ4Qi8I1FMGM}KmIK9rha/.D.!$"~0(Ep66z~%^%#
  ```
  ```
   area 0.0.0.1
  ```
  ```
    network 192.168.1.0 0.0.0.255
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
  router id 2.2.2.2
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.0.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.2.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 192.168.0.0 0.0.0.255
  ```
  ```
    authentication-mode hmac-sha256 1 cipher %^%#c;\wJ4Qi8I1FMGM}KmIK9rha/.D.!$"~0(Ep66z~%^%#
  ```
  ```
   area 0.0.0.2
  ```
  ```
    network 192.168.2.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceC configuration file
  
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
  router id 3.3.3.3
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown 
  ```
  ```
   ip address 192.168.1.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 172.16.1.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.1
  ```
  ```
    network 192.168.1.0 0.0.0.255
  ```
  ```
    network 172.16.1.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceD configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceD
  ```
  ```
  #
  ```
  ```
  router id 4.4.4.4
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.2.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 172.17.1.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.2
  ```
  ```
    network 192.168.2.0 0.0.0.255
  ```
  ```
    network 172.17.1.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceE configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceE
  ```
  ```
  #
  ```
  ```
  router id 5.5.5.5
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 172.16.1.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.1
  ```
  ```
    network 172.16.1.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceF configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceF
  ```
  ```
  #
  ```
  ```
  router id 6.6.6.6
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 172.17.1.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.2
  ```
  ```
    network 172.17.1.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  return
  ```