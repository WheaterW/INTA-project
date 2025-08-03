Example for Configuring AnyFlow to Monitor HTTP Traffic
=======================================================

Example for Configuring AnyFlow to Monitor HTTP Traffic

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0000001564109937__fig12263151651514), AnyFlow needs to be configured on DeviceA to aggregate HTTP flows with the service port number 80 and export aggregated flow entries, thereby implementing HTTP traffic monitoring.

**Figure 1** Network diagram for configuring AnyFlow to monitor HTTP traffic  
![](figure/en-us_image_0000001512670758.png)
#### Procedure

1. Enable the AnyFlow function.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] [commit](cmdqueryname=commit)
   [~DeviceA] [any-flow](cmdqueryname=any-flow)
   [*DeviceA-any-flow] [enable](cmdqueryname=enable)
   [*DeviceA-any-flow] [quit](cmdqueryname=quit)
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
2. Configure flow aggregation.
   
   
   ```
   [~DeviceA] [any-flow](cmdqueryname=any-flow) 
   [*DeviceA-any-flow] [aggregation service-port 80](cmdqueryname=aggregation+service-port+80)
   [*DeviceA-any-flow] [flow-aggregation enable](cmdqueryname=flow-aggregation+enable) 
   [*DeviceA-any-flow] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
3. Configure the aggregated flow entry export time.
   
   
   ```
   [~DeviceA] [any-flow](cmdqueryname=any-flow) 
   [*DeviceA-any-flow] flow-aggregation aging-time 80
   [*DeviceA-any-flow] flow-aggregation export interval 400
   [*DeviceA-any-flow] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
4. Configure the analyzer.
   
   
   ```
   [~DeviceA] collector collect 3 
   [*DeviceA-collect-3] source ip 10.1.1.1 export host ip 10.2.1.1 udp-port 16
   [*DeviceA-collect-3] quit 
   [*DeviceA] any-flow
   [*DeviceA-any-flow] collector collect 3
   [*DeviceA-any-flow] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

# View the flow entries on DeviceA.

```
[~DeviceA] display any-flow flow-cache ipv4 slot 1
Total: 2 
--------------------------------------------- 
SIP  : 192.168.1.2          SrcPort  : 20 
DIP  : 10.0.0.2             DstPort  : 80 
VRF  : --                   Protocol : 16 
VNI  : 10                   VLAN     : -- 
Qpair: --

SIP  : 192.168.1.3          SrcPort  : 20 
DIP  : 10.0.0.3             DstPort  : 80 
VRF  : --                   Protocol : 16
VNI  : 10                   VLAN     : --
Qpair: --
--------------------------------------------- 
```

#### Configuration Scripts

```
#
sysname DeviceA
#
any-flow  
 enable  
 collector collect 3
 flow-aggregation enable 
 aggregation service-port 80 
 flow-aggregation export interval 400 
 flow-aggregation aging-time 80 
#
collector collect 3
 source ip 10.1.1.1 export host ip 10.2.1.1 udp-port 16
#
return
```