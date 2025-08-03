Example for Configuring an ERPS Multi-ring Network
==================================================

This section provides an example for configuring an ERPS multi-ring network.

#### Networking Requirements

Generally, redundant links are used on an Ethernet switching network to provide link backup and enhance network reliability. The use of redundant links, however, may produce loops, causing broadcast storms and rendering the MAC address table unstable. As a result, the communication quality deteriorates, and communication services may even be interrupted.

To prevent loops caused by redundant links, enable ERPS on the devices of the ring network.

On the ERPS multi-ring network shown in [Figure 1](#EN-US_TASK_0172363484__fig_dc_vrp_erps_cfg_002001), Device A, Device B, and Device D constitute a major ring, and Device A, Device C, and Device D constitute a sub-ring.

**Figure 1** ERPS multi-ring networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example are GE 0/1/1, GE 0/1/2, GE 0/1/3, respectively.


  
![](images/fig_dc_vrp_erps_cfg_002001.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure the trunk link type for all ports to be added to ERPS rings.
2. Create ERPS rings and configure control VLANs and ERP instances for them.
3. Specify the ERPS version and configure a sub-ring.
4. Add Layer 2 ports to the ERPS rings and specify port roles.
5. Configure the topology change notification function on the interconnection nodes.
6. Configure the guard timer and WTR timer for the ERPS rings.
7. Configure the Layer 2 forwarding function on Device A through Device D.

#### Data Preparation

To complete the configuration, you need the following data:

* ERPS ring ID, control VLAN ID, and ERP instance ID
* Guard timer and WTR timer values
* VLAN ID for Layer 2 forwarding

#### Procedure

1. Configure the trunk link type for all ports to be added to ERPS rings.
   
   
   
   # Configure Device A.
   
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
   [~DeviceA] interface gigabitethernet 0/1/1
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] port link-type trunk
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/1/2
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] portswitch
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] undo shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] port link-type trunk
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/1/3
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/3] portswitch
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/3] undo shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/3] port link-type trunk
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/3] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure Device B.
   
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
   [~DeviceB] interface gigabitethernet 0/1/1
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] port link-type trunk
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] quit
   ```
   ```
   [*DeviceB] interface gigabitethernet 0/1/2
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/2] portswitch
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/2] undo shutdown
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/2] port link-type trunk
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/2] quit
   ```
   ```
   [*DeviceB] commit
   ```
   
   # Configure Device C.
   
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
   [~DeviceC] interface gigabitethernet 0/1/1
   ```
   ```
   [~DeviceC-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/1] port link-type trunk
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/1] quit
   ```
   ```
   [*DeviceC] interface gigabitethernet 0/1/2
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/2] portswitch
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/2] undo shutdown
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/2] port link-type trunk
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/2] quit
   ```
   ```
   [*DeviceC] commit
   ```
   
   # Configure Device D.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceD
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceD] interface gigabitethernet 0/1/1
   ```
   ```
   [~DeviceD-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/1] port link-type trunk
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/1] quit
   ```
   ```
   [*DeviceD] interface gigabitethernet 0/1/2
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/2] portswitch
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/2] undo shutdown
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/2] port link-type trunk
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/2] quit
   ```
   ```
   [*DeviceD] interface gigabitethernet 0/1/3
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/3] portswitch
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/3] undo shutdown
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/3] port link-type trunk
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/3] quit
   ```
   ```
   [*DeviceD] commit
   ```
2. Create ERPS ring1 and ERPS ring2 and configure ERP instances for the two rings. Set the control VLAN ID of ERPS ring1 to 10 and the control VLAN ID of ERPS ring2 to 20. Enable ERPS ring1 to transmit data packets carrying VLAN IDs from 100 to 200 and enable ERPS ring2 to transmit data packets carrying VLAN IDs from 300 to 400. 
   
   
   
   # Configure Device A.
   
   ```
   [~DeviceA] erps ring 1
   ```
   ```
   [*DeviceA-erps-ring1] control-vlan 10
   ```
   ```
   [*DeviceA-erps-ring1] protected-instance 1
   ```
   ```
   [*DeviceA-erps-ring1] quit
   ```
   ```
   [*DeviceA] stp region-configuration
   ```
   ```
   [*DeviceA-mst-region] instance 1 vlan 10 100 to 200
   ```
   ```
   [*DeviceA-mst-region] commit
   ```
   ```
   [~DeviceA-mst-region] quit
   ```
   ```
   [~DeviceA] erps ring 2
   ```
   ```
   [*DeviceA-erps-ring2] control-vlan 20
   ```
   ```
   [*DeviceA-erps-ring2] protected-instance 2
   ```
   ```
   [*DeviceA-erps-ring2] quit
   ```
   ```
   [*DeviceA] stp region-configuration
   ```
   ```
   [*DeviceA-mst-region] instance 2 vlan 20 300 to 400
   ```
   ```
   [*DeviceA-mst-region] commit
   ```
   ```
   [~DeviceA-mst-region] quit
   ```
   
   # Configure Device B.
   
   ```
   [~DeviceB] erps ring 1
   ```
   ```
   [*DeviceB-erps-ring1] control-vlan 10
   ```
   ```
   [*DeviceB-erps-ring1] protected-instance 1
   ```
   ```
   [*DeviceB-erps-ring1] quit
   ```
   ```
   [*DeviceB] stp region-configuration
   ```
   ```
   [*DeviceB-mst-region] instance 1 vlan 10 100 to 200
   ```
   ```
   [*DeviceB-mst-region] commit
   ```
   ```
   [~DeviceB-mst-region] quit
   ```
   
   # Configure Device C.
   
   ```
   [~DeviceC] erps ring 2
   ```
   ```
   [*DeviceC-erps-ring2] control-vlan 20
   ```
   ```
   [*DeviceC-erps-ring2] protected-instance 2
   ```
   ```
   [*DeviceC-erps-ring2] quit
   ```
   ```
   [*DeviceC] stp region-configuration
   ```
   ```
   [*DeviceC-mst-region] instance 2 vlan 20 300 to 400
   ```
   ```
   [*DeviceC-mst-region] commit
   ```
   ```
   [~DeviceC-mst-region] quit
   ```
   
   # Configure Device D.
   
   ```
   [~DeviceD] erps ring 1
   ```
   ```
   [*DeviceD-erps-ring1] control-vlan 10
   ```
   ```
   [*DeviceD-erps-ring1] protected-instance 1
   ```
   ```
   [*DeviceD-erps-ring1] quit
   ```
   ```
   [*DeviceD] stp region-configuration
   ```
   ```
   [*DeviceD-mst-region] instance 1 vlan 10 100 to 200
   ```
   ```
   [*DeviceD-mst-region] commit
   ```
   ```
   [~DeviceD-mst-region] quit
   ```
   ```
   [~DeviceD] erps ring 2
   ```
   ```
   [*DeviceD-erps-ring2] control-vlan 20
   ```
   ```
   [*DeviceD-erps-ring2] protected-instance 2
   ```
   ```
   [*DeviceD-erps-ring2] quit
   ```
   ```
   [*DeviceD] stp region-configuration
   ```
   ```
   [*DeviceD-mst-region] instance 2 vlan 20 300 to 400
   ```
   ```
   [*DeviceD-mst-region] commit
   ```
   ```
   [~DeviceD-mst-region] quit
   ```
3. Specify ERPSv2 and configure ERPS ring 2 as a sub-ring.
   
   
   
   # Configure Device A.
   
   ```
   [~DeviceA] erps ring 1
   ```
   ```
   [~DeviceA-erps-ring1] version v2
   ```
   ```
   [*DeviceA-erps-ring1] quit
   ```
   ```
   [*DeviceA] erps ring 2
   ```
   ```
   [*DeviceA-erps-ring2] version v2
   ```
   ```
   [*DeviceA-erps-ring2] sub-ring
   ```
   ```
   [*DeviceA-erps-ring2] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure Device B.
   
   ```
   [~DeviceB] erps ring 1
   ```
   ```
   [~DeviceB-erps-ring1] version v2
   ```
   ```
   [*DeviceB-erps-ring1] quit
   ```
   ```
   [*DeviceB] commit
   ```
   
   # Configure Device C.
   
   ```
   [~DeviceC] erps ring 2
   ```
   ```
   [~DeviceC-erps-ring2] version v2
   ```
   ```
   [*DeviceC-erps-ring2] sub-ring
   ```
   ```
   [*DeviceC-erps-ring2] quit
   ```
   ```
   [*DeviceC] commit
   ```
   
   # Configure Device D.
   
   ```
   [~DeviceD] erps ring 1
   ```
   ```
   [~DeviceD-erps-ring1] version v2
   ```
   ```
   [*DeviceD-erps-ring1] quit
   ```
   ```
   [*DeviceD] erps ring 2
   ```
   ```
   [*DeviceD-erps-ring2] version v2
   ```
   ```
   [*DeviceD-erps-ring2] sub-ring
   ```
   ```
   [*DeviceD-erps-ring2] quit
   ```
   ```
   [*DeviceD] commit
   ```
