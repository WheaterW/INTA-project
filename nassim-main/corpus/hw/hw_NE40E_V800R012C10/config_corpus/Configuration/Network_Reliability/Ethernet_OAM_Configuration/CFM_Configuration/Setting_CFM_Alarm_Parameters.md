Setting CFM Alarm Parameters
============================

This section describes how to set connectivity fault management (CFM) alarm parameters, which include the alarm generation and clearing anti-jitter times.

#### Context

You can set CFM alarm parameters so that CFM sends link fault alarms to a network management system (NMS). A network administrator can take measures based on the alarm information displayed on the NMS.

[Table 1](#EN-US_TASK_0172361949__tab_dc_vrp_cfm_cfg_00002701) describes CFM alarm parameters.

**Table 1** CFM alarm parameters
| Parameter | Description |
| --- | --- |
| Alarm generation anti-jitter time | When a maintenance association end point (MEP) detects a link fault:  * It sends an alarm to an NMS after a specified alarm generation anti-jitter time elapses. * It does not send an alarm if the fault is rectified within a specified alarm generation anti-jitter time. |
| Alarm clearing anti-jitter time | When a MEP detects a link fault and sends an alarm:  * It sends a clear alarm if the fault is rectified within a specified alarm clearing anti-jitter time. * It does not send a clear alarm if the fault is not rectified within a specified alarm clearing anti-jitter time. |



#### Pre-configuration Tasks

Before setting CFM alarm parameters, run the [**ma**](cmdqueryname=ma) *ma-name* command to create a maintenance association (MA).


#### Procedure

* Configure an alarm generation anti-jitter time.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**cfm md**](cmdqueryname=cfm+md) *md-name*
     
     
     
     The maintenance domain (MD) view is displayed.
  3. Run [**ma**](cmdqueryname=ma) *ma-name*
     
     
     
     The MA view is displayed.
  4. Run [**alarm occur time**](cmdqueryname=alarm+occur+time) *time*
     
     
     
     An alarm generation anti-jitter time is configured.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure an alarm clearing anti-jitter time.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**cfm md**](cmdqueryname=cfm+md) *md-name*
     
     
     
     The MD view is displayed.
  3. Run [**ma**](cmdqueryname=ma) *ma-name*
     
     
     
     The MA view is displayed.
  4. Run [**alarm finish time**](cmdqueryname=alarm+finish+time) *time*
     
     
     
     An alarm clearing anti-jitter time is configured.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.