Example for Configuring IS-IS to Import BGP Routes
==================================================

Example for Configuring IS-IS to Import BGP Routes

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001176663857__fig_dc_vrp_isis_cfg_008401), DeviceA and DeviceB are IS-IS neighbors in the same AS. BGP is disabled on DeviceA, while DeviceB and DeviceC are EBGP peers. It is required that DeviceB be configured to import BGP routes to IS-IS and the costs of the imported routes be changed using a route-policy.

**Figure 1** Network diagram for configuring IS-IS to import BGP routes![](public_sys-resources/note_3.0-en-us.png) 

Interface 1 and interface 2 in this example represent 100GE 1/0/1 and 100GE 1/0/2, respectively.


  
![](figure/en-us_image_0000001130624360.png)

#### Configuration Precautions

To improve security, you are advised to configure IS-IS authentication. For details, see Configuring IS-IS Authentication. IS-IS interface authentication is used as an example. For details, see Example for Configuring Basic IS-IS Functions.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IPv4 addresses for interfaces on each routing device.
2. Enable IS-IS and specify a NET on DeviceA and DeviceB.
3. Establish an EBGP connection between DeviceB and DeviceC.
4. Configure IS-IS and BGP to import routes from each other on DeviceB, and then check the routing table on DeviceA.

#### Procedure

1. Configure IPv4 addresses for interfaces on each routing device.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ip address 10.1.1.1 255.255.255.0
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB, DeviceC, and DeviceD are similar to the configuration of DeviceA. For detailed configurations, see [Configuration Scripts](#EN-US_TASK_0000001176663857__postreq24192593172748).
2. Enable IS-IS and specify a NET on DeviceA and DeviceB.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] isis 1
   [*DeviceA-isis-1] network-entity 10.0000.0000.0001.00
   [*DeviceA-isis-1] quit
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] isis enable 1
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
   
   The configuration of DeviceB is similar to the configuration of DeviceA. For detailed configurations, see [Configuration Scripts](#EN-US_TASK_0000001176663857__postreq24192593172748).
3. Establish an EBGP connection between DeviceB and DeviceC.
   
   
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] bgp 65008
   [*DeviceB-bgp] router-id 1.1.1.1
   [*DeviceB-bgp] peer 10.2.1.2 as-number 65009
   [*DeviceB-bgp] ipv4-family unicast
   [*DeviceB-bgp-af-ipv4] network 10.2.1.0 255.255.255.0
   [*DeviceB-bgp-af-ipv4] quit
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] bgp 65009
   [*DeviceC-bgp] router-id 2.2.2.2
   [*DeviceC-bgp] peer 10.2.1.1 as-number 65008
   [*DeviceC-bgp] ipv4-family unicast
   [*DeviceC-bgp-af-ipv4] network 10.2.1.0 255.255.255.0
   [*DeviceC-bgp-af-ipv4] quit
   [*DeviceC] commit
   ```
4. Configure IS-IS to import BGP routes.
   
   
   
   # Configure a static route on DeviceC.
   
   ```
   [~DeviceC] ip route-static 172.16.1.1 32 NULL 0
   [*DeviceC] commit
   ```
   
   # On DeviceC, configure BGP to import static routes.
   
   ```
   [~DeviceC] bgp 65009
   [*DeviceC-bgp] import-route static
   [*DeviceC-bgp] quit
   [*DeviceC] commit
   ```
   
   # On DeviceB, configure IS-IS to import BGP routes.
   
   ```
   [~DeviceB] isis 1
   [*DeviceB-isis-1] import-route bgp
   [*DeviceB-isis-1] quit
   [*DeviceB] commit
   ```
   
   # Check the routing table of DeviceA. The command output shows that IS-IS successfully imports the BGP route 172.16.1.1/32.
   
   ```
   [~DeviceA] display ip routing-table
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table: _public_
            Destinations : 6        Routes : 6
   
   Destination/Mask    Proto  Pre  Cost     Flags NextHop         Interface
   
          10.1.1.0/24  Direct 0    0           D  10.1.1.1        100GE1/0/1
          10.1.1.1/32  Direct 0    0           D  127.0.0.1       100GE1/0/1
          10.1.1.255/32  Direct 0    0           D  10.1.1.2        100GE1/0/1
          127.0.0.0/8  Direct 0    0           D  127.0.0.1       InLoopBack0
         127.0.0.1/32  Direct 0    0           D  127.0.0.1       InLoopBack0
         172.16.1.1/32  ISIS  15   74       D  10.1.1.2        100GE1/0/1
         127.255.255.255/32  Direct 0  0       D  127.0.0.1       InLoopBack0
         255.255.255.255/32  Direct 0  0       D  127.0.0.1       InLoopBack0
   ```
   
   # On DeviceB, configure an AS\_Path filter, and apply the filter in a route-policy named **RTC**.
   
   ```
   [~DeviceB] ip as-path-filter 1 permit 65009
   [*DeviceB] route-policy RTC permit node 0
   [*DeviceB-route-policy] if-match as-path-filter 1
   [*DeviceB-route-policy] apply cost + 20
   [*DeviceB-route-policy] quit
   [*DeviceB] commit
   ```
   
   # On DeviceB, configure IS-IS to import BGP routes.
   
   ```
   [~DeviceB] isis 1
   [*DeviceB-isis-1] import-route bgp route-policy RTC
   [*DeviceB-isis-1] quit
   [*DeviceB] commit
   ```
   
   # Check the routing table of DeviceA. The command output shows that the cost of the imported BGP route 172.16.1.1/32 changes from 74 to 94.
   
   ```
   [~DeviceA] display ip routing-table
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table: _public_
            Destinations : 6        Routes : 6
   
   Destination/Mask    Proto  Pre  Cost     Flags NextHop         Interface
   
          10.1.1.0/24  Direct 0    0           D  10.1.1.1        100GE1/0/1
          10.1.1.1/32  Direct 0    0           D  127.0.0.1       100GE1/0/1
          10.1.1.2/32  Direct 0    0           D  10.1.1.2        100GE1/0/1
          127.0.0.0/8  Direct 0    0           D  127.0.0.1       InLoopBack0
         127.0.0.1/32  Direct 0    0           D  127.0.0.1       InLoopBack0
      172.16.1.1/32  ISIS  15   94          D  10.1.1.2        100GE1/0/1
         127.255.255.255/32  Direct 0  0       D  127.0.0.1       InLoopBack0
         255.255.255.255/32  Direct 0  0       D  127.0.0.1       InLoopBack0
   ```
5. Configure BGP to import IS-IS routes.
   
   
   ```
   [~DeviceB] bgp 65008
   [*DeviceB-bgp] import-route isis 1
   [*DeviceB-bgp] quit
   [*DeviceB] commit
   ```

#### Verifying the Configuration

# Check the routing table of DeviceC.

```
[~DeviceC] display ip routing-table
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table: _public_
         Destinations : 7        Routes : 7

