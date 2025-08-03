Configuring a BD Profile in Simplified Mode
===========================================

Configuring a BD Profile in Simplified Mode

#### Context

When configuring VXLAN, you need to bind VLANs and VNIs to BDs, and configure EVPN-related commands. If there are many BDs, the VXLAN configuration will be demanding and slow. To resolve this issue, configure a BD profile in simplified mode. In this profile, configure BDs to automatically bind VLANs and VNIs, and also to automatically generate EVPN RDs and RTs. Then, each BD needs to be bound only to this profile, simplifying configuration.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. (Optional) Enable EVPN to function as the VXLAN control plane.
   
   
   ```
   [evpn-overlay enable](cmdqueryname=evpn-overlay+enable)
   ```
   
   This step is required when BGP EVPN is used to establish VXLAN tunnels.
3. Create a BD profile and enter the BD profile view.
   
   
   ```
   [bridge-domain profile](cmdqueryname=bridge-domain+profile) profileId
   ```
4. (Optional) Configure a description for the BD profile.
   
   
   ```
   [description](cmdqueryname=description) profdescStr
   ```
   
   Perform this step if you need to add a description for the BD profile.
5. Configure automatic binding between BDs and VLANs in the BD profile. 
   
   
   ```
   [l2 binding vlan auto](cmdqueryname=l2+binding+vlan+auto)
   ```
   
   When the BD profile is bound to a BD, the BD is then automatically bound to a VLAN.
6. Configure automatic binding between BDs and VNIs in the BD profile.
   
   
   ```
   [vxlan vni auto](cmdqueryname=vxlan+vni+auto)
   ```
   
   When the BD profile is bound to a BD, the BD is then automatically bound to a VNI.
7. (Optional) Create an EVPN profile in VXLAN mode.
   
   
   ```
   [evpn](cmdqueryname=evpn)
   ```
   
   This step and subsequent steps are required when BGP EVPN is used to establish VXLAN tunnels.
8. (Optional) Automatic RD generation is configured for the EVPN profile.
   
   
   ```
   [route-distinguisher auto](cmdqueryname=route-distinguisher+auto)
   ```
9. (Optional) Automatic RT generation is configured for the EVPN profile.
   
   
   ```
   [vpn-target auto](cmdqueryname=vpn-target+auto)
   ```
10. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```

#### Verifying the Configuration

After the configuration is complete, run the [**display this**](cmdqueryname=display+this) command in the specified BD profile view to check the configuration details.