4. Add Layer 2 ports to the ERPS rings and specify port roles. Specifically, configure GE 0/1/1 on Device B and GE 0/1/1 on Device C as their respective RPL owner ports.
   
   
   
   # Configure Device A.
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/1
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] stp disable
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] erps ring 1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/1/2
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] stp disable
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] erps ring 1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] undo shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/1/3
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/3] shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/3] stp disable
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] erps ring 2
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] undo shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure Device B.
   
   ```
   [~DeviceB] interface gigabitethernet 0/1/1
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/1] shutdown
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] stp disable
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] erps ring 1 rpl owner
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] quit
   ```
   ```
   [*DeviceB] interface gigabitethernet 0/1/2
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/2] shutdown
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/2] stp disable
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/2] erps ring 1
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/2] undo shutdown
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/2] quit
   ```
   ```
   [*DeviceB] commit
   ```
   
   # Configure Device C.
   
   ```
   [~DeviceC] interface gigabitethernet 0/1/1
   ```
   ```
   [~DeviceC-GigabitEthernet0/1/1] shutdown
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/1] stp disable
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/1] erps ring 2 rpl owner
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/1] quit
   ```
   ```
   [*DeviceC] interface gigabitethernet 0/1/2
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/2] shutdown
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/2] stp disable
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/2] erps ring 2
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/2] undo shutdown
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/2] quit
   ```
   ```
   [*DeviceC] commit
   ```
   
   # Configure Device D.
   
   ```
   [~DeviceD] interface gigabitethernet 0/1/1
   ```
   ```
   [~DeviceD-GigabitEthernet0/1/1] shutdown
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/1] stp disable
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/1] erps ring 1
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/1] quit
   ```
   ```
   [*DeviceD] interface gigabitethernet 0/1/2
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/2] shutdown
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/2] stp disable
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/2] erps ring 1
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/2] undo shutdown
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/2] quit
   ```
   ```
   [*DeviceD] interface gigabitethernet 0/1/3
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/3] shutdown
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/3] stp disable
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/3] erps ring 2
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/3] undo shutdown
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/3] quit
   ```
   ```
   [*DeviceD] commit
   ```
