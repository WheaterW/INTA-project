Example for Configuring an IGMP Snooping Querier
================================================

Example for Configuring an IGMP Snooping Querier

#### Networking Requirements

On the pure Layer 2 network shown in [Figure 1](#EN-US_TASK_0000001847202941__fig_dc_cfg_vxlan_cfgcase_000401), multicast sources Source1 and Source2 send multicast data to multicast groups 224.1.1.1 and 225.1.1.1, respectively. UserA and UserC want to receive the data of multicast group 224.1.1.1; UserB and UserD want to receive data of multicast group 225.1.1.1. All devices run IGMP Snooping V2 by default.

**Figure 1** Network diagram for configuring an IGMP snooping querier![](../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, interface3, and interface4 represent 100GE1/0/1, 100GE1/0/2, 100GE1/0/3, and 100GE1/0/4, respectively.

![](figure/en-us_image_0000001847282881.png)



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create a VLAN and add related interfaces to the VLAN.
2. Enable IGMP snooping globally and in the VLAN so that users can receive multicast data.
3. Configure a device close to the source as the IGMP snooping querier. In this example, DeviceA is used.
4. Enable all the devices to discard unknown multicast packets. In this way, the devices will not broadcast multicast data in a VLAN when there is no corresponding Layer 2 forwarding entry.

#### Procedure

1. Create a VLAN and add related interfaces to the VLAN.
   
   
   
   # Configure DeviceA.
   
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] vlan 10
   [*DeviceA-vlan10] quit
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] port link-type access
   [*DeviceA-100GE1/0/1] port default vlan 10
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] port link-type access
   [*DeviceA-100GE1/0/2] port default vlan 10
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100ge 1/0/3
   [*DeviceA-100GE1/0/3] port link-type trunk
   [*DeviceA-100GE1/0/3] port trunk allow-pass vlan 10
   [*DeviceA-100GE1/0/3] commit
   [~DeviceA-100GE1/0/3] quit
   ```
   
   The configurations of DeviceB, DeviceC, and DeviceD are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
2. Enable IGMP snooping.
   
   
   
   # Enable IGMP snooping globally on DeviceA.
   
   ```
   [~DeviceA] igmp snooping enable
   ```
   
   # Enable IGMP snooping in VLAN 10 on DeviceA.
   
   ```
   [*DeviceA] vlan 10
   [*DeviceA-vlan10] igmp snooping enable
   [*DeviceA-vlan10] commit
   ```
   
   
   
   The configurations of DeviceB, DeviceC, and DeviceD are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
3. Configure DeviceA as the querier.
   
   
   ```
   [~DeviceA-vlan10] igmp snooping querier enable
   [*DeviceA-vlan10] commit
   ```
4. Enable all the devices to discard unknown multicast packets.
   
   
   
   # Configure DeviceA.
   
   
   
   ```
   [~DeviceA-vlan10] unknown-multicast discard
   [*DeviceA-vlan10] commit
   [~DeviceA-vlan10] quit
   ```
   
   The configurations of DeviceB, DeviceC, and DeviceD are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.

#### Verifying the Configuration

# After the IGMP snooping querier begins to work, all the devices except the IGMP snooping querier receive IGMP General Query messages. Run the [**display igmp snooping statistics**](cmdqueryname=display+igmp+snooping+statistics) command on DeviceB to view IGMP message statistics.

```
[~DeviceB] display igmp snooping statistics vlan 10
 IGMP Snooping Packets Counter:                                                      
   Statistics for VLAN 10                                                            
     Receive V1 Report:          0                                                   
     Receive V2 Report:          32                                                
     Receive V3 Report:          0                                                   
     Receive V1 Query:           0                                                   
     Receive V2 Query:        30                                                   
     Receive V3 Query:           0                                                   
     Receive Leave:              0                                                   
     Receive Pim Hello:          0                                                   
     Send Query (S=0):           0                                                   
     Send Query (S!=0):          -                                                   
     Proxy Send General Query:                0                                     
     Proxy Send Group-Specific Query:         0                                      
     Proxy Send Group-Source-Specific Query:  0  
     Recv Invalid Packet:                     0
     Recv Ignore Packet:                      0
     Foward Report:              1121
     Foward Leave:               0
     Foward Query:               2
