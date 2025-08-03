Example for Disabling MAC Address Learning in a Traffic Behavior
================================================================

Example for Disabling MAC Address Learning in a Traffic Behavior

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001176664467__fig1854684211516), user networks 1 and 2 belong to VLAN 10 and VLAN 20, respectively. The two user networks are connected to DeviceA through DeviceB, and DeviceA is connected to DeviceB through 100GE 1/0/1. To prevent hackers from attacking DeviceA with a large number of packets containing forged source MAC addresses, disable MAC address learning in a traffic behavior.

**Figure 1** Networking for disabling MAC address learning in a traffic behavior![](public_sys-resources/note_3.0-en-us.png) 

Interface 1 in this example represents 100GE 1/0/1.

![](figure/en-us_image_0000001176664491.png)



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create VLANs and add 100GE 1/0/1 to them to implement Layer 2 forwarding.
2. Disable MAC address learning in a traffic behavior to prevent MAC address attacks.

#### Procedure

1. Create VLANs and add 100GE 1/0/1 to them.
   
   
   
   # Add 100GE 1/0/1 to VLAN 10 and VLAN 20.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] vlan batch 10 20
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] portswitch
   [*DeviceA-100GE1/0/1] port link-type trunk
   [*DeviceA-100GE1/0/1] port trunk allow-pass vlan 10 20
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
2. Disable MAC address learning in a traffic behavior.
   
   
   
   # Configure a traffic policy, and disable MAC address learning in the traffic behavior view.
   
   ```
   [~DeviceA] traffic classifier class1
   [*DeviceA-classifier-class1] if-match destination-mac 00e0-fc12-3456
   [*DeviceA-classifier-class1] quit
   [*DeviceA] traffic behavior b1
   [*DeviceA-behavior-b1] mac-address learning disable
   [*DeviceA-behavior-b1] quit
   [*DeviceA] traffic policy poly1
   [*DeviceA-trafficpolicy-poly1] classifier class1 behavior b1
   [*DeviceA-trafficpolicy-poly1] quit
   [*DeviceA] commit
   ```
   
   # Apply the traffic policy to 100GE 1/0/1.
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] traffic-policy poly1 inbound
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Run the **display traffic policy** command in any view to check whether MAC address learning has been disabled in the traffic behavior.

```
[~DeviceA] display traffic policy
  Traffic Policy Information:
    Policy: poly1
      Classifier: class1
        Type: OR
      Behavior: b1
        Mac-address learning:
          Mac-address learning disable

Total policy number is 1
```

# Run the **display traffic-policy applied-record** command in any view to check the traffic policy application records.

```
[~DeviceA] display traffic-policy applied-record
Total records : 1
--------------------------------------------------------------------------------
Policy Type/Name                     Apply Parameter            Slot  State
--------------------------------------------------------------------------------
poly1                                100GE1/0/1(IN)              1     success
--------------------------------------------------------------------------------
```

#### Configuration Scripts

```
#
sysname DeviceA
#
vlan batch 10 20
#
traffic classifier class1 type or
 if-match destination-mac 00e0-fc12-3456 ffff-ffff-ffff
#
traffic behavior b1
 mac-address learning disable
#
traffic policy poly1
 classifier class1 behavior b1 precedence 5
#
interface 100GE1/0/1
 port link-type trunk
 port trunk allow-pass vlan 10 20
 traffic-policy poly1 inbound
#
return
```