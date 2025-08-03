Example for Configuring an Ethernet Service Activation Test in a Layer 2 Scenario (Y.1564)
==========================================================================================

This section provides an example for configuring an Ethernet service activation test in a Layer 2 scenario to check whether network performance meets SLAs.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172373153__fig_dc_vrp_nqa_cfg_006001), it is required that Ethernet frame transmission between DeviceB and DeviceC be checked to determine whether the performance parameters meet SLAs.

**Figure 1** Configuring an Ethernet service activation test in a Layer 2 scenario![](../../../../public_sys-resources/note_3.0-en-us.png) 

* In this example, interfaces 1 and 2 represent GE0/1/1 and GE0/1/2, respectively.

  
![](images/fig_dc_vrp_nqa_cfg_006001.png)  


#### Configuration Roadmap

1. Configure DeviceC as the reflector and configure it to perform flow-based traffic filtering, with the reflector interface being GE0/1/1.
2. Configure DeviceB as the initiator and configure it to perform configuration and performance tests.

#### Data Preparation

To complete the configuration, you need the following data:

* Configurations of the reflector (DeviceC): MAC address (00e0-fc12-3457) of GE0/1/1 on DeviceD connected to UNI B; the function to reflect packets based on flows
* Configurations of the initiator (DeviceB)
  
  + Service flow configurations and characteristics:
    
    - Destination MAC address: 00e0-fc12-3457 (MAC address of GE0/1/1 on DeviceD connected to UNI B)
    - Source MAC address: 00e0-fc12-3456 (MAC address of GE0/1/1 on DeviceA connected to UNI A)
    - VLAN ID in single-tagged Ethernet packets: 10
    - UDP destination port number: 1234
    - UDP source port number: 5678
  + Bandwidth profile: 10000 kbit/s for both the CIR and EIR
  + Service acceptance criteria: 1000/100000 for the FLR and 1000 microseconds for both the FTD and FDV
  + Enabling of the simple CIR test, traffic policing test, and color mode
  + Ethernet service activation test instance

#### Procedure

1. Configure a reachable link between the initiator and reflector and add Layer 2 interfaces to VLAN 10.
2. Configure the reflector.
   
   
   ```
   [*DeviceC] nqa test-flow 1
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
   [*DeviceC-nqa-testflow-1] traffic-type mac destination 00e0-fc12-3457
   ```
   ```
   [*DeviceC-nqa-testflow-1] traffic-type mac source 00e0-fc12-3456
   ```
   ```
   [*DeviceC-nqa-testflow-1] quit
   ```
   ```
   [*DeviceC] nqa reflector 1 interface GigabitEthernet 0/1/1 test-flow 1 exchange-port agetime 0
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
   [*DeviceB-nqa-testflow-1] traffic-type mac destination 00e0-fc12-3457
   ```
   ```
   [*DeviceB-nqa-testflow-1] traffic-type mac source 00e0-fc12-3456
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
   [*DeviceB-nqa-admin-ethernet] forwarding-simulation inbound-interface GigabitEthernet 0/1/1
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

* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  # 
  vlan batch 10
  #
  interface GigabitEthernet 0/1/1
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 10
  #
  return
  ```
* DeviceB configuration file
  
  ```
  #
  sysname DeviceB
  # 
  vlan batch 10
  #
  interface GigabitEthernet 0/1/1
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 10
  #
  interface GigabitEthernet 0/1/2
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 10
  #
  nqa test-flow 1
   vlan 10
   udp destination-port 1234
   udp source-port 5678
   cir simple-test enable
   bandwidth cir 10000 eir 10000
   sac flr 1000 ftd 1000 fdv 1000
   traffic-type mac destination 00e0-fc12-3457
   traffic-type mac source 00e0-fc12-3456
   traffic-policing test enable
   color-mode 8021p green 0 7 yellow 0 7
  #
  nqa test-instance admin ethernet
   test-type ethernet-service
   forwarding-simulation inbound-interface GigabitEthernet 0/1/1
   test-flow 1
  #
  return
  ```
* DeviceC configuration file
  
  ```
  #
  sysname DeviceC
  #
  vlan batch 10
  #
  interface GigabitEthernet 0/1/1
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 10
  #
  interface GigabitEthernet 0/1/2
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 10
  #
  nqa test-flow 1
   vlan 10
   udp destination-port 1234
   udp source-port 5678
   traffic-type mac destination 00e0-fc12-3457
   traffic-type mac source 00e0-fc12-3456
  #
  nqa reflector 1 interface GigabitEthernet 0/1/1 test-flow 1 exchange-port agetime 0
  #
  return
  ```
* DeviceD configuration file
  
  ```
  #
  sysname DeviceD
  # 
  vlan batch 10
  #
  interface GigabitEthernet 0/1/1
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 10
  #
  return
  ```