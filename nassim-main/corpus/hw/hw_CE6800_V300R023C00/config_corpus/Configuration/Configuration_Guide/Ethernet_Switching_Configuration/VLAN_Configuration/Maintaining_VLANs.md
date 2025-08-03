Maintaining VLANs
=================

Maintaining VLANs

#### Maintaining VLAN Traffic Statistics

Run the [**statistics enable**](cmdqueryname=statistics+enable) command in the VLAN view to enable VLAN traffic statistics collection.

```
[system-view](cmdqueryname=system-view)
[vlan](cmdqueryname=vlan) vlan-id
[statistics enable](cmdqueryname=statistics+enable)
[commit](cmdqueryname=commit)
```
![](public_sys-resources/notice_3.0-en-us.png) 

Cleared VLAN statistics cannot be restored. Exercise caution when clearing VLAN traffic statistics.

[Table 1](#EN-US_TASK_0000001176662411__table72341247696) lists the related operations for maintaining VLAN traffic statistics.

**Table 1** Maintaining VLAN traffic statistics
| Operation | Command |
| --- | --- |
| Viewing VLAN traffic statistics | [**display vlan**](cmdqueryname=display+vlan) *vlan-id* [**statistics**](cmdqueryname=statistics) [ **slot** *slot-id* ] |
| Clearing VLAN traffic statistics | [**reset vlan**](cmdqueryname=reset+vlan) *vlan-id* [**statistics**](cmdqueryname=statistics) [ **slot** *slot-id* ] |



#### Maintaining Traffic Statistics on a VLANIF Interface

Run the [**statistics**](cmdqueryname=statistics+enable) { **ipv4** | **ipv6** } **enable** [ **inbound** | **outbound** ] command in the VLANIF interface view to enable traffic statistics collection on the VLANIF interface.

```
[system-view](cmdqueryname=system-view)[interface](cmdqueryname=interface) vlanif vlan-id
[statistics](cmdqueryname=statistics) { ipv4 | ipv6 } enable [ inbound | outbound ]
[commit](cmdqueryname=commit)
```

Statistics concerning all packets forwarded at Layer 3 in a VLAN, that is, through the corresponding VLANIF interface, is collected.

![](public_sys-resources/notice_3.0-en-us.png) 

Cleared traffic statistics on a VLANIF interface cannot be restored. Exercise caution when clearing traffic statistics on a VLANIF interface.

[Table 2](#EN-US_TASK_0000001176662411__table282942391214) lists the related operations for maintaining traffic statistics on a VLANIF interface.

**Table 2** Maintaining traffic statistics on a VLANIF interface
| Operation | Command |
| --- | --- |
| Viewing traffic statistics on a VLANIF interface | [**display interface vlanif**](cmdqueryname=display+interface+vlanif) [ *vlan-id* ] |
| Clearing traffic statistics on a VLANIF interface | [**reset interface counters vlanif**](cmdqueryname=reset+interface+counters+vlanif) *vlan-id* |



#### Viewing VLAN Resource Statistics

Run the [**display fwm vlan statistics**](cmdqueryname=display+fwm+vlan+statistics) [ **slot** *slot-id* | **ipc** | **resource-apply** ] command to check VLAN resource statistics.