Example for Configuring an MCE
==============================

Example for Configuring an MCE

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001130781458__fig_dc_vrp_mpls-l3vpn-v4_cfg_012201), Site 1 and Site 2 are both connected to PE1, but the two sites need to be isolated from each other and use independent address spaces. To meet the preceding requirements and reduce costs, an MCE solution can be used.

**Figure 1** MCE networking![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, interface 3, and interface 4 represent 100GE 1/0/1, 100GE 1/0/2, 100GE 1/0/3, and 100GE 1/0/4, respectively.


  
![](figure/en-us_image_0000001130621860.png "Click to enlarge")

#### Precautions

Note the following during the configuration:

* The MCE must have multiple VPN instances configured and have a different interface bound to each VPN instance.
* Routing loop detection must be disabled on the MCE so that the MCE exchanges routing information with the PE using the OSPF multi-VPN-instance.
* Configure RIPv2 on the MCE to import VPN routes from Site 1 and Site 2.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure VPN instances on the MCE and PE1 and bind related interfaces to the VPN instances.
2. Configure OSPF multi-instance on the MCE and PE1 to exchange VPN routing information.
3. Configure RIPv2 on the MCE, DeviceA, and DeviceB to exchange VPN routes.
4. Disable routing loop detection on the MCE and import RIP routes destined for VPN sites.

#### Procedure

1. Configure VPN instances on the MCE and PE1 and bind related interfaces to the VPN instances.
   
   
   
   # Configure PE1.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname PE1
   [*HUAWEI] commit
   [~PE1] ip vpn-instance vpna
   [*PE1-vpn-instance-vpna] ipv4-family
   [*PE1-vpn-instance-vpna-af-ipv4] route-distinguisher 200:1
   [*PE1-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
   [*PE1-vpn-instance-vpna-af-ipv4] quit
   [*PE1-vpn-instance-vpna] quit
   [*PE1] ip vpn-instance vpnb
   [*PE1-vpn-instance-vpnb] ipv4-family
   [*PE1-vpn-instance-vpnb-af-ipv4] route-distinguisher 200:2
   [*PE1-vpn-instance-vpnb-af-ipv4] vpn-target 222:2 both
   [*PE1-vpn-instance-vpnb-af-ipv4] quit
   [*PE1-vpn-instance-vpnb] quit
   [*PE1] interface 100GE1/0/1
   [*PE1-100GE1/0/1] undo portswitch
   [*PE1-100GE1/0/1] ip binding vpn-instance vpna
   [*PE1-100GE1/0/1] ip address 10.5.1.1 24
   [*PE1-100GE1/0/1] quit
   [*PE1]interface 100GE1/0/2
   [*PE1-100GE1/0/2] undo portswitch
   [*PE1-100GE1/0/2] ip binding vpn-instance vpnb
   [*PE1-100GE1/0/2] ip address 10.5.2.1 24
   [*PE1-100GE1/0/2] quit
   [*PE1] commit
   ```
   
   # Configure an MCE.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname MCE
   [*HUAWEI] commit
   [~MCE] ip vpn-instance vpna
   [*MCE-vpn-instance-vpna] ipv4-family
   [*MCE-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
   [*MCE-vpn-instance-vpna-af-ipv4] quit
   [*MCE-vpn-instance-vpna] quit
   [*MCE] ip vpn-instance vpnb
   [*MCE-vpn-instance-vpnb] ipv4-family
   [*MCE-vpn-instance-vpnb-af-ipv4] route-distinguisher 100:2
   [*MCE-vpn-instance-vpnb-af-ipv4] quit
   [*MCE-vpn-instance-vpnb] quit
   [*MCE] interface 100GE1/0/1
   [*MCE-100GE1/0/1] undo portswitch
   [*MCE-100GE1/0/1] ip binding vpn-instance vpna
   [*MCE-100GE1/0/1] ip address 10.5.1.2 24
   [*MCE-100GE1/0/1] quit
   [*MCE] interface 100GE1/0/2
   [*MCE-100GE1/0/2] undo portswitch
   [*MCE-100GE1/0/2] ip binding vpn-instance vpnb
   [*MCE-100GE1/0/2] ip address 10.5.2.2 24
   [*MCE-100GE1/0/2] quit
   [*MCE] interface 100GE1/0/3
   [*MCE-100GE1/0/3] undo portswitch
   [*MCE-100GE1/0/3] ip binding vpn-instance vpna
   [*MCE-100GE1/0/3] ip address 10.3.1.2 24
   [*MCE-100GE1/0/3] quit
   [*MCE] interface 100GE1/0/4
   [*MCE-100GE1/0/4] undo portswitch
   [*MCE-100GE1/0/4] ip binding vpn-instance vpnb
   [*MCE-100GE1/0/4] ip address 10.4.1.2 24
   [*MCE-100GE1/0/4] quit
   [*MCE] commit
   ```
2. Configure OSPF multi-instance between PE1 and the MCE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] ospf 100 vpn-instance vpna
   [*PE1-ospf-100] area 0
   [*PE1-ospf-100-area-0.0.0.0] network 10.5.1.0 0.0.0.255
   [*PE1-ospf-100-area-0.0.0.0] quit
   [*PE1-ospf-100] quit
   [*PE1] ospf 200 vpn-instance vpnb
   [*PE1-ospf-200] area 0
   [*PE1-ospf-200-area-0.0.0.0] network 10.5.2.0 0.0.0.255
   [*PE1-ospf-200-area-0.0.0.0] quit
   [*PE1-ospf-200] quit
   [*PE1] commit
   ```
   
   # Configure the MCE.
   
   ```
   [~MCE] ospf 100 vpn-instance vpna
   [*MCE-ospf-100] area 0
   [*MCE-ospf-100-area-0.0.0.0] network 10.5.1.0 0.0.0.255
   [*MCE-ospf-100-area-0.0.0.0] quit
   [*MCE-ospf-100] quit
   [*MCE] ospf 200 vpn-instance vpnb
   [*MCE-ospf-200] area 0
   [*MCE-ospf-200-area-0.0.0.0] network 10.5.2.0 0.0.0.255
   [*MCE-ospf-200-area-0.0.0.0] quit
   [*MCE-ospf-200] quit
   [*MCE] commit
   ```
3. Configure RIPv2 on the MCE to import VPN routes from Site 1 and Site 2.
   
   
   
   # Configure the MCE.
   
   ```
   [~MCE] rip 100 vpn-instance vpna
   [~MCE-rip-100] version 2
   [*MCE-rip-100] network 10.0.0.0
   [*MCE-rip-100] import-route ospf 100
   [*MCE-rip-100] quit
   [*MCE] rip 200 vpn-instance vpnb
   [*MCE-rip-200] version 2
   [*MCE-rip-200] network 10.0.0.0
   [*MCE-rip-200] import-route ospf 200
   [*MCE-rip-200] quit
   [*MCE] commit
   ```
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface 100GE1/0/1
   [*DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ip address 10.3.1.1 24
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface Loopback1
   [*DeviceA-Loopback1] ip address 3.3.3.3 32
   [*DeviceA-Loopback1] quit
   [*DeviceA] rip 100
   [*DeviceA-rip-100] version 2
   [*DeviceA-rip-100] network 10.0.0.0
   [*DeviceA-rip-100] network 3.0.0.0
   [*DeviceA-rip-100] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] interface 100GE1/0/1
   [*DeviceB-100GE1/0/1] undo portswitch
   [*DeviceB-100GE1/0/1] ip address 10.4.1.1 24
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] interface Loopback1
   [*DeviceB-Loopback1] ip address 4.4.4.4 32
   [*DeviceB-Loopback1] quit
   [*DeviceB] rip 200
   [*DeviceB-rip-200] version 2
   [*DeviceB-rip-200] network 10.0.0.0
   [*DeviceB-rip-200] network 4.0.0.0
   [*DeviceB-rip-200] quit
   [*DeviceB] commit
   ```
4. Disable routing loop detection on the MCE and import RIP routes destined for VPN sites.
   
   
   ```
   [~MCE] ospf 100 vpn-instance vpna
   [~MCE-ospf-100] vpn-instance-capability simple
   [*MCE-ospf-100] import-route rip 100
   [*MCE-ospf-100] quit
   [*MCE] ospf 200 vpn-instance vpnb
   [*MCE-ospf-200] vpn-instance-capability simple
   [*MCE-ospf-200] import-route rip 200
   [*MCE-ospf-200] quit
   [*MCE] commit
   ```

#### Verifying the Configuration

After the configuration is complete, run the **display ip routing-table** **vpn-instance** command on the MCE to check the routing information of the VPN instances.

The following uses the routing table of the VPN instance named **vpna** as an example.

```
[~MCE] display ip routing-table vpn-instance vpna
Proto: Protocol        Pre: Preference
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table : vpna
         Destinations : 9       Routes : 9

Destination/Mask    Proto  Pre  Cost        Flags NextHop         Interface

       10.3.1.0/24  Direct 0    0             D  10.3.1.2        100GE1/0/3
       10.3.1.2/32  Direct 0    0             D  127.0.0.1       100GE1/0/3
     10.3.1.255/32  Direct 0    0             D  127.0.0.1       100GE1/0/3
        3.3.3.3/32  RIP    100  1             D  10.3.1.1        100GE1/0/3
       10.5.1.0/24  Direct 0    0             D  10.5.1.2        100GE1/0/1
       10.5.1.1/32  Direct 0    0             D  10.5.1.1        100GE1/0/1
       10.5.1.2/32  Direct 0    0             D  127.0.0.1       100GE1/0/1
     10.5.1.255/32  Direct 0    0             D  127.0.0.1       100GE1/0/1
255.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
```

#### Configuration Scripts

* PE1
  
  ```
  #
  sysname PE1
  #
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 200:1
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  #
  ip vpn-instance vpnb
   ipv4-family
    route-distinguisher 200:2
    vpn-target 222:2 export-extcommunity
    vpn-target 222:2 import-extcommunity
  #
  interface 100GE1/0/1
   undo portswitch
   ip binding vpn-instance vpna
   ip address 10.5.1.1 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip binding vpn-instance vpnb
   ip address 10.5.2.1 255.255.255.0
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
  #
  ospf 100 vpn-instance vpna
   area 0.0.0.0
    network 10.5.1.0 0.0.0.255
  #
  ospf 200 vpn-instance vpnb
   area 0.0.0.0
    network 10.5.2.0 0.0.0.255
  #
  return
  ```
* MCE
  
  ```
  #
  sysname MCE
  #
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 100:1
  #
  ip vpn-instance vpnb
   ipv4-family
    route-distinguisher 100:2
  #
  interface 100GE1/0/1
   undo portswitch
   ip binding vpn-instance vpna
   ip address 10.5.1.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip binding vpn-instance vpnb
   ip address 10.5.2.2 255.255.255.0
  #
  interface 100GE1/0/3
   undo portswitch
   ip binding vpn-instance vpna
   ip address 10.3.1.2 255.255.255.0
  #
  interface 100GE1/0/4
   undo portswitch
   ip binding vpn-instance vpnb
   ip address 10.4.1.2 255.255.255.0
  #
  ospf 100 vpn-instance vpna
   import-route rip 100
   vpn-instance-capability simple
   area 0.0.0.0
    network 10.3.1.0 0.0.0.255
    network 10.5.1.0 0.0.0.255
  #
  ospf 200 vpn-instance vpnb
   import-route rip 200
   vpn-instance-capability simple
   area 0.0.0.0
    network 10.4.1.0 0.0.0.255
    network 10.5.2.0 0.0.0.255
  #
  rip 100 vpn-instance vpna
   version 2
   network 10.0.0.0
   import-route ospf 100
  #
  rip 200 vpn-instance vpnb
   version 2
   network 10.0.0.0
   import-route ospf 200
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
   ip address 10.3.1.1 255.255.255.0
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
  #
  rip 100
   version 2
   network 10.0.0.0
   network 3.0.0.0
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
   ip address 10.4.1.1 255.255.255.0
  #
  interface LoopBack1
   ip address 4.4.4.4 255.255.255.255
  #
  rip 200
   version 2
   network 10.0.0.0
   network 4.0.0.0
  #
  return
  ```