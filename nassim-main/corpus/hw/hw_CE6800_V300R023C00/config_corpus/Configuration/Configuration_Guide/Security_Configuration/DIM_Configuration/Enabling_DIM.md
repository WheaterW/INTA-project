Enabling DIM
============

Enabling DIM

#### Context

The DIM function must be used together with RA. The DIM result is obtained by the RA server, which then generates the DIM trust report of the device.

You can enable the DIM function in either of the following ways:

* Periodically enabling the DIM function: In this mode, the device enables the DIM function at a specified time every day to measure the running process memory.
* Immediately enabling the DIM function: In this mode, the DIM function is disabled after the measurement is complete. To perform DIM on the running process memory again, re-execute the command for immediately enabling the DIM function.

#### Procedure

* Enable the DIM function periodically.
  
  
  ```
  [system-view](cmdqueryname=system-view)
  [trustem](cmdqueryname=trustem)
  [dynamic-integrity-measurement daily](cmdqueryname=dynamic-integrity-measurement+daily) time-value
  [commit](cmdqueryname=commit)
  ```
  
  If the [**dynamic-integrity-measurement daily**](cmdqueryname=dynamic-integrity-measurement+daily) command is run more than once, the latest configuration overrides the previous one.
  
  The DIM function is triggered only when the CPU usage of the device falls below 85%. If the CPU usage is greater than or equal to 85%, the DIM function is triggered when the CPU usage falls below 85%.
* Enable the DIM function immediately.
  
  
  ```
  [system-view](cmdqueryname=system-view)
  [trustem](cmdqueryname=trustem)
  [start dynamic-integrity-measurement right-now](cmdqueryname=start+dynamic-integrity-measurement+right-now)
  ```