Example for Configuring Basic IGMP Snooping Functions
=====================================================

Example for Configuring Basic IGMP Snooping Functions

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0000001130781908__fig75201555914), the router runs IGMPv2 and is connected to user hosts through a Layer 2 device (marked as Device). The multicast source (marked as Source) sends multicast data to groups 225.1.1.1 to 225.1.1.3. There are three multicast receivers (HostA, HostB, and HostC) on the network. It is required that basic IGMP snooping functions be configured on Device.

**Figure 1** Network diagram of configuring basic IGMP snooping functions![](../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.


  
![](figure/en-us_image_0000001176741595.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create a VLAN on Device and add related interfaces to the VLAN.
2. Enable IGMP snooping globally and in the VLAN.

#### Procedure

1. Create a VLAN and add related interfaces to the VLAN.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname Device
   [*HUAWEI] commit
   [~Device] vlan 10
   [*Device-vlan10] quit
   [*Device] interface  100ge 1/0/1
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

#### Verifying the Configuration

# Check the member port information on Device.

```
[~Device] display igmp snooping port-info vlan 10 
 -------------------------------------------------------------------------------
  Flag: S:Static     D:Dynamic     M:Ssm-mapping                                
        A:Active     P:Protocol    T:Trill                               
                     (Source, Group)  Port                                  Flag
 -------------------------------------------------------------------------------
 VLAN 10, 3 Entry(s)                                                            
                      (*, 225.1.1.1)                                        PA- 
                                      100GE1/0/1                             -D- 
                                      100GE1/0/2                             -D- 
                                                        2 port(s) include       
                      (*, 225.1.1.2)                                        PA- 
                                      100GE1/0/1                             -D- 
                                      100GE1/0/2                             -D- 
                                                        2 port(s) include       
                      (*, 225.1.1.3)                                        PA- 
                                      100GE1/0/1                             -D- 
                                      100GE1/0/2                             -D- 
                                                        2 port(s) include       
 -------------------------------------------------------------------------------
```

The command output on Device shows that dynamic member ports of multicast groups 225.1.1.1 to 225.1.1.3 are 100GE1/0/1 and 100GE1/0/2.

# Check the router port information on Device.

```
[~Device] display igmp snooping router-port vlan 10 
 Port Name                            UpTime        Expires       Flags
 -------------------------------------------------------------------------- 
 VLAN 10, 1 router-port(s)
 100GE1/0/3                            12h03m12s     00h02m31s     DYNAMIC
```

The command output shows that the router port is 100GE1/0/3.


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
  #
  interface 100GE1/0/2
   port default vlan 10
  #
  interface 100GE1/0/3
   port link-type trunk
   port trunk allow-pass vlan 10
  #
  return
  ```