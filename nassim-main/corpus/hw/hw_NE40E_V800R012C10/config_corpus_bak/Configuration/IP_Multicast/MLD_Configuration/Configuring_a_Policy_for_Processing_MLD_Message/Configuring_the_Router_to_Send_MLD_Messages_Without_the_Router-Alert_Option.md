Configuring the Router to Send MLD Messages Without the Router-Alert Option
===========================================================================

If some MLD interfaces on the same network need to receive MLD messages without the Router-Alert option, configure the Router connected to the user network segment to send MLD messages without the Router-Alert option.

#### Context

By default, the Router sends MLD messages with the Router-Alert option.

You can perform configurations either globally or on an interface.

* The [**undo send-router-alert**](cmdqueryname=undo+send-router-alert) command configuration in the system view takes effect on all interfaces.
* The [**undo send-router-alert**](cmdqueryname=undo+send-router-alert) command configuration in the view of an interface takes effect only on the interface. The interface-specific configuration takes precedence over the global configuration. If an interface-specific configuration is not available, the interface uses the global configuration.

#### Procedure

* Global configuration:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mld**](cmdqueryname=mld)
     
     
     
     The MLD view is displayed.
  3. Run [**undo send-router-alert**](cmdqueryname=undo+send-router-alert)
     
     
     
     The Router is configured to send MLD messages without the Router-Alert option.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Interface-specific configuration:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the interface connected to a user host or switch is displayed.
  3. Run [**undo mld send-router-alert**](cmdqueryname=undo+mld+send-router-alert)
     
     
     
     The interface is configured to send MLD messages without the Router-Alert option.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.