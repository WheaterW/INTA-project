Configuring DLDP Timers
=======================

Configuring DLDP Timers

#### Context

DLDP maintains neighbor relationships by sending and receiving Advertisement packets. You can set an appropriate interval for sending such packets to ensure that DLDP promptly detects unidirectional links in different network environments. Upon detecting an interface down event, a DLDP-enabled interface in the Active, Advertisement, or Probe state immediately enters the Inactive state and deletes the neighbor entry. You can set a timeout period for the DelayDown timer to prevent the interface from entering the Inactive state immediately.

If a DLDP-enabled interface in the Active, Advertisement, or Probe state detects an interface down event (such as a Tx fiber fault), optical signal jitter on the Rx fiber may cause an interface to go down and back up again. To prevent the DLDP-enabled interface from directly entering the Inactive state and deleting the neighbor entry, the DelayDown timer can be set. In this case, the DLDP-enabled interface first enters the DelayDown state and starts the DelayDown timer. Before the DelayDown timer times out, the interface retains the neighbor entry and responds to only interface up events.

* If no interface up event is detected before the DelayDown timer times out, the interface deletes the neighbor entry and enters the Inactive state.
* If an interface up event is detected before the DelayDown timer times out, the interface changes its state from DelayDown to its original Active, Advertisement, or Probe state.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface or interface group view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   [port-group](cmdqueryname=port-group) port-group-name
   ```
3. Switch the interface working mode from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch) 
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Set an interval for sending Advertisement packets.
   
   
   ```
   [dldp interval](cmdqueryname=dldp+interval) time
   ```
   
   
   
   The default interval for sending Advertisement packets is 5 seconds.
   
   You are advised to use the default interval. If a longer interval is set, STP loops may occur before DLDP can detect and shut down unidirectional links. Conversely, if a shorter interval is set, the traffic volume on the network increases.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The interval for sending Advertisement packets must be the same on both the local and remote devices that are connected through optical fibers or copper twisted pairs; otherwise, DLDP cannot work properly.
5. Set a timeout period for the DelayDown timer.
   
   
   ```
   [dldp delaydown-timer](cmdqueryname=dldp+delaydown-timer) time
   ```
   
   The default timeout value of the DelayDown timer is 1 second.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display dldp**](cmdqueryname=display+dldp) [ **interface** *interface-type* *interface-number* ] command to check the DLDP configuration and neighbor entries.
* Run the [**display dldp statistics**](cmdqueryname=display+dldp+statistics) [ **interface** *interface-type* *interface-number* ] command to check statistics about DLDPDUs on all interfaces or a specific one.
* Run the [**display fwm dldp statistics**](cmdqueryname=display+fwm+dldp+statistics) [ **all** ] **slot** *slot-id* command in any view to check statistics about the DLDP module on a specified board.