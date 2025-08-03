Adjusting DR Parameters
=======================

A source's Designated router (DR) is responsible for sending Register messages to a Rendezvous Point (RP), and a receiver's DR is responsible for sending Join messages to an RP. The Routers elect a DR by exchanging Hello messages. The Router with the highest priority wins the election. If the Router have the same priority, the Router with the largest IP address wins the election.

#### Context

In PIM-SM, DRs need to be elected on a shared network segment. They are responsible for the registering of the local multicast source or the joining of receivers. DR election is based on DR priorities and IP addresses. The Routers exchange Hello messages carrying DR priorities to elect DRs.

* If all Routers support Hello messages carrying DR priorities, the interface with the highest DR priority is selected as the DR. If the Routers have the same priority, the interface with the largest IP address is elected as the DR.
* The interface with the highest IP address on a Router is elected as a DR as long as one Router in the same network segment does not support Hello messages carrying DR priorities.

You can set a DR priority either globally or on an interface.

* Global configuration: takes effect on all interfaces.
* Interface-specific configuration: takes precedence over the global configuration. If an interface-specific configuration is not available, the interface uses the global configuration.

#### Procedure

* Configure a DR priority globally.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**pim**](cmdqueryname=pim) [ **vpn-instance** *vpn-instance-name* ]
     
     
     
     The PIM view is displayed.
  3. Run [**hello-option dr-priority**](cmdqueryname=hello-option+dr-priority) *priority*
     
     
     
     A priority is set for all the interfaces on the Router that participate in the DR election.
     
     A higher *priority* value indicates a higher priority.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a DR priority for a specific interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The PIM interface view is displayed.
  3. Run [**pim hello-option dr-priority**](cmdqueryname=pim+hello-option+dr-priority) *priority*
     
     
     
     A priority for DR election is set for the interface.
     
     A higher *priority* value indicates a higher priority.
  4. Run [**pim timer dr-switch-delay**](cmdqueryname=pim+timer+dr-switch-delay) *interval*
     
     
     
     A DR switchover delay is set. If an interface changes from a DR to a non-DR, the original entries are valid till the delay expires.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.