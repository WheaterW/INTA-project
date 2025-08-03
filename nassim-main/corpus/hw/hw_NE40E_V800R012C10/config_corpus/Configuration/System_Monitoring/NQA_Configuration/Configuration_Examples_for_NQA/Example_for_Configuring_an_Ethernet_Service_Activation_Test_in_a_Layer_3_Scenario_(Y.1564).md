Example for Configuring an Ethernet Service Activation Test in a Layer 3 Scenario (Y.1564)
==========================================================================================

This section provides an example for configuring an Ethernet service activation test in a Layer 3 scenario to check whether network performance meets SLAs.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172373156__fig_dc_vrp_nqa_cfg_006101), it is required that Ethernet frame transmission between DeviceB and DeviceC be checked to determine whether the performance parameters meet SLAs.

**Figure 1** Configuring an Ethernet service activation test in a Layer 3 scenario![](../../../../public_sys-resources/note_3.0-en-us.png) 

* In this example, interfaces 1 and 2 represent GE0/1/1 and GE0/1/2, respectively.

  
![](images/fig_dc_vrp_nqa_cfg_006001.png)

#### Configuration Roadmap

1. Configure DeviceC as the reflector and configure it to perform flow-based traffic filtering.
2. Configure DeviceB as the initiator and configure it to perform configuration and performance tests.

#### Data Preparation

To complete the configuration, you need the following data:

* Configurations on the reflector (DeviceC)
  + Service flow configurations and characteristics:
    - Destination MAC address: 00e0-fc12-3459 (MAC address of GE0/1/1 on DeviceD connected to UNI B)
    - Source MAC address: 00e0-fc12-3458 (MAC address of UNI B)
    - Destination IP address: IP address (10.1.3.2 used as an example) of the downstream device or an IP address on the network segment where UNI B resides
    - Source IP address: IP address (10.1.1.1 used as an example) of the downstream device or an IP address on the network segment where UNI A resides
* Configurations of the initiator (DeviceB)
  
  + Service flow configurations and characteristics:
    
    - Destination MAC address: 00e0-fc12-3457 (MAC address of UNI A)
    - Source MAC address: 00e0-fc12-3456 (MAC address of GE0/1/1 on DeviceA connected to UNI A)
    - Destination IP address: IP address (10.1.3.2 used as an example) of the downstream device or an IP address on the network segment where UNI B resides
    - Source IP address: IP address (10.1.1.1 used as an example) of the downstream device or an IP address on the network segment where UNI A resides
  + Bandwidth profile: 500000 Kbit/s for the CIR and 20000 kbit/s for the EIR
  + Service acceptance criteria: 1000/100000 for the FLR, 1 microsecond for the FTD, and 10000000 microseconds for the FDV

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The link between the two user networks must be reachable. Otherwise, static ARP entries must be configured.



#### Procedure

1. Configure Layer 3 link reachability for the initiator and reflector.
2. Configure the reflector.
   
   
   ```
   [*DeviceC] nqa test-flow 1
   ```
   ```
   [*DeviceC-nqa-testflow-1] vlan 10
   ```
   ```
   [*DeviceC-nqa-testflow-1] traffic-type mac destination 00e0-fc12-3459
   ```
   ```
   [*DeviceC-nqa-testflow-1] traffic-type mac source 00e0-fc12-3458
   ```
   ```
   [*DeviceC-nqa-testflow-1] traffic-type ipv4 destination 10.1.3.2
   ```
   ```
   [*DeviceC-nqa-testflow-1] traffic-type ipv4 source 10.1.1.1
   ```
   ```
   [*DeviceC-nqa-testflow-1] traffic-policing test enable
   ```
   ```
   [*DeviceC-nqa-testflow-1] quit
   ```
   ```
   [*DeviceC] nqa reflector 1 interface GigabitEthernet 0/1/1.1 test-flow 1 exchange-port agetime 0
   ```
   ```
   [*DeviceC] commit
   ```
