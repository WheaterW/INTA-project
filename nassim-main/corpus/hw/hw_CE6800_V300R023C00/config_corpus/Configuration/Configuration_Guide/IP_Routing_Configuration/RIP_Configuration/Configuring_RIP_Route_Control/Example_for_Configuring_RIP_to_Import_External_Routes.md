Example for Configuring RIP to Import External Routes
=====================================================

Example for Configuring RIP to Import External Routes

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001176662715__fig_dc_vrp_rip_cfg_005001), two RIP processes, RIP 100 and RIP 200, run on DeviceB. DeviceB exchanges routing information with DeviceA through RIP 100 and with DeviceC through RIP 200.

Both of DeviceB's processes are required to import RIP routes from each other, and the default metric of the routes imported from RIP 200 is set to 3. In addition, a route-policy needs to be configured on DeviceB to filter out the route (192.168.4.0/24) imported from RIP 200 so that it is not advertised to DeviceA.

**Figure 1** Network diagram of configuring RIP to import external routes![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001130623192.png)

#### Precautions

Run one of the following commands to set a metric for imported routes. The commands are listed in descending order of priority:

* Run the [**apply cost**](cmdqueryname=apply+cost) command to apply a metric to routes matching a route-policy.
* Run the **import-route** command in the RIP view to set a metric for imported routes.
* Run the **default-cost** command in the RIP view to set a metric for default routes.

To improve security, you are advised to configure RIP-2 packet authentication. For details, see "Improving RIP Network Security." The following example describes how to configure an authentication mode for RIP-2 packets. For details, see "Example for Configuring Basic RIP Functions."


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable RIP on and specify a network segment for each device.
2. Configure two RIP processes on DeviceB to import routes from each other and set the default metric of the routes imported from RIP 200 to 3.
3. Configure an ACL on DeviceB to filter out the routes imported from RIP 200.

#### Procedure

