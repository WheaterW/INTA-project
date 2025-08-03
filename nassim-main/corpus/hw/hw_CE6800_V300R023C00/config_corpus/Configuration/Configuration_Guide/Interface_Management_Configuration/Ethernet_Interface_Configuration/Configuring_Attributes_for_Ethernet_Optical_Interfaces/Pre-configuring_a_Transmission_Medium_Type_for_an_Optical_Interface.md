Pre-configuring a Transmission Medium Type for an Optical Interface
===================================================================

Pre-configuring a Transmission Medium Type for an Optical Interface

#### Context

Some functions can be configured on an optical interface only after the interface connects to a transmission medium (such as an optical module or copper module). Therefore, optical interfaces must connect to transmission media before configuration of these functions. Sometimes the installation and configuration personnel are different. The configuration personnel can configure services only after the installation personnel install the transmission media on interfaces, lengthening the time of service deployment. To shorten the service deployment time, the configuration personnel can pre-configure a transmission medium type on optical interfaces and then configure functions on the interfaces. These functions subsequently take effect after the installation personnel install the correct transmission media on the interfaces. This way, configuration can be more flexible.

A transmission medium type can be pre-configured for an optical interface only when the interface does not connect to a transmission medium. If the type of the installed transmission medium is the same as the pre-configured one, the interface has met the condition to go up, and the later configurations can take effect. If the types are different, the installed transmission medium type is preferentially used.

![](public_sys-resources/notice_3.0-en-us.png) 

* If the pre-configured transmission medium is a high-speed cable but an optical module is installed, the optical module may be damaged. Ensure that the installed transmission medium is the same as the pre-configured transmission medium.
* If the type of the installed optical module is unknown, a device cannot identify the optical module. Only when the pre-configured transmission medium and the installed optical module have the same bandwidth can the interface go up. To ensure that the interface works properly, you are advised to use Huawei-certified optical modules.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
   
   
   
   Enter the corresponding interface view based on the interface type to be configured.
3. Pre-configure a transmission medium type for the interface.
   
   
   ```
   [device transceiver](cmdqueryname=device+transceiver) transceiver-type
   ```
   
   
   
   By default, no transmission medium type is pre-configured for interfaces.
4. (Optional) Bring up the current interface.
   
   
   ```
   [undo shutdown](cmdqueryname=undo+shutdown)
   ```
   
   Perform this step only when the current optical interface is shut down.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display this**](cmdqueryname=display+this) command in the interface view to check information about the pre-configured transmission medium.