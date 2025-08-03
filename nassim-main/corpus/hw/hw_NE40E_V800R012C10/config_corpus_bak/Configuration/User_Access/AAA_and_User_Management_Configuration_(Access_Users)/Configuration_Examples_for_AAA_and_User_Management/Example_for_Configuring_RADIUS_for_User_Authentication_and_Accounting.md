Example for Configuring RADIUS for User Authentication and Accounting
=====================================================================

This section provides an example for configuring RADIUS for user authentication and accounting.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172373745__fig_dc_ne_aaa_cfg_040101), users access the network through DeviceA and belong to the domain **huawei**. DeviceB functions as the access server on the destination network. To access the destination network, the users need to traverse the network where DeviceA and DeviceB reside. They can access the network through DeviceB after passing remote authentication on the RADIUS server. Remote authentication on DeviceB is as follows:

* The RADIUS server performs authentication and accounting for access users.
* The RADIUS server at 10.7.66.66/24 functions as the primary authentication and accounting server, and the RADIUS server at 10.7.66.67/24 functions as the secondary authentication and accounting server. The default authentication port number is 1812, and the default accounting port number is 1813.

**Figure 1** Configuring RADIUS for user authentication and accounting  
![](images/fig_dc_ne_aaa_cfg_040101.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a RADIUS server group, an authentication scheme, and an accounting scheme.
2. Bind the RADIUS server group, authentication scheme, and accounting scheme to a domain.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Run the [**adminuser-priority**](cmdqueryname=adminuser-priority) command in the view of a domain (not the default\_admin domain) to which a user belongs if you want to configure this user to log in as an administrator. The domain must be configured as the authentication domain for BAS access users.



#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of the primary and secondary RADIUS authentication servers
* IP addresses of the primary and secondary RADIUS accounting servers
* RADIUS authentication is performed for users on DeviceB.

#### Procedure

1. Set the host name of the BRAS to **HUAWEI**.
   
   
   ```
   <Device> system-view
   ```
   ```
   [~Device] sysname HUAWEI
   ```
   ```
   [*Device] commit
   ```
2. Configure a RADIUS server group, an authentication scheme, and an accounting scheme.
   
   
   
   # Configure a RADIUS server group named **shiva**.
   
   ```
   [~HUAWEI] radius-server group shiva
   ```
   
   # Configure an IP address and port numbers for the primary RADIUS authentication and accounting server.
   
   ```
   [*HUAWEI-radius-shiva] radius-server authentication 10.7.66.66 1812
   ```
   ```
   [*HUAWEI-radius-shiva] radius-server accounting 10.7.66.66 1813
   ```
   
   # Configure an IP address and port numbers for the secondary RADIUS authentication and accounting server.
   
   ```
   [*HUAWEI-radius-shiva] radius-server authentication 10.7.66.67 1812
   ```
   ```
   [*HUAWEI-radius-shiva] radius-server accounting 10.7.66.67 1813
   ```
   
   # Configure a shared key and the number of retransmissions for the RADIUS server.
   
   ```
   [*HUAWEI-radius-shiva] radius-server shared-key-cipher YsHsjx_202206
   ```
   ```
   [*HUAWEI-radius-shiva] radius-server retransmit 2
   ```
   ```
   [*HUAWEI-radius-shiva] commit
   ```
   ```
   [~HUAWEI-radius-shiva] quit
   ```
   
   # Enter the AAA view.
   
   ```
   [~HUAWEI] aaa
   ```
   
   # Configure authentication scheme 1, with the authentication mode being RADIUS.
   
   ```
   [~HUAWEI-aaa] authentication-scheme 1
   ```
   ```
   [*HUAWEI-aaa-authen-1] authentication-mode radius
   ```
   ```
   [*HUAWEI-aaa-authen-1] commit
   ```
   ```
   [~HUAWEI-aaa-authen-1] quit
   ```
   
   # Configure accounting scheme 1, with the accounting mode being RADIUS.
   
   ```
   [~HUAWEI-aaa] accounting-scheme 1
   ```
   ```
   [*HUAWEI-aaa-accounting-1] accounting-mode radius
   ```
   ```
   [*HUAWEI-aaa-accounting-1] commit
   ```
   ```
   [~HUAWEI-aaa-accounting-1] quit
   ```
3. Configure a domain named **huawei** and bind authentication scheme 1, accounting scheme 1, and RADIUS server group **shiva** to the domain.
   
   
   ```
   [~HUAWEI-aaa] domain huawei
   ```
   ```
   [*HUAWEI-aaa-domain-huawei] authentication-scheme 1
   ```
   ```
   [*HUAWEI-aaa-domain-huawei] accounting-scheme 1
   ```
   ```
   [*HUAWEI-aaa-domain-huawei] radius-server group shiva
   ```
   ```
   [*HUAWEI-aaa-domain-huawei] commit
   ```
   ```
   [~HUAWEI-aaa-domain-huawei] quit
   ```
   ```
   [~HUAWEI-aaa] quit
   ```
   ```
   [~HUAWEI] quit
   ```
4. Verify the configuration. 
   
   
   
   Run the **display radius-server configuration group shiva** command on the Router. The command output shows that the RADIUS server group configurations meet the requirements.
   
   ```
   <HUAWEI> display radius-server configuration group shiva
   ```
   ```
     -------------------------------------------------------
     Server-group-name    :  shiva
     Authentication-server:  IP:10.7.66.66 Port:1812 Weight[0] [UP]
                             Vpn: -
     Authentication-server:  IP:10.7.66.67 Port:1812 Weight[0] [UP]
                             Vpn: -
     Authentication-server:  -
     Authentication-server:  -
     Authentication-server:  -
     Authentication-server:  -
     Authentication-server:  -
     Authentication-server:  -
     Accounting-server    :  IP:10.7.66.66 Port:1813 Weight[0] [UP]
                             Vpn: -
     Accounting-server    :  IP:10.7.66.67 Port:1813 Weight[0] [UP]
                             Vpn: -
     Accounting-server    :  -
     Accounting-server    :  -
     Accounting-server    :  -
     Accounting-server    :  -
     Accounting-server    :  -
     Accounting-server    :  -
     Protocol-version     :  radius
     Shared-secret-key    :  ******
     Retransmission       :  2
     Timeout-interval(s)  :  5
     Acct-Stop-Packet Resend  :  NO
     Acct-Stop-Packet Resend-Times  :  0
     Traffic-unit         :  B
     ClassAsCar           :  NO
     User-name-format     :  Domain-included
     Option82 parse mode  :  -
     Attribute-translation:  NO
     Packet send algorithm:  Master-Backup
     Tunnel password      :  cipher
   
   ```
   
   Run the **display domain** *domain-name* command on the Router to check domain configurations.
   
   ```
   <HUAWEI> display domain huawei
   ```
   ```
     ------------------------------------------------------------------------------
     Domain-name                     : huawei
     Domain-state                    : Active
     Authentication-scheme-name      : 1
     Accounting-scheme-name          : 1
     Authorization-scheme-name       :
     Primary-DNS-IP-address          : -
     Second-DNS-IP-address           : -
     Primary-NBNS-IP-address         : -
     Second-NBNS-IP-address          : -
     User-group-name                 : -
     Idle-data-attribute (time,flow) : 0, 60
     Install-BOD-Count               : 0
     Report-VSM-User-Count           : 0
     Value-added-service             : -
     User-access-limit               : 279552
     Online-number                   : 0
     Web-IP-address                  : -
     Web-URL                         : -
     Portal-server-IP                : -
     Portal-URL                      : -
     Portal-force-times              : 2
     PPPoE-user-URL                  : Disable
     IPUser-ReAuth-Time(second)      : 300
     Ancp auto qos adapt             : Disable
     RADIUS-server-template          : shiva
     Two-acct-template               : -
     HWTACACS-server-template        : -
     Bill Flow                       : Disable
     Tunnel-acct-2867                : Disabled
   
     Flow Statistic:
     Flow-Statistic-Up               : Yes
     Flow-Statistic-Down             : Yes
     Source-IP-route                 : Disable
     IP-warning-threshold            : -
     Multicast Forwarding            : Yes
     Multicast Virtual               : No
     Max-multilist num               : 4
     Multicast-profile               : -
     Quota-out                     : Offline
     ------------------------------------------------------------------------------
   
   ```

#### Configuration Files

```
#
```
```
sysname HUAWEI
```
```
#                                                                               
radius-server group shiva                                                       
 radius-server authentication 10.7.66.66 1812 weight 0                         
 radius-server authentication 10.7.66.67 1812 weight 0                         
 radius-server accounting 10.7.66.66 1813 weight 0                             
 radius-server accounting 10.7.66.67 1813 weight 0                             
 radius-server shared-key-cipher %^%#h{FXVBLZX9#`VI]EWUUaOSHGd5E!.1DGeVYEie=%^%                                       
 radius-server retransmit 2                                                    
#                                                                               
aaa                                                                             
  authentication-scheme 1                                                        
  authentication-mode radius                                                   
 #                                                                              
 authorization-scheme default                                                   
 #                                                                              
  accounting-scheme 1                                                            
  accounting-mode radius                                                        
 #                                                                              
 domain huawei                                                                   
  authentication-scheme 1                                                        
  accounting-scheme 1                                                            
  radius-server group shiva                                                     

```
```
#
```
```
return
```