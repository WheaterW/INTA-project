Configuring an Eth-Trunk Member Interface as a Force-Up Interface When a Device Connects to a Server
====================================================================================================

Configuring an Eth-Trunk Member Interface as a Force-Up Interface When a Device Connects to a Server

#### Context

When a device directly connects to a server using an Eth-Trunk member interface in static LACP mode, if the server restarts or goes online, this interface will go down as it will not receive LACPDUs from the server within the timeout period. In this situation, you can configure Eth-Trunk member interfaces as force-up interfaces so that the interfaces can continue to forward traffic even if it does not receive LACPDUs from the server.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the view of an Eth-Trunk member interface.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Configure Eth-Trunk member interfaces as force-up interfaces.
   
   
   ```
   [lacp force-up](cmdqueryname=lacp+force-up) [ extension ]
   ```
   
   This function is disabled by default.
   
   If the **extension** parameter is specified, the force-up function takes effect only once. This prevents packet loss when a server interface is incorrectly connected or an Eth-Trunk member interface is removed from the Eth-Trunk interface by mistake. If the interface changes from down to up later, the force-up function takes effect again.
   
   With this function enabled, Eth-Trunk member interface will enter the force-up state only when the Eth-Trunk interface works in static LACP mode and all member interfaces do not receive LACPDUs from the server within the specified timeout period.
   
   When all Eth-Trunk member interfaces enter the force-up state, the lower threshold for the number of active interfaces configured using the [**least active-linknumber**](cmdqueryname=least+active-linknumber) *link-number* command takes effect, but the upper threshold for the number of active interfaces configured using the [**lacp max active-linknumber**](cmdqueryname=lacp+max+active-linknumber) *link-number* command does not take effect.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```