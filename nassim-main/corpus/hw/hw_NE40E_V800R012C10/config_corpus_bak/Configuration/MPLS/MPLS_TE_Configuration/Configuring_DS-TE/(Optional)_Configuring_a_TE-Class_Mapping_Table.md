(Optional) Configuring a TE-Class Mapping Table
===============================================

Configuring the same TE-class mapping table on the whole DS-TE domain is recommended. Otherwise, LSPs may be incorrectly established.

#### Context

Skip this section if the non-IETF DS-TE mode is used.

In IETF DS-TE mode, plan a TE-class mapping table. Configuring the same TE-class mapping table on the whole DS-TE domain is recommended. Otherwise, LSPs may be incorrectly established.

Perform the following steps on each LSR in a DS-TE domain:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**te-class-mapping**](cmdqueryname=te-class-mapping)
   
   
   
   A TE-class mapping table is created, and the TE-class mapping view is displayed.
3. Perform one or more commands to configure TE-classes:
   
   
   * To configure TE-class 0, run [**te-class**](cmdqueryname=te-class)**0** **class-type** { **ct0** | **ct1** | **ct2** | **ct3** | **ct4** | **ct5** | **ct6** | **ct7** } **priority** *priority* [ **description** *description-info* ]
   * To configure TE-class 1, run [**te-class**](cmdqueryname=te-class) **1** **class-type** { **ct0** | **ct1** | **ct2** | **ct3** | **ct4** | **ct5** | **ct6** | **ct7** } **priority** *priority* [ **description** *description-info* ]
   * To configure TE-class 2, run [**te-class**](cmdqueryname=te-class) **2** **class-type** { **ct0** | **ct1** | **ct2** | **ct3** | **ct4** | **ct5** | **ct6** | **ct7** } **priority** *priority* [ **description** *description-info* ]
   * To configure TE-class 3, run [**te-class**](cmdqueryname=te-class) **3** **class-type** { **ct0** | **ct1** | **ct2** | **ct3** | **ct4** | **ct5** | **ct6** | **ct7** } **priority** *priority* [ **description** *description-info* ]
   * To configure TE-class 4, run [**te-class**](cmdqueryname=te-class) **4** **class-type** { **ct0** | **ct1** | **ct2** | **ct3** | **ct4** | **ct5** | **ct6** | **ct7** } **priority** *priority* [ **description** *description-info* ]
   * To configure TE-class 5, run [**te-class**](cmdqueryname=te-class) **5** **class-type** { **ct0** | **ct1** | **ct2** | **ct3** | **ct4** | **ct5** | **ct6** | **ct7** } **priority** *priority* [ **description** *description-info* ]
   * To configure TE-class 6, run [**te-class**](cmdqueryname=te-class) **6** **class-type** { **ct0** | **ct1** | **ct2** | **ct3** | **ct4** | **ct5** | **ct6** | **ct7** } **priority** *priority* [ **description** *description-info* ]
   * To configure TE-class 7, run [**te-class**](cmdqueryname=te-class) **7** **class-type** { **ct0** | **ct1** | **ct2** | **ct3** | **ct4** | **ct5** | **ct6** | **ct7** } **priority** *priority* [ **description** *description-info* ]
   
   Note the following information when you configure a TE-class mapping table:
   
   * The TE-class mapping table is unique on each device.
   * The TE-class mapping table takes effect globally. It takes effect on all DS-TE tunnels passing through the local LSR.
   * A TE-class refers to a combination of a CT and a *priority*, in the format of <CT, *priority*>. The priority is the priority of a CR-LSP in the TE-class mapping table, not the EXP value in the MPLS header. The priority value is an integer ranging from 0 to 7. The smaller the value, the higher the priority is.
     
     When you create a CR-LSP, you can set the setup and holding priorities for it (see [Configuring a Tunnel Interface](dc_vrp_te-p2p_cfg_0306.html)) and CT bandwidth values (see [Configuring an RSVP CR-LSP and Specifying Bandwidth Values](dc_vrp_te-p2p_cfg_0308.html)).
     
     A CR-LSP can be established only when both <CT, setup-priority> and <CT, holding-priority> exist in a TE-class mapping table. For example, the TE-class mapping table of a node contains only TE-Class [0] = <CT0, 6> and TE-Class [1] = <CT0, 7>, only can the following three types of CR-LSPs be successfully set up:
     + Class-Type = CT0, setup-priority = 6, holding-priority = 6
     + Class-Type = CT0, setup-priority = 7, holding-priority = 6
     + Class-Type = CT0, setup-priority = 7, holding-priority = 7![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The combination of setup-priority = 6 and hold-priority = 7 does not exist because the setup priority cannot be higher than the holding priority on a CR-LSP.
   * In a MAM model, a higher-class CT preempts bandwidth of the same CT, not bandwidth of different CTs.
   * In the RDM module, CT bandwidth preemption is limited by priorities of CR-LSPs and matching BCs. Assumed that priorities of CR-LSPs are set to m and n and CT values are set to i and j. If 0 <= m < n <= 7 and 0 <= i < j <= 7, the following situations occur:
     + CTi with priority m can preempt the bandwidth of CTi with priority n or of CTj with priority n.
     + Total CTi bandwidth <= BCi bandwidth
   
   In IETF DS-TE mode, if no TE-class mapping table is configured, a default TE-class mapping table is used. [Table 1](#EN-US_TASK_0172368191__tab_dc_vrp_te-p2p_cfg_030401) describes the default TE-class mapping table.
   
   **Table 1** Default TE-class mapping table
   | TE-Class | CT | Priority |
   | --- | --- | --- |
   | TE-Class[0] | 0 | 0 |
   | TE-Class[1] | 1 | 0 |
   | TE-Class[2] | 2 | 0 |
   | TE-Class[3] | 3 | 0 |
   | TE-Class[4] | 0 | 7 |
   | TE-Class[5] | 1 | 7 |
   | TE-Class[6] | 2 | 7 |
   | TE-Class[7] | 3 | 7 |
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) After the TE-class mapping is configured, to change TE-class descriptions, run the { **te-class0** | **te-class1** | **te-class2** | **te-class3** | **te-class4** | **te-class5** | **te-class6** | **te-class7** } **description** *description-info* command.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.