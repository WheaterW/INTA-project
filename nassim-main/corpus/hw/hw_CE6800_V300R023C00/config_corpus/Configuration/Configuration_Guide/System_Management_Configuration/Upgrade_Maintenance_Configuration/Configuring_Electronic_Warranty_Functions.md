Configuring Electronic Warranty Functions
=========================================

Configuring Electronic Warranty Functions

#### Context

Electronic warranties are provided for devices to record the service life of products and related components, better serving users in the information age. You can activate electronic warranties and check the recorded hardware activation date, committed hardware service life, and hardware warranty status.

![](public_sys-resources/note_3.0-en-us.png) 

To facilitate the maintenance of product service life information during product inventory management and service processes, an electronic warranty is provided to each live-network device.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the warranty view.
   
   
   ```
   [warranty](cmdqueryname=warranty)
   ```
3. Activate the electronic warranty.
   
   
   ```
   [import warranty file](cmdqueryname=import+warranty+file) ewmfile
   ```
   
   By default, electronic warranties are not activated.
4. Enable the alarm function for electronic warranties.
   
   
   ```
   [undo alarm disable](cmdqueryname=undo+alarm+disable)
   ```
   
   By default, the alarm function is enabled for electronic warranties. If the alarm function needs to be disabled, reactivate the electronic warranties within the service life to clear alarms first.
   
   After the alarm function is enabled:
   
   * The **hwWarrantyToBeExpired** alarm is reported when the service life of a device is about to expire.
   * The **hwWarrantyExpired** alarm is reported when the service life of a device expires.
   * The **hwWarrantyMissingSession** alarm is reported when the service life information of a device is missing.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display warranty**](cmdqueryname=display+warranty) [ [**device**](cmdqueryname=device) | [**parts**](cmdqueryname=parts) [ [**slot**](cmdqueryname=slot) *slot-id* ] ] command to check information about activated electronic warranties in the system.

Run the [**display warranty software**](cmdqueryname=display+warranty+software) command to check information about the software electronic warranty.