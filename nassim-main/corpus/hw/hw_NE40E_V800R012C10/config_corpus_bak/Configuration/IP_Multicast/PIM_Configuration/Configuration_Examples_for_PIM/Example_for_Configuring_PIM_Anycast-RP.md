Example for Configuring PIM Anycast-RP
======================================

In the scenario where multiple multicast sources and receivers are located in a PIM-SM domain, you can configure Anycast-Rendezvous Point (RP) peer relationships so that IP routing will automatically select the topologically closest RP for each source and receiver. This alleviates burdens on RPs, implements RP backup, and optimizes multicast forwarding paths.

#### Networking Requirements

On a traditional PIM-SM domain, all multicast groups map to one RP. When the network is overloaded or traffic congests on an RP, the RP may be overburdened. If the RP fails, routes are converged slowly or multicast packets are forwarded over non-optimal paths. Configuring the Anycast-RP in the PIM-SM domain can address these problems. IP routing will automatically select the topologically closest RP for each source and receiver. This feature can accelerate data transmission to receivers. On the network shown in [Figure 1](#EN-US_TASK_0172366936__fig61819557114), Receiver 2 requests multicast data from the source. In this case, configure an Anycast-RP peer relationship between DeviceC and DeviceD so that Receiver 2 can send a Join message to the closest RP, that is, DeviceD. After receiving multicast data from the source, DeviceA encapsulates the multicast data into a Register message and sends it to DeviceC. Upon receipt, DeviceC forwards it to DeviceD so that Receiver 2 can receive the multicast data from the source.

**Figure 1** Configuring PIM Anycast-RP  
![](figure/en-us_image_0258940455.png)

| Device | Interface | IP Address |
| --- | --- | --- |
| DeviceA | GE 0/1/0 | 10.110.1.1/24 |
| GE 0/2/0 | 192.168.1.1/24 |
| DeviceB | GE 0/1/0 | 192.168.2.1/24 |
| DeviceC | GE 0/1/0 | 192.168.3.1/24 |
| GE 0/2/0 | 192.168.1.2/24 |
| GE 0/3/0 | 10.110.2.1/24 |
| Loopback 0 | 1.1.1.1/32 |
| Loopback 1 | 2.2.2.2/32 |
| DeviceD | GE 0/1/0 | 192.168.2.2/24 |
| GE 0/2/0 | 10.110.3.1/24 |
| GE 0/3/0 | 192.168.3.2/24 |
| Loopback 0 | 1.1.1.1/32 |
| Loopback 1 | 3.3.3.3/32 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IP address to each Router interface and configure OSPF to implement IP interworking.
2. Enable multicast routing on each Router and PIM-SM on each Router interface.
3. Enable IGMP on interfaces connecting Routers to hosts.
4. On DeviceC and DeviceD, configure the Loopback 0 interfaces as both Candidate-Rendezvous Points (C-RPs) and Candidate-BootStrap Routers (C-BSRs).
5. Configure the address of the Loopback 0 interfaces on DeviceC and DeviceD as the Anycast-RP address.
6. On DeviceC and DeviceD, configure the addresses of the Loopback 1 interfaces as the local addresses of Anycast-RPs.
7. Configure an Anycast-RP peer relationship between DeviceC and DeviceD.

#### Data Preparation

To complete the configuration, you need the following data:

* Multicast group address: 226.1.1.1/24
* RP address
* Local RP address of the Anycast-RP

#### Procedure

1. Assign an IP address to each Router interface and configure OSPF to implement IP interworking. Enable multicast routing on each Router and PIM-SM on each Router interface. For configuration details, see Configuration Files in this section.
   
   
   
   # Assign an IP address and mask for each Router interface in the PIM-SM domain based on [Figure 1](#EN-US_TASK_0172366936__fig61819557114), and configure OSPF between Routers to implement IP interworking. Enable multicast routing on each Router and PIM-SM on each Router interface.
   
   # Configure DeviceA.
   
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
   [~DeviceA] multicast routing-enable
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] ip address 10.110.1.1 24
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] pim sm
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceA] interface gigabitEthernet 0/2/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] ip address 192.168.1.1 24
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] pim sm
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceA] ospf
   ```
   ```
   [*DeviceA-ospf-1] area 0
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.0] network 10.110.1.0 0.0.0.255
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.0] network 192.168.1.0 0.0.0.255
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [*DeviceA-ospf-1] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceB
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceB] multicast routing-enable
   ```
   ```
   [*DeviceB] interface gigabitEthernet 0/1/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] ip address 192.168.2.1 24
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] pim sm
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceB] ospf
   ```
   ```
   [*DeviceB-ospf-1] area 0
   ```
   ```
   [*DeviceB-ospf-1-area-0.0.0.0] network 192.168.2.0 0.0.0.255
   ```
   ```
   [*DeviceB-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [*DeviceB-ospf-1] quit
   ```
   ```
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceC
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceC] multicast routing-enable
   ```
   ```
   [*DeviceC] interface gigabitEthernet 0/1/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] ip address 192.168.3.1 24
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] pim sm
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceC] interface gigabitEthernet 0/2/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] ip address 192.168.1.2 24
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] pim sm
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceC] interface gigabitethernet 0/3/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/3/0] ip address 10.110.2.1 24
   ```
   ```
   [*DeviceC-GigabitEthernet0/3/0] pim sm
   ```
   ```
   [*DeviceC-GigabitEthernet0/3/0] quit
   ```
   ```
   [*DeviceC] interface loopback 0
   ```
   ```
   [*DeviceC-LoopBack0] ip address 1.1.1.1 32
   ```
   ```
   [*DeviceC-LoopBack0] pim sm
   ```
   ```
   [*DeviceC-LoopBack0] quit
   ```
   ```
   [*DeviceC] interface loopback 1
   ```
   ```
   [*DeviceC-LoopBack1] ip address 2.2.2.2 32
   ```
   ```
   [*DeviceC-LoopBack1] pim sm
   ```
   ```
   [*DeviceC-LoopBack1] quit
   ```
   ```
   [*DeviceC] ospf
   ```
   ```
   [*DeviceC-ospf-1] area 0
   ```
   ```
   [*DeviceC-ospf-1-area-0.0.0.0] network 192.168.3.0 0.0.0.255
   ```
   ```
   [*DeviceC-ospf-1-area-0.0.0.0] network 192.168.1.0 0.0.0.255
   ```
   ```
   [*DeviceC-ospf-1-area-0.0.0.0] network 10.110.2.0 0.0.0.255
   ```
   ```
   [*DeviceC-ospf-1-area-0.0.0.0] network 1.1.1.1 0.0.0.0
   ```
   ```
   [*DeviceC-ospf-1-area-0.0.0.0] network 2.2.2.2 0.0.0.0
   ```
   ```
   [*DeviceC-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [*DeviceC-ospf-1] quit
   ```
   ```
   [*DeviceC] commit
   ```
   
   # Configure DeviceD.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceD
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceD] multicast routing-enable
   ```
   ```
   [*DeviceD] interface gigabitEthernet 0/1/0
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] ip address 192.168.2.2 24
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] pim sm
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceD] interface gigabitethernet 0/2/0
   ```
   ```
   [*DeviceD-GigabitEthernet0/2/0] ip address 10.110.3.1 24
   ```
   ```
   [*DeviceD-GigabitEthernet0/2/0] pim sm
   ```
   ```
   [*DeviceD-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceD] interface gigabitEthernet 0/3/0
   ```
   ```
   [*DeviceD-GigabitEthernet0/3/0] ip address 192.168.3.2 24
   ```
   ```
   [*DeviceD-GigabitEthernet0/3/0] pim sm
   ```
   ```
   [*DeviceD-GigabitEthernet0/3/0] quit
   ```
   ```
   [*DeviceD] interface loopback 0
   ```
   ```
   [*DeviceD-LoopBack0] ip address 1.1.1.1 32
   ```
   ```
   [*DeviceD-LoopBack0] pim sm
   ```
   ```
   [*DeviceD-LoopBack0] quit
   ```
   ```
   [*DeviceD] interface loopback 1
   ```
   ```
   [*DeviceD-LoopBack1] ip address 3.3.3.3 32
   ```
   ```
   [*DeviceD-LoopBack1] pim sm
   ```
   ```
   [*DeviceD-LoopBack1] quit
   ```
   ```
   [*DeviceD] ospf
   ```
   ```
   [*DeviceD-ospf-1] area 0
   ```
   ```
   [*DeviceD-ospf-1-area-0.0.0.0] network 192.168.2.0 0.0.0.255
   ```
   ```
   [*DeviceD-ospf-1-area-0.0.0.0] network 10.110.3.0 0.0.0.255
   ```
   ```
   [*DeviceD-ospf-1-area-0.0.0.0] network 192.168.3.0 0.0.0.255
   ```
   ```
   [*DeviceD-ospf-1-area-0.0.0.0] network 1.1.1.1 0.0.0.0
   ```
   ```
   [*DeviceD-ospf-1-area-0.0.0.0] network 3.3.3.3 0.0.0.0
   ```
   ```
   [*DeviceD-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [*DeviceD-ospf-1] quit
   ```
   ```
   [*DeviceD] commit
   ```
2. Enable IGMP on interfaces connecting Routers to hosts.
   
   
   
   # Enable IGMP on the interfaces connecting DeviceC and DeviceD to hosts.
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] interface gigabitethernet 0/3/0
   ```
   ```
   [~DeviceC-GigabitEthernet0/3/0] igmp enable
   ```
   ```
   [*DeviceC-GigabitEthernet0/3/0] quit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] interface gigabitethernet 0/2/0
   ```
   ```
   [~DeviceD-GigabitEthernet0/2/0] igmp enable
   ```
   ```
   [*DeviceD-GigabitEthernet0/2/0] quit
   ```
3. On DeviceC and DeviceD, configure the Loopback 0 interfaces as both C-RPs and C-BSRs.
   
   
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] pim
   ```
   ```
   [*DeviceC-pim] c-bsr loopback 0
   ```
   ```
   [*DeviceC-pim] c-rp loopback 0
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] pim
   ```
   ```
   [*DeviceD-pim] c-bsr loopback 0
   ```
   ```
   [*DeviceD-pim] c-rp loopback 0
   ```
