Example for Configuring a Dynamic Routing Protocol (IPv4 over IPv4) for GRE
===========================================================================

This section provides an example for configuring a dynamic routing protocol for GRE. The configuration allows traffic between users to be transmitted over GRE tunnels. A dynamic routing protocol is required between a device and its connected clients.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172369099__fig_dc_vrp_gre_cfg_203201), DeviceA, DeviceB, and DeviceC belong to the VPN backbone network, and OSPF runs among them.

DeviceA and DeviceC are directly connected through a GRE tunnel for communication between PC1 and PC2. OSPF is enabled on the tunnel interface. OSPF process 1 is used for the VPN backbone network, and OSPF process 2 is used for user access.

PC1 and PC2 respectively use DeviceA and DeviceC as their default gateways.

**Figure 1** Configuring a dynamic routing protocol (IPv4 over IPv4) for GRE![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 through 3 represent GE0/1/0, GE0/2/0, and Tunnel1, respectively.


  
![](images/fig_dc_vrp_gre_cfg_203201.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IGP on the Routers of the backbone network for them to communicate. OSPF process 1 is used here.
2. Establish a GRE tunnel between the Routers connected to PCs so that data between any two PCs is transmitted through the GRE tunnel.
3. Configure a dynamic routing protocol on the network segment through which PCs access the backbone network. OSPF process 2 is used here.

#### Data Preparation

To complete the configuration, you need the following data:

* Source and destination addresses of the GRE tunnel
* IP addresses of the tunnel interfaces on both ends

#### Procedure

1. Configure interface IP addresses.
   
   
   
   For configuration details, see the configuration files.
2. Configure IGP on the VPN backbone network.
   
   
   
   The specific configuration procedures are the same as those in [Example for Configuring a Static Route for GRE](dc_vrp_gre_cfg_2031.html).
3. Configure tunnel interfaces.
   
   
   
   The specific configuration procedures are the same as those in [Example for Configuring a Static Route for GRE](dc_vrp_gre_cfg_2031.html).
4. Configure OSPF on the tunnel interfaces.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] ospf 2
   ```
   ```
   [*DeviceA-ospf-2] area 0
   ```
   ```
   [*DeviceA-ospf-2-area-0.0.0.0] network 172.18.1.0 0.0.0.255
   ```
   ```
   [*DeviceA-ospf-2-area-0.0.0.0] network 10.1.1.0 0.0.0.255
   ```
   ```
   [*DeviceA-ospf-2-area-0.0.0.0] quit
   ```
   ```
   [*DeviceA-ospf-2] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] ospf 2
   ```
   ```
   [*DeviceC-ospf-2] area 0
   ```
   ```
   [*DeviceC-ospf-2-area-0.0.0.0] network 172.18.1.0 0.0.0.255
   ```
   ```
   [*DeviceC-ospf-2-area-0.0.0.0] network 10.2.1.0 0.0.0.255
   ```
   ```
   [*DeviceC-ospf-2-area-0.0.0.0] quit
   ```
   ```
   [*DeviceC-ospf-2] quit
   ```
   ```
   [*DeviceC] commit
   ```
5. Verify the configuration.
   
   
   
   # After the configuration is complete, run the **display ip routing-table** command on DeviceA and DeviceC. The command output shows the OSPF route from the tunnel interface to the user-side network segment of the peer. In addition, the next hop of the route to the destination physical interface (172.17.1.0/24) of the tunnel is not a tunnel interface.
   
   # The following example uses the command output on DeviceA.
   
   ```
   [~DeviceA] display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : _public_
            Destinations : 15       Routes : 15
   
   Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface
   
           1.1.1.1/32  Direct  0    0             D  127.0.0.1       InLoopBack0
           2.2.2.2/24  OSPF    10   2             D  172.16.1.2      Vlanif10
          10.1.1.0/24  Direct  0    0             D  10.1.1.2        Vlanif20
          10.1.1.2/32  Direct  0    0             D  127.0.0.1       Vlanif20
        10.1.1.255/32  Direct  0    0             D  127.0.0.1       Vlanif20
          10.2.1.0/24  OSPF    10  2              D  172.18.1.2      Tunnel1
        172.16.1.0/24  Direct  0    0             D  172.16.1.1      Vlanif10
        172.16.1.1/32  Direct  0    0             D  127.0.0.1       Vlanif10
      172.16.1.255/32  Direct  0    0             D  127.0.0.1       Vlanif10
        172.17.1.0/24  OSPF    10  2              D  172.16.1.2      Vlanif10
        172.18.1.0/24  Direct  0    0             D  172.18.1.1      Tunnel1
        172.18.1.1/32  Direct  0    0             D  127.0.0.1       Tunnel1
      172.18.1.255/32  Direct  0    0             D  127.0.0.1       Tunnel1
         127.0.0.0/8   Direct  0    0             D  127.0.0.1       InLoopBack0
         127.0.0.1/32  Direct  0    0             D  127.0.0.1       InLoopBack0
   127.255.255.255/32  Direct  0    0             D  127.0.0.1       InLoopBack0
   255.255.255.255/32  Direct  0    0             D  127.0.0.1       InLoopBack0
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  #
  vlan batch 10 20
  #
  interface Vlanif10
   ip address 172.16.1.1 255.255.255.0
  #
  interface Vlanif20
   ip address 10.1.1.2 255.255.255.0
  #
  interface GigabitEthernet0/1/0
   portswitch
   undo shutdown
   port default vlan 10
  #
  interface GigabitEthernet0/2/0
   portswitch
   undo shutdown
   port default vlan 20
  #
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
   binding tunnel gre
  #
  interface Tunnel1
   ip address 172.18.1.1 255.255.255.0
   tunnel-protocol gre
   source 1.1.1.1
   destination 2.2.2.2
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 172.16.1.0 0.0.0.255
  #
  ospf 2
   area 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 172.18.1.0 0.0.0.255
  #
  return
  ```
* DeviceB configuration file
  
  ```
  #
  sysname DeviceB
  #
  vlan batch 10 20
  #
  interface Vlanif10
   ip address 172.16.1.2 255.255.255.0
  #
  interface Vlanif20
   ip address 172.17.1.1 255.255.255.0
  #
  interface GigabitEthernet0/1/0
   portswitch
   undo shutdown
   port default vlan 10
  #
  interface GigabitEthernet0/2/0
   portswitch
   undo shutdown
   port default vlan 20
  #
  ospf 1
   area 0.0.0.0
    network 172.16.1.0 0.0.0.255
    network 172.17.1.0 0.0.0.255
  #
  return
  ```
* DeviceC configuration file
  
  ```
  #
  sysname DeviceC
  #
  vlan batch 10 20
  #
  interface Vlanif10
   ip address 10.2.1.2 255.255.255.0
  #
  interface Vlanif20
   ip address 172.17.1.2 255.255.255.0
  #
  interface GigabitEthernet0/1/0
   portswitch
   undo shutdown
   port default vlan 20
  #
  interface GigabitEthernet0/2/0
   portswitch
   undo shutdown
   port default vlan 10
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
   binding tunnel gre
  #
  interface Tunnel1
   ip address 172.18.1.2 255.255.255.0
   tunnel-protocol gre
   source 2.2.2.2
   destination 1.1.1.1
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 172.17.1.0 0.0.0.255
  #
  ospf 2
   area 0.0.0.0
    network 10.2.1.0 0.0.0.255
    network 172.18.1.0 0.0.0.255
  #
  return
  ```