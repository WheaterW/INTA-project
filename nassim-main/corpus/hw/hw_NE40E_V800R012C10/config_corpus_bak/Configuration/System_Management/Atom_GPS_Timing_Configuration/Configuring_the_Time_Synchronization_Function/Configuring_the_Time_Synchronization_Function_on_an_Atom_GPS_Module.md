Configuring the Time Synchronization Function on an Atom GPS Module
===================================================================

This section describes how to configure the time synchronization function on an Atom GPS module so that GPS time signals can be transmitted to the Router where the Atom GPS module resides through 1588v2 packets and then to downstream devices.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The attributes that can be configured on an Atom GPS module are the clock domain and priority1 and priority2 of the time source.

* The class of a clock source cannot be specified. The initial class 248 is used by default when a clock source goes online. After the clock source successfully traces GPS signals, its class changes to 6 (a device using a class-6 clock source cannot be the secondary devices of other clocks in the clock domain). After the clock source loses track of GPS signals, its class changes to 248 again.
* The accuracy of a clock source cannot be specified. The initial value 0xFE is used by default when a clock source goes online. After the clock source successfully traces GPS signals, its accuracy changes to 0x21 (specific to 100 ns). After the clock source loses track of GPS signals, its class changes to 0xFE again.
* The stability of a clock source cannot be configured. The value is 0xFFFF (if T-GM is not connected to ePRTC).

Perform the following operations on the Router where the Atom GPS module resides:


#### Procedure

1. Run the **system-view** command to enter the system view.
2. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface view.
3. (Optional) Run the [**smart-clock ptp domain**](cmdqueryname=smart-clock+ptp+domain) *domain-value* command to configure a clock domain for the Atom GPS module.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   By default, the clock domain in 1588v2 mode is 0, and the clock domain in G.8275.1 mode is 24. Therefore, you need to change the clock domain of the Atom GPS module to be the same as that on the network. Otherwise, the interconnection fails.
4. (Optional) Run the [**smart-clock ptp**](cmdqueryname=smart-clock+ptp) { **priority1** *priority1-value* | **priority2** *priority2-value* } command to configure the time source priority1 or priority2 for the Atom GPS module.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   When you plan network tracing by modifying the time source priority of a module, you are advised to configure **priority2** *priority2-value* instead of **priority1** *priority1-value*. If **priority1** *priority1-value* is configured, source switching cannot be performed in case of a quality decrease.
5. Run the **commit** command to commit the configuration.