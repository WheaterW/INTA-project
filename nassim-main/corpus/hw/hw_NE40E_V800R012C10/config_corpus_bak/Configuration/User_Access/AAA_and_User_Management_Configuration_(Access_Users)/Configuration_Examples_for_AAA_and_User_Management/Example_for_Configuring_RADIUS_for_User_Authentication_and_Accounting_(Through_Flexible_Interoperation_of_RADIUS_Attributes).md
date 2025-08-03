Example for Configuring RADIUS for User Authentication and Accounting (Through Flexible Interoperation of RADIUS Attributes)
============================================================================================================================

This section provides an example for configuring RADIUS for user authentication and accounting. When a Huawei device interworks with a RADIUS server, the RADIUS attributes supported by the two devices may be different. Python scripts can be loaded to implement flexible interoperation of RADIUS attributes.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172373749__fig_dc_ne_aaa_cfg_040101), users access the network through DeviceA and belong to the domain **huawei**. DeviceB functions as the access server on the destination network. To access the destination network, the users need to traverse the network where DeviceA and DeviceB reside. They can access the network through DeviceB after passing remote authentication on the RADIUS server. Remote authentication on DeviceB is as follows:

* The RADIUS server performs authentication and accounting for access users.
* The RADIUS server at 10.7.66.66/24 functions as the active authentication and accounting server, and the RADIUS server at 10.7.66.67/24 functions as the standby authentication and accounting server. The default authentication port number is 1812, and the default accounting port number is 1813.

However, when DeviceB interworks with the RADIUS server, the attributes carried in authentication and accounting request packets are not all the same. Therefore, you need to load the python script package to implement flexible interoperation of RADIUS attributes.

