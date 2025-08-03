Example for Configuring Priority Mappings for MPLS Packets Based on BA Classification
=====================================================================================

This section provides an example for configuring priority mappings for MPLS packets based on BA classification.

#### Networking Requirements

MPLS neighbor relationships are established between three Routers. When IP packets reach DeviceA, DeviceA adds MPLS headers to the IP packets before transmitting them to DeviceC. When the MPLS packets reach DeviceC, DeviceC removes their MPLS headers and forwards them as IP packets.

The DSCP value of the IP packets needs to be changed to the EXP value of MPLS packets on DeviceA, and the EXP value of the MPLS packets needs to be changed to the DSCP value of the IP packets on DeviceC.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* In this configuration example, it is assumed that MPLS has been configured on the three Routers so that DeviceA forwards IP traffic as MPLS traffic to DeviceC, and DeviceC forwards MPLS traffic as IP traffic.
* This example lists only the commands related to QoS.
* interface1 and interface2 in this example represent GE 0/1/0 and GE 0/2/0, respectively.

**Figure 1** Networking diagram for configuring priority mappings based on BA classification  
![](images/fig_dc_ne_qos_cfg_007201.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. On the inbound interface GE 0/1/0 of DeviceA, configure the mapping from the IP DSCP field to the MPLS EXP field and enable BA classification.
2. On the inbound interface GE 0/1/0 of DeviceC, configure the mapping from the MPLS EXP field to the IP DSCP field and enable BA classification.

#### Data Preparation

To complete the configuration, you need the following data:

MPLS EXP values, service classes, colors, and IP DSCP values to be mapped


#### Procedure

1. Configure basic MPLS functions and routes.
   
   
   
   For configuration details, see *HUAWEI NE40E-M2 series Universal Service Router Configuration Guide - MPLS*.
2. Configure the mapping from the IP DSCP field to the MPLS EXP field on GE 0/1/0 of DeviceA.
   
   
   ```
   [~DeviceA] diffserv domain default
   ```
   ```
   [~DeviceA-dsdomain-default] ip-dscp-inbound 18 phb af4 green
   ```
   ```
   [*DeviceA-dsdomain-default] mpls-exp-outbound af4 green map 5
   ```
   ```
   [*DeviceA-dsdomain-default] commit
   ```
   ```
   [~DeviceA-dsdomain-default] quit
   ```
   ```
   [~DeviceA] interface GigabitEthernet 0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] trust upstream default
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [~DeviceA] interface GigabitEthernet 0/2/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0] trust upstream default
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0] quit
   ```
   
   In the preceding configuration, the service class AF2 (green packets with the DSCP value being 18) is mapped to the service class AF4 of the Router on the inbound interface of DeviceA; and the service class AF4 of the Router is mapped to the MPLS service class EF (priority 5) on the outbound interface. In this manner, the traffic sent from DeviceA is EF traffic.
3. Configure the mapping from the MPLS EXP field to the IP DSCP field on GE 0/1/0 of DeviceC.
   
   
   ```
   [~DeviceC] diffserv domain default
   ```
   ```
   [~DeviceC-dsdomain-default] mpls-exp-inbound 5 phb af3 green
   ```
   ```
   [*DeviceC-dsdomain-default] ip-dscp-outbound af3 green map 32
   ```
   ```
   [*DeviceC-dsdomain-default] commit
   ```
   ```
   [~DeviceC-dsdomain-default] quit
   ```
   ```
   [~DeviceC] interface GigabitEthernet 0/1/0
   ```
   ```
   [~DeviceC-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [~DeviceC-GigabitEthernet0/1/0] trust upstream default
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceC-GigabitEthernet0/1/0] quit
   ```
   ```
   [~DeviceC] interface GigabitEthernet 0/2/0
   ```
   ```
   [~DeviceC-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [~DeviceC-GigabitEthernet0/2/0] trust upstream default
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] commit
   ```
   ```
   [~DeviceC-GigabitEthernet0/2/0] quit
   ```
   
   In the preceding configuration, the MPLS priority 5 is mapped to the service class AF3 (green packets) of the Router on the inbound interface of DeviceC; and the service class AF3 (green packets) of the Router is mapped to the DSCP value 32 on the outbound interface. In this manner, the traffic sent from DeviceC is AF4 traffic.
4. Verify the configuration.
   
   
   
   After the configuration is complete, 100 Mbit/s traffic with the DSCP value being 18 is sent from GE 0/1/0 of DeviceA, and 100 Mbit/s traffic with the DSCP value being 32 is sent from DeviceC.

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
  diffserv domain default
  ```
  ```
    ip-dscp-inbound 18 phb af4 green 
  ```
  ```
    mpls-exp-outbound af4 green map 5
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
   ip address 2.2.2.1 255.255.255.0
  ```
  ```
   trust upstream default
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
   ip address 3.3.3.1 255.255.255.0
  ```
  ```
   trust upstream default
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
  diffserv domain default
  ```
  ```
    ip-dscp-outbound af3 green map 32
  ```
  ```
    mpls-exp-inbound 5 phb af3 green 
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
   ip address 4.4.4.1 255.255.255.0
  ```
  ```
   trust upstream default
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
   ip address 5.5.5.1 255.255.255.0
  ```
  ```
   trust upstream default
  ```
  ```
  #
  ```
  ```
  return
  ```