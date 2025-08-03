Example for Configuring Mutual Access Between Local IPv6 L3VPNs
===============================================================

Example for Configuring Mutual Access Between Local IPv6 L3VPNs

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001176661213__fig_dc_vrp_gre_cfg_203101), CE1 and CE2 both connect to PE1. CE1 belongs to VPNA, and CE2 belongs to VPNB. It is required that Site 1 and Site 2 communicate with each other. To meet this requirement, configure mutual access between local VPNs.

**Figure 1** Mutual access between local IPv6 VPNs![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE 1/0/1 and 100GE 1/0/7, respectively.


  
![](figure/en-us_image_0000001176661411.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure VPN instances on PE1 and different VPN targets for the VPN instances to isolate VPNs.
2. On PE1, bind the interfaces connected to CEs to the corresponding VPN instances to provide access for VPN users.
3. Import direct routes destined for local CEs into the VPN routing tables on PE1. On each CE connected to PE1, configure a static route to the other local CE so that both CEs can communicate with each other.

#### Procedure

1. Configure VPN instances on PE1 and bind PE1 interfaces connected to CEs to the corresponding VPN instances.
   
   
   
   # Configure PE1.
   
   ```
   <HUAWEI> system-view 
   [~HUAWEI] sysname PE1 
   [*HUAWEI] commit
   [~PE1] ip vpn-instance vpna 
   [*PE1-vpn-instance-vpna] ipv6-family 
   [*PE1-vpn-instance-vpna-af-ipv6] route-distinguisher 100:1 
   [*PE1-vpn-instance-vpna-af-ipv6] vpn-target 111:1 export-extcommunity 
   [*PE1-vpn-instance-vpna-af-ipv6] vpn-target 111:1 222:2 import-extcommunity 
   [*PE1-vpn-instance-vpna-af-ipv6] quit 
   [*PE1-vpn-instance-vpna] quit 
   [*PE1] ip vpn-instance vpnb 
   [*PE1-vpn-instance-vpnb] ipv6-family 
   [*PE1-vpn-instance-vpnb-af-ipv6] route-distinguisher 100:2 
   [*PE1-vpn-instance-vpnb-af-ipv6] vpn-target 222:2 export-extcommunity 
   [*PE1-vpn-instance-vpnb-af-ipv6] vpn-target 222:2 111:1 import-extcommunity 
   [*PE1-vpn-instance-vpnb-af-ipv6] quit 
   [*PE1-vpn-instance-vpnb] quit 
   [*PE1] interface 100ge 1/0/1 
   [*PE1-100GE1/0/1] undo portswitch
   [*PE1-100GE1/0/1] ip binding vpn-instance vpna
   [*PE1-100GE1/0/1] ipv6 enable 
   [*PE1-100GE1/0/1] ipv6 address 2001:DB8::11:2 112 
   [*PE1-100GE1/0/1] quit 
   [*PE1] interface 100ge 1/0/7
   [*PE1-100GE1/0/7] undo portswitch
   [*PE1-100GE1/0/7] ip binding vpn-instance vpnb 
   [*PE1-100GE1/0/7] ipv6 enable
   [*PE1-100GE1/0/7] ipv6 address 2001:DB8::12:2 112 
   [*PE1-100GE1/0/7] quit 
   [*PE1] commit
   ```
   
   # Configure an IP address for the interface used by CE1 to connect to PE1.
   
   ```
   <HUAWEI> system-view 
   [~HUAWEI] sysname CE1 
   [*HUAWEI] commit 
   [~CE1] interface 100ge 1/0/1 
   [~CE1-100GE1/0/1] undo portswitch
   [*CE1-100GE1/0/1] ipv6 enable 
   [*CE1-100GE1/0/1] ipv6 address 2001:DB8::11:1 112 
   [*CE1-100GE1/0/1] commit 
   [~CE1-100GE1/0/1] quit
   ```
   
   # Configure an IP address for the interface used by CE2 to connect to PE1.
   
   ```
   <HUAWEI> system-view 
   [~HUAWEI] sysname CE2 
   [*HUAWEI] commit 
   [~CE2] interface 100ge 1/0/1 
   [~CE2-100GE1/0/1] undo portswitch
   [*CE2-100GE1/0/1] ipv6 enable 
   [*CE2-100GE1/0/1] ipv6 address 2001:DB8::12:1 112 
   [*CE2-100GE1/0/1] commit 
   [~CE2-100GE1/0/1] quit
   ```
   
   PE1 can ping its connected CEs. The following example uses PE1 and CE1.
   
   ```
   [~PE1] ping ipv6 vpn-instance vpna 2001:DB8::11:1
     PING 2001:DB8::11:1 : 56  data bytes, press CTRL_C to break 
       Reply from 2001:DB8::11:1                                 
       bytes=56 Sequence=1 hop limit=64 time=2 ms                
       Reply from 2001:DB8::11:1                                 
       bytes=56 Sequence=2 hop limit=64 time=2 ms                
       Reply from 2001:DB8::11:1                                 
       bytes=56 Sequence=3 hop limit=64 time=2 ms                
       Reply from 2001:DB8::11:1                                 
       bytes=56 Sequence=4 hop limit=64 time=2 ms                
       Reply from 2001:DB8::11:1                                 
       bytes=56 Sequence=5 hop limit=64 time=2 ms                
   
     --- 2001:DB8::11:1 ping statistics---                       
       5 packet(s) transmitted                                   
       5 packet(s) received                                      
       0.00% packet loss                                         
       round-trip min/avg/max=2/2/2 ms
   ```
2. Configure BGP and import the direct routes destined for local CEs to the VPN routing tables on PE1.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100 
   [*PE1-bgp] ipv6-family vpn-instance vpna 
   [*PE1-bgp-6-vpna] import-route direct 
   [*PE1-bgp-6-vpna] quit 
   [*PE1-bgp] ipv6-family vpn-instance vpnb 
   [*PE1-bgp-6-vpnb] import-route direct 
   [*PE1-bgp-6-vpnb] quit 
   [*PE1-bgp] quit 
   [*PE1] commit
   ```
3. Configure static routes on CEs.
   
   
   
   # Configure CE1.
   
   ```
   [~CE1] ipv6 route-static 2001:DB8::12:1 112 2001:DB8::11:2
   [*CE1] commit
   ```
   
   # Configure CE2.
   
   ```
   [~CE2] ipv6 route-static 2001:DB8::11:1 112 2001:DB8::12:2
   [*CE2] commit
   ```

#### Verifying the Configuration

After the configuration is complete, run the [**display ipv6 routing-table vpn-instance**](cmdqueryname=display+ipv6+routing-table+vpn-instance) command on PE1 to check route exchange between VPNs.

The following example uses the VPN instance **vpna**.

```
[~PE1] display ipv6 routing-table vpn-instance vpna
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route 
------------------------------------------------------------------------------ 
Routing Table : vpna  
         Destinations : 5        Routes : 5                                  

Destination  : 2001:DB8::11:0                          PrefixLength : 112    
NextHop      : 2001:DB8::11:2                          Preference   : 0      
Cost         : 0                                       Protocol     : Direct 
RelayNextHop : ::                                      TunnelID     : 0x0    
Interface    : 100GE1/0/1                               Flags        : D      

Destination  : 2001:DB8::11:2                          PrefixLength : 128    
NextHop      : ::1                                     Preference   : 0      
Cost         : 0                                       Protocol     : Direct 
RelayNextHop : ::                                      TunnelID     : 0x0    
Interface    : 100GE1/0/1                               Flags        : D      

Destination  : 2001:DB8::12:0                          PrefixLength : 112    
NextHop      : 2001:DB8::12:2                          Preference   : 255    
Cost         : 0                                       Protocol     : BGP    
RelayNextHop : 2001:DB8::12:2                          TunnelID     : 0x0    
Interface    : 100GE1/0/7                               Flags        : RD     

Destination  : 2001:DB8::12:2                          PrefixLength : 128    
NextHop      : ::1                                     Preference   : 255 
Cost         : 0                                       Protocol     : BGP    
RelayNextHop : ::1                                     TunnelID     : 0x0    
Interface    : 100GE1/0/7                               Flags        : RD     

Destination  : FE80::                                  PrefixLength : 10     
NextHop      : ::                                      Preference   : 0      
Cost         : 0                                       Protocol     : Direct 
RelayNextHop : ::                                      TunnelID     : 0x0    
Interface    : NULL0                                   Flags        : DB
```

CE1 and CE2 can ping each other. The following example uses the command output on CE1.

```
[~CE1] ping ipv6 2001:DB8::12:1                                
  PING 2001:DB8::12:1 : 56  data bytes, press CTRL_C to break 
    Reply from 2001:DB8::12:1                                 
    bytes=56 Sequence=1 hop limit=63 time=3 ms                
    Reply from 2001:DB8::12:1                                 
    bytes=56 Sequence=2 hop limit=63 time=2 ms                
    Reply from 2001:DB8::12:1                                 
    bytes=56 Sequence=3 hop limit=63 time=3 ms                
    Reply from 2001:DB8::12:1                                 
    bytes=56 Sequence=4 hop limit=63 time=3 ms                
    Reply from 2001:DB8::12:1                                 
    bytes=56 Sequence=5 hop limit=63 time=2 ms                

  --- 2001:DB8::12:1 ping statistics---                       
    5 packet(s) transmitted                                   
    5 packet(s) received                                      
    0.00% packet loss                                         
    round-trip min/avg/max=2/2/3 ms
```

#### Configuration Scripts

* PE1
  
  ```
  #
  sysname PE1
  #
  ip vpn-instance vpna
   ipv6-family
    route-distinguisher 100:1
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
    vpn-target 222:2 import-extcommunity
  #
  ip vpn-instance vpnb
   ipv6-family 
    route-distinguisher 100:2
    vpn-target 222:2 export-extcommunity
    vpn-target 222:2 import-extcommunity
    vpn-target 111:1 import-extcommunity
  #
  interface 100GE1/0/1
   undo portswitch
   ip binding vpn-instance vpna
   ipv6 enable 
   ipv6 address 2001:DB8::11:2/112
  # 
  interface 100GE1/0/7
   undo portswitch
   ip binding vpn-instance vpnb
   ipv6 enable 
   ipv6 address 2001:DB8::12:2/112
  #
  bgp 100
   #
   ipv6-family unicast
   # 
   ipv6-family vpn-instance vpna
    import-route direct
   #
   ipv6-family vpn-instance vpnb
    import-route direct
  #
  return
  ```
* CE1
  
  ```
  #
  sysname CE1
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable 
   ipv6 address 2001:DB8::11:1/112
  #
  ipv6 route-static 2001:DB8::12:1 112 2001:DB8::11:2
  #
  return
  ```
* CE2
  
  ```
  #
  sysname CE2
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8::12:1/112
  #
  ipv6 route-static 2001:DB8::11:1 112 2001:DB8::12:2
  #
  return
  ```