Configuring a Working Mode for an E1 Channel of a CPOS-Trunk Interface
======================================================================

An E1 channel of a CPOS-Trunk interface can be configured to work in clear channel or channelized mode to form trunk serial interfaces with different bandwidths.

#### Procedure

* Configure an E1 channel of a CPOS-Trunk interface to work in clear channel mode so that a trunk serial interface is generated.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface cpos-trunk**](cmdqueryname=interface+cpos-trunk) *trunk-id*
     
     
     
     The CPOS-Trunk interface view is displayed.
  3. Run [**e1**](cmdqueryname=e1) *e1-number* **unframed**
     
     
     
     An E1 channel of the CPOS-Trunk interface is configured to work in clear channel mode, and a trunk serial interface is generated.
     
     
     
     After the trunk serial interface in clear channel mode is generated, you can run the [**interface**](cmdqueryname=interface) **trunk-serial** *cpos-trunk-id*/*e1-number*:**0** command to enter the trunk serial interface view.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure an E1 channel of a CPOS-Trunk interface to work in channelized mode so that a trunk serial interface in channelized mode can be generated.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface cpos-trunk**](cmdqueryname=interface+cpos-trunk) *trunk-id*
     
     
     
     The CPOS-Trunk interface view is displayed.
  3. Run [**e1**](cmdqueryname=e1) *e1-number* **channel-set** *set-number* **timeslot-list** *slot-list*
     
     
     
     Timeslots of an E1 channel of the CPOS-Trunk interface are bundled, and a trunk serial interface is generated.
     
     
     
     After the trunk serial interface in channelized mode is generated, you can run the [**interface**](cmdqueryname=interface) **trunk-serial** *cpos-trunk-id*/*e1-number*:*set-number* command to enter the trunk serial interface view.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.