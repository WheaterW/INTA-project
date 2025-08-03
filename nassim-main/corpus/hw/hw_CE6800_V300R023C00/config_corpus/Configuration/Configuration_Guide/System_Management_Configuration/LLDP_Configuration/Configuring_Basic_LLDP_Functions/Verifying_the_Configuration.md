Verifying the Configuration
===========================

Verifying the Configuration

#### Prerequisites

All configurations of basic LLDP functions are complete.


#### Procedure

* Run the [**display lldp local**](cmdqueryname=display+lldp+local) [ **interface** *interface-type interface-number* ] command to check local LLDP status information about all interfaces or a specified interface.
* Run the [**display lldp neighbor**](cmdqueryname=display+lldp+neighbor) [ **interface** *interface-type interface-number* ] command to check LLDP status information about neighbors connected to all interfaces or the neighbor connected to a specified interface.
* Run the [**display lldp neighbor brief**](cmdqueryname=display+lldp+neighbor+brief) command to check brief information about neighboring nodes.
* Run the [**display lldp tlv-config**](cmdqueryname=display+lldp+tlv-config) [ **interface** *interface-type interface-number* ] command to check information about optional TLVs that can be advertised by all interfaces or a specified interface.
* Run the [**display lldp mdn local**](cmdqueryname=display+lldp+mdn+local) [ **interface** *interface-type interface-number* ] command to check the configurations and status information about MDN on all interfaces or a specified interface.
* Run the [**display lldp mdn neighbor**](cmdqueryname=display+lldp+mdn+neighbor) [ **interface** *interface-type interface-number* ] command to check information about MDN neighbors connected to all interfaces or a specified interface.
* Run the [**display lldp mdn neighbor brief**](cmdqueryname=display+lldp+mdn+neighbor+brief) command to check information about MDN neighbors of all interfaces or a specified interface.