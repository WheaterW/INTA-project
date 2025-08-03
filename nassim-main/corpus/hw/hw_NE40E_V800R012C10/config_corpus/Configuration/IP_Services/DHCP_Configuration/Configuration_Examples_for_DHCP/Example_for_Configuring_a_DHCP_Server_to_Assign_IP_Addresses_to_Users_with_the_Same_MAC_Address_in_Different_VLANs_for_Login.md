Example for Configuring a DHCP Server to Assign IP Addresses to Users with the Same MAC Address in Different VLANs for Login
============================================================================================================================

This section provides an example for configuring a DHCP server (with no relay agent configured) to assign IP addresses to Ethernet users with the same MAC addresses in different VLANs.

#### Networking Requirements

IP addresses of different network segments need to be applied for VoIP and IPTV services deployed on different user planes. DHCP clients that support these services use one MAC address to apply for IP addresses of different network segments and differentiate services based on VLAN IDs. This requires the DHCP server to assign IP addresses to users with the same MAC address in different VLANs.

On the network shown in [Figure 1](#EN-US_TASK_0139427840__fig_dc_vrp_dhcp_server_cfg_002001), the DHCP server is configured to dynamically assign IP addresses to DHCP clients. When receiving a user packet in which the VLAN ID is 100, the DHCP server selects the address pool **pool1** to assign an IP address to the user based on the gateway address 10.10.10.1/24. When receiving a user packet in which the VLAN ID is 200, the DHCP server selects the address pool **pool2** to assign an IP address to the user based on the gateway address 10.10.20.1/24.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The DHCP server can only assign IP addresses from different address pools to users with the same MAC address in different VLANs.


**Figure 1** Networking for configuring a DHCP server to assign IP addresses to users with the same MAC address in different VLANs for login![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 in this example represents GE 0/1/1.


  
![](images/fig_dc_vrp_dhcp_server_cfg_002001.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IP address for the interface through which users go online.
2. Configure gateway addresses and address segments for address pools.
3. Configure Layer 3 sub-interfaces.

#### Data Preparation

To complete the configuration, you need the following data:

* IP address of the interface through which users go online
* Gateway addresses
* Numbers and ranges of address segments

#### Procedure

1. Configure an IP address for the user access interface and enable the DHCP server function on the interface.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DHCP Server
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DHCP Server] interface gigabitethernet 0/1/1
   ```
   ```
   [~DHCP Server-GigabitEthernet0/1/1] ip address 10.1.1.1 255.255.255.0
   ```
   ```
   [*DHCP Server-GigabitEthernet0/1/1] dhcp server enable
   ```
   ```
   [*DHCP Server-GigabitEthernet0/1/1] commit
   ```
   ```
   [~DHCP Server-GigabitEthernet0/1/1] quit
   ```
2. Configure gateway addresses and address segments for address pools.
   
   
   
   # Configure an address pool named **pool1**.
   
   ```
   [~DHCP Server] dhcp enable
   ```
   ```
   [*DHCP Server] ip pool pool1 server
   ```
   ```
   [*DHCP Server-ip-pool-pool1] gateway 10.10.10.1 255.255.255.0
   ```
   ```
   [*DHCP Server-ip-pool-pool1] section 0 10.10.10.20 10.10.10.30
   ```
   ```
   [*DHCP Server-ip-pool-pool1] commit
   ```
   ```
   [~DHCP Server-ip-pool-pool1] quit
   ```
   
   # Configure an address pool named **pool2**.
   
   ```
   [~DHCP Server] ip pool pool2 server
   ```
   ```
   [*DHCP Server-ip-pool-pool2] gateway 10.10.20.1 255.255.255.0
   ```
   ```
   [*DHCP Server-ip-pool-pool2] section 0 10.10.20.20 10.10.20.30
   ```
   ```
   [*DHCP Server-ip-pool-pool2] commit
   ```
   ```
   [~DHCP Server-ip-pool-pool2] quit
   ```
3. Configure Layer 3 sub-interfaces (for example, dot1q VLAN tag termination sub-interfaces) and enable the DHCP server function on them.
   
   
   ```
   [~DHCP Server] interface gigabitethernet 0/1/1.1
   ```
   ```
   [*DHCP Server-GigabitEthernet0/1/1.1] ip address 10.10.10.1 255.255.255.0
   ```
   ```
   [*DHCP Server-GigabitEthernet0/1/1.1] encapsulation dot1q-termination
   ```
   ```
   [*DHCP Server-GigabitEthernet0/1/1.1] dot1q termination vid 100
   ```
   ```
   [*DHCP Server-GigabitEthernet0/1/1.1] dhcp server enable
   ```
   ```
   [*DHCP Server-GigabitEthernet0/1/1.1] commit
   ```
   ```
   [~DHCP Server-GigabitEthernet0/1/1.1] quit
   ```
   ```
   [~DHCP Server] interface gigabitethernet 0/1/1.2
   ```
   ```
   [*DHCP Server-GigabitEthernet0/1/1.2] ip address 10.10.20.1 255.255.255.0
   ```
   ```
   [*DHCP Server-GigabitEthernet0/1/1.2] encapsulation dot1q-termination
   ```
   ```
   [*DHCP Server-GigabitEthernet0/1/1.2] dhcp server enable
   ```
   ```
   [*DHCP Server-GigabitEthernet0/1/1.2] dot1q termination vid 200
   ```
   ```
   [*DHCP Server-GigabitEthernet0/1/1.2] commit
   ```
   ```
   [~DHCP Server-GigabitEthernet0/1/1.2] quit
   ```
4. Verify the configuration.
   
   
   
   # Run the [**display ip pool**](cmdqueryname=display+ip+pool) command on the DHCP server to check the IP address pool configuration.
   
   ```
   [~DHCP Server] display ip pool name pool1
   ```
   ```
     Pool-Name      : pool1
     Pool-No        : 2
     Pool-constant-index: -
     Lease          : 3 Days 0 Hours 0 Minutes
     NetBios Type   : N-Node
     Auto recycle   : 30
     Option 3       : Enable
     DNS-Suffix     : -
     Dom-Search-List0: -
     Dom-Search-List1: -
     Dom-Search-List2: -
     Dom-Search-List3: -
     Option-Code 125 : enterprise-code : 2011, string: -
     Position       : Server          Status           : Unlocked        
     RUI-Flag       : -
     Attribute      : Private         
     Gateway        : 10.10.10.1      Mask             : 255.255.255.0   
     Vpn instance   : --              Unnumbered gateway: -               
     Profile-Name   : -               Server-Name     : -               
     Total Idle     : 11              Have Dhcp IP     : 1
     Timeouts       : 0
     Timeout Count  : 0               Sub Option Count : 0               
     Option Count   : 0               Force-reply Count: 0               
     Codes: CFLCT(conflicted)
     ---------------------------------------------------------------------------------------
     ID           start             end total  used  idle CFLCT disable reserved static-bind
     ---------------------------------------------------------------------------------------
      0     10.10.10.20     10.10.10.30    11     0    11     0       0        0           0
     ---------------------------------------------------------------------------------------
   ```
   ```
   [~DHCP Server] display ip pool name pool2
   ```
   ```
     Pool-Name      : pool2
     Pool-No        : 3
     Pool-constant-index: -
     Lease          : 3 Days 0 Hours 0 Minutes
     NetBios Type   : N-Node
     Auto recycle   : 30
     Option 3       : Enable
     DNS-Suffix     : -
     Dom-Search-List0: -
     Dom-Search-List1: -
     Dom-Search-List2: -
     Dom-Search-List3: -
     Option-Code 125 : enterprise-code : 2011, string: -
     Position       : Server          Status           : Unlocked        
     RUI-Flag       : -
     Attribute      : Private         
     Gateway        : 10.10.20.1      Mask             : 255.255.255.0   
     Vpn instance   : --              Unnumbered gateway: -               
     Profile-Name   : -               Server-Name     : -               
     Total Idle     : 11              Have Dhcp IP     : 1
     Timeouts       : 0
     Timeout Count  : 0               Sub Option Count : 0               
     Option Count   : 0               Force-reply Count: 0               
     Codes: CFLCT(conflicted)
     ---------------------------------------------------------------------------------------
     ID           start             end total  used  idle CFLCT disable reserved static-bind
     ---------------------------------------------------------------------------------------
      0     10.10.20.20     10.10.20.30    11     0    11     0       0        0           0
     ---------------------------------------------------------------------------------------
   ```

#### Configuration Files

DHCP server configuration file

```
#
sysname DHCP Server
#
dhcp enable
#
ip pool pool1 server
 gateway 10.10.10.1 255.255.255.0  
 section 0 10.10.10.20 10.10.10.30
#
ip pool pool2 server
 gateway 10.10.20.1 255.255.255.0  
 section 0 10.10.20.20 10.10.20.30
#
interface GigabitEthernet0/1/1
 ip address 10.1.1.1 255.255.255.0
 dhcp server enable
#
interface GigabitEthernet0/1/1.1
 ip address 10.10.10.1 255.255.255.0
 encapsulation dot1q-termination
 dot1q termination vid 100
 dhcp server enable
#
interface GigabitEthernet0/1/1.2
 ip address 10.10.20.1 255.255.255.0
 encapsulation dot1q-termination
 dot1q termination vid 200
 dhcp server enable
#
return
```