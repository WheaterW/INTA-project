Configuring Unidirectional Isolation from the Access Side to the Tunnel Side
============================================================================

Configuring Unidirectional Isolation from the Access Side to the Tunnel Side

#### Context

On a VXLAN network, users in the same BD can directly communicate with each other. To isolate unidirectional traffic from the access side to the tunnel side in a BD, you can configure unidirectional isolation from the access side to the tunnel side.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a BD and enter its view.
   
   
   ```
   [bridge-domain](cmdqueryname=bridge-domain) bd-id
   ```
   
   By default, no BD is created.
3. Enable unidirectional isolation from the access side to the tunnel side in the BD.
   
   
   ```
   [isolate remote enable](cmdqueryname=isolate+remote+enable)
   ```
   
   By default, unidirectional isolation from the access side to the tunnel side is not configured in a BD.
4. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
5. (Optional) If users who access a BD through a VLAN need to communicate with the tunnel side, set the access-side mode of the VLAN to hub. 
   1. Create a VLAN and enter the VLAN view. If the VLAN already exists, this command will directly display the VLAN view.
      
      
      ```
      [vlan](cmdqueryname=vlan) vlan-id
      ```
   2. Set the access-side mode to hub.
      
      
      ```
      [hub-mode enable](cmdqueryname=hub-mode+enable)
      ```
      ![](../public_sys-resources/note_3.0-en-us.png) 
      
      Before setting the access-side mode of a VLAN to hub, run the [**l2 binding vlan**](cmdqueryname=l2+binding+vlan) command in the BD view to bind the VLAN to the BD.
6. (Optional) If users who access a BD through a Layer 2 sub-interface need to communicate with the tunnel side, set the access-side mode of the Layer 2 sub-interface to hub.
   1. Create a Layer 2 sub-interface and enter its view. If a Layer 2 sub-interface has been created, this command directly displays the Layer 2 sub-interface view.
      
      
      ```
      
      [interface](cmdqueryname=interface) interface-type interface-number.subnum mode l2
      ```
   2. Set the access-side mode to hub.
      
      
      ```
      [hub-mode enable](cmdqueryname=hub-mode+enable)
      ```
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```