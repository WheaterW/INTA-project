Example for Configuring Access Control Based on Source MAC Addresses
====================================================================

Example for Configuring Access Control Based on Source MAC Addresses

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001577611025__fig_dc_ar_cfg_qos_04490501), users of an enterprise access the Internet through DeviceA. The enterprise does not allow some hosts on the LAN to access the Internet. However, users can still access the Internet from these hosts by changing host IP addresses, and firewalls cannot prevent such unauthorized access based on IP addresses. Access control based on source MAC addresses can be configured to solve this problem. In this example, some hosts can be prevented from accessing the Internet but can access DeviceA.

**Figure 1** Network diagram![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 represents 100GE 1/0/1.


  
![](images/fig_dc_ar_cfg_qos_04490501.png)

#### Procedure

1. Create a VLAN and configure interfaces.
   
   # On DeviceA, create VLAN 10, configure VLANIF 10, and add 100GE 1/0/1 to the VLAN.
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] [commit](cmdqueryname=commit)
   [~DeviceA] vlan 10
   [*DeviceA-vlan10] quit
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] port link-type trunk
   [*DeviceA-100GE1/0/1] port trunk allow-pass vlan 10
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface vlanif 10
   [*DeviceA-Vlanif10] ip address 10.1.1.1 255.255.255.0
   [*DeviceA] commit
   ```
2. Configure an ACL rule.
   
   
   
   # On DeviceA, create ACL 3001 to match the traffic with the destination IP address 10.1.1.1/24.
   
   ```
   [~DeviceA] acl 3001
   [*DeviceA-acl4-advance-3001] rule 1 permit ip destination 10.1.1.0 0.0.0.255
   [*DeviceA-acl4-advance-3001] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
3. Configure traffic classifiers.
   
   
   
   # On DeviceA, create a traffic classifier **c1** and reference ACL 3001 in the traffic classifier.
   
   ```
   [~DeviceA] traffic classifier c1 type and
   [*DeviceA-classifier-c1] if-match acl 3001
   [*DeviceA-classifier-c1] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
   
   # On DeviceA, create traffic classifiers **c2** to **c4** to match MAC addresses of user hosts.
   
   ```
   [~DeviceA] traffic classifier c2 type and
   [*DeviceA-classifier-c2] if-match source-mac 00e0-fc0d-0001
   [*DeviceA-classifier-c2] quit
   [*DeviceA] traffic classifier c3 type and
   [*DeviceA-classifier-c3] if-match source-mac 00e0-fc0d-0002
   [*DeviceA-classifier-c3] quit
   [*DeviceA] traffic classifier c4 type and
   [*DeviceA-classifier-c4] if-match source-mac 00e0-fc0d-0003
   [*DeviceA-classifier-c4] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
4. Configure traffic behaviors.
   
   
   
   # On DeviceA, create a traffic behavior **b1** and configure the permit action in the traffic behavior.
   
   ```
   [~DeviceA] traffic behavior b1
   [*DeviceA-behavior-b1] permit
   [*DeviceA-behavior-b1] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
   
   
   
   # On DeviceA, create a traffic behavior **b2** and configure the deny action in the traffic behavior.
   
   ```
   [~DeviceA] traffic behavior b2
   [*DeviceA-behavior-b2] deny
   [*DeviceA-behavior-b2] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
5. Configure a traffic policy and apply it to the inbound direction of an interface.
   
   
   
   # On DeviceA, create a traffic policy **p1** and bind traffic classifiers to traffic behaviors in the traffic policy.
   
   ```
   [~DeviceA] traffic policy p1
   [*DeviceA-trafficpolicy-p1] classifier c1 behavior b1 precedence 5
   [*DeviceA-trafficpolicy-p1] classifier c2 behavior b2 precedence 10
   [*DeviceA-trafficpolicy-p1] classifier c3 behavior b2 precedence 15
   [*DeviceA-trafficpolicy-p1] classifier c4 behavior b2 precedence 20
   [*DeviceA-trafficpolicy-p1] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
   
   # Apply the traffic policy **p1** to the inbound direction of an interface.
   
   ```
   [~DeviceA] interface vlanif 10
   [*DeviceA-Vlanif10] traffic-policy p1 inbound
   [*DeviceA-Vlanif10] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

# Check the ACL rule configuration.

```
<DeviceA> display acl 3001
Advanced ACL 3001, 1 rule                                                                                                           
ACL's step is 5                                                                                                                     
 rule 1 permit ip destination 10.1.1.0 0.0.0.255 
 (0 times matched)                                 
```

# Check the traffic classifier configuration.

```
<DeviceA> display traffic classifier c1
  Traffic Classifier Information:
    Classifier: c1
      Type: AND
      Rule(s):
        if-match acl 3001
```
```
<DeviceA> display traffic classifier c2
  Traffic Classifier Information:
    Classifier: c2
      Type: AND
      Rule(s):
        if-match source-mac 00e0-fc0d-0001 ffff-ffff-ffff
```

# Check the traffic policy configuration.

```
<DeviceA> display traffic policy p1
  Traffic Policy Information:
    Policy: p1
      Classifier: c1
        Type: AND
      Behavior: b1

      Classifier: c2
        Type: AND
      Behavior: b2
        Deny

      Classifier: c3
        Type: AND
      Behavior: b2
        Deny

      Classifier: c4
        Type: AND
      Behavior: b2
        Deny
```

#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
vlan batch 10
#
interface 100GE1/0/1
 port link-type trunk
 port trunk allow-pass vlan 10
#
acl 3001
 rule 1 permit ip destination 10.1.1.0 0.0.0.255
# 
traffic classifier c1 type and
 if-match acl 3001
#
traffic classifier c2 type and
 if-match source-mac 00e0-fc0d-0001
#
traffic classifier c3 type and
 if-match source-mac 00e0-fc0d-0002
#
traffic classifier c4 type and
 if-match source-mac 00e0-fc0d-0003
#
traffic behavior b1
 permit
#
traffic behavior b2
 deny
#
traffic policy p1
 classifier c1 behavior b1 precedence 5
 classifier c2 behavior b2 precedence 10
 classifier c3 behavior b2 precedence 15
 classifier c4 behavior b2 precedence 20
#
interface Vlanif10
 ip address 10.1.1.1 255.255.255.0
 traffic-policy p1 inbound
#
return
```