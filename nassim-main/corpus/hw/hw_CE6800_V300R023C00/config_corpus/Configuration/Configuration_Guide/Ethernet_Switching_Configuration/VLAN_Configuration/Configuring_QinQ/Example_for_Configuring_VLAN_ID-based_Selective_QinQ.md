Example for Configuring VLAN ID-based Selective QinQ
====================================================

Example for Configuring VLAN ID-based Selective QinQ

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001262805456__fig10534133734710), service A and service B are user services in location X and location Y. Service A at both locations belongs to one VLAN range, and service B at both locations belongs to another VLAN range. To ensure security between services and conserve VLAN IDs on the core/backbone network, traffic between the two locations must be transparently transmitted through the core/backbone network. In addition, the same services at both locations must be able to communicate with each other, but different services must be isolated from each other.

**Figure 1** Network diagram of configuring VLAN ID-based selective QinQ![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE 1/0/1 and 100GE 1/0/2, respectively.


  
![](figure/en-us_image_0000001310445549.png)

#### Procedure

1. Create VLANs.
   
   
   
   # Create VLAN 2 and VLAN 3 (outer VLAN IDs to be added) on 100GE 1/0/1 of DeviceA. The configuration of DeviceB is similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] vlan batch 2 3
   [*DeviceA] commit
   ```
2. Create VLANs and add interfaces to the VLANs.
   
   
   
   # Configure selective QinQ on 100GE 1/0/1 of DeviceA. The configuration of DeviceB is similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] portswitch
   [~DeviceA-100GE1/0/1] port link-type hybrid
   [*DeviceA-100GE1/0/1] port hybrid untagged vlan 2 3
   [*DeviceA-100GE1/0/1] port vlan-stacking vlan 200 to 299 stack-vlan 2
   [*DeviceA-100GE1/0/1] port vlan-stacking vlan 300 to 399 stack-vlan 3
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
3. Add the outbound interfaces to the outer VLANs.
   
   
   
   # Configure 100GE 1/0/2 on DeviceA to allow packets from VLAN 2 and VLAN 3 to pass through. The configuration of DeviceB is similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
   
   ```
   [~DeviceA] interface 100ge 1/0/2
   [~DeviceA-100GE1/0/2] portswitch
   [~DeviceA-100GE1/0/2] port link-type trunk
   [*DeviceA-100GE1/0/2] port trunk allow-pass vlan 2 3
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

* From the server running service A in VLAN 200 to VLAN 299 in location X, ping the server running the same service in the same VLANs in location Y. If the ping succeeds, the servers running service A in the same VLANs in both locations can communicate with each other.
* From the server running service B in VLAN 300 to VLAN 399 in location X, ping the server running the same service in the same VLANs in location Y. If the ping succeeds, the servers running service B in the same VLANs in both locations can communicate with each other.
* From the server running service A in VLAN 200 to VLAN 299 in location X, ping the server running service B in VLAN 300 to VLAN 399 in location Y. If the ping fails, different services are isolated from each other.

#### Configuration Scripts

* DeviceA
  ```
  #
  sysname DeviceA
  #
  vlan batch 2 3
  #
  interface 100GE1/0/1
   port link-type hybrid
   port hybrid untagged vlan 2 3
   port vlan-stacking vlan 200 to 299 stack-vlan 2
   port vlan-stacking vlan 300 to 399 stack-vlan 3
  #
  interface 100GE1/0/2
   port link-type trunk
   port trunk allow-pass vlan 2 3
  #
  return
  ```
* DeviceB
  ```
  #
  sysname DeviceB
  #
  vlan batch 2 3
  #
  interface 100GE1/0/1
   port link-type hybrid
   port hybrid untagged vlan 2 3
   port vlan-stacking vlan 200 to 299 stack-vlan 2
   port vlan-stacking vlan 300 to 399 stack-vlan 3
  #
  interface 100GE1/0/2
   port link-type trunk
   port trunk allow-pass vlan 2 3
  #
  return
  ```