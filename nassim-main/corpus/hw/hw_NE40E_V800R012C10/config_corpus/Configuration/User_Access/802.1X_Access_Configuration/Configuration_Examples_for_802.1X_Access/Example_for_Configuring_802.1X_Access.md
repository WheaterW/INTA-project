Example for Configuring 802.1X Access
=====================================

This section provides an example for configuring 802.1X access. A networking diagram is provided to help you understand the configuration procedure. This example covers networking requirements, configuration roadmap, configuration procedure, and configuration files.

#### Networking Requirements

To prevent unauthorized users or devices from gaining access to a network and ensure network security, you can configure 802.1X access services to allow only authorized users to access the network. On the network shown in [Figure 1](#EN-US_TASK_0172374179__fig_dc_ne_cfg_01359301):

* The user belongs to the domain **isp4** and accesses the Internet through GE0/1/2.1 on the Router in 802.1X mode.
* RADIUS authentication and accounting are used.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  In the 802.1X system, the NE40E functions as a relay agent, which must transmit EAP packets through the RADIUS server.
* The IP address of the RADIUS server is 192.168.7.249. The authentication and accounting port numbers are 1645 and 1646, respectively. RADIUS+1.1 is used, with the key being **Huawei**.
* The IP address of the DNS server is 192.168.7.252.
* The network-side interface is GE0/2/1.

**Figure 1** Configuring 802.1X access![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 and 2 represent GE0/1/2.1 and GE0/2/1, respectively.


  
![](images/fig_dc_ne_cfg_01359301.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an 802.1X template.
2. Configure an authentication scheme.
3. Configure an accounting scheme.
4. Configure a RADIUS server group.
5. Configure an address pool.
6. Configure a domain named **isp4**.
7. Configure a BAS interface.

#### Data Preparation

To complete the configuration, you need the following data:

* Name of the 802.1X template
* Timeout period for the device to wait for an EAP response packet from the authentication server
* Timeout period for the device to wait for a packet from the client and the number of packet retransmissions
* Number of handshake packet retransmissions between the EAP client and server and the timeout period
* IP address of the RADIUS server
* Address pool name, gateway address, IP address range, and DNS server address

#### Procedure

1. Configure an 802.1X template.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname Router
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~Router] dot1x-template 4
   ```
   ```
   [*Router-dot1x-template-4] authentication timeout 20
   ```
   ```
   [*Router-dot1x-template-4] request interval 20 retransmit 3
   ```
   ```
   [*Router-dot1x-template-4] reauthentication interval 1800
   ```
   ```
   [*Router-dot1x-template-4] keepalive interval 15 retransmit 2
   ```
   ```
   [*Router-dot1x-template-4] commit
   ```
   ```
   [~Router-dot1x-template-4] quit
   ```
2. Configure an authentication scheme.
   
   
   ```
   [~Router] aaa
   ```
   ```
   [~Router-aaa] authentication-scheme auth4
   ```
   ```
   [*Router-aaa-authen-auth4] authentication-mode radius
   ```
   ```
   [*Router-aaa-authen-auth4] commit
   ```
   ```
   [~Router-aaa-authen-auth4] quit
   ```
3. Configure an accounting scheme.
   
   
   ```
   [~Router-aaa] accounting-scheme acct4
   ```
   ```
   [*Router-aaa-accounting-acct4] accounting-mode radius
   ```
   ```
   [*Router-aaa-accounting-acct4] commit
   ```
   ```
   [~Router-aaa-accounting-acct4] quit
   ```
   ```
   [~Router-aaa] quit
   ```
4. Configure a RADIUS server group.
   
   
   ```
   [~Router] radius-server group rd4
   ```
   ```
   [*Router-radius-rd4] radius-server authentication 192.168.7.249 1645
   ```
   ```
   [*Router-radius-rd4] radius-server accounting 192.168.7.249 1646
   ```
   ```
   [*Router-radius-rd4] radius-server type plus11
   ```
   ```
   [*Router-radius-rd4] radius-server traffic-unit kbyte
   ```
   ```
   [*Router-radius-rd4] radius-server shared-key Huawei
   ```
   ```
   [*Router-radius-rd4] commit
   ```
   ```
   [~Router-radius-rd4] quit
   ```
5. Configure an address pool.
   
   
   ```
   [~Router] ip pool pool4 bas local
   ```
   ```
   [~Router-ip-pool-pool4] gateway 10.82.1.1 255.255.255.0
   ```
   ```
   [*Router-ip-pool-pool4] commit
   ```
   ```
   [~Router-ip-pool-pool4] section 0 10.82.1.2 10.82.1.200
   ```
   ```
   [~Router-ip-pool-pool4] dns-server 192.168.7.252
   ```
   ```
   [*Router-ip-pool-pool4] commit
   ```
   ```
   [~Router-ip-pool-pool4] quit
   ```
6. Configure a domain named **isp4**.
   
   
   ```
   [~Router] aaa
   ```
   ```
   [~Router-aaa] domain isp4
   ```
   ```
   [*Router-aaa-domain-isp4] authentication-scheme auth4
   ```
   ```
   [*Router-aaa-domain-isp4] accounting-scheme acct4
   ```
   ```
   [*Router-aaa-domain-isp4] commit
   ```
   ```
   [~Router-aaa-domain-isp4] radius-server group rd4
   ```
   ```
   [*Router-aaa-domain-isp4] commit
   ```
   ```
   [~Router-aaa-domain-isp4] ip-pool pool4
   ```
   ```
   [*Router-aaa-domain-isp4] dot1x-template 4
   ```
   ```
   [*Router-aaa-domain-isp4] commit
   ```
   ```
   [~Router-aaa-domain-isp4] quit
   ```
   ```
   [~Router-aaa] quit
   ```
7. Configure a BAS interface.
   
   
   ```
   [~Router] interface gigabitEthernet 0/1/2.1
   ```
   ```
   [*Router-GigabitEthernet0/1/2.1] commit
   ```
   ```
   [~Router-GigabitEthernet0/1/2.1] user-vlan 100
   ```
   ```
   [~Router-GigabitEthernet0/1/2.1-vlan-100-100] quit
   ```
   ```
   [~Router-GigabitEthernet0/1/2.1] bas
   ```
   ```
   [~Router-GigabitEthernet0/1/2.1-bas] access-type layer2-subscriber
   ```
   ```
   [*Router-GigabitEthernet0/1/2.1-bas] default-domain authentication isp4
   [*Router-GigabitEthernet0/1/2.1-bas] authentication-method dot1x
   [*Router-GigabitEthernet0/1/2.1-bas] commit
   [~Router-GigabitEthernet0/1/2.1-bas] quit
   [~Router-GigabitEthernet0/1/2.1] quit
   ```

#### Configuration Files

```
#
```
```
sysname Router
```
```
#
```
```
radius-server group rd4
```
```
 radius-server authentication 192.168.7.249 1645 weight 0
```
```
 radius-server accounting 192.168.7.249 1646 weight 0
```
```
 radius-server shared-key %^%#`E)v.Q@BHVzxxZ;ij{>&_M0!TGP7YRA@8a7mq<\/%^%#
```
```
 radius-server type plus11
```
```
 radius-server traffic-unit kbyte
```
```
#
```
```
interface GigabitEthernet1/0/2.1
```
```
 user-vlan 100
```
```
 bas
```
```
  access-type layer2-subscriber default-domain authentication isp4
```
```
  authentication-method dot1x
```
```
#
```
```
ip pool pool4 bas local
```
```
 gateway 10.82.1.1 255.255.255.0
```
```
 section 0 10.82.1.2 10.82.1.200
```
```
 dns-server 192.168.7.252
```
```
#
```
```
dot1x-template 4
```
```
 authentication timeout 20
```
```
 request retransmit 3 interval 20
```
```
 request interval 20 retransmit 3
```
```
 reauthentication interval 1800
```
```
 keepalive retransmit 2 interval 15
```
```
 keepalive interval 15 retransmit 2
```
```
#
```
```
aaa
```
```
authentication-scheme auth4
```
```
accounting-scheme acct4
```
```
domain isp4
```
```
 authentication-scheme auth4
```
```
 accounting-scheme acct4
```
```
 radius-server group rd4
```
```
 dot1x-template 4
```
```
 ip-pool pool4
```
```
#
```
```
return
```