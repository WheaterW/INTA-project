Verifying the Configuration of the QinQ-based BPDU Tunneling Function
=====================================================================

After configuring QinQ-based bridge protocol data unit (BPDU) tunneling, verify the configuration (QinQ is short for 802.1Q in 802.1Q).

#### Prerequisites

QinQ-based BPDU tunneling has been configured.
#### Procedure

* Run the [**display bpdu-tunnel interface config**](cmdqueryname=display+bpdu-tunnel+interface+config) command to check BPDU tunneling configuration on an interface.
* Run the [**display bpdu-tunnel global config**](cmdqueryname=display+bpdu-tunnel+global+config) command to check BPDU tunneling configuration globally.
* Run the [**display stp**](cmdqueryname=display+stp) [ **brief** ] command to check spanning tree information.
* Run the [**display vlan**](cmdqueryname=display+vlan) [ *vlan-id* [ **verbose** ] ] command to check VLAN information.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  + The [**display bpdu-tunnel global config**](cmdqueryname=display+bpdu-tunnel+global+config) command can be run only in the system view.
  + The [**display bpdu-tunnel interface config**](cmdqueryname=display+bpdu-tunnel+interface+config) command can be run only in the interface view.