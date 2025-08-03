Example for Configuring an IOAM Network in Edge-to-Edge Mode
============================================================

Example for Configuring an IOAM Network in Edge-to-Edge Mode

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001563998321__fig12922810919), packets sent from Host1 to Host2 are forwarded on the IOAM network. The network administrator requires that the forwarding information of such packets be reported to the analyzer so that the traffic forwarding path and status can be monitored.

**Figure 1** IOAM networking in edge-to-edge mode![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 represents 100GE 1/0/1.


  
![](figure/en-us_image_0000001563878077.png)

#### Procedure

1. Enable the IOAM function.
   
   
   
   # On DeviceA, enter the IOAM view, enable the IOAM function, and set the device ID to 11 and namespace ID to 20.
   
   
   
   ```
   <HUAWEI> system-view
   <~HUAWEI> sysname DeviceA
   [*HUAWEI] [commit](cmdqueryname=commit)
   [~DeviceA] [ptp enable](cmdqueryname=ptp+enable)
   [*DeviceA] [commit](cmdqueryname=commit)
   [~DeviceA] [ioam](cmdqueryname=ioam)
   [*DeviceA-ioam] [enable](cmdqueryname=enable)
   [*DeviceA-ioam] [device-id](cmdqueryname=device-id) 11
   [*DeviceA-ioam] [namespace-id](cmdqueryname=namespace-id) 20
   [*DeviceA-ioam] [quit](cmdqueryname=quit)
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
   
   
   
   # On DeviceB, enter the IOAM view, enable the IOAM function, and set the device ID to 12 and namespace ID to 20.
   
   
   
   ```
   <HUAWEI> system-view
   <~HUAWEI> sysname DeviceB
   [*HUAWEI] [commit](cmdqueryname=commit)
   [~DeviceB] [ptp enable](cmdqueryname=ptp+enable)
   [*DeviceB] [commit](cmdqueryname=commit)
   [~DeviceB] [ioam](cmdqueryname=ioam)
   [*DeviceB-ioam] [enable](cmdqueryname=enable)
   [*DeviceB-ioam] [device-id](cmdqueryname=device-id) 12
   [*DeviceB-ioam] [namespace-id](cmdqueryname=namespace-id) 20
   [*DeviceB-ioam] [quit](cmdqueryname=quit)
   [*DeviceB] [commit](cmdqueryname=commit)
   ```
   
   
   
   # On DeviceC, enter the IOAM view, enable the IOAM function, and set the device ID to 13 and namespace ID to 20.
   
   
   
   ```
   <HUAWEI> system-view
   <~HUAWEI> sysname DeviceC
   [*HUAWEI] [commit](cmdqueryname=commit)
   [~DeviceC] [ptp enable](cmdqueryname=ptp+enable)
   [*DeviceC] [commit](cmdqueryname=commit)
   [~DeviceC] [ioam](cmdqueryname=ioam)
   [*DeviceC-ioam] [enable](cmdqueryname=enable)
   [*DeviceC-ioam] [device-id](cmdqueryname=device-id) 13
   [*DeviceC-ioam] [namespace-id](cmdqueryname=namespace-id) 20
   [*DeviceC-ioam] [quit](cmdqueryname=quit)
   [*DeviceC] [commit](cmdqueryname=commit)
   ```
2. Configure DeviceA as the encapsulation node to sample the service traffic sent from Host1 to Host2 based on ACL rules, and set the data collection mode to edge-to-edge mode.
   
   
   
   # Create advanced ACL 3001 on DeviceA to match TCP packets sent from Host1 at 10.1.1.1 to Host2 at 10.1.2.1.
   
   ```
   [~DeviceA] acl 3001
   [~DeviceA-acl4-advance-3001] rule permit tcp source 10.1.1.1 0.0.0.0 destination 10.1.2.1 0.0.0.0 
   [*DeviceA-acl4-advance-3001] quit
   [*DeviceA] commit
   ```
   
   
   
   # On DeviceA, enter the IOAM view, enter the view of the IOAM profile named **default**, and create an IOAM policy named **1**.
   
   
   
   ```
   [~DeviceA] [ioam](cmdqueryname=ioam)
   [~DeviceA-ioam] [profile default](cmdqueryname=profile+default)
   [~DeviceA-ioam-profile-default] [policy](cmdqueryname=policy) 1
   [*DeviceA-ioam-profile-default-policy-1] [quit](cmdqueryname=quit)
   ```
   
   
   
   # On DeviceA, enter the IOAM policy view, set the data collection mode to edge-to-edge mode, and configure advanced ACL 3001 to match packets.
   
   
   
   ```
   [*DeviceA-ioam-profile-default] [policy](cmdqueryname=policy) 1
   [*DeviceA-ioam-profile-default-policy-1] [action-type encapsulate](cmdqueryname=action-type+encapsulate) service-type edge-to-edge
   [*DeviceA-ioam-profile-default-policy-1] [acl 3001](cmdqueryname=acl+3001) 
   [*DeviceA-ioam-profile-default-policy-1] [quit](cmdqueryname=quit)
   [*DeviceA-ioam-profile-default] [quit](cmdqueryname=quit)
   [*DeviceA-ioam] [quit](cmdqueryname=quit)
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
3. Configure DeviceC as the decapsulation node to send IOAM packets to the analyzer.
   
   # On DeviceC, create an analyzer with the ID 1, and set the source IP address to the device's IP address 10.1.3.1, destination IP address to the analyzer's IP address 10.2.2.2, and the analyzer's port number to 9000. Ensure that there are reachable routes between the device and analyzer. For detailed configurations, see "Configuration Scripts".
   ```
   [~DeviceC] collector collect 1
   [*DeviceC-collect-1] source ip 10.1.3.1 export host ip 10.2.2.2 udp-port 9000
   [*DeviceC-collect-1] quit
   [*DeviceC] commit
   ```
   
   
   
   # On DeviceC, enter the IOAM view, set the ID of the analyzer to which IOAM data is sent to 1, and enable the decapsulation function.
   
   
   
   ```
   [~DeviceC] [ioam](cmdqueryname=ioam)
   [~DeviceC-ioam] [collector](cmdqueryname=collector) collect 1
   [*DeviceC-ioam] [action-type decapsulate](cmdqueryname=action-type+decapsulate)
   [*DeviceC-ioam] quit
   [*DeviceC] [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

# Check the application of the ACL rule on DeviceA.

```
[~DeviceA] display ioam encapsulate acl applied-record slot 1
Total records: 1 
--------------------------------------------------------------------------------
ACL Number/Name                    TYPE   Rule       Count   State
--------------------------------------------------------------------------------
3001                               IPv4   5          1       Success
--------------------------------------------------------------------------------
```

#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
ptp enable
#
ioam
 enable
 namespace-id 20
 device-id 11
 #
 profile default
  #
   policy 1
    action-type encapsulate service-type edge-to-edge
    acl 3001
#
acl number 3001
 rule 5 permit tcp source 10.1.1.1 0 destination 10.1.2.1 0
#  
return
```

DeviceB

```
#
sysname DeviceB
#
ptp enable
#
ioam
 enable
 namespace-id 20
 device-id 12                                                              
#  
return
```

DeviceC

```
#
sysname DeviceC
#
vlan 10
#
interface Vlanif10
 ip address 10.2.2.1 255.255.255.0
#
interface 100GE1/0/1
 port link-type trunk
 port trunk allow-pass vlan 10
#
arp static 10.2.2.2 00e0-fc12-3456 vlan 10 interface 100GE1/0/1
#
ptp enable
#
ioam
 enable
 namespace-id 20
 device-id 13
 action-type decapsulate
 collector collect 1    
#  
collector collect 1 
 source ip 10.1.3.1 export host ip 10.2.2.2 udp-port 9000 
#
return
```