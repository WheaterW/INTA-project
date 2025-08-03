Example for Configuring a BGP Confederation
===========================================

Example for Configuring a BGP Confederation

#### Networking Requirements

If multiple devices are deployed in an AS and fully meshed IBGP connections must be set up between every two devices in the AS, a large number of IBGP connections will be established, increasing operation and maintenance costs. To address this issue, configure a BGP confederation.

As shown in [Figure 1](#EN-US_TASK_0000001130783876__fig_dc_vrp_bgp_cfg_407601), to implement IP connectivity between devices in AS 200, full-mesh IBGP connections need to be established between the devices. However, since multiple devices run BGP in AS 200, the configuration workload for establishing a full-mesh network is heavy. To reduce the number of IBGP connections to be established, you can configure the confederation function on the devices in AS 200. Configuring a confederation is a method to handle the sharp increase of IBGP connections in an AS. In [Figure 1](#EN-US_TASK_0000001130783876__fig_dc_vrp_bgp_cfg_407601), AS 200 is divided into three sub-ASs: AS 65001, AS 65002, and AS 65003. A confederation EBGP multi-peer relationship can be established between AS 65001 and each of AS 65002 and AS 65003. The three devices in AS 65001 establish full-mesh IBGP connections. This greatly reduces the number of IBGP connections to be established in AS 200 and reduces O&M costs.

**Figure 1** Network diagram of configuring a BGP confederation![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, interface 3, interface 4, and interface 5 represent 100GE1/0/1, 100GE1/0/2, 100GE1/0/3, 100GE1/0/4, and 100GE1/0/5, respectively.


  
![](figure/en-us_image_0000001130624162.png)

#### Precautions

During the configuration, note the following:

* To improve security, you are advised to deploy BGP security measures. For details, see "Configuring BGP Authentication." Keychain authentication is used as an example. For details, see Example for Configuring Keychain Authentication for BGP.

#### Procedure

1. Assign an IP address to each involved interface. For detailed configurations, see [Configuration Scripts](#EN-US_TASK_0000001130783876__postreq17364171716277).
2. Configure a BGP confederation.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] bgp 65001
   [*DeviceA-bgp] router-id 1.1.1.1
   [*DeviceA-bgp] confederation id 200
   [*DeviceA-bgp] confederation peer-as 65002 65003
   [*DeviceA-bgp] peer 10.1.1.2 as-number 65002 
   [*DeviceA-bgp] peer 10.1.2.2 as-number 65003
   [*DeviceA-bgp] ipv4-family unicast
   [*DeviceA-bgp-af-ipv4] peer 10.1.1.2 next-hop-local
   [*DeviceA-bgp-af-ipv4] peer 10.1.2.2 next-hop-local
   [*DeviceA-bgp-af-ipv4] quit
   [*DeviceA-bgp] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] bgp 65002
   [*DeviceB-bgp] router-id 2.2.2.2
   [*DeviceB-bgp] confederation id 200
   [*DeviceB-bgp] confederation peer-as 65001
   [*DeviceB-bgp] peer 10.1.1.1 as-number 65001
   [*DeviceB-bgp] quit
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] bgp 65003
   [*DeviceC-bgp] router-id 3.3.3.3
   [*DeviceC-bgp] confederation id 200
   [*DeviceC-bgp] confederation peer-as 65001
   [*DeviceC-bgp] peer 10.1.2.1 as-number 65001
   [*DeviceC-bgp] quit
   [*DeviceC] commit
   ```
3. Configure IBGP connections in AS 65001.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] bgp 65001
   [~DeviceA-bgp] peer 10.1.3.2 as-number 65001
   [*DeviceA-bgp] peer 10.1.4.2 as-number 65001
   [*DeviceA-bgp] ipv4-family unicast
   [*DeviceA-bgp-af-ipv4] peer 10.1.3.2 next-hop-local
   [*DeviceA-bgp-af-ipv4] peer 10.1.4.2 next-hop-local
   [*DeviceA-bgp-af-ipv4] quit 
   [*DeviceA-bgp] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] bgp 65001
   [*DeviceD-bgp] router-id 4.4.4.4
   [*DeviceD-bgp] confederation id 200
   [*DeviceD-bgp] peer 10.1.3.1 as-number 65001
   [*DeviceD-bgp] peer 10.1.5.2 as-number 65001
   [*DeviceD-bgp] quit
   [*DeviceD] commit
   ```
   
   # Configure DeviceE.
   
   ```
   [~DeviceE] bgp 65001
   [*DeviceE-bgp] router-id 5.5.5.5
   [*DeviceE-bgp] confederation id 200
   [*DeviceE-bgp] peer 10.1.4.1 as-number 65001
   [*DeviceE-bgp] peer 10.1.5.1 as-number 65001
   [*DeviceE-bgp] quit
   [*DeviceE] commit
   ```
4. Establish an EBGP connection between AS 100 and AS 200.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] bgp 65001
   [~DeviceA-bgp] peer 172.16.1.2 as-number 100 
   [*DeviceA-bgp] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceF.
   
   ```
   [~DeviceF] bgp 100
   [*DeviceF-bgp] router-id 6.6.6.6
   [*DeviceF-bgp] peer 172.16.1.1 as-number 200 
   [*DeviceF-bgp] ipv4-family unicast
   [*DeviceF-bgp-af-ipv4] network 192.168.1.0 255.255.255.0
   [*DeviceF-bgp-af-ipv4] quit
   [*DeviceF-bgp] quit
   [*DeviceF] commit
   ```

