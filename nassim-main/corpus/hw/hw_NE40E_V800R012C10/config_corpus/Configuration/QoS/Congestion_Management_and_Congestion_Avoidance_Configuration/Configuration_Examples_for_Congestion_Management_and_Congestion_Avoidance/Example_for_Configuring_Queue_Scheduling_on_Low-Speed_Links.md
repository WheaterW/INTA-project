Example for Configuring Queue Scheduling on Low-Speed Links
===========================================================

This section provides an example for configuring queue scheduling on low-speed links to ensure that higher-priority packets are forwarded ahead of lower-priority packets.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172371207__fig_dc_ne_qos_cfg_500601), DeviceA and DeviceB are connected through a low-speed link with limited bandwidth resources. To ensure that packets of different priorities are allocated bandwidth resources based on their CoSs when congestion occurs, priority queuing (PQ) and weighted fair queuing (WFQ) need to be configured on the DeviceA's interface connecting to DeviceB. PQ applies to higher-priority packets, and WFQ applies to other packets.

In this example, PQ applies to packets in the EF queue, and the peak information rate (PIR) is set for the expedited forwarding (EF) queue; WFQ applies to packets in the assured forwarding 2 (AF2), AF3, and AF4 queues, and the same PIR is set for the AF2, AF3, and AF4 queues.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 represents Serial 0/2/0:0.


**Figure 1** Networking diagram for configuring queue scheduling on a low-speed link  
![](images/fig_dc_ne_qos_cfg_500601.png)  


#### Precautions

None


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IP addresses for interfaces on DeviceA and DeviceB.
2. Configure PQ and WFQ on DeviceA.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of interfaces
* PIR for the EF queue to which PQ applies
* PIR for the AF2, AF3, and AF4 queues to which WFQ applies

#### Procedure

1. Configure serial interfaces on DeviceA and DeviceB.
   
   
   
   The configuration details are not provided here. For details, see the *HUAWEI NE40E-M2 series Universal Service Router Configuration Guide - WAN Access*.
2. Configure IP addresses for interfaces on DeviceA and DeviceB to ensure network connectivity.
   
   
   
   The configuration details are not provided here. For details, see the *HUAWEI NE40E-M2 series Universal Service Router Configuration Guide - IP Routing*.
