Example for Configuring Dynamic BFD for RIP
===========================================

Example for Configuring Dynamic BFD for RIP

#### Networking Requirements

As technologies develop, voice and video services continue to be widely applied. These services are sensitive to packet loss and delay, and prolonged fault detection will cause a large amount of data to be lost. As such, the high reliability requirements of carrier-class networks cannot be met. Dynamic BFD for RIP can be deployed to complete link fault detection within milliseconds, speeding up RIP convergence.

RIP periodically exchanges Update messages to monitor the status of neighbors. By default, if a local device does not receive any Update messages from its neighbor after six update intervals (180s) elapse, it considers the neighbor down.

In [Figure 1](#EN-US_TASK_0000001130782962__fig12972203819300), the primary link (DeviceA -> DeviceB) and backup link (DeviceA -> DeviceC -> DeviceB) are deployed on the network. In normal cases, service traffic is transmitted along the primary link. However, if the primary link goes faulty, it is expected that the fault is quickly detected and traffic is switched to the backup link. In this case, BFD for RIP can be configured. BFD is used to detect the RIP neighbor relationship between DeviceA and DeviceB, and when the link between DeviceA and DeviceB fails, BFD rapidly detects the failure and reports it to RIP, allowing service traffic to be quickly switched to the backup link. The minimum intervals at which DeviceA and DeviceB send and receive BFD packets are 100 ms, and the local detection multiplier is 10.

**Figure 1** Network diagram of configuring dynamic BFD for RIP![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001176662739.png)

#### Precautions

To improve security, you are advised to configure RIP-2 packet authentication. For details, see "Improving RIP Network Security." The following example describes how to configure an authentication mode for RIP-2 packets. For details, see "Example for Configuring Basic RIP Functions."


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable basic RIP functions on each device and ensure that RIP neighbor relationships are established.
2. Enable BFD globally.
3. Configure BFD on interfaces at both ends of the link between DeviceA and DeviceB.

#### Procedure

1. Assign an IP address to each interface. For detailed configurations, see Configuration Scripts.
2. Configure basic RIP functions.
   
   
   
   # Configure DeviceA.
   
   ```
   <DeviceA> system-view
   [~DeviceA] rip 1
   [*DeviceA-rip-1] version 2
   [*DeviceA-rip-1] network 192.168.0.0
   [*DeviceA-rip-1] network 10.1.0.0
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
   IP Address         Interface Type          Type       Last Heard Time 
   ---------------------------------------------------------------------
    10.1.1.2             100GE1/0/2               RIP        0:0:5
    Number of RIP routes  :2
    192.168.2.2          100GE1/0/1               RIP        0:0:5
    Number of RIP routes  :4
   ```
   
   # Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) command. The command output shows that the configured devices can import routes from each other. The following example uses the command output on DeviceA.
   
   ```
   [~DeviceA] display ip routing-table
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : _public_
            Destinations : 15       Routes : 16        
   
   Destination/Mask    Proto  Pre  Cost        Flags NextHop         Interface
   
           10.1.0.0/8   RIP    100  3             D  10.1.1.2         100GE1/0/2
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
            1.1.1.0/24  RIP    100  1             D  10.1.1.2         100GE0/2/0
                        RIP    100  1             D  192.168.2.2      100GE1/0/1
    255.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
   ```
   
   As shown in the routing table, the next hop address of the route to 172.16.1.0/24 is 192.168.2.2, the outbound interface is 100GE1/0/1, and traffic is transmitted on the primary link DeviceA -> DeviceB.
3. Configure BFD for RIP.
   
   
   
   # Configure BFD on all interfaces of DeviceA.
   
   ```
   [~DeviceA] bfd
   [*DeviceA-bfd] quit
   [*DeviceA] rip 1
   [*DeviceA-rip-1] bfd all-interfaces enable
   [*DeviceA-rip-1] bfd all-interfaces min-rx-interval 100 min-tx-interval 100 detect-multiplier 10
   [*DeviceA-rip-1] quit
   [*DeviceA] commit
   ```
   
   The configuration on DeviceB is similar to the configuration on DeviceA. For detailed configurations, see Configuration Scripts.
   
   # After completing the configuration, run the [**display rip bfd session**](cmdqueryname=display+rip+bfd+session) command. The command output shows that a BFD session has been established between DeviceA and DeviceB, and **BFDState** is displayed as **Up**. The following example uses the command output on DeviceA.
   
   ```
   [~DeviceA] display rip 1 bfd session all
   LocalIp      :192.168.2.1         RemoteIp   :192.168.2.2         BFDState :Up      
    TX           :100             RX         :100             Multiplier:10       
    BFD Local Dis:8192            Interface  :100GE1/0/1                    
    DiagnosticInfo: No diagnostic information                               
    LocalIp       :10.1.1.1         RemoteIp  :10.1.1.2         BFDState :Up
    TX            :0               RX        :0               Multiplier:0
    BFD Local Dis :8200            Interface :100GE1/0/2
    Diagnostic Info:No diagnostic information                     
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

```
[~DeviceA] display rip 1 bfd session all
 LocalIp       :10.1.1.1         RemoteIp  :10.1.1.2         BFDState  :Down
 TX            :0               RX        :0               Multiplier:0
 BFD Local Dis :8200            Interface :100GE1/0/2
 Diagnostic Info:No diagnostic information   
```

# Check the routing table of DeviceA.

```
[~DeviceA] display ip routing-table
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table : _public_
         Destinations : 8        Routes : 8         

Destination/Mask    Proto  Pre  Cost        Flags NextHop         Interface

        10.1.1.0/24  Direct 0    0             D  10.1.1.1        100GE1/0/2
        10.1.1.1/32  Direct 0    0             D  127.0.0.1       100GE1/0/2
      10.1.1.255/32  Direct 0    0             D  127.0.0.1       100GE1/0/2
       127.0.0.0/8   Direct 0    0             D  127.0.0.1       InLoopBack0
       127.0.0.1/32  Direct 0    0             D  127.0.0.1       InLoopBack0
 127.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
      172.16.1.0/24  RIP    100  2             D  10.1.1.2        100GE1/0/2
 255.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
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
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.1.1 255.255.255.0
  #
  rip 1 
   version 2 
   network 192.168.0.0
   network 10.1.0.0
   bfd all-interfaces enable 
   bfd all-interfaces min-tx-interval 100 min-rx-interval 100 detect-multiplier 10 
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
   bfd all-interfaces enable 
   bfd all-interfaces min-tx-interval 100 min-rx-interval 100 detect-multiplier 10 
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
   ip address 10.1.1.2 255.255.255.0
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