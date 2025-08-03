Configuring Data Plane Fast Recovery
====================================

Configuring Data Plane Fast Recovery

#### Context

DPFR can be configured to quickly detect faults and provide sub-millisecond-level local or remote fast fault convergence based on the data plane.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable DPFR globally, and set the sampling rate and aging time of entries in the fault table.
   
   
   ```
   [dpfr enable](cmdqueryname=dpfr+enable) [ sampler random-packet-number ] [ aging-time time-value ]
   ```
   
   By default, DPFR is disabled globally.
3. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
4. Enable fault detection on an interface for DPFR.
   
   
   ```
   [dpfr enable](cmdqueryname=dpfr+enable)
   ```
   
   By default, fault detection is disabled on an interface for DPFR.