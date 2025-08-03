Example for Configuring Static SSM Mapping
==========================================

Example for Configuring Static SSM Mapping

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0000001130784218__fig_01), the network runs PIM-SM and uses the SSM model to provide multicast services to group members. DeviceD's interface connected to Receiver's network segment runs IGMPv3. Receiver runs IGMPv2 and does not support IGMPv3; therefore, Receiver cannot specify multicast sources when it joins a multicast group. The SSM group address range on the network is 232.1.1.0/24. Source1, Source2, and Source3 all send multicast data to the multicast groups in this range.

Receiver needs to obtain the SSM service and wants to receive multicast data only from Source1 and Source3 and block multicast data from Source2.

**Figure 1** Network diagram of configuring static SSM mapping![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.


  
![](figure/en-us_image_0000001176743909.png "Click to enlarge")

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IP addresses and a unicast routing protocol for interfaces on each device to ensure connectivity at the network layer.
2. Configure basic multicast functions on each device to implement multicast data forwarding on the network.
3. Enable IGMP SSM mapping on DeviceD and configure mapping rules.

#### Procedure

1. Configure interface IP addresses and a unicast routing protocol on each device.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ip address 10.10.1.2 24
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] undo portswitch
   [*DeviceA-100GE1/0/2] ip address 192.168.1.1 24
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100ge 1/0/3
   [*DeviceA-100GE1/0/3] undo portswitch
   [*DeviceA-100GE1/0/3] ip address 192.168.4.2 24
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] ospf 1
   [*DeviceA-ospf-1] area 0.0.0.0
   [*DeviceA-ospf-1-area-0.0.0.0] network 192.168.1.0 0.0.0.255
   [*DeviceA-ospf-1-area-0.0.0.0] network 192.168.4.0 0.0.0.255
   [*DeviceA-ospf-1-area-0.0.0.0] network 10.10.1.0 0.0.0.255
   [*DeviceA-ospf-1-area-0.0.0.0] quit
   [*DeviceB-ospf-1] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB, DeviceC, and DeviceD are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
2. Enable the multicast function on all the devices and enable PIM-SM on all the involved interfaces.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] multicast routing-enable
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] pim sm
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] pim sm
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100ge 1/0/3
   [*DeviceA-100GE1/0/3] pim sm
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB, DeviceC, and DeviceD are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
3. Enable IGMP on the interface connected to the user host.
   
   
   
   # Enable IGMP on DeviceD's interface1 and set the version to IGMPv3.
   
   ```
   [~DeviceD] interface 100ge 1/0/1
   [~DeviceD-100GE1/0/1] igmp enable
   [*DeviceD-100GE1/0/1] igmp version 3
   [*DeviceD-100GE1/0/1] quit
   [*DeviceD] commit
   ```
4. Enable IGMP SSM mapping on the interface connected to the user host.
   
   
   
   # Enable IGMP SSM mapping on DeviceD's interface1.
   
   ```
   [~DeviceD] interface 100ge 1/0/1
   [~DeviceD-100GE1/0/1] igmp ssm-mapping enable
   [*DeviceD-100GE1/0/1] quit
   [*DeviceD] commit
   ```
5. Configure the SSM group address range on all devices.
   
   
   
   # Set the SSM group address range to 232.1.1.0/24 on DeviceA.
   
   ```
   [~DeviceA] acl number 2000
   [*DeviceA-acl4-basic-2000] rule permit source 232.1.1.0 0.0.0.255
   [*DeviceA-acl4-basic-2000] quit
   [*DeviceA] pim
   [*DeviceA-pim] ssm-policy 2000
   [*DeviceA-pim] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB, DeviceC, and DeviceD are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
6. Configure IGMP SSM mapping rules on the device connected to the user host.
   
   
   
   # On DeviceD, map the multicast groups in the range of 232.1.1.0/24 to Source1 and Source3.
   
   ```
   [~DeviceD] igmp
   [*DeviceD-igmp] ssm-mapping 232.1.1.0 24 10.10.1.1
   [*DeviceD-igmp] ssm-mapping 232.1.1.0 24 10.10.3.1
   [*DeviceD-igmp] quit
   [*DeviceD] commit
   ```

#### Verifying the Configuration

# Run the **display igmp ssm-mapping group** command on DeviceD to check the mappings between multicast sources and groups.

```
<DeviceD> display igmp ssm-mapping group
IGMP SSM-Mapping conversion table of VPN Instance: public net
 Total entries: 2    (2 entries matched)

 00001: (10.10.1.1, 232.1.1.0)
 00002: (10.10.3.1, 232.1.1.0)

 Total 2 entries matched
