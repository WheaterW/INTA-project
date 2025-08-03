Example for Configuring Latency Visualization
=============================================

Example for Configuring Latency Visualization

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001563999389__fig14041944132712), Host1 and Host2 communicate with each other through DeviceA. The network administrator wants DeviceA to report flow entries carrying information about high-latency packets to the collector to prevent network congestion.

![](public_sys-resources/note_3.0-en-us.png) 

Only the following models support the latency visualization function: CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, .


**Figure 1** Network diagram of latency visualization  
![](figure/en-us_image_0000001512839610.png)

#### Procedure

1. Create a collector and set the ID of the collector that receives packet loss visualization and latency visualization flow entries to that of the created collector.
   
   
   
   # On DeviceA, create a collector with the ID of 1. The device's and collector's IP addresses are 10.1.1.1 and 10.1.2.1, respectively. The collector's port number is 9000.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] collector collect 1
   [*DeviceA-collect-1] source ip 10.1.1.1 export host ip 10.1.2.1 udp-port 9000
   [*DeviceA-collect-1] quit
   [*DeviceA] commit
   ```
   
   # Enable 1588v2 on DeviceA.
   
   ```
   [~DeviceA] [ptp enable](cmdqueryname=ptp+enable)
   [*DeviceA] commit
   ```
   
   # On DeviceA, enter the packet monitoring view and set the ID of the collector that receives packet loss visualization flow entries to 1.
   
   ```
   [~DeviceA] packet event monitor
   [*DeviceA-packet-event-monitor] collector collect 1
   [*DeviceA-packet-event-monitor] commit
   ```
2. Enable the latency visualization function.
   
   
   
   # On DeviceA, enter the latency visualization view and set the latency threshold to 832 ns.
   
   ```
   [~DeviceA-packet-event-monitor] capture latency-event
   [*DeviceA-packet-event-monitor-latency-event] latency threshold 832
   [*DeviceA-packet-event-monitor-latency-event] commit
   ```
3. Configure the time for reporting latency visualization flow entries.
   
   
   
   # On DeviceA, set the aging time for latency visualization flow entries to 50 seconds.
   
   ```
   [~DeviceA-packet-event-monitor-latency-event] aging-time 50
   [*DeviceA-packet-event-monitor-latency-event] quit
   [*DeviceA-packet-event-monitor] commit
   ```
   
   # On DeviceA, set the interval for reporting latency visualization flow entries to 30 seconds.
   
   ```
   [~DeviceA-packet-event-monitor] export interval 30
   [*DeviceA-packet-event-monitor] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

Check the latency visualization flow table information when packets exceed the configured latency threshold on DeviceA.

# Display information in the latency visualization flow table.

```
[~DeviceA] display latency-event flow-cache slot 1
Total: 1
------------------------------------------------------------
Number                  :3                                  
 Latency packet Count   :1                                  
 Latency Byte Count     :124                                
 Latency Peak           :1376329803                         
 Latency Last           :1376329803                         
 Source MAC             :0000-c055-0107                     
 Destination MAC        :0000-0000-0077                     
 PE-VLAN                :0                                  
 CE-VLAN                :0                                  
 Source IPv4            :11.1.1.1                           
 Destination IPv4       :10.1.1.1                           
 Source IPv6            :-                                  
 Destination IPv6       :-                                  
 ProtocolId             :253                                
 L4 Source Port         :0                                  
 L4 Destination Port    :0                                  
 outer TTL              :64                                 
 inner TTL              :64                                 
 Tos                    :0                                  
 VNI ID                 :0                                  
 Queue                  :48                                 
 Start Timestamp        :2020-01-01 16:10:28                           
 Last Timestamp         :2020-01-01 16:10:37                           
 In Interface           :-                        
 Out Interface          :100GE1/0/1                                 
 causeID                :8191                               
 outerSrcIPv4           :-                                  
 outerDstIPv4           :-                                  
 outerSrcIPv6           :-                                  
 outerDstIPv6           :-
 RoCEv2 Qpair           :-  
 NVME Namespace ID      :-  
```
#### Configuration Scripts

DeviceA
```
#
sysname DeviceA
#
collector collect 1
 source ip 10.1.1.1 export host ip 10.1.2.1 udp-port 9000
#
ptp enable
#
packet event monitor 
 collector collect 1
 export interval 30
 #   
 capture latency-event
  latency threshold 832
  aging-time 50
#
return
```