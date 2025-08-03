Example for Filtering Routes to Be Received and Those to Be Advertised
======================================================================

Example for Filtering Routes to Be Received and Those to Be Advertised

#### Networking Requirements

On the OSPF network shown in [Figure 1](#EN-US_TASK_0000001176743437__fig_dc_vrp_route-policy_cfg_002901), DeviceA receives routes from the Internet and provides some of the Internet routes for DeviceB. It is required that DeviceA advertise only the routes 172.16.17.0/24, 172.16.18.0/24, and 172.16.19.0/24 to DeviceB, DeviceC accept only the route 172.16.18.0/24, and that DeviceD accept all the routes advertised by DeviceB.

**Figure 1** Filtering the routes to be received and those to be advertised![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.


  
![](figure/en-us_image_0000001176743449.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IPv4 addresses for interfaces on each routing device.
2. Configure basic OSPF functions on DeviceA, DeviceB, DeviceC, and DeviceD.
3. Configure static routes on DeviceA and import these routes into the OSPF routing table.
4. Configure an export policy for filtering routes to be advertised on DeviceA.
5. Configure an import policy for filtering routes to be received on DeviceC.

#### Procedure

1. Configure IPv4 addresses for interfaces on each routing device.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ip address 192.168.1.1 255.255.255.0
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB, DeviceC, and DeviceD are similar to the configuration of DeviceA. For detailed configurations, see [Configuration Scripts](#EN-US_TASK_0000001176743437__postreq24192593172748).
2. Configure OSPF routes.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] ospf
   [*DeviceA-ospf-1] area 0
   [*DeviceA-ospf-1-area-0.0.0.0] network 192.168.1.0 0.0.0.255
   [*DeviceA-ospf-1-area-0.0.0.0] quit
   [*DeviceA-ospf-1] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] ospf
   [*DeviceB-ospf-1] area 0
   [*DeviceB-ospf-1-area-0.0.0.0] network 192.168.1.0 0.0.0.255
   [*DeviceB-ospf-1-area-0.0.0.0] network 192.168.2.0 0.0.0.255
   [*DeviceB-ospf-1-area-0.0.0.0] network 192.168.3.0 0.0.0.255
   [*DeviceB-ospf-1-area-0.0.0.0] quit
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] ospf
   [*DeviceC-ospf-1] area 0
   [*DeviceC-ospf-1-area-0.0.0.0] network 192.168.2.0 0.0.0.255
   [*DeviceC-ospf-1-area-0.0.0.0] quit
   [*DeviceC-ospf-1] quit
   [*DeviceC] commit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] ospf
   [*DeviceD-ospf-1] area 0
   [*DeviceD-ospf-1-area-0.0.0.0] network 192.168.3.0 0.0.0.255
   [*DeviceD-ospf-1-area-0.0.0.0] quit
   [*DeviceD] commit
   ```
3. Configure five static routes on DeviceA and import these routes into the OSPF routing table.
   
   
   ```
   [~DeviceA] ip route-static 172.16.16.0 24 NULL0
   [*DeviceA] ip route-static 172.16.17.0 24 NULL0
   [*DeviceA] ip route-static 172.16.18.0 24 NULL0
   [*DeviceA] ip route-static 172.16.19.0 24 NULL0
   [*DeviceA] ip route-static 172.16.20.0 24 NULL0
   [*DeviceA] ospf
   [*DeviceA-ospf-1] import-route static
   [*DeviceA-ospf-1] quit
   [*DeviceA] commit
   ```
   
   # Check the IP routing table on DeviceB. The following command output shows that the five static routes have been imported into the OSPF routing table.
   
   ```
   [~DeviceB] display ip routing-table
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : Public
            Destinations : 22       Routes : 22
   
   Destination/Mask    Proto  Pre  Cost        Flags NextHop       Interface
   
           1.1.1.1/32  Direct 0    0             D  127.0.0.1       LoopBack1
         127.0.0.0/8   Direct 0    0             D  127.0.0.1       InLoopBack0
         127.0.0.1/32  Direct 0    0             D  127.0.0.1       InLoopBack0
   127.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
   255.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
      172.16.16.0/24  O_ASE  150  1             D  192.168.1.1     100GE1/0/1
      172.16.17.0/24  O_ASE  150  1             D  192.168.1.1     100GE1/0/1
      172.16.18.0/24  O_ASE  150  1             D  192.168.1.1     100GE1/0/1
      172.16.19.0/24  O_ASE  150  1             D  192.168.1.1     100GE1/0/1
      172.16.20.0/24  O_ASE  150  1             D  192.168.1.1     100GE1/0/1
       192.168.1.0/24  Direct 0    0             D  192.168.1.2     100GE1/0/1
       192.168.1.1/32  Direct 0    0             D  192.168.1.1     100GE1/0/1
       192.168.1.2/32  Direct 0    0             D  127.0.0.1       100GE1/0/1
     192.168.1.255/32  Direct 0    0             D  127.0.0.1       100GE1/0/1
       192.168.2.0/24  Direct 0    0             D  192.168.2.1     100GE1/0/3
       192.168.2.1/32  Direct 0    0             D  127.0.0.1       100GE1/0/3
       192.168.2.2/32  Direct 0    0             D  192.168.2.2     100GE1/0/3
     192.168.2.255/32  Direct 0    0             D  127.0.0.1       100GE1/0/3
       192.168.3.0/24  Direct 0    0             D  192.168.3.1     100GE1/0/2
       192.168.3.1/32  Direct 0    0             D  127.0.0.1       100GE1/0/2
       192.168.3.2/32  Direct 0    0             D  192.168.3.2     100GE1/0/2
     192.168.3.255/32  Direct 0    0             D  127.0.0.1       100GE1/0/2
   ```
4. Configure an export policy to filter the routes to be advertised.
   
   
   
   # Configure the IP prefix list named **a2b** on DeviceA.
   
   ```
   [~DeviceA] ip ip-prefix a2b index 10 permit 172.16.17.0 24
   [*DeviceA] ip ip-prefix a2b index 20 permit 172.16.18.0 24
   [*DeviceA] ip ip-prefix a2b index 30 permit 172.16.19.0 24
   [*DeviceA] commit
   ```
   
   # Configure an export policy on DeviceA to filter routes based on the IP prefix list **a2b**.
   
   ```
   [~DeviceA] ospf
   [*DeviceA-ospf-1] filter-policy ip-prefix a2b export static
   [*DeviceA-ospf-1] quit
   [*DeviceA] commit
   ```
5. Configure an import policy to filter the routes to be received.
   
   
   
   # Configure an IP prefix list named **in** on DeviceC.
   
   ```
   [~DeviceC] ip ip-prefix in index 10 permit 172.16.18.0 24
   [*DeviceC] commit
   ```
   
   # Configure an import policy on DeviceC to use the IP prefix list named **in** to filter routes.
   
   ```
   [~DeviceC] ospf
   [*DeviceC-ospf-1] filter-policy ip-prefix in import
   [*DeviceC] commit
   ```

#### Verifying the Configuration

# Check the IP routing table on DeviceB.

```
[~DeviceB] display ip routing-table
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table : Public
         Destinations : 20       Routes : 20

