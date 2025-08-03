Configuring RIP Hardware Replication
====================================

After RIP hardware replication is configured, RIP packets can be forwarded in hardware replication mode. This implements fast forwarding and optimizes system performance.

#### Context

If a device has dot1q VLAN tag termination sub-interfaces, QinQ VLAN tag termination sub-interfaces, and user VLAN sub-interfaces and these sub-interfaces are configured with a large number of VLANs, protocol packets to be forwarded need to be replicated and broadcast in these VLANs. This increases the CPU load and may even cause problems such as packet replication and sending failures. To solve the problems, enable hardware replication for RIPv2 packets. After this function is enabled, hardware replicates the protocol packets to be broadcast, which reduces CPU consumption.


#### Procedure

* Enable hardware replication on a dot1q VLAN tag termination sub-interface.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**interface**](cmdqueryname=interface) *interface-type interface-number* . *subinterface-number* command to enter the sub-interface view.
  3. Run the [**encapsulation dot1q-termination**](cmdqueryname=encapsulation+dot1q-termination) command to configure the sub-interface as a dot1q VLAN tag termination sub-interface.
  4. Run the [**rip-broadcast-copy fast enable**](cmdqueryname=rip-broadcast-copy+fast+enable) command to enable hardware replication for RIPv2 packets.
  5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Enable hardware replication on a QinQ VLAN tag termination sub-interface.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**interface**](cmdqueryname=interface) *interface-type interface-number* . *subinterface-number* command to enter the sub-interface view.
  3. Run the [**encapsulation qinq-termination**](cmdqueryname=encapsulation+qinq-termination) command to configure the sub-interface as a QinQ VLAN tag termination sub-interface.
  4. Run the [**rip-broadcast-copy fast enable**](cmdqueryname=rip-broadcast-copy+fast+enable) command to enable hardware replication for RIPv2 packets.
  5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Enable hardware replication on a user VLAN sub-interface.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**interface**](cmdqueryname=interface) *interface-type interface-number* . *subinterface-number* command to enter the sub-interface view.
  3. Run the [**user-vlan**](cmdqueryname=user-vlan) { *start-vlan-id* [ *end-vlan-id* ] | *cevlan* } **qinq** { *start-pe-vlan* [ *end-pe-vlan* ] | *pevlan* } command to configure the sub-interface as a user VLAN sub-interface.
  4. Run the [**rip-broadcast-copy fast enable**](cmdqueryname=rip-broadcast-copy+fast+enable) command to enable hardware replication for RIPv2 packets.
  5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.