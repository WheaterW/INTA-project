Example for Configuring an IPv6 MCE
===================================

Example for Configuring an IPv6 MCE

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001176741111__fig_dc_vrp_mpls-l3vpn-v4_cfg_012201), site 1 and site 2 both connect to PE1, but the two sites need to be isolated from each other and use independent address spaces. To meet the preceding requirements and reduce costs, use the MCE solution.

**Figure 1** Network diagram for IPv6 MCE![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, interface 3, and interface 4 represent 100GE 1/0/1, 100GE 1/0/2, 100GE 1/0/3, and 100GE 1/0/4, respectively.


  
![](figure/en-us_image_0000001130781518.png "Click to enlarge")

#### Precautions

During the configuration, note the following:

* The MCE must have multiple VPN instances configured and have a different interface bound to each VPN instance.
* Routing loop detection must be disabled on the MCE, so that the MCE can exchange routing information with PEs through OSPFv3 multi-instance.
* RIPng must be configured on the MCE to import VPN routes from sites 1 and 2.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure VPN instances on the MCE and PE1 and bind interfaces to the VPN instances.
2. Configure OSPFv3 multi-instance on the MCE and PE1 to exchange VPN routing information.
3. Configure RIPng on the MCE, DeviceA, and DeviceB to exchange VPN routing information.
4. Disable routing loop detection on the MCE, and import RIPng routes destined for VPN sites.

#### Procedure

1. Configure VPN instances on the MCE and PE1 and bind interfaces to the VPN instances.
   
   
   
   # Configure PE1.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname PE1
   [*HUAWEI] commit
   [~PE1] ip vpn-instance vpna
   [*PE1-vpn-instance-vpna] ipv6-family
   [*PE1-vpn-instance-vpna-af-ipv6] route-distinguisher 200:1
   [*PE1-vpn-instance-vpna-af-ipv6] vpn-target 111:1 both
   [*PE1-vpn-instance-vpna-af-ipv6] quit
   [*PE1-vpn-instance-vpna] quit
   [*PE1] ip vpn-instance vpnb
   [*PE1-vpn-instance-vpnb] ipv6-family
   [*PE1-vpn-instance-vpnb-af-ipv6] route-distinguisher 200:2
   [*PE1-vpn-instance-vpnb-af-ipv6] vpn-target 222:2 both
   [*PE1-vpn-instance-vpnb-af-ipv6] quit
   [*PE1-vpn-instance-vpnb] quit
   [*PE1] interface 100GE1/0/1
   [*PE1-100GE1/0/1] undo portswitch
   [*PE1-100GE1/0/1] ip binding vpn-instance vpna
   [*PE1-100GE1/0/1] ipv6 enable
   [*PE1-100GE1/0/1] ipv6 address 2001:DB8:8::1 64
   [*PE1-100GE1/0/1] quit
   [*PE1]interface 100GE1/0/2
   [*PE1-100GE1/0/2] undo portswitch
   [*PE1-100GE1/0/2] ip binding vpn-instance vpnb
   [*PE1-100GE1/0/2] ipv6 enable
   [*PE1-100GE1/0/2] ipv6 address 2001:DB8:9::1 64
   [*PE1-100GE1/0/2] quit
   [*PE1] commit
   ```
   
   # Configure the MCE.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname MCE
   [*HUAWEI] commit
   [~MCE] ip vpn-instance vpna
   [*MCE-vpn-instance-vpna] ipv6-family
   [*MCE-vpn-instance-vpna-af-ipv6] route-distinguisher 100:1
   [*MCE-vpn-instance-vpna-af-ipv6] quit
   [*MCE-vpn-instance-vpna] quit
   [*MCE] ip vpn-instance vpnb
   [*MCE-vpn-instance-vpnb] ipv6-family
   [*MCE-vpn-instance-vpnb-af-ipv6] route-distinguisher 100:2
   [*MCE-vpn-instance-vpnb-af-ipv6] quit
   [*MCE-vpn-instance-vpnb] quit
   [*MCE] interface 100GE1/0/1
   [*MCE-100GE1/0/1] undo portswitch
   [*MCE-100GE1/0/1] ipv6 enable
   [*MCE-100GE1/0/1] ip binding vpn-instance vpna
   [*MCE-100GE1/0/1] ipv6 address 2001:DB8:8::2 64
   [*MCE-100GE1/0/1] quit
   [*MCE] interface 100GE1/0/2
   [*MCE-100GE1/0/2] undo portswitch
   [*MCE-100GE1/0/2] ipv6 enable
   [*MCE-100GE1/0/2] ip binding vpn-instance vpnb
   [*MCE-100GE1/0/2] ipv6 address 2001:DB8:9::2 64
   [*MCE-100GE1/0/2] quit
   [*MCE] interface 100GE1/0/3
   [*MCE-100GE1/0/3] undo portswitch
   [*MCE-100GE1/0/3] ipv6 enable
   [*MCE-100GE1/0/3] ip binding vpn-instance vpna
   [*MCE-100GE1/0/3] ipv6 address 2001:DB8:3::2 64
   [*MCE-100GE1/0/3] quit
   [*MCE] interface 100GE1/0/4
   [*MCE-100GE1/0/4] undo portswitch
   [*MCE-100GE1/0/4] ipv6 enable
   [*MCE-100GE1/0/4] ip binding vpn-instance vpnb
   [*MCE-100GE1/0/4] ipv6 address 2001:DB8:4::2 64
   [*MCE-100GE1/0/4] quit
   [*MCE] commit
   ```
2. Configure OSPFv3 multi-instance on PE1 and the MCE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] ospfv3 100 vpn-instance vpna
   [*PE1-ospfv3-100] router-id 10.5.5.5
   [*PE1-ospfv3-100] quit
   [*PE1] interface 100GE1/0/1
   [*PE1-100GE1/0/1] ospfv3 100 area 1 instance 1
   [*PE1-100GE1/0/1] quit
   [*PE1] ospfv3 200 vpn-instance vpnb
   [*PE1-ospfv3-200] router-id 10.6.6.6
   [*PE1-ospfv3-200] quit 
   [*PE1] interface 100GE1/0/2
   [*PE1-100GE1/0/2] ospfv3 200 area 2 instance 2
   [*PE1-100GE1/0/2] quit
   [*PE1] commit
   ```
   
   # Configure the MCE.
   
   ```
   [~MCE] ospfv3 100 vpn-instance vpna
   [*MCE-ospfv3-100] router-id 10.7.7.7
   [*MCE-ospfv3-100] quit
   [*MCE] interface 100GE1/0/1
   [*MCE-100GE1/0/1] ospfv3 100 area 1 instance 1
   [*MCE-100GE1/0/1] quit
   [*MCE] ospfv3 200 vpn-instance vpnb
   [*MCE-ospfv3-200] router-id 10.8.8.8
   [*MCE-ospfv3-200] quit
   [*MCE] interface 100GE1/0/2
   [*MCE-100GE1/0/2] ospfv3 200 area 2 instance 2
   [*MCE-100GE1/0/2] quit
   [*MCE] commit
   ```
3. Configure RIPng on the MCE to import VPN routes from sites 1 and 2.
   
   
   
   # Configure the MCE.
   
   ```
   [~MCE] ripng 100 vpn-instance vpna
   [*MCE-ripng-100] import-route ospfv3 100
   [*MCE-ripng-100] quit
   [*MCE] interface 100GE1/0/3
   [*MCE-100GE1/0/3] ripng 100 enable
   [*MCE-100GE1/0/3] quit
   [*MCE] ripng 200 vpn-instance vpnb
   [*MCE-ripng-200] import-route ospfv3 200
   [*MCE-ripng-200] quit
   [*MCE] interface 100GE1/0/4
   [*MCE-100GE1/0/4] ripng 200 enable
   [*MCE-100GE1/0/4] quit
   [*MCE] commit
   ```
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface 100GE1/0/1
   [*DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ipv6 enable
   [*DeviceA-100GE1/0/1] ipv6 address 2001:DB8:3::1 64
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface Loopback 1
   [*DeviceA-Loopback1] ipv6 enable
   [*DeviceA-Loopback1] ipv6 address 2001:DB8:13::3 128
   [*DeviceA-Loopback1] quit
   [*DeviceA] ripng 100
   [*DeviceA-ripng-100] quit
   [*DeviceA] interface 100GE1/0/1
   [*DeviceA-100GE1/0/1] ripng 100 enable
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface Loopback 1
   [*DeviceA-Loopback1] ripng 100 enable
   [*DeviceA-Loopback1] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] interface 100GE1/0/1
   [*DeviceB-100GE1/0/1] undo portswitch
   [*DeviceB-100GE1/0/1] ipv6 enable
   [*DeviceB-100GE1/0/1] ipv6 address 2001:DB8:4::1 64
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] interface Loopback 1
   [*DeviceB-Loopback1] ipv6 enable
   [*DeviceB-Loopback1] ipv6 address 2001:DB8:14::4 128
   [*DeviceB-Loopback1] quit
   [*DeviceB] ripng 200
   [*DeviceB-ripng-200] quit
   [*DeviceB] interface 100GE1/0/1
   [*DeviceB-100GE1/0/1] ripng 200 enable
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] interface Loopback 1
   [*DeviceB-Loopback1] ripng 200 enable
   [*DeviceB-Loopback1] quit
   [*DeviceB] commit
   ```
