Configuring the Clock Mode for the E1 Channels of a CPOS Interface
==================================================================

An E1 channel works in either master clock mode or slave
clock mode.

#### Context

The clock modes of different E1 channels on the same CPOS
interface are independent of each other.

When CPOS interfaces
on two devices are directly connected, one E1 channel must be configured
to work in master clock mode and use internal clock signals, and the
other E1 channel must be configured to work in slave clock mode and
use line clock signals.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view
   is displayed.
2. Run [**controller cpos**](cmdqueryname=controller+cpos) *cpos-number*
   
   
   
   The CPOS interface
   view is displayed.
3. Run [**e1**](cmdqueryname=e1) *e1-number* **set** **clock** { **master** | **slave** }
   
   
   
   A clock mode is configured for the
   E1 channel.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.