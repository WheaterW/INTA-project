Example for Configuring IPv6 PIM Anycast RP
===========================================

Example for Configuring IPv6 PIM Anycast RP

#### Networking Requirements

In scenarios where multiple multicast sources and receivers are located in an IPv6 PIM-SM domain, you can configure anycast RP peer relationships so that multicast source registration and multicast group joining can be implemented through the closest RP. This alleviates RP burdens and optimizes multicast data forwarding paths.

In a traditional PIM-SM domain, each multicast group can be mapped to only one RP. When the network is overloaded or traffic congestion occurs, the following problems may occur: the RP is overburdened; route convergence is slow after the RP fails; the multicast forwarding path is not optimal. PIM anycast RP in a single AS allows multicast source registration and multicast group joining to be implemented through the closest RP. In this way, receivers can quickly receive multicast data. On the network shown in [Figure 1](#EN-US_TASK_0000001589525021__fig61819557114), Receiver 2 needs to receive multicast data from Source. To do this, configure an anycast RP peer relationship between DeviceC and DeviceD so that Receiver 2 can send a Join message to the closest RP (DeviceD). After receiving multicast data from Source, DeviceA encapsulates the multicast data into a Register message and sends it to DeviceC. Upon receipt, DeviceC forwards it to DeviceD so that Receiver 2 can receive the multicast data from Source.

![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


**Figure 1** Network diagram of configuring IPv6 PIM anycast RP  
![](figure/en-us_image_0000001589365349.png)

| Device | Interface | IPv6 Address  Link-local Address |
| --- | --- | --- |
| DeviceA | interface1 | 2001:db8:2::1/64  FE80::2 |
| interface2 | 2001:db8:1::1/64  FE80::1 |
| DeviceB | interface1 | 2001:db8:3::1/64  FE80::3 |
| DeviceC | interface1 | 2001:db8:4::1/64  FE80::4 |
| interface2 | 2001:db8:2::2/64  FE80::5 |
| interface3 | 2001:db8:5::1/64  FE80::6 |
| Loopback0 | 2001:db8:7::7/128  FE80::7 |
| Loopback1 | 2001:db8:8::8/128  FE80::8 |
| DeviceD | interface1 | 2001:db8:3::2/64  FE80::9 |
| interface2 | 2001:db8:6::1/64  FE80::10 |
| interface3 | 2001:db8:4::2/64  FE80::11 |
| Loopback0 | 2001:db8:7::7/128  FE80::12 |
| Loopback1 | 2001:db8:9::9/128  FE80::13 |

To complete the configuration, prepare the following data:

* Multicast group address: FF5E::6/64
* RP address
* Anycast RPs' local addresses

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IPv6 address to each device interface and configure OSPFv3 to implement IP interworking.
2. Enable the IPv6 multicast function, and enable IPv6 PIM-SM on related interfaces.
3. Enable MLD on the interfaces connecting devices to hosts.
4. Configure Loopback0 interfaces on DeviceC and DeviceD as both C-RPs and C-BSRs.
5. Configure the addresses of Loopback0 interfaces on DeviceC and DeviceD as the anycast RP address.
6. Configure the addresses of Loopback1 interfaces on DeviceC and DeviceD as the local addresses of the anycast RPs.
7. Configure an anycast RP peer relationship between DeviceC and DeviceD.

#### Procedure

1. Assign an IPv6 address to each device interface and configure OSPFv3 to implement IP interworking. Enable the multicast function, and enable IPv6 PIM-SM on related interfaces.
   
   
   
   # Assign an IPv6 address and mask to each device interface in the IPv6 PIM-SM domain according to [Figure 1](#EN-US_TASK_0000001589525021__fig61819557114), and configure OSPFv3 between devices to implement interworking. Enable the multicast function, and enable IPv6 PIM-SM on related interfaces.
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] ospfv3 1
   [*DeviceA-ospfv3-1] router-id 1.1.1.1
   [*DeviceA-ospfv3-1] area 0.0.0.0
   [*DeviceA-ospfv3-1-area-0.0.0.0] quit
   [*DeviceA-ospfv3-1] quit
   [*DeviceA] multicast ipv6 routing-enable
   [*DeviceA] interface 100GE 1/0/1
   [*DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ipv6 enable
   [*DeviceA-100GE1/0/1] ipv6 address 2001:db8:2::1/64
   [*DeviceA-100GE1/0/1] pim ipv6 sm
   [*DeviceA-100GE1/0/1] ospfv3 1 area 0.0.0.0
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100GE 1/0/2
   [*DeviceA-100GE1/0/2] undo portswitch
   [*DeviceA-100GE1/0/2] ipv6 enable
   [*DeviceA-100GE1/0/2] ipv6 address 2001:db8:1::1/64
   [*DeviceA-100GE1/0/2] pim ipv6 sm
   [*DeviceA-100GE1/0/2] ospfv3 1 area 0.0.0.0
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] ospfv3 1
   [*DeviceB-ospfv3-1] router-id 2.2.2.2
   [*DeviceB-ospfv3-1] area 0.0.0.0
   [*DeviceB-ospfv3-1-area-0.0.0.0] quit
   [*DeviceB-ospfv3-1] quit
   [*DeviceB] multicast ipv6 routing-enable
   [*DeviceB] interface 100GE 1/0/1
   [*DeviceB-100GE1/0/1] undo portswitch
   [*DeviceB-100GE1/0/1] ipv6 enable
   [*DeviceB-100GE1/0/1] ipv6 address 2001:db8:3::1/64
   [*DeviceB-100GE1/0/1] pim ipv6 sm
   [*DeviceB-100GE1/0/1] ospfv3 1 area 0.0.0.0
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceC
   [*HUAWEI] commit
   [~DeviceC] ospfv3 1
   [*DeviceC-ospfv3-1] router-id 3.3.3.3
   [*DeviceC-ospfv3-1] area 0.0.0.0
   [*DeviceC-ospfv3-1-area-0.0.0.0] quit
   [*DeviceC-ospfv3-1] quit
   [*DeviceC] multicast ipv6 routing-enable
   [*DeviceC] interface 100GE 1/0/1
   [*DeviceC-100GE1/0/1] undo portswitch
   [*DeviceC-100GE1/0/1] ipv6 enable
   [*DeviceC-100GE1/0/1] ipv6 address 2001:db8:4::1/64
   [*DeviceC-100GE1/0/1] pim ipv6 sm
   [*DeviceC-100GE1/0/1] ospfv3 1 area 0.0.0.0
   [*DeviceC-100GE1/0/1] quit
   [*DeviceC] interface 100GE 1/0/2
   [*DeviceC-100GE1/0/2] undo portswitch
   [*DeviceC-100GE1/0/2] ipv6 enable
   [*DeviceC-100GE1/0/2] ipv6 address 2001:db8:2::2/64
   [*DeviceC-100GE1/0/2] pim ipv6 sm
   [*DeviceC-100GE1/0/2] ospfv3 1 area 0.0.0.0
   [*DeviceC-100GE1/0/2] quit
   [*DeviceC] interface 100GE 1/0/3
   [*DeviceC-100GE1/0/3] undo portswitch
   [*DeviceC-100GE1/0/3] ipv6 enable
   [*DeviceC-100GE1/0/3] ipv6 address 2001:db8:5::1/64
   [*DeviceC-100GE1/0/3] pim ipv6 sm
   [*DeviceC-100GE1/0/3] ospfv3 1 area 0.0.0.0
   [*DeviceC-100GE1/0/3] quit
   [*DeviceC] interface loopback 0
   [*DeviceC-LoopBack0] ipv6 enable
   [*DeviceC-LoopBack0] ipv6 address 2001:db8:7::7/128
   [*DeviceC-LoopBack0] pim ipv6 sm
   [*DeviceC-LoopBack0] ospfv3 1 area 0.0.0.0
   [*DeviceC-LoopBack0] quit
   [*DeviceC] interface loopback 1
   [*DeviceC-LoopBack1] ipv6 enable
   [*DeviceC-LoopBack1] ipv6 address 2001:db8:8::8/128
   [*DeviceC-LoopBack1] pim ipv6 sm
   [*DeviceC-LoopBack1] ospfv3 1 area 0.0.0.0
   [*DeviceC-LoopBack1] quit
   [*DeviceC] commit
   ```
   
   # Configure DeviceD.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceD
   [*HUAWEI] commit
   [~DeviceD] ospfv3 1
   [*DeviceD-ospfv3-1] router-id 4.4.4.4
   [*DeviceD-ospfv3-1] area 0.0.0.0
   [*DeviceD-ospfv3-1-area-0.0.0.0] quit
   [*DeviceD-ospfv3-1] quit
   [*DeviceD] multicast ipv6 routing-enable
   [*DeviceD] interface 100GE1/0/1
   [*DeviceD-100GE1/0/1] undo portswitch
   [*DeviceD-100GE1/0/1] ipv6 enable
   [*DeviceD-100GE1/0/1] ipv6 address 2001:db8:3::2/64
   [*DeviceD-100GE1/0/1] pim ipv6 sm
   [*DeviceD-100GE1/0/1] ospfv3 1 area 0.0.0.0
   [*DeviceD-100GE1/0/1] quit
   [*DeviceD] interface 100GE 1/0/2
   [*DeviceD-100GE1/0/2] undo portswitch
   [*DeviceD-100GE1/0/2] ipv6 enable
   [*DeviceD-100GE1/0/2] ipv6 address 2001:db8:6::1/64
   [*DeviceD-100GE1/0/2] pim ipv6 sm
   [*DeviceD-100GE1/0/2] ospfv3 1 area 0.0.0.0
   [*DeviceD-100GE1/0/2] quit
   [*DeviceD] interface 100GE 1/0/3
   [*DeviceD-100GE1/0/3] undo portswitch
   [*DeviceD-100GE1/0/3] ipv6 enable
   [*DeviceD-100GE1/0/3] ipv6 address 2001:db8:4::2/64
   [*DeviceD-100GE1/0/3] pim ipv6 sm
   [*DeviceD-100GE1/0/3] ospfv3 1 area 0.0.0.0
   [*DeviceD-100GE1/0/3] quit
   [*DeviceD] interface loopback 0
   [*DeviceD-LoopBack0] ipv6 enable
   [*DeviceD-LoopBack0] ipv6 address 2001:db8:7::7/128
   [*DeviceD-LoopBack0] pim ipv6 sm
   [*DeviceD-LoopBack0] ospfv3 1 area 0.0.0.0
   [*DeviceD-LoopBack0] quit
   [*DeviceD] interface loopback 1
   [*DeviceD-LoopBack1] ipv6 enable
   [*DeviceD-LoopBack1] ipv6 address 2001:db8:9::9/128
   [*DeviceD-LoopBack1] pim ipv6 sm
   [*DeviceD-LoopBack1] ospfv3 1 area 0.0.0.0
   [*DeviceD-LoopBack1] quit
   [*DeviceD] commit
   ```
2. Enable MLD on the interfaces connecting devices to hosts.
   
   
   
   # Enable MLD on the interfaces connecting DeviceC and DeviceD to hosts.
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] interface 100GE 1/0/3
   [*DeviceC-100GE1/0/3] mld enable
   [*DeviceC-100GE1/0/3] quit
   [*DeviceC] commit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] interface 100GE 1/0/2
   [*DeviceD-100GE1/0/2] mld enable
   [*DeviceD-100GE1/0/2] quit
   [*DeviceD] commit
   ```
3. Configure Loopback0 interfaces on DeviceC and DeviceD as both C-RPs and C-BSRs.
   
   
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] pim ipv6
   [*DeviceC-pim6] c-bsr 2001:db8:7::7
   [*DeviceC-pim6] c-rp 2001:db8:8::8
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] pim ipv6
   [*DeviceD-pim6] c-bsr 2001:db8:7::7
   [*DeviceD-pim6] c-rp 2001:db8:9::9
   ```
