Example for Configuring Redirection to a Next-Hop Address
=========================================================

Example for Configuring Redirection to a Next-Hop Address

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001513050182__fig766814017525), DeviceA functioning as a Layer 3 forwarding device is routable to NetworkA and is connected to the Internet through two links. One uplink is a high-speed link with the gateway at 10.1.20.1/24, and the other is a low-speed link with the gateway at 10.1.30.1/24. The user requires that DeviceA forward packets from network segments 192.168.100.0/24 and 192.168.101.0/24 to the Internet through the high-speed link and low-speed link, respectively. This requirement can be met by configuring redirection to a next-hop address, which is sometimes also called policy-based routing (PBR).

**Figure 1** Network diagram of redirection to a next-hop address![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001512691002.png)

#### Procedure

1. Create VLANs and configure interfaces.
   
   
   
   # Create VLAN 10, VLAN 20, and VLAN 30 on DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] [commit](cmdqueryname=commit)
   [~DeviceA] vlan batch 10 20 30
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
   
   # Configure 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3 on DeviceA as trunk interfaces and add them to corresponding VLANs.
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] portswitch
   [*DeviceA-100GE1/0/1] port link-type trunk
   [*DeviceA-100GE1/0/1] port trunk allow-pass vlan 10
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] portswitch
   [*DeviceA-100GE1/0/2] port link-type trunk
   [*DeviceA-100GE1/0/2] port trunk allow-pass vlan 20
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100ge 1/0/3
   [*DeviceA-100GE1/0/3] portswitch
   [*DeviceA-100GE1/0/3] port link-type trunk
   [*DeviceA-100GE1/0/3] port trunk allow-pass vlan 30
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
   
   # Create VLANIF 10, VLANIF 20, and VLANIF 30 and configure IP addresses for them.
   
   ```
   [~DeviceA] interface vlanif 10
   [*DeviceA-Vlanif10] ip address 10.1.10.2 24
   [*DeviceA-Vlanif10] quit
   [*DeviceA] interface vlanif 20
   [*DeviceA-Vlanif20] ip address 10.1.20.2 24
   [*DeviceA-Vlanif20] quit
   [*DeviceA] interface vlanif 30
   [*DeviceA-Vlanif30] ip address 10.1.30.2 24
   [*DeviceA-Vlanif30] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
2. Configure ACL rules.
   
   
   
   # Create advanced ACLs 3001 and 3002 on DeviceA to allow packets on network segments 192.168.100.0/24 and 192.168.101.0/24 to pass through.
   
   ```
   [~DeviceA] acl 3001
   [*DeviceA-acl4-advance-3001] rule permit ip source 192.168.100.0 0.0.0.255
   [*DeviceA-acl4-advance-3001] quit
   [*DeviceA] acl 3002
   [*DeviceA-acl4-advance-3002] rule permit ip source 192.168.101.0 0.0.0.255
   [*DeviceA-acl4-advance-3002] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
3. Configure traffic classifiers.
   
   
   
   # Create traffic classifiers **c1** and **c2** on DeviceA, and bind **c1** to ACL 3001 and **c2** to ACL 3002.
   
   ```
   [~DeviceA] traffic classifier c1
   [*DeviceA-classifier-c1] if-match acl 3001
   [*DeviceA-classifier-c1] quit
   [*DeviceA] traffic classifier c2
   [*DeviceA-classifier-c2] if-match acl 3002
   [*DeviceA-classifier-c2] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
4. Configure traffic behaviors.
   
   
   
   # Create traffic behaviors **b1** and **b2** on DeviceA and configure actions that redirect packets to IP addresses 10.1.20.1 and 10.1.30.1.
   
   ```
   [~DeviceA] traffic behavior b1
   [*DeviceA-behavior-b1] redirect nexthop 10.1.20.1
   [*DeviceA-behavior-b1] quit
   [*DeviceA] traffic behavior b2
   [*DeviceA-behavior-b2] redirect nexthop 10.1.30.1
   [*DeviceA-behavior-b2] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
5. Configure a traffic policy and apply it to an interface.
   
   
   
   # Create a traffic policy **p1** on DeviceA, and bind the traffic classifier **c1** to the traffic behavior **b1** and the traffic classifier **c2** to the traffic behavior **b2**.
   
   ```
   [~DeviceA] traffic policy p1
   [*DeviceA-trafficpolicy-p1] classifier c1 behavior b1
   [*DeviceA-trafficpolicy-p1] classifier c2 behavior b2
   [*DeviceA-trafficpolicy-p1] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
   
   # Apply traffic policy **p1** to the inbound direction of 100GE 1/0/1.
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] traffic-policy p1 inbound
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

# Check the traffic classifier configuration.

```
<DeviceA> display traffic classifier
  Traffic Classifier Information:                                                                                                   
    Classifier: c1                                                                                                                  
      Type: OR                                                                                                                      
      Rule(s):                                                                                                                      
        if-match acl 3001                                                                                                           

    Classifier: c2                                                                                                                  
      Type: OR                                                                                                                      
      Rule(s):                                                                                                                      
        if-match acl 3002                                                                                                           

Total classifier number is 2
```

# Check the traffic policy configuration.

```
<DeviceA> display traffic policy
  Traffic Policy Information:
    Policy: p1
      Classifier: c1
        Type: OR
      Behavior: b1                                                                                                                  
        Redirect:                                                                                                                   
          Redirect nexthop                                                                                                          
          10.1.20.1                                                                                                                 

      Classifier: c2                                                                                                                
        Type: OR                                                                                                                    
      Behavior: b2                                                                                                                  
        Redirect:                                                                                                                   
          Redirect nexthop                                                                                                          
          10.1.30.1

Total policy number is 2
```

# Check the traffic policy application records.

```
<DeviceA> display traffic-policy applied-record
Total records : 1 
--------------------------------------------------------------------------------     
Policy Type/Name                     Apply Parameter            Slot State          
--------------------------------------------------------------------------------            
p1                                   100GE1/0/1(IN)              1    success        
--------------------------------------------------------------------------------  
```

#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
vlan batch 10 20 30
#
acl number 3001
 rule 5 permit ip source 192.168.100.0 0.0.0.255
#
acl number 3002
 rule 5 permit ip source 192.168.101.0 0.0.0.255
#
traffic classifier c1 type or
 if-match acl 3001
#
traffic classifier c2 type or
 if-match acl 3002
#
traffic behavior b1
 redirect nexthop 10.1.20.1
#
traffic behavior b2
 redirect nexthop 10.1.30.1
#
traffic policy p1
 classifier c1 behavior b1 precedence 5
 classifier c2 behavior b2 precedence 10
#
interface Vlanif10
 ip address 10.1.10.2 255.255.255.0
#
interface Vlanif20
 ip address 10.1.20.2 255.255.255.0
#
interface Vlanif30
 ip address 10.1.30.2 255.255.255.0
#
interface 100GE1/0/1
 port link-type trunk
 port trunk allow-pass vlan 10
 traffic-policy p1 inbound 
#
interface 100GE1/0/2
 port link-type trunk
 port trunk allow-pass vlan 20
#
interface 100GE1/0/3
 port link-type trunk
 port trunk allow-pass vlan 30
#
return
```