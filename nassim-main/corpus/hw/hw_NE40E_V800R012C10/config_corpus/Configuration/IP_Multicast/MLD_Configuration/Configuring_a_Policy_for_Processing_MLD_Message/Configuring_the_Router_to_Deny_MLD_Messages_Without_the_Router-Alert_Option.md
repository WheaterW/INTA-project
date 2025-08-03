Configuring the Router to Deny MLD Messages Without the Router-Alert Option
===========================================================================

If user hosts do not want to receive MLD messages without the Router-Alert option, configure the Router directly connected to the user hosts to deny all MLD messages without the Router-Alert option.

#### Context

By default, the Router does not check the Router-Alert option in received MLD messages, so it accepts and processes all received MLD messages.

You can perform configurations either globally or on an interface.

* The **require-router-alert** command configuration in the system view takes effect on all interfaces.
* The **require-router-alert** command configuration in the view of an interface takes effect only on the interface. The interface-specific configuration takes precedence over the global configuration. If an interface-specific configuration is not available, the interface uses the global configuration.

#### Procedure

* Global configuration:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mld**](cmdqueryname=mld)
     
     
     
     The MLD view is displayed.
  3. Run [**require-router-alert**](cmdqueryname=require-router-alert)
     
     
     
     The Router is configured to accept and process only MLD messages with the Router-Alert option and discard those without the Router-Alert option.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Interface-specific configuration:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the interface connected to a user host or switch is displayed.
  3. Run [**mld require-router-alert**](cmdqueryname=mld+require-router-alert)
     
     
     
     The interface is configured to accept and process only MLD messages with the Router-Alert option and discard those without the Router-Alert option.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.