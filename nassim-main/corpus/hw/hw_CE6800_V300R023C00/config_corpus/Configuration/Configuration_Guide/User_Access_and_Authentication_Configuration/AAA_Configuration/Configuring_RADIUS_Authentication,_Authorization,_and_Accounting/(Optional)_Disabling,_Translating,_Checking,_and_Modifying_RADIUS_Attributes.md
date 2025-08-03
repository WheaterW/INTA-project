(Optional) Disabling, Translating, Checking, and Modifying RADIUS Attributes
============================================================================

(Optional) Disabling, Translating, Checking, and Modifying RADIUS Attributes

#### Context

RADIUS attributes supported by different vendors are incompatible with each other, and therefore often need to be disabled, translated, checked, or modified when devices of different vendors need to be connected or replaced with each other.


#### Procedure

* Disable RADIUS attributes.
  
  
  1. Enter the system view.
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the RADIUS server template view.
     ```
     [radius-server template](cmdqueryname=radius-server+template) template-name
     ```
  3. Enable the function of disabling and translating RADIUS attributes.
     
     ```
     [radius-server attribute translate](cmdqueryname=radius-server+attribute+translate)
     ```
     
     By default, the function of disabling and translating RADIUS attributes is disabled.
  4. Configure the RADIUS attributes to be disabled.
     
     ```
     [radius-attribute disable](cmdqueryname=radius-attribute+disable) attribute-name { receive | send } *
     ```
     
     By default, no RADIUS attribute is disabled.
  5. Return to the user view.
     
     ```
     [return](cmdqueryname=return)
     ```
  6. Commit the configuration.
     ```
     commit
     ```
* Configure the device to translate RADIUS attributes.
  
  
  1. Enter the system view.
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the RADIUS server template view.
     ```
     [radius-server template](cmdqueryname=radius-server+template) template-name
     ```
  3. Enable the function of disabling and translating RADIUS attributes.
     
     ```
     [radius-server attribute translate](cmdqueryname=radius-server+attribute+translate)
     ```
     
     By default, the function of disabling and translating RADIUS attributes is disabled.
  4. Configure the device to translate RADIUS attributes.
     
     **Table 1** Three methods for translating RADIUS attributes
     | Operation | Command | Description |
     | --- | --- | --- |
     | Translate between the RADIUS attributes supported by default on the device. | [**radius-attribute translate**](cmdqueryname=radius-attribute+translate) *src-attribute-name* *dest-attribute-name* { **receive** | **send** | **access-accept** | **access-request** | **account-request** | **account-response** } \* | A device translates only the RADIUS attributes that it sends and receives. |
     | Translate the RADIUS attributes supported by the device into those of other vendors. | [**radius-attribute translate**](cmdqueryname=radius-attribute+translate) **extend** *src-attribute-name* **vendor-specific** *dest-vendor-id* *dest-sub-id* { **access-request** | **account-request** } \* | A device translates only the RADIUS attributes that it sends. |
     | Translate the RADIUS attributes of other vendors into those supported by the device. | [**radius-attribute translate**](cmdqueryname=radius-attribute+translate) **extend** **vendor-specific** *src-vendor-id* *src-sub-id* *dest-attribute-name* { **access-accept** | **account-response** } \* | A device translates only the RADIUS attributes that it receives. |
  5. Return to the user view.
     
     ```
     [return](cmdqueryname=return)
     ```
  6. Commit the configuration.
     ```
     commit
     ```
* Configure the device to check RADIUS attributes.
  
  
  1. Enter the system view.
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the RADIUS server template view.
     ```
     [radius-server template](cmdqueryname=radius-server+template) template-name
     ```
  3. Configure the device to check whether the received RADIUS Access-Accept packets contain specific attributes.
     
     ```
     [radius-attribute check](cmdqueryname=radius-attribute+check) attribute-name
     ```
     
     By default, the device does not check received RADIUS Access-Accept packets.
  4. Return to the user view.
     
     ```
     [return](cmdqueryname=return)
     ```
  5. Commit the configuration.
     ```
     commit
     ```
* Configure the device to modify RADIUS attributes.
  
  
  1. Enter the system view.
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the RADIUS server template view.
     ```
     [radius-server template](cmdqueryname=radius-server+template) template-name
     ```
  3. Configure the device to change the value of a specified RADIUS attribute.
     
     ```
     [radius-attribute set](cmdqueryname=radius-attribute+set) attribute-name attribute-value [ auth-type mac ]
     ```
     
     By default, the device does not change the values of RADIUS attributes.
     
     The **auth-type mac** parameter can be configured only for the RADIUS Service-Type attribute.
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     When the Access-Challenge packet sent by the RADIUS server contains EAP information longer than 1200 bytes, the terminal may fail to receive the EAP Request/Challenge packet. In this case, you can run this command to set *attribute-name* to Framed-MTU and reduce the Framed-MTU attribute value in the Access-Request packet sent by the device to the RADIUS server. The Framed-MTU attribute value defaults to 1500 and can be changed to 1000.
  4. Return to the user view.
     
     ```
     [return](cmdqueryname=return)
     ```
  5. Commit the configuration.
     ```
     commit
     ```