5. Configure the topology change notification function on Device A and Device D, the interconnection nodes.
   
   
   
   # Configure Device A.
   
   ```
   [~DeviceA] erps ring 1
   ```
   ```
   [~DeviceA-erps-ring1] tc-notify erps ring 2
   ```
   ```
   [*DeviceA-erps-ring1] tc-protection interval 200
   ```
   ```
   [*DeviceA-erps-ring1] tc-protection threshold 60
   ```
   ```
   [*DeviceA-erps-ring1] quit
   ```
   ```
   [*DeviceA] erps ring 2
   ```
   ```
   [*DeviceA-erps-ring2] tc-notify erps ring 1
   ```
   ```
   [*DeviceA-erps-ring2] tc-protection interval 200
   ```
   ```
   [*DeviceA-erps-ring2] tc-protection threshold 60
   ```
   ```
   [*DeviceA-erps-ring2] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure Device D.
   
   ```
   [~DeviceD] erps ring 1
   ```
   ```
   [~DeviceD-erps-ring1] tc-notify erps ring 2
   ```
   ```
   [*DeviceD-erps-ring1] tc-protection interval 200
   ```
   ```
   [*DeviceD-erps-ring1] tc-protection threshold 60
   ```
   ```
   [*DeviceD-erps-ring1] quit
   ```
   ```
   [*DeviceD] erps ring 2
   ```
   ```
   [*DeviceD-erps-ring2] tc-notify erps ring 1
   ```
   ```
   [*DeviceD-erps-ring2] tc-protection interval 200
   ```
   ```
   [*DeviceD-erps-ring2] tc-protection threshold 60
   ```
   ```
   [*DeviceD-erps-ring2] quit
   ```
   ```
   [*DeviceD] commit
   ```
6. Configure the guard timer and WTR timer for the ERPS rings.
   
   
   
   # Configure Device A.
   
   ```
   [~DeviceA] erps ring 1
   ```
   ```
   [~DeviceA-erps-ring1] wtr-timer 6
   ```
   ```
   [*DeviceA-erps-ring1] guard-timer 100
   ```
   ```
   [*DeviceA-erps-ring1] quit
   ```
   ```
   [*DeviceA] erps ring 2
   ```
   ```
   [*DeviceA-erps-ring2] wtr-timer 6
   ```
   ```
   [*DeviceA-erps-ring2] guard-timer 100
   ```
   ```
   [*DeviceA-erps-ring2] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure Device B.
   
   ```
   [~DeviceB] erps ring 1
   ```
   ```
   [~DeviceB-erps-ring1] wtr-timer 6
   ```
   ```
   [*DeviceB-erps-ring1] guard-timer 100
   ```
   ```
   [*DeviceB-erps-ring1] quit
   ```
   ```
   [*DeviceB] commit
   ```
   
   # Configure Device C.
   
   ```
   [~DeviceC] erps ring 2
   ```
   ```
   [~DeviceC-erps-ring2] wtr-timer 6
   ```
   ```
   [*DeviceC-erps-ring2] guard-timer 100
   ```
   ```
   [*DeviceC-erps-ring2] quit
   ```
   ```
   [*DeviceC] commit
   ```
   
   # Configure Device D.
   
   ```
   [~DeviceD] erps ring 1
   ```
   ```
   [~DeviceD-erps-ring1] wtr-timer 6
   ```
   ```
   [*DeviceD-erps-ring1] guard-timer 100
   ```
   ```
   [*DeviceD-erps-ring1] quit
   ```
   ```
   [*DeviceD] erps ring 2
   ```
   ```
   [*DeviceD-erps-ring2] wtr-timer 6
   ```
   ```
   [*DeviceD-erps-ring2] guard-timer 100
   ```
   ```
   [*DeviceD-erps-ring2] quit
   ```
   ```
   [*DeviceD] commit
   ```
