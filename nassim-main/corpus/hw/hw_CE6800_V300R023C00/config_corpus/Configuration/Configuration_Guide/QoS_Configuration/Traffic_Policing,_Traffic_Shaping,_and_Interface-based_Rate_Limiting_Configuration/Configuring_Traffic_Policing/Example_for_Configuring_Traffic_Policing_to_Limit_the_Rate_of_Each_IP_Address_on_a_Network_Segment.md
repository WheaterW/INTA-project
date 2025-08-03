Example for Configuring Traffic Policing to Limit the Rate of Each IP Address on a Network Segment
==================================================================================================

Example for Configuring Traffic Policing to Limit the Rate of Each IP Address on a Network Segment

#### Networking Requirements

![](public_sys-resources/note_3.0-en-us.png) 

The CE6885-LL (low latency mode) does not support this example.

In [Figure 1](#EN-US_TASK_0000001525354860__fig_dc_ar_cfg_qos_04490201), users on an enterprise network send packets through DeviceA and DeviceB, and access the external network through DeviceC. Users reside on two different network segments. It is required that the rate of traffic from each IP address on network segment 192.168.1.0/24 be limited to 64 kbit/s and the rate of traffic from each IP address on network segment 192.168.2.0/24 be limited to 128 kbit/s.

**Figure 1** Network diagram for configuring traffic policing to limit the rate of each IP address on a network segment![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE 1/0/1 and 100GE 1/0/2, respectively.


  
![](images/fig_dc_ar_cfg_qos_04490201.png)

#### Procedure

1. Create VLANs and configure interfaces so that enterprise users can access the network through DeviceB.
   
   
   
   # Create VLANs 10 and 20 on DeviceB and add 100GE 1/0/1 to the VLANs.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] vlan batch 10 20
   [*DeviceB] interface 100ge 1/0/1
   [*DeviceB-100GE1/0/1] portswitch
   [*DeviceB-100GE1/0/1] port link-type trunk
   [*DeviceB-100GE1/0/1] port trunk allow-pass vlan 10 20
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] commit
   ```
   
   # Configure VLANIF interfaces on DeviceB and configure IP addresses for them.
   
   ```
   [~DeviceB] interface vlanif 10
   [*DeviceB-Vlanif10] ip address 192.168.1.1 24
   [*DeviceB-Vlanif10] quit
   [*DeviceB] interface vlanif 20
   [*DeviceB-Vlanif20] ip address 192.168.2.1 24
   [*DeviceB-Vlanif20] quit
   [*DeviceB] commit
   ```
2. Configure traffic classifiers.
   
   
   
   # On DeviceB, create ACL rules to match packets from enterprise users, and create traffic classifiers **c1** and **c2** to classify service flows from different enterprise users based on their IP addresses.
   
   ```
   [~DeviceB] acl 2001
   [*DeviceB-acl4-basic-2001] rule permit source 192.168.1.0 0.0.0.255 
   [*DeviceB-acl4-basic-2001] quit
   [*DeviceB] acl 2002
   [*DeviceB-acl4-basic-2002] rule permit source 192.168.2.0 0.0.0.255
   [*DeviceB-acl4-basic-2002] quit
   [*DeviceB] traffic classifier c1
   [*DeviceB-classifier-c1] if-match acl 2001
   [*DeviceB-classifier-c1] quit
   [*DeviceB] traffic classifier c2
   [*DeviceB-classifier-c2] if-match acl 2002
   [*DeviceB-classifier-c2] quit
   [*DeviceB] commit
   ```
3. Configure traffic behaviors and define traffic policing.
   
   
   
   # On DeviceB, create traffic behaviors **b1** and **b2** to perform traffic policing for packets from different enterprise users.
   
   ```
   [~DeviceB] traffic behavior b1
   [*DeviceB-behavior-b1] car cir 64
   [*DeviceB-behavior-b1] quit
   [*DeviceB] traffic behavior b2
   [*DeviceB-behavior-b2] car cir 128
   [*DeviceB-behavior-b2] quit
   [*DeviceB] commit
   ```
4. Configure a traffic policy and apply it to the inbound direction of an inbound interface.
   
   
   
   # On DeviceB, create traffic policy **p1**, bind traffic classifiers to traffic behaviors in the traffic policy, and apply the traffic policy to the inbound direction of 100GE 1/0/1 to perform traffic policing for packets from two different network segments.
   
   ```
   [~DeviceB] traffic policy p1
   [*DeviceB-trafficpolicy-p1] classifier c1 behavior b1
   [*DeviceB-trafficpolicy-p1] classifier c2 behavior b2
   [*DeviceB-trafficpolicy-p1] quit
   [*DeviceB] interface 100ge 1/0/1
   [*DeviceB-100GE1/0/1] traffic-policy p1 inbound
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] commit
   ```

#### Verifying the Configuration

After the preceding configurations are complete, check the traffic policing configuration on DeviceB.

# Check the traffic classifier configuration.

```
[~DeviceB] display traffic classifier
  Traffic Classifier Information: 
    Classifier: c1
      Type: OR
      Rule(s):
        if-match acl 2001

    Classifier: c2
      Type: OR
      Rule(s):
        if-match acl 2002

Total classifier number is 2
```

# Check the traffic policy configuration.

```
[~DeviceB] display traffic policy p1
  Traffic Policy Information:
    Policy: p1
      Classifier: c1
        Type: OR
      Behavior: b1
        Committed Access Rate:
          CIR 64 (Kbps), PIR 64 (Kbps), CBS 10000 (Bytes), PBS 10000 (Bytes)
          Color Mode: color blind
          Conform Action: pass                                                  
          Yellow  Action: pass                                                  
          Exceed  Action: discard

      Classifier: c2
        Type: OR
      Behavior: b2
        Committed Access Rate:
          CIR 128 (Kbps), PIR 128 (Kbps), CBS 10000 (Bytes), PBS 10000 (Bytes)
          Color Mode: color blind
          Conform Action: pass                                                  
          Yellow  Action: pass                                                  
          Exceed  Action: discard
```
#### Configuration Scripts

DeviceB
```
#
sysname DeviceB
#
vlan batch 10 20
#
acl 2001
 rule permit source 192.168.1.0 0.0.0.255 
#
acl 2002
 rule permit source 192.168.2.0 0.0.0.255
#
traffic classifier c1 type or
 if-match acl 2001
#
traffic classifier c2 type or
 if-match acl 2002
#
traffic behavior b1
 car cir 64
#
traffic behavior b2
 car cir 128
#
traffic policy p1
 classifier c1 behavior b1 
 classifier c2 behavior b2
#
interface Vlanif10                                                              
 ip address 192.168.1.1 255.255.255.0                                           
#                                                                               
interface Vlanif20                                                              
 ip address 192.168.2.1 255.255.255.0                                            
# 
interface 100GE1/0/1
 port link-type trunk
 port trunk allow-pass vlan 10 20
 traffic-policy p1 inbound
#
return
```