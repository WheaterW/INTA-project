Example for Configuring a BGP Confederation
===========================================

BGP confederations can be used to reduce the number of IBGP connections.

#### Networking Requirements

If multiple devices are deployed in an AS and fully meshed IBGP connections must be implemented between every two devices in the AS, a large number of IBGP connections will be established, increasing operation and maintenance costs. To address this issue, configure BGP confederations.

In [Figure 1](#EN-US_TASK_0172366376__fig_dc_vrp_bgp_cfg_407601), to implement interworking between devices in AS 200, full-mesh IBGP connections need to be established between the devices. However, because multiple Routers run BGP in AS 200, the cost for establishing a fully meshed network is high. To reduce the number of IBGP connections to be established, you can configure the confederation function on the devices in AS 200. The confederation solution can deal with the increase of IBGP connections in an AS. As shown in [Figure 1](#EN-US_TASK_0172366376__fig_dc_vrp_bgp_cfg_407601), AS 200 is divided into three sub-ASs: AS 65001, AS 65002, and AS 65003. AS 65001 establishes confederation EBGP peer relationships with AS 65002 and AS 65003. The three Routers in AS 65001 establish IBGP fully meshed connections. This greatly reduces the number of IBGP connections to be established in AS 200 and reduces O&M costs.

**Figure 1** Configuring the confederation![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 5 in this example represent GE0/1/0, GE0/2/0, GE0/3/0, GE0/1/1, and GE0/1/2, respectively.


  
![](images/fig_dc_vrp_bgp_cfg_407601.png)

#### Precautions

To improve security, you are advised to deploy BGP security measures. For details, see "Configuring BGP Security." Keychain authentication is used as an example. For details, see "Example for Configuring BGP Keychain."


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a BGP confederation on each Router in AS 200.
2. Configure the IBGP connection in AS 65001.
3. Configure the EBGP connection between AS 100 and AS 200, and check the routes.

#### Data Preparation

To complete the configuration, you need the following data:

* The Router IDs of DeviceA, DeviceB, DeviceC, DeviceD, DeviceE, and DeviceF (1.1.1.1, 2.2.2.2, 3.3.3.3, 4.4.4.4, 5.5.5.5, and 6.6.6.6)
* The AS number (100), and the three sub-ASs of AS 200 (AS 65001, AS 65002, and AS 65003)

#### Procedure

1. Assign an IP address to each interface.
   
   
   
   For configuration details, see [Configuration Files](#EN-US_TASK_0172366376__section_dc_vrp_bgp_cfg_407605) in this section.
2. Configure the BGP confederation.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] bgp 65001
   ```
   ```
   [*DeviceA-bgp] router-id 1.1.1.1
   ```
   ```
   [*DeviceA-bgp] confederation id 200
   ```
   ```
   [*DeviceA-bgp] confederation peer-as 65002 65003
   ```
   ```
   [*DeviceA-bgp] peer 10.1.1.2 as-number 65002 
   ```
   ```
   [*DeviceA-bgp] peer 10.1.2.2 as-number 65003
   ```
   ```
   [*DeviceA-bgp] ipv4-family unicast
   ```
   ```
   [*DeviceA-bgp-af-ipv4] peer 10.1.1.2 next-hop-local
   ```
   ```
   [*DeviceA-bgp-af-ipv4] peer 10.1.2.2 next-hop-local
   ```
   ```
   [*DeviceA-bgp-af-ipv4] commit
   ```
   ```
   [~DeviceA-bgp-af-ipv4] quit
   ```
   ```
   [~DeviceA-bgp] quit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] bgp 65002
   ```
   ```
   [*DeviceB-bgp] router-id 2.2.2.2
   ```
   ```
   [*DeviceB-bgp] confederation id 200
   ```
   ```
   [*DeviceB-bgp] confederation peer-as 65001
   ```
   ```
   [*DeviceB-bgp] peer 10.1.1.1 as-number 65001
   ```
   ```
   [*DeviceB-bgp] commit
   ```
   ```
   [~DeviceB-bgp] quit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] bgp 65003
   ```
   ```
   [*DeviceC-bgp] router-id 3.3.3.3
   ```
   ```
   [*DeviceC-bgp] confederation id 200
   ```
   ```
   [*DeviceC-bgp] confederation peer-as 65001
   ```
   ```
   [*DeviceC-bgp] peer 10.1.2.1 as-number 65001
   ```
   ```
   [*DeviceC-bgp] commit
   ```
   ```
   [~DeviceC-bgp] quit
   ```
3. Configure IBGP connections inside AS 65001.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] bgp 65001
   ```
   ```
   [*DeviceA-bgp] peer 10.1.3.2 as-number 65001
   ```
   ```
   [*DeviceA-bgp] peer 10.1.4.2 as-number 65001
   ```
   ```
   [*DeviceA-bgp] ipv4-family unicast
   ```
   ```
   [*DeviceA-bgp-af-ipv4] peer 10.1.3.2 next-hop-local
   ```
   ```
   [*DeviceA-bgp-af-ipv4] peer 10.1.4.2 next-hop-local
   ```
   ```
   [*DeviceA-bgp-af-ipv4] commit
   ```
   ```
   [~DeviceA-bgp-af-ipv4] quit 
   ```
   ```
   [~DeviceA-bgp] quit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] bgp 65001
   ```
   ```
   [*DeviceD-bgp] router-id 4.4.4.4
   ```
   ```
   [*DeviceD-bgp] confederation id 200
   ```
   ```
   [*DeviceD-bgp] peer 10.1.3.1 as-number 65001
   ```
   ```
   [*DeviceD-bgp] peer 10.1.5.2 as-number 65001
   ```
   ```
   [*DeviceD-bgp] commit
   ```
   ```
   [~DeviceD-bgp] quit
   ```
   
   # Configure DeviceE.
   
   ```
   [~DeviceE] bgp 65001
   ```
   ```
   [*DeviceE-bgp] router-id 5.5.5.5
   ```
   ```
   [*DeviceE-bgp] confederation id 200
   ```
   ```
   [*DeviceE-bgp] peer 10.1.4.1 as-number 65001
   ```
   ```
   [*DeviceE-bgp] peer 10.1.5.1 as-number 65001
   ```
   ```
   [*DeviceE-bgp] commit
   ```
   ```
   [~DeviceE-bgp] quit
   ```
