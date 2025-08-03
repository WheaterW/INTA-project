Verifying the Configuration of Basic LLDP Functions
===================================================

After configuring basic LLDP functions, verify the configuration.

#### Prerequisites

All configurations of basic LLDP functions are complete.


#### Procedure

* Run the [**display lldp local**](cmdqueryname=display+lldp+local) [ **interface** *interface-type interface-number* ] command to check local LLDP status information about all interfaces or a specified interface.
* Run the [**display lldp neighbor**](cmdqueryname=display+lldp+neighbor) [ **interface** *interface-type interface-number* ] command to check LLDP status information about neighbors connected to all interfaces or the neighbor connected to a specified interface.
  
  
  
  If the peer interface is a POS interface, its encapsulation protocol must be PPP or HDLC so that LLDP can discover it.
* Run the [**display lldp neighbor brief**](cmdqueryname=display+lldp+neighbor+brief) command to check the summary LLDP status information about a neighbor.
  
  
  
  If the peer interface is a POS interface, its encapsulation protocol must be PPP or HDLC so that LLDP can discover it.
* Run the [**display lldp tlv-config**](cmdqueryname=display+lldp+tlv-config) [ **interface** *interface-type interface-number* ] command to check information about optional TLVs that are allowed to be advertised by all interfaces or a specified interface.