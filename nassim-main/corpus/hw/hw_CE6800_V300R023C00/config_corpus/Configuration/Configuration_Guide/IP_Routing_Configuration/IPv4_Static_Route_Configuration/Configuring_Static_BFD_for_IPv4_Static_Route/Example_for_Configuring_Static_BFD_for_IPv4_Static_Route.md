Example for Configuring Static BFD for IPv4 Static Route
========================================================

Example for Configuring Static BFD for IPv4 Static Route

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001176742409__fig1279133692210), DeviceA is connected to DeviceB through a switch. You can configure the default static route on DeviceA so that DeviceA can communicate with other devices. In addition, a BFD session needs to be configured between DeviceA and DeviceB to rapidly detect link faults.

**Figure 1** Network diagram of static BFD for IPv4 static route![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE1/0/1 and 100GE1/0/2, respectively.


  
![](figure/en-us_image_0000001130782792.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IPv4 addresses for interfaces on each device.
2. Configure a BFD session on DeviceA and DeviceB to monitor the link between the two devices.
3. Configure a default static route from DeviceA to the external network and bind the default static route to the BFD session.

#### Procedure

1. Configure IPv4 addresses for interfaces on each device.
   
   
   
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
   
   The configuration of DeviceB is similar to the configuration of DeviceA. For detailed configurations, see [Configuration Scripts](#EN-US_TASK_0000001176742409__postreq24192593172748).
2. Configure a BFD session on DeviceA and DeviceB to monitor the link between the two devices.
   
   
   
   # On DeviceA, configure a BFD session to DeviceB.
   
   ```
   [~DeviceA] bfd
   [*DeviceA-bfd] quit
   [*DeviceA] bfd aa bind peer-ip 10.1.1.2
   [*DeviceA-bfd-session-aa] discriminator local 10
   [*DeviceA-bfd-session-aa] discriminator remote 20
   [*LSRDeviceA-bfd-session-aa] quit
   [*DeviceA] commit
   ```
   
   # On DeviceB, configure a BFD session to DeviceA.
   
   ```
   [~DeviceB] bfd
   [*DeviceB-bfd] quit
   [*DeviceB] bfd bb bind peer-ip 10.1.1.1
   [*DeviceB-bfd-session-bb] discriminator local 20
   [*DeviceB-bfd-session-bb] discriminator remote 10
   [*DeviceB-bfd-session-bb] quit
   [*DeviceB] commit
   ```
3. Configure a default static route from DeviceA to the external network and bind the default static route to the BFD session.
   
   
   
   # On DeviceA, configure a default static route to the external network and bind it to the BFD session named **aa**.
   
   ```
   [~DeviceA] ip route-static 0.0.0.0 0 10.1.1.2 track bfd-session aa
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Run the [**display bfd session all**](cmdqueryname=display+bfd+session+all) command on DeviceA to check the status of the static BFD session.

```
[~DeviceA] display bfd session all 
S: Static session
D: Dynamic session
IP: IP session
IF: Single-hop session
PEER: Multi-hop session
AUTO: Automatically negotiated session
VXLAN: VXLAN session
(w): State in WTR  
(*): State is invalid 
Total UP/DOWN Session Number : 1/0
------------------------------------------------------------------------------ 
Local  Remote PeerIpAddr       State     Type        InterfaceName 
------------------------------------------------------------------------------
 10    20    10.1.1.2        Up        S_IP_IF       100GE1/0/1 
 ------------------------------------------------------------------------------   
```

The command output shows that the **State** field value is **Up**, indicating that the BFD session has been established.

# Check the IP routing table of DeviceA.

```
[~DeviceA] display ip routing-table
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table: Public
         Destinations : 5        Routes : 5
Destination/Mask    Proto  Pre  Cost     Flags  NextHop         Interface

        0.0.0.0/0  Static 60   0         RD  10.1.1.2      100GE1/0/1
        10.1.1.0/24  Direct  0    0           D   10.1.1.1        100GE1/0/1
        10.1.1.1/32  Direct  0    0           D   127.0.0.1       100GE1/0/1
      10.1.1.255/32  Direct  0    0           D   127.0.0.1       100GE1/0/1
 255.255.255.255/32  Direct  0    0           D   127.0.0.1       InLoopBack0
```

The preceding command output shows that the default IPv4 static route exists in the routing table.

# Run the **shutdown** command on 100GE 1/0/1 of DeviceA to simulate a link fault.

```
[~DeviceA] interface 100ge 1/0/1
[*DeviceA-100GE1/0/1] shutdown
[*DeviceA-100GE1/0/1] commit
```

# Run the **display bfd session** **all** command on DeviceA to check the status of the static BFD session.

```
[~DeviceA] display bfd session all 
S: Static session
D: Dynamic session
IP: IP session
IF: Single-hop session
PEER: Multi-hop session
AUTO: Automatically negotiated session
VXLAN: VXLAN session
(w): State in WTR  
(*): State is invalid 
Total UP/DOWN Session Number : 0/1
------------------------------------------------------------------------------ 
Local  Remote PeerIpAddr       State     Type        InterfaceName 
------------------------------------------------------------------------------
 10     20    10.1.1.2        Down      S_IP_IF       100GE1/0/1 
 ------------------------------------------------------------------------------ 
```

The command output shows that **Down** is displayed in the **State** field, indicating that the BFD session is down.

# Check the routing table of DeviceA.

```
[~DeviceA] display ip routing-table
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table: Public
         Destinations : 4        Routes : 4
Destination/Mask    Proto  Pre  Cost      Flags  NextHop         Interface
        10.1.1.0/24  Direct 0    0           D  10.1.1.1         100GE1/0/1
        10.1.1.1/32  Direct 0    0           D  127.0.0.1        100GE1/0/1
      10.1.1.255/32  Direct 0    0           D  127.0.0.1        100GE1/0/1
255.255.255.255/32   Direct 0    0           D  127.0.0.1        InLoopBack0
```

The command output shows that the default IPv4 static route to 0.0.0.0/0 does not exist in the routing table of DeviceA.


#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  bfd
  #
  bfd aa bind peer-ip 10.1.1.2
   discriminator local 10
   discriminator remote 20
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.1 255.255.255.0
  #
  ip route-static 0.0.0.0 0.0.0.0 10.1.1.2 track bfd-session aa
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  bfd
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.2.1 255.255.255.0
  #
  bfd bb bind peer-ip 10.1.1.1
   discriminator local 20
   discriminator remote 10
  #
  return
  ```