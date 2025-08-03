Example for Configuring RIP to Import Routes
============================================

This section describes how to configure RIP to import external routes to increase the number of routes in the RIP routing table.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172365885__fig_dc_vrp_rip_cfg_005001), DeviceB runs two RIP processes: RIP 100 and RIP 200. DeviceB exchanges routing information with DeviceA through RIP 100 and with DeviceC through RIP 200.

It is required that DeviceB be configured to import routes from two processes to each other and that the default metric of the routes imported from RIP 200 be set to 3.

In addition, a filtering policy needs to be configured on DeviceB to filter out the route 192.168.4.0/24 imported from RIP 200 so that the route is not advertised to DeviceA.

**Figure 1** Network diagram of configuring RIP to import external routes![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent GE0/1/0, GE0/2/0, and GE0/3/0, respectively.


  
![](figure/en-us_image_0256711359.png)

#### Context

Run one of the following commands to set a metric for imported routes. The commands are listed in descending order of priority:

* **apply cost**: sets a route metric.
* **import-route** (RIP view): sets a metric for imported routes.
* **default-cost** (RIP view): sets a metric for default routes.

#### Precautions

To improve security, you are advised to configure RIP-2 packet authentication. For details, see "Improving RIP Network Security." The following example describes how to configure an authentication mode for RIP-2 packets. For details, see "Example for Configuring Basic RIP Functions."


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable RIP 100 and RIP 200 on each Router and specify network segments.
2. Configure two RIP processes on DeviceB to import routes from each other and set the default metric of the routes imported from RIP 200 to 3.
3. Configure an ACL on DeviceB to filter out the routes imported from RIP 200.

#### Data Preparation

To complete the configuration, you need the following data:

* RIP network segments 192.168.0.0 and 192.168.1.0 on DeviceA
* RIP network segments 192.168.1.0 and 192.168.2.0 on DeviceB
* RIP network segments 192.168.2.0, 192.168.3.0, and 192.168.4.0 on DeviceC

#### Procedure

1. Assign an IP address to each interface. For configuration details, see configuration files in this section.
2. Configure basic RIP functions.
   
   
   
   # Enable RIP process 100 on DeviceA.
   
   ```
   [~DeviceA] rip 100
   ```
   ```
   [*DeviceA-rip-100] network 192.168.0.0
   ```
   ```
   [*DeviceA-rip-100] network 192.168.1.0
   ```
   ```
   [*DeviceA-rip-100] commit
   ```
   ```
   [~DeviceA-rip-100] quit
   ```
   
   # Enable RIP 100 and RIP 200 on DeviceB.
   
   ```
   [~DeviceB] rip 100
   ```
   ```
   [*DeviceB-rip-100] network 192.168.1.0
   ```
   ```
   [*DeviceB-rip-100] quit
   ```
   ```
   [*DeviceB] rip 200
   ```
   ```
   [*DeviceB-rip-200] network 192.168.2.0
   ```
   ```
   [*DeviceB-rip-200] commit
   ```
   ```
   [~DeviceB-rip-200] quit
   ```
   
   # Enable RIP process 200 on DeviceC.
   
   ```
   [~DeviceC] rip 200
   ```
   ```
   [*DeviceC-rip-200] network 192.168.2.0
   ```
   ```
   [*DeviceC-rip-200] network 192.168.3.0
   ```
   ```
   [*DeviceC-rip-200] network 192.168.4.0
   ```
   ```
   [*DeviceC-rip-200] commit
   ```
   ```
   [~DeviceC-rip-200] quit
   ```
   
   # Check the routing table of DeviceA.
   
   ```
   [~DeviceA] display ip routing-table
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table: _public_
            Destinations : 7       Routes : 7
   
   Destination/Mask    Proto  Pre  Cost   Flags    NextHop        Interface
   
         127.0.0.0/8   Direct 0    0        D      127.0.0.1      InLoopBack0
         127.0.0.1/32  Direct 0    0        D      127.0.0.1      InLoopBack0
       192.168.0.0/24  Direct 0    0        D      192.168.0.1    GigabitEthernet0/2/0
       192.168.0.1/32  Direct 0    0        D      127.0.0.1      GigabitEthernet0/2/0
       192.168.1.0/24  Direct 0    0        D      192.168.1.1    GigabitEthernet0/1/0
       192.168.1.1/32  Direct 0    0        D      127.0.0.1      GigabitEthernet0/1/0
       192.168.1.2/32  Direct 0    0        D      192.168.1.2    GigabitEthernet0/1/0
   ```
   
   The command output shows that the routing table of DeviceA does not contain the routes of other processes.
3. Configure RIP to import external routes.
   
   
   
   # Set the default route metric to 3 on DeviceB and import routes of the two RIP processes into the routing table of each other.
   
   ```
   [~DeviceB] rip 100
   ```
   ```
   [*DeviceB-rip-100] default-cost 3
   ```
   ```
   [*DeviceB-rip-100] import-route rip 200
   ```
   ```
   [*DeviceB-rip-100] quit
   ```
   ```
   [*DeviceB] rip 200
   ```
   ```
   [*DeviceB-rip-200] import-route rip 100
   ```
   ```
   [*DeviceB-rip-200] quit
   ```
   ```
   [*DeviceB] commit
   ```
   
   # Check the routing table of DeviceA after the routes are imported.
   
   ```
   [~DeviceA] display ip routing-table
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table: _public_
            Destinations : 10       Routes : 10
   
   Destination/Mask    Proto  Pre  Cost   Flags    NextHop         Interface
   
        127.0.0.0/8    Direct 0    0       D       127.0.0.1       InLoopBack0
       127.0.0.1/32    Direct 0    0       D       127.0.0.1       InLoopBack0
     192.168.0.0/24    Direct 0    0       D       192.168.0.1     GigabitEthernet0/2/0
     192.168.0.1/32    Direct 0    0       D       127.0.0.1       GigabitEthernet0/2/0
     192.168.1.0/24    Direct 0    0       D       192.168.1.1     GigabitEthernet0/1/0
     192.168.1.1/32    Direct 0    0       D       127.0.0.1       GigabitEthernet0/1/0
     192.168.1.2/32    Direct 0    0       D       192.168.1.2     GigabitEthernet0/1/0
     192.168.2.0/24   RIP    100  4       D       192.168.1.2     GigabitEthernet0/1/0
     192.168.3.0/24   RIP    100  4       D       192.168.1.2     GigabitEthernet0/1/0
     192.168.4.0/24   RIP    100  4       D       192.168.1.2     GigabitEthernet0/1/0
   ```
   
   The RIP routing table of DeviceA contains routes 192.168.2.0/24, 192.168.3.0/24, and 192.168.3.0/24. These new routes are learned from RIP process 200 on DeviceB.
4. Configure RIP to filter imported routes.
   
   
   
   # Configure an ACL on DeviceB and set a rule to deny the packets with source address 192.168.4.0/24.
   
   ```
   [~DeviceB] acl 2000
   ```
   ```
   [*DeviceB-acl4-basic-2000] rule deny source 192.168.4.0 0.0.0.255
   ```
   ```
   [*DeviceB-acl4-basic-2000] rule permit
   ```
   ```
   [*DeviceB-acl4-basic-2000] quit
   ```
   
   # On DeviceB, filter out the route 192.168.4.0/24 imported from RIP 200 according to the ACL rule.
   
   ```
   [*DeviceB] rip 100
   ```
   ```
   [*DeviceB-rip-100] filter-policy 2000 export
   ```
   ```
   [*DeviceB-rip-100] quit
   ```
   ```
   [*DeviceB] commit
   ```
5. Verify the configuration.
   
   
   
   # Check the routing table of DeviceA after the filtering.
   
   ```
   [~DeviceA] display ip routing-table
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table: _public_
            Destinations : 9        Routes : 9
   
   Destination/Mask    Proto  Pre  Cost   Flags    NextHop         Interface
         127.0.0.0/8   Direct 0    0       D       127.0.0.1       InLoopBack0
         127.0.0.1/32  Direct 0    0       D       127.0.0.1       InLoopBack0
       192.168.0.0/24  Direct 0    0       D       192.168.0.1     GigabitEthernet0/2/0
       192.168.0.1/32  Direct 0    0       D       127.0.0.1       GigabitEthernet0/2/0
       192.168.1.0/24  Direct 0    0       D       192.168.1.1     GigabitEthernet0/1/0
       192.168.1.1/32  Direct 0    0       D       127.0.0.1       GigabitEthernet0/1/0
       192.168.1.2/32  Direct 0    0       D       192.168.1.2     GigabitEthernet0/1/0
       192.168.2.0/24  RIP    100  4       D       192.168.1.2     GigabitEthernet0/1/0
       192.168.3.0/24  RIP    100  4       D       192.168.1.2     GigabitEthernet0/1/0
   ```
   
   The command output shows that the RIP routing table of DeviceA changes. That is, the route with the source address 192.168.4.0/24 is denied.

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceA
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.0.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.1.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  rip 100
  ```
  ```
   network 192.168.0.0
  ```
  ```
   network 192.168.1.0
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceB configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceB
  ```
  ```
  #
  ```
  ```
  acl number 2000
  ```
  ```
   rule 5 deny source 192.168.4.0 0.0.0.255
  ```
  ```
   rule 10 permit
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.1.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.2.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  rip 100
  ```
  ```
   default-cost 3
  ```
  ```
   network 192.168.1.0
  ```
  ```
   filter-policy 2000 export
  ```
  ```
   import-route rip 200
  ```
  ```
  #
  ```
  ```
  rip 200
  ```
  ```
   network 192.168.2.0
  ```
  ```
   import-route rip 100
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceC configuration file
  
  ```
  #
  ```
  ```
   sysname DeviceC
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.2.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.3.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/3/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.4.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  rip 200
  ```
  ```
   network 192.168.2.0
  ```
  ```
   network 192.168.3.0
  ```
  ```
   network 192.168.4.0
  ```
  ```
  #
  ```
  ```
  return
  ```