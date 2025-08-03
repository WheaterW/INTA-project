Example for Configuring iQCN for a Lossless Queue
=================================================

Example for Configuring iQCN for a Lossless Queue

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001564119653__fig19978171395514), a lossless service carried by RoCEv2 traffic is deployed on Host1 and Host2, and DeviceA is directly connected to both hosts. DCQCN is configured on Host1 and Host2. To ensure that Host1 and Host2 do not increase their packet sending rates if they do not receive CNPs in a timely manner when congestion occurs, configure iQCN for a lossless queue on DeviceA.

**Figure 1** Network diagram for configuring iQCN for a lossless queue![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent 100GE1/0/1 and 100GE1/0/2, respectively.


  
![](figure/en-us_image_0000001564119657.png)

#### Precautions

When configuring iQCN for a lossless queue, note the following:

* NICs of the hosts must support RoCEv2 and DCQCN.
* The parameter settings in this example are for reference only. You need to configure each device based on the traffic model in the actual networking.

#### Procedure

1. Configure DeviceA to implement PFC based on the DSCP value.
   
   
   
   # In this example, a queue with priority 4 is used to carry RoCEv2 traffic. Enable PFC for the queue with priority 4 on interfaces of DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] dcb pfc
   [*DeviceA-dcb-pfc-default] priority 4
   [*DeviceA-dcb-pfc-default] quit
   [*DeviceA] port-group all_using   
   [*DeviceA-port-group-all_using] group-member 100ge 1/0/1 to 100ge 1/0/2
   [*DeviceA-port-group-all_using] dcb pfc enable mode manual
   [*DeviceA-port-group-all_using] quit
   [*DeviceA] commit
   ```
   
   # In this example, the DSCP value of RoCEv2 packets is 24, and the DSCP value of CNPs is 25. Configure the DiffServ domain **ds1** on DeviceA to map the DSCP value of RoCEv2 packets to 4 and that of CNPs to 6, ensuring that CNPs are transmitted through a queue with a higher priority. Then apply the DiffServ domain to interfaces.
   
   ```
   [~DeviceA] diffserv domain ds1 
   [*DeviceA-dsdomain-ds1] ip-dscp-inbound 24 phb af4 green
   [*DeviceA-dsdomain-ds1] ip-dscp-inbound 25 phb cs6 green
   [*DeviceA-dsdomain-ds1] quit 
   [*DeviceA] port-group all_using
   [*DeviceA-port-group-all_using] trust dscp
   [*DeviceA-port-group-all_using] trust upstream ds1
   [*DeviceA-port-group-all_using] quit
   [*DeviceA] commit
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   After the preceding configurations are complete, RoCEv2 packets are transmitted through the queue with priority 4, which is a lossless queue.
2. Configure iQCN for a lossless queue.
   
   
   
   # Enable iQCN for lossless queue 4 on DeviceA. In this example, the interval between rate increase events of the NIC is 400 µs.
   
   ```
   [~DeviceA] ai-service
   [*DeviceA-ai-service] iqcn
   [*DeviceA-ai-service-iqcn] assign queue 4
   [*DeviceA-ai-service-iqcn] iqcn enable
   [*DeviceA-ai-service-iqcn] rpg-time-reset 400
   [*DeviceA-ai-service-iqcn] quit
   [*DeviceA-ai-service] quit
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] iqcn enable
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] iqcn enable
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Check statistics about CNPs proactively sent by DeviceA.

```
[~DeviceA] display iqcn statistics slot 1  
iQCN: Enable
Queue: 4 
RPG Time Reset: 400 us
TX CNP Packets: 7891564
TX CNP Rate(pps): 89898
--------------------------------------------------
Interface      RX CNP Packets    RX CNP Rate(pps) 
100GE1/0/1       158964894615              569874 
100GE1/0/2                 22                   9
--------------------------------------------------
```

#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
dcb pfc
 priority 4
#
diffserv domain ds1  
 ip-dscp-inbound 24 phb af4 green
 ip-dscp-inbound 25 phb cs6 green
#
interface 100GE1/0/1
 iqcn enable
 trust dscp
 trust upstream ds1
 dcb pfc enable mode manual
#
interface 100GE1/0/2
 iqcn enable
 trust dscp
 trust upstream ds1
 dcb pfc enable mode manual
#
ai-service 
 #
 iqcn
  iqcn enable
  assign queue 4
  rpg-time-reset 400
#
port-group all_using        
 group-member 100GE1/0/1   
 group-member 100GE1/0/2 
#
return

```