Destination/Mask    Proto  Pre  Cost        Flags NextHop         Interface

        1.1.1.1/32  Direct 0    0             D  127.0.0.1       LoopBack1
      127.0.0.0/8   Direct 0    0             D  127.0.0.1       InLoopBack0
      127.0.0.1/32  Direct 0    0             D  127.0.0.1       InLoopBack0
127.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
255.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
  172.16.17.0/24  O_ASE  150   1            D   192.168.1.1     100GE1/0/1
  172.16.18.0/24  O_ASE  150   1            D   192.168.1.1     100GE1/0/1
  172.16.19.0/24  O_ASE  150   1            D   192.168.1.1     100GE1/0/1
    192.168.1.0/24  Direct 0    0             D  192.168.1.2      100GE1/0/1
    192.168.1.1/32  Direct 0    0             D  192.168.1.1      100GE1/0/1
    192.168.1.2/32  Direct 0    0             D  127.0.0.1        100GE1/0/1
  192.168.1.255/32  Direct 0    0             D  127.0.0.1        100GE1/0/1
    192.168.2.0/24  Direct 0    0             D  192.168.2.1      100GE1/0/3
    192.168.2.1/32  Direct 0    0             D  127.0.0.1        100GE1/0/3
    192.168.2.2/32  Direct 0    0             D  192.168.2.2      100GE1/0/3
  192.168.2.255/32  Direct 0    0             D  127.0.0.1        100GE1/0/3
    192.168.3.0/24  Direct 0    0             D  192.168.3.1      100GE1/0/2
    192.168.3.1/32  Direct 0    0             D  127.0.0.1        100GE1/0/2
    192.168.3.2/32  Direct 0    0             D  192.168.3.2      100GE1/0/2
  192.168.3.255/32  Direct 0    0             D  127.0.0.1        100GE1/0/2
