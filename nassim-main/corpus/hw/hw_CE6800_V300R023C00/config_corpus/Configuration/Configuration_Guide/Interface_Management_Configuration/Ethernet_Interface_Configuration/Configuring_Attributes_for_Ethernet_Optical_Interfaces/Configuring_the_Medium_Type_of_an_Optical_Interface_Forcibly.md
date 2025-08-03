Configuring the Medium Type of an Optical Interface Forcibly
============================================================

Configuring the Medium Type of an Optical Interface Forcibly

#### Context

CloudEngine series switches must use the optical modules certified for Huawei data center switches. If an optical module that is not certified for Huawei data center switches is used, the system may incorrectly identify the medium type. You can forcibly set the medium type of an optical interface to the actual medium type.

![](public_sys-resources/notice_3.0-en-us.png) 

* After the medium type is forcibly changed, the medium may not work properly. To ensure that the interface works properly, you are advised to use the optical modules certified for Huawei data center switches.
* If the forcibly configured medium is a high-speed cable but an optical module is installed, the optical module may be damaged. Ensure that the configured medium type is the same as the type of an installed medium.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the optical interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Configure the medium type of the optical interface forcibly.
   
   
   ```
   [force transceiver](cmdqueryname=force+transceiver) transceiver-type
   ```
   
   By default, no medium type is forcibly configured for optical interfaces.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The *transceiver-type* parameter does not distinguish models. For example, 10GBASE-FIBER indicates a 10GE optical module. All 10GE optical modules, such as 10GBASE-LR and 10GBASE-SR, have the same medium type.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the **display interface** [ *interface-type* *interface-number* | **slot** *slot-id* ] **transceiver** [ **verbose** ] command in the interface view to check the optical module type.