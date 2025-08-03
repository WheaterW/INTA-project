Example for Configuring a Remote Address Pool to Assign IPv6 Addresses to DHCPv6 Users
======================================================================================

This section provides an example for configuring a user-side remote address pool to assign IPv6 addresses to users. A networking diagram is provided to help you understand the configuration procedure. The example covers the networking requirements, configuration roadmap, configuration procedure, and configuration files.

#### Networking Requirements

When a DHCPv6 server and clients are not directly connected, the Device can function as a Layer 2 access device to relay user requests for IPv6 addresses or prefixes to the DHCPv6 server.

On the network shown in [Figure 1](#EN-US_TASK_0172373941__fig_dc_ne_ipv6_address_cfg_008701):

* The user accesses the Device in IPoE mode and belongs to the domain **isp1**.
* The user is assigned an address on the network segment 2001:db81::/64.
* RADIUS authentication and accounting are used.
* The IP address of the RADIUS server is 10.6.55.55, the authentication port number is 1550, the accounting port number is 1551, the standard RADIUS protocol is used, and the key is **YsHsjx\_202206**.
* The IP address of the DHCPv6 server is 2001:db82::2:2.

**Figure 1** Configuring a user-side remote address pool to assign IPv6 addresses![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 through 3 represent GE0/1/1.1, GE0/1/2, and GE0/1/3, respectively.


  
![](images/fig_dc_ne_ipv6_address_cfg_008701.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure AAA schemes.
2. Configure a RADIUS server group.
3. Configuring a DHCPv6 Server Group
4. Configure a remote prefix pool.
5. Configure a user-side remote address pool and bind the DHCPv6 server group and prefix pool to the address pool.
6. Configure an AAA domain to be used as the default authentication domain.
7. Configure interfaces.

#### Data Preparation

To complete the configuration, you need the following data:

* Name of the remote IPv6 prefix pool
* Name of the remote address pool
* IPv6 prefix to be assigned/prefix length
* User authentication mode on DeviceB (RADIUS authentication)

#### Procedure

1. Configure AAA schemes on the Device.
   
   
   
   # Configure an authentication scheme.
   
   ```
   <Device> system-view
   ```
   ```
   [~Device] aaa
   ```
   ```
   [~Device-aaa] authentication-scheme auth1
   ```
   ```
   [*Device-aaa-authen-auth1] authentication-mode radius
   ```
   ```
   [*Device-aaa-authen-auth1] commit
   ```
   ```
   [~Device-aaa-authen-auth1] quit
   ```
   
   # Configure an accounting scheme.
   
   ```
   [~Device-aaa] accounting-scheme acct1
   ```
   ```
   [*Device-aaa-accounting-acct1] accounting-mode radius
   ```
   ```
   [*Device-aaa-accounting-acct1] commit
   ```
   ```
   [~Device-aaa-accounting-acct1] quit
   ```
   ```
   [~Device-aaa] quit
   ```
2. Configure a RADIUS server group on the Device.
   
   
   ```
   [~Device] radius-server group rd1
   ```
   ```
   [*Device-radius-rd1] radius-server authentication 10.6.55.55 1550
   ```
   ```
   [*Device-radius-rd1] radius-server accounting 10.6.55.55 1551
   ```
   ```
   [*Device-radius-rd1] commit
   ```
   ```
   [~Device-radius-rd1] radius-server type standard
   ```
   ```
   [~Device-radius-rd1] radius-server shared-key-cipher YsHsjx_202206
   ```
   ```
   [*Device-radius-rd1] commit
   ```
   ```
   [~Device-radius-rd1] quit
   ```
3. Configure a DHCPv6 server group named **server1** on the Device.
   
   
   ```
   [~Device] dhcpv6-server group server1
   ```
   ```
   [*Device-dhcpv6-server-group-server1] commit
   ```
   ```
   [~Device-dhcpv6-server-group-server1] dhcpv6-server destination 2001:db82::2:2
   ```
   ```
   [~Device-dhcpv6-server-group-server1] quit
   ```
4. Configure a remote IPv6 prefix pool named **pre1** on the Device.
   
   
   ```
   [~Device] ipv6 prefix pre1 remote
   ```
   ```
   [~Device-ipv6-prefix-pre1] link-address 2001:db81::1/64
   ```
   ```
   [~Device-ipv6-prefix-pre1] dhcpv6-only
   ```
   ```
   [*Device-ipv6-prefix-pre1] commit
   ```
   ```
   [~Device-ipv6-prefix-pre1] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The **dhcpv6-only** command allows an IPv6 prefix pool to be used for IPv6 address or prefix assignment only for DHCPv6 users. If this command is not run, the IPv6 prefix pool can be used to assign IPv6 addresses to ND and DHCPv6 users.
5. Configure a user-side remote address pool named **pool1** on the Device.
   
   
   ```
   [~Device] ipv6 pool pool1 bas remote
   ```
   ```
   [~Device-ipv6-pool-pool1] prefix pre1
   ```
   ```
   [~Device-ipv6-pool-pool1] dhcpv6-server group server1
   ```
   ```
   [~Device-ipv6-pool-pool1] commit
   ```
   ```
   [~Device-ipv6-pool-pool1] quit
   ```
6. Configure a domain named **isp1** on the Device.
   
   
   ```
   [~Device] aaa
   ```
   ```
   [~Device-aaa] domain isp1
   ```
   ```
   [*Device-aaa-domain-isp1] authentication-scheme auth1
   ```
   ```
   [*Device-aaa-domain-isp1] accounting-scheme acct1
   ```
   ```
   [*Device-aaa-domain-isp1] radius-server group rd1
   ```
   ```
   [*Device-aaa-domain-isp1] commit
   ```
   ```
   [~Device-aaa-domain-isp1] ipv6-pool pool1
   ```
   ```
   [~Device-aaa-domain-isp1] quit
   ```
   ```
   [~Device-aaa] quit
   ```
7. Configure interfaces.
   
   
   
   # Configure a BAS interface.
   
   ```
   [~Device] interface GigabitEthernet 0/1/1.1
   ```
   ```
   [*Device-GigabitEthernet0/1/1.1] user-vlan 1 20
   ```
   ```
   [*Device-GigabitEthernet0/1/1.1] commit
   ```
   ```
   [~Device-GigabitEthernet0/1/1.1-vlan-1-20] quit
   ```
   ```
   [~Device-GigabitEthernet0/1/1.1] bas
   ```
   ```
   [~Device-GigabitEthernet0/1/1.1-bas] access-type layer2-subscriber default-domain authentication isp1
   ```
   ```
   [~Device-GigabitEthernet0/1/1.1-bas] authentication-method-ipv6 bind
   ```
   ```
   [*Device-GigabitEthernet0/1/1.1-bas] commit
   ```
   ```
   [~Device-GigabitEthernet0/1/1.1-bas] quit
   ```
   
   
   
   # On the Device, enable IPv6 on the interface and set the M/O value.
   
   ```
   [~Device-GigabitEthernet0/1/1.1] ipv6 enable
   ```
   ```
   [*Device-GigabitEthernet0/1/1.1] ipv6 address auto link-local
   ```
   ```
   [*Device-GigabitEthernet0/1/1.1] ipv6 nd autoconfig managed-address-flag
   ```
   ```
   [*Device-GigabitEthernet0/1/1.1] ipv6 nd autoconfig other-flag
   ```
   ```
   [*Device-GigabitEthernet0/1/1.1] commit
   ```
   ```
   [~Device-GigabitEthernet0/1/1.1] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * In binding authentication, the username is automatically generated based on the location of the NE40E to which a user logs in and domain name. Therefore, configure a username based on the generation rule and configure the password **vlan** on the RADIUS server.
   * For details about the username format used in binding authentication, see the description of the **vlanpvc-to-username** command in *HUAWEI NE40E-M2 series Universal Service Router Command Reference*.
   
   
   
   # Configure the interface connecting Device to the server.
   
   
   
   ```
   [~Device] interface GigabitEthernet 0/1/3
   ```
   ```
   [~Device-GigabitEthernet0/1/3] ipv6 enable
   ```
   ```
   [*Device-GigabitEthernet0/1/3] ipv6 address 2001:db82::2:1 64
   ```
   ```
   [*Device-GigabitEthernet0/1/3] commit
   ```
   ```
   [~Device-GigabitEthernet0/1/3] quit
   ```
8. Verify the configuration.
   
   
   
   # Check information about the prefix pool named **pre1**. The command output shows that the prefix pool is a remote prefix pool.
   
   ```
   [~Device] display ipv6 prefix pre1
   ```
   ```
   -------------------------------------------------------------
    Prefix Name        : pre1
    Prefix Index       : 5
    Prefix constant index: -
    Prefix Type        : REMOTE
    Link-Address       : 2001:db81::1
    Prefix Length      : 64
    Reserved Type      : NONE
    IfLocked           : Unlocked
    Vpn instance       : -
    Lease manage       : false
    Reserved Prefix Count: 0
    Excluded Prefix Count: 0     
   ------------------------------------------------------------- 
   ```
   
   # Check information about the address pool named **pool1**. The command output shows that the address pool is a user-side remote address pool and is bound to the remote prefix pool named **pre1**.
   
   ```
   [~Device] display ipv6 pool pool1
   ```
   ```
   ---------------------------------------------------------------
    Pool name          : pool1
    Pool No            : 3
    Pool constant index: -
    Pool type          : BAS REMOTE
    RUI-Flag           : -
    Preference         : 255
    Renew time         : 50
    Rebind time        : 80
    Status             : UNLOCKED
    Refresh interval   : infinite
    Used by domain     : 1
    Dhcpv6 Unicast     : disable
    Dhcpv6 rapid-commit: disable
    Dns list           : -
    Dns server master  : -
    Dns server slave   : -
    AFTR name          : -
    State              : UP
    Server down times  : 0
    ----------------------------------------------------------------------
    Prefix-Name                      Prefix-Type
    ----------------------------------------------------------------------
    pre1                             REMOTE
    --------------------------------------------------------------- 
   ```

#### Configuration Files

```
#  
sysname Device                                                          
# 
radius-server group rd1
 radius-server authentication 10.6.55.55 1550 weight 0
 radius-server accounting 10.6.55.55 1551 weight 0
 radius-server shared-key-cipher %^%#vS%796FO7%C~pB%CR=q;j}gSCqR-X6+P!.DYI@)%^%#
#
dhcpv6-server group server1
 dhcpv6-server destination 2001:DB82::2:2
#
ipv6 prefix pre1 remote
link-address 2001:DB81::1/64
dhcpv6-only
#
ipv6 pool pool1 bas remote
prefix pre1
dhcpv6-server group server1
#
aaa
 authentication-scheme auth1
 #
 authorization-scheme default
 #
 accounting-scheme acct1
#
domain isp1
  authentication-scheme auth1
  accounting-scheme acct1
  radius-server group rd1
  ipv6-pool pool1    
#
interface GigabitEthernet0/1/1.1
 statistic enable
 ipv6 enable
 ipv6 address auto link-local
 user-vlan 1 20
 ipv6 nd autoconfig managed-address-flag
 ipv6 nd autoconfig other-flag
 bas
 #
  access-type layer2-subscriber default-domain authentication isp1
  authentication-method-ipv6 bind
#
interface GigabitEthernet0/1/3
 ipv6 enable
 ipv6 address 2001:DB82::2:1/64
#
return
```