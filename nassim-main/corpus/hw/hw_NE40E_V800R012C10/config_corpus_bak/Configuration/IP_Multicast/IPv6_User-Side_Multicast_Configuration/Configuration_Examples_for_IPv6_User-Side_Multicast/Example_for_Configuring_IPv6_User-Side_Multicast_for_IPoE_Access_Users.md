Example for Configuring IPv6 User-Side Multicast for IPoE Access Users
======================================================================

This section provides an example for configuring IPv6 user-side multicast service for Internet Protocol over Ethernet (IPoE) access users.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172367725__fig_dc_vrp_bras-multicast_cfg_000901), users (PC) are IPoE access users, and they want to join multicast programs. Configure IPv6 user-side multicast to implement user-based on-demand multicast data forwarding.

**Figure 1** Configuring IPv6 user-side multicast for IPoE access users![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 and interface 2 in this example stand for GE 0/1/0 and GE 0/1/1.1, respectively.


  
![](images/fig_dc_vrp_ipv6bras-multicast_cfg_000801.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure Authentication, Authorization and Accounting (AAA) schemes.
2. Configure a local IPv6 prefix pool.
3. Configure a local IPv6 address pool and bind the local IPv6 prefix pool to the local address pool.
4. Configure an AAA domain and bind it to the IPv6 address pool.
5. Configure the IPoE access mode:
   
   1. Configure an authentication scheme.
   2. Bind a sub-interface to a VLAN.
   3. Configure a BAS interface and specify a user access type for the interface.
6. Configure a multicast replication mode. Multicast replication by interface + VLAN is used as an example.
7. Configure basic multicast functions:
   
   1. Enable IPv6 multicast routing.
   2. Enable IPv6 Protocol Independent Multicast-Sparse Mode (PIM-SM) on all BRAS interfaces.
   3. Enable MLD on the BRAS interface connected to users.

#### Data Preparation

* Local prefix pool, address prefix, and prefix length parameters
* Local address pool parameters
* Authentication and accounting schemes (user authentication on the BRAS through RADIUS)
* User domain
* BAS interface parameters

#### Procedure

1. Configure AAA schemes.
   
   
   
   # Configure an authentication scheme.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [HUAWEI] sysname BRAS
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~BRAS] aaa
   ```
   ```
   [*BRAS-aaa] authentication-scheme radius
   ```
   ```
   [*BRAS-aaa-authen-radius] authentication-mode radius
   ```
   ```
   [*BRAS-aaa-authen-radius] quit
   ```
   ```
   [*BRAS-aaa] commit
   ```
   
   # Configure an accounting scheme.
   
   ```
   [~BRAS-aaa] accounting-scheme none
   ```
   ```
   [*BRAS-aaa-accounting-none] accounting-mode none
   ```
   ```
   [*BRAS-aaa-accounting-none] quit
   ```
   ```
   [*BRAS-aaa] quit
   ```
   ```
   [*BRAS] commit
   ```
2. Configure a local IPv6 prefix pool.
   
   
   ```
   [~BRAS] ipv6 prefix ipv6 local
   ```
   ```
   [*BRAS-ipv6-prefix-ipv6] prefix 2001:db8:1::/64
   ```
   ```
   [*BRAS-ipv6-prefix-ipv6] quit
   ```
   ```
   [*BRAS] commit
   ```
3. Configure a local IPv6 address pool and bind the local IPv6 prefix pool to the local address pool.
   
   
   ```
   [~BRAS] ipv6 pool ipv6 bas local
   ```
   ```
   [*BRAS-ipv6-pool-ipv6] prefix ipv6
   ```
   ```
   [*BRAS-ipv6-pool-ipv6] quit
   ```
   ```
   [*BRAS] commit
   ```
4. Configure a RADIUS server group.
   
   
   
   # Configure a RADIUS server group named **shiva**.
   
   ```
   [~BRAS] radius-server group shiva
   ```
   
   # Configure an IP address and port numbers for the primary RADIUS authentication and accounting server.
   
   ```
   [*BRAS-radius-shiva] radius-server authentication 10.7.66.66 1812
   ```
   ```
   [*BRAS-radius-shiva] radius-server accounting 10.7.66.66 1813
   ```
   
   # Configure a shared key and the number of retransmissions for the RADIUS server.
   
   ```
   [*BRAS-radius-shiva] radius-server shared-key-cipher YsHsjx_202206
   ```
   ```
   [*BRAS-radius-shiva] radius-server retransmit 2
   ```
   ```
   [*BRAS-radius-shiva] commit
   ```
   ```
   [~BRAS-radius-shiva] quit
   ```
5. Configure a domain and bind the local address pool to the domain.
   
   
   ```
   [~BRAS] aaa
   ```
   ```
   [*BRAS-aaa] domain wdomain
   ```
   ```
   [*BRAS-aaa-domain-wdomain] authentication-scheme radius
   ```
   ```
   [*BRAS-aaa-domain-wdomain] accounting-scheme none
   ```
   ```
   [*BRAS-aaa-domain-wdomain] radius-server group shiva
   ```
   ```
   [*BRAS-aaa-domain-wdomain] ipv6-pool ipv6
   ```
   ```
   [*BRAS-aaa-domain-wdomain] quit
   ```
   ```
   [*BRAS-aaa] quit
   ```
   ```
   [*BRAS] commit
   ```
6. Bind a sub-interface to a VLAN.
   
   
   ```
   [~BRAS] interface gigabitethernet 0/1/1.1
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1] user-vlan 133
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1-vlan-133] quit
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1] commit
   ```
7. Configure a BAS interface, specify a user access type for the interface, and configure an authentication scheme.
   
   
   ```
   [~BRAS-GigabitEthernet0/1/1.1] bas
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1-bas] access-type layer2-subscriber default-domain authentication wdomain
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1-bas] authentication-method bind
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1-bas] quit
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1] quit
   ```
   ```
   [*BRAS] commit
   ```
8. Enable multicast replication by interface + VLAN on a BAS interface.
   
   
   ```
   [~BRAS] interface gigabitethernet 0/1/1.1
   ```
   ```
   [~BRAS-GigabitEthernet0/1/1.1] bas
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1-bas] multicast copy by-vlan
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1-bas] commit
   ```
   ```
   [~BRAS-GigabitEthernet0/1/1.1-bas] quit
   ```
9. Configure basic multicast functions.
   
   
   ```
   [~BRAS] multicast ipv6 routing-enable
   ```
   ```
   [*BRAS] interface gigabitethernet 0/1/0
   ```
   ```
   [*BRAS-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*BRAS-GigabitEthernet0/1/0] ipv6 enable
   ```
   ```
   [*BRAS-GigabitEthernet0/1/0] ipv6 address 2001:db8:1::1/64
   ```
   ```
   [*BRAS-GigabitEthernet0/1/0] pim ipv6 sm
   ```
   ```
   [*BRAS-GigabitEthernet0/1/0] quit
   ```
   ```
   [*BRAS] commit
   ```
   ```
   [~BRAS] interface gigabitethernet 0/1/1.1
   ```
   ```
   [~BRAS-GigabitEthernet0/1/1.1] ipv6 enable
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1] ipv6 address auto link-local
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1] pim ipv6 sm
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1] mld enable
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1] quit
   ```
   ```
   [*BRAS] commit
   ```
10. Verify the configuration.
    
    # Run the **display multicast group-ip** command to display information about users of a specified multicast group. The command output shows that the user with ID 65 joins the multicast program whose group address is FF18::1.
    ```
    [~BRAS] display multicast group-ip FF18::1 out-interface GigabitEthernet 0/1/1.1
      User ID    User IP                     User type    Interface
    
      65         2001:db8:1::10:CC00:200:27E9      Local        GigabitEthernet0/1/1.1
    
      Local user number :1
      Remote user number:0
      Total user number :1
    ```
    
    # Run the **display multicast user-id** command to check the multicast programs that a specified user joins on a BAS interface.
    ```
    [~BRAS] display multicast user-id 65
      User information:
      User ID             :65
      User IPv6 address   :2001:db8:1::10:CC00:200:27E9
      Gateway IPv6 address:FE80::200:14FF:FE00:571
      BRAS interface      :GigabitEthernet0/1/1.1
      User MAC-address    :00-e0-fc-12-34-56
      MAX program list    :4
    
      User order program:
      Group IP           Source IP
      FF18::1            ::
    
      Total:1
    ```
    
    # Run the **display pim ipv6 routing-table** command to check IPv6 PIM routing entries. For example:
    ```
    [~BRAS] display pim ipv6 routing-table
     VPN-Instance: public net
     Total 1 (*, G) entry; 1 (S, G) entry
    
     (*, FF18::1)
         RP: NULL
         Protocol: pim-sm, Flag: WC NIIF
         UpTime: 00:01:31
         Upstream interface: NULL, Refresh time: 00:01:31
             Upstream neighbor: NULL
             RPF prime neighbor: NULL
         Downstream interface(s) information:
         Total number of downstreams: 1
            1: GigabitEthernet0/1/1(bas)
                 Protocol: mld, UpTime: 00:01:31, Expires: -
    
     (2001:db8:1::2, FF18::1)
         RP: NULL
         Protocol: pim-sm, Flag: SPT LOC ACT
         UpTime: 01:39:59
         Upstream interface: GigabitEthernet0/1/0, Refresh time: 01:39:59
             Upstream neighbor: NULL
             RPF prime neighbor: NULL
         Downstream interface(s) information:
         Total number of downstreams: 1
            1: GigabitEthernet0/1/1(bas)
                 Protocol: pim-sm, UpTime: 00:01:31, Expires: -  
    ```

#### Configuration Files

```
#
sysname BRAS
#
multicast ipv6 routing-enable      
#
radius-server group shiva                                                       
 radius-server authentication 10.7.66.66 1812 weight 0                                             
 radius-server accounting 10.7.66.66 1813 weight 0                                                        
 radius-server shared-key-cipher %^%#h{FXVBLZX9#`VI]EWUUaOSHGd5E!.1DGeVYEie=%^%                                       
 radius-server retransmit 2                                                    
# 
aaa
 #
 authentication-scheme radius
  authentication-mode radius
 #
 accounting-scheme none
  accounting-mode none
 #
 domain wdomain
  authentication-scheme radius
  accounting-scheme none
  radius-server group shiva
  ipv6-pool ipv6
#
interface GigabitEthernet0/1/0
 undo shutdown
 ipv6 enable
 ipv6 address 2001:db8:1::1/64
 pim ipv6 sm     
#
interface GigabitEthernet0/1/1.1
 ipv6 enable
 ipv6 address auto link-local
 user-vlan 133
 pim ipv6 sm
 mld enable
 bas
 #
  access-type layer2-subscriber default-domain authentication wdomain
  authentication-method bind
  multicast copy by-vlan
 #                                      
#
ipv6 prefix ipv6 local
 prefix 2001:db8:1::/64
#
ipv6 pool ipv6 bas local
 prefix ipv6                     
#
return  
```