Configuring MEth Management Interface Attributes
================================================

Configuring MEth Management Interface Attributes

#### Context

The MEth management interface is a special Ethernet interface used to log in to a device to perform configuration and management. This interface does not transmit services.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the MEth management interface view.
   
   
   ```
   [interface](cmdqueryname=interface) [meth](cmdqueryname=meth) 0/0/0
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The working MEth management interface is displayed as the logical management interface MEth0/0/0. To check the status of a physical management interface or determine the working management interface if there are multiple MEth management interfaces, run the [**display interface**](cmdqueryname=display+interface) *meth* [**status**](cmdqueryname=status) command.
3. Configure an IP address for the MEth management interface.
   
   
   ```
   [ip address](cmdqueryname=ip+address) ip-address { mask | mask-length } [ sub ][ [tag](cmdqueryname=tag) tag-value ]
   ```
4. (Optional) Disable auto-negotiation and set a working speed for the MEth management interface.
   
   
   ```
   [negotiation disable](cmdqueryname=negotiation+disable)
   [speed](cmdqueryname=speed) { 10 | 100 | 1000 }
   ```
   
   By default, an interface works in auto-negotiation mode.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If interface hardware complies with auto-negotiation standards, it is recommended that Ethernet interfaces work in auto-negotiation mode.
   
   Manually setting interface rates usually complicates network planning and maintenance, and improper settings will affect or even interrupt the network communication.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```