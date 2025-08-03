Example for Configuring an Ethernet Service Activation Test on an EVPN VXLAN (Y.1564)
=====================================================================================

This section provides an example for configuring an Ethernet service activation test on an EVPN VXLAN to check whether network performance meets Service Level Agreement(SLA) requirements.

#### Networking Requirements

After network deployment is complete and before services are provisioned, you can configure an Ethernet service activation test to evaluate the network performance. This provides necessary data support for business planning and service promotion.

On the network shown in [Figure 1](#EN-US_TASK_0172373157__fig_dc_vrp_evpn_cfg_001101), the EVPN VXLAN network to be tested is located between user-network interfaces (UNIs). DeviceB is configured as the initiator, and DeviceC is configured as the reflector to check whether Ethernet frame transmission performance between them meets SLA requirements.

**Figure 1** Ethernet service activation test on an EVPN VXLAN![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, the destination MAC address is specified in a test instance to check the network performance between CEs on both ends of a Layer 2 EVPN. In a Layer 3 scenario, the destination IP address must be specified.

In this example, interfaces 1 and 2 represent GE0/1/0 and GE0/2/0, respectively.


  
![](images/fig_dc_vrp_nqa_cfg_006002.png)

#### Configuration Roadmap

The roadmap is as follows:

1. Configure a VXLAN network.
2. Configure DeviceA to communicate with DeviceB, and DeviceC to communicate with DeviceD.
3. Configure DeviceC as the reflector to reflect service traffic.
4. Configure DeviceB as the initiator to send simulated service traffic.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of interconnected interfaces of devices
* Service flow characteristics:
  
  + Destination MAC address: 00e0-fc12-3467 (MAC address of GE0/2/0 on DeviceD)
  + Source MAC address: 00e0-fc12-3465 (MAC address of GE0/2/0 on DeviceA)
  + VLAN ID carried in Ethernet frames: 10
  + UDP destination port number: 1234
  + UDP source port number: 5678
* Bandwidth profile: 10000 kbit/s for both the CIR and EIR
* Service acceptance criteria: 1000/100000 for the FLR and 1000 microseconds for both the FTD and FDV

#### Procedure

1. Assign IP addresses to node interfaces, including loopback interfaces.
   
   
   
   For configuration details, see [Configuration Files](#EN-US_TASK_0172373157__file1).
2. Configure an IGP on the backbone network. In this example, OSPF is used.
   
   
   
   For configuration details, see [Configuration Files](#EN-US_TASK_0172373157__file1).
3. Configure a VXLAN tunnel between DeviceB and DeviceC.
   
   
   
   For details about the configuration roadmap, see [VXLAN Configuration](dc_vrp_vxlan_cfg_1082.html). For configuration details, see [Configuration Files](#EN-US_TASK_0172373157__file1).
   
   After a VXLAN tunnel is established, you can run the [**display vxlan tunnel**](cmdqueryname=display+vxlan+tunnel) command on DeviceB or DeviceC to view VXLAN tunnel information. The command output on DeviceB is used as an example.
   
   ```
   [~DeviceB] display vxlan tunnel
   ```
   ```
   Number of vxlan tunnel : 1
   Tunnel ID   Source                Destination           State  Type     Uptime
   -----------------------------------------------------------------------------------
   4026531841  1.1.1.1               2.2.2.2               up     dynamic  00:12:56  
   ```
4. Configure communication between DeviceA and DeviceB, and between DeviceC and Device D.
   
   
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] interface gigabitethernet 0/2/0.1 mode l2
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0.1] encapsulation dot1q vid 10
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0.1] bridge-domain 10
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0.1] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/2/0.1] quit
   ```
   
   The configuration of DeviceC is similar to the configuration of DeviceB. For configuration details, see [Configuration Files](#EN-US_TASK_0172373157__file1).
   
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
   [~DeviceA] interface gigabitethernet 0/2/0.1
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0.1] ip address 10.100.0.1 24
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0.1] vlan-type dot1q 10
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0.1] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0.1] quit
   ```
   
   The configuration of DeviceD is similar to the configuration of DeviceA. For configuration details, see [Configuration Files](#EN-US_TASK_0172373157__file1).
5. Configure DeviceC as the reflector to reflect service traffic.
   
   
   ```
   [~DeviceC] nqa test-flow 1
   ```
   ```
   [*DeviceC-nqa-testflow-1] vlan 10
   ```
   ```
   [*DeviceC-nqa-testflow-1] udp destination-port 1234
   ```
   ```
   [*DeviceC-nqa-testflow-1] udp source-port 5678
   ```
   ```
   [*DeviceC-nqa-testflow-1] traffic-type mac destination 00e0-fc12-3467
   ```
   ```
   [*DeviceC-nqa-testflow-1] traffic-type mac source 00e0-fc12-3465
   ```
   ```
   [*DeviceC-nqa-testflow-1] quit
   ```
   ```
   [*DeviceC] nqa reflector 1 interface GigabitEthernet 0/2/0.1 test-flow 1 exchange-port agetime 0
   ```
   ```
   [*DeviceC] commit
   ```
6. Configure DeviceB as the initiator to send simulated service traffic.
   
   
   ```
   [~DeviceB] nqa test-flow 1
   ```
   ```
   [*DeviceB-nqa-testflow-1] vlan 10
   ```
   ```
   [*DeviceB-nqa-testflow-1] udp destination-port 1234
   ```
   ```
   [*DeviceB-nqa-testflow-1] udp source-port 5678
   ```
   ```
   [*DeviceB-nqa-testflow-1] cir simple-test enable
   ```
   ```
   [*DeviceB-nqa-testflow-1] bandwidth cir 10000 eir 10000
   ```
   ```
   [*DeviceB-nqa-testflow-1] sac flr 1000 ftd 1000 fdv 1000
   ```
   ```
   [*DeviceB-nqa-testflow-1] traffic-type mac destination 00e0-fc12-3467
   ```
   ```
   [*DeviceB-nqa-testflow-1] traffic-type mac source 00e0-fc12-3465
   ```
   ```
   [*DeviceB-nqa-testflow-1] traffic-policing test enable
   ```
   ```
   [*DeviceB-nqa-testflow-1] color-mode 8021p green 0 7 yellow 0 7
   ```
   ```
   [*DeviceB-nqa-testflow-1] commit
   ```
   ```
   [~DeviceB-nqa-testflow-1] quit
   ```
7. Start the Ethernet service activation test.
   
   
   ```
   [~DeviceB] nqa test-instance admin ethernet
   ```
   ```
   [*DeviceB-nqa-admin-ethernet] test-type ethernet-service
   ```
   ```
   [*DeviceB-nqa-admin-ethernet] forwarding-simulation inbound-interface GigabitEthernet 0/2/0.1
   ```
   ```
   [*DeviceB-nqa-admin-ethernet] test-flow 1
   ```
   ```
   [*DeviceB-nqa-admin-ethernet] start now
   ```
   ```
   [*DeviceB-nqa-admin-ethernet] commit
   ```
8. Verify the configuration.
   
   
   
   Run the **display nqa results test-instance admin ethernet** command on DeviceB. The command output shows that the test status is **Pass**, indicating that the test is successful.
   
   ```
   [~DeviceB-nqa-admin-ethernet] display nqa results test-instance admin ethernet
   ```
   ```
   NQA entry(admin, ethernet) :testflag is inactive ,testtype is ethernet-service
     1 . Test 1 result   The test is finished                                      
      Status           : Pass                                                      
      Test-flow number : 1                                                         
      Mode             : Round-trip                                                
      Last step        : Performance-test                                          
      Estimated total time  :6
      Real test time        :6
      1 . Configuration-test                                                       
       Test-flow 1, CIR simple test                                                
        Begin                    : 2014-06-25 16:22:45.8                           
        End                      : 2014-06-25 16:22:48.8                           
        Status                   : Pass                                            
        Min/Max/Mean IR(kbit/s)  : 9961/10075/10012                                
        Min/Max/Mean FTD(us)     : 99/111/104                                      
        Min/Max/Mean FDV(us)     : 0/7/3                                           
        FL Count/FLR             : 0/0.000%
        Disorder packets         : 0
        Unavail Count/AVAIL      : 0/0.000%                                        
       Test-flow 1, CIR/EIR test, Green                                            
        Begin                    : 2014-06-25 16:23:15.8                           
        End                      : 2014-06-25 16:23:18.8                           
        Status                   : Pass                                            
        Min/Max/Mean IR(kbit/s)  : 9979/10054/10012                                
        Min/Max/Mean FTD(us)     : 101/111/105                                     
        Min/Max/Mean FDV(us)     : 0/10/3                                          
        FL Count/FLR             : 0/0.000%
        Disorder packets         : 0
        Unavail Count/AVAIL      : 0/0.000%                                        
       Test-flow 1, CIR/EIR test, Yellow                                           
        Begin                    : 2014-06-25 16:23:15.8                           
        End                      : 2014-06-25 16:23:18.8                           
        Status                   : --                                              
        Min/Max/Mean IR(kbit/s)  : 9979/10057/10013                                
        Min/Max/Mean FTD(us)     : 98/111/104                                      
        Min/Max/Mean FDV(us)     : 1/11/5                                          
        FL Count/FLR             : 0/0.000%                                        
        Disorder packets         : 0
        Unavail Count/AVAIL      : 0/0.000%
       Test-flow 1, Traffic policing test, Green                                   
        Begin                    : 2014-06-25 16:23:45.8                           
        End                      : 2014-06-25 16:23:48.8                           
        Status                   : Pass                                            
        Min/Max/Mean IR(kbit/s)  : 10039/10054/10045                               
        Min/Max/Mean FTD(us)     : 96/110/104                                      
        Min/Max/Mean FDV(us)     : 1/9/4                                           
        FL Count/FLR             : 0/0.000% 
        Disorder packets         : 0
        Unavail Count/AVAIL      : 0/0.000%                                       
       Test-flow 1, Traffic policing test, Yellow                                  
        Begin                    : 2014-06-25 16:23:45.8                           
        End                      : 2014-06-25 16:23:48.8                           
        Status                   : --                                              
        Min/Max/Mean IR(kbit/s)  : 12544/12566/12554                               
        Min/Max/Mean FTD(us)     : 101/111/105                                     
        Min/Max/Mean FDV(us)     : 1/8/3                                           
        FL Count/FLR             : 0/0.000%
        Disorder packets         : 0
        Unavail Count/AVAIL      : 0/0.000%                                        
      2 . Performance-test                                                         
       Test-flow 1, Performance-test                                               
        Begin                    : 2014-06-25 16:24:15.8                           
        End                      : 2014-06-25 16:39:15.8                           
        Status                   : Pass                                            
        Min/Max/Mean IR(kbit/s)  : 9888/10132/10004                                
        Min/Max/Mean FTD(us)     : 101/111/105                                     
        Min/Max/Mean FDV(us)     : 0/8/2                                           
        FL Count/FLR             : 0/0.000%
        Disorder packets         : 0
        Unavail Count/AVAIL      : 0/0.000%
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  #
  interface GigabitEthernet0/2/0
   undo shutdown
  #
  interface GigabitEthernet0/2/0.1
   vlan-type dot1q 10
   ip address 10.100.0.1 255.255.255.0
  #
  ospf 1
   import-route direct 
   area 0.0.0.0
    network 10.100.0.0 0.0.0.255
  #
  return
  ```
* DeviceB configuration file
  
  ```
  #
  sysname DeviceB
  #
  evpn vpn-instance evpna bd-mode
   route-distinguisher 1:1
   apply-label per-instance
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #
  ip vpn-instance evpna
   ipv4-family
    route-distinguisher 1:1
    apply-label per-instance
    vpn-target 1:1 export-extcommunity evpn
    vpn-target 1:1 import-extcommunity evpn
  vxlan vni 100
  #
  bridge-domain 10
   vxlan vni 1 split-horizon-mode
   evpn binding vpn-instance evpna
  #
  interface Vbdif10
   ip binding vpn-instance evpna
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.0.0.1 255.255.255.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
  #
  interface GigabitEthernet0/2/0.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
   bridge-domain 10
  #
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
  #
  interface Nve1
   source 1.1.1.1
   vni 1 head-end peer-list protocol bgp
  #
  bgp 100
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 2.2.2.2 enable
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 2.2.2.2 enable
    peer 2.2.2.2 advertise irb
    peer 2.2.2.2 advertise encap-type vxlan
  #
  ospf 1
   import-route direct 
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 10.0.0.0 0.0.0.255
  #
  nqa test-flow 1
   vlan 10
   udp destination-port 1234
   udp source-port 5678
   cir simple-test enable
   bandwidth cir 10000 eir 10000
   sac flr 1000 ftd 1000 fdv 1000
   traffic-type mac destination 00e0-fc12-3467
   traffic-type mac source 00e0-fc12-3465
   traffic-policing test enable
   color-mode 8021p green 0 7 yellow 0 7
  #
  nqa test-instance admin ethernet
   test-type ethernet-service
   forwarding-simulation inbound-interface GigabitEthernet 0/2/0.1
   test-flow 1
  #
  return
  ```
* DeviceC configuration file
  
  ```
  #
  sysname DeviceC
  #
  evpn vpn-instance evpna bd-mode
   route-distinguisher 1:1
   apply-label per-instance
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #
  ip vpn-instance evpna
   ipv4-family
    route-distinguisher 1:1
    apply-label per-instance
    vpn-target 1:1 export-extcommunity evpn
    vpn-target 1:1 import-extcommunity evpn
  vxlan vni 100
  #
  bridge-domain 10
   vxlan vni 1 split-horizon-mode
   evpn binding vpn-instance evpna
  #
  interface Vbdif10
   ip binding vpn-instance evpna
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.0.0.2 255.255.255.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
  #
  interface GigabitEthernet0/2/0.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
   bridge-domain 10
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
  #
  interface Nve1
   source 2.2.2.2
   vni 1 head-end peer-list protocol bgp
  #
  bgp 100
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.1 enable
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 1.1.1.1 enable
    peer 1.1.1.1 advertise irb
    peer 1.1.1.1 advertise encap-type vxlan
  #
  ospf 1
   import-route direct 
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 10.0.0.0 0.0.0.255
  #
  nqa test-flow 1
   vlan 10
   udp destination-port 1234
   udp source-port 5678
   traffic-type mac destination 00e0-fc12-3467
   traffic-type mac source 00e0-fc12-3465
  #
  nqa reflector 1 interface GigabitEthernet 0/2/0.1 test-flow 1 exchange-port agetime 0
  #
  return
  ```
* DeviceD configuration file
  
  ```
  #
  sysname DeviceD
  #
  interface GigabitEthernet0/2/0
   undo shutdown
  #
  interface GigabitEthernet0/2/0.1
   vlan-type dot1q 10
   ip address 10.100.0.2 255.255.255.0
  #
  ospf 1
   import-route direct 
   area 0.0.0.0
    network 10.100.0.0 0.0.0.255
  #
  return
  ```