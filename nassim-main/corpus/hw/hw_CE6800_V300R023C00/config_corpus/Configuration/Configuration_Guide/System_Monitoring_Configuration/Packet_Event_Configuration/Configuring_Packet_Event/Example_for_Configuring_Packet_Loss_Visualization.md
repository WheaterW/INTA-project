Example for Configuring Packet Loss Visualization
=================================================

Example for Configuring Packet Loss Visualization

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001512679966__fig14041944132712), Host1 and Host2 communicate with each other through DeviceA. To facilitate fault locating, the network administrator wants DeviceA to report flow entries carrying packet loss information to the collector.

**Figure 1** Network diagram of packet loss visualization  
![](figure/en-us_image_0000001513039182.png)

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
   
   # On DeviceA, enter the packet monitoring view and set the ID of the collector that receives packet loss visualization flow entries to 1.
   
   ```
   [~DeviceA] packet event monitor
   [*DeviceA-packet-event-monitor] collector collect 1
   [*DeviceA-packet-event-monitor] commit
   ```
2. Enable the packet loss visualization function.
   
   
   
   # On DeviceA, enter the packet loss visualization view and enable packet loss visualization for packets discarded due to reasons such as a forwarding exception, specified packet discarding rules, a full buffer, and ACL rule deny actions.
   
   ```
   [~DeviceA-packet-event-monitor] capture drop-event
   [*DeviceA-packet-event-monitor-drop-event] capture drop-packet forward-exception enable
   [*DeviceA-packet-event-monitor-drop-event] capture drop-packet forward-normal enable
   [*DeviceA-packet-event-monitor-drop-event] capture drop-packet buffer-overflow enable
   [*DeviceA-packet-event-monitor-drop-event] capture drop-packet acl-deny enable //This command is not supported by the following: CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, CE6863E-48S8CQ. However, when the packet loss visualization function for the packets discarded due to a forwarding exception is enabled, the packet loss visualization function for the packets discarded due to the ACL rule deny actions also takes effect.
   [*DeviceA-packet-event-monitor-drop-event] commit
   ```
3. Configure the time for reporting packet loss visualization flow entries to the collector.
   
   
   
   # On DeviceA, set the aging time for packet loss visualization flow entries to 50 seconds.
   
   ```
   [~DeviceA-packet-event-monitor-drop-event] aging-time 50
   [*DeviceA-packet-event-monitor-drop-event] quit
   [*DeviceA-packet-event-monitor] commit
   ```
   
   # On DeviceA, set the interval for reporting packet loss visualization flow entries to 30 seconds.
   
   ```
   [~DeviceA-packet-event-monitor] export interval 30
   [*DeviceA-packet-event-monitor] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

Check the packet loss visualization flow table information when packet loss occurs on DeviceA.

# Check the packet loss visualization flow table information.

```
[~DeviceA] display drop-event flow-cache slot 1
Total: 1
------------------------------------------------------------
Number                  :1                                  
 Drop Reason            :DISCARD_CAUSE_XXX                                              
 Drop packet Count      :25                                 
 Drop Byte Count        :1500                               
 Source MAC             :0000-c055-0102                     
 Destination MAC        :ffff-ffff-ffff                     
 PE-VLAN                :0                                  
 CE-VLAN                :0                                  
 Source IPv4            :-                                  
 Destination IPv4       :-                                  
 Source IPv6            :-                                  
 Destination IPv6       :-                                  
 ProtocolId             :0                                  
 L4 Source Port         :0                                  
 L4 Destination Port    :0                                  
 Outer TTL              :64                                 
 Inner TTL              :64                                 
 Tos                    :0                                  
 VNI ID                 :0                                  
 Queue                  :255                                
 Start Timestamp        :2020-01-01 16:10:28                             
 Last Timestamp         :2020-01-01 16:10:37                             
 In Interface           :100GE1/0/17                         
 Out Interface          :-                                  
 causeID                :99                                 
 outerSrcIPv4           :-                                  
 outerDstIPv4           :-                                  
 outerSrcIPv6           :-
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
packet event monitor 
 collector collect 1
 export interval 30
 #   
 capture drop-event
  capture drop-packet forward-exception enable
  capture drop-packet forward-normal enable
  capture drop-packet buffer-overflow enable
  capture drop-packet acl-deny enable //This command is not supported by the following: CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, CE6863E-48S8CQ. However, when the packet loss visualization function for the packets discarded due to a forwarding exception is enabled, the packet loss visualization function for the packets discarded due to the ACL rule deny actions also takes effect.
  aging-time 50
#
return
```