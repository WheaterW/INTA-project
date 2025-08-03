Example for Configuring a Device as an IPv6 DNS Client for DNS Query (Static Domain Name Resolution)
====================================================================================================

Example for Configuring a Device as an IPv6 DNS Client for DNS Query (Static Domain Name Resolution)

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001564110593__fig_dc_s_cfg_10332801), DeviceA functions as an IPv6 DNS client. The customer wants DeviceA to communicate with DeviceB using the domain name (DeviceB).

**Figure 1** Network diagram of IPv6 static domain name resolution![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 represents 100GE 1/0/1.


  
![](figure/en-us_image_0000001563750901.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a static IPv6 DNS entry on DeviceA and enable DeviceA to communicate with DeviceB using a domain name.

#### Procedure

1. Configure an IPv6 address for the interface on DeviceA.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [~DeviceA] vlan batch 10
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] portswitch
   [*DeviceA-100GE1/0/1] port link-type trunk
   [*DeviceA-100GE1/0/1] port trunk allow-pass vlan 10
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface vlanif 10
   [*DeviceA-Vlanif10] ipv6 enable
   [*DeviceA-Vlanif10] ipv6 address 2001:db8:1::1/64
   [*DeviceA-Vlanif10] quit
   ```
2. Configure a static IPv6 DNS entry on DeviceA.
   
   
   ```
   [~DeviceA] ipv6 host DeviceB 2001:db8:1::2
   [*DeviceA] commit
   [~DeviceA] quit
   ```

#### Verifying the Configuration

# Run the **ping ipv6 DeviceB** command on DeviceA. If successful, the resolved destination IPv6 address is shown. In this example, the address is 2001:db8:1::2.

```
<DeviceA> ping ipv6 DeviceB
  Resolved Host ( DeviceB -> 2001:DB8:1::2)
  PING DeviceB : 56  data bytes, press CTRL_C to break
    Reply from 2001:DB8:1::2                                                         
    bytes=56 Sequence=1 hop limit=64  time = 1 ms                               
    Reply from 2001:DB8:1::2                                                         
    bytes=56 Sequence=2 hop limit=64  time = 1 ms                               
    Reply from 2001:DB8:1::2                                                         
    bytes=56 Sequence=3 hop limit=64  time = 1 ms                               
    Reply from 2001:DB8:1::2                                                         
    bytes=56 Sequence=4 hop limit=64  time = 1 ms                               
    Reply from 2001:DB8:1::2                                                         
    bytes=56 Sequence=5 hop limit=64  time = 1 ms                               
  --- DeviceB ping statistics ---                                               
    5 packet(s) transmitted                                                     
    5 packet(s) received                                                        
    0.00% packet loss                                                           
    round-trip min/avg/max = 1/1/1 ms      
```

# Run the **display ipv6 host** command on DeviceA to check the mapping between the hostname and IPv6 address in the static IPv6 DNS entry.

```
<DeviceA> display ipv6 host
Host                 Age        Flag    IPv6 Address 
DeviceB               0        static   2001:DB8:1::2
Total    :  1 
```

#### Configuration Scripts

```
#
 sysname DeviceA
#
ipv6 host DeviceB 2001:DB8:1::2
#
vlan batch 10
#
interface Vlanif10
 ipv6 enable
 ipv6 address 2001:DB8:1::1/64 
#
interface 100GE1/0/1
 port link-type trunk
 port trunk allow-pass vlan 10
#
return
```