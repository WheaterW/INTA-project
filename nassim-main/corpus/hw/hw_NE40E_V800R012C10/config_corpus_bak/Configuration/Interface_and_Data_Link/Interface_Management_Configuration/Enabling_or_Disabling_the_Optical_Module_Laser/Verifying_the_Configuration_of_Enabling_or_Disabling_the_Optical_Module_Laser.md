Verifying the Configuration of Enabling or Disabling the Optical Module Laser
=============================================================================

After enabling or disabling the optical module laser, check its status.

#### Prerequisites

The optical module laser has been enabled or disabled as required.


#### Context

The following operations
affect the status of the optical module laser:

* Run the [**laser turn-on**](cmdqueryname=laser+turn-on) command to enable the optical module laser.
* Run the [**laser turn-off**](cmdqueryname=laser+turn-off) command to disable the optical module laser.
* Run the [**laser
  autoshutdown enable**](cmdqueryname=laser+autoshutdown+enable) command to configure the optical
  module to disable the laser automatically if it detects a link failure.
* Run the [**shutdown**](cmdqueryname=shutdown) command to deactivate the interface.


#### Procedure

* Run the [**display laser status**](cmdqueryname=display+laser+status) command in any view to check the laser status of the optical module.