Example for Configuring PIM Anycast RP
======================================

Example for Configuring PIM Anycast RP

#### Networking Requirements

In scenarios where multiple multicast sources and receivers are located in a PIM-SM domain, you can configure anycast RP peer relationships so that IP routing will select the closest RP for each source and receiver. This alleviates burdens on RPs and optimizes multicast data forwarding paths.

In a traditional PIM-SM domain, each multicast group can be mapped to only one RP. When the network is overloaded or traffic congestion occurs, the following problems may occur: the RP is overburdened; route convergence is slow after the RP fails; the multicast forwarding path is not optimal. Configuring PIM anycast RP in a single AS can address these problems. IP routing will automatically select the topologically closest RP for each source and receiver. In this way, receivers can quickly receive multicast data. On the network shown in [Figure 1](#EN-US_TASK_0000001176743283__fig61819557114), Receiver2 needs to receive multicast data from Source. To do this, configure an anycast RP peer relationship between DeviceC and DeviceD so that Receiver2 can send a Join message to the closest RP, that is, DeviceD. After receiving multicast data from Source, DeviceA encapsulates the multicast data into a Register message and sends it to DeviceC. Upon receipt, DeviceC forwards it to DeviceD so that Receiver2 can receive the multicast data from Source.

![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.


**Figure 1** Networking diagram of configuring PIM anycast RP  
![](figure/en-us_image_0000001176743353.png)

To complete the configuration, you need the following data:

* Multicast group address: 226.1.1.1/24
* RP address
* Anycast RPs' local addresses

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IP address to each device interface and configure OSPF to implement IP interworking.
2. Enable the multicast function, and enable PIM-SM on related interfaces.
3. Enable IGMP on the interfaces connecting devices to hosts.
4. Configure Loopback0 interfaces on DeviceC and DeviceD as both Candidate-Rendezvous Points (C-RPs) and Candidate-BootStrap Routers (C-BSRs).
5. Configure the addresses of Loopback0 interfaces on DeviceC and DeviceD as the anycast RP address.
6. Configure the addresses of Loopback1 interfaces on DeviceC and DeviceD as their respective anycast RPs' local addresses.
7. Configure an anycast RP peer relationship between DeviceC and DeviceD.

#### Procedure

1. Assign an IP address to each device interface and configure OSPF to implement IP interworking. Enable the multicast function, and enable PIM-SM on related interfaces.
   
   
   
   # Assign an IP address and mask to each device interface in the PIM-SM domain according to [Figure 1](#EN-US_TASK_0000001176743283__fig61819557114), and configure OSPF between devices to implement IP interworking. Enable the multicast function, and enable PIM-SM on related interfaces.
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] multicast routing-enable
   [*DeviceA] interface 100GE 1/0/1
   [*DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ip address 10.110.1.1 24
   [*DeviceA-100GE1/0/1] pim sm
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100GE 1/0/2
   [*DeviceA-100GE1/0/2] undo portswitch
   [*DeviceA-100GE1/0/2] ip address 192.168.1.1 24
   [*DeviceA-100GE1/0/2] pim sm
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] ospf
   [*DeviceA-ospf-1] area 0
   [*DeviceA-ospf-1-area-0.0.0.0] network 10.110.1.0 0.0.0.255
   [*DeviceA-ospf-1-area-0.0.0.0] network 192.168.1.0 0.0.0.255
   [*DeviceA-ospf-1-area-0.0.0.0] quit
   [*DeviceA-ospf-1] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] multicast routing-enable
   [*DeviceB] interface 100GE 1/0/1
   [*DeviceB-100GE1/0/1] undo portswitch
   [*DeviceB-100GE1/0/1] ip address 192.168.2.1 24
   [*DeviceB-100GE1/0/1] pim sm
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] ospf
   [*DeviceB-ospf-1] area 0
   [*DeviceB-ospf-1-area-0.0.0.0] network 192.168.2.0 0.0.0.255
   [*DeviceB-ospf-1-area-0.0.0.0] quit
   [*DeviceB-ospf-1] quit
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceC
   [*HUAWEI] commit
   [~DeviceC] multicast routing-enable
   [*DeviceC] interface 100GE 1/0/1
   [*DeviceC-100GE1/0/1] undo portswitch
   [*DeviceC-100GE1/0/1] ip address 192.168.3.1 24
   [*DeviceC-100GE1/0/1] pim sm
   [*DeviceC-100GE1/0/1] quit
   [*DeviceC] interface 100GE 1/0/2
   [*DeviceC-100GE1/0/2] undo portswitch
   [*DeviceC-100GE1/0/2] ip address 192.168.1.2 24
   [*DeviceC-100GE1/0/2] pim sm
   [*DeviceC-100GE1/0/2] quit
   [*DeviceC] interface 100GE 1/0/3
   [*DeviceC-100GE1/0/3] undo portswitch
   [*DeviceC-100GE1/0/3] ip address 10.110.2.1 24
   [*DeviceC-100GE1/0/3] pim sm
   [*DeviceC-100GE1/0/3] quit
   [*DeviceC] interface loopback 0
   [*DeviceC-LoopBack0] ip address 1.1.1.1 32
   [*DeviceC-LoopBack0] pim sm
   [*DeviceC-LoopBack0] quit
   [*DeviceC] interface loopback 1
   [*DeviceC-LoopBack1] ip address 2.2.2.2 32
   [*DeviceC-LoopBack1] pim sm
   [*DeviceC-LoopBack1] quit
   [*DeviceC] ospf
   [*DeviceC-ospf-1] area 0
   [*DeviceC-ospf-1-area-0.0.0.0] network 192.168.3.0 0.0.0.255
   [*DeviceC-ospf-1-area-0.0.0.0] network 192.168.1.0 0.0.0.255
   [*DeviceC-ospf-1-area-0.0.0.0] network 10.110.2.0 0.0.0.255
   [*DeviceC-ospf-1-area-0.0.0.0] network 1.1.1.1 0.0.0.0
   [*DeviceC-ospf-1-area-0.0.0.0] network 2.2.2.2 0.0.0.0
   [*DeviceC-ospf-1-area-0.0.0.0] quit
   [*DeviceC-ospf-1] quit
   [*DeviceC] commit
   ```
   
   # Configure DeviceD.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceD
   [*HUAWEI] commit
   [~DeviceD] multicast routing-enable
   [*DeviceD] interface 100GE1/0/1
   [*DeviceD-100GE1/0/1] undo portswitch
   [*DeviceD-100GE1/0/1] ip address 192.168.2.2 24
   [*DeviceD-100GE1/0/1] pim sm
   [*DeviceD-100GE1/0/1] quit
   [*DeviceD] interface 100GE 1/0/2
   [*DeviceD-100GE1/0/2] undo portswitch
   [*DeviceD-100GE1/0/2] ip address 10.110.3.1 24
   [*DeviceD-100GE1/0/2] pim sm
   [*DeviceD-100GE1/0/2] quit
   [*DeviceD] interface 100GE 1/0/3
   [*DeviceD-100GE1/0/3] undo portswitch
   [*DeviceD-100GE1/0/3] ip address 192.168.3.2 24
   [*DeviceD-100GE1/0/3] pim sm
   [*DeviceD-100GE1/0/3] quit
   [*DeviceD] interface loopback 0
   [*DeviceD-LoopBack0] ip address 1.1.1.1 32
   [*DeviceD-LoopBack0] pim sm
   [*DeviceD-LoopBack0] quit
   [*DeviceD] interface loopback 1
   [*DeviceD-LoopBack1] ip address 3.3.3.3 32
   [*DeviceD-LoopBack1] pim sm
   [*DeviceD-LoopBack1] quit
   [*DeviceD] ospf
   [*DeviceD-ospf-1] area 0
   [*DeviceD-ospf-1-area-0.0.0.0] network 192.168.2.0 0.0.0.255
   [*DeviceD-ospf-1-area-0.0.0.0] network 10.110.3.0 0.0.0.255
   [*DeviceD-ospf-1-area-0.0.0.0] network 192.168.3.0 0.0.0.255
   [*DeviceD-ospf-1-area-0.0.0.0] network 1.1.1.1 0.0.0.0
   [*DeviceD-ospf-1-area-0.0.0.0] network 3.3.3.3 0.0.0.0
   [*DeviceD-ospf-1-area-0.0.0.0] quit
   [*DeviceD-ospf-1] quit
   [*DeviceD] commit
   ```
