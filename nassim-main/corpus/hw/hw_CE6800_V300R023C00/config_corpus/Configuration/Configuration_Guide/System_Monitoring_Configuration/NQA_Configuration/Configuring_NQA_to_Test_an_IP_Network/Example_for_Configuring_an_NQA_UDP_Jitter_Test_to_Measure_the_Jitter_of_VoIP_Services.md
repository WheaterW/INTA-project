Example for Configuring an NQA UDP Jitter Test to Measure the Jitter of VoIP Services
=====================================================================================

Example for Configuring an NQA UDP Jitter Test to Measure the Jitter of VoIP Services

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001176661847__fig_dc_vrp_nqa_cfg_002801), the headquarters and its subsidiary need to communicate with each other across an external network. DeviceA and DeviceD are egress devices of the headquarters and subsidiary, respectively. DeviceB and DeviceC are edge devices of the external network.

The headquarters and its subsidiary often need to hold teleconferences through VoIP. The RTT must be less than 250 ms, and the jitter must be less than 20 ms. A UDP jitter test instance can be configured on DeviceD to measure the jitter of VoIP services.

**Figure 1** Network diagram for an NQA UDP jitter test to monitor the jitter of VoIP service jitters![](../public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE 1/0/1 and 100GE 1/0/2, respectively.


  
![](figure/en-us_image_0000001130622322.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure DeviceA as the NQA server and DeviceD as the NQA client, and create a UDP jitter test instance on DeviceD.
2. Start the test instance.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of DeviceA and DeviceD
* Codec for simulated VoIP services

#### Procedure

1. Configure DeviceA as the NQA server.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] nqa server udpecho 10.1.1.1 4000
   ```
2. Configure DeviceD as the NQA client.
   1. Configure the packet version for the test instance.
      
      
      ```
      <HUAWEI> system-view
      [~HUAWEI] sysname DeviceD
      [*HUAWEI] commit
      [~DeviceD] nqa jitter tag-version 2
      ```
   2. Create a UDP jitter test instance and set the destination IP address to the IP address of DeviceA.
      
      
      ```
      [*DeviceD] nqa test-instance admin udpjitter
      [*DeviceD-nqa-admin-udpjitter] test-type jitter
      [*DeviceD-nqa-admin-udpjitter] destination-address ipv4 10.1.1.1
      [*DeviceD-nqa-admin-udpjitter] destination-port 4000
      ```
   3. Specify the codec for simulated VoIP services.
      
      
      ```
      [*DeviceD-nqa-admin-udpjitter] jitter-codec g711a
      ```
3. Start the test instance immediately.
   
   
   ```
   [*DeviceD-nqa-admin-udpjitter] start now
   [*DeviceD-nqa-admin-udpjitter] commit
   ```

#### Verifying the Configuration

Verify the test result. The command output indicates that the RTT is less than 250 ms, and the jitter is less than 20 ms.

```
[~DeviceD-nqa-admin-udpjitter] display nqa results test-instance admin udpjitter

NQA entry(admin, udpjitter): test flag is active, test type is JITTER
  1 . Test 1 result   The test is finished
   SendProbe: 1000                         ResponseProbe: 919                      
   Completion: success                     RTD over thresholds number: 0           
   OWD over thresholds SD number: 0        OWD over thresholds DS number: 0        
   Min/Max/Avg/Sum RTT: 1/408/5/4601       RTT square sum: 1032361                  
   Num of RTT: 919                         Drop operation number: 0               
   Operation sequence errors number: 0     RTT Stats errors number: 0             
   System busy operation number: 0         Operation timeout number: 81            
   Min positive SD: 1                      Min positive DS: 1                     
   Max positive SD: 2                      Max positive DS: 9                    
   Positive SD number: 67                  Positive DS number: 70                 
   Positive SD sum: 70                     Positive DS sum: 80                  
   Positive SD square sum: 76              Positive DS square sum: 156          
   Min negative SD: 1                      Min negative DS: 1                     
   Max negative SD: 24                     Max negative DS: 25                     
   Negative SD number: 72                  Negative DS number: 82                  
   Negative SD sum: 271                    Negative DS sum: 287                    
   Negative SD square sum: 4849            Negative DS square sum: 4937             
   Min delay SD: 0                         Min delay DS: 0                        
   Avg delay SD: 7                         Avg delay DS: 0                        
   Max delay SD: 203                       Max delay DS: 204                        
   Delay SD square sum: 254974             Delay DS square sum: 257072                 
   Packet loss SD: 0                       Packet loss DS: 0                      
   Packet loss unknown: 81                 Average of jitter: 2                  
   Average of jitter SD: 2                 Average of jitter DS: 2               
   Jitter out value: 0.0000000             Jitter in value: 0.0000000            
   Number of OWD: 919                      Packet loss ratio: 8 %                 
   OWD SD sum: 1834                        OWD DS sum: 1848                          
   ICPIF value: 23                         MOS-CQ value: 354                        
   TimeStamp unit: ms
```

#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  vlan batch 100
  #
  interface Vlanif100
   ip address 10.1.1.1 255.255.255.0
  #
  nqa server udpecho 10.1.1.1 4000
  #
  isis 1
   network-entity 00.0000.0000.0001.00
  #
  interface 100GE1/0/1
   port link-type trunk
   port trunk allow-pass vlan 100
   isis enable 1
  #
  return
  ```
* DeviceD
  
  ```
  #
  sysname DeviceD
  #
  vlan batch 100
  #
  interface Vlanif100
   ip address 10.2.2.1 255.255.255.0
  #
  nqa jitter tag-version 2
  #
  isis 1
   network-entity 00.0000.0000.0002.00
  #
  interface 100GE1/0/1
   port link-type trunk
   port trunk allow-pass vlan 100
   isis enable 1
  #
  nqa test-instance admin udpjitter
   test-type jitter
   destination-address ipv4 10.1.1.1
   destination-port 4000
   jitter-codec g711a
  #
  return
  ```