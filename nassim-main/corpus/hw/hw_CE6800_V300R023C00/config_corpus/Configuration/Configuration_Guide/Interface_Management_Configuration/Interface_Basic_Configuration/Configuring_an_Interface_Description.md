Configuring an Interface Description
====================================

Configuring an Interface Description

#### Context

To facilitate device management and maintenance, you can configure descriptions for interfaces. An interface description can contain details about the device where the interface is located, interface type, and remote device.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) { interface-name | interface-type interface-number }
   ```
3. Configure a description for the interface.
   
   
   ```
   [description](cmdqueryname=description) description
   ```
   
   The interface description is displayed from the first non-space character.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display interface description**](cmdqueryname=display+interface+description) [ *interface-name* | *interface-type* [ *interface-number* ] ] command to check the description of an interface.