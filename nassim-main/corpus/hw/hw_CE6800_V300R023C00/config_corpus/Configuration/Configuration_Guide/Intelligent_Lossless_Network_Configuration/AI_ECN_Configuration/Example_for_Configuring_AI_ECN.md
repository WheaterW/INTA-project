Example for Configuring AI ECN
==============================

Example for Configuring AI ECN

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001563872189__fig19978171395514), an AI service carried by RoCEv2 traffic is deployed on Host1 and Host2, and DeviceA is directly connected to both hosts. To achieve the optimal performance of the AI service, a network environment with low delay, zero packet loss, and high throughput is required. To meet this requirement, PFC, EAI, and AI ECN functions can be configured on DeviceA.

**Figure 1** Network diagram of AI ECN![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent 100GE1/0/1 and 100GE1/0/2, respectively.


  
![](figure/en-us_image_0000001563992473.png)

#### Precautions

* NICs of the hosts must support RoCEv2 and DCQCN.
* The parameter settings in this example are for reference only. Configure each device based on the traffic model in the actual networking.

#### Procedure

1. Configure DeviceA to implement PFC based on the DSCP value.
   
   
   
   # In this example, a queue with priority 4 is used to carry RoCEv2 traffic. Enable PFC for the queue with priority 4 on interfaces of DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] qos buffer headroom-pool size 4 mbytes slot 1      //This command is required only on the CE6855-48XS8CQ, CE6863E-48S8CQ, CE6885, CE6885-LL, CE6885-SAN, CE6885-T, CE8851-32CQ4BQ, CE8855.
   [*DeviceA] dcb pfc
   [*DeviceA-dcb-pfc-default] priority 4
   [*DeviceA-dcb-pfc-default] quit
   [*DeviceA] port-group all_using   
   [*DeviceA-port-group-all_using] group-member 100ge 1/0/1 to 100ge 1/0/2
   [*DeviceA-port-group-all_using] dcb pfc enable mode manual
   [*DeviceA-port-group-all_using] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceA to implement PFC based on the priority after DSCP mapping. (Supported only by the CE6855-48XS8CQ, CE6863E-48S8CQ, CE6885, CE6885-LL (standard forwarding mode), CE6885-SAN, CE6885-T, CE8851-32CQ4BQ, CE8855.)
   
   ```
   [~DeviceA] dcb pfc dscp-mapping enable slot 1
   [*DeviceA] commit
   ```
   
   # In this example, the DSCP value of RoCEv2 packets is 24, and the DSCP value of CNPs is 25. Configure a priority mapping profile for the DiffServ domain **ds1** on DeviceA to map the DSCP value of RoCEv2 packets to the priority 4 and that of CNPs to the priority 6, ensuring that CNPs are transmitted through a queue with a higher priority. Then apply the DiffServ domain to interfaces.
   
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
   [~DeviceA] quit 
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   After the preceding PFC-related configurations are complete, RoCEv2 packets are transmitted through the queue with priority 4, which is a lossless queue.
2. Configure EAI.
   
   
   
   # Configure EAI on DeviceA and load the model file required by the AI ECN component. In this example, the model file has been uploaded to the device, and the full path is **flash:/AI\_ECN-1.0.0-1.0.2.zip**. By default, a model file is preloaded on the device.
   
   ```
   <DeviceA> load ai-service model-file flash:/AI_ECN-1.0.0-1.0.2.zip all
   ```
3. Configure AI ECN for a lossless queue.
   
   
   
   # Enable AI ECN for lossless queue 4 on DeviceA.
   
   ```
   <DeviceA> system-view
   [~DeviceA] ai-service
   [*DeviceA-ai-service] ai-ecn
   [*DeviceA-ai-service-ai-ecn] assign queue 4
   [*DeviceA-ai-service-ai-ecn] ai-ecn enable
   [*DeviceA-ai-service-ai-ecn] quit
   [*DeviceA-ai-service] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Check information about all models on the device. The command output shows that the AI ECN function has subscribed to the newly loaded model.
```
[~DeviceA] display ai-service model
--------------------------------------------------------------------------------
File Name
          Model Name        Model Version     Model Type        Service
--------------------------------------------------------------------------------
AI_ECN-1.0.0-1.0.0.zip
          AI_ECN            1.0.0             Default           --
AI_ECN-1.0.0-1.0.2.zip
          AI_ECN            1.0.2             User Define       AI ECN
--------------------------------------------------------------------------------
```

# Check the ECN thresholds calculated by the AI ECN function for the lossless queue. The command output shows that the AI ECN function calculates the ECN thresholds of the device in NN mode (model inference mode).

```
[~DeviceA] display ai-ecn calculated state 
AI-ECN Model Version : 1.0.1
Mode : NN - Model inference    BBR - Heuristic inference    STATIC - Static threshold
-----------------------------------------------------------------------------------------------------------------------------
Interface       Queue   Low-Threshold   High-Threshold   Probability   Mode                Active model       Actived time
                               (Byte)           (Byte)           (%)
-----------------------------------------------------------------------------------------------------------------------------
100GE1/0/1          4          204800           614400             5    NN    AI_ECN_DistributedStorage   2022-01-10 09:09:23
100GE1/0/2          4          204800           614400             5    NN    AI_ECN_DistributedStorage   2022-01-10 09:09:23
-----------------------------------------------------------------------------------------------------------------------------
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
dcb pfc dscp-mapping enable slot 1    //Supported only by the CE6855-48XS8CQ, CE6863E-48S8CQ, CE6885, CE6885-LL (standard forwarding mode), CE6885-SAN, CE6885-T, CE8851-32CQ4BQ, CE8855.
#
qos buffer headroom-pool size 4 mbytes slot 1      //This command is required only on the CE6855-48XS8CQ, CE6863E-48S8CQ, CE6885, CE6885-LL, CE6885-SAN, CE6885-T, CE8851-32CQ4BQ, CE8855.
#
diffserv domain ds1  
 ip-dscp-inbound 24 phb af4 green
 ip-dscp-inbound 25 phb cs6 green
#
interface 100GE1/0/1
 trust dscp
 trust upstream ds1
 dcb pfc enable mode manual
#
interface 100GE1/0/2
 trust dscp
 trust upstream ds1
 dcb pfc enable mode manual
#
ai-service 
 #
 ai-ecn
  ai-ecn enable
  assign queue 4
#
port-group all_using        
 group-member 100GE1/0/1   
 group-member 100GE1/0/2 
#
return
```