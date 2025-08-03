Example for Configuring VLAN-based CFM (Layer 2 Network)
========================================================

This section provides an example for configuring virtual local area network (VLAN)-based connectivity fault management (CFM) on a Layer 2 network.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172361968__fig_dc_vrp_cfm_cfg_00002201), ISP1 manages DeviceA, DeviceB, and DeviceD, and ISP2 manages DeviceC, DeviceE, DeviceF, DeviceG, DeviceH, and DeviceI. Configure VLAN-based CFM to detect link faults.

**Figure 1** VLAN-based CFM on a Layer 2 network![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent GE 0/1/0, GE 0/1/1, and GE 0/1/2, respectively.


  
![](images/fig_dc_vrp_cfm_cfg_00002201.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create VLANs and add interfaces to them.
2. Create MD1 at Level 6 on all devices.
3. Create MA1 in MD1 on all devices except DeviceG, and map MA1 to VLAN2.
4. Create MA2 in MD1 on all devices except DeviceE and DeviceI, and map MA2 to VLAN3.
5. Create MD2 at Level 4 on DeviceA, DeviceB, DeviceC, and DeviceD, create MA3 in MD2, and map MA3 to VLAN4.
6. Configure maintenance association end points (MEPs) and remote maintenance association end points (RMEPs) for MA1 in MD1 on DeviceE, DeviceH, and DeviceI.
7. Configure local MEPs and RMEPs for MA2 in MD1 on DeviceH and DeviceG.
8. Configure local MEPs and RMEPs for MA3 in MD2 on DeviceA, DeviceC, and DeviceD.
9. Enable local MEPs to send continuity check messages (CCMs) and receive CCMs from RMEPs.

#### Data Preparation

To complete the configuration, you need the following data:

* MD1's level: 6
* MD2's level: 4

#### Procedure

1. Create VLANs and add interfaces to them. For configuration details, see Configuration Files in this section.
2. Create MD1.
   
   
   
   # Create MD1 on DeviceA.
   
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
   [~DeviceA] cfm enable
   ```
   ```
   [*DeviceA] cfm md md1 level 6
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Create MD1 on DeviceB, DeviceC, DeviceD, DeviceE, DeviceF, DeviceG, DeviceH, and DeviceI.
   
   The procedures for creating MD1 on these devices are similar to that on DeviceA.
3. Create and configure MA1 in MD1 on all devices except DeviceG.
   
   
   
   # Create and configure MA1 in MD1 on DeviceA.
   
   ```
   [~DeviceA-md-md1] ma ma1
   ```
   ```
   [*DeviceA-md-md1-ma-ma1] map vlan 2
   ```
   ```
   [*DeviceA-md-md1-ma-ma1] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Create and configure MA1 in MD1 on DeviceB, DeviceC, DeviceD, DeviceE, DeviceF, DeviceH, and DeviceI.
   
   The procedures for creating and configuring MA1 in MD1 on these devices are similar to that on DeviceA.
4. Create and configure MA2 in MD1 on all devices except DeviceE and DeviceI.
   
   
   
   # Create and configure MA2 in MD1 on DeviceA.
   
   ```
   [~DeviceA-md-md1] ma ma2
   ```
   ```
   [*DeviceA-md-md1-ma-ma2] map vlan 3
   ```
   ```
   [*DeviceA-md-md1-ma-ma2] quit
   ```
   ```
   [*DeviceA-md-md1] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Create and configure MA2 in MD1 on DeviceB, DeviceC, DeviceD, DeviceF, DeviceG, and DeviceH.
   
   The procedures for creating and configuring MA2 in MD1 on these devices are similar to that on DeviceA.
5. Create MD2 on DeviceA, DeviceB, DeviceC, and DeviceD, and create and configure MA3 in MD2.
   
   
   
   # Create MD2 on DeviceA, and create and configure MA3 in MD2.
   
   ```
   [~DeviceA] cfm md md2 level 4
   ```
   ```
   [*DeviceA-md-md2] ma ma3
   ```
   ```
   [*DeviceA-md-md2-ma-ma3] map vlan 4
   ```
   ```
   [*DeviceA-md-md2-ma-ma3] quit
   ```
   ```
   [*DeviceA-md-md2] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Create MD2 on Device B, Device C, and Device D, and create and configure MA3 in MD2.
   
   The procedures for creating MD2 and creating and configuring MA3 in MD2 on these devices are similar to that on DeviceA.
6. Configure local MEPs and RMEPs for MA1 in MD1 on DeviceE, DeviceH, and DeviceI.
   
   
   
   # Configure a local MEP for MA1 in MD1 on DeviceE.
   
   ```
   [~DeviceE] cfm md md1
   ```
   ```
   [*DeviceE-md-md1] ma ma1
   ```
   ```
   [*DeviceE-md-md1-ma-ma1] mep mep-id 3 interface gigabitethernet 0/1/1 inward
   ```
   
   # Configure a local MEP for MA1 in MD1 on DeviceH.
   
   ```
   [*DeviceH] cfm md md1
   ```
   ```
   [*DeviceH-md-md1] ma ma1
   ```
   ```
   [*DeviceH-md-md1-ma-ma1] mep mep-id 2 interface gigabitethernet 0/1/2 inward
   ```
   ```
   [*DeviceH] commit
   ```
   
   # Configure a local MEP for MA1 in MD1 on DeviceI.
   
   ```
   [~DeviceI] cfm md md1
   ```
   ```
   [*DeviceI-md-md1] ma ma1
   ```
   ```
   [*DeviceI-md-md1-ma-ma1] mep mep-id 1 interface gigabitethernet 0/1/1 inward
   ```
   
   # Configure an RMEP for MA1 in MD1 on DeviceE.
   
   ```
   [*DeviceE-md-md1-ma-ma1] remote-mep mep-id 1
   ```
   ```
   [*DeviceE-md-md1-ma-ma1] remote-mep mep-id 2
   ```
   
   # Configure an RMEP for MA1 in MD1 on DeviceH.
   
   ```
   [*DeviceH-md-md1-ma-ma1] remote-mep mep-id 1
   ```
   ```
   [*DeviceH-md-md1-ma-ma1] remote-mep mep-id 3
   ```
   ```
   [*DeviceH] commit
   ```
   
   # Configure an RMEP for MA1 in MD1 on DeviceI.
   
   ```
   [*DeviceI-md-md1-ma-ma1] remote-mep mep-id 2
   ```
   ```
   [*DeviceI-md-md1-ma-ma1] remote-mep mep-id 3
   ```
   ```
   [*DeviceI] commit
   ```
7. Configure local MEPs and RMEPs for MA2 in MD1 on DeviceH and DeviceG.
   
   
   
   # Configure a local MEP for MA2 in MD1 on DeviceH.
   
   ```
   [~DeviceH] cfm md md1
   ```
   ```
   [*DeviceH-md-md1] ma ma2
   ```
   ```
   [*DeviceH-md-md1-ma-ma2] mep mep-id 1 interface gigabitethernet 0/1/1 inward
   ```
   ```
   [*DeviceH] commit
   ```
   
   # Configure a local MEP for MA2 in MD1 on DeviceG.
   
   ```
   [*DeviceG] cfm md md1
   ```
   ```
   [*DeviceG-md-md1] ma ma2
   ```
   ```
   [*DeviceG-md-md1-ma-ma2] mep mep-id 2 interface gigabitethernet 0/1/0 inward
   ```
   ```
   [*DeviceG] commit
   ```
   
   # Configure an RMEP for MA2 in MD1 on DeviceH.
   
   ```
   [*DeviceH-md-md1-ma-ma2] remote-mep mep-id 2
   ```
   ```
   [*DeviceH] commit
   ```
   
   # Configure an RMEP for MA2 in MD1 on DeviceG.
   
   ```
   [*DeviceG-md-md1-ma-ma2] remote-mep mep-id 1
   ```
   ```
   [*DeviceG] commit
   ```
8. Configure local MEPs and RMEPs for MA3 in MD2 on DeviceA, DeviceC, and DeviceD.
   
   
   
   # Configure a local MEP for MA3 in MD2 on DeviceA.
   
   ```
   [~DeviceA] cfm md md2
   ```
   ```
   [*DeviceA-md-md2] ma ma3
   ```
   ```
   [*DeviceA-md-md2-ma-ma3] mep mep-id 1 interface gigabitethernet 0/1/0 inward
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure a local MEP for MA3 in MD2 on DeviceC.
   
   ```
   [*DeviceC] cfm md md2
   ```
   ```
   [*DeviceC-md-md2] ma ma3
   ```
   ```
   [DeviceC-md-md2-ma-ma3] mep mep-id 2 interface gigabitethernet 0/1/1 outward
   ```
   ```
   [*DeviceC] commit
   ```
   
   # Configure a local MEP for MA3 in MD2 on DeviceD.
   
   ```
   [~DeviceD] cfm md md2
   ```
   ```
   [*DeviceD-md-md2] ma ma3
   ```
   ```
   [*DeviceD-md-md2-ma-ma3] mep mep-id 3 interface gigabitethernet 0/1/0 inward
   ```
   ```
   [*DeviceD] commit
   ```
   
   # Configure an RMEP for MA3 in MD2 on DeviceA.
   
   ```
   [~DeviceA-md-md2-ma-ma3] remote-mep mep-id 2
   ```
   ```
   [*DeviceA-md-md2-ma-ma3] remote-mep mep-id 3
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure an RMEP for MA3 in MD2 on DeviceC.
   
   ```
   [*DeviceC-md-md2-ma-ma3] remote-mep mep-id 1
   ```
   ```
   [*DeviceC-md-md2-ma-ma3] remote-mep mep-id 3
   ```
   ```
   [*DeviceC] commit
   ```
   
   # Configure an RMEP for MA3 in MD2 on DeviceD.
   
   ```
   [~DeviceD-md-md2-ma-ma3] remote-mep mep-id 1
   ```
   ```
   [*DeviceD-md-md2-ma-ma3] remote-mep mep-id 2
   ```
   ```
   [*DeviceD] commit
   ```
9. Enable local MEPs to send CCMs and receive CCMs from RMEPs.
   
   
   
   # Enable local MEPs to send CCMs on DeviceA.
   
   ```
   [*DeviceA-md-md2-ma-ma3] mep ccm-send mep-id 1 enable
   ```
   
   # Enable local MEPs to receive CCMs from RMEPs on DeviceA.
   
   ```
   [*DeviceA-md-md2-ma-ma3] remote-mep ccm-receive enable
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Enable local MEPs to send CCMs and receive CCMs from RMEPs on DeviceB, DeviceC, DeviceD, DeviceE, DeviceF, DeviceG, DeviceH, and DeviceI.
   
   The procedures for enabling local MEPs to send CCMs and receive CCMs from RMEPs on these devices are similar to that on DeviceA.
10. Verify the configuration.
    
    
    
    Run the [**display cfm remote-mep**](cmdqueryname=display+cfm+remote-mep) command to view RMEP information. The following example uses the command output on DeviceA. The command output shows that the RMEP is up.
    
    ```
    <DeviceA> display cfm remote-mep
    The total number of RMEPs is : 1
    The status of RMEPs : 1 up, 0 down, 0 disable
    --------------------------------------------------
     MD Name            : md
     Level              : 0
     MA Name            : ma1
     RMEP ID            : 2
     VLAN ID            : 2 
     VSI Name           : --
     L2VC ID            : --
     L2VPN Name         : --  CE ID              : --  CE Offset          : --
      L2TPV3 Tunnel Name            : --
     L2TPV3 Local Connection Name  : --
     MAC                : 00e0-fc12-7890
     CCM Receive        : enabled
     Trigger-If-Down    : enabled
     CFM Status         : up
     Alarm Status       : none
     Interface TLV      : --
     Port Status TLV    : --
    ```

#### Configuration Files

* DeviceA configuration file
  
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
  vlan batch 2 to 4
  ```
  ```
  #
  ```
  ```
  cfm enable
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   portswitch
  ```
  ```
   port trunk allow-pass vlan 2 to 4
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/1
  ```
  ```
   portswitch
  ```
  ```
   port trunk allow-pass vlan 2 to 4
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/2
  ```
  ```
   portswitch
  ```
  ```
   port trunk allow-pass vlan 2 to 4
  ```
  ```
  #
  ```
  ```
   cfm md md1 level 6
  ```
  ```
    ma ma1
  ```
  ```
     map vlan 2
  ```
  ```
    ma ma2
  ```
  ```
     map vlan 3
  ```
  ```
  #
  ```
  ```
   cfm md md2 level 4
  ```
  ```
    ma ma3
  ```
  ```
     map vlan 4
  ```
  ```
     mep mep-id 1 interface gigabitethernet 0/1/0 inward
  ```
  ```
     mep ccm-send mep-id 1 enable
  ```
  ```
     remote-mep mep-id 2
  ```
  ```
     remote-mep ccm-receive mep-id 2 enable
  ```
  ```
     remote-mep mep-id 3
  ```
  ```
     remote-mep ccm-receive mep-id 3 enable
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
  vlan batch 2 to 4
  ```
  ```
  #
  ```
  ```
  cfm enable
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   portswitch
  ```
  ```
   port trunk allow-pass vlan 2 to 4
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/1
  ```
  ```
   portswitch
  ```
  ```
   port trunk allow-pass vlan 2 to 4
  ```
  ```
  #
  ```
  ```
  cfm md md1 level 6
  ```
  ```
    ma ma1
  ```
  ```
     map vlan 2
  ```
  ```
    ma ma2
  ```
  ```
     map vlan 3
  ```
  ```
  #
  ```
  ```
   cfm md md2 level 4
  ```
  ```
    ma ma3
  ```
  ```
     map vlan 4
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
  vlan batch 2 to 4
  ```
  ```
  #
  ```
  ```
  cfm enable
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   portswitch
  ```
  ```
   port trunk allow-pass vlan 2 to 4
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/1
  ```
  ```
   portswitch
  ```
  ```
   port trunk allow-pass vlan 2 to 4
  ```
  ```
  #
  ```
  ```
  cfm md md1 level 6
  ```
  ```
    ma ma1
  ```
  ```
     map vlan 2
  ```
  ```
    ma ma2
  ```
  ```
     map vlan 3
  ```
  ```
  #
  ```
  ```
   cfm md md2 level 4
  ```
  ```
    ma ma3
  ```
  ```
     map vlan 4
  ```
  ```
     mep mep-id 2 interface gigabitethernet 0/1/1 outward
  ```
  ```
     mep ccm-send mep-id 2 enable
  ```
  ```
     remote-mep mep-id 1
  ```
  ```
     remote-mep ccm-receive mep-id 1 enable
  ```
  ```
     remote-mep mep-id 3
  ```
  ```
     remote-mep ccm-receive mep-id 3 enable
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
  vlan batch 2 to 4
  ```
  ```
  #
  ```
  ```
  cfm enable
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   portswitch
  ```
  ```
   port trunk allow-pass vlan 2 to 4
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/2
  ```
  ```
   portswitch
  ```
  ```
   port trunk allow-pass vlan 2 to 4
  ```
  ```
  #
  ```
  ```
   cfm md md1 level 6
  ```
  ```
    ma ma1
  ```
  ```
     map vlan 2
  ```
  ```
    ma ma2
  ```
  ```
     map vlan 3
  ```
  ```
  #
  ```
  ```
   cfm md md2 level 4
  ```
  ```
    ma ma3
  ```
  ```
     map vlan 4
  ```
  ```
     mep mep-id 3 interface gigabitethernet 0/1/0 inward
  ```
  ```
     mep ccm-send mep-id 3 enable
  ```
  ```
     remote-mep mep-id 1
  ```
  ```
     remote-mep ccm-receive mep-id 1 enable
  ```
  ```
     remote-mep mep-id 2
  ```
  ```
     remote-mep ccm-receive mep-id 2 enable
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
  vlan batch 2
  ```
  ```
  #
  ```
  ```
  cfm enable
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   portswitch
  ```
  ```
   port trunk allow-pass vlan 2
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/1
  ```
  ```
   portswitch
  ```
  ```
   port trunk allow-pass vlan 2
  ```
  ```
  #
  ```
  ```
   cfm md md1 level 6
  ```
  ```
    ma ma1
  ```
  ```
     map vlan 2
  ```
  ```
     mep mep-id 3 interface gigabitethernet 0/1/1 inward
  ```
  ```
     mep ccm-send mep-id 3 enable
  ```
  ```
     remote-mep mep-id 1
  ```
  ```
     remote-mep ccm-receive mep-id 1 enable
  ```
  ```
     remote-mep mep-id 2
  ```
  ```
     remote-mep ccm-receive mep-id 2 enable
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
  vlan batch 2 to 3
  ```
  ```
  #
  ```
  ```
  cfm enable
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   portswitch
  ```
  ```
   port trunk allow-pass vlan 2
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/1
  ```
  ```
   portswitch
  ```
  ```
   port trunk allow-pass vlan 2 to 3
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/2
  ```
  ```
   portswitch
  ```
  ```
   port trunk allow-pass vlan 3
  ```
  ```
  #
  ```
  ```
   cfm md md1 level 6
  ```
  ```
    ma ma1
  ```
  ```
     map vlan 2
  ```
  ```
    ma ma2
  ```
  ```
     map vlan 3
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceG configuration file
  
  ```
  #
  ```
  ```
   sysname DeviceG
  ```
  ```
  #
  ```
  ```
  vlan batch 3
  ```
  ```
  #
  ```
  ```
  cfm enable
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   portswitch
  ```
  ```
   port trunk allow-pass vlan 3
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/2
  ```
  ```
   portswitch
  ```
  ```
   port trunk allow-pass vlan 3
  ```
  ```
  #
  ```
  ```
   cfm md md1 level 6
  ```
  ```
    ma ma2
  ```
  ```
     map vlan 3
  ```
  ```
     mep mep-id 2 interface gigabitethernet 0/1/0 inward
  ```
  ```
     mep ccm-send mep-id 2 enable
  ```
  ```
     remote-mep mep-id 1
  ```
  ```
     remote-mep ccm-receive mep-id 1 enable
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceH configuration file
  
  ```
  #
  ```
  ```
   sysname DeviceH
  ```
  ```
  #
  ```
  ```
  vlan batch 2 to 3
  ```
  ```
  #
  ```
  ```
  cfm enable
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   portswitch
  ```
  ```
   port trunk allow-pass vlan 2 to 3
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/1
  ```
  ```
   portswitch
  ```
  ```
  port trunk allow-pass vlan 3
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/2
  ```
  ```
   portswitch
  ```
  ```
   port trunk allow-pass vlan 2
  ```
  ```
  #
  ```
  ```
   cfm md md1 level 6
  ```
  ```
    ma ma1
  ```
  ```
     map vlan 2
  ```
  ```
     mep mep-id 2 interface gigabitethernet 0/1/2 inward
  ```
  ```
     mep ccm-send mep-id 2 enable
  ```
  ```
     remote-mep mep-id 1
  ```
  ```
     remote-mep ccm-receive mep-id 1 enable
  ```
  ```
     remote-mep mep-id 3
  ```
  ```
     remote-mep ccm-receive mep-id 3 enable
  ```
  ```
    ma ma2
  ```
  ```
     map vlan 3
  ```
  ```
     mep mep-id 1 interface gigabitethernet 0/1/1 inward
  ```
  ```
     mep ccm-send mep-id 1 enable
  ```
  ```
     remote-mep mep-id 2
  ```
  ```
     remote-mep ccm-receive mep-id 2 enable
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceI configuration file
  
  ```
  #
  ```
  ```
   sysname DeviceI
  ```
  ```
  #
  ```
  ```
  vlan batch 2
  ```
  ```
  #
  ```
  ```
  cfm enable
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   portswitch
  ```
  ```
   port trunk allow-pass vlan 2
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/1
  ```
  ```
   portswitch
  ```
  ```
   port trunk allow-pass vlan 2
  ```
  ```
  #
  ```
  ```
   cfm md md1 level 6
  ```
  ```
    ma ma1
  ```
  ```
     map vlan 2
  ```
  ```
     mep mep-id 1 interface gigabitethernet 0/1/1 inward
  ```
  ```
     mep ccm-send mep-id 1 enable
  ```
  ```
     remote-mep mep-id 2
  ```
  ```
     remote-mep ccm-receive mep-id 2 enable
  ```
  ```
     remote-mep mep-id 3
  ```
  ```
     remote-mep ccm-receive mep-id 3 enable
  ```
  ```
  #
  ```
  ```
  return
  ```