Example for Configuring Static BFD for RIP
==========================================

Example for Configuring Static BFD for RIP

#### Context

As technologies develop, voice and video services continue to be widely applied. These services are sensitive to packet loss and delay, and prolonged fault detection will cause a large amount of data to be lost. As such, the high reliability requirements of carrier-class networks cannot be met. Static BFD for RIP can be deployed to complete link fault detection within milliseconds, speeding up RIP convergence.


#### Networking Requirements

RIP periodically exchanges Update messages to monitor the status of neighbors. By default, if a local device does not receive any Update messages from its neighbor after six update intervals (180s) elapse, it considers the neighbor down.

In [Figure 1](#EN-US_TASK_0000001130782968__fig_dc_vrp_rip_cfg_005701), DeviceA, DeviceB, DeviceC, and DeviceD run RIP, and service traffic is transmitted along the primary link DeviceA -> DeviceB -> DeviceD. As such, static BFD needs to be enabled on the interfaces connecting DeviceA and DeviceB. The local and remote discriminators need to be configured for the BFD sessions between DeviceA and DeviceB. In this manner, when the primary link fails, BFD can rapidly detect the fault and notify the RIP module, allowing service traffic to be switched to the backup link.

**Figure 1** Network diagram of configuring static BFD for RIP![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001230894971.png)

#### Precautions

To improve security, you are advised to configure RIP-2 packet authentication. For details, see "Improving RIP Network Security." The following example describes how to configure an authentication mode for RIP-2 packets. For details, see "Example for Configuring Basic RIP Functions."


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic RIP functions on each device and establish RIP neighbor relationships.
2. Enable BFD globally.
3. Enable static BFD on interfaces connecting DeviceA and DeviceB.

#### Procedure

1. Assign an IP address to each interface.
   
   
   
   For detailed configurations, see Configuration Scripts.
2. Configure basic RIP functions.
   
   
   
   # Configure DeviceA.
   
   ```
   <DeviceA> system-view
   [~DeviceA] rip 1
   [*DeviceA-rip-1] version 2
   [*DeviceA-rip-1] network 192.168.0.0
   [*DeviceA-rip-1] network 10.0.0.0
   [*DeviceA-rip-1] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   <DeviceB> system-view
   [~DeviceB] rip 1
   [*DeviceB-rip-1] version 2
   [*DeviceB-rip-1] network 192.168.0.0
   [*DeviceB-rip-1] network 1.0.0.0
   [*DeviceB-rip-1] network 172.16.0.0
   [*DeviceB-rip-1] quit
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   <DeviceC> system-view
   [~DeviceC] rip 1
   [*DeviceC-rip-1] version 2
   [*DeviceC-rip-1] network 10.1.0.0
   [*DeviceC-rip-1] network 1.0.0.0
   [*DeviceC-rip-1] quit
   [*DeviceC] commit
   ```
   
   # Configure DeviceD.
   
   ```
   <DeviceD> system-view
   [~DeviceD] rip 1
   [*DeviceD-rip-1] version 2
   [*DeviceD-rip-1] network 172.16.0.0
   [*DeviceD-rip-1] quit
   [*DeviceD] commit
   ```
   
   # After completing the configurations, run the [**display rip neighbor**](cmdqueryname=display+rip+neighbor) command to check whether neighbor relationships among DeviceA, DeviceB, and DeviceC are established. The following example uses the command output on DeviceA.
   
   ```
   [~DeviceA] display rip 1 neighbor
   ---------------------------------------------------------------------
    IP Address      Interface                   Type   Last Heard Time
   ---------------------------------------------------------------------
    10.1.1.2            100GE1/0/2        RIP    0:0:5
    Number of RIP routes  :2
    192.168.2.2         100GE1/0/1        RIP    0:0:5
    Number of RIP routes  :4
   ```
   
   # Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) command. The command output shows that the configured routing devices can import routes from each other. The following example uses the command output on DeviceA.
   
   ```
   [~DeviceA] display ip routing-table
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : _public_
            Destinations : 15       Routes : 16        
   
   Destination/Mask    Proto  Pre  Cost        Flags NextHop         Interface
   
           10.0.0.0/8   RIP    100  3             D  10.1.1.2         100GE1/0/2
           10.1.1.0/24  Direct 0    0             D  10.1.1.1         100GE1/0/2
           10.1.1.1/32  Direct 0    0             D  127.0.0.1        100GE1/0/2
         10.1.1.255/32  Direct 0    0             D  127.0.0.1        100GE1/0/2
        192.168.0.0/8   RIP    100  3             D  192.168.2.2      100GE1/0/1
        192.168.2.0/24  Direct 0    0             D  192.168.2.1      100GE1/0/1
        192.168.2.1/32  Direct 0    0             D  127.0.0.1        100GE1/0/1
      192.168.2.255/32  Direct 0    0             D  127.0.0.1        100GE1/0/1
          127.0.0.0/8   Direct 0    0             D  127.0.0.1        InLoopBack0
          127.0.0.1/32  Direct 0    0             D  127.0.0.1        InLoopBack0
    127.255.255.255/32  Direct 0    0             D  127.0.0.1        InLoopBack0
         172.16.0.0/16  RIP    100  4             D  192.168.2.2      100GE1/0/1
         172.16.1.0/24  RIP    100  1             D  192.168.2.2      100GE1/0/1
            1.1.1.0/24  RIP    100  1             D  10.1.1.2         100GE1/0/2
                        RIP    100  1             D  192.168.2.2      100GE1/0/1
    255.255.255.255/32  Direct 0    0             D  127.0.0.1        InLoopBack0
   ```
   
   As shown in the routing table, the next hop address of the route to 172.16.0.0/16 is 192.168.2.2, the outbound interface is 100GE1/0/1, and traffic is transmitted on the primary link DeviceA -> DeviceB.
3. Configure static BFD.
   
   
   
   # Configure static BFD on DeviceA.
   
   ```
   [~DeviceA] bfd
   [*DeviceA-bfd] quit
   [*DeviceA] bfd 1 bind peer-ip 192.168.2.2 interface 100ge1/0/1 source-ip 192.168.2.1
   [*DeviceA-bfd-session-1] discriminator local 1
   [*DeviceA-bfd-session-1] discriminator remote 2
   [*DeviceA-bfd-session-1] quit
   [*DeviceA] commit
   [~DeviceA] interface 100ge1/0/1
   [*DeviceA-100GE1/0/1] rip bfd static
   [*DeviceA-100GE1/0/1] commit
   ```
   
   # Configure static BFD on DeviceB.
   
   ```
   [~DeviceB] bfd
   [*DeviceB-bfd] quit
   [*DeviceB] bfd 1 bind peer-ip 192.168.2.1 interface 100ge1/0/1 source-ip 192.168.2.2
   [*DeviceB-bfd-session-1] discriminator local 2
   [*DeviceB-bfd-session-1] discriminator remote 1
   [*DeviceB-bfd-session-1] quit
   [*DeviceB] commit
   [~DeviceB] interface 100ge1/0/1
   [*DeviceB-100GE1/0/1] rip bfd static
   [*DeviceB-100GE1/0/1] commit
   ```
   
   # After completing the configurations, run the [**display bfd session**](cmdqueryname=display+bfd+session) **all** command on DeviceA. The command output shows that a static BFD session has been established.
   
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
   --------------------------------------------------------------------------------
   Local  Remote  PeerIpAddr      State     Type        InterfaceName                
   --------------------------------------------------------------------------------
   1      2       192.168.2.2         Up        S_IP_IF     100GE1/0/1
   --------------------------------------------------------------------------------
   ```

#### Verifying the Configuration

# Run the [**shutdown**](cmdqueryname=shutdown) command on 100GE1/0/1 of DeviceB to simulate a fault on the primary link.

![](public_sys-resources/note_3.0-en-us.png) 

Link fault simulation is required for verification and does not need to be performed in actual applications.

```
[~DeviceB] interface 100ge1/0/1
[~DeviceB-100GE1/0/1] shutdown
[*DeviceB-100GE1/0/1] quit
[*DeviceB] commit
```

# Check the BFD session information of DeviceA. The command output shows that a BFD session is not established between DeviceA and DeviceB.

# Check the routing table of DeviceA.

```
[~DeviceA] display ip routing-table
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table : _public_
         Destinations : 8        Routes : 8         

Destination/Mask    Proto  Pre  Cost        Flags NextHop         Interface

        10.1.1.0/24  Direct 0    0             D  10.1.1.1         100GE1/0/2
        10.1.1.1/32  Direct 0    0             D  127.0.0.1        100GE1/0/2
      10.1.1.255/32  Direct 0    0             D  127.0.0.1        100GE1/0/2
      127.0.0.0/8    Direct 0    0             D  127.0.0.1        InLoopBack0
      127.0.0.1/32   Direct 0    0             D  127.0.0.1        InLoopBack0
127.255.255.255/32   Direct 0    0             D  127.0.0.1        InLoopBack0
     172.16.1.0/24   RIP    100  2             D  10.1.1.2         100GE1/0/2
255.255.255.255/32   Direct 0    0             D  127.0.0.1        InLoopBack0
```

As shown in the routing table, the backup link DeviceA -> DeviceC -> DeviceB is used after the primary link fails. The next hop address of the route to 172.16.1.0/24 is 10.1.1.2, and the outbound interface is 100GE1/0/2.


#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  bfd
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.2.1 255.255.255.0
   rip bfd static
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.1.1 255.255.255.0
  #
  rip 1 
   version 2 
   network 192.168.0.0
   network 10.0.0.0
  #
  bfd 1 bind peer-ip 192.168.2.2 interface 100GE1/0/1 source-ip 192.168.2.1
   discriminator local 1  
   discriminator remote 2
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
   ip address 192.168.2.2 255.255.255.0
   rip bfd static
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 1.1.1.1 255.255.255.0
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 172.16.1.1 255.255.255.0
  #
  rip 1 
   version 2 
   network 192.168.0.0
   network 1.0.0.0
   network 172.16.0.0
  #
  bfd 1 bind peer-ip 192.168.2.1 interface 100GE1/0/1 source-ip 192.168.2.2
   discriminator local 2  
   discriminator remote 1
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
   ip address 1.1.1.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.1.2 255.255.255.0
  #
  rip 1 
   version 2 
   network 10.1.0.0
   network 1.0.0.0
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
   ip address 172.16.1.2 255.255.255.0
  #
  rip 1 
   version 2 
   network 172.16.0.0
  #
  return
  ```