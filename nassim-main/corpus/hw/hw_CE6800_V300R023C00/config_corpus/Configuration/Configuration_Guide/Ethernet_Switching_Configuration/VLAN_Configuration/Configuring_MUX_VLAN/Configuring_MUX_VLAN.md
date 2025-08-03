Configuring MUX VLAN
====================

Configuring MUX VLAN

#### Prerequisites

Before configuring MUX VLAN, you have completed the following tasks:

1. Create VLANs.
2. Add interfaces to the VLANs as access, hybrid, or trunk interfaces.

#### Context

MUX VLAN involves the concepts of principal, group, and separate VLANs. They have the following characteristics:

* Ports in the principal VLAN can communicate with all ports in the MUX VLAN.
* Ports in a group VLAN can communicate with each other and with ports in the principal VLAN, but cannot communicate with ports in other group VLANs or separate VLANs.
* Ports in a separate VLAN can communicate with only ports in the principal VLAN.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a VLAN and enter the VLAN view.
   
   
   ```
   [vlan](cmdqueryname=vlan) vlan-id
   ```
3. Configure the VLAN as a principal VLAN.
   
   
   ```
   [mux-vlan](cmdqueryname=mux-vlan)
   ```
4. Configure a group VLAN.
   
   
   ```
   [subordinate group](cmdqueryname=subordinate+group) { vlan-id1 [ to vlan-id2 ] } &<1-10>
   ```
5. Configure a separate VLAN.
   
   
   ```
   [subordinate separate](cmdqueryname=subordinate+separate) vlan-id
   ```
6. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
7. Enable the MUX VLAN function on an interface. To configure this function on multiple interfaces, repeat this step.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   [port mux-vlan enable vlan](cmdqueryname=port+mux-vlan+enable+vlan) { vlan-id1 [ to vlan-id2 ] } &<1-10>
   [quit](cmdqueryname=quit)
   ```
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display mux-vlan**](cmdqueryname=display+mux-vlan) command to check the MUX VLAN configuration.