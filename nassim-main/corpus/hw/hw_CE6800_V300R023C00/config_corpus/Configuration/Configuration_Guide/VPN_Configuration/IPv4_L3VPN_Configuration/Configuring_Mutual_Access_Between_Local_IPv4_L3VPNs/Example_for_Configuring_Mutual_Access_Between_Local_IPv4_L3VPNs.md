Example for Configuring Mutual Access Between Local IPv4 L3VPNs
===============================================================

Example for Configuring Mutual Access Between Local IPv4 L3VPNs

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0000001130621702__fig_dc_vrp_gre_cfg_203101), CE1 and CE2 are connected to PE1. CE1 belongs to **vpna**, and CE2 belongs to **vpnb**. It is required that Site 1 and Site 2 communicate with each other. To meet this requirement, configure mutual access between local VPNs.

**Figure 1** Mutual access between local IPv4 VPNs![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE 1/0/1 and 100GE 1/0/7, respectively.


  
![](figure/en-us_image_0000001176741247.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure VPN instances on PE1 and different VPN targets for the instances to isolate VPNs.
2. On PE1, bind the interfaces connected to CEs to the VPN instances to provide access for VPN users.
3. Import direct routes destined for local CEs into the VPN routing tables on PE1. On each CE connected to PE1, configure a static route to the other local CE so that both CEs can communicate with each other.

#### Procedure

1. Configure VPN instances on PE1 and bind PE1 interfaces connected to CEs to the corresponding VPN instances.
   
   
   
   # Configure PE1.
   
   ```
   <HUAWEI> system-view 
   [~HUAWEI] sysname PE1 
   [*HUAWEI] commit
   [~PE1] ip vpn-instance vpna 
   [*PE1-vpn-instance-vpna] ipv4-family 
   [*PE1-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1 
   [*PE1-vpn-instance-vpna-af-ipv4] vpn-target 111:1 export-extcommunity 
   [*PE1-vpn-instance-vpna-af-ipv4] vpn-target 111:1 222:2 import-extcommunity 
   [*PE1-vpn-instance-vpna-af-ipv4] quit 
   [*PE1-vpn-instance-vpna] quit 
   [*PE1] ip vpn-instance vpnb 
   [*PE1-vpn-instance-vpnb] ipv4-family 
   [*PE1-vpn-instance-vpnb-af-ipv4] route-distinguisher 100:2 
   [*PE1-vpn-instance-vpnb-af-ipv4] vpn-target 222:2 export-extcommunity 
   [*PE1-vpn-instance-vpnb-af-ipv4] vpn-target 222:2 111:1 import-extcommunity 
   [*PE1-vpn-instance-vpnb-af-ipv4] quit 
   [*PE1-vpn-instance-vpnb] quit 
   [*PE1] interface 100ge 1/0/1 
   [*PE1-100GE1/0/1] undo portswitch
   [*PE1-100GE1/0/1] ip binding vpn-instance vpna 
   [*PE1-100GE1/0/1] ip address 10.1.1.2 24 
   [*PE1-100GE1/0/1] quit
   [*PE1] interface 100ge 1/0/7 
   [*PE1-100GE1/0/7] undo portswitch
   [*PE1-100GE1/0/7] ip binding vpn-instance vpnb 
   [*PE1-100GE1/0/7] ip address 10.2.1.2 24 
   [*PE1-100GE1/0/7] quit 
   [*PE1] commit
   ```
   
   # Configure an IP address for a related interface on CE1.
   
   ```
   <HUAWEI> system-view 
   [~HUAWEI] sysname CE1 
   [*HUAWEI] commit
   [~CE1] interface 100ge 1/0/1 
   [~CE1-100GE1/0/1] undo portswitch
   [*CE1-100GE1/0/1] ip address 10.1.1.1 24  
   [*CE1-100GE1/0/1] commit 
   [~CE1-100GE1/0/1] quit
   ```
   
   # Configure an IP address for the related interface on CE2.
   
   ```
   <HUAWEI> system-view 
   [~HUAWEI] sysname CE2 
   [*HUAWEI] commit 
   [~CE2] interface 100ge 1/0/1 
   [~CE2-100GE1/0/1] undo portswitch
   [*CE2-100GE1/0/1] ip address 10.2.1.1 24 
   [*CE2-100GE1/0/1] commit 
   [~CE2-100GE1/0/1] quit
   ```
   
   The PE can ping its connected CE. The following uses the ping between PE1 and CE1 as an example.
   
   ```
   [~PE1] ping -vpn-instance vpna 10.1.1.1
     PING 10.1.1.1: 56  data bytes, press CTRL_C to break         
       Reply from 10.1.1.1: bytes=56 Sequence=1 ttl=255 time=2 ms 
       Reply from 10.1.1.1: bytes=56 Sequence=2 ttl=255 time=2 ms 
       Reply from 10.1.1.1: bytes=56 Sequence=3 ttl=255 time=2 ms 
       Reply from 10.1.1.1: bytes=56 Sequence=4 ttl=255 time=2 ms 
       Reply from 10.1.1.1: bytes=56 Sequence=5 ttl=255 time=2 ms 
   
     --- 10.1.1.1 ping statistics ---                             
       5 packet(s) transmitted                                    
       5 packet(s) received                                       
       0.00% packet loss                                          
       round-trip min/avg/max = 2/2/2 ms
   ```
2. Configure BGP and import the local direct routes destined for CEs to the VPN routing table on PE1.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100  
   [*PE1-bgp] ipv4-family vpn-instance vpna 
   [*PE1-bgp-vpna] import-route direct 
   [*PE1-bgp-vpna] quit 
   [*PE1-bgp] ipv4-family vpn-instance vpnb 
   [*PE1-bgp-vpnb] import-route direct 
   [*PE1-bgp-vpnb] quit 
   [*PE1-bgp] quit 
   [*PE1] commit
   ```
3. Configure a static route on each CE.
   
   
   
   # Configure CE1.
   
   ```
   [~CE1] ip route-static 10.2.1.0 24 10.1.1.2
   [*CE1] commit
   ```
   
   # Configure CE2.
   
   ```
   [~CE2] ip route-static 10.1.1.0 24 10.2.1.2
   [*CE2] commit
   ```

#### Verifying the Configuration

After the configuration is complete, run the [**display ip routing-table vpn-instance**](cmdqueryname=display+ip+routing-table+vpn-instance) command on PE1. The VPNs have imported routes of each other. The following uses **vpna** as an example.

```
[~PE1] display ip routing-table vpn-instance vpna
Proto: Protocol        Pre: Preference
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route    
------------------------------------------------------------------------------   
Routing Table : vpna          
         Destinations : 7        Routes : 7                                      

Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface     

       10.1.1.0/24  Direct  0    0             D   10.1.1.2        100GE1/0/1
       10.1.1.2/32  Direct  0    0             D   127.0.0.1       100GE1/0/1 
     10.1.1.255/32  Direct  0    0             D   127.0.0.1       100GE1/0/1 
       10.2.1.0/24  BGP     255  0             RD  10.2.1.2        100GE1/0/7
       10.2.1.2/32  BGP     255  0             RD  127.0.0.1       100GE1/0/7
      127.0.0.0/8   Direct  0    0             D   127.0.0.1       InLoopBack0   
255.255.255.255/32  Direct  0    0             D   127.0.0.1       InLoopBack0
```

CE1 and CE2 can ping each other.

```
[~CE1] ping 10.2.1.1
  PING 10.2.1.1: 56  data bytes, press CTRL_C to break                           
    Reply from 10.2.1.1: bytes=56 Sequence=1 ttl=254 time=8 ms                   
    Reply from 10.2.1.1: bytes=56 Sequence=2 ttl=254 time=3 ms                   
    Reply from 10.2.1.1: bytes=56 Sequence=3 ttl=254 time=2 ms                   
    Reply from 10.2.1.1: bytes=56 Sequence=4 ttl=254 time=3 ms                   
    Reply from 10.2.1.1: bytes=56 Sequence=5 ttl=254 time=2 ms                   

  --- 10.2.1.1 ping statistics ---                                               
    5 packet(s) transmitted   
    5 packet(s) received      
    0.00% packet loss         
    round-trip min/avg/max = 2/3/8 ms 
```

#### Configuration Scripts

* PE1
  
  ```
  #
  sysname PE1
  #
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 100:1
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
    vpn-target 222:2 import-extcommunity
  #
  ip vpn-instance vpnb
   ipv4-family 
    route-distinguisher 100:2
    vpn-target 222:2 export-extcommunity
    vpn-target 222:2 import-extcommunity
    vpn-target 111:1 import-extcommunity
  #
  interface 100GE1/0/1
   undo portswitch
   ip binding vpn-instance vpna
   ip address 10.1.1.2 255.255.255.0
  # 
  interface 100GE1/0/7
   undo portswitch
   ip binding vpn-instance vpnb
   ip address 10.2.1.2 255.255.255.0
  #
  bgp 100
   #
   ipv4-family unicast
   # 
   ipv4-family vpn-instance vpna
    import-route direct
   #
   ipv4-family vpn-instance vpnb
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
   ip address 10.1.1.1 255.255.255.0
  #
  ip route-static 10.2.1.0 255.255.255.0 10.1.1.2
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
   ip address 10.2.1.1 255.255.255.0
  #
  ip route-static 10.1.1.0 255.255.255.0 10.2.1.2
  #
  return
  ```