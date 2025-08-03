Example for Configuring a Device as an IPv6 DNS Client for DNS Query (Dynamic Domain Name Resolution)
=====================================================================================================

Example for Configuring a Device as an IPv6 DNS Client for DNS Query (Dynamic Domain Name Resolution)

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001563750889__fig_dc_s_cfg_10332801), DeviceA functions as an IPv6 DNS client and works with the IPv6 DNS server. Assume that DeviceA is routable to the IPv6 DNS server and network server. The IPv6 DNS server records the mapping between the domain name (huawei.com) and the IPv6 address (2001:db8:2::1/64). The customer wants DeviceA to access the network server with the IPv6 address 2001:db8:2::1/64 through the domain name huawei.com.

In addition, the customer expects the IPv6 DNS server to correctly parse the domain name huawei.com even if only parts of the domain name (such as "huawei") are entered. This allows proper access to the network server.

**Figure 1** Network diagram of IPv6 dynamic domain name resolution![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE 1/0/1 and 100GE 1/0/2, respectively.


  
![](figure/en-us_image_0000001563990805.png "Click to enlarge")

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure dynamic DNS on DeviceA so that DeviceA can communicate with the network server by querying dynamic DNS entries.
2. Configure domain name suffixes on DeviceA to support a domain name suffix list.

#### Procedure

1. Configure IPv6 addresses for the interfaces on DeviceA.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] [commit](cmdqueryname=commit)
   [~DeviceA] vlan batch 10 20
   [*DeviceA] interface 100ge1/0/1
   [*DeviceA-100GE1/0/1] portswitch
   [*DeviceA-100GE1/0/1] port link-type trunk
   [*DeviceA-100GE1/0/1] port trunk allow-pass vlan 10
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge1/0/2
   [*DeviceA-100GE1/0/2] portswitch
   [*DeviceA-100GE1/0/2] port link-type trunk
   [*DeviceA-100GE1/0/2] port trunk allow-pass vlan 20
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface vlanif 10
   [*DeviceA-Vlanif10] ipv6 enable
   [*DeviceA-Vlanif10] ipv6 address 2001:db8:2::2/64
   [*DeviceA-Vlanif10] quit
   [*DeviceA] interface vlanif 20
   [*DeviceA-Vlanif20] ipv6 enable
   [*DeviceA-Vlanif20] ipv6 address 2001:db8:3::1/64
   [*DeviceA-Vlanif20] quit
   ```
2. Configure dynamic DNS.
   
   
   
   # Enable dynamic domain name resolution.
   
   ```
   [~DeviceA] dns resolve
   [*DeviceA] commit
   ```
   
   # Configure the IPv6 address of the DNS server.
   
   ```
   [~DeviceA] dns server ipv6 2001:db8:3::2
   [*DeviceA] commit
   ```
3. Configure domain name suffixes.
   
   
   ```
   [~DeviceA] dns domain net
   [*DeviceA] dns domain com
   [*DeviceA] commit
   [~DeviceA] quit
   ```

#### Verifying the Configuration

# Run the **ping ipv6 huawei.com** command on DeviceA. If successful, the resolved destination IPv6 address is shown. In this example, the address is 2001:db8:2::1.

```
<DeviceA> ping ipv6 huawei.com
  Resolved Host ( huawei.com -> 2001:DB8:2::1)
  PING huawei.com : 56  data bytes, press CTRL_C to break
    Reply from 2001:DB8:2::1                                                         
    bytes=56 Sequence=1 hop limit=64  time = 1 ms                               
    Reply from 2001:DB8:2::1                                                         
    bytes=56 Sequence=2 hop limit=64  time = 1 ms                               
    Reply from 2001:DB8:2::1                                                         
    bytes=56 Sequence=3 hop limit=64  time = 1 ms                               
    Reply from 2001:DB8:2::1                                                         
    bytes=56 Sequence=4 hop limit=64  time = 1 ms                               
    Reply from 2001:DB8:2::1                                                         
    bytes=56 Sequence=5 hop limit=64  time = 1 ms                               
  --- huawei.com ping statistics ---                                               
    5 packet(s) transmitted                                                     
    5 packet(s) received                                                        
    0.00% packet loss                                                           
    round-trip min/avg/max = 1/1/1 ms      
```

# Run the **ping ipv6 huawei** command on DeviceA. If successful, the domain name is changed to **huawei.com** and the resolved destination IPv6 address is shown. In this example, the address is 2001:db8:2::1.

```
<DeviceA> ping ipv6 huawei
  Resolved Host ( huawei.com -> 2001:DB8:2::1)
  PING huawei.com : 56  data bytes, press CTRL_C to break
    Reply from 2001:DB8:2::1                                                         
    bytes=56 Sequence=1 hop limit=64  time = 1 ms                               
    Reply from 2001:DB8:2::1                                                         
    bytes=56 Sequence=2 hop limit=64  time = 1 ms                               
    Reply from 2001:DB8:2::1                                                         
    bytes=56 Sequence=3 hop limit=64  time = 1 ms                               
    Reply from 2001:DB8:2::1                                                         
    bytes=56 Sequence=4 hop limit=64  time = 1 ms                               
    Reply from 2001:DB8:2::1                                                         
    bytes=56 Sequence=5 hop limit=64  time = 1 ms                               
  --- huawei.com ping statistics ---                                               
    5 packet(s) transmitted                                                     
    5 packet(s) received                                                        
    0.00% packet loss                                                           
    round-trip min/avg/max = 1/1/1 ms  
```

# Run the **display dns ipv6 dynamic-host** command on DeviceA to check dynamic IPv6 DNS entries in the cache.

```
<DeviceA> display dns ipv6 dynamic-host
Host                                     TTL        Type   Address
huawei.com                               3579       IPv6   2001:DB8:2::1 

Total  :  1
```

#### Configuration Scripts

```
#
 sysname DeviceA
#
dns resolve
dns server ipv6 2001:DB8:3::2
dns domain net
dns domain com
#
 vlan batch 10 20
#
interface Vlanif10
 ipv6 enable
 ipv6 address 2001:DB8:2::2/64
#
interface Vlanif20
 ipv6 enable
 ipv6 address 2001:DB8:3::1/64
#
interface 100GE1/0/1
 port link-type trunk
 port trunk allow-pass vlan 10
#
interface 100GE1/0/2
 port link-type trunk
 port trunk allow-pass vlan 20
#
return
```