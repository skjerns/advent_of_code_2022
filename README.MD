## Runtime statistics

I did not optimize my code for performance, but here are the numbers on my AMD Ryzen 9 3900X 12-Core Processor (of which of course only 1 is used due to the Python GIL) with 3.8 Ghz and 32 GB RAM. All runtimes exclude the initial reading from disk, but include all other operation like parsing, splitting and filtering the input.

| Day | Title                   | Runtime |
| --- | ----------------------- | ------- |
| 1   | Calorie Counting        | 50.6 μs |
| 2   | Rock Paper Scissors     | 2.8 ms  |
| 3   | Rucksack Reorganization | 1.5 ms  |
| 4   | Camp Cleanup            | 8.8 ms  |
| 5   | Supply Stacks           | 3.0 ms  |
| 6   | Tuning Trouble          | 6.0 ms  |