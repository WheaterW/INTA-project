Configuring Flex-Algo Link Attributes
=====================================

Flex-Algo link attributes are used by the IGP to calculate Flex-Algo-based SR-MPLS BE tunnels (Flex-Algo LSPs). The IGP selects Flex-Algo links based on the corresponding FAD.

#### Context

Either of the following methods can be used to configure Flex-Algo link attributes:

1. Inherit interface TE attributes.
2. Configure Flex-Algo link attributes separately.

#### Procedure

1. Configure the mappings between affinity bit names and values for links.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**te attribute enable**](cmdqueryname=te+attribute+enable)
      
      
      
      TE is enabled.
   3. Run [**path-constraint affinity-mapping**](cmdqueryname=path-constraint+affinity-mapping)
      
      
      
      An affinity name template is configured, and the affinity mapping view is displayed.
      
      
      
      This template must be configured on each node that is involved in path computation, and the same mappings between affinity bit values and names must be configured on each node.
   4. Run [**attribute**](cmdqueryname=attribute) *bit-name* **bit-sequence** *bit-number* Mappings between affinity bit values and names are configured.
      
      
      
      This step configures only one bit of an affinity attribute, which has a total of 128 bits. Repeat this step as needed to configure some or all of the bits.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
2. Configure Flex-Algo link attributes.
   
   
   
   Use either of the following methods:
   
   
   
   * Inherit interface TE attributes.
     1. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
        
        The interface view is displayed.
     2. Run [**te link administrative group name**](cmdqueryname=te+link+administrative+group+name) *bit-name* &<1-32>
        
        The link administrative group attribute is configured. The *bit-name* value must be in the range specified in the affinity name template.
     3. Run [**te metric**](cmdqueryname=te+metric)*metric-value*
        
        The TE metric of the link is configured.
     4. Run [**te link-attribute-application flex-algo**](cmdqueryname=te+link-attribute-application+flex-algo)
        
        The Flex-Algo link attribute application view is created and displayed.
     5. Run [**te inherit**](cmdqueryname=te+inherit)
        
        The interface TE attributes are inherited.
        
        After the [**te inherit**](cmdqueryname=te+inherit) command is run, the Flex-Algo link inherits the [**te metric**](cmdqueryname=te+metric) and [**te link administrative group name**](cmdqueryname=te+link+administrative+group+name) command configurations on the interface.
        
        In the Flex-Algo link attribute application view, the [**te inherit**](cmdqueryname=te+inherit) command is mutually exclusive from the [**metric**](cmdqueryname=metric) and [**link administrative group name**](cmdqueryname=link+administrative+group+name) commands.
   * Configure Flex-Algo link attributes separately.
     1. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
        
        The interface view is displayed.
     2. Run [**te link-attribute-application flex-algo**](cmdqueryname=te+link-attribute-application+flex-algo)
        
        The Flex-Algo link attribute application view is created and displayed.
     3. Run [**link administrative group name**](cmdqueryname=link+administrative+group+name) *name-string* &<1-128>
        
        The link administrative group attribute of the Flex-Algo link is configured. The *name-string* value must be in the range specified in the affinity name template.
     4. (Optional) Run [**delay**](cmdqueryname=delay)*delay-value*
        
        The Flex-Algo link delay is configured.
     5. (Optional) Run [**metric**](cmdqueryname=metric)*metric-value*
        
        The Flex-Algo link metric is configured.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.