Overview of MPLS DiffServ Modes
===============================

Overview of MPLS DiffServ Modes

#### CoS Processing in MPLS DiffServ

The DiffServ model allows transit nodes in a DiffServ domain to check and modify the IP Precedence, DSCP, or Exp value, which is called the class of service (CoS) value. Therefore, the CoS value may vary during transmission on an IP or MPLS network.

**Figure 1** CoS processing in MPLS DiffServ  
![](figure/en-us_image_0000001214822235.png)  

Carriers need to determine whether to trust the CoS information in an IP or MPLS packet that is entering an MPLS network or is leaving an MPLS network for an IP network. Related standards define three modes for processing the CoS: Uniform, Pipe, and Short Pipe.