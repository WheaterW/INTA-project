Configuring a VRRP Group to Track an Interface Monitoring Group
===============================================================

This section describes how to configure a VRRP group to track an interface monitoring group so that the VRRP group rapidly performs a master/backup switchover when the uplink interface status changes. This prevents service interruptions caused by uplink interface faults.

#### Context

To prevent failures on a VRRP-disabled uplink interface from causing service interruptions, configure a VRRP group to track the VRRP-disabled uplink interface. However, a VRRP group can track only one VRRP-disabled uplink interface at a time. As the network scale expands and more user interfaces are required, more VRRP groups need to be configured to track VRRP-disabled uplink interfaces. This means that the configuration workload is very heavy.

To reduce the configuration workload, you can add multiple VRRP-disabled interfaces to an interface monitoring group and enable a VRRP group to track the interface monitoring group. When the link failure rate of the interface monitoring group reaches a specified threshold, the VRRP group performs a master/backup switchover to ensure reliable service transmission.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view) The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*. The view of the interface where the VRRP group resides is displayed.
3. Run [**vrrp vrid**](cmdqueryname=vrrp+vrid) *vrid-value* **track** **monitor-group** *mtgrp-name* **failure-ratio** *failure-ratio-value* { **reduced** *reduced-value* | **link** } The VRRP group is configured to track an interface monitoring group. If the link failure rate on the access or network side reaches a specified threshold, the VRRP group performs a master/backup switchover.
4. Run [**commit**](cmdqueryname=commit)The configuration is committed.