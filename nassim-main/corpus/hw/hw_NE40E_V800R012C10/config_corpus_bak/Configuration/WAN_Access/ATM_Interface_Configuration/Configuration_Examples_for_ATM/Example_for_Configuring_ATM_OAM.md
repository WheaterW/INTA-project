Example for Configuring ATM OAM
===============================

ATM OAM detects links in real time without interrupting services.

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0172364347__fig_dc_ne_cfg_01107601), RouterDevice A, Device B, and Device C are connected to the ATM network. IPoA services are configured on all the PVCs on ATM interfaces of the three Routers.

To implement real-time and continuous detection without interrupting services, configure the OAM CC function.

**Figure 1** Configuring ATM OAM![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 in this example is ATM0/1/0.


  
![](images/fig_dc_ne_cfg_01107601.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IPoA services.
2. Configure the OAM attributes of the connection point.
3. Activate the CC function.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of the ATM interfaces of the three Router
* VPIs/VCIs of Device A connecting to Device B and Device C, respectively
* VPIs/VCIs of Device B connecting to Device A and Device C, respectively
* VPIs/VCIs of Device C connecting to Device A and Device B, respectively

#### Procedure

1. Configure IPoA.
   
   
   
   # Configure Device A.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [HUAWEI] sysname DeviceA
   ```
   ```
   [DeviceA] interface atm 0/1/0
   ```
   ```
   [DeviceA-Atm0/1/0] ip address 202.38.160.1 255.255.255.0
   ```
   ```
   [DeviceA-Atm0/1/0] pvc to_b 0/40
   ```
   ```
   [DeviceA-atm-pvc-Atm0/1/0-0/40-to_b] map ip 202.38.160.2
   ```
   ```
   [DeviceA-atm-pvc-Atm0/1/0-0/40-to_b] quit
   ```
   ```
   [DeviceA-Atm0/1/0] pvc to_c 0/41
   ```
   ```
   [DeviceA-atm-pvc-Atm0/1/0-0/41-to_c] map ip 202.38.160.3
   ```
   ```
   [DeviceA-atm-pvc-Atm0/1/0-0/41-to_c] quit
   ```
   ```
   [DeviceA-Atm0/1/0] undo shutdown
   ```
   
   # Configure Device B.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [HUAWEI] sysname DeviceB
   ```
   ```
   [DeviceB] interface atm 0/1/0
   ```
   ```
   [DeviceB-Atm0/1/0] ip address 202.38.160.2 255.255.255.0
   ```
   ```
   [DeviceB-Atm0/1/0] pvc to_a 0/40
   ```
   ```
   [DeviceB-atm-pvc-Atm0/1/0-0/40-to_a] map ip 202.38.160.1
   ```
   ```
   [DeviceB-atm-pvc-Atm0/1/0-0/40-to_a] quit
   ```
   ```
   [DeviceB-Atm0/1/0] pvc to_c 0/42
   ```
   ```
   [DeviceB-atm-pvc-Atm0/1/0-0/42-to_c] map ip 202.38.160.3
   ```
   ```
   [DeviceB-atm-pvc-Atm0/1/0-0/42-to_c] quit
   ```
   ```
   [DeviceB-Atm0/1/0] undo shutdown
   ```
   
   # Configure Device C.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [HUAWEI] sysname DeviceC
   ```
   ```
   [DeviceC] interface atm 0/1/0
   ```
   ```
   [DeviceC-Atm0/1/0] ip address 202.38.160.3 255.255.255.0
   ```
   ```
   [DeviceC-Atm0/1/0] pvc to_a 0/41
   ```
   ```
   [DeviceC-atm-pvc-Atm0/1/0-0/41-to_a] map ip 202.38.160.1
   ```
   ```
   [DeviceC-atm-pvc-Atm0/1/0-0/41-to_a] quit
   ```
   ```
   [DeviceC-Atm0/1/0] pvc to_b 0/42
   ```
   ```
   [DeviceC-atm-pvc-Atm0/1/0-0/42-to_b] map ip 202.38.160.2
   ```
   ```
   [DeviceC-atm-pvc-Atm0/1/0-0/42-to_b] quit
   ```
   ```
   [DeviceC-Atm0/1/0] undo shutdown
   ```
2. Configure the OAM attributes of the connection point.
   
   
   
   # Configure Device A.
   
   ```
   [DeviceA] interface atm 0/1/0
   ```
   ```
   [DeviceA-Atm0/1/0] oam
   ```
   ```
   [DeviceA-Atm0/1/0-fatm-oam] attribute 0/40 0/41 end-point
   ```
   
   # Configure Device B.
   
   ```
   [DeviceB] interface atm 0/1/0
   ```
   ```
   [DeviceB-Atm0/1/0] oam
   ```
   ```
   [DeviceB-Atm0/1/0-fatm-oam] attribute 0/40 end-point
   ```
   ```
   [DeviceB-Atm0/1/0-fatm-oam] attribute 0/42 end-point
   ```
   
   # Configure Device C.
   
   ```
   [DeviceC] interface atm 0/1/0
   ```
   ```
   [DeviceC-Atm0/1/0] oam
   ```
   ```
   [DeviceC-Atm0/1/0-fatm-oam] attribute 0/41 0/42 end-point
   ```
3. Activate the CC function.
   
   
   
   # Configure Device A.
   
   ```
   [DeviceA] interface atm 0/1/0
   ```
   ```
   [DeviceA-Atm0/1/0] oam
   ```
   ```
   [DeviceA-Atm0/1/0-fatm-oam] cc 0/40 0/41 end-to-end both
   ```
   
   # Configure Device B.
   
   ```
   [DeviceB] interface atm 0/1/0
   ```
   ```
   [DeviceB-Atm0/1/0] oam
   ```
   ```
   [DeviceB-Atm0/1/0-fatm-oam] cc 0/40 end-to-end both
   ```
   ```
   [DeviceB-Atm0/1/0-fatm-oam] cc 0/42 end-to-end both
   ```
   
   # # Configure Device C.
   
   ```
   [DeviceC] interface atm 0/1/0
   ```
   ```
   [DeviceC-Atm0/1/0] oam
   ```
   ```
   [DeviceC-Atm0/1/0-fatm-oam] cc 0/41 0/42 end-to-end both
   ```
4. Verify the configuration.
   
   
   
   # Display the OAM configuration on the Router.
   
   Use the display on Device A as an example:
   
   ```
   <DeviceA> system-view
   ```
   ```
   [DeviceA] interface atm 0/1/0
   ```
   ```
   [DeviceA-Atm0/1/0] oam
   ```
   ```
   [DeviceA-Atm0/1/0-fatm-oam] display atm oam configuration atm 0/1/0
   ```
   ```
   Interface       PVC      Attribute   CC func   CC dir    CC attr
   ---------      -----     ---------   -------   ------    -------
   Atm0/1/0      0/40      end-point   enable    both      end-to-end
   Atm0/1/0      0/41      end-point   enable    both      end-to-endCurrent displayed item(s) is : 2
   ```
   
   # Display the OAM statistics of the PVC on the Router.
   
   Use the display on Device A as an example:
   
   ```
   <DeviceA> display atm oam statistics atm 0/1/0 0/40
   ```
   ```
   Total number of received OAM Cells : 0
   Number of received AIS Cells       : 0
   Number of received RDI Cells       : 0
   Number of received loopback cells  : 0
   Number of received CC cells        : 0
   Number of received crc error cells : 0
   Number of received other cells     : 0
   
   Total number of sent OAM Cells     : 88
   Number of sent AIS Cells           : 0
   Number of sent RDI Cells           : 44
   Number of sent loopback cells      : 0
   Number of sent CC cells            : 44
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
  interface Atm0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 202.38.160.1 255.255.255.0
  ```
  ```
   pvc to_b 0/40
  ```
  ```
     map ip 202.38.160.2
  ```
  ```
   pvc to_c 0/41
  ```
  ```
     map ip 202.38.160.3
  ```
  ```
   oam
  ```
  ```
     attribute 0/40 0/41 end-point
  ```
  ```
     cc 0/40 0/41 end-to-end both
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
  interface Atm0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
    ip address 202.38.160.2 255.255.255.0
  ```
  ```
   pvc to_a 0/40
  ```
  ```
    map ip 202.38.160.1
  ```
  ```
     pvc to_c 0/42
  ```
  ```
    map ip 202.38.160.3
  ```
  ```
  oam
  ```
  ```
     attribute 0/40 end-point
  ```
  ```
     attribute 0/42 end-point
  ```
  ```
     cc 0/40 end-to-end both
  ```
  ```
     cc 0/42 end-to-end both
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
  interface Atm0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
    ip address 202.38.160.3 255.255.255.0
  ```
  ```
   pvc to_a 0/41
  ```
  ```
    map ip 202.38.160.1
  ```
  ```
     pvc to_b 0/42
  ```
  ```
    map ip 202.38.160.2
  ```
  ```
  oam
  ```
  ```
     attribute 0/41 0/42 end-point
  ```
  ```
     cc 0/41 0/42 end-to-end both
  ```
  ```
  #
  ```
  ```
  return
  ```