Example for Configuring L2TP Access in Client-Initiated VPN Scenarios
=====================================================================

This section provides an example for configuring L2TP in a Client-Initiated VPN scenario. A networking diagram is provided to help you understand the configuration procedure. The configuration example includes the networking requirements, configuration roadmap, configuration procedure, and configuration files.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172374276__fig_dc_ne_l2tp_cfg_01350801), an employee on a business trip connects to the NAS through the PSTN, and the LNS at the headquarters connects to the NAS over the Internet. The networking requirements are as follows:

* The employee needs to initiate a connection request to the LNS, and the communication data with the LNS can be transmitted through the tunnel.
* The LNS verifies the username and password after receiving this connection request, and assigns a private IP address to the LAC user.
* The employee communicates with the company headquarters through the tunnel.
* The user accesses the network from the domain **domain1** and obtains its IP address from the address pool **pool1**.

**Figure 1** Configuring L2TP access in Client-Initiated VPN scenarios  
![](images/fig_dc_ne_l2tp_cfg_01350801.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Install the L2TP client software on the user side and configure the related parameters.
2. Configure the LNS.
   
   * Create a VT.
   * Configure an L2TP group and its attributes.
   * Configure an address pool and a domain.
   * Configure an LNS group and its attributes.

#### Data Preparation

To complete the configuration, you need the following data:

* Username and password on the client and LNS
* Loopback address
* Name, subnet, and gateway of an address pool
* Name of the domain to which the user belongs

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This section provides only the L2TP-related configuration procedure.



#### Procedure

1. Perform configuration on the user side.
   
   # Install the L2TP client software on the user-side host and connect to the Internet through dial-up. Then, perform the following operations (the configuration process is related to the client software):
   * Set the username and password of the VPN on the user side to **vpdnuser** and **YsHsjx\_202206**, respectively.
   * Set the IP address of the LNS to the IP address of the interface connecting the device to the Internet (In this example, the IP address of the interface connecting the LNS to the channel is 10.11.11.1).
   * Modify connection attributes and set the protocol to L2TP.
2. Configure Device that functions as the LNS.
   
   
   
   # Create a VT and configure it.
   
   ```
   <Device> system-view
   ```
   ```
   [~Device] interface virtual-template 1
   ```
   ```
   [*Device-Virtual-Template1] ppp authentication-mode auto
   ```
   ```
   [*Device-Virtual-Template1] commit
   ```
   ```
   [~Device-Virtual-Template1] quit
   ```
   
   # Configure a domain named **domain1**.
   
   ```
   [~Device] aaa
   ```
   ```
   [*Device-aaa] domain domain1
   ```
   ```
   [*Device-aaa-domain-domain1] authentication-scheme default1
   ```
   ```
   [*Device-aaa-domain-domain1] accounting-scheme default1
   ```
   ```
   [*Device-aaa-domain-domain1] radius-server group radius1
   ```
   ```
   [*Device-aaa-domain-domain1] commit
   ```
   ```
   [~Device-aaa-domain-domain1] ip-pool pool1
   ```
   ```
   [~Device-aaa-domain-domain1] quit
   ```
   ```
   [~Device-aaa] quit
   ```
   
   # Enable L2TP and create an L2TP group.
   
   ```
   [~Device] l2tp enable
   ```
   ```
   [*Device] l2tp-group lns1
   ```
   ```
   [*Device-l2tp-lns1] default-domain authentication domain1
   ```
   ```
   [*Device-l2tp-lns1] commit
   ```
   
   # Configure the local tunnel name and remote tunnel name on the LNS side.
   
   ```
   [~Device-l2tp-lns1] tunnel name LNS
   ```
   ```
   [*Device-l2tp-lns1] allow l2tp virtual-template 1 remote vpdnuser
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Except for the default L2TP group **default-lns**, *remote lac-name* must be specified for other L2TP groups when L2TP connections are configured on the LNS. If the tunnel name sent by the LAC does not match the remote tunnel names configured for other L2TP groups, **default-lns** is used as the L2TP group.
   
   *remote lac-name* is the same as [**tunnel name**](cmdqueryname=tunnel+name) configured on the LAC. If this parameter is not configured, the hostname of the device is used.
   
   # Enable tunnel authentication and configure a password for tunnel authentication.
   
   ```
   [*Device-l2tp-lns1] tunnel authentication
   ```
   ```
   [*Device-l2tp-lns1] tunnel password cipher YsHsjx_202206
   ```
   ```
   [*Device-l2tp-lns1] commit
   ```
   ```
   [~Device-l2tp-lns1] quit
   ```
   # Configure an address pool to assign addresses to dialup users.
   ```
   [~Device] ip pool pool1 bas local
   ```
   ```
   [*Device-ip-pool-pool1] gateway 192.168.0.2 255.255.255.0
   ```
   ```
   [*Device-ip-pool-pool1] commit
   ```
   ```
   [~Device-ip-pool-pool1] section 0 192.168.0.10 192.168.0.100
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
   
   # Configure loopback0.
   
   ```
   [~Device] interface loopback 0
   ```
   ```
   [*Device-LoopBack0] ip address 192.168.10.1 255.255.255.255
   ```
   ```
   [*Device-LoopBack0] commit
   ```
   ```
   [~Device-LoopBack0] quit
   ```
   
   # Create an LNS group named **group1**, and bind a tunnel board and loopback interface to the LNS group.
   
   ```
   [~Device] lns-group group1
   ```
   ```
   [*Device-lns-group-group1] bind slot 1 
   ```
   ```
   [*Device-lns-group-group1] bind source loopback 0
   ```
   ```
   [*Device-lns-group-group1] commit
   ```
   ```
   [~Device-lns-group-group1] quit
   ```
3. Verify the configuration.
   
   
   
   # After completing the configuration, run the **display l2tp tunnel** command on the LNS after the VPN user goes online. The command output shows that the tunnel is established successfully.
   
   ```
   [~Device] display l2tp tunnel lns slot 1
   ```
   ```
   LocalTID RemoteTID RemoteAddress    Port   Sessions RemoteName 
   ```
   ```
    ------------------------------------------------------------------------------       
   ```
   ```
   1        1         10.1.1.1        2134   1        vpdnuser
   ```
   ```
    ------------------------------------------------------------------------------       
   ```
   ```
   Total 1, 1 printed from slot 1 
   ```
   
   # Run the **display l2tp session** command on the LNS to check the session setup status.
   
   ```
   <Device> display l2tp session lns slot 1 
   ```
   ```
   LocalSID  RemoteSID  LocalTID   RemoteTID  UserID  UserName                                                                       
    ------------------------------------------------------------------------------                                                     
     278       24768      13921      7958       62172    vpdnuser@domain1                                                                   
    ------------------------------------------------------------------------------       
   ```
   ```
   Total 1, 1 printed from slot 1 
   ```
   
   # Check that the VPN user can access the headquarters.

#### Configuration Files

Device configuration file

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
#
```
```
 radius-server shared-key %^%#vS%796FO7%C~pB%CR=q;j}gSCqR-X6+P!.DYI@)%^%
```
```
#
```
```
 radius-server authentication 10.20.20.1 1812 
```
```
 radius-server accounting 10.20.20.1 1813 
```
```
#
```
```
ip pool pool1 bas local
```
```
 gateway 192.168.0.2 255.255.255.0
```
```
 section 0 192.168.0.10 192.168.0.100
```
```
#
```
```
interface Virtual-Template1
```
```
 ppp authentication-mode auto 
```
```
#
```
```
aaa
```
```
domain domain1 
```
```
  authentication-scheme default1
```
```
  accounting-scheme default1
```
```
  radius-server group radius1
```
```
  ip-pool pool1
```
```
#
```
```
interface LoopBack0
```
```
 ip address 192.168.10.1 255.255.255.255
```
```
#
```
```
l2tp-group lns1
```
```
 allow l2tp virtual-template 1 remote vpdnuser
```
```
 default-domain authentication domain1
```
```
 tunnel password cipher %@%##!!!!!!!!!"!!!!"!!!!(!!!!1];16qfZ81fv"uMoKKZ.1k"`AO!X2K2N.b~'NB^V!!!!!!!!!!1!!!!o/4J(q"J1F.!K9%M!6x8%@%#
```
```
 tunnel name LNS
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
 bind source LoopBack0
```
```
#
```
```
return
```