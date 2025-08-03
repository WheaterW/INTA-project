Example for Configuring an Eth-Trunk Interface to Work in Dynamic LACP Mode
===========================================================================

Example for Configuring an Eth-Trunk Interface to Work in Dynamic LACP Mode

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001130621712__fig_dc_cfg_eth-trunk_006701), ServerA is directly connected to DeviceA through an Eth-Trunk in dynamic LACP mode. The two devices negotiate link aggregation using dynamic LACPDUs.

**Figure 1** Networking diagram of an Eth-Trunk in dynamic LACP mode![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001176661303.png "Click to enlarge")

#### Procedure

1. Create an Eth-Trunk interface in dynamic LACP mode on DeviceA and add Ethernet physical interfaces to the Eth-Trunk interface.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface eth-trunk 1
   [*DeviceA-Eth-Trunk1] mode lacp-dynamic
   [*DeviceA-Eth-Trunk1] quit
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] eth-trunk 1
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] eth-trunk 1
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100ge 1/0/3
   [*DeviceA-100GE1/0/3] eth-trunk 1
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] commit
   ```
2. On DeviceA, set the upper threshold for the number of active interfaces to 2.
   
   
   ```
   [~DeviceA] interface eth-trunk 1
   [~DeviceA-Eth-Trunk1] lacp max active-linknumber 2
   [*DeviceA-Eth-Trunk1] quit
   [*DeviceA] commit
   ```
3. Set LACP interface priorities and determine active interfaces on DeviceA.
   
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] lacp priority 100
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] lacp priority 100
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Run the **display eth-trunk** command on DeviceA to check Eth-Trunk information.

```
[~DeviceA] display eth-trunk 1
Eth-Trunk1's state information is:                                                                                                  
Local:                                                                                                                              
LAG ID: 1                       Working Mode: Dynamic                                                                               
Preempt Delay: Disabled         Hash Arithmetic: profile default                                                                    
System Priority: 32768          System ID: xxxx-xxxx-xxxx                                                                           
Least Active-linknumber: 1      Max Active-linknumber: 2                                                                            
Operating Status: up            Number Of Up Ports In Trunk: 0                                                                      
Timeout Period: Slow
--------------------------------------------------------------------------------                                                    
ActorPortName          Status   PortType PortPri PortNo PortKey PortState Weight                                                    
100GE1/0/1              Indep    100GE    100     0      321     10100010  1                                                         
100GE1/0/2              Indep    100GE    100     1      321     10100010  1                                                         
100GE1/0/3              Indep    100GE    32768   2      321     10100010  1                                                         
                                                                                                                                    
Partner:                                                                                                                            
--------------------------------------------------------------------------------                                                    
ActorPortName          SysPri   SystemID        PortPri PortNo PortKey PortState                                                    
100GE1/0/1              0        xxxx-xxxx-xxxx 0       0      0       10100011                                                     
100GE1/0/2              0        xxxx-xxxx-xxxx 0       0      0       10100011                                                     
100GE1/0/3              0        xxxx-xxxx-xxxx 0       0      0       10100011
```

The command output shows that the Eth-Trunk ID is 1, dynamic LACP mode is used, and Eth-Trunk member interfaces **100GE** **1/0/1**, **100GE** **1/0/2**, and **100GE** **1/0/3** are in Indep state.

# After DeviceA receives LACPDUs from ServerA and link aggregation negotiation between DeviceA and ServerA succeeds, run the **display eth-trunk** command on DeviceA to check Eth-Trunk information.

```
[~DeviceA] display eth-trunk 1
Eth-Trunk1's state information is:                                                                                                  
Local:                                                                                                                              
LAG ID: 1                       Working Mode: Dynamic                                                                               
Preempt Delay: Disabled:        Hash Arithmetic: profile default                                                                    
System Priority: 32768          System ID: xxxx-xxxx-xxxx                                                                           
Least Active-linknumber: 1      Max Active-linknumber: 2                                                                            
Operating Status: up            Number Of Up Ports In Trunk: 2                                                                      
Timeout Period: Slow
--------------------------------------------------------------------------------                                                    
ActorPortName          Status   PortType PortPri PortNo PortKey PortState Weight                                                    
100GE1/0/1              Selected 100GE     100     0      321     10111100  1                                                         
100GE1/0/2              Selected 100GE     100     1      321     10111100  1                                                         
100GE1/0/3              Unselect 100GE     32768   2      321     10100000  1                                                         
                                                                                                                                    
Partner:                                                                                                                            
--------------------------------------------------------------------------------                                                    
ActorPortName          SysPri   SystemID        PortPri PortNo PortKey PortState                                                    
100GE1/0/1              32768    xxxx-xxxx-xxxx 32768   0      321     10111100                                                     
100GE1/0/2              32768    xxxx-xxxx-xxxx 32768   1      321     10111100                                                     
100GE1/0/3              32768    xxxx-xxxx-xxxx 32768   2      321     10100000
```

The command output shows that the Eth-Trunk ID is 1, dynamic LACP mode is used, Eth-Trunk member interfaces **100GE** **1/0/1** and **100GE** **1/0/2** are active interfaces and in Selected state, and interface **100GE** **1/0/3** is in Unselect state.

#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
interface Eth-Trunk1
 mode lacp-dynamic
 lacp max active-linknumber 2
#
interface 100GE1/0/1
 eth-trunk 1
 lacp priority 100
#
interface 100GE1/0/2
 eth-trunk 1
 lacp priority 100
#
interface 100GE1/0/3
 eth-trunk 1
#
return
```