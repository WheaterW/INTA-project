Example for Configuring RADIUS for Dynamic ACL Delivery
=======================================================

This section provides an example for configuring RADIUS for dynamic ACL delivery.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172373748__fig_dc_ne_aaa_cfg_040101), users access the network through DeviceA and belong to the domain **huawei**. DeviceB functions as the access server on the destination network. To access the destination network, the users need to traverse the network where DeviceA and DeviceB reside. They can access the network through DeviceB after passing remote authentication on the RADIUS server. Remote authentication on DeviceB is as follows:

* RADIUS servers are used to authenticate access users.
* The RADIUS server at 10.7.66.66/24 functions as the primary authentication server, and the RADIUS server at 10.7.66.67/24 functions as the secondary authentication server. The default authentication port number is 1812.

**Figure 1** Configuring dynamic ACL delivery  
![](images/fig_dc_ne_aaa_cfg_040101.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a RADIUS server group, an authentication scheme, and a dynamic ACL delivery scheme.
2. Bind the RADIUS server group, authentication scheme, and dynamic ACL delivery scheme to the domain.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Run the [**adminuser-priority**](cmdqueryname=adminuser-priority) command in the view of a domain (not the default\_admin domain) to which a user belongs if you want to configure this user to log in as an administrator. The domain must be configured as the authentication domain for BAS access users.



#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of the primary and secondary RADIUS authentication servers
* RADIUS authentication is performed for users on DeviceB.

#### Procedure

1. Configure a RADIUS server group, an authentication scheme, and a dynamic ACL delivery scheme.
   
   
   
   # Configure a RADIUS server group named **shiva**.
   
   ```
   <Device> system-view
   ```
   ```
   [~Device] radius-server group shiva
   ```
   
   # Configure an IP address and a port number for the primary RADIUS authentication server.
   
   ```
   [*Device-radius-shiva] radius-server authentication 10.7.66.66 1812
   ```
   
   # Configure an IP address and a port number for the secondary RADIUS authentication server.
   
   ```
   [*Device-radius-shiva] radius-server authentication 10.7.66.67 1812
   ```
   
   # Configure a shared key and the number of retransmissions for the RADIUS server.
   
   ```
   [*Device-radius-shiva] radius-server shared-key-cipher YsHsjx_202206
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
   
   # Configure dynamic ACL delivery through the RADIUS server.
   
   ```
   [~Device] aaa
   ```
   ```
   [~Device-aaa] remote-download acl enable
   ```
   
   # Configure authentication scheme 1, with the authentication mode being RADIUS.
   
   ```
   [*Device-aaa] authentication-scheme 1
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
2. Configure a domain named **huawei** and bind authentication scheme 1 and RADIUS server group **shiva** to the domain.
   
   
   ```
   [~Device-aaa] domain huawei
   ```
   ```
   [*Device-aaa-domain-huawei] authentication-scheme 1
   ```
   ```
   [*Device-aaa-domain-huawei] radius-server group shiva
   ```
   ```
   [*Device-aaa-domain-huawei] commit
   ```
   ```
   [~Device-aaa-domain-huawei] quit
   ```
3. Configure user templates and BAS interfaces.
   
   
   ```
   [~Device-aaa] default-password template huawei cipher YsHsjx_202207
   ```
   ```
   [*Device-aaa] default-user-name template huawei include sysname
   ```
   ```
   [*Device-aaa] commit
   ```
   ```
   [~Device-aaa] quit
   ```
   
   
   ```
   [~Device] interface GigabitEthernet 0/1/1.1 
   ```
   ```
   [*Device-GigabitEthernet0/1/1.1] commit
   ```
   ```
   [~Device-GigabitEthernet0/1/1.1] user-vlan 1
   ```
   ```
   [*Device-GigabitEthernet0/1/1.1-vlan-1-1] quit
   ```
   ```
   [*Device-GigabitEthernet0/1/1.1] bas
   ```
   ```
   [*Device-GigabitEthernet0/1/1.1-bas] access-type layer2-subscriber default-domain authentication huawei
   ```
   ```
   [*Device-GigabitEthernet0/1/1.1-bas] authentication-method bind
   ```
   ```
   [*Device-GigabitEthernet0/1/1.1-bas] user detect retransmit 2 interval 0 
   ```
   ```
   [*Device-GigabitEthernet0/1/1.1-bas] default-user-name-template huawei
   ```
   ```
   [*Device-GigabitEthernet0/1/1.1-bas] commit
   ```
   ```
   [~Device-GigabitEthernet0/1/1.1-bas] default-password-template huawei 
   ```
   ```
   [*Device-GigabitEthernet0/1/1.1-bas] quit
   ```
   ```
   [~Device-GigabitEthernet0/1/1.1] commit
   ```
   ```
   [~Device-GigabitEthernet0/1/1.1] quit
   ```
4. Verify the configuration. 
   
   
   
   Run the **display aaa remote-download acl item verbose** command on the Router. The command output shows that the RADIUS server group configurations meet the requirements.
   
   ```
   <Device> display aaa remote-download acl item verbose
   ```
   ```
   -------------------------------------------------------------------------------
    ClassifierName                    ReferedNumByUser  RuleNumber  ClassifierType
   -------------------------------------------------------------------------------
    c1                                1                 1           remote
   -------------------------------------------------------------------------------
    rc=c1;
      rule:(number: 1)
        ipv4;ruleid=5;dir=in;su-group=huawei;dipv4=10.1.0.1/24;
    rb=b1;
        deny;
    The used user-id table are : 
     0
   -------------------------------------------------------------------------------
    Total Classifier-Behavior Number : 1 
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
user-group huawei
#                                                                                
radius-server group shiva                                                       
 radius-server authentication 10.7.66.66 1812 weight 0                         
 radius-server authentication 10.7.66.67 1812 weight 0                                                    
 radius-server shared-key-cipher %^%#h{FXVBLZX9#`VI]EWUUaOSHGd5E!.1DGeVYEie=%^%                                       
 radius-server retransmit 2                                                  
#                                                                               
aaa 
 remote-download acl enable
 default-password template huawei cipher %^%#M*p1,itN!4kQo5%Dc1s(whyJCM@xt0u[,,XMWG/O%^%
 default-user-name template huawei include sysname                                                                            
 #
 authentication-scheme 1                                                        
 #                                                                              
 authorization-scheme default                                                                                                      
 #                                                                              
 domain huawei                                                                   
  authentication-scheme 1                                                                                                                    
  radius-server group shiva   
  ip-pool huawei
  user-group huawei 
#
interface GigabitEthernet0/1/1
#
interface GigabitEthernet0/1/1.1
 user-vlan 1
 bas
 #
  access-type layer2-subscriber default-domain authentication huawei
  authentication-method bind
  user detect retransmit 2 interval 0
  default-user-name-template huawei
  default-password-template huawei
#
#  
return                                                                                            
```