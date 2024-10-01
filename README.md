# CPU Performance Testing Suite

[中文版本](#cpu-性能测试套件)

This repository provides a **comprehensive CPU performance testing suite** to measure various aspects of a system's CPU capabilities, including single-core, multi-core, matrix multiplication, memory bandwidth, floating-point calculations, and more. It includes additional tests for integer calculations, thread switching, sorting algorithms, compression/decompression, and file I/O operations. This suite offers a detailed evaluation of your CPU's processing power across a variety of tasks.

## Features

- **Single-core performance test**: Evaluates single-threaded computational speed.
- **Multi-core performance test**: Utilizes all available cores to measure parallel processing performance.
- **Matrix multiplication test**: Measures the efficiency of large-scale matrix operations.
- **Memory bandwidth test**: Tests the speed of memory operations on large data arrays.
- **Floating-point calculations**: Assesses CPU performance in handling floating-point math.
- **Integer calculation performance**: Tests CPU efficiency with complex integer operations.
- **Thread switching performance**: Simulates thread switching between multiple threads.
- **Sorting algorithm performance**: Evaluates the speed of sorting large arrays.
- **Compression/Decompression performance**: Tests the CPU's ability to handle data compression and decompression.
- **File I/O performance**: Measures CPU efficiency in reading and writing large files.

---

# CPU 性能测试套件

此代码库提供了一个 **全面的 CPU 性能测试套件**，用于衡量系统的 CPU 性能，涵盖单核、多核、矩阵计算、内存带宽、浮点运算等多个方面。新增的测试项包括整数运算、线程切换、排序算法、压缩解压缩性能以及文件 I/O 操作。这些测试可以帮助全面评估 CPU 在各种任务中的处理能力。

## 功能

- **单核性能测试**：评估单线程计算速度。
- **多核性能测试**：利用所有可用核心，测试并行处理性能。
- **矩阵乘法测试**：测量大规模矩阵运算的效率。
- **内存带宽测试**：测试内存操作在处理大型数据数组时的速度。
- **浮点运算测试**：评估 CPU 处理浮点数学运算的性能。
- **整数计算性能测试**：测试 CPU 处理复杂整数运算的效率。
- **线程切换性能测试**：模拟多线程任务之间的切换，评估线程调度性能。
- **排序算法性能测试**：测试 CPU 处理大规模数据排序的速度。
- **压缩/解压缩性能测试**：测试 CPU 处理数据压缩和解压缩的能力。
- **文件 I/O 性能测试**：测量 CPU 进行文件读写时的效率。

## Installation / 安装

To get started, clone this repository and ensure you have Python installed (Python 3.x recommended). Required dependencies include `numpy` and `zlib`.

开始使用时，请克隆此代码库，并确保您已安装 Python（推荐 Python 3.x 版本）。需要的依赖项包括 `numpy` 和 `zlib`。

```bash
# Clone this repository
git clone https://github.com/yourusername/cpu-performance-testing-suite.git

# Navigate to the project directory
cd cpu-performance-testing-suite

# Install necessary dependencies
pip install numpy
```

## Usage / 使用方法

Simply run the script to execute all tests and evaluate your CPU's performance.

运行脚本以执行所有测试并评估 CPU 的性能。

```bash
python3 cpu_test_suite.py
```

Upon running the script, you will see the execution times and scores for each test printed to the console. The scores are normalized based on predefined baseline values, providing a comparative measure of your CPU's performance.

运行脚本后，您将看到每个测试的执行时间和得分输出到控制台。得分是根据预设的基准值标准化的，提供了您 CPU 性能的对比评估。

## Output / 输出结果

The script will output execution times and normalized scores for each test:

该脚本将输出每个测试的执行时间和标准化得分：

```
Single-core performance: 5.4321 seconds, Score: 92.14
Multi-core performance: 2.3456 seconds, Score: 106.73
Matrix computation performance: 8.7654 seconds, Score: 114.09
Memory bandwidth performance: 1.2345 seconds, Score: 243.12
...
```

## File Cleanup / 文件清理

During the file I/O performance test, a temporary file `test_file_io.tmp` will be created. After the test completes, this file will be automatically deleted to ensure no leftover files remain on your system.

在文件 I/O 性能测试期间，会创建一个临时文件 `test_file_io.tmp`。测试完成后，该文件会被自动删除，确保系统中没有遗留的临时文件。

## Contributions / 贡献

We welcome contributions! Feel free to submit issues, pull requests, or suggestions to improve the project.

我们欢迎任何形式的贡献！请随时提交问题、拉取请求或改进建议。

---

By using this repository, you'll be able to gain detailed insights into the performance characteristics of your CPU across a wide variety of tasks. The suite provides normalized scores based on baseline metrics to help compare performance against typical expectations.

通过使用本代码库，您将能够深入了解您的 CPU 在各种任务中的性能表现。此测试套件基于基准指标提供了标准化得分，帮助您与典型预期性能进行对比。
