## Runtime statistics

I did not optimize my code for performance, but here are the numbers on my AMD Ryzen 9 3900X 12-Core Processor (of which of course only 1 is used due to the Python GIL) with 3.8 Ghz and 32 GB RAM. All runtimes exclude the initial reading from disk and all debug print statements, but include all other operation like parsing, splitting and filtering the input.

| Day | Title                     | Runtime |
| --- | ------------------------- | ------- |
| 1   | Calorie Counting          | 71 μs   |
| 2   | Rock Paper Scissors       | 2.6 ms  |
| 3   | Rucksack Reorganization   | 1.4 ms  |
| 4   | Camp Cleanup              | 8.8 ms  |
| 5   | Supply Stacks             | 3.2 ms  |
| 6   | Tuning Trouble            | 6.0 ms  |
| 7   | No Space Left On Device   | 2.9 ms  |
| 8   | Treetop Tree House        | 675 ms  |
| 9   | Rope Bridge               | 478 ms  |
| 10  | Cathode-Ray Tube          | 52 μs   |
| 11  | Monkey in the Middle [^2] | 4.9 s   |
| 12  | Hill Climbing Algorithm   | 2.0 s   |
| 13  | Distress Signal           | 560 ms  |
| 14  | Regolith Reservoir        | 2.7 s   |
| 15  | Beacon Exclusion Zone     | 30 s    |

[^1]: I did not finish this one completely and needed to look up some hints for part 1

[^2]: I did not finish this one completely and needed to look up some hints for part 2. I was on the right track, and the hints confirmed it.

[^3]: I could not finish this puzzle