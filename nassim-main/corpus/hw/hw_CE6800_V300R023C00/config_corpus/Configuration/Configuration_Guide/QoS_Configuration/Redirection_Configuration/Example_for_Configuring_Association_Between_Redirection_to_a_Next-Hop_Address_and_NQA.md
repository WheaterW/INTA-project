Example for Configuring Association Between Redirection to a Next-Hop Address and NQA
=====================================================================================

Example for Configuring Association Between Redirection to a Next-Hop Address and NQA

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001564130229__fig391718398817), DeviceA is the upper-layer device of DeviceB and DeviceB is the user gateway. There are reachable routes between DeviceA and DeviceB. DeviceA is connected to the Internet through two links: high-speed link with the gateway at 10.1.20.1/24 and low-speed link with the gateway at 10.1.30.1/24. A default route has been configured on DeviceA to ensure that traffic is transmitted through the high-speed link by default. The customer requirements are as follows:

* Packets from the network segment 192.168.101.0/24 are redirected to the low-speed link for transmission, alleviating the bandwidth pressure of the high-speed link.
* If the low-speed link fails, packets from the network segment 192.168.101.0/24 can be rapidly switched back to the high-speed link to minimize communication interruption caused by the link fault.

**Figure 1** Network diagram of association between redirection to a next-hop address and NQA![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001563890149.png)

#### Procedure

1. Create VLANs and configure interfaces.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] [commit](cmdqueryname=commit)
   [~DeviceA] vlan batch 10 20 30
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] portswitch
   [*DeviceA-100GE1/0/1] port link-type trunk
   [*DeviceA-100GE1/0/1] port trunk allow-pass vlan 10
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] portswitch
   [*DeviceA-100GE1/0/2] port link-type trunk
   [*DeviceA-100GE1/0/2] port trunk allow-pass vlan 20
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100ge1/0/3 
   [*DeviceA-100GE1/0/3] portswitch
   [*DeviceA-100GE1/0/3] port link-type trunk
   [*DeviceA-100GE1/0/3] port trunk allow-pass vlan 30
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] interface vlanif 10
   [*DeviceA-Vlanif10] ip address 10.1.20.2 24
   [*DeviceA-Vlanif10] quit
   [*DeviceA] interface vlanif 20
   [*DeviceA-Vlanif20] ip address 10.1.30.2 24
   [*DeviceA-Vlanif20] quit
   [*DeviceA] interface vlanif 30
   [*DeviceA-Vlanif30] ip address 10.1.10.2 24
   [*DeviceA-Vlanif30] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
   
   # Configure DeviceC.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceC
   [*HUAWEI] [commit](cmdqueryname=commit)
   [~DeviceC] vlan batch 10
   [*DeviceC] interface 100ge 1/0/1
   [*DeviceC-100GE1/0/1] portswitch
   [*DeviceC-100GE1/0/1] port link-type trunk
   [*DeviceC-100GE1/0/1] port trunk allow-pass vlan 10
   [*DeviceC-100GE1/0/1] quit
   [*DeviceC] interface vlanif 10
   [*DeviceC-Vlanif10] ip address 10.1.20.1 24
   [*DeviceC-Vlanif10] quit
   [*DeviceC] [commit](cmdqueryname=commit)
   ```
   
   # Configure DeviceD.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceD
   [*HUAWEI] [commit](cmdqueryname=commit)
   [~DeviceD] vlan batch 20
   [*DeviceD] interface 100ge 1/0/1
   [*DeviceD-100GE1/0/1] portswitch
   [*DeviceD-100GE1/0/1] port link-type trunk
   [*DeviceD-100GE1/0/1] port trunk allow-pass vlan 20
   [*DeviceD-100GE1/0/1] quit
   [*DeviceD] interface vlanif 20
   [*DeviceD-Vlanif20] ip address 10.1.30.1 24
   [*DeviceD-Vlanif20] quit
   [*DeviceD] [commit](cmdqueryname=commit)
   ```
2. On DeviceA, configure an NQA test instance.
   
   
   ```
   [~DeviceA] nqa test-instance user test
   [*DeviceA-nqa-user-test] test-type icmp
   [*DeviceA-nqa-user-test] destination-address ipv4 10.1.30.1
   [*DeviceA-nqa-user-test] frequency 11
   [*DeviceA-nqa-user-test] probe-count 2
   [*DeviceA-nqa-user-test] interval seconds 5
   [*DeviceA-nqa-user-test] timeout 4
   [*DeviceA-nqa-user-test] start now
   [*DeviceA-nqa-user-test] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
3. Configure an ACL rule.
   
   
   
   # Create advanced ACL 3001 on DeviceA to allow packets from the network segment 192.168.101.0/24 to pass through.
   
   ```
   [~DeviceA] acl 3001
   [*DeviceA-acl4-advance-3001] rule permit ip source 192.168.101.0 0.0.0.255
   [*DeviceA-acl4-advance-3001] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