Destination/Mask    Proto  Pre  Cost     Flags NextHop         Interface

      10.1.1.0/24  EBGP 255  0           D  10.2.1.1       100GE1/0/1
       10.2.1.0/24  Direct 0    0           D  10.2.1.2        100GE1/0/1
       10.2.1.1/32  Direct 0    0           D  10.2.1.1        100GE1/0/1
     10.2.1.255/32  Direct 0    0           D  127.0.0.1       100GE1/0/1
       127.0.0.0/8  Direct 0    0           D  127.0.0.1       InLoopBack0
      127.0.0.1/32  Direct 0    0           D  127.0.0.1       InLoopBack0
     172.16.1.1/32  Static 60   0           D  0.0.0.0         NULL0
    192.168.0.2/32  Direct 0    0           D  127.0.0.1       LoopBack0
127.255.255.255/32  Direct 0    0           D  127.0.0.1       InLoopBack0
    192.168.0.1/32  EBGP 255    0          RD   10.2.1.1       100GE1/0/1
255.255.255.255/32  Direct 0    0           D  127.0.0.1       InLoopBack0
```

BGP successfully imports the IS-IS route 10.1.1.0/24.


#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  isis 1
   network-entity 10.0000.0000.0001.00
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.1 255.255.255.0
   isis enable 1
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  isis 1
   import-route bgp route-policy RTC
   network-entity 10.0000.0000.0002.00
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.2 255.255.255.0
   isis enable 1
  #
  interface  100GE1/0/2
   undo portswitch
   ip address 10.2.1.1 255.255.255.0
  #
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.255
  #
  bgp 65008
   router-id 1.1.1.1
   peer 10.2.1.2 as-number 65009
   #
   ipv4-family unicast
    network 10.2.1.0 255.255.255.0
    import-route static
    import-route isis 1
    peer 10.2.1.2 enable
  #
  ip as-path-filter 1 index 10 permit 65009
  #
  route-policy RTC permit node 0
   if-match as-path-filter 1
   apply cost 20
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
   ip address 10.2.1.2 255.255.255.0
  #
  interface LoopBack0
   ip address 2.2.2.2 255.255.255.255
  #
  bgp 65009
   router-id 2.2.2.2
   peer 10.2.1.1 as-number 65008
   #
   ipv4-family unicast
    network 10.2.1.0 255.255.255.0
    import-route static
    peer 10.2.1.1 enable
  #
  ip route-static 172.16.1.1 255.255.255.255 NULL0
  #
  return
  ```