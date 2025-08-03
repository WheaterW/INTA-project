(Optional) Configuring RADIUS Server Status Detection
=====================================================

(Optional) Configuring RADIUS Server Status Detection

#### Context

RADIUS clients can detect the status of RADIUS servers and, based on the responses they receive, determine the real-time status of the servers. This helps identify which servers are in the Up state so that user request packets can be processed in real time.

The configuration is valid for all RADIUS servers.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**radius-server**](cmdqueryname=radius-server) { **dead-count** *count* [ **fail-rate** *fail-rate* ] | **dead-time** *dead-time* [ **recover-count** **invalid** ] | **dead-interval** *interval* }\*
   
   
   
   Parameters are configured for determining whether the state of a RADIUS server changes from Up to Down.
   
   
   
   If the device consecutively sends RADIUS packets to the RADIUS server for a number of times specified by **dead-count** but receives no response and the interval between the first ignored packet and the nth ignored packet where n is equal to **dead-count** is longer than the value of **dead-interval**, the device considers that the RADIUS server is abnormal. In this case, the device sets the state of the RADIUS server to Down.
3. Configure a mode for restoring the Up state of the RADIUS server after its state is set to Down.
   
   
   
   **Table 1** Configuring a mode for restoring the Up state of the RADIUS server after its state is set to Down
   | Operation | Command | Description |
   | --- | --- | --- |
   | Configure automatic recovery of the RADIUS server state. | [**radius-server**](cmdqueryname=radius-server%28%E7%B3%BB%E7%BB%9F%E8%A7%86%E5%9B%BE%29) **dead-time** *time-value* [ **recover-count invalid** ] | After the device sets the state of a RADIUS server to Down, the device waits a period specified by **dead-time**. The device then sets the state of the RADIUS server to Up and attempts to set up a connection with it. If the connection cannot be set up, the device sets the state of the RADIUS server to Down again. |
   | Configure RADIUS server state detection and restoration. | [**radius-server state-recovery-detect**](cmdqueryname=radius-server+state-recovery-detect) { **authentication** | **accounting** } **username** *username* [ **detect-interval** *detect-interval* ] [ **detect-threshold** *detect-threshold* ] | Run this command to enable RADIUS server state detection and restoration so that the device can accurately determine the state of the RADIUS server. The device then sends detection packets to the RADIUS server at an interval specified by **detect-interval**. If detection succeeds for a consecutive number of times specified by **detect-threshold**, the device sets the RADIUS server state to Up again.  NOTE:  After this command is run, the [**radius-server**](cmdqueryname=radius-server) **dead-time** *dead-time* [ **recover-count invalid** ] command does not take effect. That is, the RADIUS server state will not be automatically set to Up after the period specified by **dead-time** expires. |
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.