3. Configure the initiator to perform configuration and performance tests and check the test results.
   
   
   ```
   [*DeviceB] nqa test-flow 1
   ```
   ```
   [*DeviceB-nqa-testflow-1] vlan 10
   ```
   ```
   [*DeviceB-nqa-testflow-1] bandwidth cir 500000 eir 20000
   ```
   ```
   [*DeviceB-nqa-testflow-1] sac flr 1000 ftd 10000 fdv 10000000
   ```
   ```
   [*DeviceB-nqa-testflow-1] traffic-type mac destination 00e0-fc12-3457
   ```
   ```
   [*DeviceB-nqa-testflow-1] traffic-type mac source 00e0-fc12-3456
   ```
   ```
   [*DeviceB-nqa-testflow-1] traffic-type ipv4 destination 10.1.3.2
   ```
   ```
   [*DeviceB-nqa-testflow-1] traffic-type ipv4 source 10.1.1.1
   ```
   ```
   [*DeviceB-nqa-testflow-1] traffic-policing test enable
   ```
   ```
   [*DeviceB-nqa-testflow-1] color-mode 8021p green 0 7 yellow 0 7
   ```
   ```
   [*DeviceB-nqa-testflow-1] quit
   ```
   ```
   [*DeviceB] nqa test-instance admin ethernet
   ```
   ```
   [*DeviceB-nqa-admin-ethernet] test-type ethernet-service
   ```
   ```
   [*DeviceB-nqa-admin-ethernet] forwarding-simulation inbound-interface GigabitEthernet 0/1/1.1
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
   ```
   [~DeviceB-nqa-admin-ethernet] display nqa results test-instance admin ethernet
   
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
        Min/Max/Mean IR(kbit/s)    : 9961/10075/10012                                
        Min/Max/Mean FTD(us)     : 99/111/104                                      
        Min/Max/Mean FDV(us)     : 0/7/3                                           
        FL Count/FLR             : 0/0.000%
        Disorder packets         : 0
        Unavail Count/AVAIL      : 0/0.000%                                        
       Test-flow 1, CIR/EIR test, Green                                            
        Begin                    : 2014-06-25 16:23:15.8                           
        End                      : 2014-06-25 16:23:18.8                           
        Status                   : Pass                                            
        Min/Max/Mean IR(kbit/s)    : 9979/10054/10012                                
        Min/Max/Mean FTD(us)     : 101/111/105                                     
        Min/Max/Mean FDV(us)     : 0/10/3                                          
        FL Count/FLR             : 0/0.000%
        Disorder packets         : 0
        Unavail Count/AVAIL      : 0/0.000%                                        
       Test-flow 1, CIR/EIR test, Yellow                                           
        Begin                    : 2014-06-25 16:23:15.8                           
        End                      : 2014-06-25 16:23:18.8                           
        Status                   : --                                              
        Min/Max/Mean IR(kbit/s)    : 9979/10057/10013                                
        Min/Max/Mean FTD(us)     : 98/111/104                                      
        Min/Max/Mean FDV(us)     : 1/11/5                                          
        FL Count/FLR             : 0/0.000%                                        
        Disorder packets         : 0
        Unavail Count/AVAIL      : 0/0.000%
       Test-flow 1, Traffic policing test, Green                                   
        Begin                    : 2014-06-25 16:23:45.8                           
        End                      : 2014-06-25 16:23:48.8                           
        Status                   : Pass                                            
        Min/Max/Mean IR(kbit/s)    : 10039/10054/10045                               
        Min/Max/Mean FTD(us)     : 96/110/104                                      
        Min/Max/Mean FDV(us)     : 1/9/4                                           
        FL Count/FLR             : 0/0.000% 
        Disorder packets         : 0
        Unavail Count/AVAIL      : 0/0.000%                                       
       Test-flow 1, Traffic policing test, Yellow                                  
        Begin                    : 2014-06-25 16:23:45.8                           
        End                      : 2014-06-25 16:23:48.8                           
        Status                   : --                                              
        Min/Max/Mean IR(kbit/s)    : 12544/12566/12554                               
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
        Min/Max/Mean IR(kbit/s)    : 9888/10132/10004                                
        Min/Max/Mean FTD(us)     : 101/111/105                                     
        Min/Max/Mean FDV(us)     : 0/8/2                                           
        FL Count/FLR             : 0/0.000%
        Disorder packets         : 0
        Unavail Count/AVAIL      : 0/0.000%
   ```

#### Configuration Files

* DeviceB configuration file
  
  ```
  #
  sysname DeviceB
  # 
  interface GigabitEthernet 0/1/1
   undo shutdown
  #
  interface GigabitEthernet 0/1/1.1
   vlan-type dot1q 10
   ip address 10.1.1.2 255.255.255.0
  #
  interface GigabitEthernet 0/1/2
   undo shutdown
   ip address 10.1.2.1 255.255.255.0
  #
  nqa test-flow 1
   vlan 10
   bandwidth cir 500000 eir 20000
   sac flr 1000 ftd 10000 fdv 10000000
   traffic-type mac destination 00e0-fc12-3457
   traffic-type mac source 00e0-fc12-3456
   traffic-type ipv4 destination 10.1.3.2 
   traffic-type ipv4 source 10.1.1.1 
   traffic-policing test enable
   color-mode 8021p green 0 7 yellow 0 7
  #
  nqa test-instance admin ethernet
   test-type ethernet-service
   forwarding-simulation inbound-interface GigabitEthernet 0/1/1.1
   test-flow 1
  #
  return
  ```
* DeviceC configuration file
  
  ```
  #
  sysname DeviceC
  # 
  interface GigabitEthernet 0/1/1
   undo shutdown
  #
  interface GigabitEthernet 0/1/1.1
   vlan-type dot1q 10
   ip address 10.1.3.1 255.255.255.0
  #
  interface GigabitEthernet 0/1/2
   undo shutdown
   ip address 10.1.2.2 255.255.255.0
  #
  nqa test-flow 1
   vlan 10
   traffic-type mac destination 00e0-fc12-3459
   traffic-type mac source 00e0-fc12-3458
   traffic-type ipv4 destination 10.1.3.2 
   traffic-type ipv4 source 10.1.1.1 
   traffic-policing test enable
  #
  nqa reflector 1 interface GigabitEthernet 0/1/1.1 test-flow 1 exchange-port agetime 0
  #
  return
  ```