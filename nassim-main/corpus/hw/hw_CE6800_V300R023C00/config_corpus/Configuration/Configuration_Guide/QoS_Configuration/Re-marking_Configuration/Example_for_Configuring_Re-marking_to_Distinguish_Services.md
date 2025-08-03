Example for Configuring Re-marking to Distinguish Services
==========================================================

Example for Configuring Re-marking to Distinguish Services

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000002010277493__fig_dc_cfg_qos_006101), voice, video, and data terminals on the LAN of an enterprise are connected to interface 1 and interface 2 of DeviceC through DeviceA and DeviceB, and are connected to the WAN through DeviceC and DeviceD.

Packets of different services are identified by 802.1p priorities on the LAN side. When packets reach the WAN side through interface 3, it is required that differentiated services be provided based on DSCP priorities of packets.

**Figure 1** Network diagram for configuring re-marking![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000002010328769.png)

#### Procedure

1. Set the device name to DeviceC.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceC
   [*HUAWEI] [commit](cmdqueryname=commit)
   ```
2. Configure traffic classifiers.
   
   
   
   # On DeviceC, create and configure traffic classifiers **c1**, **c2**, and **c3** to classify packets based on 802.1p priorities.
   
   ```
   [~DeviceC] traffic classifier c1
   [*DeviceC-classifier-c1] if-match 8021p 2
   [*DeviceC-classifier-c1] quit
   [*DeviceC] traffic classifier c2
   [*DeviceC-classifier-c2] if-match 8021p 5
   [*DeviceC-classifier-c2] quit
   [*DeviceC] traffic classifier c3
   [*DeviceC-classifier-c3] if-match 8021p 6
   [*DeviceC-classifier-c3] quit
   [*DeviceC] [commit](cmdqueryname=commit)
   ```
3. Configure traffic behaviors.
   
   
   
   # On DeviceC, create and configure traffic behaviors **b1**, **b2**, and **b3** to re-mark priorities of user packets.
   
   ```
   [~DeviceC] traffic behavior b1
   [*DeviceC-behavior-b1] remark dscp 15
   [*DeviceC-behavior-b1] quit
   [*DeviceC] traffic behavior b2
   [*DeviceC-behavior-b2] remark dscp 40
   [*DeviceC-behavior-b2] quit
   [*DeviceC] traffic behavior b3
   [*DeviceC-behavior-b3] remark dscp 50
   [*DeviceC-behavior-b3] quit
   [*DeviceC] [commit](cmdqueryname=commit)
   ```
4. Configure a traffic policy and apply it to interfaces.
   
   
   
   # On DeviceC, create a traffic policy **p1**, bind traffic classifiers to traffic behaviors in the traffic policy, and apply the traffic policy to the inbound direction of interface 1 and interface 2 to re-mark packets.
   
   ```
   [~DeviceC] traffic policy p1
   [*DeviceC-trafficpolicy-p1] classifier c1 behavior b1
   [*DeviceC-trafficpolicy-p1] classifier c2 behavior b2
   [*DeviceC-trafficpolicy-p1] classifier c3 behavior b3
   [*DeviceC-trafficpolicy-p1] quit
   [*DeviceC] interface 100ge 1/0/1
   [*DeviceC-100GE1/0/1] traffic-policy p1 inbound
   [*DeviceC-100GE1/0/1] quit
   [*DeviceC] interface 100ge 1/0/2
   [*DeviceC-100GE1/0/2] traffic-policy p1 inbound
   [*DeviceC-100GE1/0/2] quit
   [*DeviceC] [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

# Check the traffic classifier configuration.

```
<DeviceC> display traffic classifier
  Traffic Classifier Information:
    Classifier: c1
      Type: OR
      Rule(s):
        if-match 8021p 2

    Classifier: c2
      Type: OR
      Rule(s):
        if-match 8021p 5

    Classifier: c3
      Type: OR
      Rule(s):
        if-match 8021p 6

Total classifier number is 3 
```

# Check the traffic policy configuration.

```
<DeviceC> display traffic policy
  Traffic Policy Information: 
    Policy: p1                                                                  
      Classifier: c1                                                           
        Type: OR                                                                
      Behavior: b1                                                             
        Remark:                                                                 
          Remark dscp 15                                                        

      Classifier: c2                                                           
        Type: OR                                                                
      Behavior: b2                                                             
        Remark:                                                                 
          Remark dscp cs5                                                       

      Classifier: c3                                                           
        Type: OR                                                                
      Behavior: b3                                                             
        Remark:                                                                 
          Remark dscp 50              

Total policy number is 3
```

# Check the traffic policy application records.

```
<DeviceC> display traffic-policy applied-record
Total records : 2 
--------------------------------------------------------------------------------     
Policy Type/Name                Apply Parameter                 Slot   State          
--------------------------------------------------------------------------------            
p1                               100GE1/0/1(IN)                  slot_1     success  

                                 100GE1/0/2(IN)                  slot_1     success 
--------------------------------------------------------------------------------  
```

#### Configuration Scripts

DeviceC

```
#
sysname DeviceC
#                                                                               
traffic classifier c1 type or                                                  
 if-match 8021p 2                                                               
#                                                                               
traffic classifier c2 type or                                                  
 if-match 8021p 5                                                               
#                                                                               
traffic classifier c3 type or                                                  
 if-match 8021p 6 
#                                                                               
traffic behavior b1                                                            
 remark dscp 15                                                                 
#                                                                               
traffic behavior b2                                                            
 remark dscp cs5                                                                
#                                                                               
traffic behavior b3                                                            
 remark dscp 50 
#                                                                               
traffic policy p1                                                               
 classifier c1 behavior b1 precedence 5                                       
 classifier c2 behavior b2 precedence 10                                      
 classifier c3 behavior b3 precedence 15
#                                                                               
interface 100GE1/0/1      
 traffic-policy p1 inbound                                                      
#                                                                               
interface 100GE1/0/2 
 traffic-policy p1 inbound 
#
return
```