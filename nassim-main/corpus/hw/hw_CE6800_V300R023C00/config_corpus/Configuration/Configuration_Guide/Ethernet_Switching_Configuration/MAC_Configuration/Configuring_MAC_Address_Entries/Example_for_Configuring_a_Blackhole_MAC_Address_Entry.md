Example for Configuring a Blackhole MAC Address Entry
=====================================================

Example for Configuring a Blackhole MAC Address Entry

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001568607249__fig156041758113319), a device receives an access request from an unauthorized user. The MAC address of the unauthorized user is 00e0-fc12-3456 and the unauthorized user belongs to VLAN 3. The MAC address needs to be configured as a blackhole MAC address so that the device filters out packets from the unauthorized user.

**Figure 1** Network diagram for configuring a blackhole MAC address entry  
![](figure/en-us_image_0000001569029141.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create a VLAN to implement Layer 2 forwarding.
2. Configure a blackhole MAC address entry to prevent attack packets from the MAC address of the unauthorized user.

#### Procedure

1. Configure a blackhole MAC address entry.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] vlan 3
   [*DeviceA-vlan3] quit
   [*DeviceA] mac-address blackhole 00e0-fc12-3456 vlan 3
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Run the [**display mac-address blackhole**](cmdqueryname=display+mac-address+blackhole) command in any view to check blackhole MAC address entries.
```
[~DeviceA] display mac-address blackhole vlan 3
-------------------------------------------------------------------------------
MAC Address    VLAN/VSI/BD                          Learned-From        Type        Age
-------------------------------------------------------------------------------
00e0-fc12-3456   3/-/-                               -                 blackhole        -
-------------------------------------------------------------------------------
Total items: 1
```


#### Configuration Scripts

```
#
sysname DeviceA
#
vlan batch 3
#
mac-address blackhole 00e0-fc12-3456 vlan 3                                     
#
return
```