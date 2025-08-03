Example for Collecting Statistics About IPv4 Flexible Flows
===========================================================

This section provides an example for deploying NetStream to collect statistics about IPv4 flexible flows. This example uses the configurations on an IPv4 network.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172373040__fig_dc_vrp_ns_cfg_003801), DeviceD connects network A and network B to the wide area network (WAN). DeviceD samples and aggregates flows before sending them to the NetStream Collector (NSC).

**Figure 1** Networking diagram of collecting statistics about IPv4 flexible flows![](../../../../public_sys-resources/note_3.0-en-us.png) 

* Interfaces 1 through 4 in this example represent GE0/1/0, GE0/2/0, GE0/3/0, and GE0/3/1, respectively.

  
![](figure/en-us_image_0000001481551174.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure reachable routes between DeviceA and DeviceB of the LAN and the WAN.
2. Configure reachable routes between DeviceD and the NSC.
3. Configure DeviceD to send traffic statistics to the inbound interface of the specified NSC.
4. Configure the flexible flow output function for traffic.
5. Enable NetStream on the outbound interface of DeviceD.

#### Data Preparation

To complete the configuration, you need the following data:

* IP address of each interface
* Version for outputting NetStream flows
* NetStream sampling ratio
* ID of the slot in which the NetStream service processing board resides (In this example, the NetStream service processing board is in slot 3.)

#### Procedure

1. Configure IP addresses for each Router. The configuration details are not provided here.
2. Configure reachable routes between the WAN, DeviceA, and DeviceB.
   
   
   
   # Configure reachable routes between DeviceA and DeviceD.
   
   ```
   [~DeviceA] ip route-static 192.168.1.1 24 gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure reachable routes between DeviceB and DeviceD.
   
   ```
   [~DeviceB] ip route-static 192.168.1.1 24 gigabitethernet 0/1/0
   ```
   ```
   [*DeviceB] commit
   ```
   
   # Configure reachable routes between DeviceD and DeviceE.
   
   ```
   [~DeviceD] ip route-static 172.17.1.3 24 gigabitethernet 0/3/0
   ```
   ```
   [*DeviceD] commit
   ```
3. Configure reachable routes between DeviceD and the NSC.
   
   
   
   # Configure reachable routes between DeviceD and DeviceC.
   
   ```
   [~DeviceD] ip route-static 192.168.2.1 24 192.168.2.2
   ```
   ```
   [*DeviceD] commit
   ```
4. Enable NetStream on DeviceD.
   
   
   
   # Specify the distributed NetStream sampling mode on a board.
   
   ```
   [~DeviceD] slot 3
   ```
   ```
   [~DeviceD-slot-3] ip netstream sampler to slot self
   ```
   ```
   [*DeviceD-slot-3] quit
   ```
   ```
   [*DeviceD] commit
   ```
   
   # Enable NetStream statistics collection for incoming traffic.
   
   ```
   [~DeviceD] interface gigabitethernet 0/3/0
   ```
   ```
   [*DeviceD-GigabitEthernet0/3/0] ip netstream inbound
   ```
   ```
   [~DeviceD-GigabitEthernet0/3/0] quit
   ```
   ```
   [*DeviceD] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   NetStream enabled on a main interface cannot collect traffic statistics about its sub-interface.
   
   # Configure the flexible flow template in V9 format.
   
   ```
   [~DeviceD] ip netstream record aa
   ```
   ```
   [*DeviceD-record-aa] match source as
   ```
   ```
   [*DeviceD-record-aa] collect first switched
   ```
   ```
   [*DeviceD] commit
   ```
   
   # Output flexible flows in V9 format.
   
   ```
   [~DeviceD] ip netstream export version 9
   ```
   ```
   [~DeviceD] ip netstream apply record aa
   ```
   ```
   [~DeviceD] ip netstream export source 192.168.2.1
   ```
   ```
   [~DeviceD] ip netstream export host 192.168.2.2 3000
   ```
   ```
   [*DeviceD] commit
   ```
   
   # Enable NetStream packet sampling.
   
   ```
   [~DeviceD] interface gigabitethernet 0/3/0
   ```
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
   
   
   
   # Check whether the flexible flow template is output correctly.
   
   ```
   [~DeviceD] display ip netstream export template
   ```
   ```
   ------------------------------------------------------
   TemplateName                        Success     Failed
   ------------------------------------------------------
   origin                                   69          0
   Record(system)                           14          0
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
  ip route-static 192.168.1.1 255.255.255.0 GigabitEthernet0/1/0
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
  ip route-static 192.168.1.1 255.255.255.0 GigabitEthernet0/1/0
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
   ip address 192.168.2.2 255.255.255.0
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
   ip address 192.168.1.1 255.255.255.0
  ```
  ```
   ip route-static 172.17.1.3 24 gigabitethernet 0/3/0
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
   ip address 192.168.2.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
   ip netstream export version 9
  ```
  ```
   ip netstream export source 192.168.2.1
  ```
  ```
   ip netstream export host 192.168.2.2 3000
  ```
  ```
  #
  ```
  ```
   ip netstream record aa
  ```
  ```
   match source address
  ```
  ```
   collect first switched
  ```
  ```
  #
  ```
  ```
   ip netstream apply record aa
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
  interface GigabitEthernet0/1/0
  ```
  ```
   ip address 172.17.1.3 255.255.255.0
  ```
  ```
  #
  ```
  ```
  return
  ```