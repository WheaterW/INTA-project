Example for Configuring HQoS in Common 8-CoS Mode
=================================================

This section provides an example for configuring HQoS in common 8-CoS mode so that different service traffic is transmitted through different sub-interfaces.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172371575__fig_dc_ne_qos_cfg_504301), users need to access the device through the DSLAM. The device functions as the access device of the backbone network.

Three types of services of the users are to be mapped to three PVCs of the DSLAM. The traffic flows of the same user access the device through sub-interfaces GE 0/1/0.1, GE 0/1/0.2, and GE 0/1/0.3, respectively, with different types of traffic flowing through different sub-interfaces. When reaching the device, traffic flows carry double tags. The inner tag indicates the user, and the outer tag indicates the service type. Uniform scheduling of user traffic needs to be implemented with 100 Mbit/s assured bandwidth. The bandwidth for EF flows should be 30 Mbit/s, and the bandwidth for AF1 flows should be 10 Mbit/s. The bandwidth for the user group to which the users belong should be 500 Mbit/s. On the downstream interface of the device, the traffic rate of EF flows should not be higher than 120 Mbit/s.

The VLAN tags marked for services are as follows:

* PC: The outer VLAN tag is 1; the inner VLAN tag is 1 to 100.
* VoIP: The outer VLAN tag is 2; the inner VLAN tag is 1 to 100.
* IPTV: The outer VLAN tag is 3; the inner VLAN tag is 1 to 100.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Sub-interfaces 1.1, sub-interface 2.1, subinterface 3.1, and interface 2 in this example represent GE 0/1/0.1, GE 0/1/0.2, GE 0/1/0.3, and GE 0/2/0, respectively.


