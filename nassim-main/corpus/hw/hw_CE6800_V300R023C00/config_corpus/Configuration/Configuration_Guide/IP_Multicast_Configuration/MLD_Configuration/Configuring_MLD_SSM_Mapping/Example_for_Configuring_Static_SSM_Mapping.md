Example for Configuring Static SSM Mapping
==========================================

Example for Configuring Static SSM Mapping

#### Networking Requirements

The network shown in [Figure 1](#EN-US_TASK_0000001589256137__fig_01) runs PIM-SM and uses SSM to provide IPv6 multicast services for group members. DeviceD's interface connected to Receiver's network segment runs MLDv2. Because Receiver runs MLDv1 and does not support MLDv2, it cannot specify multicast sources when it joins a multicast group. The SSM group address range on the network is FF31::/32. Source1, Source2, and Source3 all send multicast data to the multicast groups in this range.

Receiver wants to obtain the SSM service and receive IPv6 multicast data only from Source1 and Source3 while blocking multicast data from Source2.

**Figure 1** Network diagram of configuring static SSM mapping![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.


  
![](figure/en-us_image_0000001538257286.png)

| Device | Interface | IPv6 Address |
| --- | --- | --- |
| DeviceA | 100GE1/0/1 | 2001:db8:5::2/64 |
| 100GE1/0/2 | 2001:db8:1::1/64 |
| 100GE1/0/3 | 2001:db8:3::1/64 |
| DeviceB | 100GE1/0/1 | 2001:db8:6::2/64 |
| 100GE1/0/2 | 2001:db8:1::2/64 |
| 100GE1/0/3 | 2001:db8:2::1/64 |
| DeviceC | 100GE1/0/1 | 2001:db8:7::2/64 |
| 100GE1/0/2 | 2001:db8:4::1/64 |
| 100GE1/0/3 | 2001:db8:2::2/64 |
| DeviceD | 100GE1/0/1 | 2001:db8:8::2/64 |
| 100GE1/0/2 | 2001:db8:4::2/64 |
| 100GE1/0/3 | 2001:db8:3::2/64 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IPv6 addresses and a unicast routing protocol for interfaces on each device to ensure connectivity at the network layer.
2. Configure basic IPv6 multicast functions on each device to implement multicast data forwarding on the network.
3. Enable MLD SSM mapping on DeviceD.

#### Procedure

1. Configure IPv6 addresses and a unicast routing protocol for interfaces on each device.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] ospfv3 1
   [*DeviceA-ospfv3-1] quit
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ipv6 enable
   [*DeviceA-100GE1/0/1] ipv6 address 2001:db8:5::2 64
   [*DeviceA-100GE1/0/1] ospfv3 1 area 0.0.0.0
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] undo portswitch
   [*DeviceA-100GE1/0/2] ipv6 enable
   [*DeviceA-100GE1/0/2] ipv6 address 2001:db8:1::1 64
   [*DeviceA-100GE1/0/2] ospfv3 1 area 0.0.0.0
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100ge 1/0/3
   [*DeviceA-100GE1/0/3] undo portswitch
   [*DeviceA-100GE1/0/3] ipv6 enable
   [*DeviceA-100GE1/0/3] ipv6 address 2001:db8:3::1 64
   [*DeviceA-100GE1/0/3] ospfv3 1 area 0.0.0.0
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB, DeviceC, and DeviceD are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
2. Enable the multicast function on all the devices and enable IPv6 PIM-SM on all the involved interfaces.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] multicast ipv6 routing-enable
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] pim ipv6 sm
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] pim ipv6 sm
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100ge 1/0/3
   [*DeviceA-100GE1/0/3] pim ipv6 sm
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB, DeviceC, and DeviceD are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
3. Enable MLD on the interfaces connected to user hosts.
   
   
   
   # Enable MLD on 100GE1/0/1 of DeviceD and set the version to MLDv2.
   
   ```
   [~DeviceD] interface 100ge 1/0/1
   [*DeviceD-100GE1/0/1] mld enable
   [*DeviceD-100GE1/0/1] mld version 2
   [*DeviceD-100GE1/0/1] quit
   [*DeviceD] commit
   ```
4. Enable MLD SSM mapping on the interface connected to the user host.
   
   
   
   # Enable MLD SSM mapping on 100GE1/0/1 of DeviceD.
   
   ```
   [~DeviceD] interface 100ge 1/0/1
   [*DeviceD-100GE1/0/1] mld ssm-mapping enable
   [*DeviceD-100GE1/0/1] quit
   [*DeviceD] commit
   ```
