Verifying the Configuration
===========================

After configuring VLAN-based bridge protocol data unit (BPDU) tunneling, verify the configuration (VLAN is short for virtual local area network).

#### Prerequisites

VLAN-based BPDU tunneling has been configured.


#### Procedure

* Run the [**display bpdu-tunnel interface config**](cmdqueryname=display+bpdu-tunnel+interface+config) command to check BPDU tunneling configuration on an interface.
* Run the [**display bpdu-tunnel global config**](cmdqueryname=display+bpdu-tunnel+global+config) command to check the global BPDU tunneling configuration.
* Run the [**display stp**](cmdqueryname=display+stp) [ **brief** ] command to check spanning tree information.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  + The [**display bpdu-tunnel global config**](cmdqueryname=display+bpdu-tunnel+global+config) command can be run only in the system view.
  + The [**display bpdu-tunnel interface config**](cmdqueryname=display+bpdu-tunnel+interface+config) command can be run only in the interface view.