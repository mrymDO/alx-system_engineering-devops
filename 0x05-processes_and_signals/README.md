# 0x05. Processes and signals

* A PID (Process Identifier) is a unique numerical identifier assigned to each running process in a computer system. It serves as a reference to identify and manage individual processes.
* A process refers to an executing program instance, representing an independent unit of work with its own memory, resources, and execution context.
* To find a process's PID, you can use commands like ps or pgrep, which provide information about running processes along with their corresponding PIDs.
* Killing a process means terminating its execution. The kill command is commonly used to send signals to processes, where a signal is a software interrupt used to communicate with processes.
* While most signals can be caught or ignored by processes, two signals, SIGKILL (signal number 9) and SIGSTOP (signal number 19 or 17), cannot be ignored. SIGKILL is used to forcefully terminate a process, while SIGSTOP is used to pause or stop a process, and they ensure that a process can be controlled even if its signal handling is disabled.