7. Configure the Layer 2 forwarding function on Device A through Device D.
   
   
   
   # Configure Device A.
   
   ```
   [~DeviceA] vlan batch 100 to 200 300 to 400
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] port trunk allow-pass vlan 100 to 200
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/1/2
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] port trunk allow-pass vlan 100 to 200 300 to 400
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/1/3
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/3] port trunk allow-pass vlan 300 to 400
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/3] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure Device B.
   
   ```
   [~DeviceB] vlan batch 100 to 200
   ```
   ```
   [*DeviceB] interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] port trunk allow-pass vlan 100 to 200
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] quit
   ```
   ```
   [*DeviceB] interface gigabitethernet 0/1/2
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/2] port trunk allow-pass vlan 100 to 200
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/2] quit
   ```
   ```
   [*DeviceB] commit
   ```
   
   # Configure Device C.
   
   ```
   [~DeviceC] vlan batch 300 to 400
   ```
   ```
   [*DeviceC] interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/1] port trunk allow-pass vlan 300 to 400
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/1] quit
   ```
   ```
   [*DeviceC] interface gigabitethernet 0/1/2
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/2] port trunk allow-pass vlan 300 to 400
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/2] quit
   ```
   ```
   [*DeviceC] commit
   ```
   
   # Configure Device D.
   
   ```
   [~DeviceD] vlan batch 100 to 200 300 to 400
   ```
   ```
   [*DeviceD] interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/1] port trunk allow-pass vlan 100 to 200
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/1] quit
   ```
   ```
   [*DeviceD] interface gigabitethernet 0/1/2
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/2] port trunk allow-pass vlan 100 to 200 300 to 400
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/2] quit
   ```
   ```
   [*DeviceD] interface gigabitethernet 0/1/3
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/3] port trunk allow-pass vlan 300 to 400
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/3] quit
   ```
   ```
   [*DeviceD] commit
   ```
8. Verify the configuration.
   
   
   
   After completing the configurations, run either of the following commands to verify the configuration. The following example uses the command output on Device B.
   
   * Run the [**display erps**](cmdqueryname=display+erps) command on Device B. The command output shows summary configurations of Device B ports added to the ERPS ring and ring configurations.
     
     ```
     [~DeviceB] display erps
     ```
     ```
     D  : Discarding
     F  : Forwarding
     R  : RPL Owner
     N  : RPL Neighbour
     FS : Forced Switch
     MS : Manual Switch
     Total number of rings configured = 1
     Ring  Control  WTR Timer  Guard Timer  Port 1               Port 2
     ID    VLAN     (min)      (csec)
     --------------------------------------------------------------------------------
        1       10          6          100  (D,R)GE0/1/1       (F)GE0/1/2          
     --------------------------------------------------------------------------------
     ```
   * Run the [**display erps verbose**](cmdqueryname=display+erps+verbose) command on Device B. The command output shows detailed configurations of Device B ports added to the ERPS ring and ring configurations.
     
     ```
     [~DeviceB] display erps verbose
     ```
     ```
     Ring ID                             : 1
     Description                         : Ring 1
     Control Vlan                        : 10
     Protected Instance                  : 1 
     Service Vlan                        : 100 to 200
     WTR Timer Setting (min)             : 6      Running (s)           : 0  
     Guard Timer Setting (csec)          : 100    Running (csec)        : 0  
     Holdoff Timer Setting (deciseconds) : 0      Running (deciseconds) : 0  
     WTB Timer Running (sec)             : 0  
     Ring State                          : Idle
     RAPS_MEL                            : 7
     Revertive Mode                      : Revertive
     R-APS Channel Mode                  : -
     Version                             : 2
     Sub-ring                            : No 
     Forced Switch Port                  : -
     Manual Switch Port                  : -
     TC-Notify                           : -
     Time since last topology change     : 0 days 4h:12m:20s
      
     --------------------------------------------------------------------------------
     Port                Port Role     Port Status     Signal Status
     --------------------------------------------------------------------------------
     GE0/1/1             RPL Owner     Discarding      Non-failed      
     GE0/1/2             Common        Forwarding      Non-failed
     
     ```

#### Configuration Files

* Device A configuration file
  
  ```
  #
   sysname DeviceA
  #
   vlan batch 100 to 200 300 to 400
  #
  stp region-configuration
   instance 1 vlan 10 100 to 200
   instance 2 vlan 20 300 to 400
  #
  erps ring 1
   control-vlan 10
   protected-instance 1
   version v2
   wtr-timer 6
   guard-timer 100
   tc-notify erps ring 2
   tc-protection interval 200
   tc-protection threshold 60
  #
  erps ring 2
   control-vlan 20
   protected-instance 2
   wtr-timer 6
   guard-timer 100
   version v2
   sub-ring
   tc-notify erps ring 1
   tc-protection interval 200
   tc-protection threshold 60
  #
  interface GigabitEthernet0/1/1
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 10 100 to 200
   stp disable
   erps ring 1
  #
  interface GigabitEthernet0/1/2
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 10 100 to 200 300 to 400
   stp disable
   erps ring 1
  #
  interface GigabitEthernet0/1/3
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 20 300 to 400
   stp disable
   erps ring 2
  #
  return
  ```
* Device B configuration file
  
  ```
  #
   sysname DeviceB
  #
   vlan batch 100 to 200
  #
  stp region-configuration
   instance 1 vlan 10 100 to 200
  #
  erps ring 1
   control-vlan 10
   protected-instance 1
   version v2
   wtr-timer 6
   guard-timer 100
  #
  interface GigabitEthernet0/1/1
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 10 100 to 200
   stp disable
   erps ring 1 rpl owner
  #
  interface GigabitEthernet0/1/2
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 10 100 to 200
   stp disable
   erps ring 1
  #
  return
  ```
* Device C configuration file
  
  ```
  #
   sysname DeviceC
  #
   vlan batch 300 to 400
  #
  stp region-configuration
   instance 2 vlan 20 300 to 400
  #
  erps ring 2
   control-vlan 20
   protected-instance 2
   wtr-timer 6
   guard-timer 100
   version v2
   sub-ring
  #
  interface GigabitEthernet0/1/1
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 20 300 to 400
   stp disable
   erps ring 2 rpl owner
  #
  interface GigabitEthernet0/1/2
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 20 300 to 400
   stp disable
   erps ring 2
  #
  return
  ```
* Device D configuration file
  
  ```
  #
   sysname DeviceD
  #
   vlan batch 100 to 200 300 to 400
  #
  stp region-configuration
   instance 1 vlan 10 100 to 200
   instance 2 vlan 20 300 to 400
  #
  erps ring 1
   control-vlan 10
   protected-instance 1
   version v2
   wtr-timer 6
   guard-timer 100
   tc-notify erps ring 2
   tc-protection interval 200
   tc-protection threshold 60
  #
  erps ring 2
   control-vlan 20
   protected-instance 2
   wtr-timer 6
   guard-timer 100
   version v2
   sub-ring
   tc-notify erps ring 1
   tc-protection interval 200
   tc-protection threshold 60
  #
  interface GigabitEthernet0/1/1
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 10 100 to 200
   stp disable
   erps ring 1
  #
  interface GigabitEthernet0/1/2
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 10 100 to 200 300 to 400
   stp disable
   erps ring 1
  #
  interface GigabitEthernet0/1/3
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 20 300 to 400
   stp disable
   erps ring 2
  #
  return
  ```