2. Enable IGMP on the interfaces connecting devices to hosts.
   
   
   
   Enable IGMP on the interfaces connecting DeviceC and DeviceD to hosts.
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] interface 100GE 1/0/3
   [~DeviceC-100GE1/0/3] igmp enable
   [*DeviceC-100GE1/0/3] quit
   [*DeviceC] commit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] interface 100GE 1/0/2
   [~DeviceD-100GE1/0/2] igmp enable
   [*DeviceD-100GE1/0/2] quit
   [*DeviceD] commit
   ```
3. Configure Loopback0 interfaces on DeviceC and DeviceD as both C-RPs and C-BSRs.
   
   
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] pim
   [*DeviceC-pim] c-bsr loopback 0
   [*DeviceC-pim] c-rp loopback 0
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] pim
   [*DeviceD-pim] c-bsr loopback 0
   [*DeviceD-pim] c-rp loopback 0
   ```
4. Configure the addresses of Loopback0 interfaces on DeviceC and DeviceD as the anycast RP address.
   
   
   
   # Configure DeviceC.
   
   ```
   [~DeviceC-pim] anycast-rp 1.1.1.1
   [*DeviceC-pim-anycast-rp-1.1.1.1] quit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD-pim] anycast-rp 1.1.1.1
   [*DeviceD-pim-anycast-rp-1.1.1.1] quit
   ```
