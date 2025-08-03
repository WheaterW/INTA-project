Example for Configuring URPF
============================

Flow-based URPF can be used to prevent source address spoofing attacks based on certain types of packets.

#### Networking Requirements

This example describes how to enable URPF on the ISP ingress. As shown in [Figure 1](#EN-US_TASK_0172372148__fig_dc_ne_urpf_cfg_001501), DeviceA is directly connected to the ISP's DeviceB. Enable URPF on DeviceB's GE 0/1/0. Perform URPF check on the packets whose source address matches ACL 2010. Enable URPF on DeviceA's GE 0/1/0, and enable default route matching.

**Figure 1** Networking diagram for configuring URPF![](../../../../public_sys-resources/note_3.0-en-us.png) 

* The configurations in this example are performed on DeviceA and DeviceB. The HUAWEI NE40E-M2 series can function as DeviceA and DeviceB.
* interface1 in this example represents GE 0/1/0.

  
![](images/fig_dc_ne_urpf_cfg_001501.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a traffic policy on the ISP Router to allow traffic from a specified network segment to pass the URPF check.
2. Configure an IP address for the interface on the client Router and enable URPF.

#### Data Preparation

To complete the configuration, you need the following data:

* IP address of each interface
* IP addresses in the network segment that passes the URPF check

#### Procedure

1. Configure DeviceB to perform URPF check on the packets whose source address matches ACL 2010.
   
   
   
   # Configure ACL 2010.
   
   ```
   <DeviceB> system-view
   ```
   ```
   [~DeviceB] acl number 2010
   ```
   ```
   [*DeviceB-acl-basic-2010] rule permit source 10.1.1.0 0.0.0.255
   ```
   ```
   [*DeviceB-acl-basic-2010] commit
   ```
   ```
   [~DeviceB-acl-basic-2010] quit
   ```
   
   # Configure a traffic classifier and define an ACL-based matching rule.
   
   ```
   [~DeviceB] traffic classifier classifier1
   ```
   ```
   [*DeviceB-classifier-classifier1] if-match acl 2010
   ```
   ```
   [*DeviceB-classifier-classifier1] commit
   ```
   ```
   [~DeviceB-classifier-classifier1] quit
   ```
   
   # Define a traffic behavior and configure URPF.
   
   ```
   [~DeviceB] traffic behavior behavior1
   ```
   ```
   [*DeviceB-behavior-behavior1] ip urpf strict
   ```
   ```
   [*DeviceB-behavior-behavior1] commit
   ```
   ```
   [~DeviceB-behavior-behavior1] quit
   ```
   
   # Define a traffic policy to associate the traffic classifier with the traffic behavior.
   
   ```
   [~DeviceB] traffic policy policy1
   ```
   ```
   [*DeviceB-trafficpolicy-policy1] classifier classifier1 behavior behavior1
   ```
   ```
   [*DeviceB-trafficpolicy-policy1] commit
   ```
   ```
   [~DeviceB-trafficpolicy-policy1] quit
   ```
   
   # Apply the traffic policy to the interface.
   
   ```
   [~DeviceB] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] ip address 172.19.139.2 255.255.255.252
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] traffic-policy policy1 inbound
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] commit
   ```
2. Configure DeviceA.
   
   
   
   # Configure GE 0/1/0.
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] ip address 172.19.139.1 255.255.255.252
   ```
   
   # Enable URPF on GE 0/1/0.
   
   ```
   [*DeviceA-GigabitEthernet0/1/0] ip urpf strict allow-default
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
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
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 172.19.139.1 255.255.255.252
  ```
  ```
   ip urpf strict allow-default
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
  acl number 2010
  ```
  ```
   rule 5 permit source 10.1.1.0 0.0.0.255
  ```
  ```
  # 
  ```
  ```
  traffic classifier classifier1 operator or
  ```
  ```
   if-match acl 2010
  ```
  ```
  #
  ```
  ```
  traffic behavior behavior1
  ```
  ```
   ip urpf strict
  ```
  ```
  #
  ```
  ```
  traffic policy policy1
  ```
  ```
   classifier classifier1 behavior behavior1
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
   ip address 172.19.139.2 255.255.255.252
  ```
  ```
   traffic-policy policy1 inbound
  ```
  ```
  #
  ```
  ```
  return
  ```