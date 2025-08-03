Example for Configuring a Device as an IPv4 DNS Client for DNS Query (Static Domain Name Resolution)
====================================================================================================

Example for Configuring a Device as an IPv4 DNS Client for DNS Query (Static Domain Name Resolution)

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001512671386__fig_dc_s_cfg_10332801), DeviceA functions as an IPv4 DNS client. The customer wants DeviceA to communicate with DeviceB using the domain name (DeviceB).

**Figure 1** Network diagram of IPv4 static domain name resolution![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 represents 100GE 1/0/1.

![](figure/en-us_image_0000001512671406.png "Click to enlarge")



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a static IPv4 DNS entry on DeviceA and enable DeviceA to communicate with DeviceB using a domain name.

#### Procedure

1. Configure an IPv4 address for 100GE 1/0/1 on DeviceA.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] [commit](cmdqueryname=commit)
   [~DeviceA] vlan batch 10
   [*DeviceA] interface 100GE 1/0/1
   [*DeviceA-100GE1/0/1] port link-type trunk
   [*DeviceA-100GE1/0/1] port trunk allow-pass vlan 10
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface vlanif 10
   [*DeviceA-Vlanif10] ip address 192.168.1.1 24
   [*DeviceA-Vlanif10] quit
   ```
2. Configure a static IPv4 DNS entry on DeviceA.
   
   
   ```
   [*DeviceA] ip host DeviceB 192.168.1.2
   [*DeviceA] commit
   [~DeviceA] quit
   ```

#### Verifying the Configuration

# Run the **ping DeviceB** command on DeviceA. If successful, the resolved destination IPv4 address is shown. In this example, the address is 192.168.1.2.

```
<DeviceA> ping DeviceB
  Resolved Host ( DeviceB -> 192.168.1.2)
  PING DeviceB : 56  data bytes, press CTRL_C to break
    Reply from 192.168.1.2                                                         
    bytes=56 Sequence=1 hop ttl=254  time = 1 ms                               
    Reply from 192.168.1.2                                                         
    bytes=56 Sequence=2 hop ttl=254  time = 1 ms                               
    Reply from 192.168.1.2                                                         
    bytes=56 Sequence=3 hop ttl=254  time = 1 ms                               
    Reply from 192.168.1.2                                                         
    bytes=56 Sequence=4 hop ttl=254  time = 1 ms                               
    Reply from 192.168.1.2                                                         
    bytes=56 Sequence=5 hop ttl=254  time = 1 ms                               
  --- DeviceB ping statistics ---                                               
    5 packet(s) transmitted                                                     
    5 packet(s) received                                                        
    0.00% packet loss                                                           
    round-trip min/avg/max = 1/1/1 ms     
```

# Run the **display ip host** command on DeviceA to check the mapping between the hostname and IPv4 address in the static DNS entry.

```
<DeviceA> display ip host
Host                 Age        Flag    IPv4 Address 
DeviceB               0        static   192.168.1.2
Total    :  1 
```

#### Configuration Scripts

```
#
 sysname DeviceA
#
ip host DeviceB 192.168.1.2
#
vlan batch 10
#
interface Vlanif10
 ip address 192.168.1.1 24
#
interface 100GE1/0/1
 port link-type trunk
 port trunk allow-pass vlan 10
#
return
```