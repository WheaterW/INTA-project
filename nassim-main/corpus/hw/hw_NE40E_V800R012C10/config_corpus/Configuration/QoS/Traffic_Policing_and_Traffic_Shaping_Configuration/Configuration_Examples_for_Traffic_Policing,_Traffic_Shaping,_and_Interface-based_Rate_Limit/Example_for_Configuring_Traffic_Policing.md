Example for Configuring Traffic Policing
========================================

This section provides an example for configuring traffic policing. It describes how to configure traffic policing to control the overall traffic volume that is received or forwarded, and to control the rate of specified packets.

#### Networking Requirements

GE 0/3/0 of DeviceA is connected to GE 0/1/0 of DeviceB. Server, PC1, and PC2 can access the Internet through DeviceA and DeviceB.

Server, PC1, and GE 0/1/0 of DeviceA are on the same network segment. PC2 and GE 0/2/0 of DeviceA are on the same network segment.

The traffic from Server and PC1 to GE 0/1/0 is controlled on DeviceA as follows:

* A bandwidth of up to 6 Mbit/s is assured for the traffic from Server. The default bandwidth is 5 Mbit/s. For traffic whose rate exceeds 5 Mbit/s but is less than or equal to 6 Mbit/s, packets are normally forwarded. When the traffic rate exceeds 6 Mbit/s, the nonconforming traffic is treated and forwarded as BE traffic flows.
* The rate limit on the traffic from PC1 is 2 Mbit/s. When the traffic rate exceeds the rate limit, the nonconforming traffic is dropped.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/1/0, GE 0/2/0, and GE 0/3/0, respectively.


**Figure 1** Networking diagram for configuring traffic policing  
![](images/fig_dc_ne_qos_cfg_002501.png)  


#### Configuration Precautions

During the configuration, pay attention to the following:

* If the CoS of a packet is re-marked as EF, BE, CS6, or CS7, the packet can be re-marked only in green.
* To display the statistics about a traffic policy, you can enable statistics for the traffic policy by running the **statistics enable** command.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IP addresses for interfaces.
2. On the inbound interface GE 0/1/0 of DeviceA, configure MF classification-based traffic policing for traffic from Server and PC1.

#### Data Preparation

To complete the configuration, you need the following data:

* ACL numbers, traffic classifier names, traffic behavior names, traffic policy names, and the interfaces where the traffic policies are applied, for the traffic of Server and PC1
* CIR, PIR, CBS, and PBS

#### Procedure

1. Configure IP addresses for interfaces (The detailed configuration is not mentioned here).
2. Configure DeviceA.
   
   
   
   # Configure ACL rules for matching data flows from Server and PC1.
   
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
   [~DeviceA] acl number 2001
   ```
   ```
   [*DeviceA-acl-basic-2001] rule permit source 1.1.1.1 0.0.0.0
   ```
   ```
   [*DeviceA-acl-basic-2001]commit
   ```
   ```
   [~DeviceA-acl-basic-2001] quit
   ```
   ```
   [~DeviceA] acl number 2002
   ```
   ```
   [*DeviceA-acl-basic-2002] rule permit source 1.1.1.2 0.0.0.0
   ```
   ```
   [*DeviceA-acl-basic-2002] commit
   ```
   ```
   [~DeviceA-acl-basic-2002] quit
   ```
   
   # Configure traffic classifiers and define ACL-based traffic classifier matching rules.
   
   ```
   [~DeviceA] traffic classifier class1
   ```
   ```
   [*DeviceA-classifier-class1] if-match acl 2001
   ```
   ```
   [*DeviceA-classifier-class1] commit
   ```
   ```
   [~DeviceA-classifier-class1] quit
   ```
   ```
   [~DeviceA] traffic classifier class2
   ```
   ```
   [*DeviceA-classifier-class2] if-match acl 2002
   ```
   ```
   [*DeviceA-classifier-class2] commit
   ```
   ```
   [~DeviceA-classifier-class2] quit
   ```
   
   # Define a traffic behavior. Set the bandwidth for the traffic from Server to 5 Mbit/s and the maximum bandwidth to 6 Mbit/s. For traffic whose rate exceeds 5 Mbit/s but is lower than or equal to 6 Mbit/s, the traffic is directly forwarded. When the traffic rate exceeds 6 Mbit/s, the nonconforming traffic is treated and forwarded as BE traffic flows.
   
   ```
   [~DeviceA] traffic behavior behavior1
   ```
   ```
   [*DeviceA-behavior-behavior1] car cir 5000 pir 6000 green pass yellow pass red pass service-class be color green
   ```
   ```
   [*DeviceA-behavior-behavior1] commit
   ```
   ```
   [~DeviceA-behavior-behavior1] quit
   ```
   
   # Define a traffic behavior. Set the rate limit on the traffic from PC1 to 2 Mbit/s. When the traffic rate exceeds 2 Mbit/s, the nonconforming traffic is dropped.
   
   ```
   [~DeviceA] traffic behavior behavior2
   ```
   ```
   [*DeviceA-behavior-behavior2] car cir 2000 green pass red discard
   ```
   ```
   [*DeviceA-behavior-behavior2] commit
   ```
   ```
   [~DeviceA-behavior-behavior2] quit
   ```
   
   # Define a traffic policy to associate traffic classifiers with traffic behaviors.
   
   ```
   [~DeviceA] traffic policy policy1
   ```
   ```
   [*DeviceA-trafficpolicy-policy1] classifier class1 behavior behavior1
   ```
   ```
   [*DeviceA-trafficpolicy-policy1] classifier class2 behavior behavior2
   ```
   ```
   [*DeviceA-trafficpolicy-policy1] commit
   ```
   ```
   [~DeviceA-trafficpolicy-policy1] quit
   ```
   
   # Apply the traffic policy to GE 0/1/0.
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] traffic-policy policy1 inbound
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
3. Verify the configuration.
   
   
   
   Run the **display interface** command on DeviceB to view interface-based traffic statistics.

#### Configuration Files

* DeviceA configuration file
  
  ```
  # 
  sysname DeviceA
  #
  acl number 2001
   rule 5 permit source 1.1.1.1 0
  acl number 2002
   rule 5 permit source 1.1.1.2 0
  #
  traffic classifier class1 operator or
   if-match acl 2001
  traffic classifier class2 operator or
   if-match acl 2002
  #
  traffic behavior behavior1
   car cir 5000 pir 6000 green pass yellow pass red pass service-class be color green
  traffic behavior behavior2
   car cir 2000 green pass red discard
  #
  traffic policy policy1
   classifier class1 behavior behavior1 precedence 1
   classifier class2 behavior behavior2 precedence 2
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 1.1.1.3 255.255.255.0
   traffic-policy policy1 inbound
  #
  return
  ```