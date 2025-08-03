Configuring Terminal Attributes for a VTY User Interface
========================================================

Terminal attributes of a VTY user interface include the timeout period of an idle connection, number of rows displayed on a terminal screen, and buffer size for historical commands.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**user-interface**](cmdqueryname=user-interface) **vty** *first-ui-number* [ *last-ui-number* ]
   
   
   
   One or more VTY user interface views are displayed.
3. Run [**shell**](cmdqueryname=shell)
   
   
   
   The VTY terminal service is started.
4. Run [**idle-timeout**](cmdqueryname=idle-timeout) *minutes* [ *seconds* ]
   
   
   
   A timeout period is set for an idle connection.
   
   If a connection remains idle within a specified timeout period, the system automatically ends the connection after the timeout period expires.
5. Run [**screen-length**](cmdqueryname=screen-length) *screen-length*
   
   
   
   The number of rows displayed on each terminal screen is set.
6. Run [**history-command max-size**](cmdqueryname=history-command+max-size) *size-value*
   
   
   
   A buffer size is set for historical commands.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.