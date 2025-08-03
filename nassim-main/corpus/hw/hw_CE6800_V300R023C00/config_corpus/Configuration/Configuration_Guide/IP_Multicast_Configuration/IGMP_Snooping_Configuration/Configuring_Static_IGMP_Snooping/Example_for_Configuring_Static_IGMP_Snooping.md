Example for Configuring Static IGMP Snooping
============================================

Example for Configuring Static IGMP Snooping

#### Networking Requirements

On the multicast network shown in [Figure 1](#EN-US_TASK_0000001130622110__fig_dc_cfg_vxlan_cfgcase_000201), a router (marked Router) connects to a user network through a Layer 2 device (marked Device). Static IGMP multicast groups 225.1.1.1 to 225.1.1.5 are configured on the user-side Layer 3 VLANIF interface of Router, but IGMP is not configured. UserA and UserB want to receive data from groups 225.1.1.1 to 225.1.1.3 for an extended period, and UserC and UserD want to receive data from groups 225.1.1.4 to 225.1.1.5 for an extended period. To meet these requirements, configure static router ports and static member ports for IGMP snooping on Device.

**Figure 1** Network diagram of configuring static ports to implement Layer 2 multicast![](../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.

![](figure/en-us_image_0000001130622134.png)



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create a VLAN on Device and add related interfaces to the VLAN.
2. Enable IGMP snooping globally and in the VLAN.
3. Configure a static router port.
4. Configure a static member port.


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
2. Enable IGMP snooping.
   
   
   
   # Enable IGMP snooping globally.
   
   ```
   [~Device] igmp snooping enable
   ```
   
   # Enable IGMP snooping in VLAN10.
   
   ```
   [*Device] vlan 10
   [*Device-vlan10] igmp snooping enable
   [*Device-vlan10] commit
   [~Device-vlan10] quit
   ```
3. Configure a static router port.
   
   
   ```
   [~Device] interface 100ge 1/0/3
   [~Device-100GE1/0/3] igmp snooping static-router-port vlan 10
   [*Device-100GE1/0/3] commit
   [~Device-100GE1/0/3] quit
   ```
4. Configure a static member port.
   
   
   ```
   [~Device] interface 100ge 1/0/1
   [~Device-100GE1/0/1] igmp snooping static-group group-address 225.1.1.1 to 225.1.1.3 vlan 10
   [*Device-100GE1/0/1] quit
   [*Device] interface 100ge 1/0/2
   [*Device-100GE1/0/2] igmp snooping static-group group-address 225.1.1.4 to 225.1.1.5 vlan 10
   [*Device-100GE1/0/2] commit
   [~Device-100GE1/0/2] quit
   ```

#### Verifying the Configuration

# Check the router port information on Device.

```
[~Device] display igmp snooping router-port vlan 10 
 Port Name                       UpTime        Expires       Flags              
 ---------------------------------------------------------------------          
 VLAN 10, 1 router-port(s)                                                     
 100GE1/0/3                        00h20m09s     --            STATIC
```

The command output shows that 100GE1/0/3 has become a static router port.

# Check the member port information on Device.

```
[~Device] display igmp snooping port-info vlan 10 
 -------------------------------------------------------------------------------
  Flag: S:Static     D:Dynamic     M:Ssm-mapping                                
        A:Active     P:Protocol    T:Trill                               
                     (Source, Group)  Port                                  Flag
 -------------------------------------------------------------------------------
 VLAN 10, 5 Entry(s)                                                            
                      (*, 225.1.1.1)                                        P-- 
                                      100GE1/0/1                             S-- 
                                                        1 port(s) include       
                      (*, 225.1.1.2)                                        P-- 
                                      100GE1/0/1                             S-- 
                                                        1 port(s) include       
                      (*, 225.1.1.3)                                        P-- 
                                      100GE1/0/1                             S-- 
                                                        1 port(s) include       
                      (*, 225.1.1.4)                                        P-- 
                                      100GE1/0/2                             S-- 
                                                        1 port(s) include       
                      (*, 225.1.1.5)                                        P-- 
                                      100GE1/0/2                             S-- 
                                                        1 port(s) include       
 --------------------------------------------------------------------------------
```

The command output shows that groups 225.1.1.1 to 225.1.1.3 have a static member port 100GE1/0/1 on Device and groups 225.1.1.4 to 225.1.1.5 have a static member port 100GE1/0/2 on Device.


#### Configuration Scripts

* Device
  ```
  #
  sysname Device
  #
  vlan batch 10
  #
  igmp snooping enable
  #
  vlan 10
   igmp snooping enable
  #
  interface 100GE1/0/1
   port default vlan 10
   igmp snooping static-group group-address 225.1.1.1 to 225.1.1.3 vlan 10 
  #
  interface 100GE1/0/2
   port default vlan 10
   igmp snooping static-group group-address 225.1.1.4 to 225.1.1.5 vlan 10 
  #
  interface 100GE1/0/3
   port link-type trunk
   port trunk allow-pass vlan 10
   igmp snooping static-router-port vlan 10 
  #
  return
  ```