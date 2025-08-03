Configuration Precautions for AI ECN
====================================

Configuration Precautions for AI ECN

#### Licensing Requirements

AI ECN is under license control (CE-LIC-AFRD).


#### Hardware Requirements

**Table 1** Hardware requirements
| Series | Models |
| --- | --- |
| CE6800 series | CE6855-48XS8CQ/CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-LL-56F (standard forwarding mode)/CE6885-48YS8CQ-T/CE6885-LL-56F (low latency mode)/CE6885-SAN-56F |
| CE8800 series | CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8855-32CQ4BQ/CE8851-32CQ4BQ |



#### Feature Requirements

**Table 2** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| The AI Fabric feature package contains the AI ECN and iNOF features, which are included in the basic software package. By default, the basic software package contains the AI ECN and iNOF features. The AI Fabric feature package cannot be installed using the install feature-software command or uninstalled using the uninstall feature-software command. The AI Fabric feature package can be upgraded. To upgrade it, log in to the Huawei technical support website, search for the corresponding product and version in the software download zone, and download the AI Fabric feature package and corresponding documentation. For details about how to install and upgrade the feature package, see "Upgrade Maintenance Configuration" in Configuration Guide > System Management Configuration. | CE6800 series  CE8800 series | CE6855-48XS8CQ/CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-LL-56F (standard forwarding mode)/CE6885-48YS8CQ-T/CE6885-LL-56F (low latency mode)/CE6885-SAN-56F  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8855-32CQ4BQ/CE8851-32CQ4BQ |
| 1. On a PFC-enabled interface, if the static ECN function or WRED function has been enabled for the specified lossless queue where the AI ECN function is to be enabled, the AI ECN function cannot be enabled. If the AI ECN function has been enabled for a lossless queue, the static ECN function or WRED function cannot be enabled.  2. When the NPCC function is enabled on a queue with AI ECN enabled, the ECN thresholds are adjusted to fixed values. The lower threshold is 2.5 MB, the upper threshold is 3 MB, and the maximum marking probability is 10%.  3. After the AI ECN function is enabled, there is a low probability that ECN marking is performed when the packets have a large number of bytes.  4. Only two queues can load the distributed model and HPC model respectively. Other model combinations can be configured, but the performance cannot be guaranteed. | CE6800 series  CE8800 series | CE6855-48XS8CQ/CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-LL-56F (standard forwarding mode)/CE6885-48YS8CQ-T/CE6885-LL-56F (low latency mode)/CE6885-SAN-56F  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8855-32CQ4BQ/CE8851-32CQ4BQ |