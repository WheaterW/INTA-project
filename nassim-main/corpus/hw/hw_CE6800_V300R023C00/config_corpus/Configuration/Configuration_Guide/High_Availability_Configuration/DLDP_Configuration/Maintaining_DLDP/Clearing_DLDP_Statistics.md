Clearing DLDP Statistics
========================

Clearing DLDP Statistics

#### Context

Before collecting statistics about DLDPDUs within a specified period of time on an interface, you must clear existing statistics on the interface.

![](public_sys-resources/notice_3.0-en-us.png) 

DLDP statistics cannot be restored after they are cleared. Exercise caution when running reset commands.



#### Procedure

1. Run the [**reset dldp statistics**](cmdqueryname=reset+dldp+statistics) [ **interface** *interface-type* *interface-number* ] command in the user view to clear statistics about DLDPDUs on all interfaces or a specific one.
2. Run the [**reset fwm dldp statistics**](cmdqueryname=reset+fwm+dldp+statistics) [ **all** ] **slot** *slot-id* command to clear statistics about the DLDP module on a specified board.