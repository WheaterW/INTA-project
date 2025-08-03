Example for Configuring Local Flow Mirroring
============================================

Example_for_Configuring_Local_Flow_Mirroring

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172343814__fig538613283720), to monitor the packets sent from DeviceA to interface 3 on DeviceB, specify interface 5 on DeviceB as an observing port and configure flow mirroring on interface 3. To improve the working efficiency of HostD, configure a traffic policy on interface 3 of DeviceB. In this way, only the packets with the source address of 2.2.2.2 are copied to interface 5.

**Figure 1** Networking diagram for configuring flow mirroring![](../../../../public_sys-resources/note_3.0-en-us.png) 

* The configurations in this example are performed on DeviceA, DeviceB, and DeviceC, all of which can be HUAWEI NE40E-M2 series devices.
* Interfaces 1 through 5 in this example represent GE0/1/0, GE0/2/0, GE0/1/1, GE0/1/2, and GE0/1/3, respectively.

  
![](figure/en-us_image_0256403740.png)

| Device Name | Interface Number | Interface IP Address | Interface MAC Address |
| --- | --- | --- | --- |
| DeviceA | GE0/1/0 | 10.70.1.1/24 | - |
| DeviceA | GE0/2/0 | 10.1.1.0/24 | - |
| DeviceA | GE0/1/1 | 10.20.2.2/24 | - |
| DeviceB | GE0/1/1 | 10.70.1.2/24 | - |
| DeviceB | GE0/1/2 | 10.80.1.2/24 | - |
| DeviceB | GE0/1/3 | 10.90.1.1/24 | - |
| DeviceC | GE0/1/0 | 10.80.1.1/24 | - |




#### Configuration Notes

* Do not configure an interface as both an observing port and a mirrored port.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure GE0/1/3 on DeviceB as an observing port.
2. Configure a traffic policy on GE0/1/1 of DeviceB and apply the policy to the mirrored port.

#### Data Preparation

To complete the configuration, you need the following data:

* IP address of each interface
* Types and numbers of the observing port and mirrored port
* ACL number, traffic classifier name, traffic behavior name, and traffic policy name

#### Procedure

1. Configure IP addresses for interfaces and ensure that the corresponding routes are reachable. For configuration details, see [Configuration Files](#EN-US_TASK_0172343814__example843779711213933) in this section.
2. Configure GE0/1/3 as an observing port.
   
   
   ```
   <DeviceB> system-view
   ```
   ```
   [~DeviceB] interface gigabitethernet0/1/3
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/3] port-observing observe-index 3
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/3] commit
   ```
3. Specify an observing port for board-based mirroring.
   
   
   ```
   [~DeviceB] slot 1
   ```
   ```
   [~DeviceB-slot-1] mirror to observe-index 3
   ```
   ```
   [*DeviceB-slot-1] commit
   ```
   ```
   [~DeviceB-slot-1] quit
   ```
4. Configure a traffic policy on the mirrored port GE0/1/1.
   
   
   
   # Define an ACL rule.
   
   ```
   [~DeviceB] acl 2001
   ```
   ```
   [*DeviceB-acl-basic-2001] rule 5 permit source 10.20.2.2 0.0.0.0
   ```
   ```
   [*DeviceB-acl-basic-2001] commit
   ```
   ```
   [~DeviceB-acl-basic-2001] quit
   ```
   
   # Configure a traffic classifier and define an ACL-based matching rule.
   
   ```
   [~DeviceB] traffic classifier a
   ```
   ```
   [*DeviceB-classifier-a] if-match acl 2001
   ```
   ```
   [*DeviceB-classifier-a] commit
   ```
   ```
   [~DeviceB-classifier-a] quit
   ```
   
   # After the configuration is complete, run the **display traffic classifier user-defined** command to check the traffic classifier configuration.
   
   ```
   [~DeviceB] display traffic classifier user-defined
   ```
   ```
   User Defined Classifier Information:
   ```
   ```
      Classifier: a
   ```
   ```
       Operator: OR
   ```
   ```
       Rule(s) : if-match acl 2001 precedence 2
   ```
   
   # Define a traffic behavior and enable flow mirroring.
   
   ```
   [~DeviceB] traffic behavior e
   ```
   ```
   [*DeviceB-behavior-e] port-mirroring enable
   ```
   ```
   [*DeviceB-behavior-e] commit
   ```
   ```
   [~DeviceB-behavior-e] quit
   ```
   
   # Define a traffic policy to associate the traffic classifier with the traffic behavior.
   
   ```
   [~DeviceB] traffic policy 1
   ```
   ```
   [*DeviceB-trafficpolicy-1] classifier a behavior e
   ```
   ```
   [*DeviceB-trafficpolicy-1] commit
   ```
   ```
   [~DeviceB-trafficpolicy-1] quit
   ```
   
   # Apply the traffic policy to the corresponding interface.
   
   ```
   [~DeviceB] interface gigabitethernet0/1/1
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/1] traffic-policy 1 inbound
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/1] quit
   ```
5. Verify the configuration.
   
   
   
   Check mirroring information through the **ping** command or another traffic generation method. For example, if DeviceA sends 10 ping packets with the source address of 10.20.2.2/32 and another 10 ping packets with the source address of 10.1.1.0/32 to GE0/1/1, HostD is expected to receive the packets with the source address of 10.20.2.2/32 from DeviceA, not the packets with the source address of 10.1.1.0/32.

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
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.70.1.1 255.255.255.0
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
   ip address 10.1.1.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.20.2.2 255.255.255.0
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
  acl number 2001
  ```
  ```
  rule 5 permit source 10.20.2.2 0.0.0.0
  ```
  ```
  #
  ```
  ```
  traffic classifier a
  ```
  ```
   if-match acl 2001
  ```
  ```
  #
  ```
  ```
  traffic behavior e
  ```
  ```
   port-mirroring enable
  ```
  ```
  #
  ```
  ```
  traffic policy 1
  ```
  ```
   classifier a behavior e
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.70.1.2 255.255.255.0
  ```
  ```
   traffic-policy 1 inbound
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/2
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.80.1.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/3
  ```
  ```
   undo shutdown
  ```
  ```
   port-observing observe-index 3
  ```
  ```
  #
  ```
  ```
  slot 1
  ```
  ```
   mirror to observe-index 3
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
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.80.1.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  return
  ```