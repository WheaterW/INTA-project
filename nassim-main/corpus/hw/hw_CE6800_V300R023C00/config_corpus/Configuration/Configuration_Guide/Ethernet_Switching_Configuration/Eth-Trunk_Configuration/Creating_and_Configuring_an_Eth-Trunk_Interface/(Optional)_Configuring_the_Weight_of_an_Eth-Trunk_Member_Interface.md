(Optional) Configuring the Weight of an Eth-Trunk Member Interface
==================================================================

(Optional) Configuring the Weight of an Eth-Trunk Member Interface

#### Context

Traffic is distributed to the member interfaces of an Eth-Trunk interface according to their configured weights. The higher the weight of a member interface, the heavier the load over the corresponding member link. To increase the volume of the traffic load balanced by a member interface, you can configure the weight for this interface.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the view of an Eth-Trunk member interface.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Configure the weight of the Eth-Trunk member interface.
   
   
   ```
   [distribute-weight](cmdqueryname=distribute-weight) weight-value
   ```
   
   
   
   The default weight value of an Eth-Trunk member interface is 1.
   
   The sum weight of all member interfaces of an Eth-Trunk interface cannot exceed the maximum number of member interfaces supported by the Eth-Trunk interface.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```