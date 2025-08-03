Example for Configuring Redirection to an Interface
===================================================

Example for Configuring Redirection to an Interface

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001563890137__fig13543114711156), the server connects to the Internet through DeviceA, DeviceB, and DeviceD. All traffic from the Internet needs to be redirected to DeviceC for filtering to ensure the security of traffic to the server.

**Figure 1** Network diagram of redirecting packets to an interface![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, interface 3, and interface 4 represent 100GE 1/0/1, 100GE 1/0/2, 100GE 1/0/3, and 100GE 1/0/4, respectively.


  
![](figure/en-us_image_0000001563890145.png)

#### Procedure

1. Create VLANs and configure interfaces to ensure Layer 2 connectivity.
   
   
   
   # Create VLAN 200 and VLAN 300 on DeviceB.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] [commit](cmdqueryname=commit)
   [~DeviceB] vlan batch 200 300
   [*DeviceB] [commit](cmdqueryname=commit)
   ```
   
   # Configure 100GE 1/0/1 on DeviceB as a trunk interface and add it to VLAN 200 and VLAN 300. Configure 100GE 1/0/2 and 100GE 1/0/3 on DeviceB as access interfaces, and add 100GE 1/0/2 to VLAN 200 and 100GE 1/0/3 to VLAN 300.
   
   ```
   [~DeviceB] interface 100ge 1/0/1
   [~DeviceB-100GE1/0/1] portswitch
   [*DeviceB-100GE1/0/1] port link-type trunk
   [*DeviceB-100GE1/0/1] port trunk allow-pass vlan 200 300
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] interface 100ge 1/0/2
   [*DeviceB-100GE1/0/2] portswitch
   [*DeviceB-100GE1/0/2] port link-type access
   [*DeviceB-100GE1/0/2] port default vlan 200
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] interface 100ge 1/0/3
   [*DeviceB-100GE1/0/3] portswitch
   [*DeviceB-100GE1/0/3] port link-type access
   [*DeviceB-100GE1/0/3] port default vlan 300
   [*DeviceB-100GE1/0/3] quit
   [*DeviceB] [commit](cmdqueryname=commit)
   ```
   
   
   
   # Create VLAN 200 and VLAN 300 on DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] [commit](cmdqueryname=commit)
   [~DeviceA] vlan batch 200 300
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
   
   # Configure 100GE 1/0/1, 100GE 1/0/2, 100GE 1/0/3, and 100GE 1/0/4 on DeviceA as trunk interfaces and add them to VLAN 200 and VLAN 300. To prevent loops, add 100GE 1/0/3 and 100GE 1/0/4 to the same port isolation group and disable MAC address learning on 100GE 1/0/4 to prevent MAC address flapping.
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] portswitch
   [*DeviceA-100GE1/0/1] port link-type trunk
   [*DeviceA-100GE1/0/1] port trunk allow-pass vlan 200 300
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] portswitch
   [*DeviceA-100GE1/0/2] port link-type trunk
   [*DeviceA-100GE1/0/2] port trunk allow-pass vlan 200 300
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100ge 1/0/3
   [*DeviceA-100GE1/0/3] portswitch
   [*DeviceA-100GE1/0/3] port link-type trunk
   [*DeviceA-100GE1/0/3] port trunk allow-pass vlan 200 300
   [*DeviceA-100GE1/0/3] port-isolate enable group 1
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] interface 100ge 1/0/4
   [*DeviceA-100GE1/0/4] portswitch
   [*DeviceA-100GE1/0/4] port link-type trunk
   [*DeviceA-100GE1/0/4] port trunk allow-pass vlan 200 300
   [*DeviceA-100GE1/0/4] port-isolate enable group 1
   [*DeviceA-100GE1/0/4] mac-address learning disable
   [*DeviceA-100GE1/0/4] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
2. Configure redirection to an interface on DeviceA.
   
   
   
   # Configure a traffic classifier. Configure a matching rule based on all data packets in the traffic classifier **c1**.
   
   ```
   [~DeviceA] traffic classifier c1
   [*DeviceA-classifier-c1] if-match any
   [*DeviceA-classifier-c1] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
   
   # Configure a traffic behavior. Define redirection to a specified interface in the traffic behavior **b1**.
   
   ```
   [~DeviceA] traffic behavior b1
   [*DeviceA-behavior-b1] redirect interface 100ge 1/0/3
   [*DeviceA-behavior-b1] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
   
   # Create a traffic policy **p1**, and bind the traffic classifier **c1** and traffic behavior **b1** to the traffic policy.
   
   ```
   [~DeviceA] traffic policy p1
   [*DeviceA-trafficpolicy-p1] classifier c1 behavior b1
   [*DeviceA-trafficpolicy-p1] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
   
   # Apply the traffic policy to the inbound direction of 100GE 1/0/1.
   
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
        if-match any                                                                                                                

Total classifier number is 1
```

# Check the traffic behavior configuration.

```
<DeviceA> display traffic behavior
  Traffic Behavior Information:                                                                                                     
    Behavior: b1                                                                                                                    
      Redirect:                                                                                                                     
        Redirect interface 100GE1/0/3                                                                                               

Total behavior number is 1 
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
          Redirect interface 100GE1/0/3                                                                                        

Total policy number is 1
```

# Check the traffic policy application records.

```
<DeviceA> display traffic-policy applied-record
Total records : 1                                                                                                                   
--------------------------------------------------------------------------------                                                    
Policy Type/Name                     Apply Parameter            Slot  State                                                         
--------------------------------------------------------------------------------                                                    
p1                                   100GE1/0/1(IN)             1     success                                              
--------------------------------------------------------------------------------
```

#### Configuration Scripts

* DeviceA
  ```
  #
  sysname DeviceA
  #
  vlan batch 200 300
  #
  traffic classifier c1 type or
   if-match any
  #
  traffic behavior b1
   redirect interface 100GE 1/0/3
  #
  traffic policy p1
   classifier c1 behavior b1 precedence 5
  #
  interface 100GE1/0/1
   port link-type trunk
   port trunk allow-pass vlan 200 300
   traffic-policy p1 inbound 
  #
  interface 100GE1/0/2
   port link-type trunk
   port trunk allow-pass vlan 200 300
  #
  interface 100GE1/0/3
   port link-type trunk
   port trunk allow-pass vlan 200 300
   port-isolate enable group 1
  #
  interface 100GE1/0/4
   port link-type trunk
   port trunk allow-pass vlan 200 300
   port-isolate enable group 1
   mac-address learning disable
  #
  return
  ```
* DeviceB
  ```
  #
  sysname DeviceB
  #
  vlan batch 200 300
  #
  interface 100GE1/0/1
   port link-type trunk
   port trunk allow-pass vlan 200 300
  #
  interface 100GE1/0/2
   port default vlan 200
  #
  interface 100GE1/0/3
   port default vlan 300
  #
  return
  ```