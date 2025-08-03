Configuring Sampling Parameters for Attack Source Tracing
=========================================================

You can do as follows to change the value of sampling parameters.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**cpu-defend policy**](cmdqueryname=cpu-defend+policy) *policy-number*
   
   
   
   An attack defense policy is created and the attack defense view is displayed.
3. Run [**attack-source-trace sample-rate**](cmdqueryname=attack-source-trace+sample-rate) *sample-rate-value*
   
   
   
   The ratio for sampling the packet that records attack source tracing is set.
4. Run [**save attack-source-trace**](cmdqueryname=save+attack-source-trace+slot+all+file+linktype+hdlc+atm) **slot** { *slot-id* | **all** } [ **file** *filename* ] **linktype** { **hdlc** | **atm** | **ethernet** | **ppp** }
   
   
   
   Information about attack source tracing saved in the memory of an interface board is saved as a file.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.