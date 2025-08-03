Configuring IP Unnumbered on an Interface
=========================================

Configuring IP Unnumbered on an Interface

#### Context

To save IP address resources, you can configure IP unnumbered on an interface to borrow an IP address from another interface. For example, if an interface is rarely used, configure IP unnumbered on this interface to enable the interface to share an IP address with another interface. An unnumbered interface cannot run dynamic routing protocols because it does not have an IP address itself. To enable the interface to communicate with a remote device, you must configure a static route to the network segment of the remote device.

An Ethernet interface can borrow the IP address of another interface.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the unnumbered interface view.
   
   
   ```
   [interface](cmdqueryname=interface) { interface-name | interface-type interface-number } 
   ```
3. Switch the interface working mode to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
4. Configure IP unnumbered on the interface.
   
   
   ```
   [ip address unnumbered](cmdqueryname=ip+address+unnumbered+interface) interface { interface-name | interface-type interface-number }
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```