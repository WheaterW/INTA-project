Example for Configuring GVRP
============================

Example_for_Configuring_GVRP

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172362952__fig_dc_vrp_gvrp_cfg_001201), company A, a branch of company A, and company B are connected using switching devices. GVRP needs to be configured for dynamic VLAN registration. The branch of company A communicates with the headquarters (company A) through Device A and Device B. Company B communicates with company A through Device B and Device C, and only packets from the VLANs configured for company B are permitted.

**Figure 1** Configuring GVRP![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 and 2 represent GE0/1/1 and GE0/1/2, respectively.


  
![](figure/en-us_image_0000001920186958.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable GVRP to implement dynamic VLAN registration.
2. Configure GVRP on all company A switches. Set the GVRP registration mode to Normal for the interfaces of company A switches.
3. Configure GVRP on all company B switches. Set the GVRP registration mode to Fixed for the interfaces connecting to company A so that only packets in the VLANs to which company B belongs can pass.

#### Data Preparation

None


#### Procedure

1. Configure Device A.
   
   
   
   # Create VLANs 101 to 200.
   
   ```
   <<HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*Device] commit
   [~DeviceA] vlan batch 101 to 200
   [*Device] commit
   ```
   
   # Enable GVRP globally.
   
   ```
   [~DeviceA] gvrp
   ```
   
   # Configure interfaces as trunk interfaces and allow packets in all VLANs to pass.
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/1
   [~DeviceA-GigabitEthernet0/1/1] port link-type trunk
   [*DeviceA-GigabitEthernet0/1/1] port trunk allow-pass vlan all
   [*DeviceA-GigabitEthernet0/1/1] commit
   [~DeviceA-GigabitEthernet0/1/1] quit
   [~DeviceA] interface gigabitethernet 0/1/2
   [~DeviceA-GigabitEthernet0/1/2] port link-type trunk
   [*DeviceA-GigabitEthernet0/1/2] port trunk allow-pass vlan all
   [*DeviceA-GigabitEthernet0/1/2] commit
   [~DeviceA-GigabitEthernet0/1/2] quit
   ```
   
   # Enable GVRP on interfaces and set GVRP registration modes for the interfaces.
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/1
   [~DeviceA-GigabitEthernet0/1/1] gvrp
   [*DeviceA-GigabitEthernet0/1/1] gvrp registration normal
   [*DeviceA-GigabitEthernet0/1/1] commit
   [~DeviceA-GigabitEthernet0/1/1] quit
   [~DeviceA] interface gigabitethernet 0/1/2
   [~DeviceA-GigabitEthernet0/1/2] gvrp
   [*DeviceA-GigabitEthernet0/1/2] gvrp registration normal
   [*DeviceA-GigabitEthernet0/1/2] commit
   [~DeviceA-GigabitEthernet0/1/2] quit
   ```
2. Configure DeviceB.
   
   
   
   # Enable GVRP globally.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*Device] commit
   [~DeviceB] gvrp
   [*DeviceB] commit
   ```
   
   # Configure interfaces as trunk interfaces and allow packets in all VLANs to pass.
   
   ```
   [~DeviceB] interface gigabitethernet 0/1/1
   [~DeviceB-GigabitEthernet0/1/1] port link-type trunk
   [*DeviceB-GigabitEthernet0/1/1] port trunk allow-pass vlan all
   [*DeviceB-GigabitEthernet0/1/1] commit
   [~DeviceB-GigabitEthernet0/1/1] quit
   [~DeviceB] interface gigabitethernet 0/1/2
   [~DeviceB-GigabitEthernet0/1/2] port link-type trunk
   [*DeviceB-GigabitEthernet0/1/2] port trunk allow-pass vlan all
   [*DeviceB-GigabitEthernet0/1/2] commit
   [~DeviceB-GigabitEthernet0/1/2] quit
   ```
   
   # Enable GVRP on interfaces and set GVRP registration modes for the interfaces.
   
   ```
   [~DeviceB] interface gigabitethernet 0/1/1
   [~DeviceB-GigabitEthernet0/1/1] gvrp
   [*DeviceB-GigabitEthernet0/1/1] gvrp registration normal
   [*DeviceB-GigabitEthernet0/1/1] commit
   [~DeviceB-GigabitEthernet0/1/1] quit
   [~DeviceB] interface gigabitethernet 0/1/2
   [~DeviceB-GigabitEthernet0/1/2] gvrp
   [*DeviceB-GigabitEthernet0/1/2] gvrp registration normal
   [*DeviceB-GigabitEthernet0/1/2] commit
   [~DeviceB-GigabitEthernet0/1/2] quit
   ```
3. Configure DeviceC.
   
   
   
   # Create VLANs 101 to 200.
   
   ```
   <<HUAWEI> system-view
   [~HUAWEI] sysname DeviceC
   [*Device] commit
   [~DeviceC] vlan batch 101 to 200
   [*Device] commit
   ```
   
   # Enable GVRP globally.
   
   ```
   [~DeviceC] gvrp
   ```
   
   # Configure interfaces as trunk interfaces and allow packets in all VLANs to pass.
   
   ```
   [~DeviceC] interface gigabitethernet 0/1/1
   [~DeviceC-GigabitEthernet0/1/1] port link-type trunk
   [*DeviceC-GigabitEthernet0/1/1] port trunk allow-pass vlan all
   [*DeviceC-GigabitEthernet0/1/1] commit
   [*DeviceC-GigabitEthernet0/1/1] quit
   [~DeviceC] interface gigabitethernet 0/1/2
   [~DeviceC-GigabitEthernet0/1/2] port link-type trunk
   [*DeviceC-GigabitEthernet0/1/2] port trunk allow-pass vlan all
   [*DeviceC-GigabitEthernet0/1/2] commit
   [~DeviceC-GigabitEthernet0/1/2] quit
   ```
   
   # Enable GVRP on interfaces and set GVRP registration modes for the interfaces.
   
   ```
   [~DeviceC] interface gigabitethernet 0/1/1
   [~DeviceC-GigabitEthernet0/1/1] gvrp
   [*DeviceC-GigabitEthernet0/1/1] gvrp registration fixed
   [*DeviceC-GigabitEthernet0/1/1] commit
   [~DeviceC] quit
   [~DeviceC] interface gigabitethernet 0/1/2
   [~DeviceC-GigabitEthernet0/1/2] gvrp
   [*DeviceC-GigabitEthernet0/1/2] gvrp registration normal
   [*DeviceC-GigabitEthernet0/1/2] commit
   [~DeviceC-GigabitEthernet0/1/2] quit
   ```
4. Verify the configuration.
   
   
   
   After the configuration is complete, the branch of company A can communicate with the headquarters, and company A users in VLANs 101 to 200 can communicate with company B users in the same VLANs.
   
   Run the **display gvrp status** command on Device A to check the status of global GVRP. The command output shows that GVRP is enabled globally.
   
   ```
   [~DeviceA] display gvrp status
   GVRP status: enabled.
   
   ```
   
   Run the **display gvrp statistics** command on Device A to check GVRP information. The command output shows the GVRP status and registration mode of each interface, number of GVRP registration failures, and source MAC address of the last GVRP PDU.
   
   ```
   [~DeviceA] display gvrp statistics
   
     GVRP statistics on port GigabitEthernet0/1/1 
       GVRP status                         : Enabled                               
       GVRP registrations failed           : 0                                     
       GVRP last PDU origin                : 0000-0000-0000                        
       GVRP registration type              : Normal
   
     GVRP statistics on port GigabitEthernet0/1/2
       GVRP status                         : Enabled                               
       GVRP registrations failed           : 0                                     
       GVRP last PDU origin                : 0000-0000-0000                        
       GVRP registration type              : Normal
   ```
   
   The methods of verifying the configurations for Device B and Device C are similar to that for Device A. For details, see Configuration Files.

#### Configuration Files

* Device A configuration file
  
  ```
  #
  sysname DeviceA
  #
  vlan batch 101 to 200
  #
  gvrp
  #
  interface GigabitEthernet0/1/1
   port link-type trunk
   port trunk allow-pass vlan 2 to 4094
   gvrp
  #
  interface GigabitEthernet0/1/2
   port link-type trunk
   port trunk allow-pass vlan 2 to 4094
   gvrp
  #
  return
  ```

* Device B configuration file
  
  ```
  #
  sysname DeviceB
  #
  gvrp
  #
  interface GigabitEthernet0/1/1
   port link-type trunk
   port trunk allow-pass vlan 2 to 4094
   gvrp
  #
  interface GigabitEthernet0/1/2
   port link-type trunk
   port trunk allow-pass vlan 2 to 4094
   gvrp
  #
  return
  ```

* Device C configuration file
  
  ```
  #
  sysname DeviceC
  #
  vlan batch 101 to 200
  #
  gvrp
  #
  interface GigabitEthernet0/1/1
   port link-type trunk
   port trunk allow-pass vlan 2 to 4094
   gvrp
   gvrp registration fixed
  #
  interface GigabitEthernet0/1/2
   port link-type trunk
   port trunk allow-pass vlan 2 to 4094
   gvrp
  #
  return
  ```