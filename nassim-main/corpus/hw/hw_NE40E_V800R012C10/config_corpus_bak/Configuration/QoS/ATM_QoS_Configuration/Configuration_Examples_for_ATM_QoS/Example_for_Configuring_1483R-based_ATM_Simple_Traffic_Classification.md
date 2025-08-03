Example for Configuring 1483R-based ATM Simple Traffic Classification
=====================================================================

This section provides an example for configuring 1483R-based ATM simple traffic classification.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172371690__fig_dc_ne_qos_qos_cfg_01260801), DeviceA, DeviceB, and DeviceC are located at the edge of the ATM network to provide IP network access. The three Routers connect the three PSN networks that are separated by the ATM network. On the ATM network, IP packets are transmitted in AAL5 frames (IPoA services). When IP packets are sent out of the ATM network, the Routers perform ATM termination and forward the packets to other types of interfaces.

* The IP addresses for the ATM interfaces of the three Routers are 1.1.1.1/24, 1.1.1.2/24, and 1.1.1.3/24 respectively.
* On the ATM network, the VPI and VCI of DeviceA are 0/40 and 0/50, which are connected to DeviceB and DeviceC respectively; the VPI and VCI of DeviceB are 0/40 and 0/60, which are connected to DeviceA and DeviceC respectively; the VPI and VCI of DeviceC are 0/50 and 0/60, which are connected to DeviceA and DeviceB.
* All the PVCs on the ATM interfaces of the three Routers adopt IPoA.
* On the outbound interface of DeviceA, enable simple traffic classification, and map the DSCP field of IP packets to the CLP of ATM cells. (In this manner, the QoS capability of the ATM network can serve IP applications.)

**Figure 1** Networking diagram of configuring 1483R-based ATM simple traffic classification![](../../../../public_sys-resources/note_3.0-en-us.png) 

