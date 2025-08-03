Activating the MACsec License of Interfaces
===========================================

Activating the MACsec License of Interfaces

#### Pre-configuration Tasks

The license file has been loaded for MACsec.

1. The license file on the main control board has been activated by running the [**license active**](cmdqueryname=license+active) *file-name* command.
2. Interface-specific scenario licenses have been activated.
   * Interface-specific aggregation scenario licenses have been activated by running the [**active port-aggregation**](cmdqueryname=active+port-aggregation) **slot** *slot-id* **card** *card-id* **port** *port-list* command.
   * Interface-specific peering scenario licenses have been activated by running the [**active port-peering**](cmdqueryname=active+port-peering) **slot** *slot-id* **card** *card-id* **port** *port-list* command.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**license**](cmdqueryname=license)
   
   
   
   The license view is displayed.
3. Run [**active port-macsec**](cmdqueryname=active+port-macsec) **slot** *slotid* **card** *cardid* **port** *port-list*
   
   
   
   The MACsec license of interfaces is activated.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Checking the Configurations

Run the [**display license resource usage port-macsec**](cmdqueryname=display+license+resource+usage+port-macsec) { **all** | **slot** *slot-id* } [ **active** | **deactive** ] command to check the MACsec license status of interfaces on a board.

In VS mode, this command is supported only by the admin VS.