5. Configure the SSM group address range on all devices.
   
   
   
   # Set the SSM group address range to FF31::/32 on DeviceA.
   
   ```
   [~DeviceA] acl ipv6 number 2000
   [*DeviceA-acl6-basic-2000] rule permit source ff31::/32
   [*DeviceA-acl6-basic-2000] quit
   [*DeviceA] pim ipv6
   [*DeviceA-pim6] ssm-policy 2000
   [*DeviceA-pim6] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB, DeviceC, and DeviceD are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
6. Configure MLD SSM mapping rules on the device connected to the user host.
   
   
   
   # On DeviceD, map the multicast groups in the range of FF31::/32 to Source1 and Source3.
   
   ```
   [~DeviceD] mld
   [*DeviceD-mld] ssm-mapping ff31:: 32 2001:db8:5::1
   [*DeviceD-mld] ssm-mapping ff31:: 32 2001:db8:7::1
   [*DeviceD-mld] quit
   [*DeviceD] commit
   ```

#### Verifying the Configuration

# Run the **display mld ssm-mapping group** command on DeviceD to check the mappings between multicast sources and groups.

```
<DeviceD> display mld ssm-mapping group
MLD SSM-Mapping conversion table of VPN Instance: public net
 Total entries: 2    (2 entries matched)

 00001: (2001:DB8:5::1, FF31::)
 00002: (2001:DB8:7::1, FF31::)

 Total 2 entries matched
```

The command output shows that the multicast groups in the range FF31::/32 have been mapped to Source1 and Source3.

# Run the **display mld group ssm-mapping** command on DeviceD to check information about multicast groups created based on SSM mapping rules.

```
<DeviceD> display mld group ssm-mapping
MLD SSM mapping interface group report information of VPN Instance: public net
 Limited entry of this VPN Instance: - 
 100GE1/0/1 (2001:DB8:8::2):
  Total 1 MLD SSM-Mapping Group reported
   Group Address   Last Reporter   Uptime      Expires
   FF31::1        2001:DB8:8::1  00:01:44    00:00:26
```

The command output shows that Receiver has joined group FF31::1.

# Run the **display pim ipv6 routing-table** command on DeviceD to check the IPv6 PIM-SM routing table.

```
<DeviceD> display pim ipv6 routing-table
VPN-Instance: public net
 Total 2 (S, G) entries

 (2001:DB8:5::1, FF31::1)
     Protocol: pim-ssm, Flag: SG_RCVR                                           
     UpTime: 00:19:40                                                           
     Upstream interface: 100GE1/0/3                                              
         Upstream neighbor: 2001:DB8:3::1                                        
         RPF prime neighbor:  2001:DB8:3::1                                       
     Downstream interface(s) information:                                       
     Total number of downstreams: 1                                             
         1: 100GE1/0/1                                                           
             Protocol: mld, UpTime: 00:19:40, Expires: -                    

 (2001:DB8:7::1, FF31::1)
     Protocol: pim-ssm, Flag: SG_RCVR                                           
     UpTime: 00:19:40                                                           
     Upstream interface: 100GE1/0/2                                                
         Upstream neighbor: 2001:DB8:4::1                                         
         RPF prime neighbor: 2001:DB8:4::1                                        
     Downstream interface(s) information:                                       
     Total number of downstreams: 1                                             
         1: 100GE1/0/1                                                            
             Protocol: mld, UpTime: 00:19:40, Expires: -                    
```

The command output shows that multicast sources 2001:DB8:5::1 and 2001:DB8:7::1 send multicast data to multicast group FF31::1, and DeviceD receives the data from the two multicast sources through 100GE1/0/3 and 100GE1/0/2.


#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  multicast ipv6 routing-enable
  #
  acl ipv6 number 2000
   rule permit source ff31::/32
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:5::2/64
   pim ipv6 sm
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:1::1/64
   pim ipv6 sm
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/3
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:3::1/64
   pim ipv6 sm
   ospfv3 1 area 0.0.0.0
  #
  ospfv3 1
    router-id 1.1.1.1
    area 0.0.0.0
  #
  pim ipv6
   ssm-policy 2000
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  multicast ipv6 routing-enable
  #
  acl ipv6 number 2000
   rule permit source ff31::/32
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:6::2/64
   pim ipv6 sm
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:1::2/64
   pim ipv6 sm
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/3
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:2::1/64
   pim ipv6 sm
   ospfv3 1 area 0.0.0.0
  #
  ospfv3 1
    router-id 2.2.2.2
    area 0.0.0.0
  #
  pim ipv6
   ssm-policy 2000
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  multicast ipv6 routing-enable
  #
  acl ipv6 number 2000
   rule permit source ff31::/32
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:7::2/64
   pim ipv6 sm
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:4::1/64
   pim ipv6 sm
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/3
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:2::2/64
   pim ipv6 sm
   ospfv3 1 area 0.0.0.0
  #
  ospfv3 1
    router-id 3.3.3.3
    area 0.0.0.0
  #
  pim ipv6
   ssm-policy 2000
  #
  return
  ```
* DeviceD
  
  ```
  #
  sysname DeviceD
  #
  multicast ipv6 routing-enable
  #
  acl ipv6 number 2000
   rule permit source ff31::/32
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:8::2/64
   pim ipv6 sm
   mld enable
   mld version 2
   mld ssm-mapping enable
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:4::2/64
   pim ipv6 sm
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/3
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:3::2/64
   pim ipv6 sm
   ospfv3 1 area 0.0.0.0
  #
  mld
   ssm-mapping ff31:: 32 2001:DB8:5::1
   ssm-mapping ff31:: 32 2001:DB8:7::1
  #
  ospfv3 1
    router-id 4.4.4.4
    area 0.0.0.0
  #
  pim ipv6
   ssm-policy 2000
  #
  return
  ```