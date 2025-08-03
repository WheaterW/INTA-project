Example for Configuring QoS Scheduling Based on L2TP Tunnels for User Access
============================================================================

This section provides an example for configuring QoS scheduling based on L2TP tunnels. A networking diagram is provided to help you understand the configuration procedure. The example provides the networking requirements, configuration roadmap, configuration procedure, and configuration files.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172374285__fig_dc_ne_l2tp_cfg_01351101), the NE40E functions as the LNS of the L2TP tunnel. The process for a VPN user to access the headquarters is as follows:

* The user dials up to access the Internet.
* The network access server (NAS) authenticates the user and initiates a request for setting up a tunnel to the LNS if it finds that the user is a VPN user.
* After a tunnel is set up between the NAS and LNS, the NAS sends packets carrying the content negotiated between the NAS and VPN user to the LNS.
* The LNS determines whether to accept the connection according to the negotiation.
* The user communicates with the headquarters through the tunnel between the NAS and the LNS.
* The user accesses the network from the domain **doma1** and obtains an IP address from the address pool **pool1**.

It is required that L2TP tunnel-based QoS scheduling be configured on the LNS. When multiple users go online through the same tunnel, all users in the domain share the CIR of 100 Mbit/s and PIR of 200 Mbit/s.

**Figure 1** Configuring QoS scheduling based on L2TP tunnels for user access  
![](images/fig_dc_ne_l2tp_cfg_01351101.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure the LAC.
2. Configure the LNS. In this example, the NE40E functions as the LNS.
3. Configure a scheduling profile and QoS profile.
4. Apply the QoS profile to the domain.
5. Configure QoS scheduling by L2TP tunnel for the L2TP group.

#### Data Preparation

To complete the configuration, you need the following data:

* Loopback addresses
* Name, subnet, and gateway of an address pool
* Name of a user access domain
* Names of the scheduling profile and QoS profile

#### Procedure

1. Perform configuration on the user side.
   
   
   
   In the dial-up window on the user side, enter **vpdnuser@doma1** as the VPN username, **YsHsjx\_202206** as the password, and 170 as the dial-in number. In the dial-up terminal window that is displayed, enter **username** as the username and **Userpass0** as the password for RADIUS authentication.
2. Configure the NAS.
   
   
   
   The configuration procedure is not provided here. For details, see the related product documentation.
   
   The NAS is used as the LAC.
   
   # Configure the dial-in number on the NAS as 170.
   
   # On the RADIUS server, configure a VPN user whose username is **username** and password is **Userpass0**, and configure an IP address for the LNS (In this case, the IP address of the LNS is 192.168.0.1).
   
   # Set the local device name to **lac** and set the password for tunnel authentication to **1qaz#EDC**.
3. Configure the NE40E that function as the LNS.
   
   
   
   # Create a VT and configure it.
   
   ```
   <Device> system-view
   ```
   ```
   [~Device] interface virtual-template 1
   ```
   ```
   [*Device-Virtual-Template1] ppp authentication-mode chap
   ```
   ```
   [*Device-Virtual-Template1] commit
   ```
   ```
   [~Device-Virtual-Template1] quit
   ```
   
   # Enable the L2TP service and create an L2TP group.
   
   ```
   [~Device] l2tp enable
   ```
   ```
   [*Device] commit
   ```
   ```
   [~Device] l2tp-group lns1
   ```
   
   # Configure an L2TP connection on the LNS.
   
   ```
   [*Device-l2tp-lns1] tunnel name LNS
   ```
   ```
   [*Device-l2tp-lns1] allow l2tp virtual-template 1 remote lac
   ```
   
   # Enable tunnel authentication and set a password for tunnel authentication.
   
   ```
   [*Device-l2tp-lns1] tunnel authentication
   ```
   ```
   [*Device-l2tp-lns1] commit
   ```
   ```
   [~Device-l2tp-lns1] tunnel password cipher YsHsjx_202206
   ```
   ```
   [~Device-l2tp-lns1] quit
   ```
   
   # Configure an address pool to assign addresses to dial-up users.
   
   ```
   [~Device] ip pool pool1 bas local
   ```
   ```
   [*Device-ip-pool-pool1] gateway 10.10.10.1 255.255.255.0
   ```
   ```
   [*Device-ip-pool-pool1] commit
   ```
   ```
   [~Device-ip-pool-pool1] section 0 10.10.10.2 10.10.10.100
   ```
   ```
   [*Device-ip-pool-pool1] commit
   ```
   ```
   [~Device-ip-pool-pool1] quit
   ```
   
   # Configure a RADIUS server group.
   
   ```
   [~Device] radius-server group radius1
   ```
   ```
   [*Device-radius-radius1] radius-server authentication 10.20.20.1 1812
   ```
   ```
   [*Device-radius-radius1] radius-server accounting 10.20.20.1 1813
   ```
   ```
   [*Device-radius-radius1] radius-server shared-key itellin
   ```
   ```
   [*Device-radius-radius1] commit
   ```
   ```
   [~Device-radius-radius1] quit
   ```
   
   # Configure a domain named **doma1**.
   
   ```
   [~Device] aaa
   ```
   ```
   [*Device-aaa] domain doma1
   ```
   ```
   [*Device-aaa-domain-domain1] radius-server group radius1
   ```
   ```
   [*Device-aaa-domain-doma1] authentication-scheme default1
   ```
   ```
   [*Device-aaa-domain-doma1] accounting-scheme default1
   ```
   ```
   [*Device-aaa-domain-doma1] commit
   ```
   ```
   [~Device-aaa-domain-doma1] ip-pool pool1
   ```
   ```
   [~Device-aaa-domain-doma1] quit
   ```
   ```
   [~Device-aaa] quit
   ```
   
   # Configure an IP address for the LNS-side interface.
   
   ```
   [~Device] interface loopback0
   ```
   ```
   [*Device-LoopBack0] ip address 192.168.0.1 255.255.255.255
   ```
   ```
   [*Device-LoopBack0] commit
   ```
   ```
   [~Device-LoopBack0] quit
   ```
   
   # Create an LNS group named **group1**.
   
   ```
   [~Device] lns-group group1
   ```
   
   # Bind the tunnel board in slot 1 to the LNS group.
   
   ```
   [*Device-lns-group-group1] bind slot 1 
   ```
   
   # Bind an interface to the LNS group.
   
   ```
   [*Device-lns-group-group1] bind source loopback0
   ```
   ```
   [*Device-lns-group-group1] commit
   ```
   ```
   [~Device-lns-group-group1] quit
   ```
4. Configure a QoS profile.
   
   
   
   # Configure a QoS profile.
   
   ```
   [~Device] qos-profile pro1
   ```
   ```
   [*Device-qos-pro1] user-queue cir 100000 pir 200000 inbound
   ```
   ```
   [*Device-qos-pro1] user-queue cir 100000 pir 200000 outbound
   ```
   ```
   [*Device-qos-pro1] commit
   ```
   ```
   [~Device-qos-pro1] quit
   ```
5. Apply the QoS profile to the domain.
   
   
   ```
   [~Device] aaa
   ```
   ```
   [*Device-aaa] domain doma1
   ```
   ```
   [*Device-aaa-domain-doma1] qos-profile pro1 inbound lns-gts
   ```
   ```
   [*Device-aaa-domain-doma1] commit
   ```
   ```
   [~Device-aaa-domain-doma1] quit
   ```
   ```
   [~Device-aaa] quit
   ```
6. Configure QoS scheduling by tunnel for the L2TP group.
   
   
   ```
   [~Device] l2tp-group lns1
   ```
   ```
   [*Device-l2tp-lns1] qos scheduling-mode tunnel
   ```
   ```
   [*Device-l2tp-lns1] commit
   ```
   ```
   [~Device-l2tp-lns1] quit
   ```
7. Verify the configuration.
   
   
   
   Run the [**display l2tp-group**](cmdqueryname=display+l2tp-group) command on the LNS. The command output shows that the QoS scheduling mode configured for the L2TP group is **tunnel**.
   
   ```
   <Device> display l2tp-group lns1                                                
    -----------------------------------------------                                
    L2tp-index      : 3                                                            
    Group-Name      : lns1                                                            
    .........
    QOS-mode        : tunnel                                                   
    .........
    -----------------------------------------------                                
   ```
   
   Run the [**display domain**](cmdqueryname=display+domain) command. The command output shows that the QoS profile configured for L2TP users is named **pro1**.
   
   ```
   <Device> display domain doma1                                                
    ------------------------------------------------------------------------------
     Domain-name                     : doma1                                       
     Domain-state                    : Active                                      
   ...............
     L2TP-QosProfile-inbound         : pro1                                        
   ...............
     ------------------------------------------------------------------------------
   ```

#### Configuration Files

```
#
```
```
 sysname Device
```
```
#
```
```
 l2tp enable
```
```
#
```
```
radius-server group radius1
```
```
 radius-server authentication 10.20.20.1 1812 
```
```
 radius-server accounting 10.20.20.1 1813 
```
```
 radius-server shared-key %^%#vS%796FO7%C~pB%CR=q;j}gSCqR-X6+P!.DYI@)%^% 
```
```
#
```
```
qos-profile pro1
```
```
 user-queue cir 100000 pir 200000 inbound
```
```
 user-queue cir 100000 pir 200000 outbound
```
```
#
```
```
interface Virtual-Template1
```
```
 ppp authentication-mode chap 
```
```
#
```
```
interface GigabitEthernet0/1/0
```
```
 undo shutdown 
```
```
#
```
```
interface GigabitEthernet0/1/0.2
```
```
 pppoe-server bind Virtual-Template 1
```
```
 user-vlan 270 277
```
```
 undo shutdown 
```
```
 bas
```
```
  access-type layer2-subscriber
```
```
#
```
```
interface loopback0
```
```
 ip address 192.168.0.1 255.255.255.255
```
```
#
```
```
l2tp-group lns1
```
```
 allow l2tp virtual-template 1 remote lac
```
```
 tunnel password cipher %@%##!!!!!!!!!"!!!!"!!!!(!!!!1];16qfZ81fv"uMoKKZ.1k"`AO!X2K2N.b~'NB^V!!!!!!!!!!1!!!!o/4J(q"J1F.!K9%M!6x8%@%#
```
```
 tunnel name LNS
```
```
 qos scheduling-mode tunnel
```
```
#
```
```
lns-group group1
```
```
 bind slot 1 
```
```
 bind source loopback0
```
```
#
```
```
ip pool pool1 bas local
```
```
 gateway 10.10.10.1 255.255.255.0
```
```
 section 0 10.10.10.2 10.10.10.100
```
```
#
```
```
aaa
```
```
domain  doma1 
```
```
  radius-server group  radius1
```
```
 authentication-scheme default1
```
```
 accounting-scheme default1
```
```
 ip-pool pool1
```
```
 qos-profile pro1 inbound lns-gts
```
```
#
```
```
return
```