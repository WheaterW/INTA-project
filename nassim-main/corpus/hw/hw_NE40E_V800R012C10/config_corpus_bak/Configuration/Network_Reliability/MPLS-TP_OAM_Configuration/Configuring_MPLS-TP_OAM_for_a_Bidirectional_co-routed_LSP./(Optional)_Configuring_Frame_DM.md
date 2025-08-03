(Optional) Configuring Frame DM
===============================

This section describes how to configure one- and two-way frame delay measurement (DM) to collect reliability statistics for MPLS-TP services.

#### Context

Frame DM, a performance monitoring function provided by MPLS-TP, calculates the delay on links. The delay can be used to calculate the delay variation. The following DM modes are supported:

* One-way frame DM: In a point-to-point ME, a MEP sends DM frames to its RMEP to carry out one-way frame delay and variation measurement.![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If the clocks of the two MEPs are synchronized, one-way frame DM can be conducted; otherwise, only two-way frame delay variation can be measured.
* Two-way frame DM: In a point-to-point ME, a MEP sends delay measurement messages (DMMs) to its RMEP and receives delay measurement replies (DMRs) from the RMEP to carry out two-way frame delay and variation measurement.

One-way frame DM and two-way frame DM have the same monitoring scenario. The following table describes differences between them.

**Table 1** Differences between one-way frame DM and two-way frame DM
| Item | One-Way Frame DM | Two-Way Frame DM |
| --- | --- | --- |
| Statistics display | Statistics about one-way frame DM can be displayed using the [**display mpls-tp oam**](cmdqueryname=display+mpls-tp+oam) **meg** *meg-name* **statistic-type** **delay-measure** **one-way** command on an RMEP. | Statistics can be displayed using either of the following commands on a MEP:  * To display statistics about two-way on-demand frame DM, run the [**delay-measure two-way**](cmdqueryname=delay-measure+two-way) [ **interval** *interval-value* | **count** *count-value* | **exp** *exp-value* | **two-time-stamp** ]\* command. * To display statistics about two-way frame DM, run the [**display mpls-tp oam**](cmdqueryname=display+mpls-tp+oam) **meg** *meg-name* **statistic-type** **delay-measure** **two-way** command. |
| Monitoring scenario | On-demand monitoring  Proactive monitoring | On-demand monitoring  Proactive monitoring |



The procedure for configuring one-way or two-way frame DM is as follows:![](../../../../public_sys-resources/note_3.0-en-us.png) 

All the steps must be performed on both the MEP and RMEP unless otherwise specified.




#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls-tp meg**](cmdqueryname=mpls-tp+meg) *meg-name*
   
   
   
   A MEG is created, and the MEG view is displayed.
3. Choose one of the following sub-procedures as needed:
   
   
   * Configure one-way frame DM. Run any of the following commands:
     
     + Run [**delay-measure one-way**](cmdqueryname=delay-measure+one-way) [ **interval** *interval-value* | **count** *count-value* | **exp** *exp-value* ] \*
       
       One-way on-demand frame DM is enabled.
       
       Run either of the following commands to view statistics about one-way on-demand frame DM as needed:
       
       - If the [**delay-measure one-way**](cmdqueryname=delay-measure+one-way) command has been run on the MEP to measure the delay on the link from the MEP to the RMEP, run the [**display mpls-tp oam**](cmdqueryname=display+mpls-tp+oam) **meg** *meg-name* **statistic-type** **delay-measure** **one-way** command on the RMEP to view DM results.
       - If the [**delay-measure one-way**](cmdqueryname=delay-measure+one-way) command has been run on the RMEP to measure the delay on the link from the RMEP to the MEP, run the [**display mpls-tp oam**](cmdqueryname=display+mpls-tp+oam) **meg** *meg-name* **statistic-type** **delay-measure** **one-way** command on the MEP to view DM results.
     + On the MEP, run [**delay-measure one-way proactive**](cmdqueryname=delay-measure+one-way+proactive) [ **interval** *interval-value* | **exp** *exp-value* ] \*
       
       One-way proactive frame DM is enabled.
       
       On the RMEP, run [**delay-measure one-way proactive receive enable**](cmdqueryname=delay-measure+one-way+proactive+receive+enable)
       
       The receive function is enabled for one-way proactive frame DM.
       
       Run either of the following commands to view statistics about one-way proactive frame DM as needed:
       
       - If the [**delay-measure one-way proactive**](cmdqueryname=delay-measure+one-way+proactive) command has been run on the MEP, run the [**display mpls-tp oam**](cmdqueryname=display+mpls-tp+oam) **meg** *meg-name* **statistic-type** **delay-measure** **one-way** command on the RMEP to view statistics about one-way proactive frame DM in the direction from the MEP to its RMEP.
       - If the [**delay-measure one-way proactive**](cmdqueryname=delay-measure+one-way+proactive) command has been run on the RMEP, run the [**display mpls-tp oam**](cmdqueryname=display+mpls-tp+oam) **meg** *meg-name* **statistic-type** **delay-measure** **one-way** command on the MEP to view statistics about one-way proactive frame DM in the direction from the RMEP to its MEP.
   * Configure two-way frame DM. Configure either two-way on-demand or proactive frame DM as follows:
     
     + To enable two-way on-demand frame DM, run the [**delay-measure two-way**](cmdqueryname=delay-measure+two-way) [ **interval** {**1000**|**10000**} | **count** *count-value* | **exp** *exp-value* | **two-time-stamp** ] \* command.
     + To enable two-way proactive frame DM, run the [**delay-measure two-way proactive**](cmdqueryname=delay-measure+two-way+proactive) [ **interval** { **1000** | **10000** } | **exp** *exp-value* ] \* command.