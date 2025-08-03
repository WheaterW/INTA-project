Verifying the Command Line Configuration
========================================

After completing basic configuration, run display commands to verify the configuration.

#### Context

Basic configurations are complete.


#### Procedure

* Run [**display current-configuration**](cmdqueryname=display+current-configuration)[ **configuration** [ *configuration-type* [ *configuration-instance* ] | *config-type-no-inst* ] | **all** | **inactive** ] [ **include-default** ]
  
  
  
  The current configuration is displayed.
* Run [**display this**](cmdqueryname=display+this)
  
  
  
  The configuration in the current view is displayed.
  
  If the configuration parameters that are taking effect are the same as the default working parameters, they are not displayed. The configured parameters that do not take effect are not displayed either.