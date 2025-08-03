Example for Configuring MDN
===========================

Example for Configuring MDN

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001906181505__fig_dc_cfg_lldp_002601), DeviceB and DeviceC are non-Huawei devices, and DeviceA is a Huawei device. The three devices are directly connected, and there is a reachable route between DeviceA and the NMS. DeviceA needs to identify and receive non-standard discovery protocol packets from DeviceB and DeviceC, and generate traps when the neighbors change.

**Figure 1** Network diagram for configuring MDN  
![](figure/en-us_image_0000001860141688.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable LLDP globally on DeviceA.
2. Configure MDN on DeviceA so that DeviceA can discover non-Huawei devices connected to it.
3. Enable the LLDP trap function on DeviceA so that DeviceA can generate traps when the neighbors change. You can also configure the device to send traps to the NMS if necessary.

#### Procedure

1. Enable LLDP globally on DeviceA.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] lldp enable
   [*DeviceA] commit
   ```
2. Configure MDN on DeviceA.
   
   # Configure MDN on interfaces.
   ```
   [~DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] lldp mdn enable
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/1] lldp mdn enable
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
3. Enable the LLDP trap function on DeviceA.
   
   
   ```
   [~DeviceA] snmp-agent trap enable feature-name lldp
   [*DeviceA] commit
   ```
4. Verify the configuration.
   
   
   
   Check information about MDN neighbors of DeviceA.
   
   ```
   [~DeviceA] display lldp mdn neighbor
   100GE1/0/1 has 1 neighbor(s):
   Neighbor index                     :1
   MacAddress                         :0023-ea20-b010             
   Discovered time                    :2023-03-09 13:09:55
   
   100GE1/0/2 has 1 neighbor(s):
   Neighbor index                     :1
   MacAddress                         :0023-ea20-b011             
   Discovered time                    :2023-03-09 13:09:58
   ```

#### Configuration Scripts

# DeviceA
```
#
sysname DeviceA
#
interface 100GE1/0/1
 lldp mdn enable
#
interface 100GE1/0/2
 lldp mdn enable
#
snmp-agent trap enable feature-name lldp trap-name hwLldpMdnRemTablesChange
#
lldp enable
#
return
```