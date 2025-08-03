Example for Configuring IPv4 PIM FRR
====================================

Example for Configuring IPv4 PIM FRR

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001313940861__fig_dc_vrp_multicast_cfg_227901), DeviceA is a PIM device that is not directly connected to the multicast source. PIM FRR can be deployed on DeviceA to meet the requirements of the multicast services that have high requirements for real-time transmission. The primary link is DeviceB -> DeviceA, and the backup link is DeviceB -> DeviceC -> DeviceA. Multicast traffic is bidirectionally forwarded along the primary and backup links. In normal cases, traffic received from the primary link is accepted. If the primary link fails, traffic received from the backup link is accepted.

**Figure 1** Configuring PIM FRR![](public_sys-resources/note_3.0-en-us.png) 

In this example, Interface1, Interface2, and Interface3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.


  
![](figure/en-us_image_0000001317622241.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign IP addresses to interfaces on each device and configure a unicast routing protocol.
2. Enable OSPF IP FRR on DeviceA.![](public_sys-resources/note_3.0-en-us.png) 
   
   Unicast FRR can be implemented among static backup FRR routes, dynamic backup FRR routes, or both static and dynamic backup FRR routes. In this example, it is implemented among dynamic backup FRR routes.
3. Enable the multicast function and PIM-SM on all devices that need to provide multicast services.
4. Configure a static IGMP multicast group on the interface connected to the host.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   Configure a static IGMP multicast group only when multicast data of a multicast group needs to be received stably and steadily.
5. Configure the RP function.
6. Enable PIM FRR on DeviceA.

#### Data Preparation

To complete the configuration, you need the following data:

* Multicast group (G) address: 225.1.0.0
* Multicast source (S) address: 10.0.5.100

#### Procedure

1. Assign IP addresses to interfaces and configure a unicast routing protocol. For configuration details, see configuration scripts.
2. Enable OSPF IP FRR on DeviceA.
   
   
   ```
   [~DeviceA] ospf 1 
   [~DeviceA-ospf-1] frr 
   [*DeviceA-ospf-1] loop-free-alternate
   [*DeviceA-ospf-1] quit
   [*DeviceA] commit
   ```
3. Enable the multicast function on each device and PIM-SM on each interface.
   
   
   
   # Enable the multicast function on all devices and PIM-SM on all the involved interfaces.
   
   ```
   [~DeviceA] multicast routing-enable
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] pim sm
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] pim sm
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100ge 1/0/3
   [*DeviceA-100GE1/0/3] pim sm
   [*DeviceA-100GE1/0/3] quit
   ```
   
   The configurations of DeviceB and DeviceC are similar to the configuration of DeviceA. For details, see the configuration files.
4. Configure a static IGMP group on the interface connected to the host to simulate a user joining the multicast group.
   
   
   
   # Configure a static IGMP group on DeviceA's interface connected to the host side.
   
   ```
   [~DeviceA] interface 100ge 1/0/3
   [~DeviceA-100GE1/0/3] igmp static-group 225.1.0.0 source 10.0.5.100
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] commit
   ```
5. Configure the RP function.
   
   
   
   # Configure a candidate-BSR (C-BSR) and candidate-RP (C-RP) on DeviceA. The configurations of DeviceB and DeviceC are similar to the configuration of DeviceA.
   
   ```
   [~DeviceA] pim
   [~DeviceA-pim] c-bsr 100ge 1/0/1
   [*DeviceA-pim] c-rp 100ge 1/0/1
   [*DeviceA-pim] quit
   [*DeviceA] commit
   ```
   
   # Check the PIM routing table of DeviceA. The command output shows that there are no backup inbound or outbound interfaces.
   
   ```
   [~DeviceA] display pim routing-table
    VPN-Instance: public net
    Total 0 (*, G) entry; 1 (S, G) entry
   
    (10.0.5.100, 225.1.0.0)
        RP: 192.168.8.2 (local)
        Protocol: pim-sm, Flag: SPT SG_RCVR
        UpTime: 01:21:36
        Upstream interface: 100GE1/0/1, Refresh time: 01:21:36
            Upstream neighbor: 192.168.8.1
            RPF prime neighbor: 192.168.8.1
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: 100GE1/0/3
                Protocol: static, UpTime: 01:05:00, Expires: -
   ```
6. Enable PIM FRR on DeviceA.
   
   
   ```
   [~DeviceA] pim
   [~DeviceA-pim] rpf-frr
   [*DeviceA-pim] quit
   [*DeviceA] commit
   ```
   
   # Check the PIM routing table of DeviceA. Because PIM FRR is enabled, a backup inbound interface is generated in the PIM entry.
   
   ```
   [*DeviceA] display pim routing-table
    VPN-Instance: public net
    Total 0 (*, G) entry; 1 (S, G) entry
   
    (10.0.5.100, 225.1.0.0)
        RP: 192.168.8.2 (local)
        Protocol: pim-sm, Flag: SPT SG_RCVR
        UpTime: 01:22:40
        Upstream interface:  100GE1/0/1, Refresh time: 01:22:40
            Upstream neighbor: 192.168.8.1
            RPF prime neighbor: 192.168.8.1
        Backup upstream interface: 100GE1/0/2
            Backup upstream neighbor: 192.168.10.1
            Backup RPF prime neighbor: 192.168.10.1
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: 100GE1/0/3
                Protocol: static, UpTime: 01:06:04, Expires: -
   ```
7. Verify the configuration.
   
   
   
   # Run the **shutdown** command on 100GE1/0/1 of DeviceB to simulate a link fault.
   
   ```
   [~DeviceB] interface 100ge 1/0/1
   [*DeviceB-100GE1/0/1] shutdown
   [*DeviceB-100GE1/0/1] commit
   ```
   
   # Run the **display pim routing-table** command on DeviceA immediately to check the PIM routing table.
   
   ```
   [~DeviceA] display pim routing-table
    VPN-Instance: public net
    Total 0 (*, G) entry; 1 (S, G) entry
   
    (10.0.5.100, 225.1.0.0)
        RP: NULL
        Protocol: pim-sm, Flag: SPT SG_RCVR
        UpTime: 01:24:22
        Upstream interface: 100GE1/0/2, Refresh time: 01:24:22
            Upstream neighbor: 192.168.10.1
            RPF prime neighbor: 192.168.10.1
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: 100GE1/0/3
                Protocol: static, UpTime: 01:07:46, Expires: -
   ```
   
   The command output shows that the inbound interface of the route on DeviceA has been changed to 100GE1/0/2, which was on the original backup link.

#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname Device A
  #
  multicast routing-enable
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.8.2 255.255.255.0
   pim sm
   ospf enable 1 area 0.0.0.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.10.2 255.255.255.0
   pim sm
   ospf enable 1 area 0.0.0.0
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 192.168.11.1 255.255.255.0
   pim sm
   igmp static-group 225.1.0.0 source 10.0.5.100
   ospf enable 1 area 0.0.0.0
  #
  ospf 1
   frr
    loop-free-alternate 
   area 0.0.0.0
    network 192.168.11.0 0.0.0.255
    network 192.168.8.0 0.0.0.255
    network 192.168.10.0 0.0.0.255
  #
  pim
   c-bsr 100GE1/0/1
   c-rp 100GE1/0/1
   rpf-frr
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname Device B
  #
  multicast routing-enable
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 10.0.5.100 255.255.255.0
   pim sm
   ospf enable 1 area 0.0.0.0
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.8.1 255.255.255.0
   pim sm
   ospf enable 1 area 0.0.0.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.9.1 255.255.255.0
   pim sm
   ospf enable 1 area 0.0.0.0
  #
  ospf 1
   area 0.0.0.0
    network 10.0.5.0 0.0.0.255
    network 192.168.8.0 0.0.0.255
    network 192.168.9.0 0.0.0.255
  #
  pim
   c-bsr 100GE1/0/1
   c-rp 100GE1/0/1
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname Device C
  #
  multicast routing-enable
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 192.168.9.2 255.255.255.0
   pim sm
   ospf enable 1 area 0.0.0.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.10.1 255.255.255.0
   pim sm
   ospf enable 1 area 0.0.0.0
  #
  ospf 1
   area 0.0.0.0
    network 192.168.9.0 0.0.0.255
    network 192.168.10.0 0.0.0.255
  #
  pim
   c-bsr 100GE1/0/2
   c-rp 100GE1/0/2
  #
  return
  ```