Example for Configuring an IPv6 over IPv4 GRE Tunnel
====================================================

Example for Configuring an IPv6 over IPv4 GRE Tunnel

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001130782610__fig_dc_vrp_gre_cfg_203101), DeviceA, DeviceB, and DeviceC belong to the IPv4 backbone network and are running OSPF. An IPv6 direct link needs to be established between DeviceA and DeviceC to ensure that PC1 and PC2 can communicate with each other. To meet such a requirement, an IPv6 over IPv4 GRE tunnel needs to be established between DeviceA and DeviceC and IPv6 static routes need to be configured so that packets between PC1 and PC2 can be forwarded through tunnel interfaces on both ends of the tunnel. DeviceA and DeviceC are the default gateways of PC1 and PC2, respectively.

**Figure 1** Configuring an IPv6 over IPv4 GRE tunnel![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE 1/0/1 and 100GE 1/0/2, respectively.


  
![](figure/en-us_image_0000001130622840.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IPv4 dynamic routing protocol for communication between the devices.
2. Create tunnel interfaces on DeviceA and DeviceC and specify the tunnel source and destination addresses. The tunnel source address is the IPv4 address of the interface that sends packets, and the tunnel destination address is the IPv4 address of the interface that receives packets.
3. Configure IPv6 addresses for the tunnel interfaces to generate tunnel routes.
4. Configure an IPv6 static route between DeviceA and PC1 and between DeviceC and PC2 and specify the local tunnel interface as the outbound interface of the static route so that IPv6 traffic between PC1 and PC2 can be transmitted through the GRE tunnel.

#### Procedure

1. Configure IPv4 or IPv6 addresses for interfaces.
   
   
   
   Configure an IP address for each interface according to [Figure 1](#EN-US_TASK_0000001130782610__fig_dc_vrp_gre_cfg_203101). For detailed configurations, see [Configuration Scripts](#EN-US_TASK_0000001130782610__postreq24192593172748).
2. Configure an IGP on the IPv4 backbone network.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] ospf 1
   [*DeviceA-ospf-1] area 0
   [*DeviceA-ospf-1-area-0.0.0.0] network 172.20.1.0 0.0.0.255
   [*DeviceA-ospf-1-area-0.0.0.0] quit
   [*DeviceA-ospf-1] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] ospf 1
   [*DeviceB-ospf-1] area 0
   [*DeviceB-ospf-1-area-0.0.0.0] network 172.20.1.0 0.0.0.255
   [*DeviceB-ospf-1-area-0.0.0.0] network 172.21.1.0 0.0.0.255
   [*DeviceB-ospf-1-area-0.0.0.0] quit
   [*DeviceB-ospf-1] quit
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] ospf 1
   [*DeviceC-ospf-1] area 0
   [*DeviceC-ospf-1-area-0.0.0.0] network 172.21.1.0 0.0.0.255
   [*DeviceC-ospf-1-area-0.0.0.0] quit
   [*DeviceC-ospf-1] quit
   [*DeviceC] commit
   ```
   
   After the configuration is complete, run the **display ip routing-table** command on DeviceA and DeviceC. The command outputs show that DeviceA and DeviceC can learn the OSPF route to the network segment of the remote interface.
   
   # The following example uses the command output on DeviceA.
   
   ```
   [~DeviceA] display ip routing-table
   Proto: Protocol        Pre: Preference
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : _public_
            Destinations : 8        Routes : 8
   
   Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface
   
        172.20.1.0/24  Direct  0    0             D  172.20.1.1      100GE1/0/1
        172.20.1.1/32  Direct  0    0             D  127.0.0.1       100GE1/0/1
      172.20.1.255/32  Direct  0    0             D  127.0.0.1       100GE1/0/1
        172.21.1.0/24  OSPF    10   2             D  172.20.1.2      100GE1/0/1
         127.0.0.0/8   Direct  0    0             D  127.0.0.1       InLoopBack0
         127.0.0.1/32  Direct  0    0             D  127.0.0.1       InLoopBack0
   127.255.255.255/32  Direct  0    0             D  127.0.0.1       InLoopBack0
   255.255.255.255/32  Direct  0    0             D  127.0.0.1       InLoopBack0
   ```
3. Configure tunnel interfaces.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface tunnel 1
   [*DeviceA-Tunnel1] tunnel-protocol gre
   [*DeviceA-Tunnel1] ipv6 enable
   [*DeviceA-Tunnel1] ipv6 address 2001:DB8:3::1 64
   [*DeviceA-Tunnel1] source 172.20.1.1
   [*DeviceA-Tunnel1] destination 172.21.1.2
   [*DeviceA-Tunnel1] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] interface tunnel 1
   [*DeviceC-Tunnel1] tunnel-protocol gre
   [*DeviceC-Tunnel1] ipv6 enable
   [*DeviceC-Tunnel1] ipv6 address 2001:DB8:3::2 64
   [*DeviceC-Tunnel1] source 172.21.1.2
   [*DeviceC-Tunnel1] destination 172.20.1.1
   [*DeviceC-Tunnel1] quit
   [*DeviceC] commit
   ```
   
   After the configuration is complete, the IPv6 status of tunnel interfaces becomes Up and the tunnel interfaces can ping each other successfully.
   
   # The following example uses the command output on DeviceA.
   
   ```
   
   [~DeviceA] ping ipv6 -a 2001:DB8:3::1 2001:DB8:3::2
     PING 2001:DB8:3::2 : 56  data bytes, press CTRL_C to break                             
       Reply from 2001:DB8:3::2                                                             
       bytes=56 Sequence=1 hop limit=64 time=11 ms                                 
       Reply from 2001:DB8:3::2                                                             
       bytes=56 Sequence=2 hop limit=64 time=5 ms                                  
       Reply from 2001:DB8:3::2                                                             
       bytes=56 Sequence=3 hop limit=64 time=5 ms                                  
       Reply from 2001:DB8:3::2                                                             
       bytes=56 Sequence=4 hop limit=64 time=5 ms                                  
       Reply from 2001:DB8:3::2                                                             
       bytes=56 Sequence=5 hop limit=64 time=5 ms                                  
   
     --- 2001:DB8:3::2 ping statistics---                                                   
       5 packet(s) transmitted                                                     
       5 packet(s) received                                                        
       0.00% packet loss                                                           
       round-trip min/avg/max=5/6/11 ms                                            
   
   ```
