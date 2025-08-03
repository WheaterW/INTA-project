Example for Configuring NQA to Measure the VoIPv6 Service Jitter
================================================================

This section provides an example for configuring an NQA UDP jitter test instance to measure the Voice over IPv6 (VoIPv6) service jitter.

#### Networking Requirements

On the network shown in [Figure 1](dc_vrp_nqa_cfg_0028.html#EN-US_TASK_0172373137__fig_dc_vrp_nqa_cfg_002801), the headquarters often holds teleconferences with its subsidiary through VoIPv6. It is required that the round-trip delay be less than 250 ms and the jitter be less than 20 ms. An NQA UDP jitter test can be configured to simulate a VoIPv6 service and measure the service jitter.

**Figure 1** Configuring NQA to measure the VoIPv6 service jitter![](../../../../public_sys-resources/note_3.0-en-us.png) 

* In this example, interface1 represents GE0/1/0.

  
![](images/fig_dc_vrp_nqa_cfg_007001.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure DeviceD as the NQA client and DeviceA as the NQA server. Configure a UDP jitter test instance on DeviceD.
2. Start the test instance.

#### Data Preparation

To complete the configuration, you need the following data:

* IPv6 addresses of DeviceA and DeviceD
* Code type of the simulated VoIPv6 service

#### Procedure

1. Configure DeviceA (NQA server).
   
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] nqa-server udpecho ipv6 2001:db8:1::1 4000
   ```
   ```
   [*DeviceA] commit
   ```
2. Configure DeviceD (NQA client).
   1. Configure a packet version for the UDP jitter test instance to be created.
      
      
      ```
      <DeviceD> system-view
      ```
      ```
      [~DeviceD] nqa-jitter tag-version 2
      ```
   2. Create a UDP jitter test instance and set the destination address of the test instance to the IPv6 address of DeviceA.
      
      
      ```
      [*DeviceD] nqa test-instance admin udpjitter
      ```
      ```
      [*DeviceD-nqa-admin-udpjitter] test-type jitter
      ```
      ```
      [*DeviceD-nqa-admin-udpjitter] destination-address ipv6 2001:db8:1::1
      ```
      ```
      [*DeviceD-nqa-admin-udpjitter] destination-port 4000
      ```
   3. Specify a code type for the simulated VoIPv6 service.
      
      
      ```
      [*DeviceD-nqa-admin-udpjitter] jitter-codec g711a
      ```
3. Start the test instance.
   
   
   ```
   [*DeviceD-nqa-admin-udpjitter] start now
   ```
   ```
   [*DeviceD-nqa-admin-udpjitter] commit
   ```
4. Verify the test result. The command output shows that the round-trip delay is less than 250 ms, and the jitter is less than 20 ms.
   
   
   ```
   [~DeviceD-nqa-admin-udpjitter] display nqa results test-instance admin udpjitter
   ```
   ```
   NQA entry(admin, udpjitter) :testflag is active ,testtype is jitter             
     1 . Test 1 result   The test is finished                                      
      SendProbe:1000                         ResponseProbe:919                     
      Completion:success                     RTD OverThresholds number:0           
      OWD OverThresholds SD number:0         OWD OverThresholds DS number:0        
      Min/Max/Avg/Sum RTT:1/408/5/4601       RTT  Square Sum:1032361               
      NumOfRTT:919                           Drop operation number:0               
      Operation sequence errors number:0     RTT Stats errors number:0             
      System busy operation number:0         Operation timeout number:81           
      Min Positive SD:1                      Min Positive DS:1                     
      Max Positive SD:2                      Max Positive DS:9                     
      Positive SD Number:67                  Positive DS Number:70                 
      Positive SD Sum:70                     Positive DS Sum:80                    
      Positive SD Square Sum:76              Positive DS Square Sum:156            
      Min Negative SD:1                      Min Negative DS:1                     
      Max Negative SD:24                     Max Negative DS:25                    
      Negative SD Number:72                  Negative DS Number:82                 
      Negative SD Sum:271                    Negative DS Sum:287                   
      Negative SD Square Sum:4849            Negative DS Square Sum:4937           
      Min Delay SD:0                         Min Delay DS:0                        
      Max Delay SD:203                       Max Delay DS:204                      
      Delay SD Square Sum:254974             Delay DS Square Sum:257072            
      Packet Loss SD:0                       Packet Loss DS:0                      
      Packet Loss Unknown:81                 Average of Jitter:2                   
      Average of Jitter SD:2                 Average of Jitter DS:2                
      jitter out value:0.0000000             jitter in value:0.0000000             
      NumberOfOWD:919                        Packet Loss Ratio:8 %                 
      OWD SD Sum:1834                        OWD DS Sum:1848                       
      ICPIF value:23                         MOS-CQ value:354                      
      TimeStamp unit:ms       
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
   nqa-server udpecho ipv6 2001:db8:1::1 4000
  ```
  ```
  #
  ```
  ```
  isis 1
   network-entity 00.0000.0000.0001.00  
  #
  ```
  ```
   interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ipv6 address 2001:db8:1::1/128
   isis enable 1 
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
  nqa-jitter tag-version 2
  ```
  ```
  #
  ```
  ```
  isis 1
   network-entity 00.0000.0000.0001.00  
  #
  ```
  ```
   interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ipv6 address 2001:db8:2::1/128
   isis enable 1 
  ```
  ```
  #
  ```
  ```
  nqa test-instance admin udpjitter
   test-type jitter
   destination-address ipv6 2001:db8:1::1
   destination-port 4000
   jitter-codec g711a
  ```
  ```
  #
  ```
  ```
  return
  ```