```

The command output shows that the multicast groups in the range 232.1.1.0/24 have been mapped to Source1 and Source3.

# Run the **display igmp group ssm-mapping** command on DeviceD to check information about multicast groups created based on SSM mapping rules.

```
<DeviceD> display igmp group ssm-mapping
IGMP SSM mapping interface group report information of VPN Instance: public net
 Limited entry of this VPN Instance: - 
 100GE1/0/1 (10.10.4.2): 
  Total 1 IGMP SSM-Mapping Group reported
   Group Address   Last Reporter   Uptime      Expires
   232.1.1.1     10.10.4.1       00:01:44    00:00:26
```

The command output shows that Receiver has joined group 232.1.1.1.

# Run the **display pim routing-table** command on DeviceD to check the PIM-SM routing table.

```
<DeviceD> display pim routing-table
VPN-Instance: public net
 Total 2 (S, G) entries

 (10.10.1.1, 232.1.1.1)
     Protocol: pim-ssm, Flag: SG_RCVR                                           
     UpTime: 00:19:40                                                           
     Upstream interface: 100GE1/0/3                                              
         Upstream neighbor: 192.168.4.2                                         
         RPF prime neighbor: 192.168.4.2                                        
     Downstream interface(s) information:                                       
     Total number of downstreams: 1                                             
         1: 100GE1/0/1                                                            
             Protocol: ssm-map, UpTime: 00:19:40, Expires: -                    

 (10.10.3.1, 232.1.1.1)
     Protocol: pim-ssm, Flag: SG_RCVR                                           
     UpTime: 00:19:40                                                           
     Upstream interface: 100GE1/0/2                                              
         Upstream neighbor: 192.168.3.1                                         
         RPF prime neighbor: 192.168.3.1                                        
     Downstream interface(s) information:                                       
     Total number of downstreams: 1                                             
         1: 100GE1/0/1                                                            
             Protocol: ssm-map, UpTime: 00:19:40, Expires: -                    
```

The command output shows that multicast sources 10.10.1.1 and 10.10.3.1 send multicast data to multicast group 232.1.1.1, and DeviceD receives multicast data from the two multicast sources through 100GE1/0/3 and 100GE1/0/2.


#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  multicast routing-enable
  #
  acl number 2000
   rule permit source 232.1.1.0 0.0.0.255
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.10.1.2 255.255.255.0
   pim sm
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.1.1 255.255.255.0
   pim sm
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 192.168.4.2 255.255.255.0
   pim sm
  #
  ospf 1
   area 0.0.0.0
    network 192.168.1.0 0.0.0.255
    network 192.168.4.0 0.0.0.255
    network 10.10.1.0 0.0.0.255
  #
  pim
   ssm-policy 2000
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  multicast routing-enable
  #
  acl number 2000
   rule permit source 232.1.1.0 0.0.0.255
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.10.2.2 255.255.255.0
   pim sm
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.1.2 255.255.255.0
   pim sm
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 192.168.2.1 255.255.255.0
   pim sm
  #
  ospf 1
   area 0.0.0.0
    network 192.168.1.0 0.0.0.255
    network 192.168.2.0 0.0.0.255
    network 10.10.2.0 0.0.0.255
  #
  pim
   ssm-policy 2000
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  multicast routing-enable
  #
  acl number 2000
   rule permit source 232.1.1.0 0.0.0.255
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.10.3.2 255.255.255.0
   pim sm
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.3.1 255.255.255.0
   pim sm
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 192.168.2.2 255.255.255.0
   pim sm
  #
  ospf 1
   area 0.0.0.0
    network 192.168.2.0 0.0.0.255
    network 192.168.3.0 0.0.0.255
    network 10.10.3.0 0.0.0.255
  #
  pim
   ssm-policy 2000
  #
  return
  ```
* DeviceD
  
  ```
  #
  sysname DeviceD
  #
  multicast routing-enable
  #
  acl number 2000
   rule permit source 232.1.1.0 0.0.0.255
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.10.4.2 255.255.255.0
   pim sm
   igmp enable
   igmp version 3
   igmp ssm-mapping enable
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.3.2 255.255.255.0
   pim sm
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 192.168.4.1 255.255.255.0
   pim sm
  #
  ospf 1
   area 0.0.0.0
    network 192.168.3.0 0.0.0.255
    network 192.168.4.0 0.0.0.255
    network 10.10.4.0 0.0.0.255
  #
  igmp
   ssm-mapping 232.1.1.0 255.255.255.0 10.10.1.1
   ssm-mapping 232.1.1.0 255.255.255.0 10.10.3.1
  #
  pim
   ssm-policy 2000
  #
  return
  ```