4. Disable routing loop detection on the MCE and import RIP routes destined for VPN sites.
   
   
   ```
   [~MCE] ospfv3 100 vpn-instance vpna
   [~MCE-ospfv3-100] vpn-instance-capability simple
   [*MCE-ospfv3-100] import-route ripng 100
   [*MCE-ospfv3-100] quit
   [*MCE] ospfv3 200 vpn-instance vpnb
   [*MCE-ospfv3-200] vpn-instance-capability simple
   [*MCE-ospfv3-200] import-route ripng 200
   [*MCE-ospfv3-200] quit
   [*MCE] commit
   ```

#### Verifying the Configuration

After the configuration is complete, run the **display ipv6 routing-table** **vpn-instance** command on the MCE to check IPv6 routing information of VPN instances.

The following example uses the VPN instance **vpna**.

```
[~MCE] display ipv6 routing-table vpn-instance vpna
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route 
------------------------------------------------------------------------------ 
Routing Table : vpna
         Destinations : 7        Routes : 7

Destination  : 2001:DB8:13::3                          PrefixLength : 128
NextHop      : FE80::2200:10FF:FE03:0                  Preference   : 100
Cost         : 1                                       Protocol     : RIPng
RelayNextHop : ::                                      TunnelID     : 0x0
Interface    : 100GE1/0/3                               Flags        : D

Destination  : 2001:DB8:8::                            PrefixLength : 64
NextHop      : 2001:DB8:8::2                           Preference   : 0
Cost         : 0                                       Protocol     : Direct
RelayNextHop : ::                                      TunnelID     : 0x0
Interface    : 100GE1/0/1                               Flags        : D

Destination  : 2001:DB8:8::2                           PrefixLength : 128
NextHop      : ::1                                     Preference   : 0
Cost         : 0                                       Protocol     : Direct
RelayNextHop : ::                                      TunnelID     : 0x0
Interface    : 100GE1/0/1                               Flags        : D

Destination  : 2001:DB8:3::                            PrefixLength : 64
NextHop      : 2001:DB8:3::2                           Preference   : 0
Cost         : 0                                       Protocol     : Direct
RelayNextHop : ::                                      TunnelID     : 0x0
Interface    : 100GE1/0/3                               Flags        : D

Destination  : 2001:DB8:3::2                           PrefixLength : 128
NextHop      : ::1                                     Preference   : 0
Cost         : 0                                       Protocol     : Direct
RelayNextHop : ::                                      TunnelID     : 0x0
Interface    : 100GE1/0/3                               Flags        : D

Destination  : FE80::                                  PrefixLength : 10
NextHop      : ::                                      Preference   : 0
Cost         : 0                                       Protocol     : Direct
RelayNextHop : ::                                      TunnelID     : 0x0
Interface    : NULL0                                   Flags        : D
```

