Example for Using XPL to Filter the Routes to Be Accepted and Advertised (Paragraph-by-Paragraph Editing)
=========================================================================================================

This section provides an example for using XPL to filter the routes to be accepted and advertised. This section provides an example for using XPL to filter the routes based on sets and route-filters in paragraph-by-paragraph editing mode.

#### Networking Requirements

On the BGP network shown in [Figure 1](#EN-US_TASK_0172366618__fig_dc_vrp_xpl_cfg_001301), DeviceA and DeviceB belong to AS 100, and DeviceC, DeviceD, and DeviceE belong to AS 200. DeviceA imports routes 2.2.2.0/24, 3.3.3.0/24, 4.4.4.0/24, and 5.5.5.0/24. Requirements:

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

1. Configure basic BGP functions on DeviceA, DeviceB, DeviceC, DeviceD, and DeviceE.
2. Configure static routes on DeviceA and import them to the BGP routing table.
3. Configure an export policy on DeviceA and check the filtering result on DeviceB.
4. Configure an import policy on DeviceE and check the filtering result on DeviceE.

#### Data Preparation

To complete the configuration, you need the following data:

* Five static routes imported on DeviceA
* DeviceA and DeviceB in AS 100, DeviceC, DeviceD, and DeviceE in AS 200.
* Name of an IPv4 prefix set and the routes to be filtered

#### Procedure

1. Assign an IP address to each interface. For details, see [Configuration Files](#EN-US_TASK_0172366618__section_dc_vrp_xpl_cfg_001305).
2. Configure basic BGP functions.
   
   
   
   # Configure DeviceA.
   
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
   
   # Configure DeviceB.
   
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
   
   # Configure DeviceC.
   
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
   
   # Configure DeviceD.
   
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
   
   # Configure DeviceE.
   
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
3. Configure five static routes on DeviceA and import them to the BGP routing table.
   
   
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
   
   # Check the BGP routing table of DeviceB. The command output shows that DeviceB has learned the imported static routes.
   
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
   
   # Check the BGP routing table on DeviceE. The command output shows that BGP has imported four static routes (one from DeviceC and one from DeviceD).
   
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
4. Configure a route advertisement policy on DeviceA.
   
   
   
   # Configure an IPv4 prefix set named **prefix1** on DeviceA.
   
   ```
   [~DeviceA] quit
   ```
   ```
   < Device A> edit xpl ip-prefix-list prefix1 //Enter the IPv4 prefix set paragraph-by-paragraph editing view.
   xpl ip-prefix-list prefix1
   2.2.2.0 24,
   3.3.3.0 24,
   4.4.4.0 24
   end-list
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After entering the paragraph-by-paragraph editing view, press **i** to enter the text editing mode.
   
   After performing the configuration in the text editing mode of the paragraph-by-paragraph editing view, press **Esc** to exit from the text editing mode, and press **:wq** and **Enter** to save the configuration and exit from the paragraph-by-paragraph editing view. For details, see "Example of Paragraph-by-Paragraph Editing Operations" in [Introduction to XPL Paragraph-by-Paragraph Editing](dc_vrp_xpl_cfg_0002.html).
   
   After entering the XPL paragraph-by-paragraph editing view, press **i**. **-- INSERT --** is displayed at the bottom of the interface, indicating that you can enter content. Configure an IPv4 prefix set named **prefix1** in the paragraph-by-paragraph editing view and separate elements with commas (,), as shown in the following figure.
   
   ![](figure/en-us_image_0000001781264249.png)
   
   Press **Esc** to exit the text editing mode. **-- INSERT --** at the bottom of the interface then disappears. Enter **:wq** and press **Enter** to save the configuration and exit the paragraph-by-paragraph editing view. The system asks you whether to commit the configuration. If you enter **y** and return to the user view, the configuration is saved successfully.
   
   ![](figure/en-us_image_0000001781267277.png)
   
   ![](figure/en-us_image_0000001781387245.png)
   
   ![](figure/en-us_image_0000001781387801.png)
   
   To add or delete a prefix, run the [**edit xpl ip-prefix-list**](cmdqueryname=edit+xpl+ip-prefix-list) *prefix1* command again to enter the paragraph-by-paragraph editing view. Press **i**. After **-- INSERT --** is displayed at the bottom of the interface, use arrow keys to move the cursor to the desired position and modify the prefix. Use commas (,) to separate elements. Otherwise, an error may occur, and the configuration cannot be committed. For example, to delete the prefix 2.2.2.0 24, use arrow keys to move the cursor to the corresponding position and delete the prefix, as shown in the following figure.
   
   ![](figure/en-us_image_0000001734505434.png)
   
   After the modification is complete, press **Esc** to exit the text editing mode. **-- INSERT --** at the bottom of the interface disappears. Enter **:wq** and press **Enter** to save the configuration and exit the paragraph-by-paragraph editing view. The system asks you whether to commit the configuration. If you enter **y** and return to the user view, the configuration is successfully modified. The following sections do not provide detailed XPL operations. Only the content entered on the paragraph-by-paragraph editing interface is shown.
   
   ![](figure/en-us_image_0000001734152964.png)
   
   ![](figure/en-us_image_0000001784557413.png)
   
   # Configure a route-filter named **r1** on Device A, apply **prefix1** to **r1**, and permit routes 2.2.2.0/24, 3.3.3.0/24, and 4.4.4.0/24.
   
   ```
   < Device A> edit xpl route-filter r1 //Enter the route-filter paragraph-by-paragraph editing view.
   
   xpl route-filter r1
   if ip route-destination in prefix1 then
   approve
   else
   refuse
   endif
   end-filter
   ```
   
   ![](figure/en-us_image_0000001781393633.png)
   
   # Configure an advertisement policy on DeviceA and use **r1** to filter the routes to be advertised to DeviceB.
   
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
   
   # Check the BGP routing table of DeviceB. The following command output shows that the route 5.5.5.0/24 is not included in the BGP routing table of DeviceB.
   
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
5. Configure a policy for receiving routes on DeviceE.
   
   
   
   # Configure a route-filter named **appmed** with parameters on DeviceE to set MEDs for routes.
   
   ```
   [~DeviceE] quit
   ```
   ```
   < Device E> edit xpl route-filter appmed //Enter the route-filter paragraph-by-paragraph editing view.
   
   xpl route-filter appmed($med)
   apply med $med
   end-filter
   ```
   
   ![](figure/en-us_image_0000001734158368.png)
   
   # Configure route-filter named **r2** on DeviceE to permit routes 2.2.2.0/24 and 3.3.3.0/24 and use **appmed** to set the MED of the route 2.2.2.0/24 to 200.
   
   ```
   < Device E> edit xpl route-filter r2 //Enter the route-filter paragraph-by-paragraph editing view.
   
   xpl route-filter r2
   if ip route-destination in {2.2.2.0 24} then
   call route-filter appmed(200)
   elseif ip route-destination in {2.2.2.0 24, 3.3.3.0 24} then
   approve
   else
   refuse
   endif
   end-filter
   ```
   
   ![](figure/en-us_image_0000001781400549.png)
   
   # Configure a route-filter named **r3** on Device E to set the MED of 2.2.2.0/24 to 100.
   
   ```
   < Device E> edit xpl route-filter r3 //Enter the route-filter paragraph-by-paragraph editing view.
   xpl route-filter r3
   if ip route-destination in {2.2.2.0 24} then
   call route-filter appmed(100)
   else
   approve
   endif
   end-filter
   ```
   
   ![](figure/en-us_image_0000001734321280.png)
   
   # Configure an import policy on DeviceE, and apply **r2** to the export policy for the routes advertised by DeviceD and **r3** to the export policy for the routes advertised by DeviceC.
   
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
   
   # Check the BGP routing table of DeviceE. The following command output shows that the route 4.4.4.0/24 learned from DeviceD is not included in the BGP routing table of DeviceE, and the MED values of the routes 2.2.2.0/24 learned from DeviceC and DeviceD are 100 and 200, respectively.
   
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