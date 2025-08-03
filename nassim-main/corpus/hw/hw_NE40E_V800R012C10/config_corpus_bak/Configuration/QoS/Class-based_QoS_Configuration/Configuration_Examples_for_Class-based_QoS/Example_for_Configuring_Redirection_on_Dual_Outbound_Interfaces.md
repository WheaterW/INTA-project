Example for Configuring Redirection on Dual Outbound Interfaces
===============================================================

This section provides an example for configuring redirection on dual outbound interfaces.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172371300__fig_dc_ne_qos_cfg_007501), DeviceA connects to the intranet through interface1 and connects to the public network through interface2 and interface3. By default, traffic from the intranet is transmitted to the public network through interface3. To enable traffic from the server to be transmitted to the public network through interface2 and other traffic to the public network through interface3, configure a traffic policy on DeviceA.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

interface1, interface2, and interface3 in this example represent GE 0/1/0, GE 0/2/0, and GE 0/3/0, respectively.


**Figure 1** Configuring redirection on dual outbound interfaces  
![](images/fig_dc_ne_qos_cfg_007501.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a default route.
2. Configure ACL rules.
3. Configure traffic classifiers.
4. Configure traffic behaviors.
5. Configure a traffic policy.
6. Apply the traffic policy.

#### Data Preparation

To complete the configuration, you need the following data:

* ACL numbers
* Names of the traffic classifier, traffic behavior, and traffic policy, and number of the interface to which the traffic policy is applied

#### Procedure

1. Configure a default route so that intranet traffic is transmitted to the public network through interface3 by default and interface2 is used as the backup outbound interface.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] ip route-static 0.0.0.0 0.0.0.0 10.1.99.1
   ```
   ```
   [*HUAWEI] ip route-static 0.0.0.0 0.0.0.0 10.1.99.5 preference 70
   ```
   ```
   [*HUAWEI] commit
   ```
2. Configure ACL rules.
   
   
   
   # Configure ACL 3001 to match the traffic from the server to other devices on the intranet.
   
   ```
   [~HUAWEI] acl number 3001
   ```
   ```
   [*HUAWEI-acl-advance-3001] rule 5 permit ip source 10.1.40.0 0.0.0.255 destination 10.1.40.0 0.0.0.255
   ```
   ```
   [*HUAWEI-acl-advance-3001] rule 10 permit ip source 10.1.40.0 0.0.0.255 destination 10.1.41.0 0.0.0.255 
   ```
   ```
   [*HUAWEI-acl-advance-3001] rule 15 permit ip source 10.1.40.0 0.0.0.255 destination 10.1.42.0 0.0.0.255 
   ```
   ```
   [*HUAWEI-acl-advance-3001] commit
   ```
   ```
   [~HUAWEI-acl-advance-3001] quit
   ```
   
   # Configure ACL 3002 to match the traffic with the source address being the IP address of the server.
   
   ```
   [~HUAWEI] acl number 3002
   ```
   ```
   [*HUAWEI-acl-advance-3002] rule 5 permit ip source 10.1.40.0 0.0.0.255
   ```
   ```
   [*HUAWEI-acl-advance-3002] commit
   ```
   ```
   [~HUAWEI-acl-advance-3002] quit
   ```
3. Configure traffic classifiers.
   
   
   
   # Configure a traffic classifier named **c1**.
   
   ```
   [~HUAWEI] traffic classifier c1
   ```
   ```
   [*HUAWEI-classifier-c1] if-match acl 3001
   ```
   ```
   [*HUAWEI-classifier-c1] commit
   ```
   ```
   [~HUAWEI-classifier-c1] quit
   ```
   
   # Configure a traffic classifier named **c2**.
   
   ```
   [~HUAWEI]traffic classifier c2
   ```
   ```
   [*HUAWEI-classifier-c2] if-match acl 3002
   ```
   ```
   [*HUAWEI-classifier-c2] commit
   ```
   ```
   [~HUAWEI-classifier-c2] quit
   ```
4. Configure traffic behaviors.
   
   
   
   # Configure a traffic behavior named **b1**.
   
   ```
   [~HUAWEI]traffic behavior b1
   ```
   ```
   [*HUAWEI-behavior-b1] permit
   ```
   ```
   [*HUAWEI-behavior-b1] commit
   ```
   ```
   [~HUAWEI-behavior-b1] quit
   ```
   
   # Configure a traffic behavior named **b2**.
   
   ```
   [~HUAWEI] traffic behavior b2
   ```
   ```
   [*HUAWEI-behavior-b2] redirect ip-nexthop 10.1.99.5
   ```
   ```
   [*HUAWEI-behavior-b2] commit
   ```
   ```
   [~HUAWEI-behavior-b2] quit
   ```
5. Configure a traffic policy.
   
   
   ```
   [~HUAWEI] traffic policy p1
   ```
   ```
   [*HUAWEI-trafficpolicy-p1] classifier c1 behavior b1
   ```
   ```
   [*HUAWEI-trafficpolicy-p1] classifier c2 behavior b2
   ```
   ```
   [*HUAWEI-trafficpolicy-p1] commit
   ```
   ```
   [~HUAWEI-trafficpolicy-p1] quit
   ```
6. Apply the traffic policy.
   
   
   ```
   [~HUAWEI] interface gigabitethernet 0/1/0
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0] traffic-policy p1 inbound
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/0] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0] quit
   ```
7. Verify the configuration.
   
   
   
   After completing the configuration, run the **display traffic policy** command on DeviceA to check the configurations of the traffic policy, traffic classifier, and traffic behavior.
   
   ```
   [~HUAWEI] display traffic policy user-defined p1
     User Defined Traffic Policy Information:                                      
       Policy: p1                                                                  
         Total: 5120  Used: 3  Free: 5117                                          
         Description:                                                              
         Step: 1                                                                   
         Share-mode                                                                
         Classifier: c1 Precedence: 1                                              
           Behavior: b1                                                            
           -none-                                                                  
                                                                                   
         Classifier: c2 Precedence: 2                                              
           Behavior: b2                                                            
           Redirecting:                                                            
             redirect ip-nexthop 10.1.99.5                                         
                                                                                   
         Classifier: default-class Precedence: 65535                               
           Behavior: be                                                            
           -none-                              
   ```

#### Configuration Files

HUAWEI configuration file

```
#
sysname HUAWEI
#
ip route-static 0.0.0.0 0.0.0.0 10.1.99.1     
ip route-static 0.0.0.0 0.0.0.0 10.1.99.5 preference 70  
#
acl number 3001
 rule 5 permit ip source 10.1.40.0 0.0.0.255 destination 10.1.40.0 0.0.0.255    
 rule 10 permit ip source 10.1.40.0 0.0.0.255 destination 10.1.41.0 0.0.0.255    
 rule 15 permit ip source 10.1.40.0 0.0.0.255 destination 10.1.42.0 0.0.0.255
acl number 3002
 rule 5 permit ip source 10.1.40.0 0.0.0.255                   
#
traffic classifier c1 operator or
 if-match acl 3001
traffic classifier c2 operator or
 if-match acl 3002
#
traffic behavior b1                    
traffic behavior b2
 redirect ip-nexthop 10.1.99.5   
#
traffic policy p1
 classifier c1 behavior b1 precedence 1      
 classifier c2 behavior b2 precedence 1            
#
interface gigabitethernet0/1/0
 undo shutdown
 traffic-policy p1 inbound
#
return
```