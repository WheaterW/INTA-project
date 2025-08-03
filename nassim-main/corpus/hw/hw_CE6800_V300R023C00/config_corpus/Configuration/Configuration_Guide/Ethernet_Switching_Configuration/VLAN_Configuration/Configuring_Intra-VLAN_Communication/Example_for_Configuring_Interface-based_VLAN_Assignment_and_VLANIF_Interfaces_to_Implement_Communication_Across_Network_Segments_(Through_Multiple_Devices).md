Example for Configuring Interface-based VLAN Assignment and VLANIF Interfaces to Implement Communication Across Network Segments (Through Multiple Devices)
===========================================================================================================================================================

Example for Configuring Interface-based VLAN Assignment and VLANIF Interfaces to Implement Communication Across Network Segments (Through Multiple Devices)

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001130622832__fig17296449123314), Host1 and Host2 connected to DeviceA and Host3 and Host4 connected to DeviceB all belong to VLAN 2. The hosts connected to DeviceA belong to a different network segment from the hosts connected to DeviceB, and DeviceA and DeviceB can communicate at Layer 3. Host1 and Host2 connected to DeviceA need to communicate with Host3 and Host4 connected to DeviceB.

**Figure 1** Networking diagram of configuring interface-based VLAN assignment and VLANIF interfaces for communication through multiple devices![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001176662433.png "Click to enlarge")

#### Procedure

1. Create VLANs on DeviceA and DeviceB.
   
   
   
   # Configure DeviceA.
   
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] vlan batch 2
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] portswitch
   [*DeviceA-100GE1/0/1] port link-type access
   [*DeviceA-100GE1/0/1] port default vlan 2
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] portswitch
   [*DeviceA-100GE1/0/2] port link-type access
   [*DeviceA-100GE1/0/2] port default vlan 2
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
   # Configure DeviceB.
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] vlan batch 2
   [*DeviceB] interface 100ge 1/0/1
   [*DeviceB-100GE1/0/1] portswitch
   [*DeviceB-100GE1/0/1] port link-type access
   [*DeviceB-100GE1/0/1] port default vlan 2
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] interface 100ge 1/0/2
   [*DeviceB-100GE1/0/2] portswitch
   [*DeviceB-100GE1/0/2] port link-type access
   [*DeviceB-100GE1/0/2] port default vlan 2
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] commit
   ```
2. Configure the link between DeviceA and DeviceB as a trunk link.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] vlan batch 4
   [*DeviceA] interface 100ge 1/0/3
   [*DeviceA-100GE1/0/3] portswitch
   [*DeviceA-100GE1/0/3] port link-type trunk
   [*DeviceA-100GE1/0/3] port trunk allow-pass vlan 4
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] vlan batch 4
   [*DeviceB] interface 100ge 1/0/3
   [*DeviceB-100GE1/0/3] portswitch
   [*DeviceB-100GE1/0/3] port link-type trunk
   [*DeviceB-100GE1/0/3] port trunk allow-pass vlan 4
   [*DeviceB-100GE1/0/3] quit
   [*DeviceB] commit
   ```
3. Create VLANIF interfaces and configure their IP addresses.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface vlanif 2
   [*DeviceA-Vlanif2] ip address 10.10.10.1 24
   [*DeviceA-Vlanif2] quit
   [*DeviceA] interface vlanif 4
   [*DeviceA-Vlanif4] ip address 10.10.30.1 24
   [*DeviceA-Vlanif4] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] interface vlanif 2
   [*DeviceB-Vlanif2] ip address 10.10.20.1 24
   [*DeviceB-Vlanif2] quit
   [*DeviceB] interface vlanif 4
   [*DeviceB-Vlanif4] ip address 10.10.30.2 24
   [*DeviceB-Vlanif4] quit
   [*DeviceB] commit
   ```
4. Configure basic OSPF functions on DeviceA and DeviceB to ensure that there are reachable routes between them.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] router id 1.1.1.1
   [*DeviceA] ospf 1
   [*DeviceA-ospf-1] area 0
   [*DeviceA-ospf-1-area-0.0.0.0] network 10.10.10.0 0.0.0.255
   [*DeviceA-ospf-1-area-0.0.0.0] network 10.10.30.0 0.0.0.255
   [*DeviceA-ospf-1-area-0.0.0.0] quit
   [*DeviceA-ospf-1] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] router id 2.2.2.2
   [*DeviceB] ospf 1
   [*DeviceB-ospf-1] area 0
   [*DeviceB-ospf-1-area-0.0.0.0] network 10.10.20.0 0.0.0.255
   [*DeviceB-ospf-1-area-0.0.0.0] network 10.10.30.0 0.0.0.255
   [*DeviceB-ospf-1-area-0.0.0.0] quit
   [*DeviceB-ospf-1] quit
   [*DeviceB] commit
   ```

#### Verifying the Configuration

On the hosts connected to DeviceA, set the default gateway address to 10.10.10.1/24 (the IP address of VLANIF 2). On the hosts connected to DeviceB, set the default gateway address to 10.10.20.1/24 (the IP address of VLANIF 2). After the configuration is complete, Host1, Host2, Host3, and Host4 can ping one another.


#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #  
  router id 1.1.1.1
  #
  vlan batch 2 4
  # 
  interface Vlanif2
   ip address 10.10.10.1 255.255.255.0 
  # 
  interface Vlanif4  
   ip address 10.10.30.1 255.255.255.0 
  #
  interface 100GE1/0/1
   port default vlan 2
  #
  interface 100GE1/0/2
   port default vlan 2
  #
  interface 100GE1/0/3
   port link-type trunk
   port trunk allow-pass vlan 4
  #
  ospf 1
   area 0.0.0.0
    network 10.10.10.0 0.0.0.255
    network 10.10.30.0 0.0.0.255
  #
  return
  ```
* DeviceB
  ```
  #
  sysname DeviceB
  #  
  router id 2.2.2.2
  #
  vlan batch 2 4
  # 
  interface Vlanif2  
   ip address 10.10.20.1 255.255.255.0 
  # 
  interface Vlanif4  
   ip address 10.10.30.2 255.255.255.0 
  #
  interface 100GE1/0/1
   port default vlan 2
  #
  interface 100GE1/0/2
   port default vlan 2
  #
  interface 100GE1/0/3
   port link-type trunk
   port trunk allow-pass vlan 4
  #
  ospf 1
   area 0.0.0.0
    network 10.10.20.0 0.0.0.255
    network 10.10.30.0 0.0.0.255
  #
  return
  ```