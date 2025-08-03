(Optional) Configuring Frame LM
===============================

This section describes how to configure frame loss measurement (LM) for MPLS-TP services.

#### Context

Frame LM is a performance monitoring function provided by MPLS-TP OAM. Dual-ended frame LM is performed on the two MEPs of a service link. Measurement results include the following data:

* Near-end frame loss data: indicates the number and percentage of lost frames that are sent from an RMEP to a MEP.
* Far-end frame loss: indicates the number and percentage of dropped frames that are sent from a MEP to an RMEP.

The NE40E supports single-ended frame LM and dual-ended frame LM. The following table describes their differences.

**Table 1** Differences between single-ended frame LM and dual-ended frame LM
| Item | Single-ended Frame LM | Dual-ended Frame LM |
| --- | --- | --- |
| Statistics display | Statistics can be displayed using either of the following commands on a MEP:  * To display statistics about single-ended on-demand frame LM, run the [**lost-measure single-ended**](cmdqueryname=lost-measure+single-ended) command. * To display statistics about single-ended frame LM, run the [**display mpls-tp oam**](cmdqueryname=display+mpls-tp+oam) **meg** *meg-name* **statistic-type** **lost-measure** **single-ended** command. | Statistics about dual-ended frame LM can be displayed using the [**display mpls-tp oam**](cmdqueryname=display+mpls-tp+oam) **meg** *meg-name* **statistic-type** **lost-measure** **dual-ended** command on a MEP. |
| Monitoring scenario | On-demand monitoring  Proactive monitoring | Proactive monitoring |



The procedure for configuring single-ended or dual-ended frame LM is as follows:![](../../../../public_sys-resources/note_3.0-en-us.png) 

All the steps must be performed on both the MEP and RMEP unless otherwise specified.




#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls-tp meg**](cmdqueryname=mpls-tp+meg) *meg-name*
   
   
   
   A MEG is created, and the MEG view is displayed.
3. Choose one of the following sub-procedures as needed:
   
   
   * Configure single-ended frame LM.
     1. Run [**lost-measure single-ended receive enable**](cmdqueryname=lost-measure+single-ended+receive+enable)
        
        The RMEP is enabled to receive LMMs from the MEP.
     2. Perform either of the following steps:
        
        + Run [**lost-measure single-ended**](cmdqueryname=lost-measure+single-ended) [ **count** *count-value* | **exp** *exp-value* | **interval** *interval-value* ]\*
          
          Single-ended on-demand frame LM is enabled on the MEP.
        + Run [**lost-measure single-ended proactive**](cmdqueryname=lost-measure+single-ended+proactive) [ **interval** *interval-value* | **exp** *exp-value* ] \*
          
          Single-ended proactive frame LM is enabled on the MEP.
   * Configure dual-ended frame LM.
     1. (Optional) Run [**cc interval**](cmdqueryname=cc+interval) *interval-value*
        
        An interval at which CCMs are sent is configured.
        
        Typical CCM transmission intervals and their application scenarios are as follows:
        + 3.3 ms: 300 frames are sent per second. This interval is recommended for protection switching.
        + 100 ms: 10 frames are sent per second. This interval is recommended for performance monitoring.
        + 1000 ms: 1 frame is sent per second. This interval is recommended for fault management.
     2. (Optional) Run [**cc exp**](cmdqueryname=cc+exp) *exp-value*
        
        A priority is configured for CCMs in the MEG view.![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        If the MPLS-TP network is severely congested and the priority of CCMs is low, CCMs fail to be sent. Therefore, configure an appropriate priority for CCMs according to network conditions.
     3. On the MEP, run [**cc send enable**](cmdqueryname=cc+send+enable)
        
        The MEP is enabled to send CCMs.
     4. On the RMEP, run [**cc send enable**](cmdqueryname=cc+send+enable)
        
        The RMEP is enabled to send CCMs.
     5. On the MEP, run [**cc receive enable**](cmdqueryname=cc+receive+enable)
        
        The MEP is enabled to receive CCMs.
     6. On the RMEP, run [**cc receive enable**](cmdqueryname=cc+receive+enable)
        
        The RMEP is enabled to receive CCMs.
     7. Run [**lost-measure dual-ended enable**](cmdqueryname=lost-measure+dual-ended+enable)
        
        Dual-ended frame LM is enabled.