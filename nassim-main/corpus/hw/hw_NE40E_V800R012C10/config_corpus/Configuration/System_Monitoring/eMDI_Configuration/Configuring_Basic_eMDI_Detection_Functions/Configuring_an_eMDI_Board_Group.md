Configuring an eMDI Board Group
===============================

After an eMDI channel group is configured, configure a board group for eMDI detection.

#### Context

As a distributed board detection solution, the eMDI detection solution requires the configuration of boards for eMDI detection. Create a board group and then bind the eMDI-capable boards to the board group so that eMDI detection can be performed on the boards.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**emdi**](cmdqueryname=emdi)
   
   
   
   The eMDI view is displayed.
3. Run [**emdi lpu-group**](cmdqueryname=emdi+lpu-group) *lpu-group-name*
   
   
   
   An eMDI board group is created or the view of an existing board group is displayed.
4. Run [**emdi bind slot**](cmdqueryname=emdi+bind+slot) **all**
   
   
   
   The specified boards are bound to the board group.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.