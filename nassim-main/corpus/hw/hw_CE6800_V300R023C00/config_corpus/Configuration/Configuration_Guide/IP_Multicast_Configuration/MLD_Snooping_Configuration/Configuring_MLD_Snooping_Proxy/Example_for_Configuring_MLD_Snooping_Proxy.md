Example for Configuring MLD Snooping Proxy
==========================================

Example for Configuring MLD Snooping Proxy

#### Networking Requirements

[Figure 1](#EN-US_TASK_0000001372791621__fig_dc_cfg_vxlan_cfgcase_000401) shows an IPv6 multicast network on which a router (Router) runs MLDv1 and connects to a user network through a Layer 2 device (Device). There are a large number of receiver hosts on the network. The administrator wants to ensure that MLD message exchange does not burden Router while also ensuring that data receiving remains unaffected. To meet these requirements, configure MLD snooping proxy on Device.

**Figure 1** Networking diagram for configuring MLD snooping proxy![](../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.

![](figure/en-us_image_0000001444179326.png)



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create a VLAN and add related interfaces to the VLAN.
2. Enable MLD snooping globally and in the VLAN so that users can receive multicast data.
3. Configure MLD snooping proxy to reduce the number of messages exchanged between Device and Router.
4. Disable Device from sending Query messages to the upstream interface, preventing querier reelection.

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
   ```
   
   
   
   # Specify MLD snooping v2 so that the device can process MLD messages of all versions.
   
   ```
   [~Device-vlan10] mld snooping version 2
   [*Device-vlan10] commit
   ```
3. Enable MLD snooping proxy.
   
   
   ```
   [~Device-vlan10] mld snooping proxy
   [*Device-vlan10] commit
   [~Device-vlan10] quit
   ```
4. Disable Device from sending Query messages to the upstream interface.
   
   
   ```
   [~Device] interface 100ge 1/0/3
   [~Device-100GE1/0/3] mld snooping proxy-uplink-port vlan 10
   [*Device-100GE1/0/3] commit
   [~Device-100GE1/0/3] quit
   ```

#### Verifying the Configuration

# Check MLD message statistics on Device.

```
[~Device] display mld snooping statistics vlan 10
 MLD Snooping Packets Counter:                                                      
   Statistics for VLAN 10                                                            
     Receive V1 Report:          0                                                   
     Receive V2 Report:          1121                                                                                                 
     Receive V1 Query:           0                                                   
     Receive V2 Query:           2                                                                                                    
     Receive Done:               0                                                   
     Receive Pim Hello:          4                                                   
     Send Query (S=0):           0                                                   
     Send Query (S!=0):          -                                                   
     Proxy Send General Query:             13                                     
     Proxy Send Group-Specific Query:         0                                      
     Proxy Send Group-Source-Specific Query:  0  
     Recv Invalid Packet                      0
     Recv Ignore Packet                       0
     Foward Report           1121
     Foward Done             0        Foward Query            2
```

The command output shows that Device has sent General Query messages as a proxy device, indicating that the MLD snooping proxy function has taken effect.


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
 mld snooping version 2
 mld snooping proxy
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
 mld snooping proxy-uplink-port vlan 10 
#
return
```