4. Configure a traffic classifier.
   
   
   
   # Create a traffic classifier **c1** on DeviceA and reference ACL 3001.
   
   ```
   [~DeviceA] traffic classifier c1
   [*DeviceA-classifier-c1] if-match acl 3001
   [*DeviceA-classifier-c1] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
5. Configure a traffic behavior.
   
   
   
   # Create a traffic behavior **b1** on DeviceA to redirect packets to the IP address 10.1.30.1, and associate NQA with redirection to a next-hop address.
   
   ```
   [~DeviceA] traffic behavior b1
   [*DeviceA-behavior-b1] redirect nexthop 10.1.30.1 track nqa user test
   [*DeviceA-behavior-b1] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
6. Configure a traffic policy and apply it to an interface.
   
   
   
   # Create a traffic policy **p1** on DeviceA, and bind the traffic classifier **c1** and traffic behavior **b1** to the traffic policy.
   
   ```
   [~DeviceA] traffic policy p1
   [*DeviceA-trafficpolicy-p1] classifier c1 behavior b1
   [*DeviceA-trafficpolicy-p1] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
   
   # Apply traffic policy **p1** to the inbound direction of 100GE 1/0/3.
   
   ```
   [~DeviceA] interface 100ge 1/0/3
   [*DeviceA-100GE1/0/3] traffic-policy p1 inbound
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   [~DeviceA] quit
   ```

#### Verifying the Configuration

# Check the ACL configuration.

```
<DeviceA> display acl 3001
Advanced ACL 3001, 1 rule                                                                                                           
ACL's step is 5                                                                                                                     
 rule 5 permit ip source 192.168.101.0 0.0.0.255 (0 times matched)
```

# Check the traffic classifier configuration.

```
<DeviceA> display traffic classifier
  Traffic Classifier Information:
    Classifier: c1                               
      Type: OR                                   
      Rule(s):                                   
        if-match acl 3001

Total classifier number is 1
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
          10.1.30.1 track nqa user test

Total policy number is 1
```

# Check the traffic policy application records.

```
<DeviceA> display traffic-policy applied-record
Total records : 1 
--------------------------------------------------------------------------------     
Policy Type/Name                     Apply Parameter             Slot State          
--------------------------------------------------------------------------------            
p1                                   100GE1/0/3(IN)               1    success        
--------------------------------------------------------------------------------  
```

# Check the NQA test result. If "Completion:success" and "Lost packet ratio: 0 %" are displayed, the NQA test succeeds and the link is normal.

```
<DeviceA> display nqa results test-instance user test

 NQA entry(user, test) :test flag is active ,test type is ICMP 
  1 . Test 1 result The test is finished
   Send operation times: 2              Receive response times: 2          
   Completion:success                   RTD over thresholds number: 0       
   Attempts number:1                    Drop operation number:0            
   Disconnect operation number:0        Operation timeout number:0         
   System busy operation number:0       Connection fail number:0           
   Operation sequence errors number:0   RTT Status errors number:0         
   Destination IP address:10.1.30.1                                    
   Min/Max/Average completion time: 3/4/3                                
   Sum/Square-Sum  completion time: 7/25                                 
   Last response packet receiving tim: 2020-04-09 09:55:38.2                           
   Lost packet ratio: 0 %
```

#### Configuration Scripts

* DeviceA
  ```
  #
  sysname DeviceA
  #
  vlan batch 10 20 30
  #
  acl number 3001
   rule 5 permit ip source 192.168.101.0 0.0.0.255
  #
  traffic classifier c1 type or
   if-match acl 3001
  #
  traffic behavior b1
   redirect nexthop 10.1.30.1 track nqa user test
  #
  traffic policy p1
   classifier c1 behavior b1 precedence 5
  #
  interface Vlanif10
   ip address 10.1.20.2 255.255.255.0
  #
  interface Vlanif20
   ip address 10.1.30.2 255.255.255.0
  #
  interface Vlanif30
   ip address 10.1.10.2 255.255.255.0
  #
  interface 100GE1/0/1
   port link-type trunk
   port trunk allow-pass vlan 10
  #
  interface 100GE1/0/2
   port link-type trunk
   port trunk allow-pass vlan 20
  #
  interface 100GE1/0/3
   port link-type trunk
   port trunk allow-pass vlan 30
   traffic-policy p1 inbound 
  #
  nqa test-instance user test
   test-type icmp
   destination-address ipv4 10.1.30.1
   interval seconds 5
   timeout 4
   probe-count 2
   frequency 11
   start now
  #
  return
  ```
* DeviceC
  ```
  #
  sysname DeviceC
  #
  vlan batch 10
  #
  interface Vlanif10
   ip address 10.1.20.1 255.255.255.0
  #
  interface 100GE1/0/1
   port link-type trunk
   port trunk allow-pass vlan 10
  #
  return
  ```
* DeviceD
  ```
  #
  sysname DeviceD
  #
  vlan batch 20
  #
  interface Vlanif20
   ip address 10.1.30.1 255.255.255.0
  #
  interface 100GE1/0/1
   port link-type trunk
   port trunk allow-pass vlan 20
  #
  return
  ```