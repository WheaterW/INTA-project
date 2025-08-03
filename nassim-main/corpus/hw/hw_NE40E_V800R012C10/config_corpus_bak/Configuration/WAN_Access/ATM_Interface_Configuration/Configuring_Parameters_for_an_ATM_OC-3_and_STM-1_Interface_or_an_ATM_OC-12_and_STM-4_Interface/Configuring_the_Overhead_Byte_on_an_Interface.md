Configuring the Overhead Byte on an Interface
=============================================

You can configure different overhead bytes for interfaces to implement hierarchical monitoring functions.

#### Context

The Synchronous Optical Network/Synchronous Digital Hierarchy (SONET/SDH) provides various overhead bytes to implement hierarchical monitoring functions.

The signal label byte C2, a type of higher-order path overhead byte, is used to specify the multiplexing structure and attribute of the information payload in a VC frame.

The regenerator trace byte J0, a type of section overhead byte, is used to detect the continuity of connection between two interfaces on the section.

The path trace byte J1, a type of higher-order VC-N path trace byte, is used to detect whether the two interfaces are in the continuous connection status.

Perform the following steps on the Router:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface atm**](cmdqueryname=interface+atm) *interface-number*
   
   
   
   The ATM interface view is displayed.
3. Perform either of the following configurations as required:
   
   
   * Run [**flag j0**](cmdqueryname=flag+j0) { **16byte-mode** *16byte-value* | **peer** }
     
     The regenerator trace byte J0 is configured.
   * Run [**flag j1**](cmdqueryname=flag+j1) { **16byte--mode**  *j1-16trace* | **64byte-mode** *j1-64trace* | **peer** }
     
     The path trace byte J1 is configured.
   * Run [**flag c2**](cmdqueryname=flag+c2) *c2-value*
     
     The signal label byte C2 is configured.
   * Run [**flag space-padding disable**](cmdqueryname=flag+space-padding+disable)
     
     The function of automatically padding spaces at the end of the 16-byte j0 or the end of the 16-byte or 64-byte j1 configured on an ATM interface is disabled.
   
   The C2, J0, and J1 bytes on the receiving and sending ends must be consistent. Otherwise, an alarm is generated.
   
   For the ATM interface, the default value of C2 is 19 (13 in hexadecimal notation). The default value of J0 and J1 is **NetEngine**.