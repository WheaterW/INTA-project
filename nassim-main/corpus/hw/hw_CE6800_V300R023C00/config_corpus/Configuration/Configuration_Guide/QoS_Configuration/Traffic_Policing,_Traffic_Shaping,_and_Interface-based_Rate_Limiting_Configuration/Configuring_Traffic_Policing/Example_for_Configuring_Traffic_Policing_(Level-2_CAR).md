Example for Configuring Traffic Policing (Level-2 CAR)
======================================================

Example for Configuring Traffic Policing (Level-2 CAR)

#### Networking Requirements

![](public_sys-resources/note_3.0-en-us.png) 

This example is not supported by the CE6885-LL (low latency mode).

In [Figure 1](#EN-US_TASK_0000001967049892__fig_dc_cfg_qos_012902), DeviceB is connected to DeviceC through interface 2, and the enterprise can access the network through DeviceB and DeviceC.

**Figure 1** Network diagram for configuring traffic policing (level-2 CAR)![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE 1/0/1 and 100GE 1/0/2, respectively.


  
![](figure/en-us_image_0000001966901386.png)

On this network, the network-side bandwidth is lower than the enterprise's LAN bandwidth. As a result, network congestion may occur on network-side interfaces, causing data loss. Therefore, the total egress bandwidth needs to be limited to 12000 kbit/s. In addition, traffic policing needs to be performed on voice, video, and data services to limit the traffic rates within proper ranges.

Voice, video, and data services are transmitted in VLAN 10, VLAN 30, and VLAN 20 respectively, and have different QoS requirements in descending order of priority. Therefore, DeviceB needs to re-mark DSCP priorities of different service packets so that DeviceC can process the packets based on their priorities, ensuring QoS.

[Table 1](#EN-US_TASK_0000001967049892__tab_dc_cfg_qos_012901) describes the configuration requirements.

**Table 1** QoS guarantee provided by DeviceB for uplink traffic
| Traffic Type | CIR (kbit/s) | PIR (kbit/s) | DSCP Priority |
| --- | --- | --- | --- |
| Voice | 2000 | 10000 | 46 |
| Data | 4000 | 10000 | 14 |
| Video | 4000 | 10000 | 30 |



#### Procedure

1. Create VLANs and configure interfaces.
   
   
   
   # On DeviceB, create VLANs 10, 20, and 30, and add interfaces to the corresponding VLANs.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] vlan batch 10 20 30  
   [*DeviceB] interface 100ge 1/0/1
   [*DeviceB-100GE1/0/1] portswitch
   [*DeviceB-100GE1/0/1] port link-type trunk
   [*DeviceB-100GE1/0/1] port trunk allow-pass vlan 10 20 30
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] interface 100ge 1/0/2
   [*DeviceB-100GE1/0/2] portswitch
   [*DeviceB-100GE1/0/2] port link-type trunk
   [*DeviceB-100GE1/0/2] port trunk allow-pass vlan 10 20 30
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] commit
   ```
2. Configure a CAR profile.
   
   
   ```
   [~DeviceB] qos car car1 cir 12000
   [*DeviceB] commit
   ```
3. Configure traffic classifiers.
   
   # On DeviceB, create traffic classifiers **c1**, **c2**, and **c3** to classify different service flows based on their VLAN IDs.
   ```
   [~DeviceB] traffic classifier c1
   [*DeviceB-classifier-c1] if-match vlan 10
   [*DeviceB-classifier-c1] quit
   [*DeviceB] traffic classifier c2
   [*DeviceB-classifier-c2] if-match vlan 20
   [*DeviceB-classifier-c2] quit
   [*DeviceB] traffic classifier c3
   [*DeviceB-classifier-c3] if-match vlan 30
   [*DeviceB-classifier-c3] quit
   [*DeviceB] commit
   ```
4. Configure traffic behaviors and define traffic policing.
   
   
   
   # On DeviceB, create traffic behaviors **b1**, **b2**, and **b3** to perform traffic policing and priority re-marking for different service flows.
   
   ```
   [~DeviceB] traffic behavior b1
   [*DeviceB-behavior-b1] car cir 2000 pir 10000 green pass
   [*DeviceB-behavior-b1] car car1 share
   [*DeviceB-behavior-b1] remark dscp 46
   [*DeviceB-behavior-b1] statistics enable
   [*DeviceB-behavior-b1] quit
   [*DeviceB] traffic behavior b2
   [*DeviceB-behavior-b2] car cir 4000 pir 10000 green pass
   [*DeviceB-behavior-b2] remark dscp 14
   [*DeviceB-behavior-b2] statistics enable
   [*DeviceB-behavior-b2] quit
   [*DeviceB] traffic behavior b3
   [*DeviceB-behavior-b3] car cir 4000 pir 10000 green pass
   [*DeviceB-behavior-b3] remark dscp 30
   [*DeviceB-behavior-b3] statistics enable
   [*DeviceB-behavior-b3] quit
   [*DeviceB] commit
   ```
5. Configure a traffic policy and apply it to an inbound interface.
   
   
   
   # On DeviceB, create traffic policy **p1**, bind traffic classifiers to traffic behaviors in the traffic policy, and apply the traffic policy to the inbound direction of 100GE 1/0/1 to perform traffic policing and re-marking on packets.
   
   ```
   [~DeviceB] traffic policy p1
   [*DeviceB-trafficpolicy-p1] classifier c1 behavior b1
   [*DeviceB-trafficpolicy-p1] classifier c2 behavior b2
   [*DeviceB-trafficpolicy-p1] classifier c3 behavior b3
   [*DeviceB-trafficpolicy-p1] quit
   [*DeviceB] interface 100ge 1/0/1
   [*DeviceB-100GE1/0/1] traffic-policy p1 inbound
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] commit
   ```

#### Verifying the Configuration

# Check the traffic classifier configuration.

```
[~DeviceB] display traffic classifier
  Traffic Classifier Information: 
    Classifier: c1
      Type: OR
      Rule(s):
        if-match vlan 10

    Classifier: c2
      Type: OR
      Rule(s):
        if-match vlan 20

    Classifier: c3
      Type: OR
      Rule(s):
        if-match vlan 30