#### Configuration Scripts

* PE1
  
  ```
  #
  sysname PE1
  #
  ip vpn-instance vpna
   ipv6-family
    route-distinguisher 200:1
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  #
  ip vpn-instance vpnb
   ipv6-family
    route-distinguisher 200:2
    vpn-target 222:2 export-extcommunity
    vpn-target 222:2 import-extcommunity
  #
  ospfv3 100 vpn-instance vpna
   router-id 10.5.5.5
   area 0.0.0.1
  #
  ospfv3 200 vpn-instance vpnb
   router-id 10.6.6.6
   area 0.0.0.2
  #
  interface 100GE1/0/1
   undo portswitch
   ip binding vpn-instance vpna
   ipv6 enable
   ipv6 address 2001:DB8:8::1/64
   ospfv3 100 area 0.0.0.1 instance 1
  #
  interface 100GE1/0/2
   undo portswitch
   ip binding vpn-instance vpnb
   ipv6 enable
   ipv6 address 2001:DB8:9::1/64
   ospfv3 200 area 0.0.0.2 instance 2
  #
  return
  ```
* MCE
  
  ```
  #
  sysname MCE
  #
  ip vpn-instance vpna
   ipv6-family
    route-distinguisher 100:1
  #
  ip vpn-instance vpnb
   ipv6-family
    route-distinguisher 100:2
  #
  ospfv3 100 vpn-instance vpna
   router-id 10.7.7.7
   vpn-instance-capability simple
   import-route ripng 100
   area 0.0.0.1
  #
  ospfv3 200 vpn-instance vpnb
   router-id 10.8.8.8
   vpn-instance-capability simple
   import-route ripng 200
   area 0.0.0.2
  #
  interface 100GE1/0/1
   undo portswitch
   ip binding vpn-instance vpna
   ipv6 enable
   ipv6 address 2001:DB8:8::2/64
   ospfv3 100 area 0.0.0.1 instance 1
  #
  interface 100GE1/0/2
   undo portswitch
   ip binding vpn-instance vpnb
   ipv6 enable
   ipv6 address 2001:DB8:9::2/64
   ospfv3 200 area 0.0.0.2 instance 2
  #
  interface 100GE1/0/3
   undo portswitch
   ip binding vpn-instance vpna
   ipv6 enable
   ipv6 address 2001:DB8:3::2/64
   ripng 100 enable
  #
  interface 100GE1/0/4
   undo portswitch
   ip binding vpn-instance vpnb
   ipv6 enable
   ipv6 address 2001:DB8:4::2/64
   ripng 200 enable
  #
  ripng 100 vpn-instance vpna
   import-route ospfv3 100
  #
  ripng 200 vpn-instance vpnb
   import-route ospfv3 200
  #
  return
  ```
* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:3::1/64
   ripng 100 enable
  #
  interface LoopBack1
   ipv6 enable
   ipv6 address 2001:DB8:13::3/128
   ripng 100 enable
  #
  ripng 100
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:4::1/64
   ripng 200 enable
  #
  interface LoopBack1
   ipv6 enable
   ipv6 address 2001:DB8:14::4/128
   ripng 200 enable
  #
  ripng 200
  #
  return
  ```