```

The command output shows that DeviceB has accepted only three routes (those matching the IP prefix list **a2b**).

# Check the IP routing table on DeviceC.

```
[~DeviceC] display ip routing-table
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table : Public
         Destinations : 12       Routes : 12

Destination/Mask    Proto  Pre  Cost        Flags NextHop      Interface

        1.1.1.1/32  O_ASE  10   1             D  192.168.2.1    100GE1/0/1
      127.0.0.0/8   Direct 0    0             D  127.0.0.1      InLoopBack0
      127.0.0.1/32  Direct 0    0             D  127.0.0.1      InLoopBack0
127.255.255.255/32  Direct 0    0             D  127.0.0.1      InLoopBack0
255.255.255.255/32  Direct 0    0             D  127.0.0.1      InLoopBack0
  172.16.18.0/24  O_ASE  150  1             D  192.168.2.1    100GE1/0/1
    192.168.1.0/24  O_ASE  10   2             D  192.168.2.1     100GE1/0/1
    192.168.2.0/24  Direct 0    0             D  192.168.2.2     100GE1/0/1
    192.168.2.1/32  Direct 0    0             D  192.168.2.1     100GE1/0/1
    192.168.2.2/32  Direct 0    0             D  127.0.0.1       100GE1/0/1
  192.168.2.255/32  Direct 0    0             D  127.0.0.1       100GE1/0/1
    192.168.3.0/24  O_ASE  10   2             D  192.168.2.1     100GE1/0/1
```

The command output shows that DeviceC has accepted only one route (the one matching the IP prefix list **in**).

# Check the OSPF routing table on DeviceC.

```
[~DeviceC] display ospf routing
          OSPF Process 1 with Router ID 192.168.2.2
                   Routing Tables

 Routing for Network
 Destination        Cost       Type       NextHop         AdvRouter       Area

 1.1.1.1/32         1          Stub       192.168.2.1     1.1.1.1         0.0.0.0
 192.168.1.0/24     2          Transit    192.168.2.1     192.168.1.1     0.0.0.0
 192.168.3.0/24     2          Stub       192.168.2.1     1.1.1.1         0.0.0.0

 Routing for ASEs
 Destination        Cost       Type       Tag        NextHop         AdvRouter

 172.16.17.0/24    1          Type2      1          192.168.2.1     192.168.1.1

 172.16.18.0/24    1          Type2      1          192.168.2.1     192.168.1.1

 172.16.19.0/24    1          Type2      1          192.168.2.1     192.168.1.1


 Total Nets: 6
 Intra Area: 3  Inter Area: 0  ASE: 3  NSSA: 0
```

The command output shows that the OSPF routing table has accepted three routes (those matching the IP prefix list **a2b**). This is because the **filter-policy import** command is used to filter the routes that are to be added to the local core routing table from the protocol routing table.


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
  ospf 1
   filter-policy ip-prefix a2b export static
   import-route static
   area 0.0.0.0
    network 192.168.1.0 0.0.0.255
  #
  ip ip-prefix a2b index 10 permit 172.16.17.0 24
  ip ip-prefix a2b index 20 permit 172.16.18.0 24
  ip ip-prefix a2b index 30 permit 172.16.19.0 24
  #
  ip route-static 172.16.16.0 255.255.255.0 NULL0
  ip route-static 172.16.17.0 255.255.255.0 NULL0
  ip route-static 172.16.18.0 255.255.255.0 NULL0
  ip route-static 172.16.19.0 255.255.255.0 NULL0
  ip route-static 172.16.20.0 255.255.255.0 NULL0
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
   ip address 192.168.1.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.3.1 255.255.255.0
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 192.168.2.1 255.255.255.0
  #
  ospf 1
   area 0.0.0.0
    network 192.168.1.0 0.0.0.255
    network 192.168.2.0 0.0.0.255
    network 192.168.3.0 0.0.0.255
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
  ospf 1
   filter-policy ip-prefix in import
   area 0.0.0.0
    network 192.168.2.0 0.0.0.255
  #
  ip ip-prefix in index 10 permit 172.16.18.0 24
  #
  return
  ```
* DeviceD
  
  ```
  #
  sysname DeviceD
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.3.2 255.255.255.0
  #
  ospf 1
   area 0.0.0.0
    network 192.168.3.0 0.0.0.255
  #
  return
  ```