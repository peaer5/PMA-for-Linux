## Chapter 16 - anti debugging
Chapter 16 focuses on anti-debugging - a set of techniques used by malware authors to make analysis more difficult. Naturally, attackers want to prevent you from understanding their code, since doing so could lead to detection, signature creation, or even complete prevention of the malware’s execution.

The book outlines several anti-debugging methods on Windows. Similar techniques exist on Linux as well, including:

 Checking the TracerPid field in /proc/self/status
 Using timing checks to detect delays caused by a debugger (as discussed in the book)
 Scanning for the 0xCC opcode, which is used by breakpoints (as mentioned in the book)
 Attaching a debugger to the process itself to block other debuggers from attaching
