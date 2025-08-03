Setting a Router ID
===================

Setting a Router ID

#### Context

A router ID is a 32-bit IP address that uniquely identifies a routing device in an AS. The rules for selecting a router ID are as follows:

* A router ID is manually configured on a public or private network.
* A router ID is specified for a routing protocol.
* A router ID is automatically selected.

To improve network stability, you are advised to manually set the router ID to the IP address of a loopback interface. If the router ID of a device on the network is the IP address of a physical interface, route flapping occurs once the IP address changes.

The router ID specified for a protocol takes precedence over the one configured in the system view. A protocol uses the router ID configured in the system view only when no router ID is configured for the protocol. If the router ID is changed, a protocol adopts this new router ID only after the **reset** command is run.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Set a router ID.
   
   
   ```
   [router id](cmdqueryname=router+id) router-id
   ```
   
   
   
   The default router ID is 0.0.0.0.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display router id**](cmdqueryname=display+router+id) command to check the router ID of the device.