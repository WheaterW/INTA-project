Example for Using XPL to Filter the Routes to Be Received and Advertised (Line-by-Line Editing)
===============================================================================================

This section provides an example for using XPL to filter the routes to be received and advertised based on sets and route-filters in line editing mode.

#### Networking Requirements

On the BGP network shown in [Figure 1](#EN-US_TASK_0172366621__en-us_task_0172366618_fig_dc_vrp_xpl_cfg_001301), DeviceA and DeviceB belong to AS 100, and DeviceC, DeviceD, and DeviceE belong to AS 200. DeviceA imports routes 2.2.2.0/24, 3.3.3.0/24, 4.4.4.0/24, and 5.5.5.0/24. Requirements:

* DeviceA advertises routes 2.2.2.0/24, 3.3.3.0/24, and 4.4.4.0/24 only to DeviceB.
* After receiving the three routes, DeviceC needs to advertise all routes to DeviceE. DeviceD needs to advertise only routes 2.2.2.0/24 and 3.3.3.0/24 to DeviceE and the MED value of the route 2.2.2.0/24 must be greater than that of the route 2.2.2.0/24 advertised by DeviceC, so that DeviceE selects DeviceC as the egress for the traffic destined for 2.2.2.0/24.

To meet the preceding requirements, configure export or import policies. In this example, an export policy is configured on DeviceA, and two import policies are configured on DeviceE.

**Figure 1** Network diagram of filtering routes to be advertised and accepted  
![](images/fig_dc_vrp_xpl_cfg_001302.png)  

| Device Name | Interface | IP Address |
| --- | --- | --- |
| DeviceA | GE 0/3/0 | 1.1.5.2/24 |
| DeviceB | GE 0/3/0 | 1.1.5.1/24 |
| DeviceB | GE 0/3/1 | 1.1.4.2/24 |
| DeviceB | GE 0/3/2 | 1.1.3.2/24 |
| DeviceC | GE 0/3/1 | 1.1.1.2/24 |
| DeviceC | GE 0/3/2 | 1.1.3.1/24 |
| DeviceD | GE 0/3/1 | 1.1.2.2/24 |
| DeviceD | GE 0/3/2 | 1.1.4.1/24 |
| DeviceE | GE 0/3/1 | 1.1.2.1/24 |
| DeviceE | GE 0/3/2 | 1.1.1.1/24 |



#### Configuration Precautions

During the configuration, note the following:

* A prefix range needs to be specified for the prefix set as required.
* Prefix set names are case-sensitive.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic BGP functions on Device A, Device B, Device C, Device D, and Device E.
2. Configure four static routes on Device A and import them into BGP.
3. Configure an export policy on Device A and check the BGP routing table of Device B.
4. Configure two import policies on Device E and check the BGP routing table of Device E.

#### Data Preparation

To complete the configuration, you need the following data:

* Four static routes to be imported by Device A
* AS 100 (for Device A and Device B) and AS 200 (Device C, Device D, and Device E)
* Name of an IPv4 prefix set and the routes to be filtered

#### Procedure

1. Assign an IP address to each interface. For configuration details, see [Configuration Files](#EN-US_TASK_0172366621__section_dc_vrp_xpl_cfg_002105) in this section.
2. Configure basic BGP functions.
   
   
   
   # Configure Device A.
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] bgp 100
   ```
   ```
   [*DeviceA-bgp] peer 1.1.5.1 as-number 100
   ```
   ```
   [*DeviceA-bgp] commit
   ```
   ```
   [~DeviceA-bgp] quit
   ```
   
   # Configure Device B.
   
   ```
   <DeviceB> system-view
   ```
   ```
   [~DeviceB] bgp 100
   ```
   ```
   [*DeviceB-bgp] peer 1.1.5.2 as-number 100
   ```
   ```
   [*DeviceB-bgp] peer 1.1.3.1 as-number 200
   ```
   ```
   [*DeviceB-bgp] peer 1.1.4.1 as-number 200
   ```
   ```
   [*DeviceB-bgp] commit
   ```
   ```
   [~DeviceB-bgp] quit
   ```
   
   # Configure Device C:
   
   ```
   <DeviceC> system-view
   ```
   ```
   [~DeviceC] bgp 200
   ```
   ```
   [*DeviceC-bgp] peer 1.1.1.1 as-number 200
   ```
   ```
   [*DeviceC-bgp] peer 1.1.3.2 as-number 100
   ```
   ```
   [*DeviceC-bgp] commit
   ```
   ```
   [~DeviceC-bgp] quit
   ```
   
   # Configure Device D:
   
   ```
   <DeviceD> system-view
   ```
   ```
   [~DeviceD] bgp 200
   ```
   ```
   [*DeviceD-bgp] peer 1.1.2.1 as-number 200
   ```
   ```
   [*DeviceD-bgp] peer 1.1.4.2 as-number 100
   ```
   ```
   [*DeviceD-bgp] commit
   ```
   ```
   [~DeviceD-bgp] quit
   ```
   
   # Configure Device E.
   
   ```
   <DeviceE> system-view
   ```
   ```
   [~DeviceE] bgp 200
   ```
   ```
   [*DeviceE-bgp] peer 1.1.1.2 as-number 200
   ```
   ```
   [*DeviceE-bgp] peer 1.1.2.2 as-number 200
   ```
   ```
   [*DeviceE-bgp] commit
   ```
   ```
   [~DeviceE-bgp] quit
   ```
3. Configure four static routes on Device A and import them into BGP.
   
   
   ```
   [~DeviceA] ip route-static 2.2.2.0 255.255.255.0 NULL0
   ```
   ```
   [*DeviceA] ip route-static 3.3.3.0 255.255.255.0 NULL0
   ```
   ```
   [*DeviceA] ip route-static 4.4.4.0 255.255.255.0 NULL0
   ```
   ```
   [*DeviceA] ip route-static 5.5.5.0 255.255.255.0 NULL0
   ```
   ```
   [*DeviceA] bgp 100
   ```
   ```
   [*DeviceA-bgp] import-route static
   ```
   ```
   [*DeviceA-bgp] commit
   ```
   ```
   [~DeviceA-bgp] quit
   ```
   
   # Check the BGP routing table of Device B. The following command output shows that the four static routes have been added to the BGP routing table of Device B.
   
   ```
   [~DeviceB] display bgp routing-table
   ```
   ```
    
    BGP Local router ID is 1.1.5.1
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
   
   
    Total Number of Routes: 4 
           Network            NextHop        MED        LocPrf    PrefVal Path/Ogn
   
    *>i    2.2.2.0/24         1.1.5.2         0          100        0       ?
    *>i    3.3.3.0/24         1.1.5.2         0          100        0       ?
    *>i    4.4.4.0/24         1.1.5.2         0          100        0       ?
    *>i    5.5.5.0/24         1.1.5.2         0          100        0       ?
   ```
   
   # Check the BGP routing table of Device E. The following command output shows that two copies of the four static routes from Device C and Device D have been added to the BGP routing table of Device E.
   
   ```
   [~DeviceE] display bgp routing-table
   ```
   ```
    
    BGP Local router ID is 1.1.1.1
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
   
   
    Total Number of Routes: 8 
           Network            NextHop        MED        LocPrf    PrefVal Path/Ogn
   
      i    2.2.2.0/24         1.1.3.2                    100        0      100?
      i                       1.1.4.2                    100        0      100?
      i    3.3.3.0/24         1.1.4.2                    100        0      100?
      i                       1.1.3.2                    100        0      100?
      i    4.4.4.0/24         1.1.3.2                    100        0      100?
      i                       1.1.4.2                    100        0      100?
      i    5.5.5.0/24         1.1.4.2                    100        0      100?
      i                       1.1.3.2                    100        0      100?
   ```
4. Configure an export policy on Device A.
   
   
   
   # Configure an IPv4 prefix set named **prefix1** on Device A.
   
   ```
   [~DeviceA] xpl ip-prefix-list prefix1
   ```
   ```
   [~DeviceA-xpl-pfx] 2.2.2.0 24,
   ```
   ```
   [~DeviceA-xpl-pfx] 3.3.3.0 24,
   ```
   ```
   [~DeviceA-xpl-pfx] 4.4.4.0 24
   ```
   ```
   [~DeviceA-xpl-pfx] end-list
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure a route-filter named **r1** on Device A, apply **prefix1** to **r1**, and permit routes 2.2.2.0/24, 3.3.3.0/24, and 4.4.4.0/24.
   
   ```
   [~DeviceA] xpl route-filter r1
   ```
   ```
   [~DeviceA-xpl-filter] if ip route-destination in prefix1 then
   ```
   ```
   [~DeviceA-xpl-filter-if] approve
   ```
   ```
   [~DeviceA-xpl-filter-if] else
   ```
   ```
   [~DeviceA-xpl-filter-else] refuse
   ```
   ```
   [~DeviceA-xpl-filter-else] endif
   ```
   ```
   [~DeviceA-xpl-filter] end-filter
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure an export policy on Device A and apply **r1** to the policy to filter the routes to be advertised to Device B.
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] bgp 100
   ```
   ```
   [~DeviceA-bgp]  peer 1.1.5.1 route-filter r1 export
   ```
   ```
   [*DeviceA-bgp]  commit
   ```
   ```
   [~DeviceA-bgp]  quit
   ```
   
   # Check the BGP routing table of Device B. The following command output shows that the route 5.5.5.0/24 is not included in the BGP routing table of Device B.
   
   ```
   [~DeviceB] display bgp routing-table
   ```
   ```
    
    BGP Local router ID is 1.1.5.1
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
   
   
    Total Number of Routes: 3 
           Network            NextHop        MED        LocPrf    PrefVal Path/Ogn
   
    *>i    2.2.2.0/24         1.1.5.2         0          100        0       ?
    *>i    3.3.3.0/24         1.1.5.2         0          100        0       ?
    *>i    4.4.4.0/24         1.1.5.2         0          100        0       ?
   ```
5. Configure two import policies on Device E.
   
   
   
   # Configure a route-filter named **appmed** with a pre-defined variable to set the MED.
   
   ```
   [~DeviceE] xpl route-filter appmed($med)
   ```
   ```
   [~DeviceE-xpl-filter] apply med $med
   ```
   ```
   [~DeviceE-xpl-filter] end-filter
   ```
   ```
   [*DeviceE] commit
   ```
   
   # Configure a route-filter named **r2** on Device E to permit routes 2.2.2.0/24 and 3.3.3.0/24 and use **appmed** to set the MED of the route 2.2.2.0/24 to 200.
   
   ```
   [~DeviceE] xpl route-filter r2
   ```
   ```
   [~DeviceE-xpl-filter] if ip route-destination in {2.2.2.0 24} then
   ```
   ```
   [~DeviceE-xpl-filter-if] call route-filter appmed(200)
   ```
   ```
   [~DeviceE-xpl-filter-if] elseif ip route-destination in {2.2.2.0 24, 3.3.3.0 24} then
   ```
   ```
   [~DeviceE-xpl-filter-elif] approve
   ```
   ```
   [~DeviceE-xpl-filter-elif] else
   ```
   ```
   [~DeviceE-xpl-filter-else] refuse
   ```
   ```
   [~DeviceE-xpl-filter-else] endif
   ```
   ```
   [~DeviceE-xpl-filter] end-filter
   ```
   ```
   [*DeviceE] commit
   ```
   
   # Configure a route-filter named **r3** on Device E to set the MED of the route 2.2.2.0/24 to 100.
   
   ```
   [~DeviceE] xpl route-filter r3
   ```
   ```
   [~DeviceE-xpl-filter] if ip route-destination in {2.2.2.0 24} then
   ```
   ```
   [~DeviceE-xpl-filter-if] call route-filter appmed(100)
   ```
   ```
   [~DeviceE-xpl-filter-if] else
   ```
   ```
   [~DeviceE-xpl-filter-else] approve
   ```
   ```
   [~DeviceE-xpl-filter-else] endif
   ```
   ```
   [~DeviceE-xpl-filter] end-filter
   ```
   ```
   [*DeviceE] commit
   ```
   
   # Configure an import policy on Device E for the routes learned from Device D and apply **r2** to the policy. In addition, configure another import policy on Device E for the routes learned from Device C and apply **r3** to the policy.
   
   ```
   <DeviceE> system-view
   ```
   ```
   [~DeviceE] bgp 200
   ```
   ```
   [~DeviceE-bgp] peer 1.1.2.2 route-filter r2 import
   ```
   ```
   [*DeviceE-bgp] peer 1.1.1.2 route-filter r3 import
   ```
   ```
   [*DeviceE-bgp] commit
   ```
   ```
   [~DeviceE-bgp] quit
   ```
   
   # Check the BGP routing table of Device E. The following command output shows that the route 4.4.4.0/24 learned from Device D is not included in the BGP routing table of Device B and that the MED values of the routes 2.2.2.0/24 learned from Device C and Device D are 100 and 200, respectively.
   
   ```
   [~DeviceE] display bgp routing-table
   ```
   ```
    BGP Local router ID is 1.1.1.1
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
   
   
    Total Number of Routes: 5 
           Network            NextHop        MED        LocPrf    PrefVal Path/Ogn
   
      i    2.2.2.0/24         1.1.4.2         200        100        0      100?
      i                       1.1.3.2         100        100        0      100?
      i    3.3.3.0/24         1.1.4.2                    100        0      100?
      i                       1.1.3.2                    100        0      100?
      i    4.4.4.0/24         1.1.3.2                    100        0      100?
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 1.1.5.2 255.255.255.0
  #
  bgp 100
   peer 1.1.5.1 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    import-route static
    peer 1.1.5.1 enable
    peer 1.1.5.1 route-filter r1 export
  #
  ip route-static 2.2.2.0 255.255.255.0 NULL0
  ip route-static 3.3.3.0 255.255.255.0 NULL0
  ip route-static 4.4.4.0 255.255.255.0 NULL0
  ip route-static 5.5.5.0 255.255.255.0 NULL0
  #
  xpl route-filter r1
   if ip route-destination in prefix1 then
    approve
   else
    refuse
   endif
   end-filter
  #
  xpl ip-prefix-list prefix1
   2.2.2.0 24,
   3.3.3.0 24,
   4.4.4.0 24
   end-list
  #
  return
  ```
* DeviceB configuration file
  
  ```
  #
  sysname DeviceB
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 1.1.5.1 255.255.255.0
  #
  interface GigabitEthernet0/3/1
   undo shutdown
   ip address 1.1.4.2 255.255.255.0
  #
  interface GigabitEthernet0/3/2
   undo shutdown
   ip address 1.1.3.2 255.255.255.0
  #
  bgp 100
   peer 1.1.3.1 as-number 200
   peer 1.1.4.1 as-number 200
   peer 1.1.5.2 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.3.1 enable
    peer 1.1.4.1 enable
    peer 1.1.5.2 enable
  #
  return
  ```
* DeviceC configuration file
  
  ```
  #
  sysname DeviceC
  #
  interface GigabitEthernet0/3/1
   undo shutdown
   ip address 1.1.1.2 255.255.255.0
  #
  interface GigabitEthernet0/3/2
   undo shutdown
   ip address 1.1.3.1 255.255.255.0
  #
  bgp 200
   peer 1.1.1.1 as-number 200
   peer 1.1.3.2 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.1 enable
    peer 1.1.3.2 enable
  #
  return
  ```
* DeviceD configuration file
  
  ```
  #
  sysname DeviceD
  #
  interface GigabitEthernet0/3/1
   undo shutdown
   ip address 1.1.2.2 255.255.255.0
  #
  interface GigabitEthernet0/3/2
   undo shutdown
   ip address 1.1.4.1 255.255.255.0
  #
  bgp 200
   peer 1.1.2.1 as-number 200
   peer 1.1.4.2 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.2.1 enable
    peer 1.1.4.2 enable
  #
  return
  ```
* DeviceE configuration file
  
  ```
  #
  sysname DeviceE
  #
  interface GigabitEthernet0/3/1
   undo shutdown
   ip address 1.1.2.1 255.255.255.0
  #
  interface GigabitEthernet0/3/2
   undo shutdown
   ip address 1.1.1.1 255.255.255.0
  #
  bgp 200
   peer 1.1.1.2 as-number 200
   peer 1.1.2.2 as-number 200
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.2 enable
    peer 1.1.1.2 route-filter r3 import
    peer 1.1.2.2 enable
    peer 1.1.2.2 route-filter r2 import
  #
  xpl route-filter appmed($med)
   apply med $med
   end-filter
  #
  xpl route-filter r2
   if ip route-destination in {2.2.2.0 24} then
    call route-filter appmed(200)
   elseif ip route-destination in {2.2.2.0 24, 3.3.3.0 24} then
    approve
   else
    refuse
   endif
   end-filter
  #
  xpl route-filter r3
   if ip route-destination in {2.2.2.0 24} then
    call route-filter appmed(100)
   else
    approve
   endif
   end-filter
  #
  return
  ```