Enabling RIPng on an Interface
==============================

After an interface is associated with a RIPng process,
routing information on this interface can be exchanged through RIPng.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
   
   The interface is on the
   network side of the Router. Specifically, the Router is connected to other devices through this interface. To enable
   the Router to learn the routes to the network segment where this interface
   resides, ensure that the link status of the interface is Up.
3. Run [**ripng**](cmdqueryname=ripng) *process-id* **enable**
   
   
   
   RIPng is enabled on the specified
   interface.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * In the interface view, this command cannot be executed if IPv6
     has not been enabled on the interface.
   * If the Router is connected to other devices through multiple interfaces, repeatedly
     perform Step 2 and Step 3.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration
   is submitted.