interface1 through in this example is ATM0/1/0.


  
![](images/fig_dc_ne_qos_cfg_01260801.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign IP addresses for interfaces.
2. Configure IPoA mapping on the PVC of each interface.
3. Configure mapping rules for ATM simple traffic classification.
4. Enable simple traffic classification.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses for the ATM interfaces of the three Routers, which are 1.1.1.1/24, 1.1.1.2/24, and 1.1.1.3/24 respectively
* VPI/VCI of DeviceA: 0/40 and 0/50 that are connected to DeviceB and DeviceC respectively
* VPI/VCI of DeviceB: 0/40 and 0/60 that are connected to DeviceA and DeviceC respectively
* VPI/VCI of DeviceC: 0/50 and 0/60 that are connected to DeviceA and DeviceB respectively
* Service type and CLP value

#### Procedure

1. Assign an IP address to the ATM interface and enable simple traffic classification on the interface.
   
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] interface atm 0/1/0
   ```
   ```
   [~DeviceA-Atm0/1/0] undo shutdown
   ```
   ```
   [~DeviceA-Atm0/1/0] ip address 1.1.1.1 255.255.255.0
   ```
   ```
   [*DeviceA-Atm0/1/0] commit
   ```
   ```
   [~DeviceA-Atm0/1/0] return
   ```
   ```
   <DeviceB> system-view
   ```
   ```
   [~DeviceB] interface atm 0/1/0
   ```
   ```
   [~DeviceB-Atm0/1/0] undo shutdown
   ```
   ```
   [~DeviceB-Atm0/1/0] ip address 1.1.1.2 255.255.255.0
   ```
   ```
   [*DeviceA-Atm0/1/0] commit
   ```
   ```
   [~DeviceB-Atm0/1/0] return
   ```
   ```
   <DeviceC> system-view
   ```
   ```
   [~DeviceC] interface atm 0/1/0
   ```
   ```
   [~DeviceC-Atm0/1/0] undo shutdown
   ```
   ```
   [~DeviceC-Atm0/1/0] ip address 1.1.1.3 255.255.255.0
   ```
   ```
   [*DeviceA-Atm0/1/0] commit
   ```
   ```
   [~DeviceC-Atm0/1/0] return
   ```
2. Create a PVC and set the IPoA mapping for the PVC.
   
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] interface atm 0/1/0
   ```
   ```
   [~DeviceA-Atm0/1/0] pvc to_b 0/40
   ```
   ```
   [*DeviceA-atm-pvc-Atm0/1/0-0/40-to_b] map ip 1.1.1.2
   ```
   ```
   [*DeviceA-atm-pvc-Atm0/1/0-0/40-to_b] commit
   ```
   ```
   [~DeviceA-atm-pvc-Atm0/1/0-0/40-to_b] quit
   ```
   ```
   [~DeviceA-Atm0/1/0] pvc to_c 0/50
   ```
   ```
   [*DeviceA-atm-pvc-Atm0/1/0-0/50-to_c] map ip 1.1.1.3
   ```
   ```
   [*DeviceA-atm-pvc-Atm0/1/0-0/50-to_c] commit
   ```
   ```
   [~DeviceA-atm-pvc-Atm0/1/0-0/50-to_c] return
   ```
   ```
   <DeviceB> system-view
   ```
   ```
   [~DeviceB] interface atm 0/1/0
   ```
   ```
   [~DeviceB-Atm0/1/0] pvc to_a 0/40
   ```
   ```
   [*DeviceB-atm-pvc-Atm0/1/0-0/40-to_a] map ip 1.1.1.1
   ```
   ```
   [*DeviceA-Atm0/1/0] commit
   ```
   ```
   [~DeviceB-atm-pvc-Atm0/1/0-0/40-to_a] quit
   ```
   ```
   [~DeviceB-Atm0/1/0] pvc to_c 0/60
   ```
   ```
   [*DeviceB-atm-pvc-Atm0/1/0-0/60-to_c] map ip 1.1.1.3
   ```
   ```
   [*DeviceA-Atm0/1/0] commit
   ```
   ```
   [~DeviceB-atm-pvc-Atm0/1/0-0/60-to_c] return
   ```
   ```
   <~DeviceC> system-view
   ```
   ```
   [~DeviceC] interface atm 0/1/0
   ```
   ```
   [*DeviceC-Atm0/1/0] pvc to_a 0/50
   ```
   ```
   [*DeviceC-atm-pvc-Atm0/1/0-0/50-to_a] map ip 1.1.1.1
   ```
   ```
   [*DeviceC-atm-pvc-Atm0/1/0-0/50-to_a] quit
   ```
   ```
   [*DeviceC-Atm0/1/0] pvc to_b 0/60
   ```
   ```
   [*DeviceC-atm-pvc-Atm0/1/0-0/60-to_b] map ip 1.1.1.2
   ```
   ```
   [*DeviceC-atm-pvc-Atm0/1/0-0/60-to_b] commit
   ```
   ```
   [~DeviceC-atm-pvc-Atm0/1/0-0/60-to_b] return
   ```
3. Configure mapping rules for ATM simple traffic classification and enable simple traffic classification.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If you do not set mapping rules for the downstream, the Router uses the rule in the default domain. If another DS domain is applied to the interface, the Router uses the rule in the user-defined domain.
   
   * For packets that enter the ATM network, enable BA classification.
     
     ```
     <DeviceA> system-view
     ```
     ```
     [~DeviceA] interface atm 0/1/0
     ```
     ```
     [~DeviceA-Atm0/1/0] trust upstream default
     ```
     ```
     [*DeviceA-Atm0/1/0] commit
     ```
     ```
     [~DeviceA-Atm0/1/0] return
     ```
     ```
     <DeviceB> system-view
     ```
     ```
     [~DeviceB] interface atm 0/1/0
     ```
     ```
     [~DeviceB-Atm0/1/0] trust upstream default
     ```
     ```
     [*DeviceA-Atm0/1/0] commit
     ```
     ```
     [~DeviceB-Atm0/1/0] return
     ```
     ```
     <DeviceC> system-view
     ```
     ```
     [~DeviceC] interface atm 0/1/0
     ```
     ```
     [~DeviceC-Atm0/1/0] trust upstream default
     ```
     ```
     [*DeviceC-Atm0/1/0] commit
     ```
     ```
     [~DeviceC-Atm0/1/0] return
     ```
   * For packets that leave the ATM network, as IPoA has been configured, DeviceA, DeviceB, and DeviceC restore the original IP packets before forwarding them.
