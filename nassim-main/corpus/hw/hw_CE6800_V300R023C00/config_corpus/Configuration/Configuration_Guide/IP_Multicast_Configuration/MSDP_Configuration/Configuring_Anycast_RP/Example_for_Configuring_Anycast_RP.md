Example for Configuring Anycast RP
==================================

Example for Configuring Anycast RP

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001130783710__fig_dc_vrp_multicast_cfg_007301), the PIM-SM domain has multiple multicast sources and receivers. MSDP peer relationships must be set up in the PIM-SM domain to implement RP load balancing.

**Figure 1** Network diagram of configuring PIM-SM inter-domain multicast![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.


  
![](figure/en-us_image_0000001176743389.png "Click to enlarge")

#### Configuration Roadmap

Configure MSDP-based anycast RP to allow receivers to send Join messages to the closest RP and multicast sources to register with the closest RP, thereby implementing RP load balancing.

1. Enable the multicast function and configure interface IP addresses on devices, and configure OSPF in each PIM-SM domain for intra-domain interconnection.
2. Enable PIM-SM on each involved interface and enable IGMP on interfaces connected to hosts.
3. Configure the same address for Loopback10 interfaces on DeviceB and DeviceC, and configure them as C-RPs. Configure Loopback1 interfaces as C-BSRs.
4. Configure MSDP peers on Loopback0 interfaces of DeviceB and DeviceC. According to the RPF rule, SA messages sent by the source RP are accepted.

#### Procedure

1. Enable the multicast function, configure interface IP addresses and masks and loopback interfaces in each PIM-SM domain, and configure OSPF for interworking.
   
   
   
   # Configure DeviceB. The same Loopback10 interface address must be configured on DeviceB and DeviceC. The configurations of other devices are similar to the configuration of DeviceB. For detailed configurations, see Configuration Scripts.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] multicast routing-enable
   [*DeviceB] interface 100ge 1/0/1
   [*DeviceB-100GE1/0/1] undo portswitch
   [*DeviceB-100GE1/0/1] ip address 192.168.1.1 24
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] interface 100ge 1/0/2
   [*DeviceB-100GE1/0/2] undo portswitch
   [*DeviceB-100GE1/0/2] ip address 10.110.1.1 24
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] interface 100ge 1/0/3
   [*DeviceB-100GE1/0/3] undo portswitch
   [*DeviceB-100GE1/0/3] ip address 10.110.4.1 24
   [*DeviceB-100GE1/0/3] quit
   [~DeviceB] interface loopback 0
   [*DeviceB-LoopBack0] ip address 10.5.5.5 255.255.255.255
   [*DeviceB-LoopBack0] quit
   [~DeviceB] interface loopback 10
   [*DeviceB-LoopBack10] ip address 10.1.1.1 255.255.255.255
   [*DeviceB-LoopBack10] quit
   [~DeviceB] interface loopback 1
   [*DeviceB-LoopBack1] ip address 10.3.3.3 255.255.255.255
   [*DeviceB-LoopBack1] quit
   [*DeviceB] ospf 1
   [*DeviceB-ospf-1] area 0.0.0.0
   [*DeviceB-ospf-1-area-0.0.0.0] network 10.5.5.5 0.0.0.0
   [*DeviceB-ospf-1-area-0.0.0.0] network 10.3.3.3 0.0.0.0
   [*DeviceB-ospf-1-area-0.0.0.0] network 10.1.1.1 0.0.0.0
   [*DeviceB-ospf-1-area-0.0.0.0] network 10.110.1.0 0.0.0.255
   [*DeviceB-ospf-1-area-0.0.0.0] network 10.110.4.0 0.0.0.255
   [*DeviceB-ospf-1-area-0.0.0.0] network 192.168.1.0 0.0.0.255
   [*DeviceB-ospf-1-area-0.0.0.0] quit
   [*DeviceB-ospf-1] quit
   [*DeviceB] commit
   ```
2. Configure PIM-SM.
   
   
   
   # Enable PIM-SM on all involved interfaces, and enable IGMP on interfaces connected to hosts. The configurations of other devices are similar to the configuration of DeviceB. For detailed configurations, see Configuration Scripts.
   
   ```
   [~DeviceB] interface 100ge 1/0/3
   [*DeviceB-100GE1/0/3] pim sm
   [*DeviceB-100GE1/0/8] igmp enable
   [*DeviceB-100GE1/0/3] quit
   [*DeviceB] interface 100ge 1/0/2
   [*DeviceB-100GE1/0/2] pim sm
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] interface 100ge 1/0/1
   [*DeviceB-100GE1/0/1] pim sm
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] commit
   ```
3. Configure Loopback1 and Loopback10 interfaces as C-BSRs and C-RPs, respectively.
   
   
   
   # On DeviceB and DeviceC, configure Loopback1 interfaces as C-BSRs, and configure Loopback10 interfaces as C-RPs. The configuration of DeviceC is similar to the configuration of DeviceB. For detailed configuration, see Configuration Scripts.
   
   ```
   [~DeviceB] interface loopback 1
   [*DeviceB-LoopBack1] pim sm
   [*DeviceB-LoopBack1] quit
   [*DeviceB] interface loopback 10
   [*DeviceB-LoopBack10] pim sm
   [*DeviceB-LoopBack10] quit
   [*DeviceB] pim
   [*DeviceB-pim] c-bsr loopback 1
   [*DeviceB-pim] c-rp loopback 10
   [*DeviceB-pim] quit
   [*DeviceB] commit
   ```
4. Configure Loopback0 interfaces and MSDP peers.
   
   
   
   # Configure an MSDP peer on Loopback0 of DeviceB.
   
   ```
   [~DeviceB] interface loopback 0
   [*DeviceB-LoopBack0] pim sm
   [*DeviceB-LoopBack0] quit
   [*DeviceB] msdp
   [*DeviceB-msdp] originating-rp loopback0
   [*DeviceB-msdp] peer 10.2.2.2 connect-interface loopback0
   [*DeviceB-msdp] quit
   [*DeviceB] commit
   ```
   
   # Configure an MSDP peer on Loopback0 of DeviceC.
   
   ```
   [~DeviceC] interface loopback 0
   [*DeviceC-LoopBack0] ip address 10.2.2.2 255.255.255.255
   [*DeviceC-LoopBack0] pim sm
   [*DeviceC-LoopBack0] quit
   [*DeviceC] msdp
   [*DeviceC-msdp] originating-rp loopback0
   [*DeviceC-msdp] peer 10.5.5.5 connect-interface loopback0
   [*DeviceC-msdp] quit
   [*DeviceC] commit
   ```

#### Verifying the Configuration

# Run the **display msdp brief** command to check MSDP peer relationships established between devices. The following example uses the command output on DeviceB and DeviceC.
```
[~DeviceB] display msdp brief
MSDP Peer Brief Information of VPN instance: public net  
---------------------------------------------------------------------------------                                                   
  Configured   Up           Listen       Connect      Shutdown     Down                                                             
           1    1                0             0             0        0                                                             