Total classifier number is 3
```

# Check the configuration of traffic policy **p1**.

```
[~DeviceB] display traffic policy p1
  Traffic Policy Information:                                                   
    Policy: p1                                                                 
      Classifier: c1                                                           
        Type: OR                                                                
      Behavior: b1                                                             
        Committed Access Rate:                                                  
          CIR 2000 (Kbps), PIR 10000 (Kbps), CBS 16000 (Bytes), PBS 80000 (Bytes)               
          Color Mode: color blind                                               
          Conform Action: pass                                                  
          Yellow  Action: pass                                                  
          Exceed  Action: discard                                               
        Remark:                                                                 
          Remark dscp ef                                                        
        Statistics: enable                                                      

      Classifier: c2                                                           
        Type: OR                                                                
      Behavior: b2                                                             
        Committed Access Rate:                                                  
          CIR 4000 (Kbps), PIR 10000 (Kbps), CBS 32000 (Bytes), PBS 80000 (Bytes) 
          Color Mode: color blind                                               
          Conform Action: pass                                                  
          Yellow  Action: pass                                                  
          Exceed  Action: discard                                               
        Remark:                                                                 
          Remark dscp af13                                                      
        Statistics: enable                                                      

      Classifier: c3                                                           
        Type: OR                                                                
      Behavior: b3                                                             
        Committed Access Rate:                                                  
          CIR 4000 (Kbps), PIR 10000 (Kbps), CBS 32000 (Bytes), PBS 80000 (Bytes)
          Color Mode: color blind                                               
          Conform Action: pass                                                  
          Yellow  Action: pass                                                  
          Exceed  Action: discard                                               
        Remark:                                                                 
          Remark dscp af33                                                      
        Statistics: enable 
```

# Check statistics about the traffic policy applied to 100GE 1/0/1.

```
[~DeviceB] display traffic-policy statistics interface 100ge 1/0/1 inbound
Traffic policy: p1, inbound                                                                                                          
--------------------------------------------------------------------------------
 Slot: 1                                                                          
 Item                  Packets                Bytes           pps           bps   
-------------------------------------------------------------------------------
 Matched                    0                    0             0             0    
  Passed                    0                    0             0             0    
  Dropped                   0                    0             0             0     
   Filter                   0                    0             0             0     
   CAR                      0                    0             0             0 
-------------------------------------------------------------------------------
```

# Take voice packets as an example. Send voice packets with VLAN ID 10 to 100GE 1/0/1 at the rates of 1500 kbit/s and 12500 kbit/s. Then, run the **display traffic-policy statistics interface 100ge 1/0/1 inbound** command to view traffic statistics on the interface. If the configuration is successful, all packets with VLAN ID 10 and sent at the rate of 1500 kbit/s can pass through 100GE1/0/1, and no packet is discarded. Packets with VLAN ID 10 and sent at the rate of 12500 kbit/s pass through 100GE 1/0/1 at the rate of 10000 kbit/s, and no packet is discarded. If packets with VLAN ID 10, packets with VLAN ID 30, and packets with VLAN ID 20 are sent to 100GE 1/0/1 at the rates of 3000 kbit/s, 5000 kbit/s, and 5000 kbit/s respectively, these packets pass through the interface at the rate of 12000 kbit/s, and excess packets are discarded.

#### Configuration Scripts

* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  vlan batch 10 20 30
  #                                                                               
  qos car car1 cir 12000 kbps
  #                                                                               
  traffic classifier c1 type or                                                  
   if-match vlan 10
  #                                                                               
  traffic classifier c2 type or                                                  
   if-match vlan 20
  #                                                                               
  traffic classifier c3 type or                                                  
   if-match vlan 30
  #                                                                               
  traffic behavior b1                                                            
   statistics enable                                                              
   car cir 2000 kbps pir 10000 kbps green pass
   car car1 share                                    
   remark dscp ef                                                                                                
  #                                                                               
  traffic behavior b2                                                            
   statistics enable                                                              
   car cir 4000 kbps pir 10000 kbps green pass                                    
   remark dscp af13                                                                                                                   
  #                                                                               
  traffic behavior b3                                                            
   statistics enable                                                              
   car cir 4000 kbps pir 10000 kbps green pass                                    
   remark dscp af33
  #                                                                               
  traffic policy p1                                                              
   classifier c1 behavior b1 precedence 5                                       
   classifier c2 behavior b2 precedence 10                                      
   classifier c3 behavior b3 precedence 15 
  #                                                                               
  interface 100GE1/0/1
   port link-type trunk                                                           
   port trunk allow-pass vlan 10 20 30                                            
   traffic-policy p1 inbound
  #                                                                               
  interface 100GE1/0/2
   port link-type trunk                                                           
   port trunk allow-pass vlan 10 20 30
  #
  return
  ```