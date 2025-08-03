Verifying the Configuration
===========================

After configuring LDP-IGP synchronization, you can check the synchronization states of interfaces on which LDP-IGP synchronization has been enabled.

#### Prerequisites

LDP-IGP synchronization has been configured.


#### Procedure

* Run the [**display mpls ldp**](cmdqueryname=display+mpls+ldp) command to check the global LDP configuration.
* Run the [**display isis**](cmdqueryname=display+isis+ldp-sync+interface) [ *process-id* ] **ldp-sync** **interface** command to check the synchronization states of interfaces on which LDP-IS-IS synchronization has been enabled.
* Run the [**display ospf ldp-sync interface**](cmdqueryname=display+ospf+ldp-sync+interface+all) { **all** | *interface-type* *interface-number* } command to check the synchronization states of interfaces on which LDP-OSPF synchronization has been enabled.