3. Configure PQ and WFQ on Serial 0/2/0:0 of DeviceA.
   
   
   
   # Configure PQ.
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA]interface serial 0/2/0:0
   ```
   ```
   [*DeviceA-serial0/2/0:0] port-queue ef pq shaping pir percentage 60
   ```
   ```
   [*DeviceA-serial0/2/0:0] commit
   ```
   
   # Configure WFQ.
   
   ```
   [~DeviceA-serial0/2/0:0] port-queue af4 wfq shaping cir 200 pir percentage 40
   ```
   ```
   [*DeviceA-serial0/2/0:0] port-queue af3 wfq shaping cir 300 pir percentage 40
   ```
   ```
   [*DeviceA-serial0/2/0:0] port-queue af2 wfq shaping cir 400 pir percentage 40
   ```
   ```
   [*DeviceA-serial0/2/0:0] commit
   ```
   ```
   [*DeviceA-serial0/2/0:0] quit
   ```
4. Verify the configuration.
   
   
   
   # After the preceding configuration is complete, run the **display ls-port-queue configuration interface** command to check the detailed configuration of port queues.
   
   ```
   [~DeviceA]display ls-port-queue configuration interface Serial0/2/0:0 outbound 
    GigabitEthernet0/2/0 outbound current port-queue configuration: 
    be :  arithmetic: wfq                weight: 10         tm weight: 3                                                               
          fact weight: 10.00             shaping(kbps): NA                                                                             
          port-wred: NA                                                                                                                
            green (low-high limit) (kbytes)                  712704 - 1425408                                                          
            yellow(low-high limit) (kbytes)                  712704 - 1425408                                                          
            red   (low-high limit) (kbytes)                  712704 - 1425408                                                          
          current queue-length     (kbytes)                  1425408 
          cir(kbps):123,000              cir-percentage:NA
          cir-arithmetic:pq              cir-weight:NA
          pir(kbps):123,000              pir-percentage:NA
          pir-arithmetic:lpq             pir-weight:NA                                                                  
    af1:  arithmetic: wfq                weight: 10         tm weight: 3                                                               
          fact weight: 10.00             shaping(kbps): NA                                                                             
          port-wred: NA                                                                                                                
            green (low-high limit) (kbytes)                  712704 - 1425408                                                          
            yellow(low-high limit) (kbytes)                  712704 - 1425408                                                          
            red   (low-high limit) (kbytes)                  712704 - 1425408                                                          
          current queue-length     (kbytes)                  1425408    
          cir(kbps):NA                   cir-percentage:10
          cir-arithmetic:pq              cir-weight:NA
          pir(kbps):NA                   pir-percentage:20
          pir-arithmetic:wfq             pir-weight:15                                                               
    af2:  arithmetic: wfq                weight: 10         tm weight: 3                                                               
          fact weight: 10.00             shaping(kbps): NA                                                                             
          port-wred: NA                                                                                                                
            green (low-high limit) (kbytes)                  712704 - 1425408                                                          
            yellow(low-high limit) (kbytes)                  712704 - 1425408                                                          
            red   (low-high limit) (kbytes)                  712704 - 1425408                                                          
          current queue-length     (kbytes)                  1425408
          cir(kbps):NA                   cir-percentage:NA
          cir-arithmetic:NA              cir-weight:NA
          pir(kbps):NA                   pir-percentage:NA
          pir-arithmetic:NA              pir-weight:NA                                                                    
    af3:  arithmetic: wfq                weight: 15         tm weight: 2                                                               
          fact weight: 15.00             shaping(kbps): NA                                                                             
          port-wred: NA                                                                                                                
            green (low-high limit) (kbytes)                  712704 - 1425408                                                          
            yellow(low-high limit) (kbytes)                  712704 - 1425408                                                          
            red   (low-high limit) (kbytes)                  712704 - 1425408                                                          
          current queue-length     (kbytes)                  1425408     
          cir(kbps):NA                   cir-percentage:NA
          cir-arithmetic:NA              cir-weight:NA
          pir:(kbps)NA                   pir-percentage:NA
          pir-arithmetic:NA              pir-weight:NA                                                                
    af4:  arithmetic: wfq                weight: 15         tm weight: 2                                                               
          fact weight: 15.00             shaping(kbps): NA                                                                             
          port-wred: NA                                                                                                                
            green (low-high limit) (kbytes)                  712704 - 1425408                                                          
            yellow(low-high limit) (kbytes)                  712704 - 1425408                                                          
            red   (low-high limit) (kbytes)                  712704 - 1425408                                                          
          current queue-length     (kbytes)                  1425408
          cir(kbps):NA                   cir-percentage:NA
          cir-arithmetic:NA              cir-weight:NA
          pir(kbps):NA                   pir-percentage:NA
          pir-arithmetic:NA              pir-weight:NA                                                                     
    ef :  arithmetic: pq                 weight: NA         tm weight: NA                                                              
          fact weight: NA                shaping(kbps): NA                                                                             
          port-wred: NA                                                                                                                
            green (low-high limit) (kbytes)                  6096 - 12192                                                              
            yellow(low-high limit) (kbytes)                  6096 - 12192                                                              
            red   (low-high limit) (kbytes)                  6096 - 12192                                                              
          current queue-length     (kbytes)                  12192
          cir(kbps):NA                   cir-percentage:NA
          cir-arithmetic:NA              cir-weight:NA
          pir:(kbps)NA                   pir-percentage:NA
          pir-arithmetic:NA              pir-weight:NA                                                                      
    cs6:  arithmetic: pq                 weight: NA         tm weight: NA                                                              
          fact weight: NA                shaping(kbps): NA                                                                             
          port-wred: NA                                                                                                                
            green (low-high limit) (kbytes)                  6096 - 12192                                                              
            yellow(low-high limit) (kbytes)                  6096 - 12192                                                              
            red   (low-high limit) (kbytes)                  6096 - 12192                                                              
          current queue-length     (kbytes)                  12192 
          cir(kbps):NA                   cir-percentage:NA
          cir-arithmetic:NA              cir-weight:NA
          pir(kbps):NA                   pir-percentage:NA
          pir-arithmetic:NA              pir-weight:NA                                                                     
    cs7:  arithmetic: pq                 weight: NA         tm weight: NA                                                              
          fact weight: NA                shaping(kbps): NA                                                                             
          port-wred: NA                                                                                                                
            green (low-high limit) (kbytes)                  6096 - 12192                                                              
            yellow(low-high limit) (kbytes)                  6096 - 12192                                                              
            red   (low-high limit) (kbytes)                  6096 - 12192                                                              
          current queue-length     (kbytes)                  12192   
          cir(kbps):NA                   cir-percentage:NA
          cir-arithmetic:NA              cir-weight:NA
          pir:(kbps)NA                   pir-percentage:NA
          pir-arithmetic:NA              pir-weight:NA
   ```

#### Configuration Files

* DeviceA configuration file

```
#
```
```
 Sysname DeviceA
```
```
#
```
```
 controller e1 0/2/0
```
```
  channel-set 0 timeslot-list 1-31
```
```
  undo shutdown
```
```
#
```
```
interface Serial0/2/0:0 
```
```
 undo shutdown
```
```
 ip address 3.3.3.1 255.255.255.0
```
```
 port-queue af2 wfq shaping cir 400 pir percentage 40                                       
```
```
 port-queue af3 wfq shaping cir 300 pir percentage 40                                       
```
```
 port-queue af4 wfq shaping cir 200 pir percentage 40                                       
```
```
 port-queue ef pq shaping pir percentage 60  
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
 Sysname DeviceB
```
```
#
```
```
 controller e1 0/2/0
```
```
  channel-set 0 timeslot-list 1-31
```
```
  undo shutdown
```
```
#
```
```
interface Serial0/2/0:0 
```
```
 undo shutdown
```
```
 ip address 3.3.3.2 255.255.255.0
```
```
#
```
```
return
```