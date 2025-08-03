Example for Configuring Queue Scheduling for an ATM PVC
=======================================================

This section provides an example for configuring queue scheduling on ATM PVCs.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172371699__fig_dc_ne_qos_qos_cfg_01261201), interface3 of DeviceA connects to interface1 of DeviceB. Server, PC1, and PC2 can access the Internet through DeviceA and DeviceB. Server, PC1, and interface1 of DeviceA are in the same network segment. PC2 and interface2 of DeviceA are in the same network segment.

To avoid congestion when huge traffic enters the ATM network, it is required that traffic shaping and queue scheduling be configured on interface4 of DeviceB.

**Figure 1** Networking diagram for configuring queue scheduling of ATM PVCs![](../../../../public_sys-resources/note_3.0-en-us.png) 

interfaces 1 through 4 in this example represent GE0/1/0, GE0/2/0, GE0/1/1, and ATM0/2/0 respectively.


  
![](images/fig_dc_ne_qos_cfg_01261201.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IP addresses for interfaces and the route.
2. Configure IPoA on DeviceB.
3. Configure the traffic shaping for the ATM PVC on ATM 0/2/0 of DeviceB.
4. Configure the queue scheduling for the ATM PVC on ATM 0/2/0 of DeviceB.

#### Data Preparation

To complete the configuration, you need the following data:

* PVC name and VPI or VCI number
* Traffic shaping rate
* Queue name, queue scheduling type, and WFQ weight

#### Procedure

1. Configure IP addresses and routes to ensure normal operation of the network (omitted).
2. Create a PVC and configure IPoA mapping of the PVC (omitted).
   
   
   
   For details of the configurations, refer to "ATM Configuration" in the HUAWEI NE40E-M2 series Universal Service Router *Configuration Guide* - *WAN Access*.
3. Configure the simple traffic classification on GE 1/0/0 of DeviceB.
   
   
   ```
   <DeviceB> system-view
   ```
   ```
   [~DeviceB] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] ip address 10.1.2.1 255.0.0.0
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] trust upstream default
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] return
   ```
4. Configure the traffic shaping and queue scheduling for the ATM PVC on DeviceB.
   
   
   ```
   <DeviceB> system-view
   ```
   ```
   [~DeviceB] atm service cbr-name cbr 100 2000
   ```
   ```
   [~DeviceB] interface atm 0/2/0
   ```
   ```
   [~DeviceB-Atm0/2/0] pvc 0/40
   ```
   ```
   [*DeviceB-atm-pvc-Atm0/2/0-0/40] shutdown
   ```
   ```
   [*DeviceB-atm-pvc-Atm0/2/0-0/40] service output cbr-name
   ```
   ```
   [*DeviceB-atm-pvc-Atm0/2/0-0/40] pvc-queue ef pq outbound
   ```
   ```
   [*DeviceB-atm-pvc-Atm0/2/0-0/40] pvc-queue af4 wfq 50 outbound
   ```
   ```
   [*DeviceB-atm-pvc-Atm0/2/0-0/40] undo shutdown
   ```
   ```
   [*DeviceB-atm-pvc-Atm0/2/0-0/40] commit
   ```
   ```
   [~DeviceB-atm-pvc-Atm0/2/0-0/40] return
   ```
5. Verify the configuration.
   
   
   
   Run the **display atm pvc-queue** command on DeviceB and view the queue scheduling information about PVC 0/40 on ATM 0/2/0. For example:
   
   ```
   <DeviceB> display atm pvc-queue interface atm 0/2/0 pvc 0/40
   ```
   ```
   Show CBQ PVC configuration of interface Atm0/2/0 PVC 0/40:
   ```
   ```
     be  distribute OutBound wfq Weight 20
   ```
   ```
     af1 distribute OutBound wfq Weight 20
   ```
   ```
     af2 distribute OutBound wfq Weight 20
   ```
   ```
     af3 distribute OutBound wfq Weight 20
   ```
   ```
     af4 distribute OutBound wfq Weight 50
   ```
   ```
     ef  distribute OutBound pq
   ```
   ```
     cs6 distribute OutBound wfq Weight 20
   ```
   ```
     cs7 distribute OutBound wfq Weight 20
   ```

#### Configuration Files

* Configuration file of DeviceA
  
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
  interface gigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
  ip address 1.1.1.10 255.0.0.0
  ```
  ```
  #
  ```
  ```
  interface gigabitEthernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
  ip address 10.1.2.2 255.0.0.0
  ```
  ```
  #
  ```
  ```
  interface gigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
  ip address 10.1.1.1 255.0.0.0
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
    network 1.0.0.0 0.255.255.255
  ```
  ```
    network 10.0.0.0 0.255.255.255
  ```
  ```
  network 20.0.0.0 0.255.255.255
  ```
  ```
  #   
  ```
  ```
  return
  ```
* Configuration file of DeviceB
  
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
  atm service cbr-name cbr 100 2000
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet1/0/0
  ```
  ```
   undo shutdown
  ```
  ```
  ip address 10.1.2.1 255.0.0.0
  ```
  ```
  trust upstream default
  ```
  ```
  #
  ```
  ```
  interface Atm0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
  ip address 10.1.3.1 255.0.0.0
  ```
  ```
   pvc 0/40
  ```
  ```
    map ip 192.168.160.2
  ```
  ```
  service output cbr-name
  ```
  ```
  pvc-queue ef pq outbound
  ```
  ```
  pvc-queue af4 wfq 50 outbound
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
    network 20.0.0.0 0.255.255.255
  ```
  ```
  network 30.0.0.0 0.255.255.255
  ```
  ```
  #
  ```
  ```
  return
  ```