(Optional) Configuring a One-Click Test for ATM Services
========================================================

After ATM cell relay has been configured on an ATM interface or a logical interface that runs the ATM protocol, a one-click test can be configured for ATM services.

#### Context

Before configuring a one-click test for ATM services, you must complete the following tasks:

1. Check that the physical layer status and protocol layer status of the interface on which the one-click test will be performed are Up. If the interface is a synchronous serial interface, configure ATM on the interface.
2. Configure a PVC or PVP on the interface.
3. Run the [**llid**](cmdqueryname=llid) command to configure a local LLID for both the local end and peer end.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**test connectivity**](cmdqueryname=test+connectivity) **interface** *interface-type* *interface-number* { **pvc** *vpi/vci* | **pvp** *vpi* } **llid** *llid*
   
   
   
   A one-click test is configured for ATM services.

#### Result

Run the [**display connectivity-test**](cmdqueryname=display+connectivity-test) **interface** *interface-type* *interface-number* { **pvc** *vpi/vci* | **pvp** *vpi* } command to check the one-click test results for ATM services.