4. Configure the addresses of Loopback0 interfaces on DeviceC and DeviceD as the anycast RP address.
   
   
   
   # Configure DeviceC.
   
   ```
   [*DeviceC-pim6] anycast-rp 2001:db8:7::7
   [*DeviceC-pim6-anycast-rp-2001:db8:7::7] quit
   ```
   
   # Configure DeviceD.
   
   ```
   [*DeviceD-pim] anycast-rp 2001:db8:7::7
   [*DeviceD-pim6-anycast-rp-2001:db8:7::7] quit
   ```
5. Configure the addresses of Loopback1 interfaces on DeviceC and DeviceD as the local addresses of the anycast RPs.
   
   
   
   # Configure DeviceC.
   
   ```
   [*DeviceC-pim6] anycast-rp 2001:db8:7::7
   [*DeviceC-pim6-anycast-rp-2001:db8:7::7] local-address 2001:db8:8::8
   [*DeviceC-pim6-anycast-rp-2001:db8:7::7] quit
   ```
   
   # Configure DeviceD.
   
   ```
   [*DeviceD-pim6] anycast-rp 2001:db8:7::7
   [*DeviceD-pim6-anycast-rp-2001:db8:7::7] local-address 2001:db8:9::9
   [*DeviceD-pim6-anycast-rp-2001:db8:7::7] quit
   ```