4. Configure the address of the Loopback 0 interfaces on DeviceC and DeviceD as the Anycast-RP address.
   
   
   
   # Configure DeviceC.
   
   ```
   [*DeviceC-pim] anycast-rp 1.1.1.1
   ```
   ```
   [*DeviceC-pim-anycast-rp-1.1.1.1] quit
   ```
   
   # Configure DeviceD.
   
   ```
   [*DeviceD-pim] anycast-rp 1.1.1.1
   ```
   ```
   [*DeviceD-pim-anycast-rp-1.1.1.1] quit
   ```
5. On DeviceC and DeviceD, configure the addresses of the Loopback 1 interfaces as the local addresses of Anycast-RPs.
   
   
   
   # Configure DeviceC.
   
   ```
   [*DeviceC-pim] anycast-rp 1.1.1.1
   ```
   ```
   [*DeviceC-pim-anycast-rp-1.1.1.1] local-address 2.2.2.2
   ```
   ```
   [*DeviceC-pim-anycast-rp-1.1.1.1] quit
   ```
   
   # Configure DeviceD.
   
   ```
   [*DeviceD-pim] anycast-rp 1.1.1.1
   ```
   ```
   [*DeviceD-pim-anycast-rp-1.1.1.1] local-address 3.3.3.3
   ```
   ```
   [*DeviceD-pim-anycast-rp-1.1.1.1] quit
   ```
