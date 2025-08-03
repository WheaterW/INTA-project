Example for Configuring PIM-DM
==============================

Example for Configuring PIM-DM

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001176663393__fig_dc_vrp_multicast_cfg_227201), it is required that the multicast function be deployed on devices so that user hosts on the network can receive VoD traffic in multicast mode. On a small-scale network with densely distributed group members, PIM-DM is often used to deploy the multicast function.

To complete the configuration, you need the following data:

* Multicast group G address: 225.1.1.1/24
* Multicast source S address: 10.1.4.100/24
* Version number of IGMP running between devices and user hosts: 2

**Figure 1** Network diagram for configuring basic PIM-DM functions![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.


  
![](figure/en-us_image_0000001176743357.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IP addresses and a unicast routing protocol for interfaces on each device.
2. Enable the multicast function on all devices and enable PIM-DM on all the involved interfaces.
3. Configure IGMP on all device interfaces connected to user hosts.

#### Procedure

1. Assign an IP address to each device interface and configure a unicast routing protocol. For detailed configurations, see Configuration Scripts.
2. Enable the multicast function globally and PIM-DM on all interfaces.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] multicast routing-enable
   [*DeviceA] interface 100GE 1/0/1
   [*DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] pim dm
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100GE 1/0/2
   [*DeviceA-100GE1/0/2] pim dm
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB, DeviceC, and DeviceD are similar to those of DeviceA.
3. Configure IGMP on all device interfaces connected to user hosts.
   
   
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] interface 100GE 1/0/1
   [~DeviceC-100GE1/0/1] undo portswitch
   [*DeviceC-100GE1/0/1] igmp enable
   [*DeviceC-100GE1/0/1] igmp static-group 225.1.1.1
   [*DeviceC-100GE1/0/1] quit
   [*DeviceC] commit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] interface 100GE 1/0/2
   [~DeviceD-100GE 1/0/2] undo portswitch
   [*DeviceD-100GE1/0/2] igmp enable
   [*DeviceD-100GE1/0/2] igmp static-group 225.1.1.1
   [*DeviceD-100GE1/0/2] quit
   [*DeviceD] commit
   ```

#### Verifying the Configuration

# Run the **display pim interface** command to check PIM-DM configurations and the running status on device interfaces. The following example shows the PIM-DM configurations on DeviceB.

```
<DeviceB> display pim interface
 VPN-Instance: public net
 Interface           State     NbrCnt HelloInt     DR-Pri   DR-Address      
 100GE1/0/1             up         1       30          1     10.1.1.2 (local) 
 100GE1/0/2             up         1       30          1     10.1.2.2         
 100GE1/0/3             up         1       30          1     10.1.3.2 
```

# Run the **display pim neighbor** command to check PIM-DM neighbor relationships between devices. The following example uses the command output (containing PIM-DM neighbor relationships) on DeviceB.

```
<DeviceB> display pim neighbor
VPN-Instance: public net
 Total Number of Neighbors = 3 

        Neighbor           Interface   Uptime  Expires  Dr-Priority BFD-Session 
        10.1.1.1            100GE1/0/1  04:34:59 00:01:18            1           N
        10.1.2.2            100GE1/0/2  04:29:56 00:01:23            1           N
        10.1.3.2            100GE1/0/3  04:24:22 00:01:28            1           N
```

# Run the **display pim routing-table** command to check the PIM routing tables of devices. When the multicast source S (10.1.4.100/24) sends multicast data to the multicast group G, an MDT is established through flooding. Each device on the MDT has an (S, G) entry.

```
<DeviceA> display pim routing-table
 VPN-Instance: public net
 Total 0 (*, G) entry; 1 (S, G) entry

 (10.1.4.100, 225.1.1.1)
     Protocol: pim-dm, Flag: LOC ACT 
     UpTime: 00:08:18     
     Upstream interface: 100GE1/0/2, Refresh time: 00:08:18
         Upstream neighbor: NULL
         RPF prime neighbor: NULL
     Downstream interface(s) information:
     Total number of downstreams: 1
        1: 100GE1/0/1
             Protocol: pim-dm, UpTime: 00:08:18, Expires: never
<DeviceB> display pim routing-table
 VPN-Instance: public net
 Total 0 (*, G) entry; 1 (S, G) entry

 (10.1.4.100, 225.1.1.1)
     Protocol: pim-dm, Flag: ACT 
     UpTime: 00:10:25     
     Upstream interface: 100GE1/0/1, Refresh time: 00:10:25
         Upstream neighbor: 10.1.1.1
         RPF prime neighbor: 10.1.1.1
     Downstream interface(s) information:
     Total number of downstreams: 2
        1: 100GE1/0/2
             Protocol: pim-dm, UpTime: 00:06:48, Expires: never 
        2: 100GE1/0/3
             Protocol: pim-dm, UpTime: 00:05:53, Expires: never 
<DeviceC> display pim routing-table
 VPN-Instance: public net
 Total 0 (*, G) entry; 1 (S, G) entry

 (10.1.4.100, 225.1.1.1)
     Protocol: pim-dm, Flag: ACT 
     UpTime: 00:17:13     
     Upstream interface: 100GE1/0/2, Refresh time: 00:17:13
         Upstream neighbor: 10.1.2.1
         RPF prime neighbor: 10.1.2.1
     Downstream interface(s) information:
     Total number of downstreams: 1
        1: 100GE1/0/1
             Protocol: pim-dm, UpTime: 00:11:47, Expires: -
<DeviceD> display pim routing-table
 VPN-Instance: public net
 Total 0 (*, G) entry; 1 (S, G) entry

 (10.1.4.100, 225.1.1.1)
     Protocol: pim-dm, Flag: ACT 
     UpTime: 00:09:58     
     Upstream interface: 100GE1/0/3, Refresh time: 00:09:58
         Upstream neighbor: 10.1.3.1
         RPF prime neighbor: 10.1.3.1
     Downstream interface(s) information:
     Total number of downstreams: 1
        1: 100GE1/0/2
             Protocol: pim-dm, UpTime: 00:05:26, Expires: - 
```
#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  multicast routing-enable
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.1 255.255.255.0
   pim dm
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.4.1 255.255.255.0
   pim dm
  #
  ospf 1
   area 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.1.4.0 0.0.0.255
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  multicast routing-enable
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.2 255.255.255.0
   pim dm
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.2.1 255.255.255.0
   pim dm
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 10.1.3.1 255.255.255.0
   pim dm
  #
  ospf 1
   area 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.1.2.0 0.0.0.255
    network 10.1.3.0 0.0.0.255
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  multicast routing-enable
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.5.1 255.255.255.0
   pim dm
   igmp enable
   igmp static-group 225.1.1.1
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.2.2 255.255.255.0
   pim dm
  #
  ospf 1
   area 0.0.0.0
    network 10.1.2.0 0.0.0.255
    network 10.1.5.0 0.0.0.255
  #
  return
  ```
* DeviceD
  
  ```
  #
  sysname DeviceD
  #
  multicast routing-enable
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.6.1 255.255.255.0
   pim dm
   igmp enable
   igmp static-group 225.1.1.1
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 10.1.3.2 255.255.255.0
   pim dm
  #
  ospf 1
   area 0.0.0.0
    network 10.1.3.0 0.0.0.255
    network 10.1.6.0 0.0.0.255
  #
  return
  ```