---------------------------------------------------------------------------------                                                   
  Peer's Address     State     Up/Down time    AS          SA Count   Reset Count                                                   
  10.2.2.2               Up     00:10:17        ?(unknown)         0             0    

[~DeviceC] display msdp brief
MSDP Peer Brief Information of VPN instance: public net  
---------------------------------------------------------------------------------                                                   
  Configured   Up           Listen       Connect      Shutdown     Down                                                             
           1    1                0             0             0        0                                                             
---------------------------------------------------------------------------------                                                   
  Peer's Address     State     Up/Down time    AS          SA Count   Reset Count                                                   
  10.5.5.5               Up     00:10:18        ?(unknown)         0             0           
```

# Run the **display pim routing-table** command to check the PIM routing table on DeviceB and DeviceC. S1 (10.110.5.100/24) in the PIM-SM domain sends multicast data to multicast group G (225.1.1.1), and User1 joins G and receives the multicast data sent to G. The PIM routes displayed on DeviceB and DeviceC show that DeviceB is the valid RP: S1 registers with DeviceB, and User1 sends Join messages to DeviceB.

```
[~DeviceB] display pim routing-table
VPN-Instance: public net
 Total 1 (*, G) entry; 1 (S, G) entry
 
 (*, 225.1.1.1)
     RP: 10.1.1.1 (local)
     Protocol: pim-sm, Flag: WC
     UpTime: 00:08:49
     Upstream interface: Register, Refresh time: 00:28:49
         Upstream neighbor: NULL
         RPF prime neighbor: NULL
     Downstream interface(s) information:
     Total number of downstreams: 1
         1: 100GE1/0/3
             Protocol: igmp, UpTime: 00:08:49, Expires: -
 
 (10.110.5.1, 225.1.1.1)
     RP: 10.1.1.1 (local)
     Protocol: pim-sm, Flag: SPT 2MSDP ACT
     UpTime: 00:07:26
     Upstream interface: 100GE1/0/2, Refresh time: 00:28:49
         Upstream neighbor: 10.110.1.2
         RPF prime neighbor: 10.110.1.2
     Downstream interface(s) information:
     Total number of downstreams: 1
         1: 100GE1/0/3
             Protocol: pim-sm, UpTime: 00:07:26, Expires: -
