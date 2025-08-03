Example for Configuring MF Classification on QinQ VLAN Tag Termination Sub-interfaces
=====================================================================================

This section provides an example for configuring MF classification on QinQ VLAN tag termination sub-interfaces.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172371303__fig_dc_ne_qos_cfg_205301), SwitchA and SwitchB connect to the carrier network through DeviceA and DeviceB. MF classification needs to be configured on DeviceA's GE0/2/0.1 (a QinQ VLAN tag termination sub-interface) to limit the rate of traffic sent by users attached to SwitchA to 10 Mbit/s and limit the CBS to 150000 bytes.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

For details on QinQ interfaces, see "QinQ Configuration" in *HUAWEI NE40E-M2 series Universal Service Router Configuration Guide - LAN Access and MAN Access*.

Interfaces 1 and 2 in this example represent GE0/1/0 and GE0/2/0.1, respectively.


**Figure 1** Configuring MF classification on QinQ VLAN tag termination sub-interfaces  
![](images/fig_dc_ne_qos_cfg_205301.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure GE0/2/0.1 on DeviceA and DeviceB as QinQ VLAN tag termination sub-interfaces.
2. Configure MF classification-based traffic policing on the QinQ VLAN tag termination sub-interfaces.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of interfaces
* Ranges of VLAN IDs in packet tags to be removed on QinQ VLAN tag termination sub-interfaces
* Rate of traffic sent from users attached to SwitchA: 10 Mbit/s; CBS: 150000 bytes
* Names of a traffic classifier, traffic behavior, and traffic policy, and number of the sub-interface to which the traffic policy is applied

#### Procedure

1. Configure an IGP on the backbone network. In this example, OSPF is used as an IGP. For details, see "OSPF Configuration" in *HUAWEI NE40E-M2 series Universal Service Router Configuration Guide - IP Routing*.
   
   
   
   # Configure DeviceA.
   
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
   [~DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] ip address 10.10.1.1 24
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [~DeviceA] ospf
   ```
   ```
   [*DeviceA-ospf-1] area 0
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.0] network 10.10.1.0 0.0.0.255
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.0] network 10.1.1.0 0.0.0.255
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~DeviceA-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [~DeviceA-ospf-1] quit
   ```
   
   # Configure DeviceB.
   
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
   [~DeviceB] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] ip address 10.10.1.2 24
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] quit
   ```
   ```
   [~DeviceB] ospf
   ```
   ```
   [*DeviceB-ospf-1] area 0
   ```
   ```
   [*DeviceB-ospf-1-area-0.0.0.0] network 10.10.1.0 0.0.0.255
   ```
   ```
   [*DeviceB-ospf-1-area-0.0.0.0] network 10.2.1.0 0.0.0.255
   ```
   ```
   [*DeviceB-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~DeviceB-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [~DeviceB-ospf-1] quit
   ```
2. Configure QinQ VLAN tag termination sub-interfaces.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface gigabitethernet 0/2/0.1
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0.1] control-vid 1 qinq-termination
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0.1] qinq termination pe-vid 100 ce-vid 10 to 20
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0.1] ip address 10.1.1.1 24
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0.1] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0.1] quit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] interface gigabitethernet 0/2/0.1
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0.1] control-vid 1 qinq-termination
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0.1] qinq termination pe-vid 100 ce-vid 10 to 20
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0.1] ip address 10.2.1.1 24
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0.1] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/2/0.1] quit
   ```
3. Configure MF classification on DeviceA's QinQ VLAN tag termination sub-interface.
   
   
   
   # Configure a traffic classifier and define a matching rule.
   
   ```
   [~DeviceA] traffic classifier c1
   ```
   ```
   [*DeviceA-classifier-c1] if-match any
   ```
   ```
   [*DeviceA-classifier-c1] commit
   ```
   ```
   [~DeviceA-classifier-c1] quit
   ```
   
   # Configure a traffic behavior.
   
   ```
   [~DeviceA] traffic behavior b1
   ```
   ```
   [*DeviceA-behavior-b1] car cir 10000 cbs 150000 pbs 0
   ```
   ```
   [*DeviceA-behavior-b1] commit
   ```
   ```
   [~DeviceA-behavior-b1] quit
   ```
   
   # Configure a traffic policy to associate the traffic classifier with the traffic behavior.
   
   ```
   [~DeviceA] traffic policy p1
   ```
   ```
   [*DeviceA-trafficpolicy-p1] classifier c1 behavior b1
   ```
   ```
   [*DeviceA-trafficpolicy-p1] commit
   ```
   ```
   [~DeviceA-trafficpolicy-p1] quit
   ```
   
   # After completing the preceding configuration, run the **display traffic policy** command to check information about the configured traffic policy, traffic classifier, and traffic behavior.
   
   ```
   [~DeviceA] display traffic policy user-defined
   ```
   ```
     User Defined Traffic Policy Information:
   ```
   ```
     Policy: p1
   ```
   ```
      Classifier: default-class
   ```
   ```
        Behavior: be
   ```
   ```
         -none-
   ```
   ```
      Classifier: c1
   ```
   ```
        Behavior: b1
   ```
   ```
         Committed Access Rate:
   ```
   ```
           CIR 10000 (Kbps), PIR 0 (Kbps), CBS 150000 (byte), PBS 0 (byte)
   ```
   ```
           Conform Action: pass
   ```
   ```
           Yellow  Action: pass
   ```
   ```
           Exceed  Action: discard
   ```
   
   # Apply the traffic policy to the sub-interface.
   
   ```
   [~DeviceA] interface gigabitethernet 0/2/0.1
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0.1] traffic-policy p1 inbound
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0.1] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0.1] quit
   ```
4. Verify the configuration.
   
   
   
   After the traffic policy is applied to DeviceA's GE0/2/0.1, the sub-interface accepts only 10 Mbit/s traffic and discards excess traffic.

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
  traffic classifier c1 operator or
  ```
  ```
   if-match any
  ```
  ```
  #
  ```
  ```
  traffic behavior b1
  ```
  ```
   car cir 10000 cbs 150000 green pass red discard
  ```
  ```
  #
  ```
  ```
  traffic policy p1
  ```
  ```
   classifier c1 behavior b1 precedence 1
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
   ip address 10.10.1.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0.1
  ```
  ```
   encapsulation qinq-termination
  ```
  ```
   qinq termination pe-vid 100 ce-vid 10 to 20
  ```
  ```
   ip address 10.1.1.1 255.255.255.0
  ```
  ```
   traffic-policy p1 inbound
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
    network 10.1.1.0 0.0.0.255
  ```
  ```
    network 10.10.1.0 0.0.0.255
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
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.10.1.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0.1
  ```
  ```
   encapsulation qinq-termination
  ```
  ```
   qinq termination pe-vid 100 ce-vid 10 to 20
  ```
  ```
   ip address 10.2.1.1 255.255.255.0
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
    network 10.2.1.0 0.0.0.255
  ```
  ```
    network 10.10.1.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  return
  ```