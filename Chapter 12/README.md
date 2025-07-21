In Chapter 12, we learned about special techniques used to launch malware covertly.

“As computer systems and users have become more sophisticated, malware, too, has evolved.”
(p.m.a)

Malware authors don’t want their code to be easily discovered, so they rely on stealthy execution methods to hide and blend malicious payloads into legitimate processes.
While many of the techniques covered in the chapter are demonstrated on Windows, equivalent methods exist on Linux just implemented differently.

 * "DLL injection" can be achieved using LD_PRELOAD, allowing attackers to load a malicious shared object before any legitimate ones.

 * Code injection can be done via ptrace, which lets one process manipulate another's memory and execution flow.

 * Process hollowing, a common Windows trick, has a Linux counterpart through combinations of fork() and execve(), where a benign-looking process is replaced mid execution.

 * You can hook functions by patching PLT/GOT entries or even creating trampoline functions that redirect to your own malicious code.

 * Classic techniques like downloaders, loaders, or embedding payloads in resources or ELF sections still apply.

In short: the tactics are different, but the goal is the same evade detection and execute malicious code stealthily.
Linux gives attackers all the tools they need if they know where to look
