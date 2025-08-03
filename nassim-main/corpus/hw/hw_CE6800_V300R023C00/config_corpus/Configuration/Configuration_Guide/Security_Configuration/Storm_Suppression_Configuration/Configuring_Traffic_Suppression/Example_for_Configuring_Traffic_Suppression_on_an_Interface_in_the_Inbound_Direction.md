Example for Configuring Traffic Suppression on an Interface in the Inbound Direction
====================================================================================

Example for Configuring Traffic Suppression on an Interface in the Inbound Direction

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001513168462__fig_dc_cfg_storm_001101), DeviceA connects a Layer 2 network to a Layer 3 device. Traffic suppression needs to be configured on one of DeviceA's interfaces in the inbound direction to rate-limit broadcast packets, unknown multicast packets, and unknown unicast packets forwarded at Layer 2, ultimately preventing broadcast storms.

**Figure 1** Networking diagram of traffic suppression on an interface in the inbound direction![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 represents 100GE1/0/1.


  
![](figure/en-us_image_0000001564008749.png)

#### Procedure

1. Enter the interface view.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*DeviceA] commit
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] portswitch
   ```
2. Set the CIR of broadcast packets to 100 kbit/s.
   
   
   ```
   [*DeviceA-100GE1/0/1] storm suppression broadcast cir 100
   ```
3. Set the percentage of bandwidth occupied by unknown multicast packets to 80%.
   
   
   ```
   [*DeviceA-100GE1/0/1] storm suppression multicast 80
   ```
4. Set the CIR of unknown unicast packets to 100 kbit/s.
   
   
   ```
   [*DeviceA-100GE1/0/1] storm suppression unknown-unicast cir 100
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Check the traffic suppression configuration in the inbound direction of the interface.

```
[~DeviceA] display storm suppression broadcast interface 100ge 1/0/1
------------------------------------------------------------------------------------------------
                            Configured                           Current            
interface        percent(%) cir(kbps) cbs(bytes)     pps percent(%) cir(kbps) cbs(bytes)     pps
------------------------------------------------------------------------------------------------
100GE1/0/1                --       100      18800      --         --       100      18800      --
------------------------------------------------------------------------------------------------
```
```
[~DeviceA] display storm suppression multicast interface 100ge 1/0/1
------------------------------------------------------------------------------------------------
                            Configured                           Current            
interface        percent(%) cir(kbps) cbs(bytes)     pps percent(%) cir(kbps) cbs(bytes)     pps
------------------------------------------------------------------------------------------------
100GE1/0/1                80        --         --      --         80        --         --      --
------------------------------------------------------------------------------------------------
```
```
[~DeviceA] display storm suppression unknown-unicast interface 100ge 1/0/1
------------------------------------------------------------------------------------------------
                            Configured                           Current            
interface        percent(%) cir(kbps) cbs(bytes)     pps percent(%) cir(kbps) cbs(bytes)     pps
------------------------------------------------------------------------------------------------
100GE1/0/1                --       100      18800      --         --       100      18800      --
------------------------------------------------------------------------------------------------
```

The **Configured** field displays the configured traffic suppression percentage, CIR, and committed burst size (CBS). The **Current** field displays the effective traffic suppression percentage, CIR, and CBS. The preceding command output shows that the maximum rate of broadcast packets is 100 kbit/s, the percentage of interface bandwidth occupied by unknown multicast packets is 80%, and the maximum rate of unknown unicast packets is 100 kbit/s on 100GE1/0/1 of DeviceA in the inbound direction.


#### Configuration Scripts

DeviceA

```
# 
sysname DeviceA
# 
interface 100GE1/0/1
 storm suppression broadcast cir 100 kbps
 storm suppression multicast 80
 storm suppression unknown-unicast cir 100 kbps
#
return
```