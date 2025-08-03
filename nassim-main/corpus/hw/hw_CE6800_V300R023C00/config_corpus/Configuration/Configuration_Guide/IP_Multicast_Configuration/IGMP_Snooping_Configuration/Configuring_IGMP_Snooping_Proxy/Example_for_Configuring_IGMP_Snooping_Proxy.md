Example for Configuring IGMP Snooping Proxy
===========================================

Example for Configuring IGMP Snooping Proxy

#### Networking Requirements

[Figure 1](#EN-US_TASK_0000001176661659__fig_dc_cfg_vxlan_cfgcase_000401) shows an IPv4 multicast network on which a router (Router) runs IGMPv2 and connects to a user network through a Layer 2 device (Device). There are a large number of receiver hosts on the network. The administrator wants to ensure that IGMP message exchange does not burden Router while also ensuring that data receiving remains unaffected. To meet these requirements, configure IGMP snooping proxy on Device.

**Figure 1** Network diagram of IGMP snooping proxy![](../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.

![](figure/en-us_image_0000001130622142.png)



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create a VLAN and add related interfaces to the VLAN.
2. Enable IGMP snooping globally and in the VLAN so that users can receive multicast data.
3. Configure IGMP snooping proxy to reduce the number of messages exchanged between Device and Router.
4. Disable Device from sending Query messages to the upstream interface, preventing reelection of the IGMP querier.

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
   ```
   
   
   
   # Specify IGMP snooping v3 so that the device can process IGMP messages of all versions.
   
   ```
   [~Device-vlan10] igmp snooping version 3
   [*Device-vlan10] commit
   ```
3. Enable IGMP snooping proxy.
   
   
   ```
   [~Device-vlan10] igmp snooping proxy
   [*Device-vlan10] commit
   [~Device-vlan10] quit
   ```
4. Disable Device from sending Query messages to the upstream interface.
   
   
   ```
   [~Device] interface 100ge 1/0/3
   [~Device-100GE1/0/3] igmp snooping proxy-uplink-port vlan 10
   [*Device-100GE1/0/3] commit
   [~Device-100GE1/0/3] quit
   ```

#### Verifying the Configuration

# Check the IGMP message statistics on Device.

```
[~Device] display igmp snooping statistics vlan 10
 IGMP Snooping Packets Counter:                                                      
   Statistics for VLAN 10                                                            
     Receive V1 Report:          0                                                   
     Receive V2 Report:          1121                                                
     Receive V3 Report:          0                                                   
     Receive V1 Query:           0                                                   
     Receive V2 Query:           2                                                   
     Receive V3 Query:           0                                                   
     Receive Leave:              0                                                   
     Receive Pim Hello:          4                                                   
     Send Query (S=0):           0                                                   
     Send Query (S!=0):          -                                                   
     Proxy Send General Query:             13                                     
     Proxy Send Group-Specific Query:         0                                      
     Proxy Send Group-Source-Specific Query:  0  
     Recv Invalid Packet:                     0
     Recv Ignore Packet:                      0
     Foward Report:              1121
     Foward Leave:               0
     Foward Query:               2
```

The command output shows that Device has sent General Query messages as a proxy device, indicating that the IGMP snooping proxy function has taken effect.


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
   igmp snooping version 3
   igmp snooping proxy
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
   igmp snooping proxy-uplink-port vlan 10 
  #
  return
  ```