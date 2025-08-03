Example for Configuring Dual-Stack Static User Access (CPE Working in Bridging Mode)
====================================================================================

This section describes how to configure dual-stack static user access on a network where a CPE works in bridging mode. Configure static IPv4 and IPv6 addresses for a client, and allow the client to be triggered to go online by sending NS/NA or IPv6 packets. A networking diagram is provided to help you understand the configuration procedure.

#### Networking Requirements

[Figure 1](#EN-US_TASK_0188372431__fig112721616111120) shows a network for dual-stack static user access. The CPE works in bridging mode. The requirements are as follows: Static IPv4 and IPv6 addresses are configured for the client. The client can be triggered to go online by sending NS/NA or IPv6 packets. The CPE transparently transmits user packets to the BRAS. After RADIUS authentication succeeds, the static user can access the Internet.

**Figure 1** Configuring dual-stack static user access (CPE working in bridging mode)![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/2/1.1 and GE 0/1/1, respectively.


  
![](figure/en-us_image_0188403495.png)
#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure AAA schemes and a RADIUS server group.
2. Configure a username generation mode and a user password.
3. Configure address pools.
   * Configure a local IPv4 address pool. Configure the device to exclude the IP address of the static user in automatic address assignment.
   * Configure a local IPv6 prefix pool.
   * Configure a local IPv6 address pool. Bind the local IPv6 prefix pool to this local IPv6 address pool.
4. Configure an AAA domain. Apply the RADIUS server group, authentication and accounting schemes, and address pools to the AAA domain.
5. Configure the DHCPv6 device to generate DUIDs in DUID-LLT mode.
6. Configure interfaces.
7. Configure IS-IS and BGP.
8. Configure a static user.

#### Data Preparation

To complete the configuration, you need the following data:

* RADIUS server group name, and IP address and port numbers of the RADIUS authentication and accounting server
* Name and authentication mode of the authentication template (RADIUS authentication is performed for users on the BRAS.)
* Accounting scheme name and accounting mode
* Local IPv4 address pool-related parameters, including the gateway address and address range
* Local IPv6 prefix pool name, address prefix, and prefix length
* AAA domain name
* Interface IPv4 and IPv6 addresses
* BGP peer addresses and passwords


#### Procedure

1. # Set a host name, such as **Device**, for the BRAS.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname Device
   ```
   ```
   [*HUAWEI] commit
   ```
2. Configure AAA schemes.
   1. Configure an authentication scheme.
      
      
      ```
      [~Device] aaa
      ```
      ```
      [~Device-aaa] authentication-scheme radius
      ```
      ```
      [*Device-aaa-authen-radius] authentication-mode radius
      ```
      ```
      [*Device-aaa-authen-radius] quit
      ```
      ```
      [*Device-aaa] commit
      ```
   2. Configure an accounting scheme.
      
      
      ```
      [~Device-aaa] accounting-scheme radius
      ```
      ```
      [*Device-aaa-accounting-radius] accounting-mode radius
      ```
      ```
      [*Device-aaa-accounting-radius] quit
      ```
      ```
      [*Device-aaa] quit
      ```
      ```
      [*Device] commit
      ```
3. Configure a RADIUS server group.
   
   
   ```
   [~Device] radius-server group radius
   ```
   ```
   [*Device-radius-radius] radius-server authentication 192.168.7.249 1812
   ```
   ```
   [*Device-radius-radius] radius-server accounting 192.168.7.249 1813
   ```
   ```
   [*Device-radius-radius] radius-server shared-key-cipher YsHsjx_202206
   ```
   ```
   [*Device-radius-radius] quit
   ```
   ```
   [*Device] commit
   ```
4. Configure a username generation mode and a user password.
   
   
   ```
   [~Device] aaa
   ```
   ```
   [~Device-aaa] default-user-name include ip-address .
   ```
   ```
   [*Device-aaa] default-password cipher YsHsjx_202206
   ```
   ```
   [*Device-aaa] commit
   ```
   ```
   [~Device-aaa] quit
   ```
5. Configure address pools.
   1. Configure a local IPv4 address pool. Configure the device to exclude the IP address segment of the user's IPv4 address during automatic address assignment.
      
      
      ```
      [~Device] ip pool pool1 bas local
      ```
      ```
      [~Device-ip-pool-pool1] gateway 10.179.180.1 255.255.255.0
      ```
      ```
      [*Device-ip-pool-pool1] section 0 10.179.180.2 10.179.180.254
      ```
      ```
      [*Device-ip-pool-pool1] excluded-ip-address 10.179.180.2 10.179.180.254
      ```
      ```
      [*Device-ip-pool-pool1] quit
      ```
   2. Configure a local IPv6 prefix pool.
      
      
      ```
      [*Device] ipv6 prefix pre1 local
      ```
      ```
      [*Device-ipv6-prefix-pre1] prefix 2001:db8:1::/48
      ```
      ```
      [*Device-ipv6-prefix-pre1] excluded-ipv6-address 2001:db8:1::1
      ```
      ```
      [*Device-ipv6-prefix-pre1] quit
      ```
   3. Configure a local IPv6 address pool. Bind the local IPv6 prefix pool to this local IPv6 address pool.
      
      
      ```
      [*Device] ipv6 pool pool1 bas local
      ```
      ```
      [*Device-ipv6-pool-pool1] prefix pre1
      ```
      ```
      [*Device-ipv6-pool-pool1] quit
      ```
      ```
      [*Device] commit
      ```
6. Configure an AAA domain. Bind the configured authentication and accounting schemes, RADIUS server group, and IPv4 and IPv6 address pools to the AAA domain.
   
   
   ```
   [~Device] aaa
   ```
   ```
   [~Device-aaa] domain dom1
   ```
   ```
   [*Device-aaa-domain-dom1] authentication-scheme radius
   ```
   ```
   [*Device-aaa-domain-dom1] accounting-scheme radius
   ```
   ```
   [*Device-aaa-domain-dom1] radius-server group radius
   ```
   ```
   [*Device-aaa-domain-dom1] commit
   ```
   ```
   [~Device-aaa-domain-dom1] ip-pool pool1
   ```
   ```
   [*Device-aaa-domain-dom1] ipv6-pool pool1
   ```
   ```
   [*Device-aaa-domain-dom1] quit
   ```
   ```
   [*Device-aaa] quit
   ```
7. Configure the DHCPv6 device to generate DUIDs in DUID-LLT mode.
   
   
   ```
   [*Device] dhcpv6 duid llt
   ```
   ```
   [*Device] commit
   ```
8. Configure interfaces.
   1. Configure a network-side interface, and enable IPv6 for the interface.
      
      
      ```
      [~Device] interface GigabitEthernet 0/1/1 
      ```
      ```
      [~Device-GigabitEthernet0/1/1] ipv6 enable
      ```
      ```
      [*Device-GigabitEthernet0/1/1] ipv6 address 2001:db8:0200:2:2102:2205:1:1 127
      ```
      ```
      [*Device-GigabitEthernet0/1/1] ipv6 address auto link-local
      ```
      ```
      [*Device-GigabitEthernet0/1/1] ip address 172.16.0.10 16
      ```
      ```
      [*Device-GigabitEthernet0/1/1] commit
      ```
      ```
      [~Device-GigabitEthernet0/1/1] quit
      ```
   2. Configure a loopback interface, such as loopback 0, and enable IPv6 for the interface.
      
      
      ```
      [~Device] interface loopback0
      ```
      ```
      [~Device-LoopBack0] ipv6 enable
      ```
      ```
      [*Device-LoopBack0] ipv6 address 2001:db8:0200::2205 128
      ```
      ```
      [*Device-LoopBack0] ipv6 address auto link-local
      ```
      ```
      [*Device-LoopBack0] ip address 10.10.10.10 16 
      ```
      ```
      [*Device-LoopBack0] commit
      ```
      ```
      [~Device-LoopBack0] quit
      ```
   3. Configure a BAS interface, and enable IPv6 for the BAS interface.
      
      
      ```
      [~Device] interface GigabitEthernet 0/2/1.1
      ```
      ```
      [~Device-GigabitEthernet0/2/1.1] ipv6 enable
      ```
      ```
      [*Device-GigabitEthernet0/2/1.1] ipv6 address auto link-local
      ```
      ```
      [*Device-GigabitEthernet0/2/1.1] commit
      ```
      ```
      [~Device-GigabitEthernet0/2/1.1] user-vlan 1 10 qinq 100
      ```
      ```
      [*Device-GigabitEthernet0/2/1.1-vlan-1-10-QinQ-100-100] bas
      ```
      ```
      [*Device-GigabitEthernet0/2/1.1-bas] access-type layer2-subscriber default-domain authentication dom1
      ```
      ```
      [*Device-GigabitEthernet0/2/1.1-bas] authentication-method bind
      ```
      ```
      [*Device-GigabitEthernet0/2/1.1-bas] authentication-method-ipv6 bind
      ```
      ```
      [*Device-GigabitEthernet0/2/1.1-bas] ip-trigger
      ```
      ```
      [*Device-GigabitEthernet0/2/1.1-bas] arp-trigger
      ```
      ```
      [~Device-GigabitEthernet0/2/1.1-bas] ipv6-trigger
      ```
      ```
      [*Device-GigabitEthernet0/2/1.1-bas] nd-trigger
      ```
      ```
      [*Device-GigabitEthernet0/2/1.1-bas] commit
      ```
      ```
      [~Device-GigabitEthernet0/2/1.1-bas] quit
      ```
      ```
      [~Device-GigabitEthernet0/2/1.1] quit
      ```
9. Configure basic IS-IS functions.
   1. Create an IS-IS process, and enable IPv6 for the process.
      
      
      ```
      [~Device] isis 100
      ```
      ```
      [*Device-isis-100] cost-style wide
      ```
      ```
      [*Device-isis-100] ipv6 enable topology ipv6                
      ```
      ```
      [*Device-isis-100] ipv6 preference 105
      ```
      ```
      [*Device-isis-100] commit
      ```
      ```
      [~Device-isis-100] quit
      ```
   2. Configure an IS-IS interface. (The cost value needs to be planned based on the actual situation.)
      
      
      ```
      [~Device] interface GigabitEthernet 0/1/1
      ```
      ```
      [~Device-GigabitEthernet0/1/1] isis enable 100
      ```
      ```
      [*Device-GigabitEthernet0/1/1] isis ipv6 enable 100
      ```
      ```
      [*Device-GigabitEthernet0/1/1] isis ipv6 cost 500 level-2
      ```
      ```
      [*Device-GigabitEthernet0/1/1] commit
      ```
      ```
      [~Device-GigabitEthernet0/1/1] quit
      ```
      
      
      ```
      [~Device] interface loopback0
      ```
      ```
      [~Device-LoopBack0] isis enable 100
      ```
      ```
      [*Device-LoopBack0] isis ipv6 enable 100
      ```
      ```
      [*Device-LoopBack0] commit
      ```
      ```
      [~Device-LoopBack0] quit
      ```
10. Configure basic BGP functions.
    1. Create a BGP process, and configure peers to set up BGP peer relationships.
       
       
       ```
       [~Device] bgp 64830 
       ```
       ```
       [*Device-bgp] group IPv6-GROUP internal
       ```
       ```
       [*Device-bgp] peer IPv6-GROUP password cipher YsHsjx_202206
       ```
       ```
       [*Device-bgp] peer 2001:db8:0200::2101 as-number 64830
       ```
       ```
       [*Device-bgp] peer 2001:db8:0200::2101 group IPv6-GROUP
       ```
       ```
       [*Device-bgp] group group2 external
       ```
       
       
       ```
       [*Device-bgp] peer 2.2.2.2 as-number 101
       ```
       ```
       [*Device-bgp] peer 2.2.2.2 group group2 
       ```
       ```
       [*Device-bgp] peer 3.3.3.3 as-number 101 
       ```
       ```
       [*Device-bgp] peer 3.3.3.3 group group2 
       ```
    2. Configure the device to import UNRs to the IPv4 unicast address family.
       
       
       ```
       [*Device-bgp] ipv4-family unicast
       ```
       ```
       [*Device-bgp-af-ipv4] undo synchronization  
       ```
       ```
       [*Device-bgp-af-ipv4] peer group2 enable  
       ```
       ```
       [*Device-bgp-af-ipv4] import-route unr  
       ```
       
       
       ```
       [*Device-bgp-af-ipv4] commit  
       ```
       ```
       [~Device-bgp-af-ipv4] quit
       ```
    3. Enable the IPv6 peer in the IPv6 unicast address family view. Configure BGP process 64830 to import UNRs.
       
       
       ```
       [~Device-bgp] ipv6-family unicast
       ```
       ```
       [*Device-bgp-af-ipv6] undo synchronization  
       ```
       ```
       [*Device-bgp-af-ipv6] preference 20 230 230
       ```
       ```
       [*Device-bgp-af-ipv6] maximum load-balancing 6
       ```
       ```
       [*Device-bgp-af-ipv6] peer IPv6-GROUP enable
       ```
       ```
       [*Device-bgp-af-ipv6] peer IPv6-GROUP advertise-community
       ```
       ```
       [*Device-bgp-af-ipv6] peer IPv6-GROUP keep-all-routes
       ```
       
       
       ```
       [*Device-bgp-af-ipv6] peer 2001:db8:0200::2101 enable
       ```
       ```
       [*Device-bgp-af-ipv6] peer 2001:db8:0200::2101 group IPv6-GROUP
       ```
       
       
       ```
       [*Device-bgp-af-ipv6] import-route unr
       ```
       ```
       [*Device-bgp-af-ipv6] commit
       ```
       ```
       [~Device-bgp-af-ipv6] quit
       ```
       ```
       [~Device-bgp] quit
       ```
11. Configure a static user. The VLAN configured here must be within the VLAN range configured for the BAS interface.
    
    
    ```
    [~Device] static-user 10.179.180.253 10.179.180.253 gateway 10.179.180.1 2001:db8:1::1 2001:db8:1::1 ipv6-gateway 2001:db8:1:: interface GigabitEthernet0/2/1.1 vlan 1 qinq 100 domain-name dom1 detect 
    ```
    ```
    [*Device] commit
    ```
    ```
    [~Device] quit
    ```
12. Verify the configuration.
    
    
    
    # Run the **display ip pool** command on the Router. The command output shows that the configurations meet the requirements.
    
    ```
    <Device> display ip pool
    ```
    ```
    -----------------------------------------------------------------------
       Pool-Name      : pool1
       Pool-No        : 0
       Pool-constant-index: -
       Position       : Local          Status           : Unlocked
       RUI-Flag       : -    
       Gateway        : 10.179.180.1      Mask             : 255.255.255.0
       Vpn instance   : --              Unnumbered gateway: -
       IP address Statistic
         Total       :253
         Used        :0          Free      :0
         Conflicted  :0          Disable   :0
         Designated  :0          Gateway   :0
         Ratio       :100%
         Isolated    :0
    ----------------------------------------------------------------------
        IP address pool Statistic
         Local       :1          Remote    :0          Server    :0
        IP address Statistic
         Total       :253
         Used        :0          Free      :0
         Conflicted  :0          Disable   :0
         Designated  :0          Gateway   :0
         Ratio       :100%
         Isolated    :0  
    ```
    
    
    
    # Run the **display ipv6 prefix** command on the Router. The command output shows that the configurations meet the requirements.
    
    ```
    <Device> display ipv6 prefix
    ```
    ```
     -------------------------------------------------------------------------------
     Index Name            Address/Length            Type            Constant-index
     -------------------------------------------------------------------------------
     0     pre1           2001:db8:1::/48           LOCAL           - 
     -------------------------------------------------------------------------------
     Total created prefix pool(s): 1
    ```

#### Configuration Files

```
#
sysname Device
#
dhcpv6 duid 0001000124fbc193dc99141ea1e9
#
ipv6 prefix pre1 local
 prefix 2001:db8:1::/48
 excluded-ipv6-address 2001:db8:1::1
#
ipv6 pool pool1 bas local
 prefix pre1
#
radius-server group radius
 radius-server shared-key-cipher %^%#glhJ;yPG#$=tC&(Is%q!S_";(k.Ef$:978$$e:TY%^%
 radius-server authentication 192.168.7.249 1812 weight 0
 radius-server accounting 192.168.7.249 1813 weight 0
#
ip pool pool1 bas local
 gateway 10.179.180.1 255.255.255.0
 section 0 10.179.180.2 10.179.180.254
 excluded-ip-address 10.179.180.2 10.179.180.254
#
aaa
 default-user-name include ip-address .
 default-password cipher $$e:TY%^%glhJ;yPG#$=tC&(Is%q!S_";(k.Ef$%^%#:978 
 authentication-scheme radius
 accounting-scheme radius
 #
 domain dom1
  authentication-scheme radius
  accounting-scheme radius
  radius-server group radius
  ip-pool pool1
  ipv6-pool pool1
#
isis 100
 cost-style wide
 traffic-eng level-2
 #
 ipv6 enable topology ipv6
 ipv6 preference 105
 #
#
interface GigabitEthernet0/1/1
 ipv6 enable
 ipv6 address 2001:db8:200:2:2102:2205:1:1/127
 ipv6 address auto link-local
 ip address 172.16.0.10 255.255.0.0 
 isis enable 100
 isis ipv6 enable 100
 isis ipv6 cost 500 level-2
#
interface GigabitEthernet0/2/1.1
 ipv6 enable
 ipv6 address auto link-local
 statistic enable
 user-vlan 1 10 qinq 100
 bas
 #
  access-type layer2-subscriber default-domain authentication dom1
  authentication-method bind
  authentication-method-ipv6 bind
  ip-trigger
  arp-trigger
  ipv6-trigger
  nd-trigger
 #
#
interface LoopBack0
 ipv6 enable
 ipv6 address 2001:db8:0200::2205/128
 ipv6 address auto link-local
 ip address 10.10.10.10 255.255.0.0 
 isis enable 100
 isis ipv6 enable 100
#
bgp 64830
 group IPv6-GROUP internal
 peer IPv6-GROUP password cipher %^%#rxKl0^%`n7zLXD<YQ,gFwwtzMEjGK!j}a`L;h(aU%^%#
 peer 2001:DB8:200::2101 as-number 64830
 peer 2001:DB8:200::2101 group IPv6-GROUP
 group group2 external
 peer 2.2.2.2 as-number 101
 peer 2.2.2.2 group group2
 peer 3.3.3.3 as-number 101
 peer 3.3.3.3 group group2
 #
 ipv4-family unicast
  undo synchronization
  import-route unr
  peer group2 enable
  peer 2.2.2.2 enable
  peer 2.2.2.2 group group2
  peer 3.3.3.3 enable
  peer 3.3.3.3 group group2
 # 
 ipv6-family unicast
  undo synchronization
  preference 20 230 230
  import-route unr
  maximum load-balancing 6
  peer IPv6-GROUP enable
  peer IPv6-GROUP advertise-community
  peer IPv6-GROUP keep-all-routes
  peer 2001:DB8:200::2101 enable
  peer 2001:DB8:200::2101 group IPv6-GROUP
#  
static-user 10.179.180.253 10.179.180.253 gateway 10.179.180.1 2001:db8:1::1 2001:db8:1::1 ipv6-gateway 2001:db8:1:: interface GigabitEthernet0/2/1.1 vlan 1 qinq 100 domain-name dom1 detect
#
return                                                                             
```