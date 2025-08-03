Binding a Management VPN to a Service Interface
===============================================

Binding_a_Management_VPN_to_a_Service_Interface

#### Networking Requirements

An independent VPN is bound to a service interface so that only the service interface can receive management protocol packets.


#### Configuration Roadmap

Create a management VPN and bind it to a selected service interface and the loopback interface, configure another VPN for other service interfaces, and ensure that the two VPNs are isolated.


#### Data Preparation

None


#### Procedure

1. Create a management VPN.
   ```
   [~HUAWEI] ip vpn-instance management
   [*HUAWEI-vpn-instance-management] ipv4-family
   [*HUAWEI-vpn-instance-management] commit
   [~HUAWEI-vpn-instance-management-af-ipv4] quit
   [~HUAWEI-vpn-instance-management] display this
   #
   ip vpn-instance management
    ipv4-family
   #
   return
   
   ```
2. Bind the VPN to the service interface and loopback interface for management.
   ```
   [~HUAWEI] interface gigabitethernet0/3/1
   [~HUAWEI-GigabitEthernet0/3/1] ip binding vpn-instance management
   Info: All IPv4 and IPv6 related configurations on this interface are removed.
   [*HUAWEI-GigabitEthernet0/3/1] commit
   [~HUAWEI-GigabitEthernet0/3/1] quit
   [~HUAWEI] interface LoopBack0
   [~HUAWEI-LoopBack0]ip binding vpn-instance management
   Info: All IPv4 and IPv6 related configurations on this interface are removed.
   [*HUAWEI-LoopBack0]commit
   ```
3. Configure IP addresses for the service interface and loopback interface for management.
   ```
   [~HUAWEI-GigabitEthernet0/3/1] ip address 10.3.1.1 24
   [*HUAWEI-GigabitEthernet0/3/1] commit
   [~HUAWEI-GigabitEthernet0/3/1] display this
   #
   interface GigabitEthernet0/3/1
    undo shutdown
    ip binding vpn-instance management
    ip address 10.3.1.1 255.255.255.0
   #
   [~HUAWEI]interface LoopBack 0
   [~HUAWEI-LoopBack0] ip address 1.1.1.1 32
   [*HUAWEI-LoopBack0] commit
   [~HUAWEI-LoopBack0] display this
   #
   interface LoopBack0
    ip binding vpn-instance management
    ip address 1.1.1.1 255.255.255.255
   #
   return
   
   ```

#### Verifying the Security Hardening Result

* Run the [**display this**](cmdqueryname=display+this) command to check the configuration.
* Run the [**display ip routing-table vpn-instance**](cmdqueryname=display+ip+routing-table+vpn-instance) *vpn-instance-name* command to check route information in the VPN instance IPv4 address family.