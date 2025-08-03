Adjusting DR Parameters
=======================

A source's Designated router (DR) is responsible for sending Register messages to a Rendezvous Point (RP), and a receiver's DR is responsible for sending Join messages to an RP. Devices elect a DR by exchanging Hello messages. The device with the highest priority wins the election. In the case of the same priority, the device with the largest IP address wins the election

#### Context

In IPv6 PIM-SM, a DR needs to be elected on a shared network segment to process multicast source registration and multicast group join requests. DR election is based on DR priorities and IPv6 addresses. The Routers exchange Hello messages carrying DR priorities to elect a DR.

* If all Routers support Hello messages carrying DR priorities, the PIM interface with the highest DR priority is elected as the DR. If all Routers have the same priority, the interface with the largest IPv6 address is elected as the DR.
* If one or more Routers do not support Hello messages carrying the DR priority, the PIM interface with the largest IPv6 address is elected as the DR.

You can configure a DR priority either globally or on an interface:

* Global configuration: takes effect on all interfaces.
* Interface-specific configuration: takes precedence over the global configuration. If an interface-specific configuration is not available, the interface uses the global configuration.

#### Procedure

* Configure a DR priority globally.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**pim-ipv6**](cmdqueryname=pim-ipv6)
     
     
     
     The IPv6 PIM view is displayed.
  3. Run [**hello-option dr-priority**](cmdqueryname=hello-option+dr-priority) *priority*
     
     
     
     A priority is set for all the interfaces on the Router that participate in the DR election.
     
     A higher *priority* value indicates a higher priority.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a DR priority for a specific interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The IPv6 PIM interface view is displayed.
  3. Run [**pim ipv6 hello-option dr-priority**](cmdqueryname=pim+ipv6+hello-option+dr-priority) *priority*
     
     
     
     A priority for DR election is set for the interface.
     
     A higher *priority* value indicates a higher priority.
  4. Run [**pim ipv6 timer dr-switch-delay**](cmdqueryname=pim+ipv6+timer+dr-switch-delay) *interval*
     
     
     
     The DR switchover delay is configured, and the delay timer is specified.
     
     
     
     When an interface changes from a DR to a non-DR, the original entries are valid till the delay timer expires.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.