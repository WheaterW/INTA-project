Configuring a DiffServ Mode for a BD
====================================

Configuring a DiffServ Mode for a BD

#### Usage Scenario

When multiple BDs access a VPLS network, configure a DiffServ mode for each BD to implement differentiated user services among various BDs.

When you configure a DiffServ model, note the following:

* If you want to differentiate service priorities in a BD, configure the uniform mode.
* If you do not want to differentiate service priorities in a BD, configure the pipe or short pipe mode.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
   
   
   
   The BD view is displayed.
3. Run [**diffserv-mode**](cmdqueryname=diffserv-mode) { **pipe** *service-class* *color* | **short-pipe** *service-class* *color* [ **domain** *ds-name* ] | **uniform** }
   
   
   
   A DiffServ mode is configured for the BD.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.