6. Configure an anycast RP peer relationship between DeviceC and DeviceD.
   
   
   
   # Configure DeviceC.
   
   ```
   [*DeviceC-pim6] anycast-rp 2001:db8:7::7
   [*DeviceC-pim6-anycast-rp-2001:db8:7::7] peer 2001:db8:9::9
   [*DeviceC-pim6-anycast-rp-2001:db8:7::7] quit
   [*DeviceC-pim6] quit
   [*DeviceC] commit
   ```
   
   # Configure DeviceD.
   
   ```
   [*DeviceD-pim6] anycast-rp 2001:db8:7::7
   [*DeviceD-pim6-anycast-rp-2001:db8:7::7] peer 2001:db8:8::8
   [*DeviceD-pim6-anycast-rp-2001:db8:7::7] quit
   [*DeviceD-pim6] quit
   [*DeviceD] commit
   ```

#### Verifying the Configuration

# Run the **display pim ipv6 rp-info** command on DeviceC and DeviceD to check RP information.

```
<DeviceC> display pim ipv6 rp-info
 VPN-Instance: public net
 PIM-SM BSR RP Number:1
 Group/MaskLen: FF00::/8
     RP: 2001:DB8:7::7 (local)
     Priority: 192
     Uptime: 00:45:19
     Expires: 00:02:11
<DeviceD> display pim ipv6 rp-info
 VPN-Instance: public net
 PIM-SM BSR RP Number:1
 Group/MaskLen: FF00::/8
     RP: 2001:DB8:7::7 (local)
     Priority: 192
     Uptime: 02:27:56
     Expires: 00:01:39
```