4. Configure static routes.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] ipv6 route-static 2001:DB8:2:: 64 tunnel1
   [*DeviceA] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] ipv6 route-static 2001:DB8:1:: 64 tunnel1
   [*DeviceC] commit
   ```

#### Verifying the Configuration

After the configuration is complete, run the **display** **ipv6 routing-table** command on DeviceA and DeviceC. The command outputs show the IPv6 static route with the local tunnel interface as the outbound interface and destined for the network segment of the remote end.

# The following example uses the command output on DeviceA.

```
[~DeviceA] display ipv6 routing-table 
Route Flags: R - relay, D - download to fib, B - black hole route               
------------------------------------------------------------------------------  
Routing Table : _public_                                                        
         Destinations : 8        Routes : 8                                     

Destination  : ::1                                     PrefixLength : 128       
NextHop      : ::1                                     Preference   : 0         
Cost         : 0                                       Protocol     : Direct    
RelayNextHop : ::                                      TunnelID     : 0x0       
Interface    : InLoopBack0                             Flags        : D         

Destination  : ::FFFF:127.0.0.0                        PrefixLength : 104       
NextHop      : ::FFFF:127.0.0.1                        Preference   : 0         
Cost         : 0                                       Protocol     : Direct    
RelayNextHop : ::                                      TunnelID     : 0x0       
Interface    : InLoopBack0                             Flags        : D         

Destination  : ::FFFF:127.0.0.1                        PrefixLength : 128       
NextHop      : ::1                                     Preference   : 0         
Cost         : 0                                       Protocol     : Direct    
RelayNextHop : ::                                      TunnelID     : 0x0       
Interface    : InLoopBack0                             Flags        : D         

Destination  : 2001:DB8:3::                            PrefixLength : 64        
NextHop      : 2001:DB8:3::1                           Preference   : 0         
Cost         : 0                                       Protocol     : Direct    
RelayNextHop : ::                                      TunnelID     : 0x0       
Interface    : Tunnel1                                 Flags        : D         

Destination  : 2001:DB8:3::1                           PrefixLength : 128       
NextHop      : ::1                                     Preference   : 0         
Cost         : 0                                       Protocol     : Direct    
RelayNextHop : ::                                      TunnelID     : 0x0       
Interface    : Tunnel1                                 Flags        : D         

Destination  : 2001:DB8:1::                            PrefixLength : 64       
NextHop      : ::1                                     Preference   : 0         
Cost         : 0                                       Protocol     : Direct    
RelayNextHop : ::                                      TunnelID     : 0x0       
Interface    : 100GE1/0/2                               Flags        : D
         
Destination  : 2001:DB8:1::2                           PrefixLength : 128       
NextHop      : ::1                                     Preference   : 0         
Cost         : 0                                       Protocol     : Direct    
RelayNextHop : ::                                      TunnelID     : 0x0       
Interface    : 100GE1/0/2                               Flags        : D

Destination  : 2001:DB8:2::                            PrefixLength : 64       
NextHop      : ::1                                    Preference   : 60        
Cost         : 0                                       Protocol     : Static    
RelayNextHop : ::                                      TunnelID     : 0x0       
Interface    : Tunnel1                             Flags        : D      
```

#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 172.20.1.1 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:1::2/64
  #
  interface Tunnel1
   ipv6 enable
   ipv6 address 2001:DB8:3::1/64
   tunnel-protocol gre
   source 172.20.1.1
   destination 172.21.1.2
  #
  ospf 1
   area 0.0.0.0
    network 172.20.1.0 0.0.0.255
  #
  ipv6 route-static 2001:DB8:2:: 64 Tunnel1
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 172.20.1.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 172.21.1.1 255.255.255.0
  #
  ospf 1
   area 0.0.0.0
    network 172.20.1.0 0.0.0.255
    network 172.21.1.0 0.0.0.255
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 172.21.1.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:2::2/64
  #
  interface Tunnel1
   ipv6 enable
   ipv6 address 2001:DB8:3::2/64
   tunnel-protocol gre
   source 172.21.1.2
   destination 172.20.1.1
  #
  ospf 1
   area 0.0.0.0
   network 172.21.1.0 0.0.0.255
  #
  ipv6 route-static 2001:DB8:1:: 64 Tunnel1
  #
  return
  ```