**Figure 1** Network diagram of configuring HQoS in common 8-CoS mode  
![](images/fig_dc_ne_qos_cfg_504301.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure packet drop parameters for a flow WRED object.
2. Configure scheduling algorithms and parameters for FQs.
3. Configure a shaping value for a GQ.
4. Configure a network header length for a service profile.
5. Configure user-queue scheduling parameters for a QoS profile.
6. Configure packet drop parameters for a port WRED object.
7. Configure PQs on the downstream interface of the device.

#### Data Preparation

To complete the configuration, you need the following data:

* Packet drop parameters for flow WRED
* Scheduling algorithms and parameters for FQs
* Shaping value for a GQ
* CIR, PIR, and network header length for user-queue in the QoS profile
* Interface to which the QoS profile is applied
* Port WRED parameters that are referenced by port-queue
* Scheduling algorithms, related parameters, and shaping values for port-queue

#### Procedure

1. Configure a flow WRED object.
   
   
   
   # Configure packet drop parameters for flow WRED.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] flow-wred test
   ```
   ```
   [*HUAWEI-flow-wred-test] color green low-limit 70 high-limit 100 discard-percentage 100
   ```
   ```
   [*HUAWEI-flow-wred-test] color yellow low-limit 60 high-limit 90 discard-percentage 100 
   ```
   ```
   [*HUAWEI-flow-wred-test] color red low-limit 50 high-limit 80 discard-percentage 100 
   ```
   ```
   [*HUAWEI-flow-wred-test] commit
   ```
   ```
   [~HUAWEI-flow-wred-test] return
   ```
   
   After the preceding configuration, you can run the **display flow-wred configuration verbose** command to view the configured parameters of the flow WRED object.
   
   ```
   <HUAWEI> display flow-wred configuration verbose test
   ```
   ```
   Flow wred name : test
   ---------------------------------------------------
   Color    Low-limit    High-limit    Discard-percent
   ---------------------------------------------------
   green    70           100           100
   yellow   60           90            100
   red      50           80            100
   
   ```
   ```
   Queue Depth(kbytes) : 1000   
   ```
   ```
   Reference relationships : NULL        
   ```
2. Configure scheduling algorithms and parameters for FQs.
   
   
   
   # Configure scheduling algorithms, WRED parameters, and shaping values for FQs.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] flow-queue test
   ```
   ```
   [*HUAWEI-flow-queue-template-test] queue af1 lpq flow-wred test shaping 10000
   ```
   ```
   [*HUAWEI-flow-queue-template-test] queue ef pq flow-wred test shaping 30000
   ```
   ```
   [*HUAWEI-flow-queue-template-test] commit
   ```
   ```
   [~HUAWEI-flow-queue-template-test] return
   ```
   
   After the preceding configuration, you can run the **display flow-queue configuration verbose** command to view the configuration of the FQ profile.
   
   ```
   <HUAWEI> display flow-queue configuration verbose test 
   ```
   ```
   Codes: Arith(Schedule algorithm)
          U-Weight(Schedule weight configured by users)
          I-Weight(Inverse schedule weight used by TM)
          A-Weight(Actual schedule weight obtained by users)
          Shp(Shaping value)
          Pct(The percentage of subscriber queue's PIR)
          Drop-Arith(The name of the WRED object used by the flow queue)
   
   Flow Queue Template : test
   ------------------------------------------------------------------
   Cos  Arith  U-Weight  I-Weight  A-Weight  Shp      Pct  Drop-Arith
   ------------------------------------------------------------------
   be   wfq    10        3         10.00     -        -    Tail Drop
   af1  lpq    -         -         -         10000    -    test
   af2  wfq    10        3         10.00     -        -    Tail Drop
   af3  wfq    15        2         15.00     -        -    Tail Drop
   af4  wfq    15        2         15.00     -        -    Tail Drop
   ef   pq     -         -         -         30000    -    test
   cs6  pq     -         -         -         -        -    Tail Drop
   cs7  pq     -         -         -         -        -    Tail Drop
   Reference relationships : NULL    
   ```
3. Configure a shaping value for a GQ.
   
   
   
   # Configure a GQ.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] user-group-queue test
   ```
   ```
   [*HUAWEI-user-group-queue-test-slot-all] shaping 500000 inbound
   ```
   ```
   [*HUAWEI-user-group-queue-test-slot-all] commit
   ```
   ```
   [~HUAWEI-user-group-queue-test-slot-all] return
   ```
   
   After the preceding configuration, you can run the **display user-group-queue configuration verbose** command to view the configuration and the reference relationship of the GQ.
   
   ```
   <HUAWEI> display user-group-queue configuration verbose test
   ```
   ```
   user-group-queue-name : test
   ```
   ```
    slot : all
   ```
   ```
    [current configuration]
   ```
   ```
     inbound
   ```
   ```
      shaping-value <kbps> : 500000
   ```
   ```
      pbs-value <byte> : 524288
   ```
   ```
     outbound
   ```
   ```
      shaping-value <kbps> : NA
   ```
   ```
      pbs-value <byte> : NA
   ```
   ```
      weight-value : NA
   ```
   ```
    [reference relationship]
   ```
4. Configure a network header length for a service profile.
   
   
   
   # Create a service profile and configure a network header length for it.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] service-template test
   ```
   ```
   [*HUAWEI-service-template-test-slot-all] network-header-length 12 inbound
   ```
   ```
   [*HUAWEI-service-template-test-slot-all] commit
   ```
   ```
   [~HUAWEI-service-template-test-slot-all] return
   ```
   After the preceding configuration, you can run the **display service-template configuration verbose** command to view the configuration, network header length, and reference relationship of the service profile.
   ```
   <HUAWEI> display service-template configuration verbose
   ```
   ```
   [service-template detail information]
   total number : 1
   slot all     : 1
   
   service-template-name : test
    slot : all
    [current configuration]
     inbound network-header-length: 12
   
     outbound network-header-length: NA
   
    [reference relationship]
     NULL
   ```
5. Configure scheduling parameters for a QoS profile and apply it to interfaces.
   
   
   
   # Configure user-queue scheduling parameters for a QoS profile.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] qos-profile test
   ```
   ```
   [*HUAWEI-qos-profile-test] user-queue cir 100000 flow-queue test user-group-queue test service-template test
   ```
   ```
   [*HUAWEI-qos-profile-test] commit
   ```
   ```
   [~HUAWEI-qos-profile-test] return
   ```
   
   # Create QinQ VLAN tag termination sub-interfaces GE 0/1/0.1, GE 0/1/0.2, and GE 0/1/0.3, and apply the QoS profile to them.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] interface gigabitethernet 0/1/0.1
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/0.1] control-vid 1 qinq-termination
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/0.1] qinq termination pe-vid 1 ce-vid 1 to 100 
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/0.1] ip address 10.10.1.1 24
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/0.1] qos-profile test inbound pe-vid 1 ce-vid 1 to 100 identifier ce-vid group group1
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/0.1] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [~HUAWEI] interface gigabitethernet 0/1/0.2
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/0.2] control-vid 2 qinq-termination
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/0.2] qinq termination pe-vid 2 ce-vid 1 to 100
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/0.2] ip address 10.10.2.1 24
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/0.2] qos-profile test inbound pe-vid 2 ce-vid 1 to 100 identifier ce-vid group group1
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/0.2] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0.2] quit
   ```
   ```
   [~HUAWEI] interface gigabitethernet 0/1/0.3
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/0.3] control-vid 3 qinq-termination
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/0.3] qinq termination pe-vid 3 ce-vid 1 to 100 
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/0.3] ip address 10.10.3.1 24
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/0.3] qos-profile test inbound pe-vid 3 ce-vid 1 to 100 identifier ce-vid group group1
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/0.3] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0.3] return
   ```
   
   After the preceding configuration, you can run the [**display qos-profile configuration**](cmdqueryname=display+qos-profile+configuration) *qos-profile-name* and [**display qos-profile application**](cmdqueryname=display+qos-profile+application) *profile-name* commands to view the configuration and application of the QoS profile.
   
   ```
   <HUAWEI> display qos-profile configuration test
   ```
   ```
   qos-profile: test 
   inbound: 
   outbound: 
   both: 
   user-queue cir 100000 pir 100000 flow-queue test user-group-queue test service-template test 
   ```
   ```
   <HUAWEI>  display qos-profile application test
   ```
   ```
   qos-profile test: 
   GigabitEthernet0/1/0.1 
   GigabitEthernet0/1/0.2 
   GigabitEthernet0/1/0.3 
   Reference number by access user: [inbound] 0, [outbound] 0
   Reference number by VNI: [inbound] 0, [outbound] 0
   ```
6. Configure a port WRED object.
   
   
   
   # Configure packet drop parameters for port WRED.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] port-wred test
   ```
   ```
   [*HUAWEI-port-wred-test] color green low-limit 70 high-limit 100 discard-percentage 100
   ```
   ```
   [*HUAWEI-port-wred-test] color yellow low-limit 60 high-limit 90 discard-percentage 100
   ```
   ```
   [*HUAWEI-port-wred-test] color red low-limit 50 high-limit 80 discard-percentage 100
   ```
   ```
   [*HUAWEI-port-wred-test] commit
   ```
   ```
   [~HUAWEI-port-wred-test] return
   ```
   
   After the preceding configuration, you can run the **display port-wred configuration verbose** command to view the configuration of the port WRED object.
   
   ```
   <HUAWEI> display port-wred configuration verbose test
   ```
   ```
   Port wred name : test
   ---------------------------------------------------
   Color    Low-limit    High-limit    Discard-percent
   ---------------------------------------------------
   green    70           100           100
   yellow   60           90            100
   red      50           80            100
   Queue Depth(kbytes) : 8000 
   Reference relationships : NULL  
   ```
7. Configure a PQ.
   
   
   
   # Configure a scheduling algorithm, WRED parameter, and shaping value for a PQ.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] interface gigabitethernet 0/2/0
   ```
   ```
   [~HUAWEI-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [*HUAWEI-GigabitEthernet0/2/0] port-queue ef pq shaping 120 port-wred test outbound
   ```
   ```
   [*HUAWEI-GigabitEthernet0/2/0] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/2/0] return
   ```
   
   After the preceding configuration, you can run the **display port-queue configuration interface** command to view the configuration of the PQ.
   
   ```
   <HUAWEI> display port-queue configuration interface gigabitethernet 0/2/0 outbound
   ```
   ```
   GigabitEthernet0/2/0 outbound current port-queue configuration:  
    be : arithmetic: wfq                weight: 10         tm weight: 3                       
          fact weight: 10.00             shaping(kbps): NA                                   
          port-wred: NA                                                                                                                
            green (low-high limit) (kbytes)                  12800 - 12800                                                            
            yellow(low-high limit) (kbytes)                  12800 - 12800                                                             
            red   (low-high limit) (kbytes)                  12800 - 12800                                                             
          current queue-length     (kbytes)                  12800                                                                     
          cir:123                        cir-percentage:NA
          cir-arithmetic:pq              cir-weight:NA
          pir:123                        pir-percentage:NA
          pir-arithmetic:lpq             pir-weight:NA      
    af1: arithmetic: wfq                weight: 10         tm weight: 3                                                               
          fact weight: 10.00             shaping(kbps): NA                                                                             
          port-wred: NA                                                                                                                
            green (low-high limit) (kbytes)                  12800 - 12800                                                             
            yellow(low-high limit) (kbytes)                  12800 - 12800                                                             
            red   (low-high limit) (kbytes)                  12800 - 12800                                                             
          current queue-length     (kbytes)                  12800                                                                     
          cir:NA                         cir-percentage:10
          cir-arithmetic:pq              cir-weight:NA
          pir:NA                         pir-percentage:20
          pir-arithmetic:wfq             pir-weight:15    
    af2: arithmetic: wfq                weight: 10         tm weight: 3                                                               
          fact weight: 10.00             shaping(kbps): NA                                                                             
          port-wred: NA                                                                                                                
            green (low-high limit) (kbytes)                  12800 - 12800                                                             
            yellow(low-high limit) (kbytes)                  12800 - 12800                                                             
            red   (low-high limit) (kbytes)                  12800 - 12800                                                             
          current queue-length     (kbytes)                  12800                                                                     
          cir:NA                         cir-percentage:NA
          cir-arithmetic:NA              cir-weight:NA
          pir:NA                         pir-percentage:NA
          pir-arithmetic:NA              pir-weight:NA 
    af3: arithmetic: wfq                weight: 15         tm weight: 2                                                               
          fact weight: 15.00             shaping(kbps): NA                                                                             
          port-wred: NA                                                                                                                
            green (low-high limit) (kbytes)                  12800 - 12800                                                             
            yellow(low-high limit) (kbytes)                  12800 - 12800                                                             
            red   (low-high limit) (kbytes)                  12800 - 12800                                                            
          current queue-length     (kbytes)                  12800                                                                     
          cir:NA                         cir-percentage:NA
          cir-arithmetic:NA              cir-weight:NA
          pir:NA                         pir-percentage:NA
          pir-arithmetic:NA              pir-weight:NA 
    af4: arithmetic: wfq                weight: 15         tm weight: 2                                                               
          fact weight: 15.00             shaping(kbps): NA                                                                             
          port-wred: NA                                                                                                                
            green (low-high limit) (kbytes)                  12800 - 12800                                                             
            yellow(low-high limit) (kbytes)                  12800 - 12800                                                             
            red   (low-high limit) (kbytes)                  12800 - 12800                                                             
          current queue-length     (kbytes)                  12800                                                                     
          cir:NA                         cir-percentage:NA
          cir-arithmetic:NA              cir-weight:NA
          pir:NA                         pir-percentage:NA
          pir-arithmetic:NA              pir-weight:NA 
    ef : arithmetic: pq                 weight: NA         tm weight: 0                                                               
          fact weight: 0.00              shaping(kbps): NA                                                                             
          port-wred: NA                                                                                                                
            green (low-high limit) (kbytes)                  1280 - 1280                                                               
            yellow(low-high limit) (kbytes)                  1280 - 1280                                                               
            red   (low-high limit) (kbytes)                  1280 - 1280                                                               
          current queue-length     (kbytes)                  1280                                                                      
          cir:NA                         cir-percentage:NA
          cir-arithmetic:NA              cir-weight:NA
          pir:NA                         pir-percentage:NA
          pir-arithmetic:NA              pir-weight:NA 
    cs6: arithmetic: pq                 weight: NA         tm weight: 0                                                               
          fact weight: 0.00              shaping(kbps): NA                                                                             
          port-wred: NA                                                                                                                
            green (low-high limit) (kbytes)                  1280 - 1280                                                               
            yellow(low-high limit) (kbytes)                  1280 - 1280                                                               
            red   (low-high limit) (kbytes)                  1280 - 1280                                                               
          current queue-length     (kbytes)                  1280                                                                      
          cir:NA                         cir-percentage:NA
          cir-arithmetic:NA              cir-weight:NA
          pir:NA                         pir-percentage:NA
          pir-arithmetic:NA              pir-weight:NA 
    cs7: arithmetic: pq                 weight: NA         tm weight: 0                                                               
          fact weight: 0.00              shaping(kbps): NA                                                                             
          port-wred: NA                                                                                                                
            green (low-high limit) (kbytes)                  1280 - 1280                                                               
            yellow(low-high limit) (kbytes)                  1280 - 1280                                                               
            red   (low-high limit) (kbytes)                  1280 - 1280                                                               
          current queue-length     (kbytes)                  1280                                                                      
          cir:NA                         cir-percentage:NA
          cir-arithmetic:NA              cir-weight:NA
          pir:NA                         pir-percentage:NA
          pir-arithmetic:NA              pir-weight:NA
   ```
8. Verify the configuration.
   
   
   
   When there are flows on the network, you can observe that packets of user 1's AF1 and EF flows and user 2's EF flows are forwarded at the assured bandwidth.
   
   Running the **display port-queue statistics** command on the downstream interface GE 0/2/0 of the device, you can see that EF packets increase rapidly.
   
   ```
   <HUAWEI> display port-queue statistics interface gigabitethernet 0/2/0 ef outbound
   ```
   ```
   GigabitEthernet0/2/0 outbound traffic statistics:                            
   [ef]
     Current usage percentage of queue: 10  
     Total pass:
                              5,097,976 packets,                458,817,750 bytes
     Total discard:
                                      0 packets,                          0 bytes
       Drop tail discard:
                                      0 packets,                          0 bytes
       Wred discard:
                                      0 packets,                          0 bytes
     Last 30 seconds pass rate:
                                 12,030 pps,                      8,661,600 bps
     Last 30 seconds discard rate:
                                      0 pps,                              0 bps
       Drop tail discard rate:
                                      0 pps,                              0 bps
       Wred discard rate:
                                      0 pps,                              0 bps    
     buffer size:                    10 kbytes   
     used buffer size:                0 kbytes   
     Peak rate:                                                                    
                             2013-11-17 13:15:18                          8,661,600 bps 
   ```

#### Configuration Files

* HUAWEI configuration file
  
  ```
  #
  ```
  ```
  flow-wred test
  ```
  ```
   color green low-limit 70 high-limit 100 discard-percentage 100
  ```
  ```
   color yellow low-limit 60 high-limit 90 discard-percentage 100
  ```
  ```
   color red low-limit 50 high-limit 80 discard-percentage 100
  ```
  ```
  #
  ```
  ```
  flow-queue test
  ```
  ```
   queue af1 lpq shaping 10000 flow-wred test
  ```
  ```
   queue ef pq shaping 30000 flow-wred test
  ```
  ```
  #
  ```
  ```
  user-group-queue test
  ```
  ```
   shaping 500000 inbound
  ```
  ```
  #
  ```
  ```
  service-template test
  ```
  ```
   network-header-length 12 inbound
  ```
  ```
  #
  ```
  ```
  qos-profile test
  ```
  ```
   user-queue cir 100000 pir 100000 flow-queue test user-group-queue test service-template test  
  ```
  ```
  #
  ```
  ```
  port-wred test
  ```
  ```
   color green low-limit 70 high-limit 100 discard-percentage 100
  ```
  ```
   color yellow low-limit 60 high-limit 90 discard-percentage 100
  ```
  ```
   color red low-limit 50 high-limit 80 discard-percentage 100
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0.1  
  ```
  ```
   encapsulation qinq-termination
  ```
  ```
   qinq termination pe-vid 1 ce-vid 1 to 100 
  ```
  ```
   ip address 10.10.1.1 255.255.255.0
  ```
  ```
   qos-profile test inbound pe-vid 1 ce-vid 1 to 100 identifier ce-vid group group1
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0.2 
  ```
  ```
   encapsulation qinq-termination
  ```
  ```
   qinq termination pe-vid 2 ce-vid 1 to 100 
  ```
  ```
   ip address 10.10.2.1 255.255.255.0
  ```
  ```
   qos-profile test inbound pe-vid 2 ce-vid 1 to 100 identifier ce-vid group group1
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0.3 
  ```
  ```
   encapsulation qinq-termination
  ```
  ```
   qinq termination pe-vid 3 ce-vid 1 to 100 
  ```
  ```
   ip address 10.10.3.1 255.255.255.0
  ```
  ```
   qos-profile test inbound pe-vid 3 ce-vid 1 to 100 identifier ce-vid group group1
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
   ip address 10.20.1.1 255.255.255.0
  ```
  ```
   port-queue ef pq shaping 120 port-wred test outbound
  ```
  ```
  #
  ```
  ```
  ospf 10
  ```
  ```
   area 0.0.0.0
  ```
  ```
   network 10.20.1.0 0.0.0.255
  ```
  ```
   network 10.10.1.0 0.0.0.255
  ```
  ```
   network 10.10.2.0 0.0.0.255
  ```
  ```
   network 10.10.3.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  return
  ```