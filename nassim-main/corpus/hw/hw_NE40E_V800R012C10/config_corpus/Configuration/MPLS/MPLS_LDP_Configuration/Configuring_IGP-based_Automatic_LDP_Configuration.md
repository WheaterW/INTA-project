Configuring IGP-based Automatic LDP Configuration
=================================================

IGP-based automatic LDP configuration reduces the configuration workload and ensures configuration correctness.

#### Usage Scenario

To configure IGP-based MPLS LDP, you need to enable MPLS LDP globally and then enable MPLS LDP on all interfaces that require the function. If a large number of interfaces require the function, this configuration method is time-consuming and prone to configuration errors.

To address this issue, configure IGP-based automatic LDP configuration, allowing MPLS LDP to be enabled automatically on IGP-capable interfaces after MPLS LDP is enabled globally.


#### Pre-configuration Tasks

Before configuring IGP-based automatic LDP configuration, complete the following tasks:

* Configure basic IGP functions.
* Enable MPLS and MPLS LDP globally.

#### Procedure

* Configure IS-IS-based automatic LDP configuration.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
     
     
     
     The IS-IS view is displayed.
  3. Run [**mpls ldp auto-config**](cmdqueryname=mpls+ldp+auto-config)
     
     
     
     Automatic LDP configuration is enabled on IS-IS interfaces.
     
     
     
     After the command is run, MPLS LDP is enabled automatically on all interfaces which can establish IS-IS neighbor relationships in the IS-IS process. If you want to disable MPLS LDP on an interface, run the [**isis mpls ldp auto-config disable**](cmdqueryname=isis+mpls+ldp+auto-config+disable) command in the interface view.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure OSPF-based automatic LDP configuration.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ospf**](cmdqueryname=ospf)
     
     
     
     The OSPF view is displayed.
  3. Run [**mpls ldp auto-config**](cmdqueryname=mpls+ldp+auto-config)
     
     
     
     Automatic LDP configuration is enabled on OSPF interfaces.
     
     
     
     After the command is run, MPLS LDP is enabled automatically on all interfaces which can establish OSPF neighbor relationships in the OSPF process. If you want to disable MPLS LDP on an interface, run the [**ospf mpls ldp auto-config disable**](cmdqueryname=ospf+mpls+ldp+auto-config+disable) command in the interface view.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Verifying the Configuration

After completing the configuration, verify the configuration.

* Run the [**display mpls ldp interface**](cmdqueryname=display+mpls+ldp+interface+verbose+all) [ *interface-type* *interface-name* | **verbose** | **all** ] command to check information about MPLS LDP-enabled interfaces.