4. Configure the EBGP connection between AS 100 and AS 200.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] bgp 65001
   ```
   ```
   [*DeviceA-bgp] peer 10.216.1.2 as-number 100 
   ```
   ```
   [*DeviceA-bgp] commit
   ```
   ```
   [~DeviceA-bgp] quit
   ```
   
   # Configure DeviceF.
   
   ```
   [~DeviceF] bgp 100
   ```
   ```
   [*DeviceF-bgp] router-id 6.6.6.6
   ```
   ```
   [*DeviceF-bgp] peer 10.216.1.1 as-number 200 
   ```
   ```
   [*DeviceF-bgp] ipv4-family unicast
   ```
   ```
   [*DeviceF-bgp-af-ipv4] network 192.168.1.0 255.255.255.0
   ```
   ```
   [*DeviceF-bgp-af-ipv4] commit
   ```
   ```
   [~DeviceF-bgp-af-ipv4] quit
   ```
   ```
   [~DeviceF-bgp] quit
   ```
5. Verify the configuration.
   
   
   
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
    Relay IP Out-Interface: GigabitEthernet0/1/0
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
    Relay IP Out-Interface: GigabitEthernet0/1/0
    Original nexthop: 10.1.3.1
    Qos information : 0x0
    AS-path 100, origin igp, MED 0, localpref 100, pref-val 0, valid, internal-confed, best, select, active, pre 255
    Not advertised to any peer yet
   ```

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
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.216.1.1 255.255.255.0
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
   ip address 10.1.1.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/3/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.2.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.3.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/2
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.4.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  bgp 65001
  ```
  ```
   router-id 1.1.1.1
  ```
  ```
   confederation id 200
  ```
  ```
   confederation peer-as 65002 65003
  ```
  ```
   peer 10.1.1.2 as-number 65002
  ```
  ```
   peer 10.1.2.2 as-number 65003
  ```
  ```
   peer 10.1.3.2 as-number 65001
  ```
  ```
   peer 10.1.4.2 as-number 65001
  ```
  ```
   peer 10.216.1.2 as-number 100
  ```
  ```
   #
  ```
  ```
   ipv4-family unicast
  ```
  ```
    undo synchronization 
    peer 10.216.1.2 enable
  ```
  ```
    peer 10.1.1.2 enable
  ```
  ```
    peer 10.1.1.2 next-hop-local
  ```
  ```
    peer 10.1.2.2 enable
  ```
  ```
    peer 10.1.2.2 next-hop-local
  ```
  ```
    peer 10.1.3.2 enable
  ```
  ```
    peer 10.1.3.2 next-hop-local
  ```
  ```
    peer 10.1.4.2 enable
  ```
  ```
    peer 10.1.4.2 next-hop-local
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceB configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceB
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
   ip address 10.1.1.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  bgp 65002
  ```
  ```
   router-id 2.2.2.2
  ```
  ```
   confederation id 200
  ```
  ```
   confederation peer-as 65001
  ```
  ```
   peer 10.1.1.1 as-number 65001
  ```
  ```
   #
  ```
  ```
   ipv4-family unicast
  ```
  ```
    undo synchronization 
    peer 10.1.1.1 enable
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
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.2.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  bgp 65003
  ```
  ```
   router-id 3.3.3.3
  ```
  ```
   confederation id 200
  ```
  ```
   confederation peer-as 65001
  ```
  ```
   peer 10.1.2.1 as-number 65001
  ```
  ```
   #
  ```
  ```
   ipv4-family unicast
  ```
  ```
    undo synchronization 
    peer 10.1.2.1 enable
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceD configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceD
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
   ip address 10.1.3.2 255.255.255.0
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
   ip address 10.1.5.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  bgp 65001
  ```
  ```
   router-id 4.4.4.4
  ```
  ```
   confederation id 200
  ```
  ```
   peer 10.1.3.1 as-number 65001
  ```
  ```
   peer 10.1.5.2 as-number 65001
  ```
  ```
   #
  ```
  ```
   ipv4-family unicast
  ```
  ```
    undo synchronization 
    peer 10.1.3.1 enable
  ```
  ```
    peer 10.1.5.2 enable
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceE configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceE
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
   ip address 10.1.3.2 255.255.255.0
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
   ip address 10.1.5.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  bgp 65001
  ```
  ```
   router-id 5.5.5.5
  ```
  ```
   confederation id 200
  ```
  ```
   peer 10.1.4.1 as-number 65001
  ```
  ```
   peer 10.1.5.1 as-number 65001
  ```
  ```
   #
  ```
  ```
   ipv4-family unicast
  ```
  ```
    undo synchronization 
    peer 10.1.4.1 enable
  ```
  ```
    peer 10.1.5.1 enable
  ```
  ```
  #
  ```
  ```
  return
  ```
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  The configuration file of DeviceE is similar to that of DeviceD.
* DeviceF configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceF
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
   ip address 10.216.1.2 255.255.255.0
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
   ip address 192.168.1.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  bgp 100
  ```
  ```
   router-id 6.6.6.6
  ```
  ```
   peer 10.216.1.1 as-number 200
  ```
  ```
   #
  ```
  ```
   ipv4-family unicast
  ```
  ```
    undo synchronization 
    network 192.168.1.0 255.255.255.0
  ```
  ```
    peer 10.216.1.1 enable
  ```
  ```
  #
  ```
  ```
  return
  ```