#### Verifying the Configuration

# Check the BGP routing table of DeviceB.

```
[~DeviceB] display bgp routing-table
 BGP Local router ID is 2.2.2.2
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
               Origin : i - IGP, e - EGP, ? - incomplete
 RPKI validation codes: V - valid, I - invalid, N - not-found

 Total Number of Routes: 1
      Network            NextHop        MED        LocPrf    PrefVal Path/Ogn

 *>i  192.168.1.0/24     10.1.1.1        0          100        0      (65001) 100i
```
```
[~DeviceB] display bgp routing-table 192.168.1.0
BGP local router ID : 2.2.2.2
 Local AS number : 65002
 Paths:   1 available, 1 best, 1 select
 BGP routing table entry information of 192.168.1.0/24:
 From: 10.1.1.1 (1.1.1.1)
 Route Duration: 00h12m29s
 Relay IP Nexthop: 0.0.0.0
 Relay IP Out-Interface: 100GE1/0/1
 Original nexthop: 10.1.1.1
 Qos information : 0x0
 AS-path (65001) 100, origin igp, MED 0, localpref 100, pref-val 0, valid, external-confed, best, select, active, pre 255
 Not advertised to any peer yet
```

# Check the BGP routing table of DeviceD.

```
[~DeviceD] display bgp routing-table
 BGP Local router ID is 4.4.4.4
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
               Origin : i - IGP, e - EGP, ? - incomplete
 RPKI validation codes: V - valid, I - invalid, N - not-found

 Total Number of Routes: 1
      Network            NextHop        MED        LocPrf    PrefVal Path/Ogn

 *>i  192.168.1.0/24     10.1.3.1        0          100        0      100i
```
```
[~DeviceD] display bgp routing-table 192.168.1.0
BGP local router ID : 4.4.4.4
 Local AS number : 65001
 Paths:   1 available, 1 best, 1 select
 BGP routing table entry information of 192.168.1.0/24:
 From: 10.1.3.1 (1.1.1.1)
 Route Duration: 00h23m57s
 Relay IP Nexthop: 0.0.0.0
 Relay IP Out-Interface:100GE1/0/1
 Original nexthop: 10.1.3.1
 Qos information : 0x0
 AS-path 100, origin igp, MED 0, localpref 100, pref-val 0, valid, internal-confed, best, select, active, pre 255
 Not advertised to any peer yet
```

#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 172.16.1.1 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.1.1 255.255.255.0
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 10.1.2.1 255.255.255.0
  #
  interface 100GE1/0/4
   undo portswitch
   ip address 10.1.3.1 255.255.255.0
  #
  interface 100GE1/0/5
   undo portswitch
   ip address 10.1.4.1 255.255.255.0
  #
  bgp 65001
   router-id 1.1.1.1
   confederation id 200
   confederation peer-as 65002 65003
   peer 10.1.1.2 as-number 65002
   peer 10.1.2.2 as-number 65003
   peer 10.1.3.2 as-number 65001
   peer 10.1.4.2 as-number 65001
   peer 172.16.1.2 as-number 100
   #
   ipv4-family unicast
    undo synchronization 
    peer 172.16.1.2 enable
    peer 10.1.1.2 enable
    peer 10.1.1.2 next-hop-local
    peer 10.1.2.2 enable
    peer 10.1.2.2 next-hop-local
    peer 10.1.3.2 enable
    peer 10.1.3.2 next-hop-local
    peer 10.1.4.2 enable
    peer 10.1.4.2 next-hop-local
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
   ip address 10.1.1.2 255.255.255.0
  #
  bgp 65002
   router-id 2.2.2.2
   confederation id 200
   confederation peer-as 65001
   peer 10.1.1.1 as-number 65001
   #
   ipv4-family unicast
    undo synchronization 
    peer 10.1.1.1 enable
  #
  return
  ```
  ![](public_sys-resources/note_3.0-en-us.png) 
  
  The configuration script of DeviceC is similar to that of DeviceB.
* DeviceD
  
  ```
  #
  sysname DeviceD
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.3.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.5.1 255.255.255.0
  #
  bgp 65001
   router-id 4.4.4.4
   confederation id 200
   peer 10.1.3.1 as-number 65001
   peer 10.1.5.2 as-number 65001
   #
   ipv4-family unicast
    undo synchronization 
    peer 10.1.3.1 enable
    peer 10.1.5.2 enable
  #
  return
  ```
  ![](public_sys-resources/note_3.0-en-us.png) 
  
  The configuration script of DeviceE is similar to that of DeviceD.
* DeviceF
  
  ```
  #
  sysname DeviceF
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 172.16.1.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.1.1 255.255.255.0
  #
  bgp 100
   router-id 6.6.6.6
   peer 172.16.1.1 as-number 200
   #
   ipv4-family unicast
    undo synchronization 
    network 192.168.1.0 255.255.255.0
    peer 172.16.1.1 enable
  #
  return
  ```