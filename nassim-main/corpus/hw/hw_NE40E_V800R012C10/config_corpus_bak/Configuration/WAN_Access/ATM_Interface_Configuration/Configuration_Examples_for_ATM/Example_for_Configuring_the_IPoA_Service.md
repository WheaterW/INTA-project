Example for Configuring the IPoA Service
========================================

This example describes how to configure IPoA to allow IP packets to be transmitted along ATM Permanent Virtual Circuits (PVCs) in typical networking.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172364344__fig_dc_vrp_cfg_01406401), Device A, Device B, and Device C access an ATM network for communication. All the PVCs on the ATM interfaces of Routers must be configured with IPoA.

**Figure 1** Networking for IPoA configuration![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 in this example is ATM0/1/0.


  
![](images/fig_dc_vrp_cfg_01406401.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create PVCs on the ATM interface of each Router.
2. Configure ATM PVCs to carry IP packets.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of the ATM interfaces on the Routers
* Virtual Path Identifier (VPI)/Virtual Channel Identifier (VCI) values of the PVCs connecting Device A to Device B and Device C
* VPI/VCI values of the PVCs connecting Device B to Device A and Device C
* VPI/VCI values of the PVCs connecting Device C to Device A and Device B

#### Procedure

1. Configure Device A.
   
   
   
   # Enter the ATM interface view and configure an IP address for the ATM interface.
   
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
   [~DeviceA] interface atm 0/1/0
   ```
   ```
   [~DeviceA-Atm0/1/0] ip address 10.1.1.1 255.255.255.0
   ```
   
   # Create PVCs and configure IPoA mapping on the PVCs.
   
   ```
   [*DeviceA-Atm0/1/0] pvc to_b 0/40
   ```
   ```
   [*DeviceA-atm-pvc-Atm0/1/0-0/40-to_b] map ip 10.1.1.2
   ```
   ```
   [*DeviceA-atm-pvc-Atm0/1/0-0/40-to_b] quit
   ```
   ```
   [*DeviceA-Atm0/1/0] pvc to_c 0/41
   ```
   ```
   [*DeviceA-atm-pvc-Atm0/1/0-0/41-to_c] map ip 10.1.1.3
   ```
   ```
   [*DeviceA-atm-pvc-Atm0/1/0-0/41-to_c] quit
   ```
   ```
   [*DeviceA-Atm0/1/0] undo shutdown
   ```
   ```
   [*DeviceA-Atm0/1/0] quit
   ```
   ```
   [*DeviceA] commit
   ```
2. Configure Device B.
   
   
   
   # Enter the ATM interface view and configure an IP address for the ATM interface.
   
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
   [~DeviceB] interface atm 0/1/0
   ```
   ```
   [~DeviceB-Atm0/1/0] ip address 10.1.1.2 255.255.255.0
   ```
   
   # Create PVCs and configure IPoA mapping on the PVCs.
   
   ```
   [*DeviceB-Atm0/1/0] pvc to_a 0/40
   ```
   ```
   [*DeviceB-atm-pvc-Atm0/1/0-0/40-to_a] map ip 10.1.1.1
   ```
   ```
   [*DeviceB-atm-pvc-Atm0/1/0-0/40-to_a] quit
   ```
   ```
   [*DeviceB-Atm0/1/0] pvc to_c 0/42
   ```
   ```
   [*DeviceB-atm-pvc-Atm0/1/0-0/42-to_c] map ip 10.1.1.3
   ```
   ```
   [*DeviceB-atm-pvc-Atm0/1/0-0/42-to_c] quit
   ```
   ```
   [*DeviceB-Atm0/1/0] undo shutdown
   ```
   ```
   [*DeviceB-Atm0/1/0] quit
   ```
   ```
   [*DeviceB] commit
   ```
3. Configure Device C.
   
   
   
   # Enter the ATM interface view and configure an IP address for the ATM interface.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceC
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceC] interface atm 0/1/0
   ```
   ```
   [~DeviceC-Atm0/1/0] ip address 10.1.1.3 255.255.255.0
   ```
   
   # Create PVCs and configure IPoA mapping on the PVCs.
   
   ```
   [*DeviceC-Atm0/1/0] pvc to_a 0/41
   ```
   ```
   [*DeviceC-atm-pvc-Atm0/1/0-0/41-to_a] map ip 10.1.1.1
   ```
   ```
   [*DeviceC-atm-pvc-Atm0/1/0-0/41-to_a] quit
   ```
   ```
   [*DeviceC-Atm0/1/0] pvc to_b 0/42
   ```
   ```
   [*DeviceC-atm-pvc-Atm0/1/0-0/42-to_b] map ip 10.1.1.2
   ```
   ```
   [*DeviceC-atm-pvc-Atm0/1/0-0/42-to_b] quit
   ```
   ```
   [*DeviceC-Atm0/1/0] undo shutdown
   ```
   ```
   [*DeviceC-Atm0/1/0] quit
   ```
   ```
   [*DeviceC] commit
   ```
4. Verify the configuration.
   
   
   
   # Check the PVC status on Device A.
   
   ```
   [~DeviceA] display atm pvc-info
   ```
   ```
    VPI/VCI  |STATE|PVC-NAME        |ENCAP    |PROTOCOL|INTERFACE
   ----------|-----|----------------|---------|--------|-----------------
     0/40    |UP   |to_b            |1        |IP      |Atm0/1/0 (UP)       
     0/41    |UP   |to_c            |2        |IP      |Atm0/1/0 (UP)
   ```
   
   # Check mappings between PVCs and IP addresses on Device A.
   
   ```
   [~DeviceA] display atm map-info
   ```
   ```
   Atm0/1/0, PVC 0/40, IP, State UP
   ```
   ```
     10.1.1.2
   ```
   ```
   Atm0/1/0, PVC 0/41, IP, State UP
   ```
   ```
     10.1.1.3
   ```
   
   Perform the same steps to view the PVC status and mappings between PVCs and IP addresses on Device B and Device C.
   
   # Run the **ping** command on Device A to ping Device B. The ping operation succeeds.
   
   ```
   [~DeviceA] ping 10.1.1.2
   ```
   ```
     PING 10.1.1.2: 56  data bytes, press CTRL_C to break
      Reply from 10.1.1.2: bytes=56 Sequence=1 ttl=255 time=62 ms
       Reply from 10.1.1.2: bytes=56 Sequence=2 ttl=255 time=31 ms
       Reply from 10.1.1.2: bytes=56 Sequence=3 ttl=255 time=31 ms
       Reply from 10.1.1.2: bytes=56 Sequence=4 ttl=255 time=31 ms
       Reply from 10.1.1.2: bytes=56 Sequence=5 ttl=255 time=31 ms
   
     --- 10.1.1.2 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss    round-trip min/avg/max = 31/37/62 ms 
   ```
   
   Run the **ping** command on Device A to ping Device C, on Device B to ping Device A and Device C, and on Device C to ping Device A and Device B. All the ping operations succeed.

#### Configuration Files

* Configuration file of Device A
  
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
   ip address 10.1.1.1 255.255.255.0
  ```
  ```
   pvc to_b 0/40
  ```
  ```
    map ip 10.1.1.2
  ```
  ```
   pvc to_c 0/41
  ```
  ```
    map ip 10.1.1.3
  ```
  ```
  #
  ```
  ```
  return
  ```
* Configuration file of Device B
  
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
   ip address 10.1.1.2 255.255.255.0
  ```
  ```
   pvc to_a 0/40
  ```
  ```
    map ip 10.1.1.1
  ```
  ```
   pvc to_c 0/42
  ```
  ```
    map ip 10.1.1.3
  ```
  ```
  #
  ```
  ```
  return
  ```
* Configuration file of Device C
  
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
   ip address 10.1.1.3 255.255.255.0
  ```
  ```
   pvc to_a 0/41
  ```
  ```
    map ip 10.1.1.1
  ```
  ```
   pvc to_b 0/42
  ```
  ```
    map ip 10.1.1.2
  ```
  ```
  #
  ```
  ```
  return
  ```