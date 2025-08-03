Binding a VPN to Management Interfaces
======================================

Binding_a_VPN_to_Management_Interfaces

#### Networking Requirements

[Figure 1](#EN-US_CONCEPT_0000001883896528__en-us_concept_0000001134623504_fig_dc_vrp_sec_hardening_202501) shows the networking of three-plane isolation.

**Figure 1** Three-Plane Isolation  
![](../ne/vrp/figure/en-us_image_0000001180503167.png)

#### Configuration Roadmap

Bind the specific management VPN to the management network interface and the loopback interface for management, configure another VPN for the service interfaces, and ensure that the two VPNs are isolated.


#### Data Preparation

None


#### Configuration Procedure

1. Create a management VPN.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] ip vpn-instance management
   [*HUAWEI-vpn-instance-management] ipv4-family
   [*HUAWEI-vpn-instance-management-af-ipv4] commit
   [~HUAWEI-vpn-instance-management-af-ipv4] quit
   [~HUAWEI-vpn-instance-management] display this 
   #                                                                               
   ip vpn-instance management                                                      
    ipv4-family                                                                    
   #                                                                               
   return  
   [~HUAWEI-vpn-instance-management] quit
   ```
2. Bind the VPN to the management interface and loopback interface for management.
   ```
   [~HUAWEI] interface GigabitEthernet0/0/0
   [~HUAWEI-GigabitEthernet0/0/0] ip binding vpn-instance management
   [*HUAWEI-GigabitEthernet0/0/0] commit
   [~HUAWEI-GigabitEthernet0/0/0] quit 
   ```
   ```
   [~HUAWEI] interface LoopBack0
   [~HUAWEI-LoopBack0] ip binding vpn-instance management
   [*HUAWEI-LoopBack0] commit
   [~HUAWEI-LoopBack0] quit
   ```
3. Configure IP addresses for the management interface and loopback interface for management.
   ```
   [~HUAWEI] interface GigabitEthernet0/0/0
   ```
   ```
   [~HUAWEI-GigabitEthernet0/0/0] ip address 10.10.11.100 24
   ```
   ```
   [*HUAWEI-GigabitEthernet0/0/0] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/0/0] display this
   ```
   ```
   #
   interface GigabitEthernet0/0/0
    undo shutdown
    ip binding vpn-instance management
    ip address 10.10.11.100 255.255.255.0
   #
   ```
   ```
   [~HUAWEI] interface LoopBack0
   [~HUAWEI-LoopBack0] ip address 1.1.1.1 32
   [*HUAWEI-LoopBack0] commit
   ```
   ```
   [~HUAWEI-LoopBack0] display this
   #
   interface LoopBack0
    ip binding vpn-instance management
    ip address 1.1.1.1 255.255.255.255
   #
   return
   [~HUAWEI-LoopBack0] quit
   ```
4. View the routing table to check whether routes on the management and control planes are isolated.
   ```
   [~HUAWEI] display ip routing-table 
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table: Public
            Destinations : 2        Routes : 2
   
   Destination/Mask    Proto   Pre  Cost      Flags NextHop         Interface
   
         127.0.0.0/8   Direct  0    0           D   127.0.0.1       InLoopBack0
         127.0.0.1/32  Direct  0    0           D   127.0.0.1       InLoopBack0
   
   [~HUAWEI] display ip routing-table vpn-instance management 
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table: management
            Destinations : 3        Routes : 3
   
   Destination/Mask    Proto   Pre  Cost      Flags NextHop         Interface
   
           1.1.1.1/32  Direct  0    0           D   127.0.0.1       LoopBack0
        10.10.11.0/24  Direct  0    0           D   10.10.11.100    GigabitEthernet0/0/0
      10.10.11.100/32  Direct  0    0           D   127.0.0.1       GigabitEthernet0/0/0
   
   
   ```
5. Perform the ping operation to check whether routes on the management and control planes are isolated.
   ```
   <HUAWEI> ping 10.10.11.100
   PING 10.10.11.100: 56  data bytes, press CTRL_C to break
       Request time out
       Request time out
       Request time out
       Request time out
       Request time out
   
     --- 10.10.11.100 ping statistics ---
       5 packet(s) transmitted
       0 packet(s) received
       100.00% packet loss
   
   ```
   ```
   <HUAWEI> ping -vpn-instance management 10.10.11.100
   PING 10.10.11.100: 56  data bytes, press CTRL_C to break
       Reply from 10.10.11.100: bytes=56 Sequence=1 ttl=255 time=1 ms
       Reply from 10.10.11.100: bytes=56 Sequence=2 ttl=255 time=30 ms
       Reply from 10.10.11.100: bytes=56 Sequence=3 ttl=255 time=10 ms
       Reply from 10.10.11.100: bytes=56 Sequence=4 ttl=255 time=30 ms
       Reply from 10.10.11.100: bytes=56 Sequence=5 ttl=255 time=30 ms
   
     --- 10.10.11.100 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 1/20/30 ms
   ```

#### Verifying the Security Hardening Result

* Run the [**display this**](cmdqueryname=display+this) command to check the configuration.
* Run the [**display ip routing-table vpn-instance**](cmdqueryname=display+ip+routing-table+vpn-instance) *vpn-instance-name* command to check the route information of the management plane.
* Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) command to check the route information of the control plane.