The preceding command outputs show that DeviceC and DeviceD both serve as RPs and can forward Register messages from the multicast source to each other.

# Run the **display pim ipv6 routing-table** command on the devices to check PIM entries. Source (2001:db8:1::2/64) in the PIM-SM domain sends multicast data to multicast group G (ff5e::6). Receiver 2 joins G and receives the multicast data sent to G. Source is registered with DeviceC, and Receiver 2 sends a Join message to DeviceD.

```
<DeviceC> display pim ipv6 routing-table
 VPN-Instance: public net
 Total 0 (*, G) entry; 1 (S, G) entries

 (2001:DB8:1::2, FF5E::6)
     RP: 2001:DB8:7::7 (local)
     Protocol: pim-sm, Flag: SPT ACT
     UpTime: 00:00:38
     Upstream interface: Register, Refresh time: 00:00:38
         Upstream neighbor: NULL
         RPF prime neighbor: NULL
     Downstream interface(s) information: None
<DeviceD> display pim ipv6 routing-table
 VPN-Instance: public net
 Total 1 (*, G) entry; 1 (S, G) entries

 (*, FF5E::6)
     RP: 2001:DB8:7::7 (local)
     Protocol: pim-sm, Flag: WC
     UpTime: 00:01:25
     Upstream interface: Register, Refresh time: 00:01:25
         Upstream neighbor: NULL
         RPF prime neighbor: NULL
     Downstream interface(s) information:
     Total number of downstreams: 1
         1: 100GE1/0/2
             Protocol: mld, UpTime: 00:01:25, Expires: -

 (2001:DB8:1::2, FF5E::6)
     RP: 2001:DB8:7::7 (local)
     Protocol: pim-sm, Flag: SWT ACT
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
  multicast ipv6 routing-enable
  #
  ospfv3 1
   router-id 1.1.1.1
   area 0.0.0.0
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:2::1/64
   pim ipv6 sm
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1::1/64
   pim ipv6 sm
   ospfv3 1 area 0.0.0.0
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  multicast ipv6 routing-enable
  #
  ospfv3 1
   router-id 2.2.2.2
   area 0.0.0.0
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:3::1/64
   pim ipv6 sm
   ospfv3 1 area 0.0.0.0
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  multicast ipv6 routing-enable
  #
  ospfv3 1
   router-id 3.3.3.3
   area 0.0.0.0
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:4::1/64
   pim ipv6 sm
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:2::2/64
   pim ipv6 sm
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE 1/0/3
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:5::1/64
   pim ipv6 sm
   mld enable
   ospfv3 1 area 0.0.0.0
  #
  interface LoopBack0
   ipv6 enable
   ipv6 address 2001:db8:7::7/128
   pim ipv6 sm
   ospfv3 1 area 0.0.0.0
  #
  interface LoopBack1
   ipv6 enable
   ipv6 address 2001:db8:8::8/128
   pim ipv6 sm
   ospfv3 1 area 0.0.0.0
  #
  pim ipv6
   c-bsr 2001:db8:7::7
   c-rp 2001:db8:8::8
   anycast-rp 2001:db8:7::7
    local-address 2001:db8:8::8
    peer 2001:db8:9::9
  #
  return
  ```
* DeviceD
  
  ```
  #
  sysname DeviceD
  #
  multicast ipv6 routing-enable
  #
  ospfv3 1
   router-id 4.4.4.4
   area 0.0.0.0
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:3::2/64
   pim ipv6 sm
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:6::1/64
   pim ipv6 sm
   mld enable
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE 1/0/3
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:4::2/64
   pim ipv6 sm
   ospfv3 1 area 0.0.0.0
  #
  interface LoopBack0
   ipv6 enable
   ipv6 address 2001:db8:7::7/128
   pim ipv6 sm
   ospfv3 1 area 0.0.0.0
  #
  interface LoopBack1
   ipv6 enable
   ipv6 address 2001:db8:9::9/128
   pim ipv6 sm
   ospfv3 1 area 0.0.0.0
  #
  pim ipv6
   c-bsr 2001:db8:7::7
   c-rp 2001:db8:9::9
   anycast-rp 2001:db8:7::7
    local-address 2001:db8:9::9
    peer 2001:db8:8::8
  #
  return
  ```