6. Configure an Anycast-RP peer relationship between DeviceC and DeviceD.
   
   
   
   # Configure DeviceC.
   
   ```
   [*DeviceC-pim] anycast-rp 1.1.1.1
   ```
   ```
   [*DeviceC-pim-anycast-rp-1.1.1.1] peer 3.3.3.3
   ```
   ```
   [*DeviceC-pim-anycast-rp-1.1.1.1] quit
   ```
   ```
   [*DeviceC-pim] quit
   ```
   ```
   [*DeviceC] commit
   ```
   
   # Configure DeviceD.
   
   ```
   [*DeviceD-pim] anycast-rp 1.1.1.1
   ```
   ```
   [*DeviceD-pim-anycast-rp-1.1.1.1] peer 2.2.2.2
   ```
   ```
   [*DeviceD-pim-anycast-rp-1.1.1.1] quit
   ```
   ```
   [*DeviceD-pim] quit
   ```
   ```
   [*DeviceD] commit
   ```
7. Verify the configuration.
   
   
   
   # Run the **display pim rp-info** command on DeviceC and DeviceD to check RP information.
   
   ```
   <DeviceC> display pim rp-info
   ```
   ```
    VPN-Instance: public net
    PIM-SM BSR RP Number:1
    Group/MaskLen: 224.0.0.0/4
        RP: 1.1.1.1 (local)
        Priority: 0
        Uptime: 00:45:19
        Expires: 00:02:11
   ```
   ```
   <DeviceD> display pim rp-info
   ```
   ```
    VPN-Instance: public net
    PIM-SM BSR RP Number:1
    Group/MaskLen: 224.0.0.0/4
        RP: 1.1.1.1 (local)
        Priority: 0
        Uptime: 02:27:56
        Expires: 00:01:39
   
   ```
   
   The preceding command output shows that DeviceC and DeviceD both serve as an RP and can forward Register messages from the multicast source to each other.
   
   # Run the **display pim routing-table** command to check PIM entries on each Router. Source (10.110.1.2/24) in the PIM-SM domain sends multicast data to G (226.1.1.1), and Receiver2 joins G and receives the multicast data sent to G. Source registers with DeviceC, and Receiver 2 sends a Join message to DeviceD.
   
   ```
   <DeviceC> display pim routing-table
   ```
   ```
    VPN-Instance: public net
    Total 0 (*, G) entry; 1 (S, G) entries
   
    (10.110.1.2, 226.1.1.1)
        RP: 1.1.1.1 (local)
        Protocol: pim-sm, Flag: 2MSDP ACT
        UpTime: 00:00:38
        Upstream interface: Register, Refresh time: 00:00:38
            Upstream neighbor: NULL
            RPF prime neighbor: NULL
        Downstream interface(s) information: None
   ```
   ```
   <DeviceD> display pim routing-table
   ```
   ```
    VPN-Instance: public net
    Total 1 (*, G) entry; 1 (S, G) entries
   
    (*, 226.1.1.1)
        RP: 1.1.1.1 (local)
        Protocol: pim-sm, Flag: WC
        UpTime: 00:01:25
        Upstream interface: Register, Refresh time: 00:01:25
            Upstream neighbor: NULL
            RPF prime neighbor: NULL
        Downstream interface(s) information:
        Total number of downstreams: 1
            1: GigabitEthernet0/2/0
                Protocol: igmp, UpTime: 00:01:25, Expires: -
   
    (10.110.1.2, 226.1.1.1)
        RP: 1.1.1.1 (local)
        Protocol: pim-sm, Flag: 2MSDP SWT ACT
        UpTime: 00:00:02
        Upstream interface: Register, Refresh time: 00:00:02
            Upstream neighbor: NULL
            RPF prime neighbor: NULL
        Downstream interface(s) information:
        Total number of downstreams: 1
            1: GigabitEthernet0/2/0
                Protocol: pim-sm, UpTime: 00:00:02, Expires: -
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  #
  multicast routing-enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.110.1.1 255.255.255.0
   pim sm
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 192.168.1.1 255.255.255.0
   pim sm
  #
  ospf 1
   area 0.0.0.0
    network 10.110.1.0 0.0.0.255
    network 192.168.1.0 0.0.0.255
  #
  return
  ```
