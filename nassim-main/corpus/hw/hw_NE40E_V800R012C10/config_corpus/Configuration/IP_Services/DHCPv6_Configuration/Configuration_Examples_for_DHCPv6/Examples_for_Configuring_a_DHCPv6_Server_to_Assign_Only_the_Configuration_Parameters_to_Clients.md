Examples for Configuring a DHCPv6 Server to Assign Only the Configuration Parameters to Clients
===============================================================================================

This section provides an example for configuring a DHCPv6 server to assign configuration parameters to clients when the server and clients are on the same network segment.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001292241672__fig_dc_vrp_dhcpv6_server_cfg_002001), DeviceA functions as the DHCPv6 server and DeviceB is a user access device. The following describes how to configure a DHCPv6 server to dynamically assign configuration parameters to clients on the same network segment.

**Figure 1** Networking diagram for configuring a DHCPv6 server  
![](figure/en-us_image_0000001291921908.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable the DHCPv6 function.
2. Create an IPv6 address pool and configure its attributes.
3. Enable the DHCPv6 server function on the VLANIF interface.

#### Data Preparation

To complete the configuration, you need the following data:

* IPv6 address pool name: pool1
* IPv6 address of the DHCPv6 server's VLANIF interface: 2001:db8:1::1/64
* DNS server address: 2001:db8:2::1/64

#### Procedure

1. Enable the IPv6 function on the interface.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceA
   ```
   ```
   [*HUAWEI] commit
   ```
   
   
   ```
   [~DeviceA] vlan 10
   ```
   ```
   [*DeviceA-vlan10] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet0/1/1
   ```
   ```
   [*DeviceA-gigabitethernet0/1/1] portswitch
   ```
   ```
   [*DeviceA-gigabitethernet0/1/1] port link-type access
   ```
   ```
   [*DeviceA-gigabitethernet0/1/1] port default vlan 10
   ```
   ```
   [*DeviceA-gigabitethernet0/1/1] quit
   ```
   ```
   [*DeviceA] interface vlanif 10
   ```
   ```
   [*DeviceA-Vlanif10] ipv6 enable
   ```
   ```
   [*DeviceA-Vlanif10] ipv6 address 2001:db8:1::1/64
   ```
   ```
   [*DeviceA-Vlanif10] quit
   ```
   ```
   [*DeviceA] commit
   ```
2. Create an IPv6 address pool on DeviceA and configure its attributes.
   
   
   ```
   [~DeviceA] dhcpv6 pool pool1
   ```
   ```
   [*DeviceA-dhcpv6-pool-pool1] dns-server 2001:db8:2::1
   ```
   ```
   [*DeviceA-dhcpv6-pool-pool1] dns-domain-name huawei.com
   ```
   ```
   [*DeviceA-dhcpv6-pool-pool1] commit
   ```
   ```
   [~DeviceA-dhcpv6-pool-pool1] quit
   ```
3. Enable the DHCPv6 server function on the VLANIF interface of DeviceA.
   
   
   ```
   [~DeviceA] interface vlanif 10
   ```
   ```
   [~DeviceA-Vlanif10] dhcpv6 server pool1
   ```
   ```
   [*DeviceA-Vlanif10] commit
   ```
4. Enable IPv6 address assignment in stateless mode and configuration parameter assignment in stateful mode on the VLANIF interface of DeviceA.
   
   
   ```
   [~DeviceA-Vlanif10] undo ipv6 nd ra halt
   ```
   ```
   [*DeviceA-Vlanif10] ipv6 nd autoconfig other-flag
   ```
   ```
   [*DeviceA-Vlanif10] commit
   ```
   ```
   [~DeviceA-Vlanif10] quit
   ```
5. Verify the configuration.
   
   
   
   # Run the [**display dhcpv6 pool**](cmdqueryname=display+dhcpv6+pool) command on DeviceA to check the IPv6 address pool configuration.
   
   ```
   [~DeviceA] display dhcpv6 pool
   ```
   ```
   DHCPv6 pool: pool1
     Vpn name: --
     Information refresh time: 86400                                               
     DNS server address: 2001:DB8:2::1                               
     DNS server domain name: huawei.com                                               
     Conflict-address expire-time: 172800                                           
     renew-time-percent : 50                                                       
     rebind-time-percent : 80             
     Active normal clients: 0       
   ```
   
   
   
   # Run the [**display dhcpv6 server**](cmdqueryname=display+dhcpv6+server) command on DeviceA to check information about messages sent and received by the DHCPv6 server.
   
   ```
   [~DeviceA] display dhcpv6 server statistics
   ```
   ```
    -------------------------------------------------------------
     DHCPv6 packets received                       :   1
            DHCPv6 Solicit                         :   0
            DHCPv6 Request                         :   0
            DHCPv6 Confirm                         :   0
            DHCPv6 Renew                           :   0
            DHCPv6 Rebind                          :   0
            DHCPv6 Release                         :   0
            DHCPv6 Decline                         :   0
            DHCPv6 Information-request             :   1
            DHCPv6 Relay-forward                   :   0
            DHCPv6 UnknownType                     :   0
   
     DHCPv6 packets sent                           :   1
            DHCPv6 Advertise                       :   0
            DHCPv6 Reply                           :   1
            DHCPv6 Relay-reply                     :   0
   
     DHCPv6 packets dropped                        :   0
            Bad packet                             :   0
            Server check failed                    :   0
            Table full                             :   0
            General error                          :   0
            IPSec authentication failed            :   0
            Address manager error                  :   0
    -------------------------------------------------------------
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  #
  vlan 10
  #
  dhcpv6 pool pool1
   dns-server 2001:DB8:2::1
   dns-domain-name huawei.com
  #
  interface Vlanif10
   ipv6 enable
   ipv6 address 2001:DB8:1::1/64
   undo ipv6 nd ra halt
   ipv6 nd autoconfig other-flag
   dhcpv6 server pool1
  #
  interface gigabitethernet0/1/1
   portswitch
   undo shutdown
   port link-type access
   port default vlan 10
  #
  return
  
  ```