Example for Using Advanced ACLs to Prevent User Hosts on Different Network Segments from Communicating
======================================================================================================

Example for Using Advanced ACLs to Prevent User Hosts on Different Network Segments from Communicating

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0251067105__fig224411471769), the departments of a company are connected through Device. To facilitate network management, the administrator plans IP addresses of different network segments for the R&D and marketing departments. In addition, the administrator adds the two departments to different VLANs for broadcast domain isolation. The company requires that Device prevent the user hosts on different network segments from communicating to ensure information security.

**Figure 1** Example for using advanced ACLs to prevent user hosts on different network segments from communicating![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent VLANIF 10 and VLANIF 20, respectively.


  
![](figure/en-us_image_0251079856.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an advanced ACL and ACL-based traffic classifier to filter the packets exchanged between the R&D and marketing departments.
2. Configure a traffic behavior to deny the packets matching the ACL rules.
3. Configure and apply a traffic policy for the ACL and traffic behavior to take effect.

#### Procedure

1. Configure VLANs to which interfaces belong and allocate IP addresses to VLANIF interfaces.
   
   
   
   # Configure VLAN 10 and VLAN 20.
   
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
   [~Device] vlan batch 10 20
   ```
   ```
   [*Device] commit
   ```
   ```
   [~Device] quit
   ```
   
   # Configure interfaces 1 and 2 on Device as trunk interfaces and add them to VLAN 10 and VLAN 20, respectively.
   
   ```
   [~Device] interface gigabitethernet 0/1/0
   ```
   ```
   [~Device-GigabitEthernet0/1/0] port link-type trunk
   ```
   ```
   [~Device-GigabitEthernet0/1/0] port trunk allow-pass vlan 10
   ```
   ```
   [~Device-GigabitEthernet0/1/0] quit
   ```
   ```
   [~Device] interface gigabitethernet 0/2/0
   ```
   ```
   [~Device-GigabitEthernet0/2/0] port link-type trunk
   ```
   ```
   [~Device-GigabitEthernet0/2/0] port trunk allow-pass vlan 20
   ```
   ```
   [~Device-GigabitEthernet0/2/0] quit
   ```
   ```
   [*Device] commit
   ```
   ```
   [~Device] quit
   ```
   
   
   
   # Create VLANIF 10 and VLANIF 20 and configure IP addresses for them.
   
   
   
   ```
   [~Device] interface vlanif 10
   ```
   ```
   [~Device-Vlanif10] ip address 10.1.1.1 24
   ```
   ```
   [*Device-Vlanif10] commit
   ```
   ```
   [~Device-Vlanif10] quit
   ```
   ```
   [~Device] interface vlanif 20
   ```
   ```
   [~Device-Vlanif20] ip address 10.1.2.1 24
   ```
   ```
   [*Device-Vlanif20] commit
   ```
   ```
   [~Device-Vlanif20] quit
   ```
2. Configure ACLs.
   
   
   
   # Create ACL 3001 and configure rules for the ACL to deny packets from the R&D department to the marketing department.
   
   ```
   [~Device] acl number 3001
   ```
   ```
   [*Device-acl4-advance-3001] rule deny ip source 10.1.1.0 0.0.0.255 destination 10.1.2.0 0.0.0.255
   ```
   ```
   [~Device-acl4-advance-3001] commit
   ```
   ```
   [~Device-acl4-advance-3001] quit
   ```
   
   
   
   # Create ACL 3002 and configure rules for the ACL to deny packets from the marketing department to the R&D department.
   
   
   
   ```
   [~Device] acl number 3002
   ```
   ```
   [*Device-acl4-advance-3002] rule deny ip source 10.1.2.0 0.0.0.255 destination 10.1.1.0 0.0.0.255
   ```
   ```
   [~Device-acl4-advance-3002] commit
   ```
   ```
   [~Device-acl4-advance-3002] quit
   ```
3. Configure a traffic classifier based on the advanced ACLs.
   
   
   
   # Configure a traffic classifier named **tc1** to classify packets that match ACL 3001 and ACL 3002.
   
   ```
   [~Device] traffic classifier tc1
   ```
   ```
   [*Device-classifier-tc1] if-match acl 3001
   ```
   ```
   [~Device-classifier-tc1] if-match acl 3002
   ```
   ```
   [~Device-classifier-tc1] commit
   ```
   ```
   [~Device-classifier-tc1] quit
   ```
4. Configure a traffic behavior.
   
   
   
   # Configure a traffic behavior named **tb1** to deny packets.
   
   ```
   [~Device] traffic behavior tb1
   ```
   ```
   [*Device-behavior-tb1] deny
   ```
   ```
   [~Device-behavior-tb1] commit
   ```
   ```
   [~Device-behavior-tb1] quit
   ```
5. Configure a traffic policy.
   
   
   
   # Define a traffic policy, and associate the traffic classifier and traffic behavior with the traffic policy.
   
   ```
   [~Device] traffic policy tp1
   ```
   ```
   [*Device-trafficpolicy-tp1] classifier tc1 behavior tb1
   ```
   ```
   [~Device-trafficpolicy-tp1] commit
   ```
   ```
   [~Device-trafficpolicy-tp1] quit
   ```
6. Apply the traffic policy in the inbound direction of interface 1 and interface 2.
   
   
   ```
   [~Device] interface gigabitethernet 0/1/0
   ```
   ```
   [~Device-GigabitEthernet0/1/0] traffic-policy tp1 inbound
   ```
   ```
   [~Device-GigabitEthernet0/1/0] commit
   ```
   ```
   [~Device-GigabitEthernet0/1/0] quit
   ```
   ```
   [~Device] interface gigabitethernet 0/2/0
   ```
   ```
   [~Device-GigabitEthernet0/2/0] traffic-policy tp1 inbound
   ```
   ```
   [~Device-GigabitEthernet0/2/0] commit
   ```
   ```
   [~Device-GigabitEthernet0/2/0] quit
   ```
7. Verify the configuration.
   
   
   
   # Check the ACL rule configuration.
   
   ```
   [~Device] display acl 3001
   ```
   ```
   Advanced ACL 3001, 1 rule                                                        
   Acl's step is 5                                                                  
    rule 5 deny ip source 10.1.1.0 0.0.0.255 destination 10.1.2.0 0.0.0.255
   ```
   ```
   [~Device] display acl 3002
   ```
   ```
   Advanced ACL 3002, 1 rule                                                        
   Acl's step is 5                                                                  
    rule 5 deny ip source 10.1.2.0 0.0.0.255 destination 10.1.1.0 0.0.0.255 
   ```
   
   # Check the traffic classifier configuration.
   
   ```
   [~Device] display traffic classifier user-defined
   ```
   ```
     User Defined Classifier Information:                                           
      Classifier: class1                                                            
       Operator: OR                                                                 
       Rule(s) :  -none-                                                            
      Classifier: tc1                                                               
       Operator: OR                                                                 
       Rule(s) :                                                                    
        if-match acl 3001 precedence 1                                                           
        if-match acl 3002 precedence 2
   ```
   
   # Check the traffic policy configuration.
   
   ```
   [~Device] display traffic policy user-defined tp1
   ```
   ```
     User Defined Traffic Policy Information:                                       
     Policy: tp1                                                                    
      Classifier: tc1                                                               
       Operator: OR                                                                 
        Behavior: tb1                                                         
         Deny         
        Precedence: 5  
   ```

#### Configuration Files

* Device configuration file
  
  ```
  # 
   sysname Device 
  # 
  vlan batch 10 20  
  # 
  acl number 3001                                                                  
   rule 5 deny ip source 10.1.1.0 0.0.0.255 destination 10.1.2.0 0.0.0.255         
  acl number 3002                                                                  
   rule 5 deny ip source 10.1.2.0 0.0.0.255 destination 10.1.1.0 0.0.0.255 
  # 
  traffic classifier tc1 operator or    
   if-match acl 3001                                                               
   if-match acl 3002    
  # 
  traffic behavior tb1 
   deny 
  # 
  traffic policy tp1 
   classifier tc1 behavior tb1 precedence 5 
  # 
  interface Vlanif10 
   ip address 10.1.1.1 255.255.255.0 
  # 
  interface Vlanif20 
   ip address 10.1.2.1 255.255.255.0 
  # 
  interface GigabitEthernet0/1/0 
   port link-type trunk                                                            
   port trunk allow-pass vlan 10  
   traffic-policy tp1 inbound 
  # 
  interface GigabitEthernet0/2/0 
   port link-type trunk                                                            
   port trunk allow-pass vlan 20  
   traffic-policy tp1 inbound 
  # 
  return
  ```