4. Check the configuration.
   
   
   
   # View the status of the PVC on DeviceA.
   
   ```
   [~DeviceA] display atm pvc-info
   ```
   ```
   VPI/VCI |STATE|PVC-NAME        |INDEX   |ENCAP|PROT |INTERFACE
   ```
   ```
   --------|-----|----------------|--------|-----|-----|---------------------
   ```
   ```
     0/40   |UP    |to_b              |0        |SNAP |IP   |Atm0/1/0 (UP)
   ```
   ```
     0/50   |UP    |to_c              |1        |SNAP |IP   |Atm0/1/0 (UP)
   ```
   
   # View the mapping rule for the PVC on DeviceA.
   
   ```
   [~DeviceA] display atm map-info
   ```
   ```
   Atm0/1/0, PVC 0/40, IP, State UP
   ```
   ```
     1.1.1.2, vlink 393217
   ```
   ```
   Atm0/1/0, PVC 0/50, IP, State UP
   ```
   ```
     1.1.1.3, vlink 393218          
   ```
   
   Similarly, you can view the status of the PVC and the mapping rule on DeviceB and DeviceC.
   
   # On DeviceA, run the **ping** command to ping DeviceB. DeviceA can ping through DeviceB.
   
   ```
   [~DeviceA] ping 1.1.1.2
   ```
   ```
     PING 1.1.1.2: 56  data bytes, press CTRL_C to break
   ```
   ```
       Reply from 1.1.1.2: bytes=56 Sequence=1 ttl=255 time=62 ms
   ```
   ```
       Reply from 1.1.1.2: bytes=56 Sequence=2 ttl=255 time=31 ms
   ```
   ```
       Reply from 1.1.1.2: bytes=56 Sequence=3 ttl=255 time=31 ms
   ```
   ```
       Reply from 1.1.1.2: bytes=56 Sequence=4 ttl=255 time=31 ms
   ```
   ```
       Reply from 1.1.1.2: bytes=56 Sequence=5 ttl=255 time=31 ms
   ```
   ```
     --- 1.1.1.2 ping statistics ---
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
       round-trip min/avg/max = 31/37/62 ms  
   ```
   
   Similarly, DeviceA can ping through DeviceC; DeviceB can ping through DeviceA and DeviceC; DeviceC can ping through DeviceA and DeviceB.

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
  interface Atm0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   trust upstream default
  ```
  ```
  pvc to_b 0/40
  ```
  ```
    map ip 1.1.1.2
  ```
  ```
  pvc to_c 0/50
  ```
  ```
    map ip 1.1.1.3
  ```
  ```
  ip address 1.1.1.1 255.255.255.0
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
  interface Atm0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   trust upstream default
  ```
  ```
   pvc to_a 0/40
  ```
  ```
    map ip 1.1.1.1
  ```
  ```
   pvc to_c 0/60
  ```
  ```
    map ip 1.1.1.3
  ```
  ```
   ip address 1.1.1.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  return
  ```
* Configuration file of DeviceC
  
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
  interface Atm0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   trust upstream default
  ```
  ```
   pvc to_a 0/50
  ```
  ```
    map ip 1.1.1.1
  ```
  ```
   pvc to_b 0/60
  ```
  ```
    map ip 1.1.1.2
  ```
  ```
   ip address 1.1.1.3 255.255.255.0
  ```
  ```
  #
  ```
  ```
  return
  ```