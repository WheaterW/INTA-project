Example for Configuring a Device as an IPv4 DNS Client for DNS Query (Dynamic Domain Name Resolution)
=====================================================================================================

Example for Configuring a Device as an IPv4 DNS Client for DNS Query (Dynamic Domain Name Resolution)

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001512830986__fig_dc_s_cfg_10332801), DeviceA functions as an IPv4 DNS client and works with the IPv4 DNS server. Assume that DeviceA is routable to the IPv4 DNS server and network server. The IPv4 DNS server records the mapping between the domain name (huawei.com) and the IPv4 address (192.168.10.1/24). The customer wants DeviceA to access the network server with the IPv4 address 192.168.10.1/24 through the domain name huawei.com.

The IPv4 DNS server needs to correctly parse a domain name if a user enters only parts of the domain name. The user then can properly access the network server. For example, the user only needs to enter "huawei" to access the host huawei.com using an IPv4 DNS client.

**Figure 1** Network diagram of IPv4 dynamic domain name resolution![](public_sys-resources/note_3.0-en-us.png) 

In this example, Interface1 and Interface2 represent 100GE 1/0/1 and 100GE 1/0/2, respectively.

![](figure/en-us_image_0000001512671414.png "Click to enlarge")



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure dynamic DNS on DeviceA so that DeviceA can communicate with the network server by querying dynamic DNS entries.
2. Configure domain name suffixes on DeviceA to support a domain name suffix list.

#### Procedure

1. Configure IPv4 addresses for 100GE 1/0/1 and 100GE 1/0/2 on DeviceA.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] [commit](cmdqueryname=commit)
   [~DeviceA] vlan batch 10 20
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] port link-type trunk
   [*DeviceA-100GE1/0/1] port trunk allow-pass vlan 10
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] port link-type trunk
   [*DeviceA-100GE1/0/2] port trunk allow-pass vlan 20
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface vlanif 10
   [*DeviceA-Vlanif10] ip address 192.168.10.2 24
   [*DeviceA-Vlanif10] quit
   [*DeviceA] interface vlanif 20
   [*DeviceA-Vlanif20] ip address 192.168.20.1 24
   [*DeviceA-Vlanif20] quit
   ```
2. Configure dynamic DNS.
   
   
   
   # Enable dynamic domain name resolution.
   
   ```
   [*DeviceA] dns resolve
   [*DeviceA] commit
   ```
   
   # Configure the IPv4 address of the DNS server.
   
   ```
   [~DeviceA] dns server 192.168.20.2
   [*DeviceA] commit
   ```
3. Configure a domain name suffix.
   
   
   ```
   [~DeviceA] dns domain com
   [*DeviceA] commit
   [~DeviceA] quit
   ```

#### Verifying the Configuration

# Run the **ping huawei.com** command on DeviceA. If successful, the resolved destination IPv4 address is shown. In this example, the address is 192.168.10.1.

```
<DeviceA> ping huawei.com
  Resolved Host ( huawei.com -> 192.168.10.1)
  PING huawei.com : 56  data bytes, press CTRL_C to break
    Reply from 192.168.10.1                                                         
    bytes=56 Sequence=1 ttl=254  time = 1 ms                               
    Reply from 192.168.10.1                                                         
    bytes=56 Sequence=2 ttl=254  time = 1 ms                               
    Reply from 192.168.10.1                                                         
    bytes=56 Sequence=3 ttl=254  time = 1 ms                               
    Reply from 192.168.10.1                                                         
    bytes=56 Sequence=4 ttl=254  time = 1 ms                               
    Reply from 192.168.10.1                                                         
    bytes=56 Sequence=5 ttl=254  time = 1 ms                               
  --- huawei.com ping statistics ---                                               
    5 packet(s) transmitted                                                     
    5 packet(s) received                                                        
    0.00% packet loss                                                           
    round-trip min/avg/max = 4/4/6 ms      
```

# Run the **ping huawei** command on DeviceA. If successful, the domain name is changed to **huawei.com** and the resolved destination IPv4 address is shown. In this example, the address is 192.168.10.1.

```
<DeviceA> ping huawei
  Resolved Host ( huawei.com -> 192.168.10.1)
  PING huawei.com : 56  data bytes, press CTRL_C to break
    Reply from 192.168.10.1                                                         
    bytes=56 Sequence=1 ttl=254  time = 1 ms                               
    Reply from 192.168.10.1                                                         
    bytes=56 Sequence=2 ttl=254  time = 1 ms                               
    Reply from 192.168.10.1                                                         
    bytes=56 Sequence=3 ttl=254  time = 1 ms                               
    Reply from 192.168.10.1                                                        
    bytes=56 Sequence=4 ttl=254  time = 1 ms                               
    Reply from 192.168.10.1                                                         
    bytes=56 Sequence=5 ttl=254  time = 1 ms                               
  --- huawei.com ping statistics ---                                               
    5 packet(s) transmitted                                                     
    5 packet(s) received                                                        
    0.00% packet loss                                                           
    round-trip min/avg/max = 4/4/6 ms  
```

# Run the **display dns dynamic-host** **ip** command on DeviceA to check dynamic IPv4 DNS entries in the cache.

```
<DeviceA> display dns dynamic-host ip
Host                                     TTL        Type   Address
huawei.com                               114        IPv4   192.168.10.1
Total  :  1
```

#### Configuration Scripts

```
#
 sysname DeviceA
#
dns resolve
dns server 192.168.20.2
dns domain net
dns domain com
#
 vlan batch 10 20
#
interface Vlanif10
 ip address 192.168.10.2 24
#
interface Vlanif20
 ip address 192.168.20.1 24
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