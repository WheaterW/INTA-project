Configuring the Clock Mode for a CPOS Interface
===============================================

A CPOS interface works in either master clock mode or slave clock mode. You can configure the clock mode for a CPOS interface.

#### Context

A CPOS interface supports the following clock modes:

* Master clock mode: uses internal clock signals.
* Slave clock mode: uses line clock signals.

When a CPOS interface is connected to an SDH device, configure the CPOS interface to work in slave clock mode because the precision of the clock in the SDH network is higher than the precision of the internal clock source of the CPOS interface.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**controller cpos**](cmdqueryname=controller+cpos) *cpos-number*
   
   
   
   The CPOS interface view is displayed.
3. Run [**clock**](cmdqueryname=clock) { **master** | **slave** }
   
   
   
   A clock mode is configured for the CPOS interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.