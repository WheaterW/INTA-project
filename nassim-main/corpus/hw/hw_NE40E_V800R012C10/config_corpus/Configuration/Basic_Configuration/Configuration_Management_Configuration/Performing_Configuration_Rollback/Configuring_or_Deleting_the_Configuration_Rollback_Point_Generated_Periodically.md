Configuring or Deleting the Configuration Rollback Point Generated Periodically
===============================================================================

This section describes how to set the time when configuration rollback points are periodically generated during proper system running, so that system configurations can be saved in configuration rollback point files.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**set save-configuration checkpoint daily**](cmdqueryname=set+save-configuration+checkpoint+daily) **time** *time*
   
   
   
   The time when configuration rollback points are periodically generated is set.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   The user view is displayed.
5. (Optional) Run [**clear configuration commit**](cmdqueryname=clear+configuration+commit) **label** *label-name*
   
   
   
   The configuration rollback point with a specified label is deleted.