```
```
[~DeviceC] display pim routing-table
```

No information is output.

# User1 leaves G, and S1 stops sending multicast data to G. Run the **reset pim routing-table** command in the user view to clear PIM routing entries on DeviceB.

```
<DeviceB> reset pim routing-table group 225.1.1.1 mask 255.255.255.255 source 10.110.5.100 interface 100GE 1/0/3 
```

# User2 joins G, and S2 (10.110.6.100/24) begins to send multicast data to G. The PIM routes displayed on DeviceB and DeviceC show that DeviceC is the valid RP: S2 registers with DeviceC, and User2 sends Join messages to DeviceC.

```
[~DeviceB] display pim routing-table
```

No information is output.

```
[~DeviceC] display pim routing-table
VPN-Instance: public net  
Total 1 (*, G) entry; 1 (S, G) entry
 
(*, 225.1.1.1)
     RP: 10.1.1.1 (local)
     Protocol: pim-sm, Flag: WC
     UpTime: 00:07:23
     Upstream interface: Register, Refresh time: 00:07:23
         Upstream neighbor: NULL
         RPF prime neighbor: NULL
     Downstream interface(s) information:
     Total number of downstreams: 1
         1: 100GE1/0/3,
             Protocol: igmp, UpTime: 00:07:23, Expires:-

 (10.110.6.100, 225.1.1.1)
     RP: 10.1.1.1 (local)
     Protocol: pim-sm, Flag: SPT 2MSDP ACT
     UpTime: 00:05:20
     Upstream interface: 100GE1/0/2
         Upstream neighbor: 10.110.2.2
         RPF prime neighbor: 10.110.2.2
     Downstream interface(s) information:
     Total number of downstreams: 1
         1: 100GE1/0/3
             Protocol: pim-sm, UpTime: 00:05:20, Expires: -
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
   ip address 10.110.5.1 255.255.255.0
   pim sm
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.110.1.2 255.255.255.0
   pim sm
  #
  ospf 1
   area 0.0.0.0
    network 10.110.1.0 0.0.0.255
    network 10.110.5.0 0.0.0.255
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
   ip address 192.168.1.1 255.255.255.0
   pim sm
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.110.1.1 255.255.255.0
   pim sm
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 10.110.4.1 255.255.255.0
   pim sm
   igmp enable
  #
  interface LoopBack0
   ip address 10.5.5.5 255.255.255.255
   pim sm
  #
  interface LoopBack1
   ip address 10.3.3.3 255.255.255.255
   pim sm
  #
  interface LoopBack10
   ip address 10.1.1.1 255.255.255.255
   pim sm
  #
  ospf 1
   area 0.0.0.0
    network 10.5.5.5 0.0.0.0
    network 10.3.3.3 0.0.0.0
    network 10.1.1.1 0.0.0.0
    network 10.110.1.0 0.0.0.255
    network 10.110.4.0 0.0.0.255
    network 192.168.1.0 0.0.0.255
  #
  pim
   c-bsr LoopBack1
   c-rp LoopBack10
  #
  msdp
   originating-rp LoopBack0
   peer 10.2.2.2 connect-interface LoopBack0
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
  interface 100GE1/0/2
   undo portswitch
   ip address 10.110.2.1 255.255.255.0
   pim sm
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 10.110.3.1 255.255.255.0
   pim sm
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.3.1 255.255.255.0
   pim sm
   igmp enable
  #
  interface LoopBack0
   ip address 10.2.2.2 255.255.255.255
   pim sm
  #
  interface LoopBack1
   ip address 10.4.4.4 255.255.255.255
   pim sm
  #
  interface LoopBack10
   ip address 10.1.1.1 255.255.255.255
   pim sm
  #
  ospf 1
   area 0.0.0.0
    network 10.2.2.2 0.0.0.0
    network 10.4.4.4 0.0.0.0
    network 10.1.1.1 0.0.0.0
    network 10.110.2.0 0.0.0.255
    network 10.110.3.0 0.0.0.255
    network 192.168.3.0 0.0.0.255
  #
  pim
   c-bsr LoopBack1
   c-rp LoopBack10
  #
  msdp
   originating-rp LoopBack0
   peer 10.5.5.5 connect-interface LoopBack0
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
   ip address 192.168.1.2 255.255.255.0
   pim sm
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.3.2 255.255.255.0
   pim sm
  #
  ospf 1
   area 0.0.0.0
    network 192.168.1.0 0.0.0.255
    network 192.168.3.0 0.0.0.255
  #
  return
  ```
* DeviceE
  
  ```
  #
  sysname DeviceE
  #
  multicast routing-enable
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.110.2.2 255.255.255.0
   pim sm
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.110.6.1 255.255.255.0
   pim sm
  #
  ospf 1
   area 0.0.0.0
    network 10.110.2.0 0.0.0.255
    network 10.110.6.0 0.0.0.255
  #
  return
  ```