1. Assign an IP address to each interface. For detailed configurations, see [Configuration Scripts](#EN-US_TASK_0000001176662715__postreq24192593172748).
2. Configure basic RIP functions.
   
   
   
   # Create RIP process 100 on DeviceA.
   
   ```
   [~DeviceA] rip 100
   [*DeviceA-rip-100] network 192.168.0.0
   [*DeviceA-rip-100] network 192.168.1.0
   [*DeviceA-rip-100] quit
   [*DeviceA] commit
   ```
   
   # Create RIP process 100 and RIP process 200 on DeviceB.
   
   ```
   [~DeviceB] rip 100
   [*DeviceB-rip-100] network 192.168.1.0
   [*DeviceB-rip-100] quit
   [*DeviceB] rip 200
   [*DeviceB-rip-200] network 192.168.2.0
   [*DeviceB-rip-200] quit
   [*DeviceB] commit
   ```
   
   # Create RIP process 200 on DeviceC.
   
   ```
   [~DeviceC] rip 200
   [*DeviceC-rip-200] network 192.168.2.0
   [*DeviceC-rip-200] network 192.168.3.0
   [*DeviceC-rip-200] network 192.168.4.0
   [*DeviceC-rip-200] quit
   [*DeviceC] commit
   ```
3. Configure RIP to import external routes.
   
   
   
   # On DeviceB, set the default metric of imported routes to 3 and configure the two RIP processes to import routes into each other's routing table.
   
   ```
   [~DeviceB] rip 100
   [*DeviceB-rip-100] default-cost 3
   [*DeviceB-rip-100] import-route rip 200
   [*DeviceB-rip-100] quit
   [*DeviceB] rip 200
   [*DeviceB-rip-200] import-route rip 100
   [*DeviceB-rip-200] quit
   [*DeviceB] commit
   ```
4. Configure RIP to filter the imported routes.
   
   
   
   # Configure an ACL on DeviceB to deny the packets sent from 192.168.4.0/24.
   
   ```
   [~DeviceB] acl 2000
   [*DeviceB-acl4-basic-2000] rule deny source 192.168.4.0 0.0.0.255
   [*DeviceB-acl4-basic-2000] rule permit
   [*DeviceB-acl4-basic-2000] quit
   [*DeviceB] commit
   ```
   
   # On DeviceB, filter out the route 192.168.4.0/24 imported from RIP 200 according to the ACL rule.
   
   ```
   [~DeviceB] rip 100
   [*DeviceB-rip-100] filter-policy 2000 export
   [*DeviceB-rip-100] quit
   [*DeviceB] commit
   ```

#### Verifying the Configuration

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
    192.168.0.0/24  Direct 0    0        D      192.168.0.1    100GE1/0/2
    192.168.0.1/32  Direct 0    0        D      127.0.0.1      100GE1/0/2
    192.168.1.0/24  Direct 0    0        D      192.168.1.1    100GE1/0/1
    192.168.1.1/32  Direct 0    0        D      127.0.0.1      100GE1/0/1
    192.168.1.2/32  Direct 0    0        D      192.168.1.2    100GE1/0/1
```

The routing table of DeviceA does not contain the routes imported from other processes.

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
  192.168.0.0/24    Direct 0    0       D       192.168.0.1     100GE1/0/2
  192.168.0.1/32    Direct 0    0       D       127.0.0.1       100GE1/0/2
  192.168.1.0/24    Direct 0    0       D       192.168.1.1     100GE1/0/1
  192.168.1.1/32    Direct 0    0       D       127.0.0.1       100GE1/0/1
  192.168.1.2/32    Direct 0    0       D       192.168.1.2     100GE1/0/1
  192.168.2.0/24  RIP    100  4       D          192.168.1.2     100GE1/0/1
  192.168.3.0/24  RIP    100  4       D          192.168.1.2     100GE1/0/1
  192.168.4.0/24  RIP    100  4       D          192.168.1.2     100GE1/0/1
```

The RIP routing table of DeviceA contains routes to 192.168.2.0/24, 192.168.3.0/24, and 192.168.3.0/24, which are learned from DeviceB through RIP process 200.

# Check the routing table of DeviceA after external routes are filtered.

```
[~DeviceA] display ip routing-table
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table: _public_
         Destinations : 9        Routes : 9
Destination/Mask    Proto  Pre  Cost   Flags    NextHop         Interface
      127.0.0.0/8   Direct 0    0       D       127.0.0.1       InLoopBack0
      127.0.0.1/32  Direct 0    0       D       127.0.0.1       InLoopBack0
    192.168.0.0/24  Direct 0    0       D       192.168.0.1     100GE1/0/2
    192.168.0.1/32  Direct 0    0       D       127.0.0.1       100GE1/0/2
    192.168.1.0/24  Direct 0    0       D       192.168.1.1     100GE1/0/1
    192.168.1.1/32  Direct 0    0       D       127.0.0.1       100GE1/0/1
    192.168.1.2/32  Direct 0    0       D       192.168.1.2     100GE1/0/1
    192.168.2.0/24  RIP    100  4       D       192.168.1.2     100GE1/0/1
    192.168.3.0/24  RIP    100  4       D       192.168.1.2     100GE1/0/1
```

The command output shows that the RIP routing table of DeviceA is changed. That is, the route originating from 192.168.4.0/24 is denied.


#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.1.1 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.0.1 255.255.255.0
  #
  rip 100
   network 192.168.0.0
   network 192.168.1.0
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  acl number 2000
   rule 5 deny source 192.168.4.0 0.0.0.255
   rule 10 permit
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.1.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.2.1 255.255.255.0
  #
  rip 100
   default-cost 3
   network 192.168.1.0
   filter-policy 2000 export
   import-route rip 200
  #
  rip 200
   network 192.168.2.0
   import-route rip 100
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
   ip address 192.168.2.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.3.1 255.255.255.0
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 192.168.4.1 255.255.255.0
  #
  rip 200
   network 192.168.2.0
   network 192.168.3.0
   network 192.168.4.0
  #
  return
  ```