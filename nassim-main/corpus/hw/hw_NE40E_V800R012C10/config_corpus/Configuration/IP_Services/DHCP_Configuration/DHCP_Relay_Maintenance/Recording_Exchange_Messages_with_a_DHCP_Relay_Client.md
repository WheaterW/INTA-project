Recording Exchange Messages with a DHCP Relay Client
====================================================

A DHCP relay agent can record information exchanged between DHCP servers and clients based on a specific option or sub-option in DHCP messages to facilitate fault location.

#### Usage Scenario

If a DHCP client cannot obtain an IP address properly, a DHCP relay agent can be configured to record the information exchanged between DHCP servers and DHCP clients to help locate the fault. Then, the DHCP relay agent records the information exchanged between the DHCP client and server based on the specified option code and sub-option code in DHCP messages.


#### Procedure

1. (Optional) Run the [**reset dhcp relay client-info**](cmdqueryname=reset+dhcp+relay+client-info) [ **interface** *interface-type* *interface-number* [ **pevlan** *pevlan-id* [ *end-pevlan-id* ] [ **cevlan** *cevlan-id* [ *end-cevlan-id* ] ] ] | **mac-address** *mac-address* | **option** *option-value* ] command in the user view to clear the saved historical records about the interaction between a DHCP client and DHCP server through the DHCP relay agent.
   
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   * The historical records about interaction through the DHCP relay agent cannot be restored after being cleared. Exercise caution when running the [**reset dhcp relay client-info**](cmdqueryname=reset+dhcp+relay+client-info) command.
2. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
3. Run [**dhcp relay client-info**](cmdqueryname=dhcp+relay+client-info) **option** *option-code* [ **sub-option** *sub-option-code* ]
   
   
   
   The DHCP relay agent has been configured to specify the DHCP messages to recorded.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

* Run the [**display dhcp relay client-info option configuration**](cmdqueryname=display+dhcp+relay+client-info+option+configuration) command in any view to view the DHCP option code or sub-option code based on which the DHCP relay agent records DHCP messages.
* Run the [**display dhcp relay client-info**](cmdqueryname=display+dhcp+relay+client-info) [ **interface** { *interface-name* | *interface-type* *interface-number* } [ **pevlan** *pevlan-id* [ *end-pevlan-id* ] [ **cevlan** *cevlan-id* [ *end-cevlan-id* ] ] ] | **mac-address** *mac-address* | **option** *option-value* ] command in any view to view history records of the information exchanged between the DHCP client and server over the DHCP relay agent.