**Figure 1** Configuring RADIUS for user authentication and accounting  
![](images/fig_dc_ne_aaa_cfg_040101.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a RADIUS server group, an authentication scheme, and an accounting scheme.
2. Bind the RADIUS server group, authentication scheme, and accounting scheme to a domain.
3. Load the python script package.
4. Configure a python policy template.
5. Bind the python policy template to the RADIUS server group.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The python script package must have been uploaded to the cfcard: directory.



#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of the active and standby RADIUS authentication servers
* IP addresses of the active and standby RADIUS accounting servers
* Python script package
* access-request.py, the python script that processes Access-Request packets
* acct-request.py, the python script that processes Accounting-Request packets
* RADIUS authentication is performed for users on DeviceB.

#### Procedure

1. Configure a RADIUS server group, an authentication scheme, and an accounting scheme.
   
   
   
   # Configure a RADIUS server group named **shiva**.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname Device
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~Device] radius-server group shiva
   ```
   
   # Configure an IP address and port numbers for the active RADIUS authentication and accounting server.
   
   ```
   [*Device-radius-shiva] radius-server authentication 10.7.66.66 1812
   ```
   ```
   [*Device-radius-shiva] radius-server accounting 10.7.66.66 1813
   ```
   
   # Configure an IP address and port numbers for the standby RADIUS authentication and accounting server.
   
   ```
   [*Device-radius-shiva] radius-server authentication 10.7.66.67 1812
   ```
   ```
   [*Device-radius-shiva] radius-server accounting 10.7.66.67 1813
   ```
   
   # Configure a shared key and the number of retransmissions for the RADIUS server.
   
   ```
   [*Device-radius-shiva] radius-server shared-key-cipher it-is-my-secret1
   ```
   ```
   [*Device-radius-shiva] radius-server retransmit 2
   ```
   ```
   [*Device-radius-shiva] commit
   ```
   ```
   [~Device-radius-shiva] quit
   ```
   
   # Enter the AAA view.
   
   ```
   [~Device] aaa
   ```
   
   # Configure authentication scheme 1, with the authentication mode being RADIUS.
   
   ```
   [~Device-aaa] authentication-scheme 1
   ```
   ```
   [*Device-aaa-authen-1] authentication-mode radius
   ```
   ```
   [*Device-aaa-authen-1] commit
   ```
   ```
   [~Device-aaa-authen-1] quit
   ```
   
   # Configure accounting scheme 1, with the accounting mode being RADIUS.
   
   ```
   [~Device-aaa] accounting-scheme 1
   ```
   ```
   [*Device-aaa-accounting-1] accounting-mode radius
   ```
   ```
   [*Device-aaa-accounting-1] commit
   ```
   ```
   [~Device-aaa-accounting-1] quit
   ```
2. Configure a domain named **huawei** and bind authentication scheme 1, accounting scheme 1, and RADIUS server group **shiva** to the domain.
   
   
   ```
   [~Device-aaa] domain huawei
   ```
   ```
   [*Device-aaa-domain-huawei] authentication-scheme 1
   ```
   ```
   [*Device-aaa-domain-huawei] accounting-scheme 1
   ```
   ```
   [*Device-aaa-domain-huawei] radius-server group shiva
   ```
   ```
   [*Device-aaa-domain-huawei] commit
   ```
   ```
   [~Device-aaa] quit
   ```
   ```
   [~Device-aaa] quit
   ```
3. Enable the python script extension function.
   
   
   ```
   [~Device] access enable python extend script-package V800R023C00SPC500.zip
   ```
   ```
   [*Device] commit
   ```
4. Configure a python policy template for packet processing.
   
   
   
   # Create a python policy template.
   
   ```
   [~Device] access python-policy py
   ```
   ```
   [*Device-python-policy py] commit
   ```
   
   # Configure the association between packets and scripts in the python policy template named **py**.
   
   ```
   [~Device-python-policy py] protocol radius packet access-request direction egress python-script access-request.py
   ```
   ```
   [*Device-python-policy py] protocol radius packet accounting-request direction egress python-script acct-request.py
   ```
   ```
   [*Device-python-policy py] protocol radius packet process-fail passthrough
   ```
   ```
   [*Device-python-policy py] commit
   ```
   ```
   [~Device-python-policy py] quit
   ```
5. Bind the RADIUS server group to the python policy template.
   
   
   ```
   [~Device] radius-server group shiva
   ```
   ```
   [*Device-radius-shiva] python-policy py
   ```
   ```
   [*Device-radius-shiva] commit
   ```
   ```
   [~Device-radius-shiva] quit
   ```
   ```
   [~Device] quit
   ```
6. Verify the configuration.
   
   
   
   # Run the **display radius-server configuration group shiva** command on the Router. The command output shows that the RADIUS server group configurations meet the requirements.
   
   ```
   <Device> display radius-server configuration group shiva
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
   
   # Run the **display domain** *domain-name* command on the Router to check domain configurations.
   
   ```
   <Device> display domain huawei
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
     Value-added-service             : default
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
   
   # Run the **display access python-script information** command on the Router to check related information about the loaded python script package.
   
   ```
   <Device> display access python-script information
   ```
   ```
     Script Package Name                       : cfcard:/V800R023C00SPC500.zip
     Script Package Version                    : V800R023C00SPC500
     Script Package Run Time                   : 2018-05-21 05:06:22
     Script Info:
     ---------------------------------------------------------------
     ScriptName                                State
     ---------------------------------------------------------------
     acct-request.py                           Running
     access-request.py                         Running
     ---------------------------------------------------------------
     Total = 2
   
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
radius-server group shiva                                                       
 radius-server authentication 10.7.66.66 1812 weight 0                         
 radius-server authentication 10.7.66.67 1812 weight 0                         
 radius-server accounting 10.7.66.66 1813 weight 0                             
 radius-server accounting 10.7.66.67 1813 weight 0                             
 radius-server shared-key-cipher %^%#h{FXVBLZX9#`VI]EWUUaOSHGd5E!.1DGeVYEie=%^%                                       
 radius-server retransmit 2                                                    
 python-policy py
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
#
access enable python extend script-package cfcard:/V800R023C00SPC500c.zip
#
access python-policy py
 protocol radius packet access-request direction egress python-script access-request.py
 protocol radius packet accounting-request direction egress python-script acct-request.py
#
```
```
return
```