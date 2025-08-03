Examples for Configuring a DHCPv6 Server to Assign IPv6 Addresses and Other Configuration Parameters to Clients
===============================================================================================================

This section provides an example for configuring a DHCPv6 server to assign IPv6 addresses and other configuration parameters to clients when the server and clients are on the same network segment.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001292081832__fig_dc_vrp_dhcpv6_server_cfg_002101), DeviceA functions as the DHCPv6 server and DeviceB is a user access device. The following describes how to configure a DHCPv6 server to dynamically assign IPv6 addresses and other configuration parameters to clients on the same network segment.

**Figure 1** Networking diagram for configuring a DHCPv6 server  
![](figure/en-us_image_0000001291921916.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable the DHCPv6 function.
2. Create an IPv6 address pool and configure its attributes.
3. Enable the DHCPv6 server function and RA message advertisement on the VLANIF interface. (The DHCPv6 client must be capable of generating default routes.)

#### Data Preparation

To complete the configuration, you need the following data:

* IPv6 address pool name: pool1
* IPv6 address of the DHCPv6 server's VLANIF interface: 2001:db8:1::1/64
* Network segment of the IPv6 address pool: 2001:db8:1::/64.
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
   [*DeviceA-gigabitethernet0/1/1 portswitch
   ```
   ```
   [*DeviceA-gigabitethernet0/1/1 port link-type access
   ```
   ```
   [*DeviceA-gigabitethernet0/1/1 port default vlan 10
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
   [*DeviceA-dhcpv6-pool-pool1] address prefix 2001:db8:1::/64
   ```
   ```
   [*DeviceA-dhcpv6-pool-pool1] excluded-address 2001:db8:1::1
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
3. Configure the DHCPv6 server function and RA message advertisement on the VLANIF interface of DeviceA.
   
   
   ```
   [~DeviceA] interface vlanif 10
   ```
   ```
   [~DeviceA-Vlanif10] dhcpv6 server pool1
   ```
   ```
   [~DeviceA-Vlanif10] undo ipv6 nd ra halt
   ```
   ```
   [~DeviceA-Vlanif10] ipv6 nd autoconfig managed-address-flag
   ```
   ```
   [~DeviceA-Vlanif10] ipv6 nd autoconfig other-flag
   ```
   ```
   [*DeviceA-Vlanif10] commit
   ```
   ```
   [~DeviceA-Vlanif10] quit
   ```
4. Verify the configuration.
   
   
   
   # Run the [**display dhcpv6 pool**](cmdqueryname=display+dhcpv6+pool) command on DeviceA to check the IPv6 address pool configuration.
   
   ```
   [~DeviceA] display dhcpv6 pool
   ```
   ```
   DHCPv6 pool: pool1 
     Vpn name: --
     Address prefix: 2001:DB8:1::/64                                                     
       Lifetime 172800 seconds, preferred 86400 seconds                      
       0 in use, 0 conflicts                                                       
     Excluded-address 2001:DB8:1::1
     1 excluded addresses
     Information refresh time: 86400                                               
     DNS server address: 2001:DB8:2::1                               
     DNS server domain name: huawei.com                                               
     Conflict-address expire-time: 172800                                           
     renew-time-percent : 50                                                       
     rebind-time-percent : 80             
     Active normal clients: 0       
   ```
   
   
   
   # Run the [**display dhcpv6 server**](cmdqueryname=display+dhcpv6+server) command on DeviceA to check information about the DHCPv6 server.
   
   ```
   [~DeviceA] display dhcpv6 server statistics 
   ```
   ```
    -------------------------------------------------------------
     DHCPv6 packets received                       :   2
            DHCPv6 Solicit                         :   1
            DHCPv6 Request                         :   1
            DHCPv6 Confirm                         :   0
            DHCPv6 Renew                           :   0
            DHCPv6 Rebind                          :   0
            DHCPv6 Release                         :   0
            DHCPv6 Decline                         :   0
            DHCPv6 Information-request             :   0
            DHCPv6 Relay-forward                   :   0
            DHCPv6 UnknownType                     :   0
   
     DHCPv6 packets sent                           :   2
            DHCPv6 Advertise                       :   1
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
   address prefix 2001:DB8:1::/64
   excluded-address 2001:DB8:1::1
   dns-server 2001:DB8:2::1
   dns-domain-name huawei.com
  #
  interface Vlanif10
   ipv6 enable
   ipv6 address 2001:DB8:1::1/64
   dhcpv6 server pool1
   undo ipv6 nd ra halt
   ipv6 nd autoconfig managed-address-flag
   ipv6 nd autoconfig other-flag
  #
  interface gigabitethernet0/1/1
   portswitch
   undo shutdown
   port link-type access
   port default vlan 10
  #
  return
  
  ```