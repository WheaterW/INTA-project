Configuring Strict Filter for EVC Sub-Interfaces
================================================

This section describes how to configure strict filter for EVC sub-interfaces.

#### Usage Scenario

In a BD scenario, the Router has two sub-interfaces configured on an interface: one with the dot1q encapsulation type and the other with the default encapsulation type. If the sub-interface with the dot1q encapsulation type receives traffic, the sub-interface with the default encapsulation type may also send a copy of the traffic. This causes an illusion of backflow. Besides, the Router has two interfaces configured in a BD scenario. The first interface has one sub-interface with the dot1q encapsulation type. The second interface has two sub-interfaces: one with the dot1q encapsulation type and the other with the default encapsulation type. Once traffic passes through the sub-interface on the first interface, the second interface also sends two copied traffic from each of its sub-interfaces. This causes traffic to be replicated, wasting resources and reducing the board's forwarding efficiency. To allow traffic to be sent through specific interfaces, enable strict filter.


#### Pre-configuration Tasks

Before configuring strict filter on an interface, configure physical attributes for interfaces on the Router.


#### Procedure

* Enable strict filter globally.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ethernet egress-strict-filter enable**](cmdqueryname=ethernet+egress-strict-filter+enable)
     
     
     
     Strict filter is enabled globally.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Enable strict filter on an EVC sub-interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*.*sub-interface-number* **mode l2**
     
     
     
     The EVC sub-interface view is displayed.
  3. Run [**ethernet egress-strict-filter enable**](cmdqueryname=ethernet+egress-strict-filter+enable)
     
     
     
     Strict filter is enabled for the EVC sub-interface.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The strict filter configuration on an EVC sub-interface takes precedence over that configured in the system view. The strict filter configuration on an EVC sub-interface takes effect, regardless of whether strict filter is configured globally.