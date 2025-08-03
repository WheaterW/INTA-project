Example for Configuring Static MLD Snooping
===========================================

Example for Configuring Static MLD Snooping

#### Networking Requirements

On the multicast network shown in [Figure 1](#EN-US_TASK_0000001321630886__fig_dc_cfg_vxlan_cfgcase_000201), a router (marked as Router) connects to user networks through a Layer 2 device (marked as Device). Static MLD multicast groups are configured on the user-side Layer 3 VLANIF interface of Router, but MLD is not configured. There are four receivers on the network: UserA, UserB, UserC, and UserD. UserA and UserB want to receive data of multicast groups FF16::1 to FF16::3 for a long time, and UserC and UserD want to receive data of multicast groups FF16::4 to FF16::5 for a long time. To meet these requirements, configure static router ports and static member ports for MLD snooping on Device.

**Figure 1** Network diagram of configuring static ports to implement Layer 2 multicast![](../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.

![](figure/en-us_image_0000001494698705.png)



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create a VLAN on Device and add related interfaces to the VLAN.
2. Enable MLD snooping globally and in the VLAN.
3. Configure a static router port.
4. Configure static member ports.


#### Procedure

1. Create a VLAN and add related interfaces to the VLAN.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname Device
   [*HUAWEI] commit
   [~Device] vlan 10
   [*Device-vlan10] quit
   [*Device] interface 100ge 1/0/1
   [*Device-100GE1/0/1] port link-type access
   [*Device-100GE1/0/1] port default vlan 10
   [*Device-100GE1/0/1] quit
   [*Device] interface 100ge 1/0/2
   [*Device-100GE1/0/2] port link-type access
   [*Device-100GE1/0/2] port default vlan 10
   [*Device-100GE1/0/2] quit
   [*Device] interface 100ge 1/0/3
   [*Device-100GE1/0/3] port link-type trunk
   [*Device-100GE1/0/3] port trunk allow-pass vlan 10
   [*Device-100GE1/0/3] commit
   [~Device-100GE1/0/3] quit
   ```
2. Enable MLD snooping.
   
   
   
   # Enable MLD snooping globally.
   
   ```
   [~Device] mld snooping enable
   ```
   
   # Enable MLD snooping in VLAN 10.
   
   ```
   [*Device] vlan 10
   [*Device-vlan10] mld snooping enable
   [*Device-vlan10] commit
   [~Device-vlan10] quit
   ```
3. Configure a static router port.
   
   
   ```
   [~Device] interface 100ge 1/0/3
   [~Device-100GE1/0/3] mld snooping static-router-port vlan 10
   [*Device-100GE1/0/3] commit
   [~Device-100GE1/0/3] quit
   ```
4. Configure static member ports.
   
   
   ```
   [~Device] interface 100ge 1/0/1
   [~Device-100GE1/0/1] mld snooping static-group group-address ff16::1 to ff16::3 vlan 10
   [*Device-100GE1/0/1] quit
   [*Device] interface 100ge 1/0/2
   [*Device-100GE1/0/2] mld snooping static-group group-address ff16::4 to ff16::5 vlan 10
   [*Device-100GE1/0/2] commit
   [~Device-100GE1/0/2] quit
   ```

#### Verifying the Configuration

# Check the router port information on Device.

```
[~Device] display mld snooping router-port vlan 10 
 Port Name                       UpTime        Expires       Flags              
 ---------------------------------------------------------------------          
 VLAN 10, 1 router-port(s)                                                     
 100GE1/0/3                        00h20m09s     --            STATIC
```

The command output shows that 100GE1/0/3 has become a static router port.

# Check the member port information on Device.

```
[~Device] display mld snooping port-info vlan 10 
 -------------------------------------------------------------------------------
  Flag: S:Static     D:Dynamic     M:Ssm-mapping                                
        A:Active     P:Protocol    T:Trill                               
                     (Source, Group)  Port                                  Flag
 -------------------------------------------------------------------------------
 VLAN 10, 5 Entry(s)                                                            
         (*, FF16::1)                                                       P-- 
                                      100GE1/0/1                             S-- 
                                                        1 port(s) include       
         (*, FF16::2)                                                       P-- 
                                      100GE1/0/1                             S-- 
                                                        1 port(s) include       
         (*, FF16::3)                                                       P-- 
                                      100GE1/0/1                             S-- 
                                                        1 port(s) include       
         (*, FF16::4)                                                       P-- 
                                      100GE1/0/2                             S-- 
                                                        1 port(s) include       
         (*, FF16::5)                                                       P-- 
                                      100GE1/0/2                             S-- 
                                                        1 port(s) include       
 --------------------------------------------------------------------------------
```

The command output shows that multicast groups FF16::1 to FF16::3 have static member port 100GE1/0/1 on Device, and multicast groups FF16::4 to FF16::5 have static member port 100GE1/0/2 on Device.


#### Configuration Scripts

```
#
sysname Device
#
vlan batch 10
#
mld snooping enable
#
vlan 10
 mld snooping enable
#
interface 100GE1/0/1
 port default vlan 10
 mld snooping static-group group-address FF16::1 to FF16::3 vlan 10 
#
interface 100GE1/0/2
 port default vlan 10
 mld snooping static-group group-address FF16::4 to FF16::5 vlan 10 
#
interface 100GE1/0/3
 port link-type trunk
 port trunk allow-pass vlan 10
 mld snooping static-router-port vlan 10 
#
return
```