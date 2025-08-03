Example for Configuring IPv6 User-Side Multicast for PPPoE Access Users
=======================================================================

This section provides an example for configuring IPv6 user-side multicast for PPPoE access users.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172367722__fig_dc_vrp_ipv6bras-multicast_cfg_000801), a user (PC) accesses the network through PPPoE and orders multicast programs.

**Figure 1** Configuring IPv6 user-side multicast for PPPoE access users![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 and interface 2 in this example stand for GE 0/1/0 and GE 0/1/1.1, respectively.


  
![](images/fig_dc_vrp_ipv6bras-multicast_cfg_000801.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure Authentication, Authorization and Accounting (AAA) schemes.
2. Configure a local IPv6 prefix pool.
3. Configure a local IPv6 address pool and bind the local IPv6 prefix pool to the local address pool.
4. Configure an AAA domain and bind it to the IPv6 address pool.
5. Configure the PPPoE access mode:
   
   1. Configure a virtual template (VT) interface.
   2. Bind a VT to an interface.
   3. Bind a sub-interface to a VLAN.
   4. Configure a BAS interface and specify a user access type for the interface.
6. Configure a multicast replication mode. Multicast replication by multicast VLAN is used as an example.
7. Configure basic multicast functions:
   
   1. Enable IPv6 multicast routing.
   2. Enable IPv6 PIM-SM on all BRAS interfaces.
   3. Enable MLD on the BRAS interface connected to users.

#### Data Preparation

* Local prefix pool, address prefix, and prefix length parameters
* Local address pool parameters
* Authentication and accounting schemes (user authentication on the BRAS through RADIUS)
* User domain
* VT number
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
6. Configure a VT interface.
   
   
   ```
   [~BRAS] interface virtual-template 100
   ```
   ```
   [*BRAS-Virtual-Template100] ppp authentication-mode chap
   ```
   ```
   [*BRAS-Virtual-Template100] quit
   ```
   ```
   [*BRAS] commit
   ```
7. Bind a sub-interface to a VLAN and specify a VT interface for the sub-interface.
   
   
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
   [*BRAS-GigabitEthernet0/1/1.1] pppoe-server bind virtual-template 100
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1] commit
   ```
8. Configure a BAS interface and specify a user access type for the interface.
   
   
   ```
   [~BRAS-GigabitEthernet0/1/1.1] bas
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1-bas] access-type layer2-subscriber default-domain authentication wdomain
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
   # Run the **display access-user domain wdomain** command to check information about users that have gone online. The command output shows that the user with the user ID 65 has gone online in PPPoE mode.
   ```
   [~BRAS] display  access-user domain wdomain
     ------------------------------------------------------------------------------
     UserID  Username                Interface      IP address       MAC
             Vlan          IPv6 address             Access type
     ------------------------------------------------------------------------------
     65      spirent33@wdomain       GE0/1/1.1      -                00-e0-fc-12-34-56
             133/-         2001:db8:1::10:CC00:200:27E9   PPPoE
     ------------------------------------------------------------------------------
     Normal users                       : 1
     RUI Local users                    : 0
     RUI Remote users                   : 0
     Total users                        : 1
   ```
9. Enable multicast replication by multicast VLAN on a BAS interface.
   
   
   ```
   [~BRAS] interface gigabitethernet 0/1/1.1
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1] multicast user-aggregation vlan 81
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1] commit
   ```
   ```
   [~BRAS-GigabitEthernet0/1/1.1] quit
   ```
10. Configure basic multicast functions.
    
    
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
11. Verify the configuration.
    
    # Run the **display multicast group-ip** command to display information about users of a specified multicast group. The command output shows that the user with ID 65 joins the multicast program whose group address is FF18::1.
    ```
    [~BRAS] display multicast group-ip FF18::1 out-interface GigabitEthernet 0/1/1.1
      User ID    User IP                     User type    Interface
    
      65         2001:db8:1::10:CC00:200:27E9      Local        GigabitEthernet0/1/1.1
    
      Local user number :1
      Remote user number:0
      Total user number :1
    ```
    
    # Run the **display multicast user-id** command to display information about the multicast programs that a specified user joins on a BAS interface.
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
interface Virtual-Template100
 ppp authentication-mode chap
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
 pppoe-server bind Virtual-Template 100
 pim ipv6 sm
 mld enable
 multicast user-aggregation vlan 81
 bas
 #
  access-type layer2-subscriber default-domain authentication wdomain
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