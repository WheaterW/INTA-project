Configuring ATM Forced Traffic Classification
=============================================

This section describes how to configure asynchronous transfer
mode (ATM) forced traffic classification. ATM forced traffic classification
can be configured on ATM interfaces, ATM sub-interfaces, permanent
virtual circuits (PVCs), and permanent virtual paths (PVPs).

#### Context

Perform the following steps on the Router on which ATM forced traffic classification is required:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run any of the following commands on the Router:
   
   
   * To enter the ATM interface view, run the [**interface**](cmdqueryname=interface) **atm** *interface-number* command.
   * To create an ATM sub-interface and enter the ATM sub-interface
     view, run the [**interface**](cmdqueryname=interface) **atm** *interface-number.sub-interface* command.
   * To create a PVC or PVP and enter the PVC or PVP view, run the [**pvc**](cmdqueryname=pvc) [ *pvc-name* ] *vpi/vci* or [**pvp**](cmdqueryname=pvp) *vpi* command in the ATM sub-interface
     view.
3. Run [**traffic queue**](cmdqueryname=traffic+queue) *service-class* { **green** | **red** | **yellow** }
   
   
   
   ATM forced traffic classification is configured on
   the upstream interface.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The value of the *service class* parameter determines whether the *color* parameter
   must be specified:
   
   * If the value of *service class* is **AF1**, **AF2**, **AF3**, or **AF4**, you must specify the *color* parameter.
   * If the value of *service class* is **CS7**, **CS6**, **EF**, or **BE**, you cannot specify the *color* parameter.
   
   *color* has the following values:
   
   * **green**: indicates the action to take
     for data packets when the traffic rate is smaller than or equal to
     the committed information rate (CIR). The default action is **pass**.
   * **yellow**: indicates the action to take
     for data packets when the traffic rate is smaller than or equal to
     the peak information rate (PIR). The default action is **pass**.
   * **red**: indicates the action to take for
     data packets when the traffic rate exceeds the PIR. The default action
     is **discard**.
4. Run [**return**](cmdqueryname=return)
   
   
   
   Return to the user view.
5. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
6. Run [**interface**](cmdqueryname=interface) **interface-type** *interface-number* [.*subinterface-number* ]
   
   
   
   The downstream
   interface view is displayed.
7. Run [**trust upstream**](cmdqueryname=trust+upstream) **default**
   
   
   
   The default
   domain is applied to the downstream interface so that the downstream
   interface trusts ATM forced traffic classification.