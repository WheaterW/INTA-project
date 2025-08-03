Overview of SAID
================

Overview_of_SAID

#### Introduction

A network is prone to severe problems if it fails to recover from a service interruption. At present, device reliability is implemented through various detection functions. Once a device fault occurs, the device reports an alarm or requires a reset for fault recovery. However, this mechanism is intended for fault detection of a single module. When a service interruption occurs, the network may fail to promptly recover from the fault, adversely affecting services.

In addition, after receiving a reported fault, maintenance engineers may face a difficulty in collecting fault information, preventing problem locating and adversely affecting device maintenance.

The SAID is promoted to address the preceding issues. The SAID achieves automated device fault diagnosis, fault information collection, and service recovery, comprehensively improving the self-healing capability and maintainability of devices.


#### Basic Concepts

* **SAID node:** detects, diagnoses, and rectifies faults
  on a device's modules in the SAID. SAID nodes are classified
  into the following types:
  + Module-level SAID node: defends against, detects, diagnoses, and
    rectifies faults on a module.
  + SAID-level SAID node: detects, diagnoses, and rectifies faults
    on multiple modules.
* **SAID node state machine:** state triggered when a SAID
  node detects, diagnoses, and rectifies faults. A SAID node involves
  seven states: initial, detecting, diagnosing, invalid-diagnose, recovering,
  judging, and service exception states.
* **SAID tracing:** The SAID collects and stores information
  generated when a SAID node detects, diagnoses, and rectifies faults.
  The information can be used to locate the root cause of a fault.

#### SAID

Fault
locating in the SAID involves the fault detection, diagnosis, and
recovery phases. The SAID has multiple SAID nodes. Each time valid
diagnosis is triggered (that is, the recovery process has been triggered),
the SAID records the diagnosis process information for fault tracing.
The SAID's main processes are described as follows:

1. Defense startup phase: After the system runs, it instructs
   modules to deploy fault defense (for example, periodic logic re-loading
   and entry synchronization), starting the entire device's fault
   defense.
2. Detection phase: A SAID node detects faults and finds prerequisites
   for problem occurrence. Fault detection is classified as periodic
   detection (for example, periodic traffic decrease detection) or triggered
   detection (for example, IS-IS Down detection).
3. Diagnosis phase: Once a SAID node detects a fault, the SAID
   node diagnoses the fault and collects various fault entries to locate
   fault causes (only causes based on which recovery measures can be
   taken need to be located).
4. Recovery phase: After recording information, the SAID node
   starts to rectify the fault by level. After the recovery action is
   completed at each level, the SAID node determines whether services
   recover (by determining whether the fault symptom disappears). If
   the fault persists, the SAID node continues to perform the recovery
   action at the next level until the fault is rectified. The recovery
   action is gradually performed from a lightweight level to a heavyweight
   level.
5. Tracing phase: If the SAID determines the fault and its cause,
   this fault diagnosis is a valid diagnosis. The SAID then records the
   diagnosis process. After entering the recovery phase, the SAID records
   the recovery process for subsequent analysis.