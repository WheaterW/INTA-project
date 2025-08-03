Activating and Viewing Digital Warranties
=========================================

Digital warranties record the service life of devices and components. Users can activate and view the digital warranties on devices.

#### Context

Digital warranties record the service life of devices and components. Users can process the information about the service life in digital warranties to support the market lifecycle management.

In VS mode, only the admin VS supports the following procedure.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**warranty**](cmdqueryname=warranty) command to enter the electronic warranty view.
3. Run the [**import warranty**](cmdqueryname=import+warranty) **file** *ewmfile* command to activate the electronic warranty based on the imported file.
4. (Optional) Run the [**undo alarm disable**](cmdqueryname=undo+alarm+disable) command to enable the alarm function for the digital warranty.
5. Run the [**display warranty**](cmdqueryname=display+warranty) [ **device** | **parts** [ **slot** *slot-id* ] ] command to check information about the activated digital warranties of the device or a specified board.