```

# Run the **[**display igmp snooping**](cmdqueryname=display+igmp+snooping) vlan** command on the querier to check whether a VLAN takes effect on the querier.

```
[~DeviceA] display igmp snooping vlan 10
  IGMP Snooping Information for VLAN 10
     IGMP Snooping is Enabled
     IGMP Version is Set to default 2
     IGMP Query Interval is Set to default 60
     IGMP Max Response Interval is Set to default 10
     IGMP Robustness is Set to default 2
     IGMP Last Member Query Interval is Set to default 1
     IGMP Router Port Aging Interval is Set to 180s or holdtime in hello
     IGMP Filter Group-Policy is Set to default : Permit All
     IGMP Filter IP-Source-Policy is Set to default : Permit All
     IGMP Filter Query IP-Source-Policy is Set to default : Permit All
     IGMP Prompt Leave Disable
     IGMP Router Alert is Not Required
     IGMP Send Router Alert Enable
     IGMP Router Port Learning Enable
     IGMP Proxy Disable
     IGMP Proxy Router Protocol Action is Set to default: Terminate All
     IGMP Report Suppress Disable
     IGMP Querier Enable
     IGMP Snooping Explicit-tracking Disable
     IGMP Snooping querier-election Disable
     IGMP ASM-SSM
     IGMP SSM-Mapping Disable
     IGMP Suppress-dynamic-join Disable
     IGMP Query Source IP Address is 192.168.0.1
```

# Run the **[**display igmp snooping querier**](cmdqueryname=display+igmp+snooping+querier) vlan** command on the querier to view the querier status.

```
[~DeviceA] display igmp snooping querier vlan 10
 VLAN                            Querier-state Querier
---------------------------------------------------------------
 10                              Enable        192.168.0.1
```

The command output shows that the source address in a Query message is 192.168.0.1 by default. In some scenarios, this address may be used by other devices. You can run the [**igmp snooping send-query source-address**](cmdqueryname=igmp+snooping+send-query+source-address) command to change the source address of Query messages.


#### Configuration Scripts

* DeviceA
  ```
  #
  sysname DeviceA
  #
  vlan batch 10
  #
  igmp snooping enable
  #
  vlan 10
   unknown-multicast discard
   igmp snooping enable
   igmp snooping querier enable
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

* DeviceB
  ```
  #
  sysname DeviceB
  #
  vlan batch 10
  #
  igmp snooping enable
  #
  vlan 10
   unknown-multicast discard
   igmp snooping enable
  #
  interface 100GE1/0/1
   port default vlan 10
  #
  interface 100GE1/0/2
   port default vlan 10
  #
  interface 100GE1/0/3
   port default vlan 10
  #
  interface 100GE1/0/4
   port link-type trunk
   port trunk allow-pass vlan 10
  #
  return
  ```

* DeviceC
  ```
  #
  sysname DeviceC
  #
  vlan batch 10
  #
  igmp snooping enable
  #
  vlan 10
   unknown-multicast discard
   igmp snooping enable
  #
  interface 100GE1/0/1
   port default vlan 10
  #
  interface 100GE1/0/2
   port default vlan 10
  #
  interface 100GE1/0/3
   port default vlan 10
  #
  return
  ```

* DeviceD
  ```
  #
  sysname DeviceD
  #
  vlan batch 10
  #
  igmp snooping enable
  #
  vlan 10
   unknown-multicast discard
   igmp snooping enable
  #
  interface 100GE1/0/1
   port default vlan 10
  #
  interface 100GE1/0/2
   port default vlan 10
  #
  return
  ```