Configuring the Time Synchronization Function on an Atom GNSS Module
====================================================================

This section describes how to configure the time synchronization function on an Atom GNSS module so that GNSS time signals can be transmitted to the Router where the Atom GNSS module resides through 1588v2 packets and then to downstream devices.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The attributes that can be configured on an Atom GNSS module are the clock domain and priority1 and priority2 of the time source.

* The class of a clock source cannot be specified. The initial class 248 is used by default when a clock source goes online. After the clock source successfully traces GNSS signals, its class changes to 6 (a device using a class-6 clock source cannot be the secondary devices of other clocks in the clock domain). After the clock source loses track of GNSS signals, its class changes to 248 again.
* The accuracy of a clock source cannot be specified. The initial value 0xFE is used by default when a clock source goes online. After the clock source successfully traces GNSS signals, its accuracy changes to 0x21 (specific to 100 ns). After the clock source loses track of GNSS signals, its class changes to 0xFE again.
* The stability of a clock source cannot be configured. The value is 0xFFFF (if T-GM is not connected to ePRTC).

Perform the following operations on the Router where the Atom GNSS module resides:


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface view.
3. Run the [**smart-clock gnss-model**](cmdqueryname=smart-clock+gnss-model) { **gps** | **glonass** | **beidou** | **gps-glonass** | **gps-beidou** } [ **gps** | **glonass** | **beidou** | **gps-glonass** | **gps-beidou** ] [ **gps** | **glonass** | **beidou** | **gps-glonass** | **gps-beidou** ] [ **gps** | **glonass** | **beidou** | **gps-glonass** | **gps-beidou** ] [ **gps** | **glonass** | **beidou** | **gps-glonass** | **gps-beidou** ] command to configure a working mode for the Atom GNSS module.
4. Run the [**smart-clock cable-delay**](cmdqueryname=smart-clock+cable-delay) *delay-value* command to configure the feeder delay compensation value for the Atom GNSS module.
5. (Optional) Run the [**smart-clock leap manual-mode enable**](cmdqueryname=smart-clock+leap+manual-mode+enable) command to configure the Atom GNSS module to obtain leap seconds in manual mode.
6. (Optional) Run the [**smart-clock leap current-leap**](cmdqueryname=smart-clock+leap+current-leap) *current-leap-value* [ { **leap59** | **leap61** } **date** *date* ] command to configure the current leap second value of the Atom GNSS module as well as the direction and date of the next leap second adjustment.
7. (Optional) Run the [**smart-clock ptp domain**](cmdqueryname=smart-clock+ptp+domain) *domain-value* command to configure a clock domain for the Atom GNSS module.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   By default, the clock domain in 1588v2 mode is 0, and the clock domain in G.8275.1 mode is 24. Therefore, you need to change the clock domain of the Atom GPS module to be the same as that on the network. Otherwise, the interconnection fails.
8. (Optional) Run the [**smart-clock ptp**](cmdqueryname=smart-clock+ptp) { **priority1** *priority1-value* | **priority2** *priority2-value* } command to configure the time source priority1 or priority2 for the Atom GNSS module.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   When you plan network tracing by modifying the time source priority of a module, you are advised to configure **priority2** *priority2-value* instead of **priority1** *priority1-value*. If **priority1** *priority1-value* is configured, source switching cannot be performed in case of a quality decrease.
9. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.