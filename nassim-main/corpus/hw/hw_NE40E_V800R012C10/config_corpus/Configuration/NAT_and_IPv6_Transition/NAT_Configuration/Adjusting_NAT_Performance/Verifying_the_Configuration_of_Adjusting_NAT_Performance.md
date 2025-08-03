Verifying the Configuration of Adjusting NAT Performance
========================================================

After configuring the NAT performance parameters, you can run display commands to verify the configuration.

#### Procedure

* Run the [**display nat session aging-time**](cmdqueryname=display+nat+session+aging-time) command to check the configured aging time for NAT session entries.
* Run the [**display nat session-table size**](cmdqueryname=display+nat+session-table+size) [ **slot** *slot-id* ] command to check the session resources allocated to service boards.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Only the NE40E-M2K and NE40E-M2K-B support this configuration.