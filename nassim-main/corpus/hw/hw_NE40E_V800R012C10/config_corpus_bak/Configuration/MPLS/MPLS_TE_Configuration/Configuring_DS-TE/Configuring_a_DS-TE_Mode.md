Configuring a DS-TE Mode
========================

You can configure an MPLS TE tunnel to work a DS-TE mode, either IETF mode or non-IETF mode.

#### Context

Perform the following steps on each LSR in a DS-TE domain:

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If bandwidth constraints are configured for a tunnel, the IETF and non-IETF modes cannot be switched to each other.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
3. Run [**mpls te ds-te mode**](cmdqueryname=mpls+te+ds-te+mode) { **ietf** | **non-ietf** }
   
   
   
   A DS-TE mode is configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

The NE40E supports the switching between the IETF mode and non-IETF mode. [Table 1](#EN-US_TASK_0172368186__tab_dc_vrp_te-p2p_cfg_00030201) describes switching between DS-TE modes. The arrow symbol (â>) indicates "switched to."

**Table 1** Switching between DS-TE modes
| Item | Non-IETFâ>IETF | IETFâ>Non-IETF |
| --- | --- | --- |
| Changes in bandwidth constraint models | N/A | RDMâ>N/A  MAMâ>N/A |
| Bandwidth change | BC0 bandwidth values remain. | BC0 bandwidth values remain. |
| TE-class mapping table | If the TE-class mapping table is not configured, the default TE-Class mapping table is used. Otherwise, the configured one is used. NOTE:  For information about the default TE-class mapping table, see [Table 1](dc_vrp_te-p2p_cfg_0304.html#EN-US_TASK_0172368191__tab_dc_vrp_te-p2p_cfg_030401). | No TE-class mapping table is used.   * A TE-class mapping table is not deleted once it is configured. * If no TE-Class mapping table is configured, the default TE-Class mapping table is deleted. |