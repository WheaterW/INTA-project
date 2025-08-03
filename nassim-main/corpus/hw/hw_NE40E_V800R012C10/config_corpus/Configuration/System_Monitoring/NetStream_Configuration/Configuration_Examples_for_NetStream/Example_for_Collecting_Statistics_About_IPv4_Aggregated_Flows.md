Example for Collecting Statistics About IPv4 Aggregated Flows
=============================================================

This section provides an example for configuring NetStream to collect statistics about IPv4 flows aggregated based on the AS number. This facilitates accounting and management.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172373025__fig_dc_vrp_ns_cfg_003801), DeviceD connects network A and network B to the wide area network (WAN). DeviceD samples and aggregates flows before sending them to the NetStream Collector (NSC).

**Figure 1** Networking diagram of collecting statistics about aggregated flows![](../../../../public_sys-resources/note_3.0-en-us.png) 

* Interfaces 1 through 4 in this example represent GE0/1/0, GE0/2/0, GE0/3/0, and GE0/3/1, respectively.

  
![](figure/en-us_image_0000001531907881.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure reachable routes between the egress Router of the LAN and the WAN.
2. Configure reachable routes between the ingress Router of the LAN and the NSC.
3. Configure the ingress Router of the LAN to sent traffic statistics to the specified NSC.
4. Configure the ingress Router of the LAN to sent traffic statistics to the inbound interface on the NSC.
5. Aggregate sampled flows to reduce the data sent to the NSC.
6. Enable NetStream on the inbound interface of the ingress Router.

#### Data Preparation

To complete the configuration, you need the following data:

* IP address of each interface
* Address of the NSC
* Version for outputting NetStream flows
* NetStream sampling ratio
* ID of the slot in which the NetStream service processing board resides (In this example, the NetStream service processing board is in slot 3.)

#### Procedure

1. Configure IP addresses for each Router. The configuration details are not provided here.
2. Configure reachable routes between the WAN, DeviceA, and DeviceB.
   
   
   
   # Configure reachable routes between DeviceA and DeviceD.
   
   ```
   [*DeviceA] ip route-static 1.1.1.1 24 GigabitEthernet 0/1/0
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure reachable routes between DeviceB and DeviceD.
   
   ```
   [*DeviceB] ip route-static 1.1.1.1 24 GigabitEthernet 0/1/0
   ```
   ```
   [*DeviceB] commit
   ```
3. Configure reachable routes between DeviceD and the NSC.
   
   
   
   # Configure reachable routes between DeviceD and DeviceC.
   
   ```
   [*DeviceD] ip route-static 2.2.2.1 24 3.3.3.2
   ```
4. Enable NetStream on DeviceD.
   
   # Specify the distributed NetStream sampling mode on a board.
   ```
   [*DeviceD] slot 3
   ```
   ```
   [*DeviceD-slot-3] ip netstream sampler to slot self
   ```
   ```
   [*DeviceD-slot-3] quit
   ```
   
   # Enable NetStream statistics collection for incoming traffic.
   
   ```
   [*DeviceD] interface gigabitethernet 0/3/0
   ```
   ```
   [*DeviceD-GigabitEthernet0/3/0] ip netstream inbound
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   NetStream enabled on a main interface cannot collect traffic statistics about its sub-interface.
   
   # Output aggregated flows in V9 format.
   
   ```
   [*DeviceD] ip netstream aggregation as
   ```
   ```
   [*DeviceD-aggregation-as] enable
   ```
   ```
   [*DeviceD-aggregation-as] ip netstream export host 2.2.2.1 3000
   ```
   ```
   [*DeviceD-aggregation-as] ip netstream export source 3.3.3.1
   ```
   ```
   [*DeviceD-aggregation-as] export version 9
   ```
   
   # Enable NetStream packet sampling.
   
   ```
   [*DeviceD-GigabitEthernet0/3/0] ip netstream sampler fix-packets 1000 inbound
   ```
   ```
   [*DeviceD-GigabitEthernet0/3/0] quit
   ```
   ```
   [*DeviceD] commit
   ```
5. Verify the configuration.
   
   
   
   # Check whether flows are output.
   
   ```
   [~DeviceB] display ip netstream cache as slot 3
    DstIf   
    SrcIf  
    DstAs      Streams    Packets    Direction     SrcAs   
   --------------------------------------------------------------------------
    GI0/2/0        
    Unknown         
    0          985988     985988     out           0
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
   ip address 172.16.0.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  ip route-static 1.1.1.1 255.255.255.0 GigabitEthernet0/1/0
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
   ip address 172.17.1.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  ip route-static 1.1.1.1 255.255.255.0 GigabitEthernet0/1/0
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
   ip address 3.3.3.2 255.255.255.0
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
  slot 3
  ```
  ```
   ip netstream sampler to slot self
  ```
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
  interface GigabitEthernet0/1/0
  ```
  ```
   ip address 172.16.0.2 255.255.255.0 
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   ip address 172.17.1.2 255.255.255.0 
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/3/0
  ```
  ```
   ip address 1.1.1.1 255.255.255.0
  ```
  ```
   ip netstream inbound
  ```
  ```
   ip netstream sampler fix-packets 1000 inbound
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/3/1
  ```
  ```
   ip address 3.3.3.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  ip netstream aggregation as
  ```
  ```
   enable
  ```
  ```
   export version 9
  ```
  ```
   ip netstream export source 3.3.3.1
  ```
  ```
   ip netstream export host 2.2.2.1 3000
  ```
  ```
  #
  ```
  ```
  return
  ```