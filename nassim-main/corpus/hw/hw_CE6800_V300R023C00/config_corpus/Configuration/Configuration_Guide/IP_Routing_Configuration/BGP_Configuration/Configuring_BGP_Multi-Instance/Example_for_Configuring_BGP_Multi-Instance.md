Example for Configuring BGP Multi-Instance
==========================================

Example for Configuring BGP Multi-Instance

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001130783926__fig568519487491), establish a public network BGP peer relationship in the BGP basic instance between DeviceA and DeviceB, and establish a BGP peer relationship in DeviceB's BGP multi-instance and DeviceC's BGP basic instance. In this manner, routes are separately managed and maintained on DeviceB.

**Figure 1** BGP multi-instance networking![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE1/0/1 and 100GE1/0/2, respectively.


  
![](figure/en-us_image_0000001176663757.png)

#### Precautions

During the configuration, note the following:

* To improve security, you are advised to deploy BGP security measures. For details, see "Configuring BGP Authentication." Keychain authentication is used as an example. For details, see Example for Configuring Keychain Authentication for BGP.

#### Procedure

1. Assign an IP address to each interface. For detailed configurations, see [Configuration Scripts](#EN-US_TASK_0000001130783926__postreq1662236201619).
2. Establish a public network BGP peer relationship between DeviceA and DeviceB.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] bgp 100
   [*DeviceA-bgp] peer 10.1.1.2 as-number 100
   [*DeviceA-bgp] ipv4-family unicast
   [*DeviceA-bgp-af-ipv4] peer 10.1.1.2 enable
   [*DeviceA-bgp-af-ipv4] quit
   [*DeviceA-bgp] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] bgp 100
   [*DeviceB-bgp] peer 10.1.1.1 as-number 100
   [*DeviceB-bgp] ipv4-family unicast
   [*DeviceB-bgp-af-ipv4] peer 10.1.1.1 enable
   [*DeviceB-bgp-af-ipv4] quit
   [*DeviceB-bgp] quit
   [*DeviceB] commit
   ```
3. Establish a VPN BGP peer relationship between DeviceB and DeviceC.
   
   
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] ip vpn-instance aa 
   [*DeviceB-vpn-instance-aa] ipv4-family
   [*DeviceB-vpn-instance-aa-af-ipv4] route-distinguisher 100:1    
   [*DeviceB-vpn-instance-aa-af-ipv4] vpn-target 1:1 export-extcommunity 
   [*DeviceB-vpn-instance-aa-af-ipv4] vpn-target 1:1 import-extcommunity 
   [*DeviceB-vpn-instance-aa-af-ipv4] quit
   [*DeviceB-vpn-instance-aa] quit
   [*DeviceB] bgp 200 instance aa
   [*DeviceB-bgp-instance-aa] ipv4-family vpn-instance aa
   [*DeviceB-bgp-instance-aa-aa] peer 10.1.2.2 as-number 200
   [*DeviceB-bgp-instance-aa-aa] quit
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] bgp 200
   [*DeviceC-bgp] peer 10.1.2.1 as-number 200
   [*DeviceC-bgp] quit
   [*DeviceC] commit
   ```

#### Verifying the Configuration

# Run the **display bgp peer** command on DeviceB to check the status of the public network BGP connection.

```
[~DeviceB] display bgp peer

 BGP local router ID : 10.1.1.2
 Local AS number : 100 
 Total number of peers : 4                 Peers in established state : 3 

  Peer                             V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv                              
  10.1.1.1                         4         100       25       25     0 00:19:48 Established        0  
```

The command output shows that the BGP connection is established between DeviceB and DeviceA (the **State** field is displayed as **Established**).

# Run the **display bgp instance aa vpnv4 all peer** command on DeviceB to check the status of the BGP multi-instance connection.

```
[~DeviceB] display bgp instance aa vpnv4 all peer

 BGP local router ID : 10.1.1.2
 Local AS number : 200       
 Total number of peers : 1                 Peers in established state : 1


  Peer of IPv4-family for vpn instance :

  VPN-Instance aa, Router ID 10.1.1.2:                                                                                              
  Peer                             V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
  10.1.2.2                         4         200        4        4     0 00:01:07 Established        0  
```

The command output shows that the BGP multi-instance connection between DeviceB and DeviceC is in the Established state.


#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA 
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.1 255.255.255.0
  #
  bgp 100
   peer 10.1.1.2 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    peer 10.1.1.2 enable
  #
  return
  ```
* DeviceB
  ```
  #
  sysname DeviceB
  #
  ip vpn-instance aa
   ipv4-family
    route-distinguisher 100:1
    vpn-target 1:1 export-extcommunity 
    vpn-target 1:1 import-extcommunity
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip binding vpn-instance aa 
   ip address 10.1.2.1 255.255.255.0
  #
  bgp 100
   peer 10.1.1.1 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    peer 10.1.1.1 enable
  bgp 200 instance aa
   ipv4-family vpn-instance aa        
    peer 10.1.2.2 as-number 200 
  #
  return
  ```
* DeviceC
  ```
  #
  sysname DeviceC
  #
  interface 100GE1/0/2
   undo portswitch
   ip binding vpn-instance aa 
   ip address 10.1.2.2 255.255.255.0
  #
  bgp 200
   peer 10.1.2.1 as-number 200 
   #
   ipv4-family unicast
     undo synchronization
     peer 10.1.2.1 enable
  #
  return
  ```