5. Configure the addresses of Loopback1 interfaces on DeviceC and DeviceD as their respective anycast RPs' local addresses.
   
   
   
   # Configure DeviceC.
   
   ```
   [*DeviceC-pim] anycast-rp 1.1.1.1
   [*DeviceC-pim-anycast-rp-1.1.1.1] local-address 2.2.2.2
   [*DeviceC-pim-anycast-rp-1.1.1.1] quit
   ```
   
   # Configure DeviceD.
   
   ```
   [*DeviceD-pim] anycast-rp 1.1.1.1
   [*DeviceD-pim-anycast-rp-1.1.1.1] local-address 3.3.3.3
   [*DeviceD-pim-anycast-rp-1.1.1.1] quit
   ```
6. Configure an anycast RP peer relationship between DeviceC and DeviceD.
   
   
   
   # Configure DeviceC.
   
   ```
   [*DeviceC-pim] anycast-rp 1.1.1.1
   [*DeviceC-pim-anycast-rp-1.1.1.1] peer 3.3.3.3
   [*DeviceC-pim-anycast-rp-1.1.1.1] quit
   [*DeviceC-pim] quit
   [*DeviceC] commit
   ```
   
   # Configure DeviceD.
   
   ```
   [*DeviceD-pim] anycast-rp 1.1.1.1
   [*DeviceD-pim-anycast-rp-1.1.1.1] peer 2.2.2.2
   [*DeviceD-pim-anycast-rp-1.1.1.1] quit
   [*DeviceD-pim] quit
   [*DeviceD] commit
   ```

#### Verifying the Configuration

# Run the **display pim rp-info** command on DeviceC and DeviceD to check RP information.

```
<DeviceC> display pim rp-info
 VPN-Instance: public net
 PIM-SM BSR RP Number:1
 Group/MaskLen: 224.0.0.0/4
     RP: 1.1.1.1 (local)
     Priority: 0
     Uptime: 00:45:19
     Expires: 00:02:11
<DeviceD> display pim rp-info
 VPN-Instance: public net
 PIM-SM BSR RP Number:1
 Group/MaskLen: 224.0.0.0/4
     RP: 1.1.1.1 (local)
     Priority: 0
     Uptime: 02:27:56
     Expires: 00:01:39

```

The preceding command outputs show that DeviceC and DeviceD both serve as RPs and can forward Register messages from the multicast source to each other.

# Run the **display pim routing-table** command to check PIM entries on a device. Source (10.110.1.2/24) in the PIM-SM domain sends multicast data to G (226.1.1.1), and Receiver2 joins G and receives the multicast data sent to G. Source registers with DeviceC, and Receiver2 sends a Join message to DeviceD.

```
<DeviceC> display pim routing-table
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
<DeviceD> display pim routing-table
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
         1: 100GE1/0/2
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
         1: 100GE1/0/2
             Protocol: pim-sm, UpTime: 00:00:02, Expires: -
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
   ip address 10.110.1.1 255.255.255.0
   pim sm
  #
  interface 100GE1/0/2
   undo portswitch
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
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  multicast routing-enable
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.2.1 255.255.255.0
   pim sm
  #
  ospf 1
   area 0.0.0.0
     network 192.168.2.0 0.0.0.255
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
   ip address 192.168.3.1 255.255.255.0
   pim sm
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.1.2 255.255.255.0
   pim sm
  #
  interface 100GE 1/0/3
   undo portswitch
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
* DeviceD
  
  ```
  #
  sysname DeviceD
  #
  multicast routing-enable
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.2.2 255.255.255.0
   pim sm
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.110.3.1 255.255.255.0
   pim sm
   igmp enable
  #
  interface 100GE 1/0/3
   undo portswitch
   ip address 192.168.3.2 255.255.255.0
   pim sm
  #
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.255
   pim sm
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.0
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