Configuring a Multicast Group Type for a VLAN
=============================================

Configuring a Multicast Group Type for a VLAN

#### Context

Two multicast models are available: Any-Source Multicast (ASM) model and Source-Specific Multicast (SSM) model. Messages do not carry multicast source information in the ASM model, but do in the SSM model. The two models are differentiated based on multicast group addresses. Configure a multicast group type if you want a device to learn MLD messages only in the ASM or SSM group address range in a VLAN.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the VLAN view.
   
   
   ```
   [vlan](cmdqueryname=vlan) vlan-id
   ```
3. Configure a multicast group type in the VLAN.
   
   
   ```
   [mld snooping](cmdqueryname=mld+snooping) { asm-only | ssm-only | asm-ssm }
   ```
   
   The default multicast group type of a VLAN is **asm-ssm**, indicating that both ASM and SSM models of multicast groups are supported.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```