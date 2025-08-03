Example for Configuring AnyFlow to Monitor Network-wide Traffic
===============================================================

Example for Configuring AnyFlow to Monitor Network-wide Traffic

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0000001563750225__fig12263151651514), AnyFlow needs to be configured on DeviceA to monitor network-wide traffic.

**Figure 1** Network diagram for configuring AnyFlow to monitor network-wide traffic  
![](figure/en-us_image_0000001513149894.png)
#### Procedure

1. Enable the AnyFlow function.
   
   
   ```
   <HUAWEI> system-view
   <~HUAWEI> sysname DeviceA
   [*HUAWEI] [commit](cmdqueryname=commit)
   [~DeviceA] [any-flow](cmdqueryname=any-flow)
   [*DeviceA-any-flow] [enable](cmdqueryname=enable)
   [*DeviceA-any-flow] [quit](cmdqueryname=quit)
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
2. Configure the flow entry export time.
   
   
   ```
   [~DeviceA] [any-flow](cmdqueryname=any-flow) 
   [*DeviceA-any-flow] [aging-time](cmdqueryname=aging-time) 40
   [*DeviceA-any-flow] [export](cmdqueryname=export) interval 20
   [*DeviceA-any-flow] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
3. Configure the analyzer.
   
   
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
DIP  : 10.0.0.2             DstPort  : 30 
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
 aging-time 40
 export interval 20 
#
collector collect 3
 source ip 10.1.1.1 export host ip 10.2.1.1 udp-port 16
#
return
```