* DeviceB configuration file
  
  ```
  #
  sysname DeviceB
  #
  multicast routing-enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 192.168.2.1 255.255.255.0
   pim sm
  #
  ospf 1
   area 0.0.0.0
     network 192.168.2.0 0.0.0.255
  #
  return
  ```
* DeviceC configuration file
  
  ```
  #
  sysname DeviceC
  #
  multicast routing-enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 192.168.3.1 255.255.255.0
   pim sm
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 192.168.1.2 255.255.255.0
   pim sm
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 10.110.2.1 255.255.255.0
   pim sm
   igmp enable
  #
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.255
   pim sm
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
   pim sm
  #
  ospf 1
   area 0.0.0.0
    network 192.168.1.0 0.0.0.255
    network 192.168.3.0 0.0.0.255
    network 10.110.2.0 0.0.0.255
    network 1.1.1.1 0.0.0.0
    network 2.2.2.2 0.0.0.0
  #
  pim
   c-bsr LoopBack0
   c-rp LoopBack0
   anycast-rp 1.1.1.1
    local-address 2.2.2.2
    peer 3.3.3.3
  #
  return
  ```
* DeviceD configuration file
  
  ```
  #
  sysname DeviceD
  #
  multicast routing-enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 192.168.2.2 255.255.255.0
   pim sm
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.110.3.1 255.255.255.0
   pim sm
   igmp enable
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 192.168.3.2 255.255.255.0
   pim sm
  #
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.255
   pim sm
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
   pim sm
  #
  ospf 1
   area 0.0.0.0
    network 192.168.2.0 0.0.0.255
    network 192.168.3.0 0.0.0.255
    network 10.110.3.0 0.0.0.255
    network 3.3.3.3 0.0.0.0
    network 1.1.1.1 0.0.0.0
  #
  pim
   c-bsr LoopBack0
   c-rp LoopBack0
   anycast-rp 1.1.1.1
    local-address 3.3.3.3
    peer 2.2.2.2
  #
  return
  
  ```